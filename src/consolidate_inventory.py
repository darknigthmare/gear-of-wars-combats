"""Reconcile generated references without claiming finished animations or 1:1 fidelity.

Run from any directory: python src/consolidate_inventory.py
Only inventories, roster reference fields, the gallery and the current report are
written. Historical records, source images and generation result files stay intact.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-11-20"
CATALOG_CATEGORIES = (("characters", "character"), ("costumes", "costume"),
                      ("bosses", "boss"), ("stages", "stage"),
                      ("projectiles", "projectile"))


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def record_date(record: dict) -> str | None:
    """Read the production date without changing the historical source record."""
    for key in ("pass_date", "generated_at", "completed_at", "date", "created_at"):
        value = record.get(key)
        if not isinstance(value, str) or not re.match(r"^\d{4}-\d{2}-\d{2}(?:$|T| )", value):
            continue
        try:
            return date.fromisoformat(value[:10]).isoformat()
        except ValueError:
            continue
    return None


def local_path(relative: str) -> Path:
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f"Asset path outside repository: {relative}")
    return path


def notes_from(record: dict) -> list[str]:
    notes = []
    for key in ("qa_notes", "visual_notes", "notes"):
        value = record.get(key, [])
        notes.extend(value if isinstance(value, list) else [value] if isinstance(value, str) else [])
    for key in ("qa", "visual_review"):
        value = record.get(key, {})
        if isinstance(value, dict):
            for subkey in ("observations", "remaining_checks", "notes", "limitations", "visual_findings", "technical_caveats"):
                entry = value.get(subkey, [])
                notes.extend(entry if isinstance(entry, list) else [entry] if isinstance(entry, str) else [])
    return list(dict.fromkeys(x for x in notes if isinstance(x, str) and x))


def urls_from(value) -> list[str]:
    urls = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in ("url", "source_url", "page_url", "page", "image_url", "image", "source_page", "source_image") and isinstance(child, str) and child.startswith("https://"):
                urls.append(child)
            elif key in ("source_urls", "sources", "references", "source_references"):
                urls.extend(urls_from(child))
    elif isinstance(value, list):
        for child in value:
            if isinstance(child, str) and child.startswith("https://"):
                urls.append(child)
            else:
                urls.extend(urls_from(child))
    return list(dict.fromkeys(urls))


def merge_catalog_rows(base: list[dict], additions: list[dict]) -> list[dict]:
    """Merge by explicit identity, preserving original ordering and avoiding duplicates."""
    merged = {row["id"]: dict(row) for row in base}
    seen = set()
    for row in additions:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"] or not row.get("name"):
            raise ValueError("Production catalog rows require a non-empty id and name")
        if row["id"] in seen:
            raise ValueError(f"Duplicate production catalog id: {row['id']}")
        seen.add(row["id"])
        merged[row["id"]] = {**merged.get(row["id"], {}), **row}
    return list(merged.values())


def load_production_catalog(roster: list[dict]) -> dict:
    """Keep the gameplay roster separate from production extensions and costumes.

    A costume is only illustrated when an asset explicitly carries its identity.
    A different appearance of the same character never fills that costume slot.
    """
    categories = tuple(key for key, _ in CATALOG_CATEGORIES)
    catalog = {key: [] for key in categories}
    versions = []
    for path in (ROOT / "data").glob("production_catalog_v*.json"):
        match = re.fullmatch(r"production_catalog_v(\d+)\.json", path.name)
        if match:
            versions.append((int(match.group(1)), path))
    for _, path in sorted(versions):
        addition = read_json(path)
        if not isinstance(addition, dict):
            raise ValueError(f"{path.name} must contain an object")
        for key in categories:
            if not isinstance(addition.get(key, []), list):
                raise ValueError(f"Production catalog {key} must be a list: {path.name}")
            catalog[key] = merge_catalog_rows(catalog[key], addition.get(key, []))
    roster_ids = {row["id"] for row in roster}
    production_characters = [row for row in merge_catalog_rows([], catalog.get("characters", [])) if row["id"] not in roster_ids]
    inherited_costumes = []
    for character in roster:
        for skin in character.get("skins", []):
            inherited_costumes.append({
                **skin, "name": character["name"] + " — " + skin["name"],
                "costume_name": skin["name"], "character_id": character["id"],
                "parent_id": character["id"], "character_name": character["name"],
                "source_game": skin.get("source_game", skin["name"]),
                "priority": skin.get("priority", character.get("priority", "P1")),
                "source_urls": urls_from(skin), "catalog_origin": "roster_skin",
                "notes": ["Apparence du catalogue initial ; aucune image attribuée sans identité de costume explicite."],
            })
    result = {
        "characters": production_characters,
        "costumes": merge_catalog_rows(inherited_costumes, catalog.get("costumes", [])),
        "bosses": merge_catalog_rows(read_json(ROOT / "data/bosses.json"), catalog.get("bosses", [])),
        "stages": merge_catalog_rows(read_json(ROOT / "data/stages.json"), catalog.get("stages", [])),
        "projectiles": catalog["projectiles"],
    }
    identities = [row["id"] for row in roster] + [row["id"] for rows in result.values() for row in rows]
    duplicates = [key for key, count in Counter(identities).items() if count > 1]
    if duplicates:
        raise ValueError("Catalog identities must be unique across categories: " + ", ".join(duplicates))
    character_names = {row["id"]: row["name"] for row in roster + production_characters}
    for row in result["costumes"]:
        parent = row.get("character_id") or row.get("parent_id")
        if parent and parent not in character_names:
            raise ValueError(f"Unknown costume character {parent}: {row['id']}")
        if parent:
            row["character_id"] = parent
            row["character_name"] = character_names[parent]
    return result


def inspect_image(relative: str) -> dict:
    path = local_path(relative)
    with Image.open(path) as image:
        image.load()
        width, height = image.size
        alpha = image.getchannel("A") if "A" in image.getbands() else None
        alpha_info = None
        if alpha is not None:
            histogram = alpha.histogram()
            bbox = alpha.point(lambda value: 255 if value >= 128 else 0).getbbox()
            alpha_info = {
                "min": alpha.getextrema()[0], "max": alpha.getextrema()[1],
                "fully_transparent_fraction": round(histogram[0] / (width * height), 6),
                "near_opaque_fraction_alpha_ge_240": round(sum(histogram[240:]) / (width * height), 6),
                "subject_bbox_alpha_ge_128": list(bbox) if bbox else None,
                "subject_margins_ltrb_px": [bbox[0], bbox[1], width - bbox[2], height - bbox[3]] if bbox else None,
            }
        return {
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "size_bytes": path.stat().st_size, "width": width, "height": height,
            "mode": image.mode, "format": image.format, "alpha": alpha_info,
            "has_transparency": alpha is not None and alpha.getextrema()[0] < 255,
            "technical_status": "image_decoded_and_alpha_measured",
        }


def collect_assets(registry: dict, roster: list[dict], catalog: dict | None = None):
    aliases = registry.get("character_id_aliases", {})
    names = {row["id"]: row["name"] for row in roster}
    categories = {row["id"]: "character" for row in roster}
    for key, category in CATALOG_CATEGORIES:
        for row in (catalog or {}).get(key, []):
            names[row["id"]] = row["name"]
            categories[row["id"]] = category
    seeds = {row["path"]: dict(row) for row in registry["assets"]}
    attempts = {}
    warnings = []
    # Later passes are discovered by their real result files, without changing them.
    for directory in sorted((ROOT / "data").glob("generation_v*")):
        match = re.fullmatch(r"generation_v(\d+)", directory.name)
        if not match or int(match.group(1)) < 4:
            continue
        generation = int(match.group(1))
        for path in sorted(directory.glob("*.json")):
            record = read_json(path)
            if not isinstance(record, dict):
                continue
            subject = record.get("subject_id") or (record.get("costume_id") if record.get("category") == "costume" else None) or (record.get("projectile_id") if record.get("category") == "projectile" else None) or record.get("character_id") or record.get("id")
            if not subject:
                continue
            subject = aliases.get(subject, subject)
            category = record.get("category") or categories.get(subject) or ("boss" if subject.startswith("boss_") else "stage" if subject.startswith("stage_") else "projectile" if subject.startswith("projectile_") else "character")
            if category not in {category for _, category in CATALOG_CATEGORIES}:
                raise ValueError(f"Unknown asset category {category}: {path}")
            if subject in categories and categories[subject] != category:
                raise ValueError(f"Category mismatch for {subject}: {category} instead of {categories[subject]}")
            relative_record = str(path.relative_to(ROOT))
            relative_asset = record.get("asset_path") or record.get("output_path") or record.get("path")
            status = record.get("status") or ("generated" if record.get("has_image") else "blocked" if record.get("error") else "unknown")
            attempt = {"record": relative_record, "generation": generation, "status": status, "category": category,
                       "has_file": bool(relative_asset and local_path(relative_asset).is_file()),
                       "record_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            pass_date = record_date(record)
            if pass_date:
                attempt["pass_date"] = pass_date
            previous = attempts.get(subject)
            if previous is None or generation >= previous["generation"]:
                attempts[subject] = attempt
            if generation < 5 or not relative_asset or not local_path(relative_asset).is_file():
                continue
            variant = record.get("variant") or record.get("requested_variant") or record.get("source_game") or "Variante à documenter"
            if not isinstance(variant, str):
                variant = json.dumps(variant, ensure_ascii=False)
            seeds[relative_asset] = {
                "path": relative_asset, "subject_id": subject,
                "category": category,
                "name": record.get("name") or names.get(subject, subject),
                "source_variant": variant,
                "purpose": record.get("purpose") or {"costume": "costume_reference_fullbody", "stage": "stage_master", "projectile": "projectile_static"}.get(category, "reference_fullbody"),
                "character_id": record.get("character_id") or (subject if category == "character" else None),
                "costume_id": record.get("costume_id") or (subject if category == "costume" else None),
                "origin_batch": directory.name + "_" + (pass_date or DATE),
                "metadata_records": [relative_record], "source_urls": urls_from(record),
                "qa_notes": notes_from(record), "quality_state": record.get("quality_state", "candidate"),
                "variant_relation": record.get("variant_relation", "target_version_candidate"),
                "selection_priority": record.get("selection_priority", 30 + generation),
            }
    # Never silently omit a newly copied PNG that has not received its result JSON.
    for path in sorted((ROOT / "assets").rglob("*.png")):
        relative = str(path.relative_to(ROOT))
        if relative in seeds:
            continue
        subject = next((key for key in sorted(names, key=len, reverse=True) if path.stem.startswith(key + "_")), None)
        warnings.append(f"Métadonnées à compléter : {relative}")
        seeds[relative] = {
            "path": relative, "subject_id": subject or path.stem,
            "category": categories[subject] if subject else "unassigned",
            "name": names.get(subject, path.stem), "source_variant": "Variante non documentée",
            "purpose": "reference_fullbody", "origin_batch": "unregistered",
            "metadata_records": [], "source_urls": [],
            "qa_notes": ["Fichier présent, mais métadonnées de génération à compléter ; aucune sélection automatique prioritaire."],
            "quality_state": "metadata_pending", "variant_relation": "edition_unverified", "selection_priority": -1,
        }
    assets = []
    for relative, seed in sorted(seeds.items()):
        if not local_path(relative).is_file():
            raise FileNotFoundError(f"Registered asset missing: {relative}")
        asset = dict(seed)
        asset["asset_id"] = re.sub(r"[^a-z0-9]+", "_", relative.lower()).strip("_")
        asset.update(inspect_image(relative))
        asset.update(canonical_fidelity_validated=False, production_ready=False,
                     animation_status="not_produced", selection_status="alternate_candidate")
        assets.append(asset)
    archived = []
    for path in sorted((ROOT / "rejected_candidates").rglob("*.png")):
        relative = str(path.relative_to(ROOT))
        archived.append({"path": relative, "status": "archived_not_active",
                         "reason": registry.get("archived_revision_notes", {}).get(relative, "Version historique écartée ; voir les sélections et QA de generation_v2."),
                         **inspect_image(relative)})
    return assets, archived, attempts, warnings


def apply_costume_asset_links(assets: list[dict], catalog: dict) -> None:
    """Attribute an existing character PNG to a documented costume without copying it.

    The image identity, generation record and quality findings remain unchanged.
    A hash and parent check prevent an attribution from surviving a replaced image
    or silently crossing to another character. Edition matching is an explicit
    audited decision recorded in the mapping, not inferred from the filename.
    """
    # Versioned mappings add new attributions without rewriting the V7 audit.
    mappings = []
    paths = sorted((ROOT / "data").glob("costume_asset_links_v*.json"),
                   key=lambda item: int(re.search(r"_v(\d+)\.json$", item.name).group(1))
                   if re.search(r"_v(\d+)\.json$", item.name) else -1)
    for path in paths:
        relative_mapping = str(path.relative_to(ROOT))
        mapping = read_json(path)
        if not isinstance(mapping, dict) or not isinstance(mapping.get("links"), list):
            raise ValueError(f"Costume asset mapping requires a links list: {relative_mapping}")
        mappings.extend((relative_mapping, link) for link in mapping["links"])
    by_path = {asset["path"]: asset for asset in assets}
    costumes = {row["id"]: row for row in catalog["costumes"]}
    seen = set()
    for relative_mapping, link in mappings:
        if not isinstance(link, dict):
            raise ValueError("Costume asset links must be objects")
        relative = link.get("asset_path")
        if relative in seen:
            raise ValueError(f"Duplicate costume asset link: {relative}")
        seen.add(relative)
        asset = by_path.get(relative)
        if asset is None:
            raise ValueError(f"Costume link asset is not active: {relative}")
        costume_id = link.get("costume_id")
        costume = costumes.get(costume_id)
        if costume is None:
            raise ValueError(f"Unknown linked costume: {costume_id}")
        parent = costume.get("character_id") or costume.get("parent_id")
        if asset["category"] != "character" or asset["subject_id"] != parent or link.get("character_id") != parent:
            raise ValueError(f"Costume link character mismatch: {relative} -> {costume_id}")
        if asset["purpose"] == "presentation":
            raise ValueError(f"Costume link cannot use a presentation image: {relative}")
        if link.get("sha256") != asset["sha256"]:
            raise ValueError(f"Costume link image hash mismatch: {relative}")
        record = link.get("source_record_path")
        if record not in asset.get("metadata_records", []) or not local_path(record).is_file():
            raise ValueError(f"Costume link lacks its image provenance record: {relative}")
        if not isinstance(link.get("rationale"), str) or not link["rationale"].strip():
            raise ValueError(f"Costume link requires an edition rationale: {relative}")
        evidence = link.get("additional_evidence_paths", [])
        if not isinstance(evidence, list) or any(not isinstance(item, str) or not local_path(item).is_file() for item in evidence):
            raise ValueError(f"Costume link has missing supporting evidence: {relative}")
        if asset.get("costume_id") not in (None, costume_id):
            raise ValueError(f"Conflicting costume attribution: {relative}")
        asset["costume_id"] = costume_id
        # This relation belongs to the costume row. Do not overwrite the relation
        # to the character's base costume, which can still be another edition.
        asset["costume_variant_relation"] = "target_version_candidate"
        asset["costume_attribution"] = {
            "mapping_path": relative_mapping,
            "source_record_path": record,
            "additional_evidence_paths": evidence,
            "rationale": link["rationale"],
            "source_urls": link.get("source_urls", []),
            "caveats": link.get("caveats", []),
            "canonical_fidelity_validated": False,
        }


def relation_for(asset: dict, category: str) -> str:
    if category == "costume":
        return asset.get("costume_variant_relation", asset["variant_relation"])
    return asset["variant_relation"]


def select_reference(assets: list[dict]):
    # A copied PNG is a physical file, but cannot satisfy a catalog identity
    # until a provenance record establishes which edition and subject it is.
    eligible = [a for a in assets if a["purpose"] != "presentation"
                and a.get("quality_state") != "metadata_pending"]
    return max(eligible, key=lambda a: (a["selection_priority"], a["path"]), default=None)


def make_coverage(rows, category, assets, attempts):
    result = []
    for row in rows:
        references = [a for a in assets if
                      (a["category"] == category and a["subject_id"] == row["id"])
                      or (category == "costume" and a.get("costume_id") == row["id"])]
        selected = select_reference(references)
        targets = [a for a in references if relation_for(a, category) == "target_version_candidate" and a["purpose"] != "presentation"]
        selected_target = select_reference(targets)
        if selected:
            selected["selection_status"] = "selected_reference"
        last = attempts.get(row["id"])
        status = "reference_available" if selected else ("generation_blocked" if last and ("block" in last["status"] or "refus" in last["status"]) else "generation_pending" if last and last["status"] in ("requested", "pending", "generating") else "missing")
        entry = {
            "id": row["id"], "name": row["name"], "category": category,
            "requested_source_game": row.get("source_game", ""),
            "requested_base_costume": row.get("base_costume"),
            "priority": row.get("priority", "P1"), "faction": row.get("faction", ""),
            "character_id": row.get("character_id"), "character_name": row.get("character_name"),
            "parent_id": row.get("parent_id"), "source_urls": urls_from(row),
            "catalog_notes": notes_from(row), "catalog_scope": row.get("catalog_scope", "production_catalog"),
            "implementation_status": row.get("implementation_status", "Référence de production ; intégration jouable non attestée"),
            "has_visual_reference": bool(selected), "visual_status": status,
            "selected_asset_id": selected["asset_id"] if selected else None,
            "selected_path": selected["path"] if selected else None,
            "selected_source_variant": selected["source_variant"] if selected else None,
            "selected_variant_relation": relation_for(selected, category) if selected else None,
            "asset_ids": [a["asset_id"] for a in references],
            "target_version_candidate_available": bool(selected_target),
            "target_version_candidate_path": selected_target["path"] if selected_target else None,
            "canonical_fidelity_validated": False, "animation_status": "not_produced",
            "last_generation_attempt": last,
        }
        if category == "stage":
            entry["parallax_status"] = "separate_layers_not_validated"
        if category == "projectile":
            entry["weapon_id"] = row.get("weapon_id")
            entry["source_weapon"] = row.get("source_weapon")
            entry["implementation_status"] = row.get("implementation_status", "Sprite statique de projectile ; comportement et collisions non attestés")
        if category == "character":
            row["visual_reference_path"] = entry["selected_path"]
            row["visual_reference_variant"] = entry["selected_source_variant"]
            row["visual_reference_variant_relation"] = entry["selected_variant_relation"]
            row["reference_asset_paths"] = [a["path"] for a in references]
            # Keep the legacy base field only for a candidate targeting that version.
            # An alternate edition cannot silently satisfy the requested base costume.
            if selected_target:
                row["base_reference_path"] = selected_target["path"]
                row["base_reference_variant"] = selected_target["source_variant"]
            else:
                row.pop("base_reference_path", None)
                row.pop("base_reference_variant", None)
            row["target_version_candidate_available"] = bool(selected_target)
            row["canonical_fidelity_validated"] = False
            row["animation_status"] = "Animations dessinées à produire"
            if not selected:
                row["art_status"] = "Aucune référence générée ; dernier essai refusé par le générateur" if status == "generation_blocked" else "Aucune référence générée ; à produire"
            elif selected["quality_state"] == "correction_required":
                row["art_status"] = "Référence en pied récupérée ; corrections visuelles identifiées ; animations à produire"
            elif selected["variant_relation"] != "target_version_candidate":
                row["art_status"] = "Référence candidate : " + selected["source_variant"] + " ; édition cible et fidélité exacte non validées ; animations à produire"
            else:
                row["art_status"] = "Référence en pied candidate disponible ; fidélité 1:1 non validée ; animations à produire"
        result.append(entry)
    return result


def write_report(coverage, assets, archived):
    totals = coverage["totals"]
    missing = ", ".join(row["name"] for row in coverage["characters"] if not row["has_visual_reference"]) or "Aucun personnage du roster sans référence."
    recent = [a for a in assets if (match := re.match(r"generation_v(\d+)", a["origin_batch"])) and int(match.group(1)) >= 5]
    recent_rows = "\n".join(f"| {a['name']} | {a['source_variant']} | [PNG](../../{a['path']}) |" for a in recent) or "| Aucune nouvelle sortie retenue | — | — |"
    selected_rows = "\n".join(
        f"| {row['name']} | {row['selected_source_variant'] or 'À produire'} | " +
        (f"[PNG](../../{row['selected_path']})" if row["selected_path"] else "Aucun fichier") + " |"
        for row in coverage["characters"])
    report = f"""# Consolidation — Gears of War Combats — {coverage['snapshot_date']}

