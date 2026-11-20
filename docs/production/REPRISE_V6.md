# Reprise V6 — Gears of War Combats

Date de consolidation : **20 novembre 2026**.

## Résultat de la passe

Cette passe apporte **cinq nouvelles images**, récupère la référence de Dizzy Gears 2 et étend le catalogue avec **44 ajouts nets**. Le corpus contient désormais **56 PNG actifs uniques** et **12 candidats archivés**. Les sources, éditions et réserves sont reliées aux fichiers par les journaux de génération.

| Catégorie | Catalogue courant | Références associées | Travail encore ouvert |
| --- | ---: | ---: | --- |
| Personnages | 53 : 36 du roster initial + 17 extensions | 38 : 36 initiaux + Boomer Tactics + Alicia | 15 identités sans image ; certaines éditions cibles, dont Alicia Gears 5, restent aussi à produire |
| Costumes | 85 | 1 rattachement explicite : Mechanic Mac | 84 sans affectation explicite ; vérifier les images existantes avant de les déclarer absentes |
| Boss et rencontres | 31 | 5 | 26 fiches sans référence associée |
| Stages | 34 | 2 : Hollow et Gridlock | 32 fiches sans master associé ; Ephyra reste un master complémentaire |
| Validation artistique | — | 0 fidélité 1:1 certifiée | Comparaison par édition, costume, détail et orientation |
| Animation | — | 0 jeu d’animations complet | Gardes latérales, locomotion, attaques, réactions et transitions à produire |

Source de ces comptes : [coverage.json](../../production/coverage.json). Les fichiers et empreintes sont décrits dans le [manifeste courant](../../production/asset_manifest.json). Les variantes, présentations et anciennes révisions ne sont pas comptées comme des personnages supplémentaires.

## Cinq images nouvelles et un fichier récupéré

| Sujet | Édition de l’asset | Fichier | Journal | Statut |
| --- | --- | --- | --- | --- |
| Mechanic Mac | Gears 5 | [PNG](../../assets/costumes_v6/mac_mechanic_gears5_fullbody.png) | [Journal](../../data/generation_v6/mac_mechanic_record.json) | Nouveau candidat ; costume existant `mac_skin_02` |
| Boomer locuste | Gears Tactics | [PNG](../../assets/characters_v6/boomer_tactics_fullbody.png) | [Journal](../../data/generation_v6/boomer_tactics_record.json) | Nouveau candidat ; `boomer_tactics` |
| Gridlock | Gears of War 4 | [PNG](../../assets/stages_v6/gridlock_gow4_master.png) | [Journal](../../data/generation_v6/gridlock_record.json) | Nouveau master aplati ; `stage_gridlock_gow4` |
| Matriarch | Gears 5 | [PNG](../../assets/bosses_v6/matriarch_gears5_fullbody.png) | [Journal](../../data/generation_v6/matriarch_record.json) | Nouveau candidat ; boss existant `boss_matriarch` |
| Alicia Valera | Gears of War 3 — RAAM’s Shadow | [PNG](../../assets/characters_v6/alicia_valera_gow3_fullbody.png) | [Journal](../../data/generation_v6/alicia_valera_record.json) | Nouveau candidat historique ; `alternate_version` |
| Dizzy Wallin | Gears of War 2 | [PNG](../../assets/characters_v6/dizzy_gow2_fullbody.png) | [Journal](../../data/generation_v6/dizzy_record.json) | Fichier récupéré ; exclu du compte des cinq nouvelles générations |

### Alicia : conserver la différence d’édition

L’identité reste `alicia_valera`. Le catalogue vise **Gears 5 — Operation 8 Drop 2**, tandis que le PNG de cette passe est fondé sur une planche texturée face/dos **Gears 3 — RAAM’s Shadow**, créditée Epic Games 2011 / Chris Wells / Mike Buck et reproduite sur un wiki. Le journal conserve cette provenance et ses limites.

Le rattachement est `variant_relation: alternate_version`. La cible Gears 5 reste ouverte et `target_version_candidate_available` reste faux. La nouvelle image compte comme une référence du personnage ; elle ne valide ni un costume Gears 5 ni une seconde identité.

## Catalogue et ajouts nets

Le [catalogue V6](../../data/production_catalog_v6.json) ajoute **17 personnages, 10 costumes, 10 stages et 7 propositions de rencontres Boss Battle**. Il enrichit les sources de `mac_skin_02` et `boss_matriarch` en conservant ces deux identifiants existants. Le [listing détaillé](LISTING_V6.md) relie chaque sujet à l’édition cible et à ses sources.

