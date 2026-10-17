from .common import ROOT, require

def check_ci():
    try:
        import yaml
    except ImportError as exc:
        raise ValueError('Install harness/requirements-check.txt') from exc
    path=ROOT/'.github/workflows/harness.yml'
    workflow=yaml.load(path.read_text(encoding='utf-8'),Loader=yaml.BaseLoader)
    require(set(workflow['on'])=={'push','pull_request'},'Unexpected CI trigger')
    require(workflow['permissions']=={'contents':'read'},'CI permissions must stay read-only')
    steps=workflow['jobs']['harness']['steps']
    require(any(s.get('run')=='python harness/scripts/check.py' for s in steps),'Missing complete harness CI check')
    require(any('harness/requirements-check.txt' in s.get('run','') for s in steps),'Missing check dependencies')
    checkout=next(s for s in steps if s.get('uses','').startswith('actions/checkout@'))
    require(checkout['with']['persist-credentials']=='false','Checkout must not persist credentials')
    print('PASS CI definition: YAML, read-only permissions, check entry point (hosted run not executed)')