## État vérifié des fichiers

Les anciennes passes ont été réunies avec les nouvelles sorties réellement présentes. Les nombres ci-dessous proviennent du recalcul de [l’inventaire](../../production/asset_manifest.json) et de [la couverture](../../production/coverage.json). Ils remplacent les chiffres des rapports historiques pour le suivi courant.

| Contenu | Quantité |
| --- | ---: |
| Personnages possédant au moins une référence | **{totals['characters_with_reference']} / {totals['roster_characters']}** |
| Personnages sans référence | **{totals['characters_missing']}** |
| Personnages supplémentaires du catalogue avec une référence | {totals['production_characters_with_reference']} / {totals['production_character_entries']} |
| Costumes avec une attribution visuelle explicite | {totals['costumes_with_reference']} / {totals['costume_catalog_entries']} |
| PNG actifs de personnages, alternatives et présentations incluses | {totals['character_png_files']} |
| PNG actifs classés comme costumes | {totals['costume_png_files']} |
| Boss avec une référence | {totals['bosses_with_reference']} / {totals['boss_catalog_entries']} |
| Fiches d’arènes associées à un master | {totals['stages_with_reference']} / {totals['stage_catalog_entries']} |
| Masters de décor, Ephyra complémentaire inclus | {totals['stage_png_files']} |
| Projectiles avec une référence statique | {totals['projectiles_with_reference']} / {totals['projectile_catalog_entries']} |
| PNG actifs de projectiles | {totals['projectile_png_files']} |
| PNG actifs uniques | {totals['active_png_files']} |
| Anciennes versions écartées conservées séparément | {len(archived)} |
| Personnages certifiés conformes 1:1 | **0** |
| Ensembles d’animations dessinées finalisés | **0** |

