#!/usr/bin/env python3
"""Collect AI-for-investing papers and useful finance GitHub projects."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import math
import os
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

import requests
import yaml

from content_policy import clean_batch, content_allowed, review_key, review_repositories

from finance_catalog import (category, collect_catalog, eligible, grew_by_30_percent,
                             market_labels, months_ago, publish_months, render_catalog,
                             star_baseline, tool_kind)


ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "data" / "state.json"
LATEST_PATH = ROOT / "data" / "latest.json"
ARCHIVE_DIR = ROOT / "archive"
HISTORY_DIR = ROOT / "history"
ARXIV_API = "https://export.arxiv.org/api/query"
GITHUB_API = "https://api.github.com"
ATOM = {"a": "http://www.w3.org/2005/Atom"}
GITHUB_URL_RE = re.compile(r"https?://github\.com/[\w.-]+/[\w.-]+", re.I)
WORD_RE = re.compile(r"[a-z0-9]+")


class Client:
    def __init__(self, token: str | None = None) -> None:
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "ai-finance-daily/1.0"})
        self.github_headers: dict[str, str] = {"X-GitHub-Api-Version": "2022-11-28"}
        if token:
            self.github_headers["Authorization"] = f"Bearer {token}"
        self._last_github_search = 0.0
        self._last_arxiv_request = 0.0

    def get(self, url: str, **kwargs: Any) -> requests.Response:
        for attempt in range(4):
            try:
                response = self.session.get(url, timeout=35, **kwargs)
                if response.status_code == 403 and "rate limit" in response.text.lower():
                    reset = int(response.headers.get("X-RateLimit-Reset", "0"))
                    wait = max(3, min(90, reset - int(time.time()) + 1))
                    time.sleep(wait)
                    continue
                response.raise_for_status()
                return response
            except requests.RequestException:
                if attempt == 3:
                    raise
                time.sleep(2**attempt)
        raise RuntimeError("unreachable")

    def github_search(self, query: str, per_page: int = 10) -> list[dict[str, Any]]:
        # Authenticated GitHub search allows 30 requests/minute. Stay below it.
        wait = 2.1 - (time.monotonic() - self._last_github_search)
        if wait > 0:
            time.sleep(wait)
        response = self.get(
            f"{GITHUB_API}/search/repositories",
            params={"q": query, "sort": "stars", "order": "desc", "per_page": per_page},
            headers=self.github_headers,
        )
        self._last_github_search = time.monotonic()
        return response.json().get("items", [])

    def github_search_page(self, query: str, page: int = 1) -> dict[str, Any]:
        wait = 2.1 - (time.monotonic() - self._last_github_search)
        if wait > 0:
            time.sleep(wait)
        response = self.get(
            f"{GITHUB_API}/search/repositories",
            params={"q": query, "sort": "stars", "order": "desc", "per_page": 100, "page": page},
            headers=self.github_headers,
        )
        self._last_github_search = time.monotonic()
        return response.json()

    def arxiv_get(self, **params: Any) -> requests.Response:
        wait = 3.1 - (time.monotonic() - self._last_arxiv_request)
        if wait > 0:
            time.sleep(wait)
        response = self.get(ARXIV_API, params=params)
        self._last_arxiv_request = time.monotonic()
        return response

    def quick_get(self, url: str, **kwargs: Any) -> requests.Response | None:
        """Best-effort optional source lookup without retrying a slow/down service."""
        try:
            response = self.session.get(url, timeout=5, **kwargs)
            if response.ok:
                return response
        except requests.RequestException:
            pass
        return None


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def save_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def normalize(text: str) -> str:
    return " ".join(html.unescape(text).lower().split())


def contains_term(text: str, terms: list[str]) -> bool:
    lowered = normalize(text)
    return any(term.lower() in lowered for term in terms)


def qualifies_paper(title: str, abstract: str, config: dict[str, Any]) -> bool:
    if not content_allowed({"title": title, "abstract": abstract}):
        return False
    text = f"{title} {abstract}"
    title_lower = normalize(title)
    has_ai = contains_term(text, config["ai_terms"])
    # Generic market context alone is not an investment method. Require a direct
    # investing term, or a market context plus an actionable research objective.
    generic_context = {"stock market", "financial market"}
    direct_terms = [term for term in config["investment_terms"] if term not in generic_context]
    action_terms = [
        "predict",
        "forecast",
        "trade",
        "trading",
        "portfolio",
        "invest",
        "allocation",
        "return",
        "price",
        "signal",
        "timing",
        "strategy",
    ]
    has_investment = contains_term(text, direct_terms) or (
        contains_term(text, list(generic_context)) and contains_term(text, action_terms)
    )
    excluded = contains_term(text, config.get("exclude_terms", []))
    # An exclusion in the abstract is allowed only when the title is explicitly about investing.
    return has_ai and has_investment and (not excluded or contains_term(title_lower, config["investment_terms"]))


def arxiv_query(config: dict[str, Any]) -> str:
    def group(terms: list[str]) -> str:
        return " OR ".join(f'all:"{term}"' for term in terms)

    return f"({group(config['ai_terms'])}) AND ({group(config['investment_terms'])})"


def parse_arxiv_date(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def fetch_papers(client: Client, config: dict[str, Any], cutoff: dt.datetime) -> list[dict[str, Any]]:
    response = client.arxiv_get(
        search_query=arxiv_query(config),
        start=0,
        max_results=config["max_arxiv_results"],
        sortBy="submittedDate",
        sortOrder="descending",
    )
    root = ET.fromstring(response.content)
    papers: list[dict[str, Any]] = []
    for entry in root.findall("a:entry", ATOM):
        title = " ".join((entry.findtext("a:title", "", ATOM)).split())
        abstract = " ".join((entry.findtext("a:summary", "", ATOM)).split())
        published = parse_arxiv_date(entry.findtext("a:published", "", ATOM))
        if published < cutoff or not qualifies_paper(title, abstract, config):
            continue
        abs_url = entry.findtext("a:id", "", ATOM).replace("http://", "https://")
        arxiv_id = abs_url.rsplit("/", 1)[-1].split("v", 1)[0]
        authors = [node.findtext("a:name", "", ATOM) for node in entry.findall("a:author", ATOM)]
        categories = [node.attrib.get("term", "") for node in entry.findall("a:category", ATOM)]
        comment = entry.findtext("a:comment", "", ATOM)
        papers.append(
            {
                "id": arxiv_id,
                "title": title,
                "abstract": abstract,
                "authors": authors,
                "published": published.date().isoformat(),
                "updated": parse_arxiv_date(entry.findtext("a:updated", "", ATOM)).date().isoformat(),
                "categories": categories,
                "paper_url": f"https://arxiv.org/abs/{arxiv_id}",
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                "comment": comment,
                "code_url": None,
                "code_match": None,
            }
        )
    return papers


def fetch_huggingface_papers(client: Client, config: dict[str, Any], limit: int = 100) -> list[dict[str, Any]]:
    """Trending can resurface old papers; relevance and seen IDs govern admission."""
    response = client.get("https://huggingface.co/api/daily_papers", params={"sort": "trending", "limit": limit})
    payload = response.json()
    if not isinstance(payload, list):
        raise ValueError("Hugging Face Trending returned a non-list response")
    found = {}
    for entry in payload:
        paper = entry.get("paper") or {}
        identifier = re.sub(r"v\d+$", "", str(paper.get("id", "")))
        title = paper.get("title") or entry.get("title") or ""
        abstract = paper.get("summary") or entry.get("summary") or ""
        published = str(paper.get("publishedAt") or entry.get("publishedAt") or "")[:10]
        if not re.fullmatch(r"\d{4}\.\d{4,5}", identifier) or not published:
            continue
        if not qualifies_paper(title, abstract, config):
            continue
        code = github_link(str(paper.get("githubRepo") or ""))
        found[identifier] = {
            "id": identifier, "title": title, "abstract": abstract,
            "authors": [a["name"] for a in paper.get("authors", []) if a.get("name")],
            "published": published, "updated": published, "categories": [],
            "paper_url": f"https://arxiv.org/abs/{identifier}",
            "pdf_url": f"https://arxiv.org/pdf/{identifier}", "comment": "",
            "code_url": code, "code_match": "hugging-face" if code else None,
            "source": "hugging-face-trending", "hf_upvotes": paper.get("upvotes", 0),
            "hf_url": f"https://huggingface.co/papers/{identifier}",
        }
    return list(found.values())


def merge_paper_sources(arxiv_papers, hf_papers):
    found = {p["id"]: dict(p) for p in arxiv_papers}
    for paper in hf_papers:
        if paper["id"] not in found:
            found[paper["id"]] = dict(paper)
        else:
            current = found[paper["id"]]
            for key in ("hf_upvotes", "hf_url"):
                current[key] = paper[key]
            if paper.get("code_url") and not current.get("code_url"):
                current["code_url"], current["code_match"] = paper["code_url"], paper["code_match"]
    return sorted(found.values(), key=lambda p: p.get("published", ""), reverse=True)


def fetch_topic_papers(
    client: Client, config: dict[str, Any], cutoff: dt.datetime, max_results: int = 120
) -> list[dict[str, Any]]:
    terms = config["paper_terms"]
    query = " OR ".join(f'all:"{term}"' for term in terms)
    response = client.arxiv_get(
        search_query=f"({query})",
        start=0,
        max_results=max_results,
        sortBy="submittedDate",
        sortOrder="descending",
    )
    root = ET.fromstring(response.content)
    papers: list[dict[str, Any]] = []
    for entry in root.findall("a:entry", ATOM):
        title = " ".join(entry.findtext("a:title", "", ATOM).split())
        abstract = " ".join(entry.findtext("a:summary", "", ATOM).split())
        published = parse_arxiv_date(entry.findtext("a:published", "", ATOM))
        text = f"{title} {abstract}"
        if published < cutoff or not contains_term(text, terms):
            continue
        if not contains_term(text, config["application_terms"]):
            continue
        title_hit = contains_term(title, terms)
        contextual_title_hit = contains_term(title, config.get("title_terms", []))
        if not title_hit and not contextual_title_hit:
            continue
        if contains_term(text, config.get("exclude_terms", [])):
            continue
        abs_url = entry.findtext("a:id", "", ATOM).replace("http://", "https://")
        arxiv_id = abs_url.rsplit("/", 1)[-1].split("v", 1)[0]
        papers.append(
            {
                "id": arxiv_id,
                "title": title,
                "abstract": abstract,
                "authors": [
                    node.findtext("a:name", "", ATOM) for node in entry.findall("a:author", ATOM)
                ],
                "published": published.date().isoformat(),
                "updated": parse_arxiv_date(
                    entry.findtext("a:updated", "", ATOM)
                ).date().isoformat(),
                "categories": [
                    node.attrib.get("term", "") for node in entry.findall("a:category", ATOM)
                ],
                "paper_url": f"https://arxiv.org/abs/{arxiv_id}",
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                "comment": entry.findtext("a:comment", "", ATOM),
                "code_url": None,
                "code_match": None,
            }
        )
    return papers


def title_tokens(value: str) -> set[str]:
    stop = {"a", "an", "and", "for", "from", "in", "of", "on", "the", "to", "with", "using"}
    return {token for token in WORD_RE.findall(value.lower()) if len(token) > 2 and token not in stop}


def title_similarity(title: str, repo: dict[str, Any]) -> float:
    expected = title_tokens(title)
    actual = title_tokens(f"{repo.get('name', '')} {repo.get('description') or ''}")
    return len(expected & actual) / max(1, len(expected))


def github_link(text: str) -> str | None:
    match = GITHUB_URL_RE.search(text)
    return match.group(0).rstrip(".,);]'\"") if match else None


def find_papers_with_code(client: Client, paper: dict[str, Any]) -> str | None:
    paper_id = paper["id"]
    legacy = client.quick_get(f"https://arxiv.paperswithcode.com/api/v0/papers/{paper_id}")
    if legacy:
        try:
            payload = legacy.json()
            official = payload.get("official") or {}
            if official.get("url"):
                return official["url"]
        except (ValueError, AttributeError):
            pass

    api = client.quick_get(f"https://paperswithcode.com/api/v1/papers/{paper_id}/repositories/")
    if api:
        try:
            rows = api.json().get("results", [])
            rows.sort(key=lambda row: (bool(row.get("is_official")), row.get("stars", 0)), reverse=True)
            if rows:
                return rows[0].get("url")
        except (ValueError, AttributeError):
            pass
    return None


def find_research_code(client: Client, paper: dict[str, Any]) -> str | None:
    # ResearchCode does not publish a stable public API. Use its public search
    # page best-effort and fall through immediately when the service is unavailable.
    url = f"https://researchcode.com/search?q={quote_plus(paper['id'])}"
    response = client.quick_get(url)
    return github_link(response.text) if response else None


def find_arxiv_page_code(client: Client, paper: dict[str, Any]) -> str | None:
    # Inspired by zhuwenxing/arxiv-papers-with-code: inspect the paper page in
    # addition to Atom abstract/comment metadata for author-posted code links.
    response = client.quick_get(paper["paper_url"])
    return github_link(response.text) if response else None


def find_code(
    client: Client, paper: dict[str, Any], sources: dict[str, bool] | None = None
) -> tuple[str | None, str | None]:
    sources = sources or {
        "papers_with_code": True,
        "research_code": True,
        "arxiv_page": True,
        "github_search": True,
    }
    embedded = GITHUB_URL_RE.search(f"{paper['abstract']} {paper.get('comment') or ''}")
    if embedded:
        return embedded.group(0).rstrip(".,);]"), "paper-link"

    if sources.get("papers_with_code"):
        url = find_papers_with_code(client, paper)
        if url:
            return url, "papers-with-code"

    if sources.get("research_code"):
        url = find_research_code(client, paper)
        if url:
            return url, "research-code"

    if sources.get("arxiv_page"):
        url = find_arxiv_page_code(client, paper)
        if url:
            return url, "arxiv-page"

    if not sources.get("github_search"):
        return None, None

    by_id = client.github_search(f'"{paper["id"]}" in:readme', per_page=5)
    # An ID alone often finds paper lists and daily aggregators. Also require the
    # repository name/description to overlap with the paper title.
    id_candidates = [(title_similarity(paper["title"], repo), repo) for repo in by_id]
    if id_candidates:
        score, repo = max(id_candidates, key=lambda item: item[0])
        if score >= 0.35:
            return repo["html_url"], "arxiv-id"

    significant = sorted(title_tokens(paper["title"]), key=len, reverse=True)[:8]
    if not significant:
        return None, None
    by_title = client.github_search(f'{" ".join(significant)} in:name,description,readme', per_page=5)
    candidates = [(title_similarity(paper["title"], repo), repo) for repo in by_title]
    if candidates:
        score, repo = max(candidates, key=lambda item: item[0])
        if score >= 0.42:
            return repo["html_url"], "title-match"
    return None, None


def repo_score(repo: dict[str, Any], now: dt.datetime) -> float:
    pushed = parse_arxiv_date(repo["pushed_at"])
    age = max(0, (now - pushed).days)
    freshness = max(0.0, 30.0 - age) / 6.0
    return round(math.log10(repo.get("stargazers_count", 0) + 1) * 4 + freshness, 2)


def compact_repo(repo: dict[str, Any], now: dt.datetime, discovery: str) -> dict[str, Any]:
    license_obj = repo.get("license") or {}
    return {
        "id": repo["id"],
        "full_name": repo["full_name"],
        "url": repo["html_url"],
        "description": repo.get("description") or "",
        "language": repo.get("language"),
        "stars": repo.get("stargazers_count", 0),
        "forks": repo.get("forks_count", 0),
        "created_at": repo.get("created_at", "")[:10],
        "pushed_at": repo.get("pushed_at", "")[:10],
        "topics": repo.get("topics", []),
        "license": license_obj.get("spdx_id"),
        "discovery": discovery,
        "score": repo_score(repo, now),
        "archived": repo.get("archived", False),
        "disabled": repo.get("disabled", False),
    }


def fetch_repositories(
    client: Client, config: dict[str, Any], cutoff_date: str, now: dt.datetime
) -> list[dict[str, Any]]:
    found: dict[str, dict[str, Any]] = {}
    per_query = config["per_query"]
    min_stars = 200
    active_since = months_ago((now + dt.timedelta(hours=8)).date(), 6)
    for base in config["new_repo_queries"]:
        query = f"{base} created:>={cutoff_date} stars:>={min_stars} archived:false"
        for repo in client.github_search(query, per_query):
            found[repo["full_name"]] = compact_repo(repo, now, "new")
    for base in config.get("active_repo_queries", []):
        query = f"{base} pushed:>={active_since} stars:200..999 archived:false"
        for repo in client.github_search(query, per_query):
            found.setdefault(repo["full_name"], compact_repo(repo, now, "active"))
    for base in config.get("growth_repo_queries", []):
        query = f"{base} stars:200..499 archived:false"
        for repo in client.github_search(query, per_query):
            found.setdefault(repo["full_name"], compact_repo(repo, now, "growth-watch"))
    # The public list is a popularity ranking: stars first, then freshness score.
    return sorted(found.values(), key=lambda item: (item["stars"], item["score"]), reverse=True)


def daily_eligible(repo, today):
    if (repo.get("stars", 0) < 200 or repo.get("archived") or repo.get("disabled")
            or not content_allowed(repo)):
        return False
    pushed = (repo.get("pushed_at") or "")[:10]
    cutoff = months_ago(today, 6)
    baseline = repo.get("star_baseline_6m")
    return (pushed >= cutoff or bool(baseline and cutoff <= baseline["date"] < today.isoformat()
                                     and grew_by_30_percent(repo, baseline)))


def apply_star_thresholds(repos, history, run_date):
    today = dt.date.fromisoformat(run_date)
    selected = []
    for repo in repos:
        if not content_allowed(repo) or repo.get("stars", 0) < 200:
            continue
        points = history.setdefault(repo["full_name"], {})
        repo["star_baseline_6m"] = star_baseline(points, today, 6)
        repo["star_baseline_12m"] = star_baseline(points, today, 12)
        points[run_date] = repo["stars"]
        if daily_eligible(repo, today):
            selected.append(repo)
    return selected


def md_escape(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def paper_table(papers: list[dict[str, Any]]) -> str:
    if not papers:
        return "本期没有发现通过严格双重筛选的新论文。\n"
    rows = ["| 日期 | 论文 | 作者 | 代码 | 市场/因子 | 来源/热度 |", "|---|---|---|---|---|---|"]
    labels = {
        "paper-link": "论文链接",
        "papers-with-code": "Papers with Code",
        "research-code": "ResearchCode",
        "arxiv-page": "arXiv 页面",
        "arxiv-id": "ID 命中",
        "title-match": "标题匹配",
        "hugging-face": "HF 社区代码候选",
    }
    for paper in papers:
        if not content_allowed(paper):
            continue
        title = f"[{md_escape(paper['title'])}]({paper['paper_url']})"
        authors = ", ".join(paper.get("authors", [])[:3]) + (" 等" if len(paper.get("authors", [])) > 3 else "")
        code = "—"
        if paper.get("code_url"):
            code = f"[{labels.get(paper.get('code_match'), '代码')}]({paper['code_url']})"
        source = f"[HF Trending]({paper['hf_url']}) · 👍 {paper.get('hf_upvotes', 0)}" if paper.get("hf_url") else "arXiv"
        rows.append(f"| {paper['published']} | {title} | {md_escape(authors)} | {code} | {market_labels(paper)} | {source} |")
    return "\n".join(rows) + "\n"


def repo_table(repos: list[dict[str, Any]]) -> str:
    if not repos:
        return "本期没有发现符合条件的新项目。\n"
    rows = ["| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |", "|---|---|---:|---:|---|---|---|---|"]
    for repo in repos:
        if not content_allowed(repo):
            continue
        name = f"[{repo['full_name']}]({repo['url']})"
        kind = category(repo)
        detail = ("回测：明确提及" if contains_term(str(repo), ["backtest", "回测"]) else "回测：需查文档") if kind == "交易框架" else tool_kind(repo) if kind == "工具" else kind
        baseline = repo.get("star_baseline_6m")
        growth_text = f"{(repo['stars'] / baseline['stars'] - 1):+.1%}（自 {baseline['date']}）" if baseline else "—"
        rows.append(
            f"| {name} | {md_escape(repo.get('description', ''))} | {repo['stars']} | "
            f"{growth_text} | {md_escape(repo.get('language'))} | {kind} | {market_labels(repo)} | {detail} |"
        )
    return "\n".join(rows) + "\n"


def render_digest(
    run_date: str,
    papers: list[dict[str, Any]],
    repos: list[dict[str, Any]],
    topic_papers: dict[str, list[dict[str, Any]]] | None = None,
    topic_repos: dict[str, list[dict[str, Any]]] | None = None,
    topic_configs: dict[str, dict[str, Any]] | None = None,
) -> str:
    topic_papers = topic_papers or {}
    topic_repos = topic_repos or {}
    topic_configs = topic_configs or {}
    code_count = sum(bool(item.get("code_url")) for item in papers)
    content = f"""# AI 应用研究日报 · {run_date}

