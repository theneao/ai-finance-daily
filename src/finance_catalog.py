"""Persistent finance catalogue, conservative metadata labels and monthly publishing."""
from __future__ import annotations

import calendar
import datetime as dt
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from content_policy import content_allowed

MARKETS = {
    '美股': r'\b(us stocks?|u\.s\.|nasdaq|nyse|s&p|sp500|alpaca|american stock)\b',
    'A股': r'a[ -]?shares?|ashare|a股|沪深|上证|深证|tushare|baostock|akshare|china stock|chinese stock',
    '虚拟货币': r'crypto|bitcoin|ethereum|binance|币|digital asset|\bbtc\b|\bdefi\b',
    '期货': r'futures?|期货|期權|期权|derivatives?|\bcta\b',
    '因子': r'factor|alpha mining|alpha generation|因子|因子挖掘|alphagen',
}


def text_of(item: dict[str, Any]) -> str:
    return ' '.join(str(item.get(k) or '') for k in ('full_name', 'title', 'description', 'abstract')) + ' ' + ' '.join(item.get('topics') or [])


def market_labels(item: dict[str, Any]) -> str:
    text = text_of(item).lower()
    return '、'.join(label for label, pattern in MARKETS.items() if re.search(pattern, text)) or '未明确（需查文档）'


def category(item: dict[str, Any]) -> str:
    text = text_of(item).lower()
    if re.search(r'agent|multi-agent|智能体', text):
        return 'Agent'
    if re.search(r'paper|research|benchmark|survey|论文|研究|\bfinrl\b|\bqlib\b|alphagen', text):
        return '论文研究'
    if re.search(r'backtest|trading framework|trading engine|trading platform|quantitative framework|量化框架|回测|vnpy|nautilus|lean engine', text):
        return '交易框架'
    if re.search(r'\bgame\b|simulator game|游戏|gamif', text):
        return '游戏'
    return '工具'


def tool_kind(item: dict[str, Any]) -> str:
    text = text_of(item).lower()
    labels = [label for label, pattern in {
        '看板': r'dashboard|terminal|visualiz|看板|可视化|screener',
        '数据源': r'data|\bapi\b|scrap|crawler|数据|行情',
        '创意': r'experiment|creative|prototype|创意|实验',
    }.items() if re.search(pattern, text)]
    return '、'.join(labels) or '分析/策略工具'


def months_ago(today: dt.date, months: int) -> str:
    year, month = divmod(today.year * 12 + today.month - 1 - months, 12)
    day = min(today.day, calendar.monthrange(year, month + 1)[1])
    return dt.date(year, month + 1, day).isoformat()


def active_cutoff(today: dt.date) -> str:
    return months_ago(today, 36)


def star_baseline(points, today, months):
    start = months_ago(today, months)
    day = min((day for day, stars in points.items()
               if start <= day < today.isoformat() and stars > 0), default=None)
    return {"date": day, "stars": points[day]} if day else None


def grew_by_30_percent(repo, baseline):
    return bool(baseline and baseline["stars"] > 0
                and repo["stars"] * 10 >= baseline["stars"] * 13)


def eligible(repo: dict[str, Any], today: dt.date) -> bool:
    if not content_allowed(repo) or repo.get('archived') or repo.get('disabled'):
        return False
    stars = repo.get('stars', 0)
    pushed = (repo.get('pushed_at') or '')[:10]
    if stars >= 1000:
        return pushed >= active_cutoff(today)
    if stars < 500 or pushed < months_ago(today, 12):
        return False
    baseline = repo.get('star_baseline_12m')
    return bool(baseline and months_ago(today, 12) <= baseline['date'] < today.isoformat()
                and grew_by_30_percent(repo, baseline))


