import base64
import datetime as dt
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from content_policy import content_allowed, review_key, review_repositories, clean_batch
from daily_digest import render_readme
from finance_catalog import eligible

class ContentPolicyTests(unittest.TestCase):
    def test_sensitive_topics_excluded_and_normal_market_terms_allowed(self):
        for text in ['political election prediction', 'geopolitical propaganda', '政治宣传行情工具', 'political censorship dataset']:
            self.assertFalse(content_allowed({'description':text}))
        for text in ['China A-share futures trading', 'US stock market regime switching', 'Hong Kong financial data']:
            self.assertTrue(content_allowed({'description':text}))

    def test_resource_collections_and_overlong_descriptions_excluded(self):
        for repo in [
            {'full_name':'gege-circle/.github'},
            {'full_name':'owner/owner'},
            {'full_name':'x/awesome-quant'},
            {'full_name':'x/resources','description':'A curated list of trading tools'},
            {'full_name':'x/list','description':'量化项目资源合集'},
            {'full_name':'x/tool','description':'x'*401},
        ]:
            self.assertFalse(content_allowed(repo))
        self.assertTrue(content_allowed({'full_name':'x/backtest','description':'Python futures backtesting engine'}))

    def test_readme_review_cached_and_changed_revision_rechecked(self):
        client=Mock(); reviews={}
        client.get.return_value.json.return_value={'encoding':'base64','content':base64.b64encode(b'Financial data and political propaganda').decode()}
        repo={'full_name':'x/finance','pushed_at':'2026-11-10'}
        review_repositories(client,[repo],reviews)
        self.assertFalse(content_allowed(repo,reviews))
        review_repositories(client,[repo],reviews)
        self.assertEqual(client.get.call_count,1)
        client.get.return_value.json.return_value={'encoding':'base64','content':base64.b64encode(b'Financial data').decode()}
        review_repositories(client,[repo|{'pushed_at':'2026-11-11'}],reviews)
        self.assertTrue(content_allowed(repo,reviews))
        self.assertEqual(client.get.call_count,2)

    def test_large_readme_link_directory_excluded(self):
        client=Mock(); reviews={}
        text='Financial links\n'+('https://github.com/x/tool\n'*201)
        client.get.return_value.json.return_value={'encoding':'base64','content':base64.b64encode(text.encode()).decode()}
        repo={'full_name':'x/links','pushed_at':'2026-11-10'}
        review_repositories(client,[repo],reviews)
        self.assertFalse(content_allowed(repo,reviews))

    def test_unavailable_readme_held_and_linked_paper_excluded(self):
        client=Mock(); client.get.side_effect=TimeoutError()
        reviews={}; repo={'full_name':'x/y'}
        review_repositories(client,[repo],reviews)
        self.assertFalse(content_allowed(repo,reviews))
        result=clean_batch({'papers':[{'id':'1','code_url':'https://github.com/x/y'}], 'repositories':[repo]},reviews)
        self.assertEqual(result['papers'],[])
        self.assertEqual(result['repositories'],[])
        self.assertNotIn('x/y', str(reviews))

    def test_homepage_shows_popular_rows_and_strict_threshold(self):
        def repo(name,stars):
            return {'full_name':name,'url':'https://github.com/'+name,'stars':stars,'description':'financial agent','language':'Python','pushed_at':'2026-11-10'}
        rows=[repo('x/small',999),repo('x/boundary',1000),repo('x/large',5000),repo('x/politics',9000)]
        text=render_readme('2026-11-10',[],[],{},{},{},rows)
        self.assertIn('[x/boundary]',text)
        self.assertIn('[x/large]',text)
        self.assertNotIn('[x/small]',text)
        self.assertNotIn('[x/politics]',text)
        self.assertLess(text.index('[x/large]'),text.index('[x/boundary]'))
        self.assertIn('HOT_PROJECTS.md',text)
        self.assertTrue(eligible(rows[1],dt.date(2026,11,10)))
        self.assertFalse(eligible(rows[0],dt.date(2026,11,10)))

if __name__=='__main__': unittest.main()
