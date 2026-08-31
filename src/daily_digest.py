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
from urllib.parse import quote

import requests
import yaml


ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "data" / "state.json"
LATEST_PATH = ROOT / "data" / "latest.json"
ARCHIVE_DIR = ROOT / "archive"
ARXIV_API = "https://export.arxiv.org/api/query"
GITHUB_API = "https://api.github.com"
ATOM = {"a": "http://www.w3.org/2005/Atom"}
GITHUB_URL_RE = re.compile(r"https?://github\.com/[\w.-]+/[\w.-]+", re.I)
WORD_RE = re.compile(r"[a-z0-9]+")


class Client:
    def __init__(self, token: str | None = None) -> None:
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "ai-finance-daily/1.0"})
        if token:
            self.session.headers.update(
                {"Authorization": f"Bearer {token}", "X-GitHub-Api-Version": "2022-11-28"}
            )
        self._last_github_search = 0.0

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
        )
        self._last_github_search = time.monotonic()
        return response.json().get("items", [])


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
    response = client.get(
        ARXIV_API,
        params={
            "search_query": arxiv_query(config),
            "start": 0,
            "max_results": config["max_arxiv_results"],
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        },
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


def title_tokens(value: str) -> set[str]:
    stop = {"a", "an", "and", "for", "from", "in", "of", "on", "the", "to", "with", "using"}
    return {token for token in WORD_RE.findall(value.lower()) if len(token) > 2 and token not in stop}


def title_similarity(title: str, repo: dict[str, Any]) -> float:
    expected = title_tokens(title)
    actual = title_tokens(f"{repo.get('name', '')} {repo.get('description') or ''}")
    return len(expected & actual) / max(1, len(expected))


def find_code(client: Client, paper: dict[str, Any]) -> tuple[str | None, str | None]:
    embedded = GITHUB_URL_RE.search(f"{paper['abstract']} {paper.get('comment') or ''}")
    if embedded:
        return embedded.group(0).rstrip(".,);]"), "paper-link"

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
    }


def fetch_repositories(
    client: Client, config: dict[str, Any], cutoff_date: str, now: dt.datetime
) -> list[dict[str, Any]]:
    found: dict[str, dict[str, Any]] = {}
    per_query = config["per_query"]
    min_stars = config["min_stars"]
    for base in config["new_repo_queries"]:
        query = f"{base} created:>={cutoff_date} stars:>={min_stars} archived:false"
        for repo in client.github_search(query, per_query):
            found[repo["full_name"]] = compact_repo(repo, now, "new")
    for base in config.get("active_repo_queries", []):
        query = f"{base} pushed:>={cutoff_date} archived:false"
        for repo in client.github_search(query, per_query):
            found.setdefault(repo["full_name"], compact_repo(repo, now, "active"))
    # The public list is a popularity ranking: stars first, then freshness score.
    return sorted(found.values(), key=lambda item: (item["stars"], item["score"]), reverse=True)


