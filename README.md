# Gears of War Combats

Corpus de conception, prototype et références visuelles consolidés le **25 novembre 2026** pour Darknigthmare.

## État courant — passe V11 — assets fixes

**26 nouveaux PNG**, un sujet par image, sans animations. Ils sont intégrés à la galerie et à l’inventaire avec leurs sources, prompts et réserves de fidélité.

- [Images livrées, refus et recherches en attente](docs/production/LISTING_V11.md)
- [Liste complète des manquants après V11](docs/production/REPRISE_V11.md)
- [Validation technique V11](docs/production/VALIDATION_V11.json)
- [Sources et prompts V11](docs/references/production-v11-research.md)

| Catégorie | Références disponibles | Manquants |
|---|---:|---:|
| Personnages | 51 / 56 | 5 |
| Costumes | 48 / 85 | 37 |
| Boss, créatures et machines | 24 / 31 | 7 |
| Stages | 34 / 34 | 0 |
| Projectiles | 4 / 8 | 4 |

Total actif : **136 PNG uniques**. Ephyra est un décor complémentaire ; les costumes rattachés à un PNG existant ne doublent pas le total.

Les images restent des candidats statiques visant une fidélité 1:1. Les références d’édition, corps partiels, reconstitutions, créations originales et défauts identifiés sont documentés dans les journaux. Les décors sont adaptés au combat latéral ; les deux arènes d’entraînement sont des créations du projet.

2 essais V11 ont été refusés et 3 sujets restent au stade de recherche de référence ; aucun n’est compté comme PNG. Buzzkill et Dropshot V9 conservent leur état **À corriger**.

### Validation technique V11

Les dimensions natives, empreintes SHA-256, canaux alpha et marges de silhouette sont contrôlés. Les tests d’inventaire, la cohérence de la galerie et les limites du contrôle navigateur sont consignés dans le [rapport V11](docs/production/VALIDATION_V11.json). Aucun changement au moteur de combat.

### Passes V9 et V10 conservées

Les 40 images des passes V9 et V10 et leurs résultats restent documentés : [listing V9](docs/production/LISTING_V9.md), [validation V9](docs/production/VALIDATION_V9.json), [listing V10](docs/production/LISTING_V10.md), [manquants à la clôture V10](docs/production/REPRISE_V10.md), [validation V10](docs/production/VALIDATION_V10.json).

## Consulter le projet

- [Galerie des personnages, costumes, boss, stages et projectiles](Galerie_Personnages.html)
- [Reprise V7 : images, réserves et manques exacts](docs/production/REPRISE_V7.md)
- [Listing V7 : nouvelles identités et costumes rattachés](docs/production/LISTING_V7.md)
- [Audit des 34 rattachements de costumes](docs/production/AUDIT_COSTUMES_V7.md)
- [Sources du catalogue V7](docs/references/production-v7-catalog.md)
- [Rapport de validation V7](docs/production/VALIDATION_V7.json)
- [Reprise V6 historique](docs/production/REPRISE_V6.md)
- [Listing V6 et éditions cibles](docs/production/LISTING_V6.md)
- [Rapport de validation V6](docs/production/VALIDATION_V6.json)
- [État consolidé et limites de production](docs/production/CONSOLIDATION_2026-11-25.md)
- [Inventaire courant et couverture](production/coverage.json)
- [Prototype autonome](prototype/Gears_Combats_Prototype.html)
- [Bible illustrée v1 en PDF](livrables/Gears_of_War_Combats_Bible_v1.pdf)
- [Bible v1 en Markdown](livrables/Gears_of_War_Combats_Bible_v1.md)

Le fichier HTML du prototype embarque son code, ses styles et ses trois images utilisées. La galerie utilise les PNG du dossier `assets` : conserver son arborescence pour la consulter hors ligne.

## Historique — lot V7

Les comptes ci-dessous ont été vérifiés dans l’[inventaire consolidé](production/coverage.json) et le [manifeste des fichiers](production/asset_manifest.json). La consolidation ne signale aucune alerte.

