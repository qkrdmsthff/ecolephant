from copy import deepcopy
from .common import load, require, check_refs, walk
from .semantics import semantic_errors


def check_contracts(spec,helper,policy):
    try:
        from jsonschema import Draft202012Validator, FormatChecker
        from openapi_spec_validator import OpenAPIV31SpecValidator
    except ImportError as exc:
        raise ValueError('Install harness/requirements-check.txt in your Python environment first') from exc
    errors=list(OpenAPIV31SpecValidator(spec).iter_errors())
    require(not errors,'OpenAPI error: '+'; '.join(str(e)[:700] for e in errors[:3]))
    check_refs(spec)
    check_refs(helper)
    Draft202012Validator.check_schema(helper)
    for schema in spec['components']['schemas'].values():
        Draft202012Validator.check_schema(schema)
    forbidden={'image','images','frame','frames','video','landmarks','raw_imu','rotation_rate_rad_s','pitch_rad','roll_rad','baseline_landmarks','owner_id'}
    for node in walk(spec['components']['schemas']):
        require(not(forbidden & set(node.get('properties',{}))),'Forbidden raw/private field in REST contract')
        if node.get('type')=='object':
            require(node.get('additionalProperties') is False,'Every payload object must reject extra properties')
    for route,methods in spec['paths'].items():
        for method,op in methods.items():
            if method not in {'get','post','put','delete','patch'}:
                continue
            if route!='/health':
                require(bool(op.get('security',spec.get('security'))),f'Missing auth: {route}')
    passed=0
    for fixture,schema_root,base in [
        ('harness/fixtures/http/contract-cases.json',spec,'#/components/schemas/'),
        ('harness/fixtures/helper/contract-cases.json',helper,'#/$defs/')
    ]:
        cases=load(fixture)['cases']
        require(any(c['valid'] for c in cases) and any(not c['valid'] for c in cases),'Need valid and invalid fixtures')
        for case in cases:
            envelope=deepcopy(schema_root)
            if base.startswith('#/components'):
                envelope={'$ref':base+case['schema'],'components':schema_root['components']}
            else:
                envelope={'$ref':base+case['schema'],'$defs':schema_root['$defs']}
            validator=Draft202012Validator(envelope,format_checker=FormatChecker())
            shape_errors=list(validator.iter_errors(case['value']))
            shape_valid=not shape_errors
            require(shape_valid==case['valid'],f'{case["id"]} schema expectation failed: {str(shape_errors[0])[:500] if shape_errors else "unexpected acceptance"}')
            if shape_valid:
                meanings=semantic_errors(case['schema'],case['value'],policy)
                require((not meanings)==case['semantics_valid'],f'{case["id"]} semantic expectation failed: {meanings}')
            passed+=1
    print(f'PASS contracts: OpenAPI 3.1, {len(spec["components"]["schemas"])} HTTP schemas, helper schema, {passed} positive/negative cases')
