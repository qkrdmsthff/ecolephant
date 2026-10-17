import hashlib
from .common import ROOT, require, within_root


def check_manifest(manifest):
    paths=manifest['required_files']
    require(len(paths)==len(set(paths)), 'Duplicate manifest paths')
    for name in paths:
        target=(ROOT/name).resolve()
        require(within_root(target) and target.is_file(), f'Missing or outside file: {name}')
    source=ROOT/manifest['source']['path']
    digest=hashlib.sha256(source.read_bytes()).hexdigest()
    require(digest==manifest['source']['sha256'], 'Source PDF digest mismatch')
    print(f'PASS manifest: {len(paths)} required files and source PDF hash')