| Élément | Clôture V7 — 20 novembre 2026 |
| --- | --- |
| Personnages documentés | **56** : 36 du roster initial et 20 extensions |
| Personnages avec une référence | **40 / 56** : 36 / 36 du roster initial et 4 / 20 extensions |
| Identités sans image | **16** |
| Costumes avec rattachement explicite | **36 / 85** : 34 images de personnages réutilisées et 2 PNG dédiés |
| Costumes sans rattachement explicite | **49** ; chaque édition reste à documenter ou produire |
| Boss / rencontres avec une référence | **6 / 31**, dont Shibboleth en monture seule, duo avec Karn incomplet |
| Stages avec un master associé | **4 / 34** : Hollow, Gridlock, Village, Dawn |
| Décor complémentaire | Ephyra, hors des 34 fiches de stages |
| PNG actifs uniques | **62** : 49 personnages / variantes / présentations, 2 costumes, 6 boss, 5 décors |
| Archives exclues du total actif | **12** PNG |
| Fidélités 1:1 certifiées | **0** |
| Jeux d’animations complets | **0** |

Les [manques détaillés de la reprise V7](docs/production/REPRISE_V7.md) distinguent les identités sans image des éditions encore à produire. Les 34 rattachements de costumes ne sont pas ajoutés au total des PNG. Une référence disponible reste un candidat statique, dont la qualité et l’édition se vérifient dans le journal.

Le [catalogue V7](data/production_catalog_v7.json) ajoute **Adam Fenix (Gears 3 multijoueur), Alex Brand (Judgment multijoueur) et Karn (Judgment)**. Ces trois fiches sont des cibles documentées, sans image créée dans cette passe pour ces identités. Karn est distinct de la monture de la rencontre existante `boss_shibboleth`.

Le [mapping audité](data/costume_asset_links_v7.json) rattache **34 PNG existants** à leur costume exact documenté, après contrôle de l’édition, du personnage, de la provenance et de l’empreinte SHA-256. Il conserve les fichiers, leur statut artistique et leur relation à la version de base du personnage. Il ne crée aucun PNG. L’[audit V7](docs/production/AUDIT_COSTUMES_V7.md) détaille les preuves et les correspondances écartées.

### Images de la passe V7

**Six nouveaux PNG** et leurs six journaux sont présents, avec dimensions, transparence le cas échéant, empreintes et réserves consignées. La passe apporte deux références de personnages, un costume, une monture de boss et deux masters de décor.

| Sujet | Édition de l’image | Asset | Portée du rattachement |
| --- | --- | --- | --- |
| Michael Barrick | Gears of War 3 — RAAM’s Shadow | [PNG en pied](assets/characters_v7/michael_barrick_gow3_raams_shadow_fullbody.png) | `michael_barrick`, `alternate_version` ; cible Gears 5 encore absente |
| Colonel Ezra Loomis | Gears of War: Judgment | [PNG en pied](assets/characters_v7/ezra_loomis_judgment_fullbody.png) | `ezra_loomis`, candidat de l’édition cible ; uniforme de parade, bras croisés |
| Thrashball Cole | Gears of War 3 | [PNG en pied](assets/costumes_v7/cole_thrashball_gow3_fullbody.png) | Costume `cole_skin_03` ; autre tenue que Cole en campagne |
| Shibboleth | Gears of War: Judgment | [Monture seule](assets/bosses_v7/shibboleth_judgment_mount_only_fullbody.png) | Référence partielle de `boss_shibboleth` ; Karn absent du duo |
| Village | Gears 5 — Operation 8 | [Master de décor](assets/stages_v7/village_gears5_master.png) | `stage_village_g5` ; cadrage adapté au combat 2D |
| Dawn | Gears 5 — Operation 8 Drop 2 | [Master de décor](assets/stages_v7/dawn_gears5_master.png) | `stage_dawn_g5` ; cadrage adapté au combat 2D |

