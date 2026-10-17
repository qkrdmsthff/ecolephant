from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"harness/scripts"))
import json
import tempfile
from checks.architecture import inspect_source


class ArchitectureChecks(unittest.TestCase):
    def setUp(self):
        self.scratch=(ROOT/'tmp/harness-tests').resolve()
        if not self.scratch.is_relative_to(ROOT.resolve()):
            raise ValueError('Test scratch directory outside repository')
        self.scratch.mkdir(parents=True,exist_ok=True)
        self.temp=tempfile.TemporaryDirectory(prefix='case-',dir=self.scratch)
        self.addCleanup(self.safe_cleanup)
        self.root=Path(self.temp.name)
        self.policy=json.loads((ROOT/'harness/metadata/architecture-policy.json').read_text(encoding='utf-8'))
        for folder in self.policy['packages']:
            (self.root/folder).mkdir()

    def safe_cleanup(self):
        target=Path(self.temp.name).resolve()
        if target.parent!=self.scratch or not target.is_relative_to(ROOT.resolve()):
            raise ValueError('Unsafe test cleanup path')
        self.temp.cleanup()

    def inspect(self,relative,text):
        path=self.root/relative
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(text,encoding='utf-8')
        return inspect_source(path,self.root,self.policy)

    def test_frontend_can_import_analysis(self):
        self.assertEqual(self.inspect('frontend/view.py','from ai.types import Observation\n'),[])

    def test_analysis_cannot_import_backend(self):
        self.assertTrue(self.inspect('ai/engine.py','from backend.repo import Session\n'))

    def test_backend_cannot_import_frontend(self):
        self.assertTrue(self.inspect('backend/routes.py','import frontend.view\n'))

    def test_js_relative_analysis_to_backend_is_rejected(self):
        self.assertTrue(self.inspect('ai/engine.ts',"import { db } from '../backend/db';\n"))

    def test_js_frontend_to_analysis_is_allowed(self):
        self.assertEqual(self.inspect('frontend/view.ts',"import { assess } from '../ai/engine';\n"),[])

    def test_python_io_in_analysis_is_rejected(self):
        self.assertTrue(self.inspect('ai/io.py','open("output.txt", "w")\n'))

    def test_js_io_in_analysis_is_rejected(self):
        self.assertTrue(self.inspect('ai/io.ts','fetch("/api");\n'))

    def test_filesystem_import_in_analysis_is_rejected(self):
        self.assertTrue(self.inspect('ai/io.ts',"import fs from 'node:fs';\n"))

    def test_python_network_import_is_rejected(self):
        self.assertTrue(self.inspect('ai/io.py','from urllib.request import urlopen\n'))

    def test_python_comments_do_not_trigger_io_check(self):
        self.assertEqual(self.inspect('ai/pure.py','# open is forbidden\nvalue = 1\n'),[])

    def test_js_repository_escape_is_rejected(self):
        self.assertTrue(self.inspect('ai/escape.ts',"import value from '../../outside';\n"))

    def test_js_comments_do_not_trigger_io_check(self):
        self.assertEqual(self.inspect('ai/pure.ts','// fetch is forbidden\nconst value = 1;\n'),[])