**Personnages encore sans image : {missing}**

La présence d’un PNG signifie une référence statique disponible, pas un personnage jouable ni un costume certifié. [La galerie complète](../../Galerie_Personnages.html) affiche les {totals['roster_characters']} personnages du roster de conception, les {totals['production_character_entries']} extensions de personnages, les {totals['costume_catalog_entries']} costumes, les {totals['boss_catalog_entries']} boss, les {totals['stage_catalog_entries']} arènes et les {totals['projectile_catalog_entries']} projectiles, avec des cartes explicites pour les manquants. Les extensions de production ne modifient pas le roster du moteur. Ephyra reste un master complémentaire, sans attribution arbitraire à une arène précise. Une référence de projectile ne valide ni sa trajectoire, ni ses collisions, ni son effet à l’impact.

Les costumes hérités des fiches initiales restent sans attribution tant qu’un `costume_id` explicite n’est pas fourni. Cela signifie une liaison visuelle à vérifier, et non nécessairement une image à régénérer. Les mappings `data/costume_asset_links_v*.json` sont lus dans leur ordre numérique et conservent l’audit [V7](../../data/costume_asset_links_v7.json). Ils rattachent les images existantes à leur costume après vérification du personnage, de la provenance et de l’empreinte ; ils ne dupliquent aucun PNG et ne certifient aucune fidélité. Un master de décor ne vaut pas validation de ses calques de parallaxe séparés.