**Alicia Valera et Michael Barrick conservent leurs cibles Gears 5 — Operation 8 Drop 2.** Leurs références RAAM’s Shadow sont disponibles en version Gears 3, avec la relation `alternate_version`. La présence d’une image du personnage ne couvre pas automatiquement son édition cible.

**Shibboleth reste une référence de monture seule.** Karn, son placement, son échelle et ses attaches sur la monture restent à produire et contrôler avant de considérer le duo complet. La rencontre, ses phases et ses animations ne sont pas implémentées par ce PNG.

Les journaux de [génération V7](data/generation_v7) consignent les sources réellement utilisées et les réserves. Cole demande notamment une orientation vers la droite, des marges supplémentaires et une vérification de la provenance du rendu complémentaire ; Loomis conserve une pose bras croisés. Village et Dawn sont des masters aplatis, avec composition adaptée et calques de parallaxe encore absents. Aucune de ces références ne constitue une certification 1:1.

## Historique — lot V6

L’état de clôture V6 est conservé dans la [reprise V6](docs/production/REPRISE_V6.md) et son [rapport de validation](docs/production/VALIDATION_V6.json). Les comptes suivants décrivent ce lot historique, avant les ajouts et rattachements V7.

| Élément | État au 20 novembre 2026 |
| --- | --- |
| Personnages documentés | **53** : 36 du roster initial et 17 extensions de production |
| Personnages distincts avec au moins une référence | **38 / 53** : 36 du roster initial et 2 extensions |
| Personnages sans référence | **15**, listés dans le rapport de reprise V6 |
| Costumes documentés | **85**, dont **1** avec rattachement visuel explicite : Mechanic Mac |
| Costumes sans rattachement visuel explicite | **84** ; ce chiffre ne signifie pas nécessairement 84 images absentes |
| Boss et rencontres documentés | **31**, dont **5** avec une référence |
| Stages documentés | **34**, dont **2** avec un master associé : Hollow et Gridlock |
| Décor complémentaire | **Ephyra**, conservé sans attribution arbitraire à une fiche d’arène |
| PNG actifs uniques | **56** : 47 de personnages/variantes/présentations, 1 costume, 5 boss, 3 décors |
| Anciens candidats et révisions conservés | **12**, hors total actif |
| Fidélités 1:1 certifiées | **0** |
| Jeux d’animations complets | **0** |

Les 17 extensions sont des cibles de production ; leur ajout ne modifie pas le roster du moteur. Les 31 fiches de boss incluent des simulations et des adaptations de rencontres. Une référence disponible désigne une image statique, avec l’édition et les limites consignées dans son journal.

### Cinq nouvelles images V6

| Sujet | Édition de l’image | Asset | Rattachement |
| --- | --- | --- | --- |
| Mechanic Mac | Gears 5 | [PNG en pied](assets/costumes_v6/mac_mechanic_gears5_fullbody.png) | Costume existant `mac_skin_02` |
| Boomer locuste | Gears Tactics | [PNG en pied](assets/characters_v6/boomer_tactics_fullbody.png) | Nouveau personnage `boomer_tactics` |
| Gridlock | Gears of War 4 | [Master de décor](assets/stages_v6/gridlock_gow4_master.png) | Stage `stage_gridlock_gow4` |
| Matriarch | Gears 5 | [PNG en pied](assets/bosses_v6/matriarch_gears5_fullbody.png) | Boss existant `boss_matriarch` |
| Alicia Valera | Gears of War 3 — RAAM’s Shadow | [PNG en pied](assets/characters_v6/alicia_valera_gow3_fullbody.png) | Référence historique du personnage `alicia_valera` |

**Alicia conserve Gears 5 — Operation 8 Drop 2 comme cible de catalogue.** Le nouveau PNG Gears 3 est rattaché comme `alternate_version` ; la cible Gears 5 reste à produire. Il n’ajoute ni un second personnage ni un costume arbitraire. Le Boomer est un candidat pour l’édition Tactics, avec le bas du corps et certaines parties de l’arme encore à contrôler sur des vues complètes.

