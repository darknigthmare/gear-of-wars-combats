# Gears of War Combats

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
| Anya Stroud | Gears of War 3 | [PNG](assets/characters/anya_stroud/gears3/reference_fullbody_v01.png) |
| Queen Myrrah | Gears of War 3 | [PNG](assets/characters/myrrah/gears3/reference_fullbody_v01.png) |
| Theron Guard | Gears of War 3 | [PNG](assets/characters/theron_guard/gears3/reference_fullbody_v02.png) |
| Fahz Chutani | Gears 5 | [PNG](assets/characters/fahz_chutani/gears5/reference_fullbody_v01.png) |
| Clayton Carmine | Gears of War 3 | [PNG](assets/characters/clayton_carmine/gears3/reference_fullbody_v02.png) |
| Victor Hoffman | Armure classique | [PNG](assets/characters/victor_hoffman/classic/reference_fullbody_v01.png) |
| Tai Kaliso | Gears of War 2 | [PNG](assets/characters/tai_kaliso/gears2/reference_fullbody_v01.png) |
| Samantha Byrne | Gears of War 3 | [PNG](assets/characters/samantha_byrne/gears3/reference_fullbody_v01.png) |
| Gabriel Diaz | Gears Tactics | [PNG](assets/characters/gabriel_diaz/tactics/reference_fullbody_v01.png) |
| Mikayla Dorn | Gears Tactics | [PNG](assets/characters/mikayla_dorn/tactics/reference_fullbody_v01.png) |
| Lahni Kaliso | Gears 5 — Hivebuster / Escape | [PNG](assets/characters/lahni_kaliso/gears5_hivebuster/reference_fullbody_v01.png) |
| Mac MacAllister | Gears 5 — Hivebuster / Escape | [PNG](assets/characters/mac_macallister/gears5_hivebuster/reference_fullbody_v01.png) |
| Warden | Gears 5 | [PNG](assets/characters/warden/gears5/reference_fullbody_v01.png) |
| Ukkon | Gears Tactics | [PNG](assets/characters/ukkon/tactics/reference_fullbody_v02.png) |

## Manquants sans nouvelle image

Dominic Santiago, Augustus Cole, General RAAM, Dizzy Wallin, Jeremiah Keegan, DeeBee Shepherd.

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