## Ce qui a été récupéré

- Le corpus initial : bible, prototype, données de conception, 16 personnages représentés et deux décors. Les fichiers copiés lors des deux premières passes sont identiques ; les doubles copies binaires n’augmentent pas les comptes.
- La passe v4 : neuf références de personnages et quatre boss. Kestrel était généré mais resté hors d’`assets` ; il est récupéré et contrôlé, avec [un constat distinct](../../data/generation_v4/recovery_kestrel_2026-11-20.json).
- Le lot de reprise : 14 références sélectionnées, ses sources, ses prompts et son rapport visuel. Clayton v02, Theron v02 et Ukkon v02 sont conservés ; leurs trois anciennes versions sont archivées dans `rejected_candidates/characters_20261119/`.
- Les six candidats v4 recouvrant des personnages du lot de reprise sont conservés et consultables comme alternatives. Ils ne sont pas six personnages supplémentaires.

## Nouvelles sorties présentes

| Sujet | Variante demandée | Fichier |
| --- | --- | --- |
{recent_rows}

Les refus et résultats en cours sont conservés dans les dossiers `data/generation_v*/`. Un refus n’est jamais compté comme une image. Le recalcul accepte un résultat ayant un chemin de fichier valide sans dépendre d’un unique libellé de statut.

## Sélection et limites de fidélité

