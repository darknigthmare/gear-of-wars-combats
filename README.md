# Gears of War Combats

Corpus de conception, prototype et références visuelles consolidés le **20 novembre 2026** pour Darknigthmare.

## Consulter le projet

- [Galerie des personnages, variantes et boss](Galerie_Personnages.html)
- [État consolidé et limites de production](docs/production/CONSOLIDATION_2026-11-20.md)
- [Inventaire courant et couverture](production/coverage.json)
- [Prototype autonome](prototype/Gears_Combats_Prototype.html)
- [Bible illustrée v1 en PDF](livrables/Gears_of_War_Combats_Bible_v1.pdf)
- [Bible v1 en Markdown](livrables/Gears_of_War_Combats_Bible_v1.md)

Le fichier HTML du prototype embarque son code, ses styles et ses trois images utilisées. La galerie utilise les PNG du dossier `assets` : conserver son arborescence pour la consulter hors ligne.

## État vérifié du corpus récupéré

| Élément | État au 20 novembre 2026 |
| --- | --- |
| Personnages distincts avec une référence visuelle | **36 / 36** |
| Personnage encore sans image | Aucun dans le roster initial de 36 fiches |
| PNG de personnages, variantes et présentations | **45** |
| PNG de boss et véhicules | **4** : Corpser, Brumak, King Raven, Kestrel |
| PNG de décors complets | **2** : Ephyra et Hollow |
| Total de PNG actifs uniques | **51** |
| Anciens candidats et révisions écartés conservés | **12**, hors total actif |
| Images déclarées conformes 1:1 et prêtes à l’animation | **0** |

Les variantes d’un même personnage et les deux présentations initiales de Marcus/Kait ne constituent pas des personnages supplémentaires. Les références représentent des poses statiques ; elles ne prouvent pas la présence d’un costume exact, d’un moveset animé ou d’un personnage jouable.

### Nouveautés de la reprise

**Dominic Santiago** et **RAAM** reçoivent leur première référence en pied, portant la couverture de 33 à 35 personnages. Une référence du **Theron casqué classique** complète la variante Gears 3 tête nue déjà disponible. Les trois nouveaux PNG sont en RGBA, 1024 × 1536, avec un personnage entier par image. Leurs prompts, sources, empreintes et réserves figurent dans `data/generation_v5`.

Le Theron vise l’apparence du premier jeu ; les références effectivement utilisées comprennent une figurine de 2008 et un portrait attribué à Gears 2. L’édition exacte reste donc à valider. Les détails fins des trois images, leurs faibles marges et leur préparation aux atlas restent également à contrôler. La tentative V5 pour Dizzy avait été refusée ; son image V6 a été retrouvée et ajoutée. La partie inférieure de son costume et ses marges restent à contrôler avant animation.

**Dizzy Wallin — Gears of War 2** est récupéré dans `assets/characters_v6/dizzy_gow2_fullbody.png`, avec son journal et sa provenance. Le suivi distingue maintenant les personnages supplémentaires, les costumes attribués explicitement, les stages et les boss.

Les passes précédentes sont réunies sans effacer les candidats alternatifs. Le Kestrel, généré mais resté hors du dossier d’assets, a été récupéré. Les corrections antérieures retenues pour Clayton et Ukkon sont préservées. Les rapports du 19 novembre restent des instantanés historiques ; l’inventaire consolidé fait foi pour l’état courant.

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

Les PDF, Word et deux classeurs dans `livrables` sont les versions historiques produites le 19 novembre. Ils n’ont pas été reconstruits pour cette passe ; leurs décomptes d’images peuvent donc être antérieurs à ceux des JSON et de la galerie courants. Les deux masters de décor ne remplacent pas les 144 calques séparés à produire.

## Organisation et reprise

- `data` : catalogue canonique, règles, routes, rencontres et journaux des générations.
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

Le script de consolidation relit les fichiers et leurs journaux pour actualiser le manifeste et la galerie. Les anciens scripts de finalisation d’un lot ne doivent pas être utilisés pour remplacer l’inventaire courant. La reconstruction du classeur accepte `GEARS_OUTPUT_DIR`, `GEARS_OUTPUT_FILENAME` et `GEARS_QA_DIR` ; sa racine de données est relative au dépôt.

## Vérification de la reprise

Les **15 tests existants du moteur passent**, et la validation des identifiants, rivaux, routes, coups, phases, stages et estimations d’animation ne signale aucune erreur. Le rendu canvas des trois rencontres est produit ; le duel illustré Marcus/RAAM a été inspecté. Les fichiers nouveaux et récupérés disposent de contrôles de dimensions, alpha, empreinte et présence.

Le lancement Chromium a été tenté à nouveau, mais échoue avant l’ouverture d’une page avec `socket() failed: Operation not permitted`. Le responsive HTML/CSS réel et les commandes sur manette physique ne sont donc pas déclarés validés. Le test navigateur est conservé dans `prototype/qa-browser.mjs` pour un environnement compatible.

La fidélité 1:1 reste une validation artistique à réaliser personnage par personnage, par costume et par orientation. Les poses latérales, dessins d’animation, armes séparées, pivots, hitboxes, parties de boss et calques de décor constituent les travaux de production suivants.
