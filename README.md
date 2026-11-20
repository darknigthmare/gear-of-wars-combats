# Gears of War Combats

Corpus de conception, prototype et références visuelles consolidés le **20 novembre 2026** pour Darknigthmare.

## Consulter le projet

- [Galerie des personnages, variantes et boss](Galerie_Personnages.html)
- [Reprise V6 : nouvelles images, restants et suite](docs/production/REPRISE_V6.md)
- [Listing V6 et éditions cibles](docs/production/LISTING_V6.md)
- [Rapport de validation V6](docs/production/VALIDATION_V6.json)
- [État consolidé et limites de production](docs/production/CONSOLIDATION_2026-11-20.md)
- [Inventaire courant et couverture](production/coverage.json)
- [Prototype autonome](prototype/Gears_Combats_Prototype.html)
- [Bible illustrée v1 en PDF](livrables/Gears_of_War_Combats_Bible_v1.pdf)
- [Bible v1 en Markdown](livrables/Gears_of_War_Combats_Bible_v1.md)

Le fichier HTML du prototype embarque son code, ses styles et ses trois images utilisées. La galerie utilise les PNG du dossier `assets` : conserver son arborescence pour la consulter hors ligne.

## État courant — lot V6

Les comptes ci-dessous correspondent à l’[inventaire consolidé](production/coverage.json) et au [manifeste des fichiers](production/asset_manifest.json).

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

Contribution suivie dans la **[PR #1, ouverte en brouillon](https://github.com/darknigthmare/gear-of-wars-combats/pull/1)**, sur la branche `codex/gears-combats-corpus-v6-20261120`.

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

- `data` : roster, règles, routes, rencontres, catalogue de production V6 et journaux des générations.
- `production/asset_manifest.json` et `production/coverage.json` : inventaire courant et contrôle de couverture.
- `production/history` et les rapports datés du 19 novembre : archives de production.
- `assets` : images actives, sans références tierces téléchargées pour la recherche.
- `rejected_candidates` : anciennes révisions et candidats non sélectionnés, exclus de la couverture active.
- `prototype` : moteur, interface, HTML autonome et vérifications.
- `docs` et `livrables` : bible, provenance, rapports et livrables historiques.

```bash
python src/consolidate_inventory.py
python src/validate_data.py
node prototype/build.mjs
node prototype/tests.cjs
```

Le script de consolidation relit les fichiers, leurs journaux et `data/production_catalog_v6.json` pour actualiser le manifeste et la galerie. Il distingue les extensions de personnages, les identités de costumes, les variantes d’édition, les boss et les stages. Les anciens scripts de finalisation d’un lot ne doivent pas être utilisés pour remplacer l’inventaire courant. La reconstruction du classeur accepte `GEARS_OUTPUT_DIR`, `GEARS_OUTPUT_FILENAME` et `GEARS_QA_DIR` ; sa racine de données est relative au dépôt.

## Vérification de la reprise

Le [rapport de validation V6](docs/production/VALIDATION_V6.json) confirme **4 tests d’inventaire V6 réussis**, la validation des données et de la syntaxe JavaScript, ainsi que **68 PNG vérifiés** : 56 actifs et 12 archivés. Aucun échec technique n’est signalé. Le résultat antérieur des **15 tests du moteur réussis** est conservé ; ces tests n’ont pas été relancés pendant cet audit sans modification du moteur. Le rendu canvas des trois rencontres est produit ; le duel illustré Marcus/RAAM a été inspecté. Les fichiers nouveaux et récupérés disposent de contrôles de dimensions, alpha, empreinte et présence.

Le lancement Chromium a été tenté à nouveau, mais échoue avant l’ouverture d’une page avec `socket() failed: Operation not permitted`. Le responsive HTML/CSS réel et les commandes sur manette physique ne sont donc pas déclarés validés. Le test navigateur est conservé dans `prototype/qa-browser.mjs` pour un environnement compatible.

La fidélité 1:1 reste une validation artistique à réaliser personnage par personnage, par costume et par orientation. Les poses latérales, dessins d’animation, armes séparées, pivots, hitboxes, parties de boss et calques de décor constituent les travaux de production suivants.
