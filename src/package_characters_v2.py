"""Package the selected character references and their explicit production status."""
from pathlib import Path
import hashlib
import html
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
GEN = DATA / 'generation_v2'
OUT = ROOT.parent / 'outputs/gears_combats_characters_v2'
PREFIX = 'Gears_of_War_Combats_Personnages_v2'


def read(path):
    return json.loads(path.read_text())


def find_urls(value):
    if isinstance(value, dict):
        for item in value.values():
            yield from find_urls(item)
    elif isinstance(value, list):
        for item in value:
            yield from find_urls(item)
    elif isinstance(value, str) and value.startswith(('https://', 'http://')) and ' ' not in value:
        yield value


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    summary = read(GEN / 'summary.json')
    roster = read(DATA / 'roster.json')
    names = {x['id']: x for x in roster}
    selected = read(GEN / 'generated_assets.json')
    manifest = read(DATA / 'assets_manifest.json')
    prompts = {x['id']: x for x in read(GEN / 'prompts_all.json')}
    workbook = OUT / 'Gears_of_War_Combats_Production_v2.xlsx'
    assert workbook.is_file(), 'Export du classeur V2 requis avant archivage.'
    assert len(selected) == 14 and len(summary['blocked_by_image_system']) == 20
    assert len({x['character_id'] for x in selected}) == len(selected)

    report = [
        '# Gears of War Combats — Personnages, lot 2',
        '',
        'État de production du 19 novembre 2026.',
        '',
        '**14 personnages supplémentaires disposent maintenant d’une image individuelle. Les 34 personnages qui manquaient ont chacun fait l’objet d’une demande ; 20 demandes initiales ont été refusées par le système d’image.** Avec les références existantes de Marcus et Kait, 16 des 36 personnages du roster possèdent une référence visuelle.',
        '',
        'Chaque nouveau fichier contient un personnage entier dans une seule pose neutre, les mains vides, avec un canal alpha réel. Les accessoires fixés au costume, dont les grenades du Grenadier, peuvent rester présents. JACK est représenté avec ses outils intégrés. Ces fichiers sont des références de production : ils ne constituent pas des animations de combat ni des personnages nouvellement jouables.',
        '',
        '## Bilan vérifié',
        '',
        '| Indicateur | Résultat |',
        '|---|---:|',
        '| Personnages manquants demandés | 34 |',
        '| Personnages nouvellement générés et sélectionnés | 14 |',
        '| Versions corrigées retenues parmi ces 14 | 9 |',
        '| Personnages sans image après refus | 20 |',
        '| Personnages du roster avec une référence, anciens compris | 16 / 36 |',
        '| Nouvelles images avec alpha réel | 14 / 14 |',
        '| Fidélités 1:1 certifiées dans ce lot | 0 |',
        '| Nouveaux cycles d’animation finalisés | 0 |',
        '',
        'Dix corrections ciblées ont été demandées sur des images déjà produites. Neuf ont donné une nouvelle version retenue ; la correction de Lizzie a été refusée. Les nombres de personnages ci-dessus ne comptent pas les révisions comme des personnages supplémentaires.',
        '',
        '## Personnages produits',
        '',
        '| Personnage | Jeu / variante de référence | Version | Dimensions | État | Fichier |',
        '|---|---|---|---|---|---|',
    ]
    for item in selected:
        cid = item['character_id']
        report.append(f"| {item['name']} | {item['source_game']} | {item['selected_revision']} | {item['width_px']} × {item['height_px']} | {item['fidelity_check']} | [{Path(item['path']).name}]({item['path']}) |")
    report += ['', '## Corrections et limites par personnage', '']
    for item in selected:
        report.append(f"- **{item['name']} — {item['fidelity_check']}.** {item['fidelity_notes']}")
    report += [
        '',
        '« À valider » signifie que la version est retenue pour la revue artistique. Cela ne signifie ni fidélité 1:1 approuvée, ni acceptation pour l’animation. « À corriger » signale une différence concrète visible dans les références comparées. Les rapports QA détaillés donnent les comparaisons, les sources, les empreintes des fichiers et les limites du contrôle.',
        '',
        'Les références disponibles ne couvrent pas systématiquement les pieds, le dos ou tous les côtés du costume. Pour Kantus, la vue complète du bas provient d’un concept de production ; pour Reyna, le bas n’est pas suffisamment documenté. Plusieurs images ont une marge verticale courte. Une intégration sur décor, un contrôle des liserés et un cadrage de sprite restent nécessaires avant animation.',
        '',
        '## Personnages non générés',
        '',
        'Le système d’image a refusé les demandes suivantes. Aucun fichier fictif ni remplacement générique n’a été ajouté au roster pour ces personnages.',
        '',
    ]
    report += [f"- {names[cid]['name']} — {names[cid]['source_game']}." for cid in summary['blocked_by_image_system']]
    report += [
        '',
        '## Utiliser le pack',
        '',
        '1. Décompresser l’archive en conservant son arborescence.',
        '2. Ouvrir `Galerie_Personnages.html` dans un navigateur. La galerie fonctionne localement et affiche 16 personnages ; cliquer sur une image ouvre son PNG.',
        '3. Consulter les fichiers sélectionnés dans `assets/characters_v2/`. Les versions antérieures écartées ne sont pas intégrées à ce dossier.',
        '4. Ouvrir `Gears_of_War_Combats_Production_v2.xlsx` pour le roster, le catalogue des images et l’état des autres éléments du projet.',
        '5. Lire `data/generation_v2/qa_*.json` pour le contrôle détaillé. Les rapports sans suffixe v3 concernent les premières générations ; les rapports v3 concernent les versions corrigées. `queue.json` et `generated_assets.json` désignent la sélection courante.',
        '',
        'Le pack contient aussi les six images du premier lot pour conserver les chemins de son catalogue : deux références originales, deux poses détourées et deux décors. Cela ne change pas le nombre de personnages nouvellement générés. Les données de la bible sont incluses pour conserver le contexte du roster ; les fonctionnalités décrites y restent des spécifications selon leur statut existant.',
        '',
        '## Traçabilité',
        '',
        '- `data/assets_manifest.json` : fichiers effectivement présents, dimensions, alpha, empreinte SHA256, intégration et fidélité.',
        '- `data/generation_v2/summary.json` : bilan du lot.',
        '- `data/generation_v2/prompts_all.json` : 34 demandes préparées avec jeu, costume, références et points à contrôler.',
        '- `data/generation_v2/prompts_used_batch*.json` et `result_*.json` : demandes soumises et résultats initiaux.',
        '- `data/generation_v2/edit_*_v3.json` : corrections soumises et résultats.',
        '- `REFERENCES.md` : liens des sources utilisés pour la génération et les contrôles.',
        '- `PACK_SHA256.json` : inventaire des fichiers livrés et empreintes.',
        '- `src/` : scripts de suivi et d’archivage utilisés pour ce lot ; ils ne sont pas nécessaires à l’ouverture des images.',
        '',
        'Les chemins absolus présents dans certains journaux et rapports identifient les fichiers examinés au moment du contrôle. Ils servent à la traçabilité et ne sont pas nécessaires à l’ouverture de la galerie. Les références web ne sont pas incorporées comme nouveaux éléments du jeu.',
    ]
    report_text = '\n'.join(report) + '\n'
    report_path = OUT / f'{PREFIX}.md'
    report_path.write_text(report_text)

    references = ['# Références visuelles du lot 2', '', 'Les liens ci-dessous sont les sources consignées dans les demandes et rapports de contrôle. Une source d’identité ne valide pas automatiquement chaque détail d’un costume.', '']
    for item in selected:
        cid = item['character_id']
        urls = set(find_urls(prompts[cid].get('source_urls', [])))
        for qa in [GEN / f'qa_{cid}.json', GEN / f'qa_{cid}_v3.json']:
            if qa.is_file():
                urls.update(find_urls(read(qa)))
        references += [f"## {item['name']}", '', *[f'- <{url}>' for url in sorted(urls)], '']
    references_path = OUT / 'REFERENCES.md'
    references_path.write_text('\n'.join(references))

    readme = '\n'.join([
        '# Gears of War Combats — Pack personnages v2', '',
        '14 nouveaux personnages sélectionnés ; 20 autres non générés après refus du système d’image.',
        'Marcus et Kait sont également présents dans la galerie en tant que références du premier lot.', '',
        'Ouvrir Galerie_Personnages.html après extraction complète. Les 14 nouveaux PNG sont dans assets/characters_v2/.',
        'Le rapport Gears_of_War_Combats_Personnages_v2.md détaille le résultat, les corrections et les limites.',
        'Le classeur Gears_of_War_Combats_Production_v2.xlsx présente le suivi complet de production.', '',
        'Aucune fidélité 1:1 certifiée. Quatre candidats restent explicitement À corriger : Del, Lizzie, Skorge et Queen Reyna.',
        'Une pose de référence par personnage ; aucune nouvelle animation de combat ou intégration jouable.', '',
        'La bible et le prototype V1 ne sont pas remplacés par ce pack. Ce pack livre les images sélectionnées, le suivi V2 et les données utiles à leur production.', '',
    ])
    readme_path = OUT / 'LIRE_MOI.md'
    readme_path.write_text(readme)

    files = [(ROOT / 'Galerie_Personnages.html', 'Galerie_Personnages.html'), (report_path, report_path.name), (workbook, workbook.name), (references_path, references_path.name), (readme_path, readme_path.name)]
    files += [(ROOT / x['path'], x['path']) for x in manifest]
    files += [(p, str(p.relative_to(ROOT))) for p in sorted(DATA.rglob('*.json'))]
    for name in ('finalize_generation_v2.py', 'package_characters_v2.py', 'build_asset_manifest.py', 'build_workbook.mjs'):
        files.append((ROOT / 'src' / name, 'src/' + name))
    workbook_qa = ROOT / 'docs/qa_workbook_v2.json'
    if workbook_qa.is_file():
        files.append((workbook_qa, 'docs/qa_workbook_v2.json'))
    assert len({name for _, name in files}) == len(files), 'Chemins dupliqués dans le pack.'
    for path, _ in files:
        assert path.is_file(), path
    image_links = re.findall(r'<img[^>]+src="([^"]+)"', (ROOT / 'Galerie_Personnages.html').read_text())
    assert len(image_links) == 16
    included = {name for _, name in files}
    assert all(html.unescape(src) in included for src in image_links)
    inventory = [{'path': name, 'bytes': path.stat().st_size, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path, name in files]
    inventory_path = OUT / 'PACK_SHA256.json'
    inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2))
    files.append((inventory_path, inventory_path.name))
    archive_path = OUT / f'{PREFIX}.zip'
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for path, name in files:
            z.write(path, PREFIX + '/' + name)
    with zipfile.ZipFile(archive_path) as z:
        assert z.testzip() is None, 'Archive invalide.'
        assert len(z.namelist()) == len(files)
    verification = {'archive': str(archive_path), 'archive_bytes': archive_path.stat().st_size, 'files': len(files), 'selected_new_images': len(selected), 'gallery_characters': len(image_links), 'manifest_assets': len(manifest), 'sha256': hashlib.sha256(archive_path.read_bytes()).hexdigest(), 'zip_crc_ok': True, 'gallery_paths_ok': True}
    (OUT / 'verification_pack.json').write_text(json.dumps(verification, ensure_ascii=False, indent=2))
    print(json.dumps(verification, ensure_ascii=False))


if __name__ == '__main__':
    main()
