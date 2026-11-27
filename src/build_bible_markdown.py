"""Assemble the current readable bible without rewriting historical binaries.

Run after consolidate_inventory.py. Authored chapters remain the source of truth;
only heading levels and relative Markdown links are adjusted in the assembly.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
VERSION = "V13"
OUTPUT = ROOT / f"livrables/Gears_of_War_Combats_Bible_{VERSION.lower()}.md"
MANIFEST = ROOT / f"docs/production/BIBLE_BUILD_{VERSION}.json"
CHAPTERS = [
    ("Vision et systemes de combat", "docs/core_bible.md"),
    ("Roster, armes et movesets", "docs/roster_movesets.md"),
    ("Boss, arenes et campagne", "docs/boss_stages_story.md"),
    ("Guide commun et deux extensions adaptes a Gears", "docs/combat_extensions.md"),
]


def read_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def relative_link(path: Path) -> str:
    return Path(os.path.relpath(path, OUTPUT.parent)).as_posix()


def safe_cell(value) -> str:
    if value is None:
        return "—"
    if isinstance(value, (list, dict)):
        value = json.dumps(value, ensure_ascii=False)
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def table(headers, rows) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    lines += ["| " + " | ".join(safe_cell(cell) for cell in row) + " |" for row in rows]
    return "\n".join(lines)


def adapt_markdown(source: Path) -> str:
    """Keep prose intact; preserve link targets when chapters change directory."""
    text = source.read_text(encoding="utf-8").strip()

    def link(match):
        target = match.group(1)
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            return match.group(0)
        destination = (source.parent / parsed.path).resolve() if parsed.path else source
        if not destination.is_relative_to(ROOT):
            raise ValueError(f"Link outside repository in {source.name}: {target}")
        if not destination.exists():
            raise ValueError(f"Missing source link in {source.name}: {target}")
        rewritten = urlunsplit(("", "", relative_link(destination), parsed.query, parsed.fragment))
        return "](" + rewritten + ")"

    text = re.sub(r"\]\(([^\s)]+)\)", link, text)
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = marker.group(1)[0]
            elif marker.group(1)[0] == fence:
                fence = None
            lines.append(line)
            continue
        if fence is None:
            heading = re.match(r"^(#{1,6}) (.*)$", line)
            if heading:
                line = "#" * min(6, len(heading.group(1)) + 2) + " " + heading.group(2)
        lines.append(line)
    return "\n".join(lines)


def source_section(title: str, relative: str, note: str = "") -> str:
    source = ROOT / relative
    intro = f"## {title}\n\nSource complète : [{source.name}]({relative_link(source)})."
    if note:
        intro += "\n\n" + note
    return intro + "\n\n" + adapt_markdown(source)


def current_catalog(coverage: dict) -> str:
    sections = [
        "## Catalogue courant de production",
        "Ce catalogue inclut les ajouts postérieurs au noyau de conception. Une ligne documentée ne rend pas le personnage jouable. Les liens d'images renvoient à des candidats : édition, portion représentée, sources et limites doivent être lus dans les journaux de génération et dans la galerie.",
        "Les variantes d'édition, références partielles et candidats à corriger restent visibles. Le nombre d'images est distinct du nombre d'entrées couvertes : un PNG peut servir de référence à un personnage et à son costume, sans être compté deux fois.",
    ]
    groups = [
        ("Personnages", coverage["characters"] + coverage["production_characters"]),
        ("Costumes", coverage["costumes"]),
        ("Boss, creatures et machines", coverage["bosses"]),
        ("Stages", coverage["stages"]),
        ("Projectiles", coverage["projectiles"]),
    ]
    for title, entries in groups:
        rows = []
        for item in entries:
            selected = item.get("selected_path")
            reference = f"[PNG]({relative_link(ROOT / selected)})" if selected else "Absente"
            attempt = item.get("last_generation_attempt") or {}
            if attempt.get("record"):
                reference += f" · [journal]({relative_link(ROOT / attempt['record'])})"
            edition = item.get("selected_source_variant") or item.get("requested_source_game") or "À préciser"
            status = item.get("visual_status", "missing")
            relation = item.get("selected_variant_relation")
            if relation:
                status += " · " + relation
            rows.append([f"`{item['id']}`", item["name"], edition, reference, status])
        sections += ["### " + title, table(["Identifiant", "Sujet", "Édition de la référence ou cible", "Fichier", "État"], rows)]
    sections += [
        "### Donnees detaillees de conception",
        "Les fiches complètes sont conservées dans les données : [roster](../data/roster.json), [179 actions proposées](../data/movesets.json), [routes arcade](../data/arcade_routes.json), [campagne](../data/campaign.json), [boss](../data/bosses.json), [arènes](../data/stages.json) et [plan d'animation](../data/animation_plan.json). Les catalogues de production V6, V7 et V9 étendent ce périmètre sans modifier automatiquement ces fiches jouables.",
    ]
    return "\n\n".join(sections)


def requirements_section(matrix: dict) -> str:
    entries = matrix.get("requirements", matrix.get("rows", matrix.get("entries", [])))
    identifiers = [entry.get("requirement_id", entry.get("id")) for entry in entries]
    if len(entries) != 68 or set(identifiers) != {f"CG-{index:02}" for index in range(68)}:
        raise ValueError("Expected each source rubric CG-00 through CG-67 exactly once")
    sections = [
        "## Matrice complete des 68 rubriques",
        "Reprise intégrale du contenu de la matrice structurée, sans changement d'état. Les décisions documentaires, preuves et manques ci-dessous ne constituent pas un taux de fonctionnalités implémentées. Source : [GUIDE_REQUIREMENTS_V12.json](../docs/production/GUIDE_REQUIREMENTS_V12.json).",
    ]
    for entry in entries:
        ident = entry.get("id", entry.get("requirement_id", ""))
        title = entry.get("title", entry.get("section_title", entry.get("source_section_title", "")))
        sections.append(f"### {safe_cell(ident)} — {safe_cell(title)}")
        sections.append(table(["Champ source", "Valeur"], [[key, value] for key, value in entry.items()]))
    return "\n\n".join(sections)


def verify_current_records(coverage: dict) -> None:
    """Reject a stale same-day inventory, including records without images."""
    current = {}
    aliases = read_json("production/asset_registry.json").get("character_id_aliases", {})
    for path in sorted((ROOT / f"data/generation_{VERSION.lower()}").glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            continue
        subject = record.get("subject_id") or record.get("costume_id") or record.get("projectile_id") or record.get("character_id") or record.get("id")
        if subject:
            current[aliases.get(subject, subject)] = path
    rows = {row["id"]: row for group in ("characters", "production_characters", "costumes", "bosses", "stages", "projectiles", "additional_references") for row in coverage.get(group, [])}
    for subject, row in rows.items():
        attempt_path = (row.get("last_generation_attempt") or {}).get("record", "")
        if attempt_path.startswith(f"data/generation_{VERSION.lower()}/") and not (ROOT / attempt_path).is_file():
            raise ValueError(f"Coverage is stale for {subject}: generation record was removed")
    for subject, path in current.items():
        attempt = rows.get(subject, {}).get("last_generation_attempt") or {}
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if attempt.get("record") != str(path.relative_to(ROOT)) or attempt.get("record_sha256") != digest:
            raise ValueError(f"Coverage is stale for {subject}: rerun src/consolidate_inventory.py --report-suffix {VERSION}")
        record = json.loads(path.read_text(encoding="utf-8"))
        relative_asset = record.get("asset_path") or record.get("output_path") or record.get("path")
        if relative_asset and not (ROOT / relative_asset).is_file():
            raise ValueError(f"Missing generated asset for {subject}: {relative_asset}")


def build() -> dict:
    coverage = read_json("production/coverage.json")
    verify_current_records(coverage)
    snapshot = coverage["snapshot_date"]
    image_manifest = read_json("production/asset_manifest.json")
    if image_manifest["snapshot_date"] != snapshot or image_manifest["counts"] != coverage["totals"]:
        raise ValueError("Coverage and image manifest disagree: rerun src/consolidate_inventory.py")
    assets_by_path = {asset["path"]: asset for asset in image_manifest["assets"]}
    for path in (ROOT / f"data/generation_{VERSION.lower()}").glob("*.json"):
        record = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            continue
        if record.get("pass_date", "")[:10] > snapshot:
            raise ValueError("Coverage is stale: run src/consolidate_inventory.py before assembling the bible")
        relative_asset = record.get("asset_path") or record.get("output_path") or record.get("path")
        if relative_asset and (ROOT / relative_asset).is_file():
            actual_hash = hashlib.sha256((ROOT / relative_asset).read_bytes()).hexdigest()
            registered = assets_by_path.get(relative_asset)
            if registered is None or registered["sha256"] != actual_hash:
                raise ValueError(f"Image manifest is stale for {relative_asset}: rerun src/consolidate_inventory.py")
    totals = coverage["totals"]
    source_manifest = read_json("docs/guides/combat/source_manifest.json")
    for document in source_manifest["documents"]:
        source_bytes = (ROOT / "docs/guides/combat" / document["file"]).read_bytes()
        if len(source_bytes) != document["bytes"] or hashlib.sha256(source_bytes).hexdigest() != document["sha256"]:
            raise ValueError(f"Guide source differs from its provenance manifest: {document['file']}")
    matrix = read_json("docs/production/GUIDE_REQUIREMENTS_V12.json")
    acceptance_source = (ROOT / "docs/production/GUIDE_INTEGRATION_V12.md").read_text(encoding="utf-8")
    acceptance_ids = re.findall(r"^\| `(E0[12]-\d{2})` \|", acceptance_source, re.MULTILINE)
    expected_acceptance = {f"E01-{index:02}" for index in range(1, 19)} | {f"E02-{index:02}" for index in range(1, 23)}
    if len(acceptance_ids) != 40 or set(acceptance_ids) != expected_acceptance:
        raise ValueError("Expected each of the 18 + 22 extension acceptance cases exactly once")
    rows = [
        ["Personnages", totals["catalog_characters_with_reference"], totals["character_catalog_entries"], totals["catalog_characters_missing"]],
        ["Costumes", totals["costumes_with_reference"], totals["costume_catalog_entries"], totals["costumes_without_explicit_reference"]],
        ["Boss, créatures et machines", totals["bosses_with_reference"], totals["boss_catalog_entries"], totals["boss_catalog_entries"] - totals["bosses_with_reference"]],
        ["Stages", totals["stages_with_reference"], totals["stage_catalog_entries"], totals["stage_catalog_entries"] - totals["stages_with_reference"]],
        ["Projectiles", totals["projectiles_with_reference"], totals["projectile_catalog_entries"], totals["projectiles_missing"]],
    ]
    parts = [
        f"# Gears of War Combats — Bible de conception {VERSION}",
        f"**Darknigthmare · Consolidation du {snapshot} · Guide général et deux extensions inclus dans la conception.**",
        "Cette édition rassemble les chapitres de conception existants, le chapitre d'adaptation des guides, le catalogue visuel courant, les 68 rubriques de suivi et les 40 scénarios d'acceptation des extensions. Les copies exactes des trois guides sont conservées séparément avec leurs empreintes. Ce document ne remplace pas leurs originaux.",
        "## Lecture et perimetre",
        "La priorité de production actuelle reste les **assets fixes manquants, un sujet par image**. Les règles, valeurs, routes et chorégraphies proposées sont des adaptations pour un jeu de combat 2D. Les animations futures sont spécifiées dans les chapitres historiques et dans les extensions ; elles ne sont pas déclarées produites.",
        "Les chapitres initiaux décrivent le noyau de conception V1 : 36 personnages, 24 rencontres et 24 arènes. Le catalogue courant ci-dessous inclut les extensions de production postérieures. Les tableaux historiques gardent leur date et ne doivent pas être utilisés comme état courant.",
        "Le prototype conserve trois rencontres : Marcus contre RAAM, Berserker et King Raven de simulation. Les nouvelles assistances, le tag, les supers d'équipe et les règles d'accès décrites ici sont **conçus, pas implémentés ni testés dans le moteur par cette passe**. Le [README du prototype](../prototype/README.md) précise les fonctions réellement disponibles.",
        "## Sommaire",
        "\n".join([
            "- [État courant](#etat-courant)",
            "- [Vision et systèmes](#vision-et-systemes-de-combat)",
            "- [Roster, armes et movesets](#roster-armes-et-movesets)",
            "- [Boss, arènes et campagne](#boss-arenes-et-campagne)",
            "- [Guide et extensions adaptés à Gears](#guide-commun-et-deux-extensions-adaptes-a-gears)",
            "- [Catalogue de production](#catalogue-courant-de-production)",
            "- [Matrice des 68 rubriques](#matrice-complete-des-68-rubriques)",
            "- [Audit et 40 cas d'acceptation](#audit-et-cas-dacceptation-des-extensions)",
            "- [Premier lot historique](#annexe-historique-du-premier-lot)",
        ]),
        "## Etat courant",
        table(["Catégorie", "Avec référence", "Catalogue", "Sans référence"], rows),
        f"**{totals['active_png_files']} PNG actifs uniques** ; **{totals['archived_png_files']} révisions archivées** hors total actif. **{totals['canonical_fidelity_validated']} fidélités 1:1 certifiées** et **{totals['completed_animation_sets']} jeux d'animations complets**. Les catégories mesurent la présence d'au moins une référence, y compris partielle ou d'une autre édition ; elles ne mesurent pas la conformité finale. Ephyra reste un décor complémentaire, en dehors des 34 fiches de stages.",
        f"La provenance et les réserves figurent dans la [couverture courante](../production/coverage.json), le [manifeste des images](../production/asset_manifest.json), la [galerie](../Galerie_Personnages.html), le [listing {VERSION}](../docs/production/LISTING_{VERSION}.md) et la [reprise {VERSION}](../docs/production/REPRISE_{VERSION}.md). Les PDF, DOCX et classeurs V1 restent des livrables historiques ; cette bible {VERSION} est l'édition Markdown consolidée.",
        "### Trois sources originales conservees",
        table(["Document", "Octets", "SHA-256"], [
            [f"[{d['file']}](../docs/guides/combat/{d['file']})", d["bytes"], f"`{d['sha256']}`"] for d in source_manifest["documents"]
        ]),
    ]
    for title, relative in CHAPTERS:
        note = "Chapitre de conception conservé : ses nombres de contenu décrivent le noyau V1, sauf mentions V12 explicites." if relative != "docs/combat_extensions.md" else "Adaptation V12 complète. Les sources officielles étayent les identités et périodes ; les règles et chorégraphies nouvelles demeurent des créations du projet."
        parts.append(source_section(title, relative, note))
    parts += [
        current_catalog(coverage),
        requirements_section(matrix),
        source_section("Audit et cas dacceptation des extensions", "docs/production/GUIDE_INTEGRATION_V12.md"),
        source_section("Annexe historique du premier lot", "docs/delivery_status.md", "**Archive du 19 novembre 2026.** Les chiffres, tests rapportés et étapes futures de cette annexe sont ceux du premier lot ; voir l'état courant en tête de cette édition pour la production actuelle."),
        f"## Reconstruction de cette edition\n\nCommande : `python src/build_bible_markdown.py`, après `python src/consolidate_inventory.py --report-suffix {VERSION}`. Le [manifeste de construction](../docs/production/BIBLE_BUILD_{VERSION}.json) enregistre les sources et leurs SHA-256. Aucun texte original de guide ni PDF/DOCX historique n'est réécrit par ce script.",
    ]
    content = "\n\n".join(parts).rstrip() + "\n"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8")
    inputs = [p for _, p in CHAPTERS] + [
        "docs/production/GUIDE_INTEGRATION_V12.md", "docs/production/GUIDE_REQUIREMENTS_V12.json",
        "docs/guides/combat/source_manifest.json", "docs/delivery_status.md", "production/coverage.json",
        "production/asset_manifest.json",
    ] + ["docs/guides/combat/" + d["file"] for d in source_manifest["documents"]]
    result = {
        "schema_version": 1, "version": VERSION, "snapshot_date": snapshot,
        "generator": "src/build_bible_markdown.py", "output": str(OUTPUT.relative_to(ROOT)),
        "bytes": OUTPUT.stat().st_size, "words": len(content.split()),
        "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
        "source_chapters_included": 6, "requirements_included": 68, "acceptance_cases_included": 40,
        "runtime_implementation_claimed": False, "historical_binaries_rebuilt": False,
        "inputs": [{"path": relative, "sha256": hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()} for relative in inputs],
    }
    MANIFEST.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    result = build()
    print(json.dumps({key: result[key] for key in ["output", "snapshot_date", "bytes", "words", "sha256"]}, ensure_ascii=False))
