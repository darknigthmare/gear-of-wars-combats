# Listing de production V6 — Gears of War Combats

Date : 20 novembre 2026.

Ce lot poursuit le catalogue de production. Ses fiches définissent les sujets et les éditions à reproduire; elles ne signifient pas que les personnages sont jouables ou que leurs images ont déjà été produites. La disponibilité des PNG est calculée par la consolidation ; l’état courant de cette passe est repris ci-dessous.

## Comptes et déduplication

| Catégorie | Catalogue initial | Ajouts nets | Fiches existantes enrichies | Catalogue après fusion |
| --- | ---: | ---: | ---: | ---: |
| Personnages | 36 | 17 | 0 | 53 |
| Costumes | 75 | 10 | 1 | 85 |
| Boss et rencontres proposées | 24 | 7 | 1 | 31 |
| Stages | 24 | 10 | 0 | 34 |

**44 ajouts nets** au total : 17 personnages, 10 costumes, 10 stages et 7 rencontres Boss Battle proposées. Deux fiches existantes reçoivent de meilleures sources : Mechanic Mac et la Matriarch.

Le roster de conception conserve ses 36 entrées. Les 17 nouveaux personnages sont des extensions du catalogue de production et ne deviennent pas automatiquement des personnages du moteur. Les 31 entrées du catalogue de boss après fusion comprennent sept propositions de rencontres 2D; elles ne constituent pas une liste de 31 boss officiellement reconnus dans les jeux.

Identifiants à conserver : `ezra_loomis`, `alicia_valera`, `boomer_tactics`, `stage_gridlock_gow4`, `mac_skin_02`, `boss_matriarch`.

## Production effective de la passe V6

| Production | Résultat vérifié |
| --- | --- |
| Nouvelles images | **5** : Mechanic Mac Gears 5, Boomer Tactics, Gridlock Gears 4, Matriarch Gears 5, Alicia Valera Gears 3 — RAAM’s Shadow |
| Récupération | Dizzy Gears 2, avec son journal ; aucune nouvelle génération comptée pour ce fichier |
| Personnages avec référence | **38 / 53** : 36 du roster initial, Boomer Tactics et Alicia |
| Costumes avec rattachement explicite | **1 / 85** : `mac_skin_02` ; les 84 autres nécessitent un contrôle d’affectation avant de conclure qu’il faut générer une image |
| Boss et rencontres avec référence | **5 / 31** |
| Stages avec master associé | **2 / 34**, plus le master complémentaire Ephyra |
| PNG actifs / archivés | **56 / 12** fichiers uniques |
| Fidélités certifiées / jeux d’animations complets | **0 / 0** |

Alicia possède une image historique **Gears of War 3 — RAAM’s Shadow** rattachée à `alicia_valera` avec `variant_relation: alternate_version`. Sa cible catalogue **Gears 5 — Operation 8 Drop 2 reste à produire** et `target_version_candidate_available` reste faux. L’image historique améliore la couverture du personnage sans remplir cette cible d’édition.

Les détails des fichiers, les 15 personnages encore sans image et les priorités de validation figurent dans le [rapport de reprise V6](REPRISE_V6.md). Les comptes proviennent de l’[inventaire consolidé](../../production/coverage.json).

## Personnages — 17 ajouts

