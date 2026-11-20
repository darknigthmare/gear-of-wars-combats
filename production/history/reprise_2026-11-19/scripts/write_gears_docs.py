from pathlib import Path
import json
root=Path('/workspace/scratch/8b5a16f9fa4a/gear-of-wars-combats')
m=json.loads((root/'production/asset_manifest.json').read_text())
s=json.loads((root/'production/generation_session.json').read_text())
assets=m['assets']
blocked=', '.join(r['name'] for r in s['records'] if r['status']=='blocked')
rows='\n'.join(f"| {a['name']} | {a['variant_label']} | [PNG]({a['path']}) |" for a in assets)
readme=f"""# Gears of War Combats

## Lot de reprise — 19 novembre 2026

**14 nouvelles références de personnages en pied**, une image par personnage, avec un véritable canal alpha PNG. Les personnages sont des candidats visuels pour le projet de combat 2D ; leurs poses animées et leur intégration au moteur restent à produire.

[Voir la galerie](docs/production/GALERIE_2026-11-19.md) · [Bilan du lot](docs/production/REPRISE_2026-11-19.md) · [Contrôle visuel](docs/production/VISUAL_QA_2026-11-19.md) · [Méthode de production](docs/production/PIPELINE_ASSETS.md)

| État vérifié de cette livraison | Nombre |
| --- | ---: |
| Personnages avec un nouveau PNG retenu | 14 |
| Demandes de personnages refusées par le générateur | 6 |
| Anciens visuels annoncés, fichiers non récupérés | 16 |
| Personnages suivis dans le roster | 36 |
| Animations finalisées par cette passe | 0 |

Les **16 visuels historiques** sont conservés dans le suivi comme non récupérés. Ils ne sont pas comptés parmi les fichiers de ce dépôt. La bible de 78 pages et le prototype mentionnés dans les échanges antérieurs n'ont pas été retrouvés dans les sources accessibles de cette passe et ne sont pas inclus.

## Personnages ajoutés

| Personnage | Variante retenue | Fichier |
| --- | --- | --- |
{rows}

## Manquants sans nouvelle image

{blocked}.

Leur génération a renvoyé un refus de sécurité sans explication précise de catégorie. Aucun fichier de remplacement fictif ne les représente. Leurs références restent documentées pour la suite.

## Ce qui est contrôlé

- Un seul personnage en pied par fichier ; tête, mains et pieds visibles.
- PNG RGBA avec transparence vérifiée par mesures et composition sur fond de contrôle.
- Variantes nommées et provenance des références documentée.
- Inscription **GRUB KILLER** de Clayton corrigée ; longs rails d'épaule d'Ukkon corrigés.
- Dimensions, taille, empreinte SHA-256 et réserves de chaque image dans [le manifeste](production/asset_manifest.json).

La fidélité **1:1 est l'objectif de production**, pas une certification automatique : plusieurs références sont tronquées, certains détails ont été reconstitués, et les armes du Warden demandent une comparaison rapprochée. Les réserves exactes figurent dans le rapport visuel et le manifeste.

## Dossiers

- **assets/characters/** : les 14 PNG retenus, sans doublons des versions remplacées.
- **production/roster.json** : les 36 personnages et leur état réel.
- **production/asset_manifest.json** : métadonnées et empreintes des PNG.
- **production/generation_session.json** : prompts, résultats et révisions de cette passe.
- **production/references/** et **docs/references/** : références visuelles et limites de preuve.
- **docs/production/** : galerie, bilan, contrôle visuel et prochaines étapes.

Les sources d'inspiration externes sont citées ; seules les images produites pour cette passe sont incorporées ici.
"""
(root/'README.md').write_text(readme)
gallery=["# Galerie — reprise du 19 novembre 2026","",
         "14 références en pied candidates. Chaque aperçu renvoie à un PNG individuel. La fidélité détaillée reste documentée dans le [rapport visuel](VISUAL_QA_2026-11-19.md).",""]
for a in assets:
    gallery += [f"## {a['name']} — {a['variant_label']}","",
                f"[![{a['name']}](../../{a['path']})](../../{a['path']})","",
                f"{a['width']} × {a['height']} px · PNG RGBA · version {a['revision']:02}.","",
                ' '.join(a['qa_notes']),""]
