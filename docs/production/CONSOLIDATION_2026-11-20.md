# Consolidation — Gears of War Combats — 20 novembre 2026

## État vérifié des fichiers

Les anciennes passes ont été réunies avec les nouvelles sorties réellement présentes. Les nombres ci-dessous proviennent du recalcul de [l’inventaire](../../production/asset_manifest.json) et de [la couverture](../../production/coverage.json). Ils remplacent les chiffres des rapports historiques pour le suivi courant.

| Contenu | Quantité |
| --- | ---: |
| Personnages possédant au moins une référence | **36 / 36** |
| Personnages sans référence | **0** |
| Personnages supplémentaires du catalogue avec une référence | 0 / 0 |
| Costumes avec une attribution visuelle explicite | 0 / 75 |
| PNG actifs de personnages, alternatives et présentations incluses | 45 |
| PNG actifs classés comme costumes | 0 |
| Boss avec une référence | 4 / 24 |
| Fiches d’arènes associées à un master | 1 / 24 |
| Masters de décor, Ephyra complémentaire inclus | 2 |
| PNG actifs uniques | 51 |
| Anciennes versions écartées conservées séparément | 12 |
| Personnages certifiés conformes 1:1 | **0** |
| Ensembles d’animations dessinées finalisés | **0** |

**Personnages encore sans image : Aucun personnage du roster sans référence.**

La présence d’un PNG signifie une référence statique disponible, pas un personnage jouable ni un costume certifié. [La galerie complète](../../Galerie_Personnages.html) affiche les 36 personnages du roster de conception, les 0 extensions de personnages, les 75 costumes, les 24 boss et les 24 arènes, avec des cartes explicites pour les manquants. Les extensions de production ne modifient pas le roster du moteur. Ephyra reste un master complémentaire, sans attribution arbitraire à une arène précise.

Les costumes hérités des fiches initiales restent sans attribution tant qu’un `costume_id` explicite n’est pas fourni. Cela signifie une liaison visuelle à vérifier, et non nécessairement une image à régénérer. Un master de décor ne vaut pas validation de ses calques de parallaxe séparés.

## Ce qui a été récupéré

- Le corpus initial : bible, prototype, données de conception, 16 personnages représentés et deux décors. Les fichiers copiés lors des deux premières passes sont identiques ; les doubles copies binaires n’augmentent pas les comptes.
- La passe v4 : neuf références de personnages et quatre boss. Kestrel était généré mais resté hors d’`assets` ; il est récupéré et contrôlé, avec [un constat distinct](../../data/generation_v4/recovery_kestrel_2026-11-20.json).
- Le lot de reprise : 14 références sélectionnées, ses sources, ses prompts et son rapport visuel. Clayton v02, Theron v02 et Ukkon v02 sont conservés ; leurs trois anciennes versions sont archivées dans `rejected_candidates/characters_20261119/`.
- Les six candidats v4 recouvrant des personnages du lot de reprise sont conservés et consultables comme alternatives. Ils ne sont pas six personnages supplémentaires.

## Nouvelles sorties présentes

