"""Conservative topic screening for collected finance content, without raw README storage."""
import base64
import hashlib
import re
from concurrent.futures import ThreadPoolExecutor

POLICY_VERSION = 2

POLITICAL_TOPIC = re.compile(
    r'\b(?:politic\w*|geopolitic\w*|elections?|propaganda|protests?|censorship|'
    r'separatism|secession|terroris\w*|extremis\w*)\b|'
    r'政治|政党|竞选|选举|意识形态|政治宣传|抗议运动|网络审查|政治审查|'
    r'分裂主义|恐怖主义|极端主义|台独|港独|反共|法轮功|天安门事件|六四事件', re.I)


RESOURCE_COLLECTION = re.compile(
    r'(?:^|[/\s_-])awesome(?:$|[/\s_-])|curated (?:list|collection)|'
    r'collection of .*?(?:resources|repositories|links|papers)|'
    r'资源汇总|资源合集|项目合集|工具合集|资料汇总|资料合集|收藏夹|项目导航|论文列表', re.I)


def project_allowed(item):
    name = item.get('full_name', '')
    if not name:
        return True  # Papers use the topical policy, not repository naming rules.
    owner, _, repo = name.partition('/')
    if repo.lower() == '.github' or repo.lower() == owner.lower():
        return False
    description = ' '.join((item.get('description') or '').split())
    if len(description) > 400:
        return False
    return not RESOURCE_COLLECTION.search(name + ' ' + description)


def review_key(name):
    return hashlib.sha256(name.lower().encode()).hexdigest()


def content_allowed(item, reviews=None):
    if not project_allowed(item):
        return False
    text = ' '.join(str(item.get(k) or '') for k in (
        'full_name', 'title', 'description', 'abstract', 'comment', 'code_url', 'url'))
    text += ' ' + ' '.join(item.get('topics') or [])
    if POLITICAL_TOPIC.search(text):
        return False
    names = [item.get('full_name', '')]
    code = item.get('code_url') or ''
    if 'github.com/' in code:
        names.append(code.split('github.com/', 1)[1].strip('/'))
    return not any((reviews or {}).get(review_key(name), {}).get('status') in ('excluded', 'unavailable') for name in names if name)


def review_repositories(client, repos, reviews):
    """Check README on first admission or changed push date; fail closed on errors."""
    def inspect(repo):
        key = review_key(repo['full_name'])
        revision = repo.get('pushed_at', '')
        if not content_allowed(repo):
            return key, {'status': 'excluded', 'revision': revision, 'policy_version': POLICY_VERSION}
        old = reviews.get(key, {})
        if old.get('policy_version') == POLICY_VERSION and old.get('revision') == revision and old.get('status') in ('passed', 'excluded'):
            return key, old
        try:
            response = client.get(f"https://api.github.com/repos/{repo['full_name']}/readme", headers=client.github_headers)
            data = response.json()
            if data.get('encoding') != 'base64':
                raise ValueError('README could not be decoded')
            text = base64.b64decode(data.get('content', '')).decode('utf-8', errors='replace')
            link_count = len(re.findall(r'https?://github\.com/', text, re.I))
            collection = RESOURCE_COLLECTION.search(text[:2500]) or link_count > 200
            status = 'excluded' if POLITICAL_TOPIC.search(text) or collection else 'passed'
        except Exception as exc:
            status = 'passed' if getattr(getattr(exc, 'response', None), 'status_code', None) == 404 else 'unavailable'
        return key, {'status': status, 'revision': revision, 'policy_version': POLICY_VERSION}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for key, decision in pool.map(inspect, repos):
            reviews[key] = decision
    return reviews


def clean_batch(batch, reviews):
    result = dict(batch)
    for key in ('papers', 'repositories'):
        result[key] = [x for x in batch.get(key, []) if content_allowed(x, reviews)]
    result['topic_papers'] = {}
    result['topic_repositories'] = {}
    return result
