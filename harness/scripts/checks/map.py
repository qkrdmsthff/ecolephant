from datetime import date
from .common import ROOT, load, require, markdown_files

def line_budget(text, limit, path):
    require(len(text.splitlines()) <= limit, f'{path}: split this document; maximum {limit} lines')

def check_map():
    policy=load('harness/metadata/docs-policy.json')
    catalog=load('harness/metadata/documents.json')['documents']
    paths=[item['path'] for item in catalog]
    require(len(paths)==len(set(paths)), 'Duplicate document registration')
    actual={p.relative_to(ROOT).as_posix() for p in markdown_files()}
    require(set(paths)==actual, f'Document registry mismatch: missing={sorted(actual-set(paths))}, stale={sorted(set(paths)-actual)}')
    for item in catalog:
        require(item['status'] in {'draft','active','historical','reference'}, f'Invalid document status: {item["path"]}')
        if item['reviewed_on'] is not None:
            date.fromisoformat(item['reviewed_on'])
        require(bool(item['owner']), f'Missing document owner role: {item["path"]}')
    for name in policy['entry_maps']:
        line_budget((ROOT/name).read_text(encoding='utf-8'),policy['map_line_limit'],name)
    for path in (ROOT/policy['knowledge_prefix']).rglob('*.md'):
        name=path.relative_to(ROOT).as_posix()
        line_budget(path.read_text(encoding='utf-8'),policy['knowledge_line_limit'],name)
        require((path.parent/'index.md').is_file(), f'No folder index for {name}')
    index=(ROOT/'harness/docs/index.md').read_text(encoding='utf-8')
    for topic in policy['required_topics']:
        require(f'{topic}/index.md' in index, f'Unrouted topic: {topic}')
    for folder,statuses in [('active',{'planned','in_progress','blocked'}),('completed',{'completed'})]:
        for plan in (ROOT/f'harness/docs/plans/{folder}').glob('*.md'):
            if plan.name=='index.md':
                continue
            text=plan.read_text(encoding='utf-8')
            require(any(f'- 상태: {state}' in text for state in statuses), f'Invalid plan state: {plan.name}')
            require('- 생성일:' in text, f'Plan has no creation date: {plan.name}')
    print(f'PASS map: {len(actual)} documents, {len(policy["required_topics"])} knowledge topics, short files and plan states')
