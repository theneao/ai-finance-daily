import sys
import unittest
from pathlib import Path
from unittest.mock import Mock
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from daily_digest import fetch_huggingface_papers, load_yaml, merge_paper_sources

CONFIG = load_yaml(Path(__file__).resolve().parents[1] / 'config.yaml')['papers']

class HuggingFaceTests(unittest.TestCase):
    def test_filters_finance_keeps_old_trending_and_normalizes_id(self):
        client = Mock()
        client.get.return_value.json.return_value = [
            {'paper': {'id': '2412.20138v2', 'title': 'LLM multi-agent stock trading', 'summary': 'Multi-agent portfolio optimization', 'publishedAt': '2024-12-28T12:00:00Z', 'authors': [{'name': 'Author'}], 'upvotes': 164, 'githubRepo': 'https://github.com/owner/trading'}},
            {'paper': {'id': '2601.12345', 'title': 'LLM serving and KV cache', 'summary': 'Inference infrastructure', 'publishedAt': '2026-01-01'}},
            {'paper': {'id': '2602.12345', 'title': 'Coding agent for developer productivity', 'summary': 'Large language model programming', 'publishedAt': '2026-02-01'}},
            {'paper': {'id': 'bad', 'title': 'LLM stock trading', 'publishedAt': '2026-02-01'}},
        ]
        papers = fetch_huggingface_papers(client, CONFIG)
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0]['id'], '2412.20138')
        self.assertEqual(papers[0]['published'], '2024-12-28')
        self.assertEqual(papers[0]['hf_upvotes'], 164)
        self.assertEqual(papers[0]['code_match'], 'hugging-face')
        self.assertEqual(client.get.call_args.kwargs['params']['sort'], 'trending')

    def test_merges_duplicate_ids_preserving_arxiv_abstract(self):
        arxiv = {'id': '2412.20138', 'title': 'Original', 'abstract': 'Full arxiv abstract', 'published': '2024-12-28', 'code_url': None}
        hf = arxiv | {'abstract': 'HF version', 'hf_url': 'https://huggingface.co/papers/2412.20138', 'hf_upvotes': 164, 'code_url': 'https://github.com/x/y', 'code_match': 'hugging-face'}
        merged = merge_paper_sources([arxiv], [hf, hf])
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]['abstract'], arxiv['abstract'])
        self.assertEqual(merged[0]['hf_upvotes'], 164)
        self.assertEqual(merged[0]['code_url'], hf['code_url'])

    def test_bad_api_shape_raises_for_source_warning(self):
        client = Mock()
        client.get.return_value.json.return_value = {'error': 'temporary failure'}
        with self.assertRaises(ValueError): fetch_huggingface_papers(client, CONFIG)

if __name__ == '__main__': unittest.main()