本期新增：**{len(papers)} 篇论文**（其中 {code_count} 篇找到可能的代码）和 **{len(repos)} 个 GitHub 项目**。

## AI 投资与交易论文

{paper_table(papers)}

## GitHub 金融与交易工具

{repo_table(repos)}

"""
    for key, topic in topic_configs.items():
        selected_papers = topic_papers.get(key, [])
        selected_repos = topic_repos.get(key, [])
        matched = sum(bool(item.get("code_url")) for item in selected_papers)
        content += f"""## {topic['title']}

新增 **{len(selected_papers)} 篇论文**（{matched} 篇找到代码）和 **{len(selected_repos)} 个项目**。

### 论文

{paper_table(selected_papers)}

### GitHub 项目

{repo_table(selected_repos)}

"""
    content += """> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。
"""
    return content


def render_readme(
    run_date: str,
    papers: list[dict[str, Any]],
    repos: list[dict[str, Any]],
    topic_papers: dict[str, list[dict[str, Any]]],
    topic_repos: dict[str, list[dict[str, Any]]],
    topic_configs: dict[str, dict[str, Any]],
    popular_repos: list[dict[str, Any]] | None = None,
) -> str:
    popular = sorted([r for r in (popular_repos or []) if eligible(r, dt.date.fromisoformat(run_date))], key=lambda r: (-r["stars"], r["full_name"]))
    popular_sections = "## 热门项目 · Star ≥ 500\n\n按 Star 降序，按分类直接展示各类前 10 个项目；[查看全部热门项目](HOT_PROJECTS.md)。\n\n"
    for group in ("Agent", "交易框架", "工具", "游戏", "论文研究"):
        selected = [r for r in popular if category(r) == group][:10]
        if selected:
            popular_sections += f"### {group}\n\n{repo_table(selected)}\n"
    if not popular:
        popular_sections += "暂无通过筛选的热门项目。\n"
    return f"""# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集 AI 投资研究、金融 Agent、交易框架、金融工具和交易游戏。论文源结合 arXiv 与 [Hugging Face Trending Papers](https://huggingface.co/papers/trending)，仅筛选 AI 投资交易研究，按 arXiv ID 去重；Trending 中重新走热的旧论文也可收录，保留原发表日期与 HF 社区热度。

