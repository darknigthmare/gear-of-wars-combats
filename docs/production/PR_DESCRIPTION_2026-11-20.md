# Gears Combats : restaurer le corpus et poursuivre la production V6

## Pourquoi

Le dépôt distant ne contenait que son commit initial, alors que la bible, le prototype et les générations précédentes existaient dans plusieurs reprises locales. Cette PR réunit les fichiers récupérés et poursuit le listing et la génération avec des éditions de référence explicites.

## Corpus récupéré

- Restaure 277 fichiers : bible PDF/DOCX, deux tableurs, données de combat, prototype, galerie, PNG, références et journaux de génération.
- Récupère notamment Dizzy Gears of War 2 et les documents historiques du pack V2. Les 36 personnages du roster initial disposent désormais d'au moins une référence statique.
- Préserve les variantes, les 12 révisions visuelles écartées et les livrables du 19 novembre avec leur statut historique. Les inventaires JSON et la galerie portent l'état courant.

## Nouveau lot V6

| Catégorie | Nouvelle image | Édition et portée |
|---|---|---|
| Personnage | Boomer avec Boomshot | Gears Tactics ; bas du corps et parties cachées reconstruits |
| Personnage | Alicia Valera | Gears of War 3 — RAAM's Shadow ; variante distincte de la cible Gears 5 encore manquante |
| Costume | Mechanic Mac | Gears 5 ; rattaché au costume existant `mac_skin_02` |
| Boss | Matriarch | Gears 5 ; rattachée à la fiche existante `boss_matriarch` |
| Stage | Gridlock | Gears of War 4 ; master aplati adapté au cadrage de combat 2D |

Chaque génération possède un journal avec sources, prompt, empreinte SHA-256, dimensions, vérifications et points restant à contrôler. Les PNG ont été décodés et inspectés ; les quatre sujets isolés ont un véritable canal alpha.

Le catalogue ajoute **44 fiches nettes** : 17 personnages, 10 costumes, 10 stages et 7 rencontres proposées pour le mode Boss Battle. Deux fiches existantes sont enrichies, sans duplication de Mac ni de la Matriarch. Les sept nouvelles rencontres sont des adaptations de jeu documentées, pas une affirmation de classement officiel en boss.

## Couverture actuelle

| Catégorie | Références rattachées | Fiches |
|---|---:|---:|
| Personnages du roster initial | 36 | 36 |
| Personnages de l'extension de production | 2 | 17 |
| Ensemble des personnages | 38 | 53 |
| Costumes avec affectation explicite | 1 | 85 |
| Boss, véhicules et rencontres | 5 | 31 |
| Stages | 2 | 34 |

**56 PNG actifs uniques** sont présents : 47 images de personnages et variantes, un costume, cinq boss ou véhicules et trois décors. Le décor Ephyra reste une référence supplémentaire sans affectation à une fiche de stage. Les 84 costumes sans affectation explicite demandent d'abord une revue des images existantes ; ce nombre ne prouve pas l'absence de toute image correspondante.

## Vérification

- Validation des données : aucune erreur.
- Quatre tests de régression de l'inventaire V6 réussis.
- Quinze tests du moteur réussis pendant cette reprise ; le moteur n'est pas modifié par le nouveau lot visuel.
- Inventaire régénéré à partir des fichiers présents ; aucune alerte du consolidateur.
- Empreintes des fichiers publiés comparées aux objets Git locaux.
- La vérification dans Chromium reste bloquée avant ouverture de page par `socket() failed: Operation not permitted`. Aucun résultat de navigation responsive réel n'est revendiqué.

## Fidélité et limites

L'objectif reste une reproduction fidèle à l'édition indiquée. **Aucune fidélité 1:1 n'est encore certifiée**, et aucune série d'animations complète n'est livrée. Les journaux distinguent les détails observés des reconstructions et conservent les écarts à traiter : proportions et armures, visage et cicatrice d'Alicia, détails du Boomer, placement des plaques et pointes de la Matriarch, marges et poses de combat. Gridlock doit encore être séparé en couches et adapté à la scène jouable.

Les corrections antérieures de Del, Lizzie, Reyna et Skorge restent ouvertes. La version Marcus Ultimate Edition et l'édition de Hoffman conservent leurs réserves. Le prototype comporte toujours ses trois rencontres existantes ; les nouvelles références ne rendent pas automatiquement tout le catalogue jouable.

## Reprise

- `Galerie_Personnages.html` : parcourir les images et leurs statuts.
- `docs/production/LISTING_V6.md` : fiches, éditions et nouveaux sujets documentés.
- `docs/production/REPRISE_V6.md` : éléments manquants et ordre de travail.
- `docs/production/VALIDATION_V6.json` : preuves de validation et limites.
- `data/generation_v6/` et `docs/references/production-v6.md` : provenance du nouveau lot.
