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
        with tempfile.TemporaryDirectory() as folder, ExitStack() as stack:
            root = Path(folder)
            for name, path in {'ROOT': root, 'STATE_PATH': root/'data/state.json', 'LATEST_PATH': root/'data/latest.json'}.items():
                stack.enter_context(patch.object(digest, name, path))
            stack.enter_context(patch.object(digest, 'load_yaml', return_value=config))
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

if __name__ == '__main__': unittest.main()