| Sujet | Variante demandée | Fichier |
| --- | --- | --- |
| Dominic Santiago | Gears of War (2006) — COG armor | [PNG](../../assets/characters_v5/dom_gow1_fullbody.png) |
| Général RAAM | Gears of War (2006 / portage PC original) | [PNG](../../assets/characters_v5/raam_gow1_fullbody.png) |
| Garde Theron | Theron Guard classique casqué, cible GoW 2006 ; édition exacte non validée | [PNG](../../assets/characters_v5/theron_gow1_fullbody.png) |
| Dizzy Wallin | Gears of War 2 — tenue de pilote de Betty | [PNG](../../assets/characters_v6/dizzy_gow2_fullbody.png) |

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
| Marcus Fenix | Gears of War Ultimate Edition | [PNG](../../assets/marcus_neutral_cutout.png) |
| Dominic Santiago | Gears of War (2006) — COG armor | [PNG](../../assets/characters_v5/dom_gow1_fullbody.png) |
| Damon Baird | Gears of War 3 | [PNG](../../assets/characters_v2/baird_reference_v3.png) |
| Augustus Cole | Gears of War 3 | [PNG](../../assets/characters_v4/cole_reference_v4.png) |
| Anya Stroud | Gears of War 3 | [PNG](../../assets/characters/anya_stroud/gears3/reference_fullbody_v01.png) |
| Kait Diaz | Gears 5 hiver | [PNG](../../assets/kait_neutral_cutout.png) |
| Général RAAM | Gears of War (2006 / portage PC original) | [PNG](../../assets/characters_v5/raam_gow1_fullbody.png) |
| Skorge | Gears of War 2 | [PNG](../../assets/characters_v2/skorge_reference_v3.png) |
| Reine Myrrah | Gears of War 3 | [PNG](../../assets/characters/myrrah/gears3/reference_fullbody_v01.png) |
| Drone locuste | Gears of War 2006 | [PNG](../../assets/characters_v2/locust_drone_reference_v2.png) |
| Kantus | Gears of War 2 | [PNG](../../assets/characters_v2/kantus_reference_v3.png) |
| Garde Theron | Theron Guard classique casqué, cible GoW 2006 ; édition exacte non validée | [PNG](../../assets/characters_v5/theron_gow1_fullbody.png) |
| JD Fenix | Gears 5 | [PNG](../../assets/characters_v2/jd_reference_v2.png) |
| Del Walker | Gears 5 | [PNG](../../assets/characters_v2/del_reference_v3.png) |
| Fahz Chutani | Gears 5 | [PNG](../../assets/characters/fahz_chutani/gears5/reference_fullbody_v01.png) |
| Clayton Carmine | Gears of War 3 | [PNG](../../assets/characters/clayton_carmine/gears3/reference_fullbody_v02.png) |
| Lizzie Carmine | Gears 5 | [PNG](../../assets/characters_v2/lizzie_reference_v2.png) |
| Victor Hoffman | Armure classique | [PNG](../../assets/characters/victor_hoffman/classic/reference_fullbody_v01.png) |
| Tai Kaliso | Gears of War 2 | [PNG](../../assets/characters/tai_kaliso/gears2/reference_fullbody_v01.png) |
| Dizzy Wallin | Gears of War 2 — tenue de pilote de Betty | [PNG](../../assets/characters_v6/dizzy_gow2_fullbody.png) |
| Samantha Byrne | Gears of War 3 | [PNG](../../assets/characters/samantha_byrne/gears3/reference_fullbody_v01.png) |
| Garron Paduk | Gears of War Judgment | [PNG](../../assets/characters_v2/paduk_reference_v3.png) |
| Sofia Hendrik | Gears of War Judgment | [PNG](../../assets/characters_v2/sofia_reference_v3.png) |
| Gabe Diaz | Gears Tactics | [PNG](../../assets/characters/gabriel_diaz/tactics/reference_fullbody_v01.png) |
| Sid Redburn | Gears Tactics | [PNG](../../assets/characters_v2/sid_reference_v3.png) |
| Mikayla Dorn | Gears Tactics | [PNG](../../assets/characters/mikayla_dorn/tactics/reference_fullbody_v01.png) |
| Reine Reyna | Gears 5 multijoueur | [PNG](../../assets/characters_v2/reyna_reference_v3.png) |
| Lahni Kaliso | Gears 5 — Hivebuster / Escape | [PNG](../../assets/characters/lahni_kaliso/gears5_hivebuster/reference_fullbody_v01.png) |
| Keegan | Gears 5 Hivebusters | [PNG](../../assets/characters_v4/keegan_reference_v4.png) |
| Mac | Gears 5 — Hivebuster / Escape | [PNG](../../assets/characters/mac_macallister/gears5_hivebuster/reference_fullbody_v01.png) |
| JACK | Gears 5 | [PNG](../../assets/characters_v2/jack_reference_v3.png) |
| DeeBee | Gears of War 4 | [PNG](../../assets/characters_v4/deebee_reference_v4.png) |
| Warden | Gears 5 | [PNG](../../assets/characters/warden/gears5/reference_fullbody_v01.png) |
| Drone de l’Essaim | Gears of War 4 | [PNG](../../assets/characters_v2/swarm_drone_reference_v2.png) |
| Ukkon | Gears Tactics | [PNG](../../assets/characters/ukkon/tactics/reference_fullbody_v02.png) |
| Grenadier locuste | Gears Tactics | [PNG](../../assets/characters_v2/grenadier_reference_v2.png) |

## Historique et documents

- Les données initiales de roster/manifeste et l’ancienne galerie sont figées dans `production/history/initial_2026-11-19/`.
- Le lot de reprise est conservé intégralement dans `production/history/reprise_2026-11-19/` pour ses documents, journaux, références et scripts historiques. Les images actives sont conservées une seule fois à leurs chemins de production.
- [Le rapport visuel du 19 novembre](VISUAL_QA_2026-11-19.md) reste une preuve de contrôle datée ; ses chiffres de passe ne décrivent pas le total consolidé.
- Les PDF, DOCX et XLSX de `livrables/` sont des **instantanés du 19 novembre 2026**, conservés sans modification binaire. Ils ne sont pas présentés comme des exports actualisés de cette consolidation.
- Le prototype conserve son périmètre de démonstration. Les images explicitement liées dans son asset map sont signalées comme intégrées en référence statique ; cela ne crée pas d’animation dessinée. Ajouter une illustration à l’inventaire seul ne l’intègre pas automatiquement à son moteur.

## Recalcul après génération

```bash
python src/consolidate_inventory.py
```

Cette commande vérifie les fichiers, recalcule empreintes, dimensions, alpha et comptes, réconcilie les références du roster, puis reconstruit l’inventaire et la galerie autonome. Elle lit les résultats des passes v5 et suivantes sans les modifier. `src/build_asset_manifest.py` appelle également ce recalcul avant de renouveler la file de production. `src/finalize_generation_v2.py` reste un script historique de v2, pas la commande courante de consolidation.

Ce rapport décrit les fichiers préparés. Il ne constitue pas une preuve de publication GitHub, qui doit être vérifiée séparément.