def ranked(repos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(repos, key=lambda r: (-r.get('stars', 0), r['full_name'].lower()))


def collect_catalog(client, config, known, now, compact_repo):
    """Search all creation dates, paginate, and split crowded star ranges at 1,000."""
    today = now.date()
    known = {n: r for n, r in known.items() if (r.get("stars", 0) >= 500 or r.get("stars", 0) == 0) and content_allowed(r)}
    found = {}
    warnings = []

    def search(base, low=500, high=None):
        stars = f'{low}..{high}' if high is not None else f'>={low}'
        query = f'{base} stars:{stars} pushed:>={active_cutoff(today)} archived:false fork:false'
        first = client.github_search_page(query, 1)
        if first.get('incomplete_results'):
            warnings.append(f'GitHub 返回不完整结果：{base}')
        total = first.get('total_count', 0)
        if total > 1000:
            upper = high or max((r['stargazers_count'] for r in first.get('items', [])), default=low)
            if upper > low:
                mid = (low + upper) // 2
                search(base, low, mid)
                search(base, mid + 1, upper)
                return
            warnings.append(f'同 Star 分区超过 GitHub 1000 条限制：{base} ({low})')
        for page in range(1, min(10, (total + 99) // 100) + 1):
            response = first if page == 1 else client.github_search_page(query, page)
            for raw in response.get('items', []):
                repo = compact_repo(raw, now, 'historical')
                if repo.get("stars", 0) >= 500 and content_allowed(repo):
                    found[repo['full_name']] = repo

    for query in config['catalog_queries']:
        try:
            search(query)
        except Exception as exc:
            warnings.append(f'搜索失败：{query} ({type(exc).__name__})')

    # A repo falling out of a search page must still have its stars/activity refreshed.
    def refresh(item):
        name, old = item
        try:
            response = client.get(f'https://api.github.com/repos/{name}', headers=client.github_headers)
            return name, compact_repo(response.json(), now, 'historical'), None
        except Exception as exc:
            if getattr(getattr(exc, 'response', None), 'status_code', None) in (404, 410, 451):
                return name, {}, f'项目已移除或不可访问：{name}'
            # Keep last verified metadata on transient failures, and disclose its age.
            return name, old, f'刷新失败：{name} ({type(exc).__name__})'

    pending = [(name, repo) for name, repo in known.items() if name not in found]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for name, repo, error in pool.map(refresh, pending):
            if error:
                warnings.append(error)
            else:
                repo['verified_at'] = today.isoformat()
            if repo.get("stars", 0) >= 500 and content_allowed(repo):
                found[repo["full_name"]] = repo
    pending_names = {name for name, _ in pending}
    for repo in found.values():
        if repo['full_name'] not in pending_names:
            repo['verified_at'] = today.isoformat()
    return ranked(list(found.values())), warnings


def render_catalog(repos, run_date, escape, warnings=None):
    repos = ranked([r for r in repos if eligible(r, dt.date.fromisoformat(run_date))])
    lines = ['# 金融热门项目总榜', '', '[返回首页](README.md) · [月度归档](archive/index.md)', '',
             f'更新日期：{run_date}。收录 {len(repos)} 个项目。500–999 Star 须近一年有代码更新且 Star 增长 ≥ 30%。1,000 Star 及以上须近三年有代码更新。', '',
             '涨幅按窗口内最早一条有效 Star 快照与当前值比较，缺少历史快照时无法验证增长。', '',
             '覆盖历史创建的金融项目，不限制为近期新库；按当前 Star 降序排列。检索词见 config.yaml，GitHub 搜索无法保证穷尽全部项目。', '',
             '分类与市场标签依据仓库名称、简介和 topics，可同时涉及多个市场；未明确表示尚需核对文档，并非不支持。', '']
    if warnings:
        lines += [f'> 本次有 {len(warnings)} 项检索/刷新异常；失败项目保留上次核验信息。', '']
        lines += ['<details><summary>检索与刷新异常</summary>', ''] + [f'- {escape(w)}' for w in warnings] + ['', '</details>', '']
    lines += ['## 全部项目 · Star 总排名', '', '| 排名 | 项目 | ⭐ | 分类 | 市场/因子 | 语言 | 最近代码更新 | 核验日期 | 一年内已观测涨幅 |', '|---:|---|---:|---|---|---|---|---|---|']
    for i, repo in enumerate(repos, 1):
        baseline = repo.get("star_baseline_12m")
        growth = f"{(repo['stars'] / baseline['stars'] - 1):+.1%}（自 {baseline['date']}）" if baseline else "—"
        lines.append(f"| {i} | [{escape(repo['full_name'])}]({repo['url']}) | {repo['stars']} | {category(repo)} | {market_labels(repo)} | {escape(repo.get('language'))} | {repo.get('pushed_at', '')[:10]} | {repo.get('verified_at', '待刷新')} | {growth} |")
    for group in ('Agent', '交易框架', '工具', '游戏', '论文研究'):
        lines += ['', f'## {group}', '', '| 项目 | ⭐ | 简介 | 市场/因子 | 语言 | 能力/用途 |', '|---|---:|---|---|---|---|']
        for repo in repos:
            if category(repo) != group:
                continue
            text = text_of(repo).lower()
            detail = ('回测：明确提及' if re.search(r'backtest|回测', text) else '回测：未明确，需查文档') if group == '交易框架' else tool_kind(repo) if group == '工具' else group
            lines.append(f"| [{escape(repo['full_name'])}]({repo['url']}) | {repo['stars']} | {escape(repo.get('description'))} | {market_labels(repo)} | {escape(repo.get('language'))} | {detail} |")
    return '\n'.join(lines) + '\n'


def publish_months(root, result, load_json, save_json, render_digest):
    """One Markdown per month; centralized JSON is internal accumulation state."""
    archive = root / 'archive'
    months_path = root / 'data' / 'months.json'
    months = load_json(months_path, {})

    def absorb(batch):
        date = batch.get('run_date', '')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date):
            return
        month = months.setdefault(date[:7], {'papers': {}, 'repositories': {}})
        for key, identity in (('papers', 'id'), ('repositories', 'full_name')):
            for item in batch.get(key, []):
                month[key][item[identity]] = item

    legacy = sorted(archive.rglob('????-??-??.json'))
    for path in legacy:
        absorb(load_json(path, {}))
    for path in sorted((root / 'history').glob('????/??.json')):
        old = load_json(path, {})
        absorb({'run_date': old.get('month', '') + '-01', **{key: [v for v in old.get(key, {}).values() if v.get('topic', 'finance') == 'finance'] for key in ('papers', 'repositories')}})
    absorb(result)
    archive.mkdir(parents=True, exist_ok=True)
    for month, data in sorted(months.items()):
        data['papers'] = {k: v for k, v in data['papers'].items() if content_allowed(v)}
        data['repositories'] = {k: v for k, v in data['repositories'].items() if content_allowed(v)}
        papers = sorted(data['papers'].values(), key=lambda p: p.get('published', ''), reverse=True)
        repos = ranked(list(data['repositories'].values()))
        content = render_digest(month, papers, repos)
        (archive / f'{month}.md').write_text(content, encoding='utf-8')
    save_json(months_path, months)
    # Delete only legacy daily outputs after all summaries are safely written.
    for path in legacy + list(archive.rglob('????-??-??.md')) + list((root / 'history').glob('????/??.json')):
        path.unlink()
    index = '# 月度总结\n\n每月仅保存一份 Markdown，月内每天合并去重更新，项目按 Star 降序。\n\n'
    index += '\n'.join(f'- [{month}]({month}.md)' for month in sorted(months, reverse=True)) + '\n'
    (archive / 'index.md').write_text(index, encoding='utf-8')
