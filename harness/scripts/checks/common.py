from pathlib import Path
from urllib.parse import unquote
import json

ROOT = Path(__file__).resolve().parents[3]

def load(relative):
    return json.loads((ROOT / relative).read_text(encoding='utf-8'))

def require(condition, message):
    if not condition:
        raise ValueError(message)

def relative(path):
    return path.relative_to(ROOT).as_posix()

def within_root(path):
    try:
        path.relative_to(ROOT)
        return True
    except ValueError:
        return False

def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)

def check_refs(document):
    for node in walk(document):
        if '$ref' not in node:
            continue
        pointer=node['$ref']
        require(pointer.startswith('#/'), f'Only local refs are supported: {pointer}')
        current=document
        for part in pointer[2:].split('/'):
            key=unquote(part).replace('~1','/').replace('~0','~')
            current=current[int(key)] if isinstance(current,list) else current[key]

def markdown_files():
    return [p for p in ROOT.rglob("*.md") if not any(part in {".git", ".venv", "node_modules", "tmp", "__pycache__"} for part in p.relative_to(ROOT).parts)]