Les sept rencontres supplémentaires utilisent le Pouncer, le DR-1, le Guardian, le Scion, le Rager, le Riftworm et le Sire. Leur classement comme Boss Battle, les phases et la balance sont des choix de cette adaptation 2D. Les équipements DR-1 et Scion restent des variantes d’arme au sein de leur fiche ; la rencontre Riftworm est conçue comme une séquence environnementale.

## Quinze personnages encore sans image

Cette liste porte sur les identités dépourvues de référence. Elle n’inclut pas Alicia, qui dispose désormais d’une variante historique, mais sa cible Gears 5 reste à produire.

| Priorité | Identifiant | Personnage | Édition cible | Prochain contrôle |
| --- | --- | --- | --- | --- |
| P0 | anthony_carmine | Anthony Carmine | Gears of War (2006) | Verrouiller le casque et l’armure 2006 ; séparer Black Steel Gears 5. |
| P0 | benjamin_carmine | Benjamin Carmine | Gears of War 2 | Compléter les vues en pied du guide Gears 2 ; distinguer son casque de celui d’Anthony. |
| P0 | jace_stratton | Jace Stratton | Gears of War 3 | Obtenir le modèle final Gears 3 ; la couverture comic ne prouve pas cette tenue. |
| P0 | michael_barrick | Michael Barrick | Gears 5 — Operation 8 Drop 2 | Fixer le rendu Gears 5 Operation 8 ; traiter RAAM’s Shadow comme autre édition. |
| P0 | minh_young_kim | Minh Young Kim | Gears of War 3 — RAAM's Shadow | Réunir des captures précises de RAAM’s Shadow, notamment le visage et l’armure. |
| P0 | ezra_loomis | Colonel Ezra Loomis | Gears of War: Judgment | Utiliser la tenue de parade Judgment et contrôler l’armure sans disques circulaires. |
| P1 | bernadette_mataki | Bernadette « Bernie » Mataki | Gears 5 — Armored Bernie | Conserver la variante Armored Bernie de Gears 5, sans fusion avec V-Day. |
| P1 | ketor_vrol | Ketor Vrol | Gears 5 — Operation 8 | Comparer la silhouette au modèle multijoueur Gears 5 ; conserver les différences avec les comics. |
| P1 | oscar_diaz | Oscar Diaz | Gears 5 — Operation 8 Drop 2 | Reprendre le modèle Gears 5 de la source Operation 8 et contrôler les accessoires. |
| P1 | prescott | Chairman Prescott | Gears 5 — Armored Prescott | Employer les références Armored Prescott ; vérifier cou, épaules et volumes propres à ce modèle. |
| P1 | hana_cole | Hana Cole | Gears 5: Hivebusters | Confronter les concepts de production au modèle final Hivebusters avant la génération. |
| P1 | aaron_griffin | Aaron Griffin | Gears of War 3 | Rassembler des vues finales Gears 3 ; comparer visage, bijoux et vêtements. |
| P1 | locust_disciple | Disciple locuste | Gears Tactics | Verrouiller le modèle Tactics ; distinguer Disciple, Drone standard et Lambent. |
| P1 | locust_zealot | Zealot locuste | Gears Tactics | Verrouiller le Zealot Tactics, séparé du Kantus et de la variante Collector’s Gears 5. |
| P1 | locust_sniper | Sniper locuste | Gears Tactics | Confirmer le modèle Tactics en pied et le Longshot dans la même édition. |

## Priorités de validation des références disponibles

1. **Boomer Tactics et Dizzy Gears 2 :** contrôler le bas du corps sur des vues complètes de leur jeu. Le journal Boomer signale aussi la reconstruction de certaines parties du Boomshot.
2. **Alicia :** vérifier visage, cicatrice et découpes d’armure sur la planche Gears 3, puis réunir séparément la référence complète Gears 5 pour la cible du catalogue.
3. **Mechanic Mac et Matriarch :** comparer les accessoires, fermetures, plaques et implantations des pointes ; préserver leurs asymétries.
4. **Marges :** reprendre l’espacement autour de Mac, Alicia et Matriarch avant atlas. Les journaux signalent des marges inférieures aux valeurs demandées, particulièrement près des pointes de la Matriarch.
5. **Orientation :** produire les gardes franchement latérales et les autres vues après validation des modèles. Les vues actuelles ne sont pas des animations.
6. **Gridlock :** comparer les façades et placements à la map Gears 4, puis produire séparément ciel, plans éloignés, architecture, véhicules, sol et premier plan. La composition actuelle a été adaptée au combat latéral.

