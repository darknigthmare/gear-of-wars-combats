"""Check projectile coverage and dated reports without changing prior deliveries."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image


PROJECT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("gears_inventory_v9", PROJECT / "src/consolidate_inventory.py")
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


class ProjectileInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        root_patch = patch.object(inventory, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.addCleanup(self.temp.cleanup)
        self.roster = [{"id": "hero", "name": "Hero", "source_game": "Fixture game", "skins": [
            {"id": "hero_costume", "name": "Fixture costume"}
        ]}]
        for path, value in {
            "data/roster.json": self.roster,
            "data/bosses.json": [{"id": "boss_fixture", "name": "Fixture boss"}],
            "data/stages.json": [{"id": "stage_fixture", "name": "Fixture stage"}],
            "production/asset_registry.json": {"assets": []},
            "production/history/initial_2026-11-19/assets_manifest.json": [],
        }.items():
            self.write(path, value)
        template = self.root / "src/gallery_template.html"
        template.parent.mkdir(parents=True)
        template.write_text((PROJECT / "src/gallery_template.html").read_text(encoding="utf-8"), encoding="utf-8")
        for subject, category in (("hero", "character"), ("hero_costume", "costume"),
                                  ("boss_fixture", "boss"), ("stage_fixture", "stage")):
            asset_path = f"assets/fixtures/{subject}.png"
            self.image(asset_path)
            self.write(f"data/generation_v7/{subject}.json", {
                "subject_id": subject, "category": category, "asset_path": asset_path,
                "character_id": "hero" if category == "costume" else None,
                "costume_id": subject if category == "costume" else None,
                "variant": "Fixture edition", "status": "generated", "pass_date": "2026-11-20",
            })

    def write(self, path, value):
        inventory.write_json(self.root / path, value)

    def image(self, relative):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        # Technical fixture only; never copied into the production asset set.
        image = Image.new("RGBA", (8, 8), (0, 0, 0, 0))
        image.putpixel((4, 4), (255, 255, 255, 255))
        image.save(path)

    def test_projectiles_flow_through_catalog_manifest_missing_gallery_and_report(self):
        baseline = inventory.build_inventory()
        historical_report = self.root / "docs/production/CONSOLIDATION_2026-11-20.md"
        historical_bytes = historical_report.read_bytes()
        historical_record = self.root / "data/generation_v7/hero.json"
        historical_record_bytes = historical_record.read_bytes()
        self.write("data/production_catalog_v9.json", {"projectiles": [
            {"id": "projectile_bolt", "name": "Fixture bolt", "source_game": "Fixture game",
             "weapon_id": "fixture_bow", "source_weapon": "Fixture bow"},
            {"id": "projectile_missing", "name": "Missing projectile"},
            {"id": "projectile_blocked", "name": "Blocked projectile"},
        ]})
        self.image("assets/projectiles_v9/bolt.png")
        self.write("data/generation_v9/bolt.json", {
            "projectile_id": "projectile_bolt", "category": "projectile",
            "asset_path": "assets/projectiles_v9/bolt.png", "variant": "Fixture game",
            "pass_date": "2026-11-25", "status": "generated_reference_pending_validation",
        })
        self.write("data/generation_v9/missing.json", {
            "subject_id": "projectile_missing", "category": "projectile", "status": "generated",
            "asset_path": "assets/not-returned.png", "pass_date": "2026-11-25",
        })
        self.write("data/generation_v9/blocked.json", {
            "subject_id": "projectile_blocked", "category": "projectile", "status": "blocked",
            "pass_date": "2026-11-25",
        })
        result = inventory.build_inventory()
        totals = result["totals"]
        for key in baseline["totals"]:
            if key.startswith(("character", "roster", "production_character", "catalog_character", "costume", "boss", "stage", "reused_character")):
                self.assertEqual(totals[key], baseline["totals"][key], key)
        self.assertEqual(totals["projectile_catalog_entries"], 3)
        self.assertEqual(totals["projectiles_with_reference"], 1)
        self.assertEqual(totals["projectiles_missing"], 2)
        self.assertEqual(totals["projectile_png_files"], 1)
        self.assertEqual(totals["active_png_files"], 5)
        self.assertEqual(result["missing"]["projectiles"], ["projectile_missing", "projectile_blocked"])
        self.assertEqual(result["warnings"], [])

        coverage = inventory.read_json(self.root / "production/coverage.json")
        self.assertEqual(coverage["snapshot_date"], "2026-11-25")
        self.assertEqual(coverage["additional_references"], [])
        self.assertEqual(coverage["projectiles"][0]["source_weapon"], "Fixture bow")
        self.assertEqual(coverage["projectiles"][0]["selected_path"], "assets/projectiles_v9/bolt.png")
        self.assertEqual(coverage["projectiles"][2]["visual_status"], "generation_blocked")
        manifest = inventory.read_json(self.root / "production/asset_manifest.json")
        projectile = next(asset for asset in manifest["assets"] if asset["category"] == "projectile")
        self.assertEqual(projectile["purpose"], "projectile_static")
        self.assertEqual(projectile["origin_batch"], "generation_v9_2026-11-25")
        self.assertFalse(projectile["canonical_fidelity_validated"])
        self.assertFalse(projectile["production_ready"])
        self.assertEqual(projectile["prototype_integration"], "not_integrated")
        old_asset = next(asset for asset in manifest["assets"] if asset["subject_id"] == "hero")
        self.assertEqual(old_asset["origin_batch"], "generation_v7_2026-11-20")
        legacy = inventory.read_json(self.root / "data/assets_manifest.json")
        self.assertEqual(next(asset for asset in legacy if asset["subject_id"] == "projectile_bolt")["category"], "Référence de projectile")

        gallery = (self.root / "Galerie_Personnages.html").read_text(encoding="utf-8")
        self.assertIn('data-category="projectile"', gallery)
        self.assertIn('href="docs/production/CONSOLIDATION_2026-11-25.md"', gallery)
        payload = re.search(r'<script id="catalog-data" type="application/json">(.*?)</script>', gallery, re.S).group(1)
        self.assertEqual(json.loads(payload)["coverage"]["projectiles"], coverage["projectiles"])
        self.assertNotIn("__SNAPSHOT_DATE__", gallery)
        self.assertNotIn("__REPORT_PATH__", gallery)
        self.assertIn("Projectiles avec une référence statique | 1 / 3", (self.root / coverage["report_path"]).read_text(encoding="utf-8"))
        self.assertEqual(historical_report.read_bytes(), historical_bytes)
        self.assertEqual(historical_record.read_bytes(), historical_record_bytes)

    def test_optional_projectile_catalog_preserves_legacy_counts_and_date(self):
        result = inventory.build_inventory()
        for key in ("projectile_catalog_entries", "projectiles_with_reference", "projectiles_missing", "projectile_png_files"):
            self.assertEqual(result["totals"][key], 0)
        self.assertEqual(result["missing"]["projectiles"], [])
        self.assertEqual(result["totals"]["active_png_files"], 4)
        self.assertEqual(inventory.read_json(self.root / "production/coverage.json")["snapshot_date"], "2026-11-20")

    def test_same_day_versioned_pass_preserves_published_report(self):
        inventory.build_inventory()
        old_report = self.root / "docs/production/CONSOLIDATION_2026-11-20.md"
        old_bytes = old_report.read_bytes()
        record_path = "data/generation_v13/boss_fixture.json"
        self.write(record_path, {
            "subject_id": "boss_fixture", "category": "boss", "status": "research_needed",
            "pass_date": "2026-11-20", "notes": ["No new image."],
        })
        inventory.build_inventory()
        coverage = inventory.read_json(self.root / "production/coverage.json")
        expected = "docs/production/CONSOLIDATION_2026-11-20_V13.md"
        self.assertEqual(coverage["report_path"], expected)
        self.assertTrue((self.root / expected).is_file())
        self.assertEqual(old_report.read_bytes(), old_bytes)
        self.assertIn(f'href="{expected}"', (self.root / "Galerie_Personnages.html").read_text())
        attempt = coverage["bosses"][0]["last_generation_attempt"]
        self.assertEqual(attempt["record"], record_path)
        self.assertEqual(attempt["record_sha256"], inventory.hashlib.sha256((self.root / record_path).read_bytes()).hexdigest())
        inventory.build_inventory(report_suffix="V13")
        inventory.build_inventory()  # The manifest wrapper uses this form.
        self.assertEqual(inventory.read_json(self.root / "production/coverage.json")["report_path"], expected)
        self.assertEqual(old_report.read_bytes(), old_bytes)
        with self.assertRaisesRegex(ValueError, "Report suffix"):
            inventory.build_inventory(report_suffix="../V13")

    def test_projectile_identity_collision_and_wrong_category_are_rejected(self):
        self.write("data/production_catalog_v9.json", {"projectiles": [{"id": "hero", "name": "Conflicting identity"}]})
        with self.assertRaisesRegex(ValueError, "unique across categories"):
            inventory.load_production_catalog(self.roster)
        self.write("data/production_catalog_v9.json", {"projectiles": [{"id": "projectile_bolt", "name": "Bolt"}]})
        self.write("data/generation_v9/wrong.json", {"subject_id": "projectile_bolt", "category": "character"})
        with self.assertRaisesRegex(ValueError, "Category mismatch"):
            inventory.build_inventory()

    def test_dates_come_from_valid_record_dates_instead_of_the_system_clock(self):
        self.assertEqual(inventory.record_date({"pass_date": "2026-11-25", "created_at": "2026-11-26T00:00:00Z"}), "2026-11-25")
        self.assertEqual(inventory.record_date({"generated_at": "2026-11-24T23:40:00Z"}), "2026-11-24")
        self.assertIsNone(inventory.record_date({"pass_date": "2026-99-25", "date": "2026-11-25not-a-date"}))
        self.assertIsNone(inventory.record_date({"created_at": None}))
        self.write("data/generation_v9/pending.json", {
            "subject_id": "projectile_pending", "category": "projectile", "status": "pending",
            "created_at": "2026-11-25T06:30:00Z",
        })
        inventory.build_inventory()
        self.assertEqual(inventory.read_json(self.root / "production/coverage.json")["snapshot_date"], "2026-11-25")


if __name__ == "__main__":
    unittest.main()
