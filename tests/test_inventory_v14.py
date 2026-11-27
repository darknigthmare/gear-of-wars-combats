"""An audited costume alias shares coverage, never another PNG or a QA result."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image


PROJECT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("gears_inventory_v14", PROJECT / "src/consolidate_inventory.py")
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


class CostumeReferenceAliasTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        root_patch = patch.object(inventory, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.addCleanup(self.temp.cleanup)
        self.game = "Fixture game: campaign"
        self.roster = [{"id": "hero", "name": "Hero", "skins": [
            {"id": "hero_costume", "name": "Campaign armor", "source_game": self.game},
            {"id": "hero_intro", "name": "Intro armor", "source_game": self.game},
        ]}]
        for path, value in {
            "data/roster.json": self.roster,
            "data/bosses.json": [],
            "data/stages.json": [],
            "production/asset_registry.json": {"assets": []},
            "production/history/initial_2026-11-19/assets_manifest.json": [],
        }.items():
            self.write(path, value)
        template = self.root / "src/gallery_template.html"
        template.parent.mkdir(parents=True)
        template.write_text((PROJECT / "src/gallery_template.html").read_text(encoding="utf-8"), encoding="utf-8")
        self.asset_path = "assets/fixtures/campaign_armor.png"
        image_path = self.root / self.asset_path
        image_path.parent.mkdir(parents=True)
        image = Image.new("RGBA", (8, 8), (0, 0, 0, 0))
        image.putpixel((4, 4), (255, 255, 255, 255))
        image.save(image_path)
        self.source_record = "data/generation_v13/hero_costume.json"
        self.alias_attempt = "data/generation_v13/hero_intro.json"
        self.write(self.source_record, {
            "subject_id": "hero_costume", "character_id": "hero", "costume_id": "hero_costume",
            "category": "costume", "asset_path": self.asset_path, "source_game": self.game,
            "variant": "Final campaign armor", "variant_relation": "target_version_candidate",
            "status": "generated_reference_pending_validation", "pass_date": "2026-11-27",
            "qa": {"observations": ["Fixture candidate; exact details remain unvalidated."]},
        })
        self.write(self.alias_attempt, {
            "subject_id": "hero_intro", "character_id": "hero", "costume_id": "hero_intro",
            "category": "costume", "status": "reference_research_pending",
            "has_image": False, "generation_attempted": False, "pass_date": "2026-11-27",
        })
        self.evidence_path = "docs/references/fixture_alias_review.md"
        evidence = self.root / self.evidence_path
        evidence.parent.mkdir(parents=True)
        evidence.write_text("Fixture review: both IDs request the final campaign intro armor.\n", encoding="utf-8")
        self.mapping_path = "data/costume_reference_aliases_v14.json"
        self.link = {
            "alias_id": "hero_intro", "canonical_id": "hero_costume", "character_id": "hero",
            "source_game": self.game, "asset_path": self.asset_path,
            "sha256": inventory.hashlib.sha256(image_path.read_bytes()).hexdigest(),
            "source_record_path": self.source_record, "evidence_record_path": self.evidence_path,
            "rationale": "The reviewed catalog IDs request the same final costume in the same edition.",
            "source_urls": ["https://example.test/fixture-final-model"],
            "caveats": ["This is a candidate, not a validated 1:1 sprite."],
        }
        self.write_mapping()

    def write(self, relative, value):
        inventory.write_json(self.root / relative, value)

    def write_mapping(self, *links):
        self.write(self.mapping_path, {"aliases": list(links) if links else [self.link]})

    def coverage(self):
        catalog = inventory.load_production_catalog(self.roster)
        assets, _, attempts, _ = inventory.collect_assets({"assets": []}, self.roster, catalog)
        return inventory.make_coverage(catalog["costumes"], "costume", assets, attempts), assets

    def assert_rejected_without_mutation(self, rows, assets, message):
        before_rows, before_assets = deepcopy(rows), deepcopy(assets)
        with self.assertRaisesRegex(ValueError, message):
            inventory.apply_costume_reference_aliases(rows, assets)
        self.assertEqual(rows, before_rows)
        self.assertEqual(assets, before_assets)

    def test_one_png_covers_two_explicit_ids_without_new_generation_or_qa_promotion(self):
        source_bytes = (self.root / self.source_record).read_bytes()
        attempt_bytes = (self.root / self.alias_attempt).read_bytes()
        image_bytes = (self.root / self.asset_path).read_bytes()
        result = inventory.build_inventory(report_suffix="V14")
        totals = result["totals"]
        self.assertEqual(totals["costume_catalog_entries"], 2)
        self.assertEqual(totals["costumes_with_reference"], 2)
        self.assertEqual(totals["costumes_without_explicit_reference"], 0)
        self.assertEqual(totals["costume_reference_aliases"], 1)
        self.assertEqual(totals["costume_png_files"], 1)
        self.assertEqual(totals["active_png_files"], 1)
        self.assertEqual(totals["canonical_fidelity_validated"], 0)
        coverage = inventory.read_json(self.root / "production/coverage.json")
        canonical, alias = coverage["costumes"]
        self.assertEqual(alias["id"], "hero_intro")
        self.assertEqual(alias["reference_alias_of"], "hero_costume")
        for field in ("selected_asset_id", "selected_path", "asset_ids", "selected_source_variant",
                      "selected_variant_relation", "target_version_candidate_path"):
            self.assertEqual(alias[field], canonical[field])
        self.assertEqual(alias["last_generation_attempt"]["record"], self.alias_attempt)
        self.assertEqual(alias["last_generation_attempt"]["status"], "reference_research_pending")
        self.assertFalse(alias["last_generation_attempt"]["has_file"])
        self.assertFalse(alias["canonical_fidelity_validated"])
        self.assertEqual(alias["animation_status"], "not_produced")
        resolution = alias["reference_resolution"]
        self.assertEqual(resolution["mapping_path"], self.mapping_path)
        self.assertEqual(resolution["asset_sha256"], self.link["sha256"])
        self.assertEqual(resolution["source_record_path"], self.source_record)
        self.assertEqual(resolution["evidence_record_sha256"], inventory.hashlib.sha256((self.root / self.evidence_path).read_bytes()).hexdigest())
        self.assertEqual(resolution["caveats"], self.link["caveats"])
        self.assertTrue(any("aucune nouvelle génération" in note for note in alias["catalog_notes"]))
        assets = inventory.read_json(self.root / "production/asset_manifest.json")["assets"]
        self.assertEqual(len(assets), 1)
        self.assertEqual(assets[0]["subject_id"], "hero_costume")
        self.assertEqual(assets[0]["costume_id"], "hero_costume")
        self.assertEqual(assets[0]["metadata_records"], [self.source_record])
        self.assertFalse(assets[0]["canonical_fidelity_validated"])
        self.assertFalse(assets[0]["production_ready"])
        self.assertEqual(assets[0]["quality_state"], "candidate")
        self.assertEqual((self.root / self.source_record).read_bytes(), source_bytes)
        self.assertEqual((self.root / self.alias_attempt).read_bytes(), attempt_bytes)
        self.assertEqual((self.root / self.asset_path).read_bytes(), image_bytes)
        self.assertEqual(len(list((self.root / "assets").rglob("*.png"))), 1)

    def test_resolution_never_mutates_physical_asset_or_copies_qa_fields(self):
        rows, assets = self.coverage()
        canonical, alias = rows
        canonical["canonical_fidelity_validated"] = True
        canonical["production_ready"] = True
        alias.update(production_ready=False, fidelity_1to1_certified=False)
        original_canonical, original_assets = deepcopy(canonical), deepcopy(assets)
        original_attempt = deepcopy(alias["last_generation_attempt"])
        self.assertEqual(inventory.apply_costume_reference_aliases(rows, assets), 1)
        self.assertEqual(canonical, original_canonical)
        self.assertEqual(assets, original_assets)
        self.assertEqual(alias["last_generation_attempt"], original_attempt)
        self.assertFalse(alias["canonical_fidelity_validated"])
        self.assertFalse(alias["production_ready"])
        self.assertFalse(alias["fidelity_1to1_certified"])
        self.assertIsNot(alias["asset_ids"], canonical["asset_ids"])

    def test_no_mapping_never_infers_an_alias_from_similar_names(self):
        (self.root / self.mapping_path).unlink()
        rows, assets = self.coverage()
        rows[1]["name"] = rows[0]["name"]
        before_rows, before_assets = deepcopy(rows), deepcopy(assets)
        self.assertEqual(inventory.apply_costume_reference_aliases(rows, assets), 0)
        self.assertEqual(rows, before_rows)
        self.assertEqual(assets, before_assets)
        self.assertFalse(rows[1]["has_visual_reference"])

    def test_different_character_or_edition_is_rejected(self):
        for field, value, expected in (("character_id", "another_hero", "character mismatch"),
                                       ("requested_source_game", "Another edition", "edition mismatch")):
            for index in (0, 1):
                with self.subTest(field=field, row=index):
                    rows, assets = self.coverage()
                    rows[index][field] = value
                    self.assert_rejected_without_mutation(rows, assets, expected)
        self.link["source_game"] = "Another edition"
        self.write_mapping()
        self.assert_rejected_without_mutation(*self.coverage(), "edition mismatch")

    def test_changed_hash_or_actual_file_bytes_is_rejected(self):
        original = self.link["sha256"]
        self.link["sha256"] = "0" * 64
        self.write_mapping()
        self.assert_rejected_without_mutation(*self.coverage(), "image hash mismatch")
        self.link["sha256"] = original
        self.write_mapping()
        rows, assets = self.coverage()
        (self.root / self.asset_path).write_bytes(b"changed after the inventory read")
        self.assert_rejected_without_mutation(rows, assets, "image hash mismatch")

    def test_wrong_provenance_missing_evidence_or_empty_rationale_is_rejected(self):
        original = deepcopy(self.link)
        for field, value, expected in (
            ("source_record_path", self.alias_attempt, "provenance record"),
            ("evidence_record_path", "docs/references/absent.md", "supporting evidence"),
            ("rationale", "  ", "non-empty rationale"),
        ):
            with self.subTest(field=field):
                self.link = {**original, field: value}
                self.write_mapping()
                self.assert_rejected_without_mutation(*self.coverage(), expected)

    def test_unknown_identity_or_non_target_candidate_is_rejected(self):
        self.link["canonical_id"] = "absent_costume"
        self.write_mapping()
        self.assert_rejected_without_mutation(*self.coverage(), "Unknown costume")
        self.link["canonical_id"] = "hero_costume"
        self.write_mapping()
        for field, value in (("selected_variant_relation", "alternate_edition"),
                             ("target_version_candidate_available", False),
                             ("selected_path", "assets/another.png")):
            with self.subTest(field=field):
                rows, assets = self.coverage()
                rows[0][field] = value
                self.assert_rejected_without_mutation(rows, assets, "selected target candidate")

    def test_duplicate_aliases_across_versions_are_rejected(self):
        self.write("data/costume_reference_aliases_v15.json", {"aliases": [self.link]})
        self.assert_rejected_without_mutation(*self.coverage(), "Duplicate costume reference alias")

    def test_a_physical_asset_with_another_subject_cannot_supply_the_alias(self):
        rows, assets = self.coverage()
        assets[0]["subject_id"] = "another_costume"
        self.assert_rejected_without_mutation(rows, assets, "asset identity mismatch")

    def test_self_reference_chains_and_cycles_are_rejected(self):
        original = deepcopy(self.link)
        for links in (
            [{**original, "canonical_id": "hero_intro"}],
            [original, {**original, "alias_id": "hero_costume", "canonical_id": "third_costume"}],
            [original, {**original, "alias_id": "hero_costume", "canonical_id": "hero_intro"}],
        ):
            with self.subTest(links=links):
                self.write_mapping(*links)
                self.assert_rejected_without_mutation(*self.coverage(), "chain or cycle")

    def test_later_invalid_mapping_does_not_partially_resolve_an_earlier_alias(self):
        rows, assets = self.coverage()
        another = deepcopy(rows[1])
        another["id"] = "another_intro"
        rows.append(another)
        second = {**self.link, "alias_id": "another_intro", "evidence_record_path": "absent.md"}
        self.write_mapping(self.link, second)
        self.assert_rejected_without_mutation(rows, assets, "supporting evidence")


if __name__ == "__main__":
    unittest.main()
