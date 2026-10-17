"""Entry point for small, independently callable repository checks."""
import argparse
from datetime import date
from pathlib import Path
import subprocess
import sys
from checks.common import ROOT, load, require, markdown_files
from checks.manifest import check_manifest
from checks.map import check_map
from checks.links import check_links
from checks.traceability import check_traceability
from checks.policy import check_policy
from checks.contracts import check_contracts
from checks.architecture import check_architecture
from checks.secrets import check_secrets
from checks.freshness import check_freshness
from checks.ci import check_ci

def self_tests():
    result=subprocess.run([sys.executable,'-B','-m','unittest','discover','-s',str(ROOT/'harness/tests'),'-p','test_*.py'],cwd=ROOT)
    require(result.returncode==0,'Checker regression tests failed')

def main():
    require(sys.version_info>=(3,10),'Python 3.10+ required')
    checks={
        'manifest':lambda:check_manifest(load('harness/metadata/manifest.json')),
        'map':check_map,
        'links':check_links,
        'traceability':lambda:check_traceability(load('docs/api/openapi.json'),markdown_files()),
        'policy':lambda:check_policy(load('harness/fixtures/policy/example.json')),
        'contracts':lambda:check_contracts(load('docs/api/openapi.json'),load('docs/api/helper-message.schema.json'),load('harness/fixtures/policy/example.json')),
        'architecture':check_architecture,
        'secrets':check_secrets,
        'ci':check_ci,
        'self-tests':self_tests,
    }
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--only',choices=['all',*checks],default='all')
    parser.add_argument('--as-of',type=date.fromisoformat)
    args=parser.parse_args()
    failures=[]
    selected=checks.items() if args.only=='all' else [(args.only,checks[args.only])]
    for name,run in selected:
        try:
            run()
        except Exception as exc:
            failures.append(name)
            print(f'FAIL {name}: {exc}',file=sys.stderr)
    check_freshness(args.as_of)
    require(not failures,'Failed checks: '+', '.join(failures))
    print('PASS selected repository/document/contract checks. Product and device scenarios remain planned.')

if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        print(f'FAIL {exc}',file=sys.stderr)
        sys.exit(1)
