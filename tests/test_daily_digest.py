import datetime as dt
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from daily_digest import qualifies_paper, repo_score, title_similarity


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


if __name__ == "__main__":
    unittest.main()
