"""Index individual character references without marking animation or fidelity complete."""
from pathlib import Path
import hashlib
import json
import html
from datetime import datetime, timezone
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/generation_v2'
OUT = ROOT.parent / 'outputs/gears_combats_characters_v2'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    roster = json.loads((ROOT / 'data/roster.json').read_text())
    manifest = json.loads((ROOT / 'data/assets_manifest.json').read_text())
    manifest = [x for x in manifest if not x.get('path', '').startswith('assets/characters_v2/')]
    queue = json.loads((DATA / 'queue.json').read_text())
    names = {c['id']: c for c in roster}
    produced = []
    missing = []
    for item in queue:
        path = ROOT / item['output_path']
        if not path.is_file():
            result_path = DATA / f"result_{item['id']}.json"
            if result_path.is_file():
                attempt = json.loads(result_path.read_text())
                item['status'] = 'blocked_by_image_system' if 'moderation_blocked' in (attempt.get('error') or '') else 'generation_failed'
            names[item['id']]['art_status'] = 'Non généré : refus du système d’image' if item.get('status') == 'blocked_by_image_system' else 'Non généré : génération échouée'
            missing.append(item['id'])
            continue
        image = Image.open(path)
        alpha = image.getchannel('A') if 'A' in image.getbands() else None
        transparent = alpha is not None and alpha.getextrema()[0] < 255
        record = {
            'id': path.stem,
            'character_id': item['id'],
            'name': item['name'],
            'category': 'Référence de personnage',
            'source_game': item['source_game'],
            'path': item['output_path'],
            'width_px': image.width,
            'height_px': image.height,
            'has_transparency': transparent,
            'alpha_required': True,
            'produced': True,
            'technical_check': 'Fichier, dimensions et canal alpha contrôlés',
            'fidelity_check': item.get('fidelity_status', 'À valider'),
            'fidelity_notes': item.get('fidelity_notes', 'Comparaison détaillée requise ; aucune certification 1:1.'),
            'integration_check': 'Référence de production ; non intégrée au jeu',
            'status': 'Référence générée',
            'limitations': 'Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.',
            'sha256': digest(path),
            'selected_revision': 'v3' if path.stem.endswith('_v3') else 'v2',
            'ready_for_animation': False,
        }
        produced.append(record)
        manifest.append(record)
        item['status'] = 'reference_generated'
        item['fidelity_status'] = record['fidelity_check']
        names[item['id']]['base_reference_path'] = item['output_path']
        names[item['id']]['art_status'] = 'Pose neutre générée ; ' + record['fidelity_check'].lower() + ' ; animation à produire'

    (ROOT / 'data/assets_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    (ROOT / 'data/roster.json').write_text(json.dumps(roster, ensure_ascii=False, indent=2))
    (DATA / 'queue.json').write_text(json.dumps(queue, ensure_ascii=False, indent=2))
    (DATA / 'generated_assets.json').write_text(json.dumps(produced, ensure_ascii=False, indent=2))
    summary = {
        'generated_at_utc': datetime.now(timezone.utc).isoformat(),
        'requested_missing_characters': len(queue),
        'attempted_characters': sum((DATA / f"result_{x['id']}.json").is_file() for x in queue),
        'new_character_images': len(produced),
        'new_images_with_alpha': sum(x['has_transparency'] for x in produced),
        'roster_characters_with_a_reference': len(produced) + 2,
        'roster_size': len(roster),
        'not_generated': missing,
        'blocked_by_image_system': [x['id'] for x in queue if x['status'] == 'blocked_by_image_system'],
        'fidelity_approved': 0,
        'animation_cycles_completed': 0,
        'selected_corrected_revisions': [x['character_id'] for x in produced if x['selected_revision'] == 'v3'],
        'characters_requiring_correction': [x['character_id'] for x in produced if x['fidelity_check'].startswith('À corriger')],
    }
    (DATA / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2))

    cards = []
    for c in roster:
        image_path = c.get('base_reference_path')
        if c['id'] in ('marcus', 'kait'):
            image_path = f'assets/{c["id"]}_neutral_cutout.png'
        if not image_path or not (ROOT / image_path).is_file():
            continue
        selected = next((x for x in produced if x['character_id'] == c['id']), None)
        verdict = selected['fidelity_check'] if selected else 'À valider'
        notes = selected['fidelity_notes'] if selected else 'Référence issue du premier lot ; fidélité exacte à contrôler.'
        cards.append(f'<article><a href="{html.escape(image_path)}"><img src="{html.escape(image_path)}" alt="{html.escape(c["name"])}" loading="lazy"></a><h2>{html.escape(c["name"])}</h2><p>{html.escape(c["source_game"])}</p><small>Pose de référence · {html.escape(verdict)}</small><p class="note">{html.escape(notes)}</p></article>')
    gallery = '''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Gears of War Combats — Personnages</title><style>body{margin:0;padding:32px;background:#111820;color:#eff4f9;font:16px system-ui}h1{font-size:30px;margin:0 0 12px}header{max-width:1000px;margin:0 auto 30px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:22px;max-width:1600px;margin:auto}article{padding:18px;background:#1e2b38;border:1px solid #3c4b59;border-radius:12px}img{width:100%;height:340px;object-fit:contain;background:#d7dde2;border-radius:8px}h2{font-size:19px;margin:14px 0 4px}p{line-height:1.5}article p{margin:0 0 8px;color:#b7c9d7}small{color:#b7c9d7}a{color:inherit}</style><header><h1>Gears of War Combats — Références de personnages</h1><p>Une image individuelle par personnage. Cliquer sur une illustration ouvre son fichier PNG. Les poses neutres constituent des références de production ; les animations, armes séparées et contrôles de fidélité restent à réaliser.</p></header><main>''' + ''.join(cards) + '</main></html>'
    status_text = f'<section class="status"><h2>État du lot</h2><p>{len(produced)} nouveaux personnages générés sur {len(queue)} demandés ; {len(missing)} non générés. Avec Marcus et Kait, {len(cards)} personnages disposent d’une référence sur les {len(roster)} du roster. Aucune nouvelle animation finalisée ; aucune fidélité 1:1 certifiée.</p><h2>Personnages non générés</h2><p>' + ', '.join(html.escape(names[x]['name']) for x in missing) + '</p><p>Le système d’image a refusé ces demandes. Aucun PNG de remplacement ni personnage fictivement marqué comme terminé.</p></section>'
    gallery = gallery.replace('</main></html>', '</main>' + status_text + '</html>').replace('</style>', '.note{font-size:13px}.status{max-width:1000px;margin:40px auto;padding:24px;border:1px solid #3c4b59;border-radius:12px}</style>')
    (ROOT / 'Galerie_Personnages.html').write_text(gallery)
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == '__main__':
    main()