Les vérifications consignées dans les journaux couvrent le sujet entier, le nombre de sujets, la transparence lorsqu’elle est attendue et la provenance. Elles ne certifient pas une fidélité 1:1. Les poses, armes séparées, pivots, collisions et dessins d’animation restent des étapes de production.

## Prochains stages

Les priorités ci-dessous visent de nouveaux masters. La parallaxe de Hollow et Gridlock reste à compléter en parallèle. Ephyra demeure un décor complémentaire jusqu’à l’établissement d’un rattachement précis.

| Priorité | Stage | Identifiant | Préparation |
| --- | --- | --- | --- |
| P1 | Village — Gears 5 | `stage_village_g5` | Employer la vue officielle Operation 8 Drop 2, conserver huttes et quai. |
| P1 | Dawn — Gears 5 | `stage_dawn_g5` | Fixer les vues de l’ancienne colonie minière, du bar et de la mine. |
| P1 | Ritual — Gears 5 | `stage_ritual_g5` | Comparer les concepts aux vues du jeu final avant la composition latérale. |
| P1 | Tomb — Gears 5 | `stage_tomb_g5` | Verrouiller cette map multijoueur, séparément de Tomb of the Unknown du premier jeu. |
| P1 | Nexus — Gears 5 | `stage_nexus_g5` | Réunir des vues finales de l’architecture et des rivières d’Imulsion. |
| P1 | Regency — Gears 5 | `stage_regency_g5` | Fixer les façades et l’arrière-plan en hauteur. |
| P2 | River et Clocktower — Gears 5 | `stage_river_g5`, `stage_clocktower_g5` | Employer les rééditions Gears 5 choisies dans le catalogue. |
| P2 | Ilima — RAAM’s Shadow | `stage_ilima_raams_shadow` | Choisir une séquence et des façades précises du DLC avant génération. |

Les sources de ces cibles figurent dans [production-v6.md](../references/production-v6.md).

## Prochains boss et machines

Les cinq références déjà associées couvrent **Corpser, Brumak, King Raven, Kestrel et Matriarch**. Les autres entrées gardent un statut de production ouverte.

| Priorité | Sujet | Identifiant | Prochaine étape |
| --- | --- | --- | --- |
| P0 | Berserker — Gears 2006 | `boss_berserker` | Trouver des vues finales de l’édition 2006 ; distinguer les études Ultimate Edition. |
| P1 | Wakaatu — Hivebusters | `boss_wakaatu` | Compléter les concepts par des vues finales, puis contrôler ailes, tête et queue. |
| P1 | Karn sur Shibboleth — Judgment | `boss_shibboleth` | Combiner les références exactes de la monture et du cavalier de cette édition. |
| P1 | Swarmak — Gears 4 | `boss_swarmak` | Verrouiller modèle, armement et points faibles sur références complètes. |
| P1 | Snatcher — Gears 4 | `boss_snatcher` | Contrôler anatomie, queue et ouverture ventrale sur plusieurs vues. |
| P1 | Carrier — Gears 4 | `boss_carrier` | Préparer les états de plaques ouvertes/fermées et les zones vulnérables. |
| P2 | Pouncer — Gears 4 | `boss_pouncer_g4` | Préparer la référence entière puis les états de bond de l’épreuve 2D. |
| P2 | DR-1 et Guardian — Gears 4 | `boss_dr1_g4`, `boss_guardian_g4` | Fixer une variante d’armement par image et séparer la mécanique de l’adaptation. |

## Reprendre le travail

Les commandes de travail restent celles du dépôt :

```bash
python src/consolidate_inventory.py
python src/validate_data.py
node prototype/build.mjs
node prototype/tests.cjs
```

La consolidation relit les journaux et les quatre tableaux du catalogue V6. Utiliser l’identifiant du sujet et, pour un costume, un `costume_id` explicite. Toute variante d’un autre jeu doit rester signalée comme telle. Le prototype conserve son périmètre décrit dans le [README](../../README.md) ; les nouvelles images ne rendent pas automatiquement de nouveaux combattants jouables.

## Livrables historiques

Les PDF, DOCX et classeurs du **19 novembre 2026** dans `livrables/` sont conservés comme instantanés historiques. Leurs chiffres ne constituent pas les comptes courants du lot V6. Le listing, l’inventaire, les journaux et la galerie décrivent la production actualisée.

## Suivi de publication

- **PR de travail : [#1 — ouverte en brouillon](https://github.com/darknigthmare/gear-of-wars-combats/pull/1).**
- **Branche :** `codex/gears-combats-corpus-v6-20261120`.
- Les fichiers restaurés et le lot V6 sont regroupés dans cette PR ; les commits distants y constituent la référence de publication.
