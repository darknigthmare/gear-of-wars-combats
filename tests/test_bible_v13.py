"""Prevent a same-day refusal or research update from vanishing in the bible."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SOURCE = Path(__file__).resolve().parents[1] / "src/build_bible_markdown.py"
SPEC = importlib.util.spec_from_file_location("gears_bible", SOURCE)
bible = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bible)


class BibleFreshnessTests(unittest.TestCase):
    def test_no_image_record_must_match_inventory_even_on_same_date(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(bible, "ROOT", Path(temp)):
            root = Path(temp)
            registry = root / "production/asset_registry.json"
            registry.parent.mkdir()
            registry.write_text('{"character_id_aliases": {}}')
            relative = "data/generation_v13/creature.json"
            record = root / relative
            record.parent.mkdir(parents=True)
            content = {"subject_id": "creature", "category": "boss", "pass_date": "2026-11-27",
                       "has_image": False, "status": "reference_research_pending"}
            record.write_text(json.dumps(content))
            coverage = {"bosses": [{"id": "creature", "last_generation_attempt": {
                "record": relative, "record_sha256": hashlib.sha256(record.read_bytes()).hexdigest()}}]}
            bible.verify_current_records(coverage)
            content["status"] = "blocked_prior_generator_refusal"
            record.write_text(json.dumps(content))
            with self.assertRaisesRegex(ValueError, "Coverage is stale for creature"):
                bible.verify_current_records(coverage)
            coverage["bosses"][0]["last_generation_attempt"]["record_sha256"] = hashlib.sha256(record.read_bytes()).hexdigest()
            bible.verify_current_records(coverage)
            with self.assertRaisesRegex(ValueError, "Coverage is stale for creature"):
                bible.verify_current_records({"bosses": []})
            record.unlink()
            with self.assertRaisesRegex(ValueError, "generation record was removed"):
                bible.verify_current_records(coverage)
            content["has_image"] = True
            content["asset_path"] = "assets/removed.png"
            record.write_text(json.dumps(content))
            coverage["bosses"][0]["last_generation_attempt"]["record_sha256"] = hashlib.sha256(record.read_bytes()).hexdigest()
            with self.assertRaisesRegex(ValueError, "Missing generated asset for creature"):
                bible.verify_current_records(coverage)


if __name__ == "__main__":
    unittest.main()
