from datetime import date, datetime, timezone, timedelta
import hashlib
from .common import ROOT, load, require

def review_warnings(documents, as_of, interval, actual_hashes=None):
    warnings=[]
    for item in documents:
        if actual_hashes is not None and item['path'] in actual_hashes and item.get('sha256')!=actual_hashes[item['path']]:
            warnings.append(f'{item["path"]}: changed since recorded review')
        if item['status']=='historical':
            continue
        reviewed=item['reviewed_on']
        if reviewed is None:
            warnings.append(f'{item["path"]}: review date missing')
        elif (as_of-date.fromisoformat(reviewed)).days>interval:
            warnings.append(f'{item["path"]}: review overdue')
    return warnings

def check_freshness(as_of=None):
    today=as_of or datetime.now(timezone(timedelta(hours=9))).date()
    documents=load('harness/metadata/documents.json')['documents']
    policy=load('harness/metadata/docs-policy.json')
    hashes={item['path']:hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest() for item in documents if (ROOT/item['path']).is_file()}
    warnings=review_warnings(documents,today,policy['review_interval_days'],hashes)
    drafts=sum(item['status']=='draft' for item in documents)
    print(f'INFO freshness as of {today}: {len(documents)} registered docs, {drafts} drafts, {len(warnings)} review reminders')
    for warning in warnings[:12]:
        print('WARN '+warning)
    if len(warnings)>12:
        print(f'WARN {len(warnings)-12} more; inspect metadata/documents.json')
    return warnings