- **Marcus :** les fichiers historiques sont étiquetés Ultimate Edition dans leur manifeste ; la cible du roster demeure le costume original de 2006. Cette différence reste visible et n’est pas effacée par le regroupement.
- **Theron :** un nouveau candidat classique casqué vise le costume de 2006 et devient la référence de consultation ; le Gears 3 tête nue reste une alternative distincte. Les références du nouveau candidat sont une figurine NECA de 2008 et un portrait Gears 2 : elles ne certifient pas l’édition exacte du modèle original de 2006. La cible de production et la preuve disponible restent donc séparées.
- **Hoffman :** l’armure classique est la référence de consultation sélectionnée, avec édition non certifiée. Le candidat v4 visant Gears 5 Operation 6 est également conservé avec ses réserves ; leurs identités de variante ne sont pas fusionnées.
- **Clayton et Ukkon :** les corrections inspectées du lettrage `GRUB KILLER` et de la longueur des montants sont conservées dans les versions sélectionnées.
- **Warden :** les Breaker Maces nécessitent une comparaison rapprochée au modèle de jeu. Les réserves historiques sur Skorge, Del, Lizzie et Reyna restent des corrections ouvertes.
- Les corps principaux sont en pied, mais plusieurs marges sont étroites. Les mesures d’alpha et les réserves figurent par fichier. Les RGB colorés sous un alpha nul ne constituent pas un fond opaque.

