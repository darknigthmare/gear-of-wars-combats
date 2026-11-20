"""Regression checks for production scope and explicit costume attribution."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image


SOURCE = Path(__file__).resolve().parents[1] / "src/consolidate_inventory.py"
SPEC = importlib.util.spec_from_file_location("gears_inventory", SOURCE)
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


class ProductionInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.root_patch = patch.object(inventory, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.addCleanup(self.temp.cleanup)
        self.roster = [
            {"id": "marcus", "name": "Marcus Fenix", "source_game": "Gears 1", "skins": [
                {"id": "marcus_skin_01", "name": "Gears 3", "source_url": "https://example.test/gears3"}
            ]},
            {"id": "dizzy", "name": "Dizzy Wallin", "source_game": "Gears 2", "skins": []},
        ]
        for path, value in {
            "data/roster.json": self.roster,
            "data/bosses.json": [], "data/stages.json": [],
            "production/asset_registry.json": {"assets": []},
            "production/history/initial_2026-11-19/assets_manifest.json": [],
        }.items():
            self.write(path, value)
        template = self.root / "src/gallery_template.html"
        template.parent.mkdir(parents=True)
        template.write_text("__CATALOG_DATA__")

    def write(self, path, value):
        inventory.write_json(self.root / path, value)

    def image(self, path):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        # Tiny technical fixture, never a production or generated-art asset.
        image = Image.new("RGBA", (8, 8), (0, 0, 0, 0))
        image.putpixel((4, 4), (255, 255, 255, 255))
        image.save(target)

    def test_explicit_costume_subject_does_not_replace_parent_or_grow_gameplay_roster(self):
        self.write("data/production_catalog_v6.json", {
            "schema_version": "1.0",
            "characters": [{"id": "anthony", "name": "Anthony Carmine", "source_game": "Gears 1"}],
            "costumes": [{"id": "marcus_skin_01", "name": "Marcus — Gears 3", "character_id": "marcus"}],
            "bosses": [{"id": "boss_berserker", "name": "Berserker"}],
            "stages": [{"id": "stage_canals", "name": "Canals"}],
        })
        for filename, record in {
            "anthony": {"id": "anthony_gow1", "subject_id": "anthony", "category": "character", "purpose": "reference_fullbody"},
            "marcus_costume": {"id": "marcus_gow3", "subject_id": "marcus_skin_01", "category": "costume", "character_id": "marcus", "costume_id": "marcus_skin_01", "purpose": "costume_reference_fullbody"},
            "canals": {"id": "canals_master", "subject_id": "stage_canals", "category": "stage", "purpose": "stage_master"},
        }.items():
            asset_path = f"assets/v6/{filename}.png"
            self.image(asset_path)
            self.write(f"data/generation_v6/{filename}.json", {**record, "asset_path": asset_path, "status": "generated", "variant": "Reference candidate"})
        self.write("data/generation_v6/boss_without_file.json", {"id": "boss_berserker", "category": "boss", "status": "generated", "asset_path": "assets/not-returned.png"})
        self.write("data/generation_v5/dizzy.json", {"id": "dizzy", "status": "blocked", "asset_path": None})

        result = inventory.build_inventory()
        totals = result["totals"]
        self.assertEqual(totals["roster_characters"], 2)
        self.assertEqual(totals["characters_with_reference"], 0)
        self.assertEqual(totals["production_character_entries"], 1)
        self.assertEqual(totals["production_characters_with_reference"], 1)
        self.assertEqual(totals["costume_catalog_entries"], 1)
        self.assertEqual(totals["costumes_with_reference"], 1)
        self.assertEqual(totals["bosses_with_reference"], 0)
        self.assertEqual(totals["stages_with_reference"], 1)
        self.assertEqual(totals["active_png_files"], 3)
        self.assertEqual(totals["canonical_fidelity_validated"], 0)
        roster = inventory.read_json(self.root / "data/roster.json")
        self.assertEqual([row["id"] for row in roster], ["marcus", "dizzy"])
        self.assertIsNone(roster[0]["visual_reference_path"])
        coverage = inventory.read_json(self.root / "production/coverage.json")
        self.assertEqual(coverage["characters"][1]["visual_status"], "generation_blocked")
        self.assertEqual(coverage["costumes"][0]["selected_path"], "assets/v6/marcus_costume.png")
        manifest = inventory.read_json(self.root / "production/asset_manifest.json")
        costume = next(asset for asset in manifest["assets"] if asset["category"] == "costume")
        self.assertEqual(costume["subject_id"], "marcus_skin_01")
        self.assertEqual(costume["character_id"], "marcus")
        self.assertEqual(costume["purpose"], "costume_reference_fullbody")
        stage = next(asset for asset in manifest["assets"] if asset["category"] == "stage")
        self.assertEqual(stage["purpose"], "stage_master")

    def test_optional_catalog_keeps_inherited_costumes_unattributed(self):
        catalog = inventory.load_production_catalog(self.roster)
        self.assertEqual(catalog["characters"], [])
        self.assertEqual(len(catalog["costumes"]), 1)
        self.assertEqual(catalog["costumes"][0]["character_id"], "marcus")
        result = inventory.build_inventory()
        self.assertEqual(result["missing"]["costumes"], ["marcus_skin_01"])

    def test_duplicate_or_unknown_costume_parent_is_rejected(self):
        self.write("data/production_catalog_v6.json", {"costumes": [{"id": "unknown_skin", "name": "Unknown", "character_id": "not_in_catalog"}]})
        with self.assertRaisesRegex(ValueError, "Unknown costume character"):
            inventory.load_production_catalog(self.roster)
        self.write("data/production_catalog_v6.json", {"characters": [{"id": "extra", "name": "One"}, {"id": "extra", "name": "Two"}]})
        with self.assertRaisesRegex(ValueError, "Duplicate production catalog id"):
            inventory.load_production_catalog(self.roster)

    def test_costume_cannot_use_parent_character_as_its_subject(self):
        self.write("data/generation_v6/wrong_identity.json", {"id": "bad", "subject_id": "marcus", "category": "costume", "character_id": "marcus"})
        with self.assertRaisesRegex(ValueError, "Category mismatch"):
            inventory.collect_assets({"assets": []}, self.roster, inventory.load_production_catalog(self.roster))


if __name__ == "__main__":
    unittest.main()