def md_escape(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def paper_table(papers: list[dict[str, Any]]) -> str:
    if not papers:
        return "本期没有发现通过严格双重筛选的新论文。\n"
    rows = ["| 日期 | 论文 | 作者 | 代码 |", "|---|---|---|---|"]
    labels = {"paper-link": "论文链接", "arxiv-id": "ID 命中", "title-match": "标题匹配"}
    for paper in papers:
        title = f"[{md_escape(paper['title'])}]({paper['paper_url']})"
        authors = ", ".join(paper["authors"][:3]) + (" 等" if len(paper["authors"]) > 3 else "")
        code = "—"
        if paper.get("code_url"):
            code = f"[{labels.get(paper.get('code_match'), '代码')}]({paper['code_url']})"
        rows.append(f"| {paper['published']} | {title} | {md_escape(authors)} | {code} |")
    return "\n".join(rows) + "\n"


def repo_table(repos: list[dict[str, Any]]) -> str:
    if not repos:
        return "本期没有发现符合条件的新项目。\n"
    rows = ["| 项目 | 简介 | ⭐ | 语言 | 类型 |", "|---|---|---:|---|---|"]
    for repo in repos:
        name = f"[{repo['full_name']}]({repo['url']})"
        kind = "新项目" if repo["discovery"] == "new" else "近期活跃"
        rows.append(
            f"| {name} | {md_escape(repo['description'])} | {repo['stars']} | "
            f"{md_escape(repo['language'])} | {kind} |"
        )
    return "\n".join(rows) + "\n"


def render_digest(run_date: str, papers: list[dict[str, Any]], repos: list[dict[str, Any]]) -> str:
    code_count = sum(bool(item.get("code_url")) for item in papers)
    return f"""# AI 投资研究日报 · {run_date}

本期新增：**{len(papers)} 篇论文**（其中 {code_count} 篇找到可能的代码）和 **{len(repos)} 个 GitHub 项目**。

## AI 投资与交易论文

{paper_table(papers)}

## GitHub 金融与交易工具

{repo_table(repos)}

> 代码链接由规则自动匹配；“标题匹配”需要人工复核。本仓库只做研究信息整理，不构成投资建议。
"""


def render_readme(run_date: str, papers: list[dict[str, Any]], repos: list[dict[str, Any]]) -> str:
    return f"""# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集两类内容：

1. **论文**：严格要求同时涉及 AI 方法和投资、交易、资产配置或市场预测；来源至少包含 arXiv，并自动搜索对应 GitHub 代码。
2. **项目**：近期创建或活跃的量化交易、金融分析、行情/财务数据源、资金流/订单流、回测、自研策略、投资 Agent 等 GitHub 工具，按 Star 数优先排行。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。完整结构化数据位于 [`data/state.json`](data/state.json)，每日快照位于 [`archive/`](archive/)。搜索词和阈值可在 [`config.yaml`](config.yaml) 调整。

---

{render_digest(run_date, papers, repos)}
"""


def prune_archives(keep_days: int, today: dt.date) -> None:
    if not ARCHIVE_DIR.exists():
        return
    cutoff = today - dt.timedelta(days=keep_days)
    for path in ARCHIVE_DIR.glob("*.md"):
        try:
            if dt.date.fromisoformat(path.stem) < cutoff:
                path.unlink()
        except ValueError:
            continue


def run(config_path: Path, dry_run: bool = False) -> dict[str, Any]:
    config = load_yaml(config_path)
    now = dt.datetime.now(dt.timezone.utc)
    today_cn = (now + dt.timedelta(hours=8)).date()
    run_date = today_cn.isoformat()
    cutoff = now - dt.timedelta(days=config["project"]["lookback_days"])
    state = load_json(STATE_PATH, {"papers": {}, "repositories": {}, "last_run": None})
    client = Client(os.getenv("GITHUB_TOKEN"))

    papers = fetch_papers(client, config["papers"], cutoff)
    papers = [paper for paper in papers if paper["id"] not in state["papers"]]
    papers = papers[: config["project"]["max_papers_per_run"]]
    for paper in papers:
        paper["code_url"], paper["code_match"] = find_code(client, paper)

    repos = fetch_repositories(client, config["github"], cutoff.date().isoformat(), now)
    repos = [repo for repo in repos if repo["full_name"] not in state["repositories"]]
    repos = repos[: config["project"]["max_repos_per_run"]]

    result = {"run_date": run_date, "papers": papers, "repositories": repos}
    if dry_run:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return result

    for paper in papers:
        state["papers"][paper["id"]] = paper
    for repo in repos:
        state["repositories"][repo["full_name"]] = repo
    state["last_run"] = now.isoformat()
    save_json(STATE_PATH, state)
    save_json(LATEST_PATH, result)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    (ARCHIVE_DIR / f"{run_date}.md").write_text(render_digest(run_date, papers, repos), encoding="utf-8")
    (ROOT / "README.md").write_text(render_readme(run_date, papers, repos), encoding="utf-8")
    prune_archives(config["project"]["archive_keep_days"], today_cn)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=ROOT / "config.yaml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    result = run(args.config, args.dry_run)
    print(f"Collected {len(result['papers'])} papers and {len(result['repositories'])} repositories")


if __name__ == "__main__":
    main()
