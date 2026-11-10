import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from finance_catalog import active_cutoff, category, collect_catalog, eligible, market_labels, publish_months, render_catalog
from daily_digest import load_json, save_json, render_digest, md_escape


class CatalogTests(unittest.TestCase):
    def test_strict_stars_and_three_year_activity(self):
        today = dt.date(2026, 11, 10)
        base = {'stars': 1001, 'pushed_at': '2023-11-10'}
        self.assertTrue(eligible(base, today))
        for changes in ({'stars': 999}, {'pushed_at': '2023-11-09'}, {'archived': True}, {'disabled': True}, {'pushed_at': ''}):
            self.assertFalse(eligible(base | changes, today))
        self.assertEqual(active_cutoff(dt.date(2024, 2, 29)), '2021-02-28')

    def test_multiple_market_labels_and_unknown(self):
        self.assertEqual(market_labels({'description': 'A-share US stocks crypto futures alpha factor'}), '美股、A股、虚拟货币、期货、因子')
        self.assertIn('未明确', market_labels({'description': 'portfolio optimization'}))
        self.assertEqual(category({'description': 'financial multi-agent'}), 'Agent')
        self.assertEqual(category({'description': 'Python backtesting framework'}), '交易框架')

    def test_paginated_search_and_refresh_of_previous_repo(self):
        class Client:
            github_headers = {}
            def __init__(self): self.calls = []
            def github_search_page(self, query, page):
                self.calls.append((query, page))
                return {'total_count': 101, 'items': [{'full_name': f'x/{page}', 'stars': 1000 + page, 'pushed_at': '2026-11-10'}]}
            def get(self, *args, **kwargs):
                class Response:
                    def json(self): return {'full_name': 'x/known', 'stars': 5000, 'pushed_at': '2020-01-01'}
                return Response()
        client = Client()
        repos, warnings = collect_catalog(client, {'catalog_queries': ['finance']}, {'x/known': {}}, dt.datetime(2026,11,10,tzinfo=dt.timezone.utc), lambda r,*args:r)
        self.assertEqual([r['full_name'] for r in repos], ['x/2', 'x/1'])
        self.assertEqual(len(client.calls), 2)
        self.assertNotIn('created:', client.calls[0][0])
        self.assertEqual(warnings, [])

    def test_monthly_migration_rerun_and_no_daily_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            repo = {'full_name': 'x/old', 'stars': 200, 'url': 'https://github.com/x/old'}
            old = {'run_date': '2026-10-01', 'papers': [], 'repositories': [repo], 'topic_repositories': {'ai_infra': [{'full_name': 'x/excluded'}]}}
            save_json(root/'archive/2026/10/2026-10-01.json', old)
            incoming = {'run_date': '2026-10-02', 'papers': [], 'repositories': [repo | {'stars': 300}]}
            publish_months(root, incoming, load_json, save_json, render_digest)
            publish_months(root, incoming, load_json, save_json, render_digest)
            self.assertEqual(sorted(p.name for p in (root/'archive').rglob('*.md')), ['2026-10.md', 'index.md'])
            self.assertFalse(list((root/'archive').rglob('*.json')))
            text = (root/'archive/2026-10.md').read_text()
            self.assertEqual(text.count('[x/old]'), 1)
            self.assertIn('300', text)
            self.assertNotIn('x/excluded', text)

    def test_catalog_ranking_and_home_link(self):
        repos = [{'full_name': 'x/small', 'url': 'https://github.com/x/small', 'stars': 1000, 'pushed_at': '2026-11-10'}, {'full_name': 'x/big', 'url': 'https://github.com/x/big', 'stars': 5000, 'pushed_at': '2026-11-10'}]
        text = render_catalog(repos, '2026-11-10', md_escape)
        self.assertLess(text.index('[x/big]'), text.index('[x/small]'))
        self.assertIn('未明确', text)
        for group in ('Agent', '交易框架', '工具', '游戏', '论文研究'):
            self.assertIn('## '+group, text)

if __name__ == '__main__': unittest.main()
