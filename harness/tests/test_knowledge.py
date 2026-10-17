from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"harness/scripts"))
from datetime import date
from checks.map import line_budget
from checks.freshness import review_warnings
from checks.common import check_refs


class KnowledgeChecks(unittest.TestCase):
    def test_long_knowledge_file_is_rejected(self):
        with self.assertRaises(ValueError):
            line_budget('\n'.join(['text']*81),80,'topic.md')

    def test_short_knowledge_file_is_allowed(self):
        line_budget('# Topic\n\nA single subject.\n',80,'topic.md')

    def test_old_review_date_produces_reminder(self):
        docs=[{'path':'topic.md','status':'active','reviewed_on':'2026-09-01'}]
        self.assertEqual(len(review_warnings(docs,date(2026,10,17),30)),1)

    def test_current_draft_is_not_stale_by_status(self):
        docs=[{'path':'topic.md','status':'draft','reviewed_on':'2026-10-17'}]
        self.assertEqual(review_warnings(docs,date(2026,10,17),30),[])

    def test_content_change_requires_review_even_on_same_day(self):
        docs=[{'path':'topic.md','status':'active','reviewed_on':'2026-10-17','sha256':'before'}]
        self.assertEqual(len(review_warnings(docs,date(2026,10,17),30,{'topic.md':'after'})),1)

    def test_historical_report_is_not_a_current_review_reminder(self):
        docs=[{'path':'report.md','status':'historical','reviewed_on':'2025-01-01'}]
        self.assertEqual(review_warnings(docs,date(2026,10,17),30),[])

    def test_broken_local_schema_reference_is_rejected(self):
        with self.assertRaises(KeyError):
            check_refs({'$ref':'#/$defs/Absent','$defs':{}})
