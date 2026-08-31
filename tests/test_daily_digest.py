import datetime as dt
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from daily_digest import (
    apply_star_thresholds,
    compact_history,
    merge_daily_results,
    qualifies_paper,
    repo_score,
    title_similarity,
)


PAPER_CONFIG = {
    "ai_terms": ["machine learning", "reinforcement learning", "large language model"],
    "investment_terms": ["portfolio optimization", "stock trading", "stock market"],
    "exclude_terms": ["fraud detection", "credit scoring"],
}


class DailyDigestTests(unittest.TestCase):
    def test_accepts_ai_investing_research(self):
        self.assertTrue(
            qualifies_paper(
                "Reinforcement Learning for Portfolio Optimization",
                "An agent allocates capital in the stock market.",
                PAPER_CONFIG,
            )
        )

    def test_rejects_finance_without_ai(self):
        self.assertFalse(
            qualifies_paper(
                "A Convex Method for Portfolio Optimization",
                "We derive a classical estimator for the stock market.",
                PAPER_CONFIG,
            )
        )

    def test_rejects_ai_fraud_paper(self):
        self.assertFalse(
            qualifies_paper(
                "Machine Learning for Banking Operations",
                "We study fraud detection and credit scoring. Portfolio optimization is only future work.",
                PAPER_CONFIG,
            )
        )

    def test_rejects_generic_financial_compliance(self):
        self.assertFalse(
            qualifies_paper(
                "Evaluating LLM Rule Grounding in Financial Compliance",
                "A large language model agent follows regulations in financial markets.",
                PAPER_CONFIG,
            )
        )

    def test_title_similarity_prefers_related_repo(self):
        repo = {"name": "rl-portfolio-optimization", "description": "reinforcement learning for portfolios"}
        self.assertGreaterEqual(
            title_similarity("Reinforcement Learning for Portfolio Optimization", repo), 0.5
        )

    def test_repo_score_rewards_stars_and_freshness(self):
        now = dt.datetime(2026, 8, 31, tzinfo=dt.timezone.utc)
        fresh = {"stargazers_count": 100, "pushed_at": "2026-08-31T00:00:00Z"}
        stale = {"stargazers_count": 5, "pushed_at": "2025-01-01T00:00:00Z"}
        self.assertGreater(repo_score(fresh, now), repo_score(stale, now))

    def test_star_threshold_accepts_popular_or_fast_growing(self):
        project = {"min_popular_stars": 100, "weekly_star_growth": 20, "star_growth_days": 7}
        repos = [
            {"full_name": "x/popular", "stars": 100, "created_at": "2020-01-01"},
            {"full_name": "x/growing", "stars": 35, "created_at": "2020-01-01"},
            {"full_name": "x/new", "stars": 20, "created_at": "2026-08-28"},
            {"full_name": "x/quiet", "stars": 30, "created_at": "2020-01-01"},
        ]
        history = {
            "x/growing": {"2026-08-24": 10},
            "x/quiet": {"2026-08-24": 25},
        }
        selected = apply_star_thresholds(repos, history, "2026-08-31", project)
        self.assertEqual(
            {repo["full_name"] for repo in selected}, {"x/popular", "x/growing", "x/new"}
        )
        growing = next(repo for repo in selected if repo["full_name"] == "x/growing")
        self.assertEqual(growing["star_growth_7d"], 25)

    def test_daily_reruns_merge_without_overwriting(self):
        existing = {
            "run_date": "2026-08-31",
            "papers": [{"id": "1", "published": "2026-08-30"}],
            "repositories": [{"full_name": "x/old", "stars": 100}],
            "topic_papers": {"ai_infra": []},
            "topic_repositories": {},
        }
        incoming = {
            "run_date": "2026-08-31",
            "papers": [{"id": "2", "published": "2026-08-31"}],
            "repositories": [{"full_name": "x/new", "stars": 200}],
            "topic_papers": {},
            "topic_repositories": {},
        }
        merged = merge_daily_results(existing, incoming)
        self.assertEqual([paper["id"] for paper in merged["papers"]], ["2", "1"])
        self.assertEqual(
            [repo["full_name"] for repo in merged["repositories"]], ["x/new", "x/old"]
        )

    def test_cold_history_drops_low_star_repositories(self):
        result = {
            "papers": [
                {
                    "id": "1",
                    "title": "Useful paper",
                    "published": "2026-01-01",
                    "paper_url": "https://arxiv.org/abs/1",
                    "code_url": None,
                }
            ],
            "repositories": [
                {
                    "full_name": "x/keep",
                    "url": "https://github.com/x/keep",
                    "stars": 600,
                    "star_growth_7d": None,
                    "language": "Python",
                },
                {
                    "full_name": "x/drop",
                    "url": "https://github.com/x/drop",
                    "stars": 120,
                    "star_growth_7d": 2,
                    "language": "Python",
                },
                {
                    "full_name": "x/growing",
                    "url": "https://github.com/x/growing",
                    "stars": 80,
                    "star_growth_7d": 25,
                    "language": "Go",
                },
            ],
        }
        compact = compact_history(result, min_stars=500, growth_min=20)
        self.assertEqual(
            set(compact["repositories"]), {"finance:x/keep", "finance:x/growing"}
        )
        self.assertIn("finance:1", compact["papers"])


if __name__ == "__main__":
    unittest.main()