La galerie indique l’édition réellement documentée pour chaque image. Les asymétries, visages, armes, détails hors champ des références, vues strictement latérales, pivots et clips de combat restent à contrôler ou à produire.

## Personnages et référence de consultation

| Personnage | Variante sélectionnée | Référence |
| --- | --- | --- |
{selected_rows}

## Historique et documents

- Les données initiales de roster/manifeste et l’ancienne galerie sont figées dans `production/history/initial_2026-11-19/`.
- Le lot de reprise est conservé intégralement dans `production/history/reprise_2026-11-19/` pour ses documents, journaux, références et scripts historiques. Les images actives sont conservées une seule fois à leurs chemins de production.
- [Le rapport visuel du 19 novembre](VISUAL_QA_2026-11-19.md) reste une preuve de contrôle datée ; ses chiffres de passe ne décrivent pas le total consolidé.
- Les PDF, DOCX et XLSX de `livrables/` sont des **instantanés du 19 novembre 2026**, conservés sans modification binaire. Ils ne sont pas présentés comme des exports actualisés de cette consolidation.
- Le prototype conserve son périmètre de démonstration. Les images explicitement liées dans son asset map sont signalées comme intégrées en référence statique ; cela ne crée pas d’animation dessinée. Ajouter une illustration à l’inventaire seul ne l’intègre pas automatiquement à son moteur.

## Recalcul après génération

```bash
python src/consolidate_inventory.py{' --report-suffix ' + coverage['report_suffix'] if coverage.get('report_suffix') else ''}
```

Cette commande vérifie les fichiers, recalcule empreintes, dimensions, alpha et comptes, réconcilie les références du roster, puis reconstruit l’inventaire et la galerie autonome. Elle lit les résultats des passes v5 et suivantes sans les modifier. `src/build_asset_manifest.py` appelle également ce recalcul avant de renouveler la file de production. `src/finalize_generation_v2.py` reste un script historique de v2, pas la commande courante de consolidation.

