import datetime as dt
import sys
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import daily_digest as digest
import requests


class SourceFailureTests(unittest.TestCase):
    def test_arxiv_outage_still_publishes_catalog_and_preserves_history(self):
        config = digest.load_yaml(digest.ROOT / 'config.yaml')
        config['papers']['huggingface_trending'] = False
        with tempfile.TemporaryDirectory() as folder, ExitStack() as stack:
            root = Path(folder)
            for name, path in {'ROOT': root, 'STATE_PATH': root/'data/state.json', 'LATEST_PATH': root/'data/latest.json'}.items():
                stack.enter_context(patch.object(digest, name, path))
            stack.enter_context(patch.object(digest, 'load_yaml', return_value=config))
            stack.enter_context(patch.object(digest, 'review_repositories', return_value={}))
            stack.enter_context(patch.object(digest, 'fetch_papers', side_effect=requests.HTTPError('500')))
            stack.enter_context(patch.object(digest, 'fetch_repositories', return_value=[]))
            collect = stack.enter_context(patch.object(digest, 'collect_catalog', return_value=([], [])))
            today = (dt.datetime.now(dt.timezone.utc)+dt.timedelta(hours=8)).date().isoformat()
            paper = {'id': 'saved', 'title': 'Existing paper', 'published': today, 'paper_url': 'https://arxiv.org/abs/saved', 'authors': []}
            digest.save_json(root/'data/latest.json', {'run_date': today, 'papers': [paper], 'repositories': []})
            result = digest.run(root/'config.yaml')
            self.assertEqual(result['papers'][0]['id'], 'saved')
            self.assertIn('arXiv', result['collection_warnings'][0])
            self.assertIn('采集失败', (root/'README.md').read_text())
            self.assertTrue((root/'HOT_PROJECTS.md').exists())
            self.assertTrue((root/'archive'/f'{today[:7]}.md').exists())
            self.assertFalse(list((root/'archive').rglob('*.json')))
            collect.assert_called_once()

    def test_arxiv_outage_uses_huggingface_papers(self):
        config = digest.load_yaml(digest.ROOT / 'config.yaml')
        with tempfile.TemporaryDirectory() as folder, ExitStack() as stack:
            root = Path(folder)
            for name, path in {'ROOT': root, 'STATE_PATH': root/'data/state.json', 'LATEST_PATH': root/'data/latest.json'}.items():
                stack.enter_context(patch.object(digest, name, path))
            stack.enter_context(patch.object(digest, 'load_yaml', return_value=config))
            stack.enter_context(patch.object(digest, 'review_repositories', return_value={}))
            stack.enter_context(patch.object(digest, 'fetch_papers', side_effect=requests.ReadTimeout('timeout')))
            paper = {'id': '2412.20138', 'title': 'LLM stock trading', 'published': '2024-12-28',
                     'paper_url': 'https://arxiv.org/abs/2412.20138', 'abstract': 'AI trading', 'authors': [],
                     'code_url': 'https://github.com/x/trading', 'code_match': 'hugging-face',
                     'hf_url': 'https://huggingface.co/papers/2412.20138', 'hf_upvotes': 164}
            stack.enter_context(patch.object(digest, 'fetch_huggingface_papers', return_value=[paper]))
            stack.enter_context(patch.object(digest, 'fetch_repositories', return_value=[]))
            collect = stack.enter_context(patch.object(digest, 'collect_catalog', return_value=([], [])))
            result = digest.run(root/'config.yaml')
            self.assertEqual([p['id'] for p in result['papers']], ['2412.20138'])
            self.assertIn('HF Trending', (root/'README.md').read_text())
            self.assertIn('x/trading', collect.call_args.args[2])
            self.assertIn('ReadTimeout', result['collection_warnings'][0])

if __name__ == '__main__': unittest.main()