**Dizzy Wallin — Gears of War 2 a été récupéré**, avec son [PNG](assets/characters_v6/dizzy_gow2_fullbody.png), son journal et sa provenance. Il ne fait pas partie des cinq nouvelles générations. Cette récupération complète la couverture du roster initial de 36 fiches.

Les journaux de `data/generation_v6` consignent les sources, les contrôles de transparence, les réserves visuelles et les vérifications restantes. Les personnages et la Matriarch sont des poses statiques ; Gridlock est un master aplati dont les calques de parallaxe restent à produire. Les marges, les visages, les asymétries, les armes et les éléments reconstruits nécessitent une validation avant atlas et animation.

### Lots précédents conservés

La reprise V5 a ajouté Dominic Santiago, RAAM et un Theron classique casqué. Ce dernier vise le premier jeu, tandis que ses références disponibles comprennent une figurine de 2008 et un portrait attribué à Gears 2 : l’édition exacte reste à valider. Le Kestrel auparavant hors du dossier d’assets a été récupéré ; les corrections retenues de Clayton et Ukkon et les autres candidats historiques sont conservés.

Le [listing V6](docs/production/LISTING_V6.md) apporte **44 ajouts nets de catalogue** et enrichit deux identités existantes, Mechanic Mac et Matriarch. Les détails des sources figurent dans le [registre V6](docs/references/production-v6.md).