Ce rapport décrit les fichiers préparés. Il ne constitue pas une preuve de publication GitHub, qui doit être vérifiée séparément.
"""
    path = ROOT / coverage["report_path"]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")


def build_inventory(*, report_suffix: str | None = None):
    # Several passes can share one date. An explicit version keeps a later
    # consolidation from overwriting the already published daily report.
    if report_suffix and not re.fullmatch(r"V[1-9]\d*", report_suffix):
        raise ValueError("Report suffix must be a version such as V13")
    registry = read_json(ROOT / "production/asset_registry.json")
    roster = read_json(ROOT / "data/roster.json")
    catalog = load_production_catalog(roster)
    assets, archived, attempts, warnings = collect_assets(registry, roster, catalog)
    snapshot_date = max([DATE] + [attempt["pass_date"] for attempt in attempts.values() if attempt.get("pass_date")])
    if report_suffix is None:
        # The manifest wrapper also calls this function without arguments.
        # Keep an existing versioned report, or version a newer same-day pass.
        previous_path = ROOT / "production/coverage.json"
        previous = read_json(previous_path) if previous_path.is_file() else {}
        report_suffix = previous.get("report_suffix", "")
        previous_attempts = [row.get("last_generation_attempt") or {} for group in
                             ("characters", "production_characters", "costumes", "bosses", "stages", "projectiles", "additional_references")
                             for row in previous.get(group, [])]
        previous_generation = max([0] + [attempt.get("generation", 0) for attempt in previous_attempts])
        current_generation = max([0] + [attempt["generation"] for attempt in attempts.values()])
        if current_generation > previous_generation and (report_suffix or previous.get("snapshot_date") == snapshot_date):
            report_suffix = f"V{current_generation}"
        if report_suffix and not re.fullmatch(r"V[1-9]\d*", report_suffix):
            raise ValueError("Stored report suffix must be a version such as V13")
    apply_costume_asset_links(assets, catalog)
    prototype_map_path = ROOT / "prototype/asset-map.json"
    prototype_paths = set()
    if prototype_map_path.is_file():
        for value in read_json(prototype_map_path).values():
            if isinstance(value, str):
                prototype_paths.add(value if value.startswith("assets/") else "assets/" + value)
    for asset in assets:
        asset["prototype_integration"] = "static_reference" if asset["path"] in prototype_paths else "not_integrated"
    characters = make_coverage(roster, "character", assets, attempts)
    for row in characters:
        row["catalog_scope"] = "gameplay_design_roster"
    production_characters = make_coverage(catalog["characters"], "character", assets, attempts)
    for row in production_characters:
        row["catalog_scope"] = "production_extension"
        row["scope_note"] = "Extension du catalogue de production ; aucun combattant jouable ajouté automatiquement."
    costumes = make_coverage(catalog["costumes"], "costume", assets, attempts)
    bosses = make_coverage(catalog["bosses"], "boss", assets, attempts)
    stages = make_coverage(catalog["stages"], "stage", assets, attempts)
    projectiles = make_coverage(catalog["projectiles"], "projectile", assets, attempts)
    catalog_ids = {row["id"] for row in characters + production_characters + costumes + bosses + stages + projectiles}
    additional_references = []
    for subject in sorted({a["subject_id"] for a in assets} - catalog_ids):
        subject_assets = [a for a in assets if a["subject_id"] == subject]
        first = select_reference(subject_assets) or subject_assets[0]
        synthetic = {"id": subject, "name": first["name"], "source_game": first["source_variant"]}
        extra = make_coverage([synthetic], first["category"], assets, attempts)[0]
        extra["catalog_member"] = False
        extra["scope_note"] = ("Master complémentaire ; aucune fiche d’arène précise attribuée sans preuve." if first["category"] == "stage" else
                               "Référence complémentaire hors catalogue ; identité et rattachement à documenter.")
        additional_references.append(extra)
    totals = {
        "roster_characters": len(characters), "characters_with_reference": sum(c["has_visual_reference"] for c in characters),
        "characters_missing": sum(not c["has_visual_reference"] for c in characters),
        "production_character_entries": len(production_characters),
        "production_characters_with_reference": sum(c["has_visual_reference"] for c in production_characters),
        "character_catalog_entries": len(characters) + len(production_characters),
        "catalog_characters_with_reference": sum(c["has_visual_reference"] for c in characters + production_characters),
        "catalog_characters_missing": sum(not c["has_visual_reference"] for c in characters + production_characters),
        "character_png_files": sum(a["category"] == "character" for a in assets),
        "costume_catalog_entries": len(costumes), "costumes_with_reference": sum(c["has_visual_reference"] for c in costumes),
        "costumes_without_explicit_reference": sum(not c["has_visual_reference"] for c in costumes),
        "costume_png_files": sum(a["category"] == "costume" for a in assets),
        "reused_character_pngs_for_costumes": sum(a["category"] == "character" and bool(a.get("costume_attribution")) for a in assets),
        "boss_catalog_entries": len(bosses), "bosses_with_reference": sum(c["has_visual_reference"] for c in bosses),
        "boss_png_files": sum(a["category"] == "boss" for a in assets),
        "stage_catalog_entries": len(stages), "stages_with_reference": sum(c["has_visual_reference"] for c in stages),
        "stage_png_files": sum(a["category"] == "stage" for a in assets),
        "projectile_catalog_entries": len(projectiles), "projectiles_with_reference": sum(c["has_visual_reference"] for c in projectiles),
        "projectiles_missing": sum(not c["has_visual_reference"] for c in projectiles),
        "projectile_png_files": sum(a["category"] == "projectile" for a in assets),
        "additional_reference_groups": len(additional_references),
        "active_png_files": len(assets), "unique_active_png_sha256": len({a["sha256"] for a in assets}),
        "archived_png_files": len(archived), "canonical_fidelity_validated": 0, "completed_animation_sets": 0,
    }
    counts = Counter(a["asset_id"] for a in assets)
    if any(count != 1 for count in counts.values()):
        raise ValueError("Duplicate asset identifiers")
    coverage = {
        "schema_version": "1.3", "project": "Gears of War Combats", "snapshot_date": snapshot_date,
        "report_path": f"docs/production/CONSOLIDATION_{snapshot_date}{'_' + report_suffix if report_suffix else ''}.md",
        "report_suffix": report_suffix,
        "generator": "src/consolidate_inventory.py", "totals": totals,
        "characters": characters, "production_characters": production_characters, "costumes": costumes,
        "bosses": bosses, "stages": stages, "projectiles": projectiles,
        "additional_references": additional_references,
        "missing": {"characters": [c["id"] for c in characters if not c["has_visual_reference"]],
                    "production_characters": [c["id"] for c in production_characters if not c["has_visual_reference"]],
                    "costumes": [c["id"] for c in costumes if not c["has_visual_reference"]],
                    "bosses": [c["id"] for c in bosses if not c["has_visual_reference"]],
                    "stages": [c["id"] for c in stages if not c["has_visual_reference"]],
                    "projectiles": [c["id"] for c in projectiles if not c["has_visual_reference"]]},
        "warnings": warnings,
        "limits": "Comptage de fichiers de référence ; ni certification 1:1, ni animation finalisée, ni intégration automatique au moteur, ni preuve de publication.",
    }
    manifest = {"schema_version": "1.3", "project": "Gears of War Combats", "snapshot_date": snapshot_date,
                "generator": "src/consolidate_inventory.py", "counts": totals, "assets": assets,
                "archived_assets": archived, "limits": coverage["limits"]}
    write_json(ROOT / "production/asset_manifest.json", manifest)
    write_json(ROOT / "production/coverage.json", coverage)
    write_json(ROOT / "data/roster.json", roster)
    # Preserve the list-shaped legacy manifest for existing consumers.
    old = {a["path"]: a for a in read_json(ROOT / "production/history/initial_2026-11-19/assets_manifest.json")}
    compatible = []
    for asset in assets:
        previous = old.get(asset["path"], {})
        row = dict(previous)
        row.update(id=previous.get("id", asset["asset_id"]), name=asset["name"], path=asset["path"],
                   category={"character": "Référence de personnage", "costume": "Référence de costume", "boss": "Référence de boss", "stage": "Décor complet", "projectile": "Référence de projectile"}.get(asset["category"], "À classer"),
                   source_game=asset["source_variant"], character_id=asset["subject_id"] if asset["category"] == "character" else asset.get("character_id"),
                   costume_id=asset.get("costume_id"), purpose=asset["purpose"],
                   subject_id=asset["subject_id"], width_px=asset["width"], height_px=asset["height"],
                   has_transparency=asset["has_transparency"], produced=True, sha256=asset["sha256"],
                   status="Référence candidate", fidelity_check="À corriger" if asset["quality_state"] == "correction_required" else "À valider",
                   fidelity_notes=" ".join(asset["qa_notes"]), ready_for_animation=False,
                   integration_check="Intégré au prototype en référence statique" if asset["prototype_integration"] == "static_reference" else "Référence de production",
                   canonical_fidelity_validated=False, variant_relation=asset["variant_relation"],
                   selection_status=asset["selection_status"], unified_asset_id=asset["asset_id"])
        compatible.append(row)
    write_json(ROOT / "data/assets_manifest.json", compatible)
    write_report(coverage, assets, archived)
    template = (ROOT / "src/gallery_template.html").read_text(encoding="utf-8")
    payload = json.dumps({"coverage": coverage, "assets": assets, "archived_assets": archived}, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    rendered = template.replace("__CATALOG_DATA__", payload).replace("__SNAPSHOT_DATE__", snapshot_date).replace("__REPORT_PATH__", coverage["report_path"])
    (ROOT / "Galerie_Personnages.html").write_text(rendered, encoding="utf-8")
    return {"status": "passed", "totals": totals, "missing": coverage["missing"], "warnings": warnings}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-suffix", default=None, help="Versioned report suffix, e.g. V13; by default preserve the current version or version a newer same-day pass")
    args = parser.parse_args()
    print(json.dumps(build_inventory(report_suffix=args.report_suffix), ensure_ascii=False, indent=2))