| Identifiant | Personnage | Édition cible | Portée de la preuve | Sources |
| --- | --- | --- | --- | --- |
| anthony_carmine | Anthony Carmine | Gears of War (2006) | Personnage confirmé; casque et plaques de la version 2006 à capturer séparément. Ne pas utiliser Black Steel Gears 5 comme costume de base. | [carmine_riftworm](../references/production-v6.md#carmine-riftworm) |
| benjamin_carmine | Benjamin Carmine | Gears of War 2 | Personnage confirmé; guide éditeur p.35. Verrouiller casque Benjamin, ne pas substituer Anthony. | [carmine_riftworm](../references/production-v6.md#carmine-riftworm), [benjamin_guide](../references/production-v6.md#benjamin-guide) |
| jace_stratton | Jace Stratton | Gears of War 3 | Identité et présence Gears 3 confirmées par DC; finaliser captures Gears 3 avant la génération. La couverture comic est une autre époque. | [jace_dc](../references/production-v6.md#jace-dc) |
| michael_barrick | Michael Barrick | Gears 5 — Operation 8 Drop 2 | Version multijoueur Gears 5 comme cible; RAAM's Shadow sera une variante distincte. | [op8_drop2](../references/production-v6.md#op8-drop2), [raam_shadow](../references/production-v6.md#raam-shadow) |
| alicia_valera | Alicia Valera | Gears 5 — Operation 8 Drop 2 | Cible Gears 5. Une référence Gears 3 — RAAM’s Shadow est disponible comme alternate_version ; elle ne remplit pas la cible Gears 5. | [op8_drop2](../references/production-v6.md#op8-drop2), [raam_shadow](../references/production-v6.md#raam-shadow) |
| minh_young_kim | Minh Young Kim | Gears of War 3 — RAAM's Shadow | Membre Zeta avec Barrick, Tai et Valera confirmé; source de contexte, captures précises requises. | [raam_shadow](../references/production-v6.md#raam-shadow) |
| ezra_loomis | Colonel Ezra Loomis | Gears of War: Judgment | Uniforme de parade, silhouette massive; armure dépourvue des disques caractéristiques habituels selon ses créateurs. | [judgment_team](../references/production-v6.md#judgment-team) |
| bernadette_mataki | Bernadette « Bernie » Mataki | Gears 5 — Armored Bernie | Armored Bernie nom officiel; armure Gears 5 cible, ne pas mélanger avec V-Day. | [op8_bundle](../references/production-v6.md#op8-bundle), [op8_twig](../references/production-v6.md#op8-twig) |
| ketor_vrol | Ketor Vrol | Gears 5 — Operation 8 | Personnage disponible dans le lot Operation 8; figer modèle multijoueur plutôt qu'inventer une synthèse comic/jeu. | [op8_bundle](../references/production-v6.md#op8-bundle), [op8_twig](../references/production-v6.md#op8-twig) |
| oscar_diaz | Oscar Diaz | Gears 5 — Operation 8 Drop 2 | Chef de Riftworm Village et ancien Gear; rendu officiel Operation 8 disponible. | [op8_drop2](../references/production-v6.md#op8-drop2) |
| prescott | Chairman Prescott | Gears 5 — Armored Prescott | Version Armored Prescott documentée par l’artiste chargé du rig de production; proportions du cou et épaules spécifiques. | [prescott_artist](../references/production-v6.md#prescott-artist) |
| hana_cole | Hana Cole | Gears 5: Hivebusters | Référence de production publiée sous le titre Hanna; comparer au modèle final du DLC avant validation. | [hana_artist](../references/production-v6.md#hana-artist) |
| aaron_griffin | Aaron Griffin | Gears of War 3 | Personnage multijoueur confirmé dans la fiche Xbox; proportions, bijoux et tenue à vérifier sur modèle exact. | [griffin_store](../references/production-v6.md#griffin-store) |
| locust_disciple | Disciple locuste | Gears Tactics | Drone modifié à l'Imulsion; distinguer d'un Drone Lambent et du skin Gears 5. | [tactics_enemies](../references/production-v6.md#tactics-enemies) |
| locust_zealot | Zealot locuste | Gears Tactics | Kantus biologiquement modifié; identité indépendante du Kantus standard. | [tactics_enemies](../references/production-v6.md#tactics-enemies) |
| locust_sniper | Sniper locuste | Gears Tactics | Variante Drone avec Longshot; silhouette et accessoires du modèle Tactics à capturer. | [tactics_enemies](../references/production-v6.md#tactics-enemies) |
| boomer_tactics | Boomer locuste | Gears Tactics | Le blog officiel Enemies identifie le Boomer de Tactics, montre son image et précise sa grande carrure, sa lenteur et son Boomshot. | [tactics_enemies](../references/production-v6.md#tactics-enemies) |

## Costumes — 10 ajouts et 1 enrichissement

Un costume partage l’identité de son personnage. La présence d’un personnage illustré ne valide pas automatiquement tous ses costumes. Les concepts d’introduction de Lahni et Keegan restent à confronter aux tenues finales du DLC.

| Identifiant | Personnage et costume | Édition | Différentiel | Sources |
| --- | --- | --- | --- | --- |
| mac_skin_02 | Mac — Mechanic Mac | Gears 5 | Source améliorée et nouvelle image rattachée ; ID existant conservé | [hivebusters_comic](../references/production-v6.md#hivebusters-comic) |
| lahni_hivebusters_intro | Lahni Kaliso — tenue d'introduction Hivebusters | Gears 5: Hivebusters | Nouveau costume documenté | [hivebusters_intro](../references/production-v6.md#hivebusters-intro) |
| keegan_hivebusters_intro | Keegan — tenue d'introduction Hivebusters | Gears 5: Hivebusters | Nouveau costume documenté | [hivebusters_intro](../references/production-v6.md#hivebusters-intro) |
| anthony_black_steel_g5 | Anthony Carmine — Black Steel Anthony Carmine | Gears 5 | Nouveau costume documenté | [anthony_artist](../references/production-v6.md#anthony-artist) |
| bernie_armored_g5 | Bernadette « Bernie » Mataki — Armored Bernie | Gears 5 | Nouveau costume documenté | [op8_bundle](../references/production-v6.md#op8-bundle) |
| sam_vday_g5 | Samantha Byrne — V-Day Sam | Gears 5 | Nouveau costume documenté | [op8_twig](../references/production-v6.md#op8-twig) |
| myrrah_black_steel_g5 | Reine Myrrah — Black Steel Queen Myrrah | Gears 5 | Nouveau costume documenté | [op8_twig](../references/production-v6.md#op8-twig) |
| fahz_hivebuster_g5 | Fahz Chutani — Hivebuster Fahz | Gears 5 | Nouveau costume documenté | [op6_twig](../references/production-v6.md#op6-twig) |
| reyna_blood_red_g5 | Reine Reyna — Blood Red Queen Reyna | Gears 5 | Nouveau costume documenté | [op6_twig](../references/production-v6.md#op6-twig) |
| swarm_drone_uir_g5 | Drone de l’Essaim — Swarm Elite Drone UIR | Gears 5 | Nouveau costume documenté | [op6_twig](../references/production-v6.md#op6-twig) |
| zealot_collectors_g5 | Zealot locuste — Collector's Zealot | Gears 5 | Nouveau costume documenté | [op6_twig](../references/production-v6.md#op6-twig) |

`mac_skin_02` désigne déjà Mechanic Mac dans le catalogue initial. Ne pas créer `costume_mac_mechanic` ou `mac_mechanic_g5`. Armored Bernie constitue une tenue du personnage Bernie, pas un second personnage.

## Stages — 10 ajouts

Les décors conservent une édition précise. Leur cadrage en combat latéral et leur découpage en parallaxe sont des adaptations du projet; un master aplati ne vaut pas production des calques séparés.

| Identifiant | Stage | Édition cible | Repères et contrôles | Sources |
| --- | --- | --- | --- | --- |
| stage_gridlock_gow4 | Gridlock | Gears of War 4 | Référence finale artiste: clocher, hôtel, bâtiment sniper, routes détruites et végétalisées. Version Gears 4 précise. | [gridlock_artist](../references/production-v6.md#gridlock-artist) |
| stage_ritual_g5 | Ritual | Gears 5 | Map multijoueur identifiée; concepts disponibles, capture finale requise. | [op8_twig](../references/production-v6.md#op8-twig), [ritual_artist](../references/production-v6.md#ritual-artist) |
| stage_tomb_g5 | Tomb | Gears 5 | Map multijoueur confirmée et travaux de production disponibles; ne pas fusionner avec Tomb of the Unknown Gears 1. | [op8_twig](../references/production-v6.md#op8-twig), [tomb_artist](../references/production-v6.md#tomb-artist) |
| stage_village_g5 | Village | Gears 5 — Operation 8 Drop 2 | Village de pêche Weilehan abandonné, huttes et petit quai décrits officiellement. | [op8_drop2](../references/production-v6.md#op8-drop2) |
| stage_dawn_g5 | Dawn | Gears 5 — Operation 8 Drop 2 | Ancienne colonie minière réoccupée par les Outsiders; bar élevé et mine retranchée. | [op8_drop2](../references/production-v6.md#op8-drop2) |
| stage_river_g5 | River | Gears 5 — Operation 5 | Réédition officielle de la map Gears 2; verrouiller rendu Gears 5. | [op5](../references/production-v6.md#op5) |
| stage_clocktower_g5 | Clocktower | Gears 5 — Operation 5 | Map de retour confirmée; pas une simple variante de Gridlock malgré le clocher. | [op5](../references/production-v6.md#op5) |
| stage_nexus_g5 | Nexus | Gears 5 — Operation 5 | Forteresse locuste sous le mont Kadar, rivières d'Imulsion. | [op5](../references/production-v6.md#op5) |
| stage_regency_g5 | Regency | Gears 5 — Operation 5 | Map en hauteur au-dessus des nuages selon l'annonce officielle. | [op5](../references/production-v6.md#op5) |
| stage_ilima_raams_shadow | Ilima — évacuation de Zeta | Gears of War 3 — RAAM's Shadow | Lieu et évacuation confirmés; cadrage particulier et façades à fixer sur captures du DLC. | [raam_shadow](../references/production-v6.md#raam-shadow) |

## Boss Battle — 7 propositions de rencontres

Ces entrées utilisent des êtres ou machines canoniques. Les phases, objectifs et valeurs de combat 2D sont à concevoir. Leur classement comme rencontre Boss Battle est une décision du projet, sans affirmation que chaque unité est un boss officiel. La taille de la créature ne doit pas être augmentée arbitrairement.

| Identifiant | Sujet | Édition | Portée de l’adaptation | Sources |
| --- | --- | --- | --- | --- |
| boss_pouncer_g4 | Pouncer | Gears of War 4 | Quadrupède, bonds, projectiles lancés par la queue, ventre vulnérable; un sujet distinct du Snatcher. | [swarm_guide](../references/production-v6.md#swarm-guide) |
| boss_dr1_g4 | DeeBee DR-1 | Gears of War 4 | Grand robot bipède, propulseurs et autodestruction. Décliner Overkill/Tri-Shot/RL-4 Salvo en équipements, pas en trois espèces. | [deebee_guide](../references/production-v6.md#deebee-guide) |
| boss_guardian_g4 | DeeBee Guardian | Gears of War 4 | Drone volant à bouclier frontal; arme issue de la variante choisie. | [deebee_guide](../references/production-v6.md#deebee-guide) |
| boss_scion_g4 | Scion | Gears of War 4 | Humanoïde massif à arme lourde et soutien des Drones; préserver le modèle hors Warden. | [swarm_guide](../references/production-v6.md#swarm-guide) |
| boss_rager_g5 | Rager — épreuve de combat | Gears 5 — Operation 8 Drop 2 | Rager confirmé, armure minimale. Toute phase enrâgée doit être sourcée séparément dans Judgment avant ajout. | [op8_drop2](../references/production-v6.md#op8-drop2) |
| boss_riftworm_g2 | Riftworm — rencontre environnementale | Gears of War 2 | Créature géante et séquence d'évasion intérieure attestées. Adapter les objectifs internes; éviter une silhouette humaine réduite à combattant. | [carmine_riftworm](../references/production-v6.md#carmine-riftworm) |
| boss_sire_g5 | Sire — épreuve de capture | Gears 5 | Existence des Sires confirmée dans l'événement Escape from Kadar; kit, anatomie détaillée et capture doivent encore être contrôlés en jeu. | [op6_twig](../references/production-v6.md#op6-twig) |

Les équipements DR-1 (Overkill, Tri-Shot, RL-4 Salvo) et Scion (Mulcher, Dropshot, Buzzkill) sont des variantes au sein de leur fiche, pas de nouvelles espèces. La rencontre Riftworm est proposée comme séquence environnementale, avec objectifs à l’intérieur de la créature. La phase de transformation du Rager n’est pas affirmée depuis le seul rendu multijoueur Gears 5; elle nécessite une référence Judgment distincte.

### Matriarch — enrichissement sans ajout net

`boss_matriarch` existe déjà. Les [snapshots de production de P-o Lévesque](https://olygraph.artstation.com/projects/3okNAo) et la [présentation d’Aryan Hanbeck](https://mediumrare.artstation.com/projects/EV8kJv) apportent des références primaires du personnage Gears 5. Les sources de gameplay antérieures restent conservées. Aucune nouvelle entrée de boss n’est créée pour la même Matriarch. Le [nouveau PNG V6](../../assets/bosses_v6/matriarch_gears5_fullbody.png) est un candidat statique disponible ; pointes, plaques et marges restent à contrôler.

## Fidélité et état des preuves

L’existence canonique d’un sujet, la présence d’un concept de production et la validation d’un asset sont trois états différents. Toutes les fiches de ce lot portent `canonical_fidelity_validated: false`. Une image pourra être retenue comme candidate après inspection; cette sélection ne vaut pas certification du modèle, du costume, des proportions ou des asymétries.

- Le guide officiel de Gears 2 identifie Benjamin Carmine page PDF 8, page imprimée 35. Compléter les vues nécessaires à la production.
- La source DC confirme Jace et son lien avec Gears 3; la couverture comic ne remplace pas son modèle de jeu.
- Les rendus Operation 8 Drop 2 restent les cibles Gears 5 pour Valera et Barrick. Le nouveau PNG de Valera représente RAAM’s Shadow et reste explicitement une autre édition.
- Gridlock est ciblé en version Gears 4, sur les captures de son artiste de production.
- Les sources de Matriarch ciblent Gears 5; elles ne documentent pas la Berserker de 2006.

## Fichiers de référence

- [Catalogue JSON V6](../../data/production_catalog_v6.json)
- [Sources et portée des références V6](../references/production-v6.md)
- [Consolidation du corpus](CONSOLIDATION_2026-11-20.md)

La liste est un lot ciblé de production et ne revendique pas l’exhaustivité de tous les jeux, romans, bandes dessinées et contenus cosmétiques Gears.