**[📚 完整热门项目总榜（全部历史项目 · Star 排名 · 分类导航）](HOT_PROJECTS.md)** · **[月度总结](archive/index.md)**

热门总榜每天随日报刷新，按 Star 降序排列。**500–999 Star** 须近一年有代码更新且 Star 增长 **≥ 30%**。**1,000 Star 及以上**须近三年有代码更新。分类包括 Agent、交易框架（回测/语言）、工具（看板/数据源/创意）、游戏、论文研究，市场标签区分美股、A股、虚拟货币、期货、因子。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。首页保留当日日报；历史内容每月仅一份 Markdown，月内累计去重更新，不再保存逐日日报文件。`data/` 中 JSON 用于累计和去重，不是逐日归档。日报项目须 **Star ≥ 200**，且近半年有代码更新或 Star 增长 **≥ 30%**。涨幅按窗口内最早一条有效 Star 快照与当前值比较，缺少历史快照时无法验证增长。项目名称、简介、topics、README 和论文标题、摘要会进行政治敏感主题筛选，检查不可用的仓库暂缓展示。同时排除 `.github`/个人主页仓库、资源导航合集及超过 400 字符的冗长简介仓库，优先展示可使用的项目。检索范围和阈值见 [`config.yaml`](config.yaml)。

---