(root/'docs/production/GALERIE_2026-11-19.md').write_text('\n'.join(gallery))
report=f"""# Reprise des manquants — 19 novembre 2026

## Résultat

La passe traite les 20 personnages signalés manquants dans le suivi antérieur. **14 personnages ont une nouvelle référence en pied**, et **6 demandes sont refusées**. Les trois corrections retenues portent sur Theron (canal alpha), Clayton (lettrage) et Ukkon (longueur des rails).

Il y a **23 demandes au total**, dont **17 sorties réussies en comptant les révisions**. Le dépôt conserve **14 PNG sélectionnés** : les révisions ne gonflent pas le nombre de personnages.

## Limite de récupération

Au début de la passe, les branches main et codex/gears-combats-corpus-v3-20261119 pointaient au commit 2db6379ad2eb09c96b8851dd2380f02c8d618ef6 et ne contenaient que README.md. Aucune PR n'était présente. Les 16 illustrations antérieures, la bible de 78 pages et le prototype étaient mentionnés dans la continuité, mais leurs fichiers n'étaient pas accessibles dans cette passe.

Ces éléments sont conservés comme **à récupérer**, sans être annoncés comme présents ou vérifiés. Le chiffre arithmétique 16 + 14 ne constitue donc pas un inventaire vérifié de 30 fichiers.

## Nouveaux personnages

{', '.join(a['name'] for a in assets)}.

## Demandes refusées

{blocked}.

Statut exact : **moderation_blocked** à la sortie du générateur, sans motif détaillé exploitable. Aucun de ces six personnages n'a un fichier artificiellement marqué comme réussi.

## Vérification

Les 14 PNG retenus sont lisibles en RGBA et possèdent des pixels entièrement transparents. Les images ont été inspectées en pied ; les aperçus avec voile de couleur ont été contrôlés en appliquant réellement le canal alpha. Des RGB colorés sous un alpha nul ne créent pas de fond opaque.

Le manifeste enregistre les dimensions, l'empreinte SHA-256, les fractions d'alpha et le cadrage du corps principal. Le [rapport indépendant](VISUAL_QA_2026-11-19.md) précise les limites visuelles. Les identifiants de personnages sont uniques et chaque référence générée du roster renvoie à un fichier présent.

## Travail restant

1. Récupérer les 16 images historiques ainsi que la bible et le prototype pour réconcilier le corpus complet.
2. Obtenir une première image pour les six personnages encore bloqués.
3. Compléter les références des parties non visibles, vérifier les armes du Warden et les détails de tatouages, puis valider chaque costume.
4. Produire les poses latérales de combat, les états et les animations ; les références en pied actuelles ne sont pas ces animations.
5. Poursuivre ensuite les décors/parallaxes et les boss géants. Corpser, Brumak, King Raven et Kestrel restent dans les priorités historiques ; aucun nouveau visuel de boss géant n'est annoncé dans cette livraison.

La conception des coups, intros, rivaux, fins et comportements Boss Battle devra être réconciliée avec la bible récupérée. Cette passe ne prétend pas avoir reconstitué ni implémenté le jeu complet.
"""
(root/'docs/production/REPRISE_2026-11-19.md').write_text(report)
qa=root/'docs/production/VISUAL_QA_2026-11-19.md'
content=qa.read_text()
header="""# Contrôle visuel — lot du 19 novembre 2026

## Versions finales retenues

Le [manifeste](../../production/asset_manifest.json) fait autorité pour les 14 PNG retenus. **Clayton v02, Theron v02 et Ukkon v02 remplacent leurs premières sorties.** Le B de GRUB KILLER et la longueur des montants d'Ukkon sont corrigés. Les premières observations ci-dessous sont conservées comme historique de QA ; lire également les contrôles des révisions en fin de rapport.

La transparence et le cadrage complet sont vérifiés. La fidélité canonique de tous les petits détails reste à valider, particulièrement hors champ des références et pour les armes du Warden.

"""
first=content.find('\n')
qa.write_text(header+content[first+1:].lstrip())
print(json.dumps({'readme':True,'gallery_entries':len(assets),'report':True,'qa_final_banner':True},ensure_ascii=False))
for f in sorted((root/'production/references').glob('*.json')):
    d=json.loads(f.read_text())
    refs=d.get('references',d.get('records',[]))
    print(f.name, sorted({r.get('character_id') for r in refs}))
