"""Protect audited costume links from stale images and cross-edition leakage."""
from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image


SOURCE = Path(__file__).resolve().parents[1] / "src/consolidate_inventory.py"
SPEC = importlib.util.spec_from_file_location("gears_inventory_v7", SOURCE)
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


class CostumeAttributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        root_patch = patch.object(inventory, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.addCleanup(self.temp.cleanup)
        self.roster = [{"id": "marcus", "name": "Marcus", "source_game": "Gears 1", "skins": [
            {"id": "marcus_g3", "name": "Gears 3"}
        ]}]
        self.asset_path = "assets/fixture.png"
        self.record_path = "data/generation_v7/fixture.json"
        image_path = self.root / self.asset_path
        image_path.parent.mkdir(parents=True)
        # Technical test fixture only; never used as production artwork.
        Image.new("RGBA", (4, 4), (20, 30, 40, 255)).save(image_path)
        self.sha = hashlib.sha256(image_path.read_bytes()).hexdigest()
        for path, value in {
            "data/roster.json": self.roster,
            "data/bosses.json": [],
            "data/stages.json": [],
            "production/asset_registry.json": {"assets": []},
            "production/history/initial_2026-11-19/assets_manifest.json": [],
            self.record_path: {
                "id": "marcus_g3_reference", "subject_id": "marcus", "category": "character",
                "asset_path": self.asset_path, "variant": "Gears 3",
                "variant_relation": "alternate_version", "quality_state": "correction_required",
                "purpose": "reference_fullbody", "status": "generated",
            },
        }.items():
            inventory.write_json(self.root / path, value)
        template = self.root / "src/gallery_template.html"
        template.parent.mkdir(parents=True)
        template.write_text("__CATALOG_DATA__")
        self.link = {
            "asset_path": self.asset_path, "sha256": self.sha,
            "character_id": "marcus", "costume_id": "marcus_g3",
            "source_record_path": self.record_path,
            "rationale": "The recorded edition is Gears 3; the character base remains Gears 1.",
            "source_urls": [], "caveats": ["Existing art correction remains open."],
        }

    def write_links(self, links):
        inventory.write_json(self.root / "data/costume_asset_links_v7.json", {"schema_version": "1.0", "links": links})

    def test_link_reuses_one_image_without_promoting_the_base_edition_or_quality(self):
        self.write_links([self.link])
        result = inventory.build_inventory()
        self.assertEqual(result["totals"]["active_png_files"], 1)
        self.assertEqual(result["totals"]["characters_with_reference"], 1)
        self.assertEqual(result["totals"]["costumes_with_reference"], 1)
        self.assertEqual(result["totals"]["costume_png_files"], 0)
        self.assertEqual(result["totals"]["reused_character_pngs_for_costumes"], 1)
        coverage = inventory.read_json(self.root / "production/coverage.json")
        character = coverage["characters"][0]
        costume = coverage["costumes"][0]
        self.assertFalse(character["target_version_candidate_available"])
        self.assertEqual(character["selected_variant_relation"], "alternate_version")
        self.assertTrue(costume["target_version_candidate_available"])
        self.assertEqual(costume["selected_variant_relation"], "target_version_candidate")
        asset = inventory.read_json(self.root / "production/asset_manifest.json")["assets"][0]
        self.assertEqual(asset["quality_state"], "correction_required")
        self.assertFalse(asset["canonical_fidelity_validated"])
        self.assertFalse(asset["production_ready"])
        self.assertEqual(asset["metadata_records"], [self.record_path])

    def test_stale_hash_wrong_parent_and_wrong_provenance_are_rejected(self):
        for change, message in [
            ({"sha256": "0" * 64}, "image hash mismatch"),
            ({"character_id": "dom"}, "character mismatch"),
            ({"source_record_path": "data/roster.json"}, "provenance record"),
            ({"costume_id": "unknown_skin"}, "Unknown linked costume"),
            ({"asset_path": "assets/not-present.png"}, "not active"),
        ]:
            with self.subTest(change=change):
                self.write_links([{**self.link, **change}])
                with self.assertRaisesRegex(ValueError, message):
                    inventory.build_inventory()

    def test_new_pass_mapping_keeps_the_earlier_audit_unchanged(self):
        self.write_links([])
        previous = self.root / "data/costume_asset_links_v7.json"
        previous_bytes = previous.read_bytes()
        inventory.write_json(self.root / "data/costume_asset_links_v9.json", {"links": [self.link]})
        result = inventory.build_inventory()
        self.assertEqual(result["totals"]["active_png_files"], 1)
        self.assertEqual(result["totals"]["costumes_with_reference"], 1)
        self.assertEqual(previous.read_bytes(), previous_bytes)
        asset = inventory.read_json(self.root / "production/asset_manifest.json")["assets"][0]
        self.assertEqual(asset["costume_attribution"]["mapping_path"], "data/costume_asset_links_v9.json")
        self.write_links([self.link])
        with self.assertRaisesRegex(ValueError, "Duplicate costume asset link"):
            inventory.build_inventory()

    def test_duplicate_links_and_presentation_images_cannot_fill_costume_slots(self):
        self.write_links([self.link, self.link])
        with self.assertRaisesRegex(ValueError, "Duplicate costume asset link"):
            inventory.build_inventory()
        self.write_links([self.link])
        record = inventory.read_json(self.root / self.record_path)
        record["purpose"] = "presentation"
        inventory.write_json(self.root / self.record_path, record)
        with self.assertRaisesRegex(ValueError, "presentation image"):
            inventory.build_inventory()

    def test_catalog_passes_merge_numerically_without_duplicate_identities(self):
        inventory.write_json(self.root / "data/production_catalog_v6.json", {
            "characters": [{"id": "extra", "name": "Original", "source_game": "Gears 3"}],
            "bosses": [{"id": "boss_existing", "name": "Existing boss"}],
        })
        inventory.write_json(self.root / "data/production_catalog_v7.json", {
            "characters": [{"id": "extra", "name": "Pass 7"}, {"id": "new", "name": "New character"}],
        })
        inventory.write_json(self.root / "data/production_catalog_v10.json", {
            "characters": [{"id": "extra", "name": "Pass 10"}],
        })
        catalog = inventory.load_production_catalog(self.roster)
        self.assertEqual([row["id"] for row in catalog["characters"]], ["extra", "new"])
        self.assertEqual(catalog["characters"][0]["name"], "Pass 10")
        self.assertEqual(catalog["characters"][0]["source_game"], "Gears 3")
        self.assertEqual(catalog["bosses"][0]["id"], "boss_existing")
        self.assertEqual(len(catalog["costumes"]), 1)
        self.assertEqual(len(self.roster), 1)
        inventory.write_json(self.root / "data/production_catalog_v10.json", {
            "bosses": [{"id": "extra", "name": "Conflicting boss identity"}],
        })
        with self.assertRaisesRegex(ValueError, "unique across categories"):
            inventory.load_production_catalog(self.roster)


if __name__ == "__main__":
    unittest.main()