{popular_sections}
---

{render_digest(run_date, papers, repos, topic_papers, topic_repos, topic_configs)}
"""


def ensure_state_schema(state: dict[str, Any], run_date: str) -> None:
    state.setdefault("schema_version", 2)
    state.setdefault("papers", {})
    state.setdefault("repositories", {})
    state.setdefault("topic_papers", {})
    state.setdefault("topic_repositories", {})
    state.setdefault("repo_star_history", {})
    seen = state.setdefault("seen", {"paper_ids": [], "repository_names": []})
    paper_ids = set(seen.setdefault("paper_ids", []))
    repo_names = set(seen.setdefault("repository_names", []))

    for paper in state["papers"].values():
        paper.setdefault("first_seen", run_date)
        paper_ids.add(paper["id"])
    for topic in state["topic_papers"].values():
        for paper in topic.values():
            paper.setdefault("first_seen", run_date)
            paper_ids.add(paper["id"])
    for repo in state["repositories"].values():
        repo.setdefault("first_seen", run_date)
        repo_names.add(repo["full_name"])
    for topic in state["topic_repositories"].values():
        for repo in topic.values():
            repo.setdefault("first_seen", run_date)
            repo_names.add(repo["full_name"])
    seen["paper_ids"] = sorted(paper_ids)
    seen["repository_names"] = sorted(repo_names)


def prune_recent_state(state: dict[str, Any], cutoff: dt.date) -> None:
    def prune(items: dict[str, dict[str, Any]]) -> None:
        for key, item in list(items.items()):
            first_seen = item.get("first_seen")
            if first_seen and dt.date.fromisoformat(first_seen) < cutoff:
                del items[key]

    prune(state["papers"])
    prune(state["repositories"])
    for items in state["topic_papers"].values():
        prune(items)
    for items in state["topic_repositories"].values():
        prune(items)
    state["repo_star_history"] = {
        name: points for name, points in state["repo_star_history"].items() if points
    }


def archive_paths(run_date: str) -> tuple[Path, Path]:
    date = dt.date.fromisoformat(run_date)
    directory = ARCHIVE_DIR / f"{date.year:04d}" / f"{date.month:02d}"
    return directory / f"{run_date}.md", directory / f"{run_date}.json"


def merge_daily_results(existing: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    def merge_items(
        old: list[dict[str, Any]], new: list[dict[str, Any]], key: str
    ) -> list[dict[str, Any]]:
        merged = {item[key]: item for item in old}
        merged.update({item[key]: item for item in new})
        return list(merged.values())

    merged = {
        "run_date": incoming["run_date"],
        "papers": merge_items(existing.get("papers", []), incoming.get("papers", []), "id"),
        "repositories": merge_items(
            existing.get("repositories", []), incoming.get("repositories", []), "full_name"
        ),
        "topic_papers": {},
        "topic_repositories": {},
    }
    paper_topics = set(existing.get("topic_papers", {})) | set(incoming.get("topic_papers", {}))
    repo_topics = set(existing.get("topic_repositories", {})) | set(
        incoming.get("topic_repositories", {})
    )
    for topic in paper_topics:
        merged["topic_papers"][topic] = merge_items(
            existing.get("topic_papers", {}).get(topic, []),
            incoming.get("topic_papers", {}).get(topic, []),
            "id",
        )
    for topic in repo_topics:
        repos = merge_items(
            existing.get("topic_repositories", {}).get(topic, []),
            incoming.get("topic_repositories", {}).get(topic, []),
            "full_name",
        )
        merged["topic_repositories"][topic] = sorted(
            repos, key=lambda item: item.get("stars", 0), reverse=True
        )
    merged["repositories"].sort(key=lambda item: item.get("stars", 0), reverse=True)
    merged["papers"].sort(key=lambda item: item.get("published", ""), reverse=True)
    for papers in merged["topic_papers"].values():
        papers.sort(key=lambda item: item.get("published", ""), reverse=True)
    return merged


def migrate_flat_archives() -> None:
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    for path in ARCHIVE_DIR.glob("????-??-??.md"):
        try:
            md_path, _ = archive_paths(path.stem)
        except ValueError:
            continue
        md_path.parent.mkdir(parents=True, exist_ok=True)
        if not md_path.exists():
            path.replace(md_path)
        else:
            path.unlink()


def compact_history(result: dict[str, Any], min_stars: int, growth_min: int) -> dict[str, Any]:
    papers: dict[str, dict[str, Any]] = {}
    repos: dict[str, dict[str, Any]] = {}

    paper_groups = {"finance": result.get("papers", [])} | result.get("topic_papers", {})
    repo_groups = {"finance": result.get("repositories", [])} | result.get(
        "topic_repositories", {}
    )
    for topic, items in paper_groups.items():
        for paper in items:
            papers[f"{topic}:{paper['id']}"] = {
                "id": paper["id"],
                "title": paper["title"],
                "published": paper["published"],
                "paper_url": paper["paper_url"],
                "code_url": paper.get("code_url"),
                "topic": topic,
            }
    for topic, items in repo_groups.items():
        for repo in items:
            growth = repo.get("star_growth_7d")
            if repo["stars"] < min_stars and (growth is None or growth < growth_min):
                continue
            key = f"{topic}:{repo['full_name']}"
            repos[key] = {
                "full_name": repo["full_name"],
                "url": repo["url"],
                "stars": repo["stars"],
                "star_growth_7d": growth,
                "language": repo.get("language"),
                "topic": topic,
            }
    return {"papers": papers, "repositories": repos}


def rollup_expired_archives(today: dt.date, project: dict[str, Any]) -> None:
    cutoff = today - dt.timedelta(days=int(project["archive_keep_days"]))
    for json_path in sorted(ARCHIVE_DIR.glob("????/??/????-??-??.json")):
        try:
            archive_date = dt.date.fromisoformat(json_path.stem)
        except ValueError:
            continue
        if archive_date >= cutoff:
            continue
        result = load_json(json_path, {})
        compact = compact_history(
            result, int(project["historical_min_stars"]), int(project["weekly_star_growth"])
        )
        month_path = HISTORY_DIR / f"{archive_date.year:04d}" / f"{archive_date.month:02d}.json"
        month = load_json(
            month_path,
            {
                "month": archive_date.strftime("%Y-%m"),
                "dates": [],
                "papers": {},
                "repositories": {},
            },
        )
        if json_path.stem not in month["dates"]:
            month["dates"].append(json_path.stem)
            month["dates"].sort()
        month["papers"].update(compact["papers"])
        month["repositories"].update(compact["repositories"])
        save_json(month_path, month)
        json_path.unlink()
        md_path = json_path.with_suffix(".md")
        if md_path.exists():
            md_path.unlink()


def rebuild_archive_index() -> None:
    daily = sorted(ARCHIVE_DIR.glob("????/??/????-??-??.md"), reverse=True)
    monthly = sorted(HISTORY_DIR.glob("????/??.json"), reverse=True)
    lines = [
        "# 历史归档",
        "",
        "最近 90 天保留完整 Markdown 与 JSON；更早内容转为精简月度 JSON。",
        "",
        "## 最近 90 天",
        "",
    ]
    lines.extend(f"- [{path.stem}]({path.relative_to(ARCHIVE_DIR).as_posix()})" for path in daily)
    lines.extend(["", "## 精简月度历史", ""])
    lines.extend(
        f"- [{path.parent.name}-{path.stem}](../{path.relative_to(ROOT).as_posix()})"
        for path in monthly
    )
    lines.append("")
    (ARCHIVE_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


def run(config_path: Path, dry_run: bool = False) -> dict[str, Any]:
    config = load_yaml(config_path)
    now = dt.datetime.now(dt.timezone.utc)
    today_cn = (now + dt.timedelta(hours=8)).date()
    run_date = today_cn.isoformat()
    cutoff = now - dt.timedelta(days=config["project"]["lookback_days"])
    state = load_json(STATE_PATH, {"papers": {}, "repositories": {}, "last_run": None})
    state["topic_papers"] = {}
    state["topic_repositories"] = {}
    ensure_state_schema(state, run_date)
    seen_paper_ids = set(state["seen"]["paper_ids"])
    seen_repo_names = set(state["seen"]["repository_names"])
    client = Client(os.getenv("GITHUB_TOKEN"))

    collection_warnings = []
    print("Collecting arXiv papers...", flush=True)
    try:
        papers = fetch_papers(client, config["papers"], cutoff)
    except (requests.RequestException, ET.ParseError) as exc:
        warning = f"arXiv 论文源采集失败（{type(exc).__name__}）；本次未获取新论文，已收录论文保留，GitHub 项目继续更新。"
        collection_warnings.append(warning)
        print(f"::warning::{warning}", flush=True)
        papers = []
    hf_papers = []
    if config["papers"].get("huggingface_trending", True):
        print("Collecting Hugging Face Trending finance papers...", flush=True)
        try:
            hf_papers = fetch_huggingface_papers(client, config["papers"], int(config["papers"].get("max_huggingface_results", 100)))
        except (requests.RequestException, ValueError) as exc:
            warning = f"Hugging Face Trending 采集失败（{type(exc).__name__}）；保留已有数据并继续更新。"
            collection_warnings.append(warning)
            print(f"::warning::{warning}", flush=True)
    papers = merge_paper_sources(papers, hf_papers)
    papers = [paper for paper in papers if paper["id"] not in seen_paper_ids]
    papers = papers[: config["project"]["max_papers_per_run"]]
    for paper in papers:
        paper["first_seen"] = run_date
        if not paper.get("code_url"):
            paper["code_url"], paper["code_match"] = find_code(
                client, paper, config.get("code_sources")
            )
        seen_paper_ids.add(paper["id"])

    print("Collecting recent GitHub projects...", flush=True)
    repo_candidates = fetch_repositories(client, config["github"], cutoff.date().isoformat(), now)
    topic_papers: dict[str, list[dict[str, Any]]] = {}
    topic_repos: dict[str, list[dict[str, Any]]] = {}
    print("Refreshing historical finance catalogue...", flush=True)
    previous_catalog = load_json(ROOT / "data" / "catalog.json", {}).get("repositories", {})
    known_repos = state["repositories"] | previous_catalog
    for paper in hf_papers:
        if paper.get("code_url"):
            name = paper["code_url"].split("github.com/", 1)[-1]
            if name.lower() not in {n.lower() for n in known_repos}:
                known_repos[name] = {"full_name": name, "url": paper["code_url"], "stars": 0}
    catalog_repos, catalog_warnings = collect_catalog(
        client, config["github"], known_repos, now, compact_repo
    )
    # Only current API observations enter the Star history.
    current = {r["full_name"]: r for r in catalog_repos if r.get("verified_at") == now.date().isoformat()}
    current.update({r["full_name"]: r for r in repo_candidates})
    observations = sorted(current.values(), key=lambda r: (-r["stars"], r["full_name"]))
    repos = apply_star_thresholds(observations, state["repo_star_history"], run_date)
    daily_names = {repo["full_name"] for repo in repo_candidates}
    repos = [repo for repo in repos if repo["full_name"] not in seen_repo_names
             and (repo["full_name"] in daily_names or repo["full_name"] not in previous_catalog)]
    repos = repos[: config["project"]["max_repos_per_run"]]
    for repo in repos:
        repo["first_seen"] = run_date
    for repo in catalog_repos:
        repo["star_baseline_12m"] = star_baseline(
            state["repo_star_history"].get(repo["full_name"], {}), today_cn, 12)
    catalog_repos = [repo for repo in catalog_repos if eligible(repo, today_cn)]
    history_cutoff = months_ago(today_cn, 12)
    state["repo_star_history"] = {
        name: {day: stars for day, stars in points.items() if day >= history_cutoff}
        for name, points in state["repo_star_history"].items()
    }
    result = {
        "run_date": run_date,
        "papers": papers,
        "repositories": repos,
        "topic_papers": topic_papers,
        "topic_repositories": topic_repos,
    }
    reviews = load_json(ROOT / "data" / "content_review.json", {})
    months = load_json(ROOT / "data" / "months.json", {})
    review_pool = dict(state["repositories"])
    for month in months.values():
        review_pool.update(month.get("repositories", {}))
    review_pool.update({r["full_name"]: r for r in catalog_repos + repos})
    print(f"Checking content of {len(review_pool)} finance repositories...", flush=True)
    review_repositories(client, list(review_pool.values()), reviews)
    catalog_repos = [r for r in catalog_repos if content_allowed(r, reviews)]
    result = clean_batch(result, reviews)
    papers, repos = result["papers"], result["repositories"]
    state["papers"] = {k: v for k, v in state["papers"].items() if content_allowed(v, reviews)}
    state["repositories"] = {k: v for k, v in state["repositories"].items() if content_allowed(v, reviews)}
    state["repo_star_history"] = {k: v for k, v in state["repo_star_history"].items() if content_allowed({"full_name": k}, reviews)}
    seen_repo_names = {n for n in seen_repo_names if content_allowed({"full_name": n}, reviews)}
    for month in months.values():
        for key in ("papers", "repositories"):
            month[key] = {k: v for k, v in month.get(key, {}).items() if content_allowed(v, reviews)}
    if dry_run:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return result

    for paper in papers:
        state["papers"][paper["id"]] = paper
    for repo in repos:
        seen_repo_names.add(repo["full_name"])
        state["repositories"][repo["full_name"]] = repo
    for key, selected_papers in topic_papers.items():
        for paper in selected_papers:
            state["topic_papers"][key][paper["id"]] = paper
    for key, selected_repos in topic_repos.items():
        for repo in selected_repos:
            state["topic_repositories"][key][repo["full_name"]] = repo
    state["seen"]["paper_ids"] = sorted(seen_paper_ids)
    state["seen"]["repository_names"] = sorted(seen_repo_names)
    state["last_run"] = now.isoformat()
    recent_cutoff = today_cn - dt.timedelta(days=int(config["project"]["archive_keep_days"]))
    prune_recent_state(state, recent_cutoff)
    save_json(ROOT / "data" / "content_review.json", reviews)
    save_json(ROOT / "data" / "months.json", months)
    save_json(STATE_PATH, state)
    latest = clean_batch(load_json(LATEST_PATH, {}), reviews)
    if latest.get("run_date") == run_date:
        latest["topic_papers"] = {}
        latest["topic_repositories"] = {}
        latest["repositories"] = [r | current.get(r["full_name"], {}) for r in latest["repositories"]]
        latest["repositories"] = [r for r in latest["repositories"]
                                  if daily_eligible(r, today_cn) and content_allowed(r, reviews)]
        result = merge_daily_results(latest, result)
    result["collection_warnings"] = collection_warnings
    save_json(LATEST_PATH, result)
    save_json(ROOT / "data" / "catalog.json", {
        "run_date": run_date,
        "repositories": {r["full_name"]: r for r in catalog_repos},
        "warnings": catalog_warnings,
    })
    (ROOT / "HOT_PROJECTS.md").write_text(
        render_catalog(catalog_repos, run_date, md_escape, catalog_warnings), encoding="utf-8"
    )
    publish_months(ROOT, result, load_json, save_json, render_digest)
    (ROOT / "README.md").write_text(
        render_readme(run_date, result["papers"], result["repositories"], {}, {}, {}, catalog_repos)
        + ("\n> " + "\n> ".join(collection_warnings) + "\n" if collection_warnings else ""),
        encoding="utf-8",
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=ROOT / "config.yaml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    result = run(args.config, args.dry_run)
    topic_paper_count = sum(len(items) for items in result.get("topic_papers", {}).values())
    topic_repo_count = sum(len(items) for items in result.get("topic_repositories", {}).values())
    print(
        f"Collected {len(result['papers']) + topic_paper_count} papers and "
        f"{len(result['repositories']) + topic_repo_count} repositories"
    )


if __name__ == "__main__":
    main()
