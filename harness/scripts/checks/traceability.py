import re
from .common import ROOT, load, require, relative


def check_traceability(spec, markdown):
    trace=load('harness/metadata/traceability.json')['requirements']
    scenarios=load('harness/fixtures/acceptance/scenarios.json')['scenarios']
    req_ids={r['id'] for r in trace}
    scenario_ids={s['id'] for s in scenarios}
    decision_text=(ROOT/'docs/decisions/open-decisions.md').read_text(encoding='utf-8')
    decision_ids=set(re.findall(r'DEC-\d{3}',decision_text))
    operations=[op['operationId'] for path in spec['paths'].values() for method,op in path.items() if method in {'get','post','put','delete','patch'}]
    require(len(operations)==len(set(operations)),'Duplicate operationId')
    require(len(req_ids)==len(trace),'Duplicate requirement ID')
    require(len(scenario_ids)==len(scenarios),'Duplicate scenario ID')
    mapping={r['id']:r for r in trace}
    for req in trace:
        require(req['scenarios'],f'No scenario: {req["id"]}')
        require(set(req['scenarios'])<=scenario_ids,f'Unknown scenario: {req["id"]}')
        require(set(req['operations'])<=set(operations),f'Unknown operation: {req["id"]}')
        require(all((ROOT/p).is_file() for p in req['specs']),f'Missing spec: {req["id"]}')
        require(all(isinstance(p,int) and 1<=p<=10 for p in req['source_pages']),f'Invalid source page: {req["id"]}')
    for scenario in scenarios:
        require(set(scenario['requirements'])<=req_ids,f'Unknown requirement: {scenario["id"]}')
        require(scenario['status'] in {'planned','passed','failed','blocked'},f'Invalid status: {scenario["id"]}')
        require(scenario['status']!='passed' or bool(scenario['evidence']),f'Missing pass evidence: {scenario["id"]}')
        for rid in scenario['requirements']:
            require(scenario['id'] in mapping[rid]['scenarios'],f'Asymmetric trace: {rid}/{scenario["id"]}')
        for field in ['given','when','then','verification_layer']:
            require(bool(scenario[field]),f'Missing {field}: {scenario["id"]}')
    for req in trace:
        for sid in req['scenarios']:
            target=next(s for s in scenarios if s['id']==sid)
            require(req['id'] in target['requirements'],f'Asymmetric trace: {req["id"]}/{sid}')
    linked={op for r in trace for op in r['operations']}
    require(set(operations)-{'getHealth'}<=linked,'Unlinked product operation')
    for path in markdown:
        text=path.read_text(encoding='utf-8')
        for pattern,known in [(r'REQ-\d{3}',req_ids),(r'AC-\d{3}',scenario_ids),(r'DEC-\d{3}',decision_ids)]:
            require(set(re.findall(pattern,text))<=known,f'Unknown ID in {relative(path)}')
    print(f'PASS traceability: {len(req_ids)} requirements, {len(scenario_ids)} planned/evidenced scenarios, {len(operations)} operations, {len(decision_ids)} decisions')