Contribution historique fusionnée dans la **[PR #1](https://github.com/darknigthmare/gear-of-wars-combats/pull/1)**, sur la branche `codex/gears-combats-corpus-v6-20261120`.

## Prototype réellement jouable

Trois rencontres sont disponibles : **Marcus contre RAAM**, **Berserker** et **King Raven** en simulation. Le prototype comprend déplacement, deux coups de corps à corps, tir, garde, esquive, recharge active, spécial, IA, phases de boss, pause et résultats.

La nouvelle image de **RAAM est intégrée au duel**, avec la pose existante de Marcus et le décor Ephyra. L’option d’illustration concerne les deux combattants. Ces dessins restent des poses neutres déplacées par le moteur ; ils ne possèdent pas encore de dessins d’attaque ou de locomotion. Berserker et King Raven gardent leurs représentations de jeu provisoires. Les autres personnages du catalogue ne deviennent pas jouables du seul fait que leur PNG est présent.

La campagne, le tournoi, les exécutions finales, le roster jouable complet, les animations dessinées, le multijoueur local et le réseau demeurent spécifiés dans la bible et non implémentés.

| Action | Clavier |
| --- | --- |
| Déplacement | Q/A, D, flèches |
| Coup léger / lourd | J / K |
| Tir / spécial | L / I |
| Garde | F ou flèche bas |
| Esquive | Espace avec une direction |
| Recharge puis confirmation | R, puis R |
| Pause | Échap |

Des commandes tactiles et la prise en charge de l’API manette standard existent. La manette physique n’a pas été testée.

## Conception conservée

La bible v1 comporte 78 pages et décrit 36 combattants, 75 costumes ou époques, 179 actions, 36 routes arcade, 24 propositions de combos pour le noyau, 12 chapitres de campagne, 24 rencontres Boss Battle avec 72 phases et 24 arènes avec 144 calques spécifiés. Les valeurs et les scénarios d’exhibition sont des adaptations originales pour le jeu 2D.

Les PDF, Word et deux classeurs dans `livrables` sont les versions historiques produites le 19 novembre. Ils n’ont pas été reconstruits pour cette passe ; leurs décomptes d’images peuvent donc être antérieurs à ceux des JSON et de la galerie courants. Les masters de décor ne remplacent pas les 144 calques séparés spécifiés par la bible initiale, ni les calques des nouvelles arènes V6.

## Organisation et reprise

- `data` : roster, règles, routes, rencontres, catalogues de production versionnés, mapping des costumes et journaux des générations.
- `production/asset_manifest.json` et `production/coverage.json` : inventaire courant et contrôle de couverture.
- `production/history` et les rapports datés du 19 novembre : archives de production.
- `assets` : images actives, sans références tierces téléchargées pour la recherche.
- `rejected_candidates` : anciennes révisions et candidats non sélectionnés, exclus de la couverture active.
- `prototype` : moteur, interface, HTML autonome et vérifications.
- `docs` et `livrables` : bible, provenance, rapports et livrables historiques.

```bash
python -m unittest discover -s tests -p 'test_inventory_v*.py' -v
python src/consolidate_inventory.py
python src/validate_data.py
node prototype/build.mjs
node prototype/tests.cjs
```

Le script de consolidation relit les fichiers, leurs journaux et tous les `data/production_catalog_v*.json` dans l’ordre numérique des versions pour actualiser le manifeste, la couverture et la galerie. Il fusionne les entrées par identifiant et rejette les collisions entre catégories. Après collecte des assets, il applique tous les `data/costume_asset_links_v*.json` dans leur ordre numérique : le personnage parent, l’empreinte SHA-256, le journal déjà associé à l’image et les preuves complémentaires doivent correspondre. Une image de présentation, un doublon de lien ou une provenance absente ne peut pas combler un costume. Il distingue les extensions de personnages, les identités de costumes, les variantes d’édition, les boss, les stages et les projectiles. Les anciens scripts de finalisation d’un lot ne doivent pas être utilisés pour remplacer l’inventaire courant. La reconstruction du classeur accepte `GEARS_OUTPUT_DIR`, `GEARS_OUTPUT_FILENAME` et `GEARS_QA_DIR` ; sa racine de données est relative au dépôt.

## Historique de validation — V7

Le [rapport de validation V7](docs/production/VALIDATION_V7.json) contrôle **74 PNG** : 62 actifs uniques et 12 archives. Il vérifie aussi les six journaux, les 34 rattachements de costumes, les références entre sujets et images, la syntaxe JavaScript et l’identité du catalogue embarqué dans la galerie avec les JSON consolidés. Aucune erreur technique n’est signalée.

Les **8 tests d’inventaire ont réussi** : 4 tests V6 et 4 tests V7. Ils couvrent notamment la réutilisation d’un PNG sans promotion de sa qualité ou de son édition de base, le rejet des empreintes et provenances incohérentes, l’exclusion des doublons et images de présentation, ainsi que l’ordre numérique des catalogues versionnés. Les totaux et les listes de manques des rapports V7 correspondent à la couverture finale ; les six PNG V7 ont un journal associé. Ces vérifications techniques ne certifient pas la fidélité artistique.

### Validation V6 conservée

Le [rapport de validation V6](docs/production/VALIDATION_V6.json) confirme **4 tests d’inventaire V6 réussis**, la validation des données et de la syntaxe JavaScript, ainsi que **68 PNG vérifiés** : 56 actifs et 12 archivés. Aucun échec technique n’est signalé. Le résultat antérieur des **15 tests du moteur réussis** est conservé ; ces tests n’ont pas été relancés pendant cet audit sans modification du moteur. Le rendu canvas des trois rencontres est produit ; le duel illustré Marcus/RAAM a été inspecté. Les fichiers nouveaux et récupérés disposent de contrôles de dimensions, alpha, empreinte et présence.

Lors de la reprise précédente, le lancement Chromium a échoué avant l’ouverture d’une page avec `socket() failed: Operation not permitted`. Aucun nouvel essai n’est revendiqué pour V7 ; le responsive HTML/CSS réel et les commandes sur manette physique restent non validés. Le test navigateur est conservé dans `prototype/qa-browser.mjs` pour un environnement compatible.

La fidélité 1:1 reste une validation artistique à réaliser personnage par personnage, par costume et par orientation. Les poses latérales, dessins d’animation, armes séparées, pivots, hitboxes, parties de boss et calques de décor constituent les travaux de production suivants.
