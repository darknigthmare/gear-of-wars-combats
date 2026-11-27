# Consolidation — Gears of War Combats — 2026-11-27

## État vérifié des fichiers

Les anciennes passes ont été réunies avec les nouvelles sorties réellement présentes. Les nombres ci-dessous proviennent du recalcul de [l’inventaire](../../production/asset_manifest.json) et de [la couverture](../../production/coverage.json). Ils remplacent les chiffres des rapports historiques pour le suivi courant.

| Contenu | Quantité |
| --- | ---: |
| Personnages possédant au moins une référence | **36 / 36** |
| Personnages sans référence | **0** |
| Personnages supplémentaires du catalogue avec une référence | 18 / 21 |
| Costumes avec une attribution visuelle explicite | 68 / 85 |
| Appellations de costume résolues par alias documenté | 2 |
| PNG actifs de personnages, alternatives et présentations incluses | 63 |
| PNG actifs classés comme costumes | 31 |
| Boss avec une référence | 30 / 34 |
| Fiches d’arènes associées à un master | 34 / 34 |
| Masters de décor, Ephyra complémentaire inclus | 35 |
| Projectiles avec une référence statique | 5 / 9 |
| PNG actifs de projectiles | 5 |
| PNG actifs uniques | 164 |
| Anciennes versions écartées conservées séparément | 18 |
| Personnages certifiés conformes 1:1 | **0** |
| Ensembles d’animations dessinées finalisés | **0** |

**Personnages encore sans image : Aucun personnage du roster sans référence.**

La présence d’un PNG signifie une référence statique disponible, pas un personnage jouable ni un costume certifié. [La galerie complète](../../Galerie_Personnages.html) affiche les 36 personnages du roster de conception, les 21 extensions de personnages, les 85 costumes, les 34 boss, les 34 arènes et les 9 projectiles, avec des cartes explicites pour les manquants. Les extensions de production ne modifient pas le roster du moteur. Ephyra reste un master complémentaire, sans attribution arbitraire à une arène précise. Une référence de projectile ne valide ni sa trajectoire, ni ses collisions, ni son effet à l’impact.

Les costumes hérités des fiches initiales restent sans attribution tant qu’un `costume_id` explicite n’est pas fourni. Cela signifie une liaison visuelle à vérifier, et non nécessairement une image à régénérer. Les mappings `data/costume_asset_links_v*.json` sont lus dans leur ordre numérique et conservent l’audit [V7](../../data/costume_asset_links_v7.json). Ils rattachent les images existantes à leur costume après vérification du personnage, de la provenance et de l’empreinte ; ils ne dupliquent aucun PNG et ne certifient aucune fidélité. Un master de décor ne vaut pas validation de ses calques de parallaxe séparés.

Les mappings `data/costume_reference_aliases_v*.json` rapprochent deux appellations explicitement documentées du même costume. Ils exigent le même personnage, la même édition, un candidat de référence, son empreinte et ses preuves. Les deux entrées peuvent partager le même PNG sans lui ajouter un second `costume_id` physique ; le compteur d’alias n’augmente pas le nombre d’images et ne modifie pas leurs réserves de qualité.

## Ce qui a été récupéré

- Le corpus initial : bible, prototype, données de conception, 16 personnages représentés et deux décors. Les fichiers copiés lors des deux premières passes sont identiques ; les doubles copies binaires n’augmentent pas les comptes.
- La passe v4 : neuf références de personnages et quatre boss. Kestrel était généré mais resté hors d’`assets` ; il est récupéré et contrôlé, avec [un constat distinct](../../data/generation_v4/recovery_kestrel_2026-11-20.json).
- Le lot de reprise : 14 références sélectionnées, ses sources, ses prompts et son rapport visuel. Clayton v02, Theron v02 et Ukkon v02 sont conservés ; leurs trois anciennes versions sont archivées dans `rejected_candidates/characters_20261119/`.
- Les six candidats v4 recouvrant des personnages du lot de reprise sont conservés et consultables comme alternatives. Ils ne sont pas six personnages supplémentaires.

## Nouvelles sorties présentes

| Sujet | Variante demandée | Fichier |
| --- | --- | --- |
| Carrier | Gears of War 4 — Carrier, pose fixe | [PNG](../../assets/bosses_v10/carrier_gears4_fullbody.png) |
| Centaur | Gears of War 2 — Centaur, pose fixe | [PNG](../../assets/bosses_v10/centaur_gears2_fullbody.png) |
| Reaver | Gears of War 2 — Reaver, pose fixe | [PNG](../../assets/bosses_v10/reaver_gears2_mount_only_fullbody.png) |
| Snatcher | Gears of War 4 — Snatcher, pose fixe | [PNG](../../assets/bosses_v10/snatcher_gears4_fullbody.png) |
| Swarmak | Gears of War 4 — Swarmak, pose fixe | [PNG](../../assets/bosses_v10/swarmak_gears4_fullbody.png) |
| Hive Beast | Gears of War 4 — Hive Beast, portion émergente attestée et quatre tentacules, pose fixe | [PNG](../../assets/bosses_v11/hive_beast_gears4_visible_portion.png) |
| Hydra d’Ukkon | Gears Tactics — Hydra d’Ukkon, tête et torse supérieur attestés, sans cavalier | [PNG](../../assets/bosses_v11/hydra_ukkon_tactics_upperbody_portion.png) |
| Lambent Brumak | Gears of War 2 — Lambent Brumak final, assemblage statique du modèle attesté | [PNG](../../assets/bosses_v11/lambent_brumak_gears2_model_assembly.png) |
| Lambent Leviathan | Gears of War 3 — Lambent Leviathan, volume visible du modèle, pose fixe | [PNG](../../assets/bosses_v11/lambent_leviathan_gears3_visible_model.png) |
| Leviathan | Gears of War 2 — Leviathan original, modèle recourbé et pose fixe | [PNG](../../assets/bosses_v11/leviathan_gears2_fullbody.png) |
| Rager — forme normale Gears 5 | Rager normal de Gears 5 Op8 Drop2, échelle humanoïde, mains vides | [PNG](../../assets/bosses_v11/rager_gears5_normal_fullbody.png) |
| Flock | Gears 5 — essaim de Leeches, formation collective recomposée | [PNG](../../assets/bosses_v12/flock_gears5_swarm.png) |
| Kraken | Gears 5 — tête et manteau exposés du Kraken, ensemble central seulement | [PNG](../../assets/bosses_v12/kraken_gears5_head_mantle.png) |
| Riftworm — extérieur Gears of War 2 | Riftworm Gears of War 2 — corps extérieur complet, vue latérale de modèle | [PNG](../../assets/bosses_v13/riftworm_g2_exterior.png) |
| Matriarch | Gears 5 — modèle de campagne | [PNG](../../assets/bosses_v6/matriarch_gears5_fullbody.png) |
| Shibboleth seul — monture sans Karn | Gears of War: Judgment — monture seule ; Karn absent ; duo non complet | [PNG](../../assets/bosses_v7/shibboleth_judgment_mount_only_fullbody.png) |
| Berserker Lambent | Gears of War 3 — poitrine ouverte, pose de référence | [PNG](../../assets/bosses_v8/lambent_berserker_gow3_fullbody.png) |
| Tempest seul — monture sans Myrrah | Gears of War 3 — monture seule ; Myrrah absente ; duo non complet | [PNG](../../assets/bosses_v8/tempest_gow3_mount_only_fullbody.png) |
| Berserker | Gears of War (2006) — candidat guidé par promotion d'époque et artbook | [PNG](../../assets/bosses_v9/berserker_gears2006_fullbody.png) |
| DR-1 DeeBee | Gears of War 4 — DR-1 bleu avec Overkill | [PNG](../../assets/bosses_v9/dr1_gears4_fullbody.png) |
| Guardian DeeBee | Gears of War 4 — Guardian Tri-Shot, drone seul sans bouclier actif | [PNG](../../assets/bosses_v9/guardian_gears4_fullbody.png) |
| Pouncer | Gears of War 4 — Pouncer, pose fixe | [PNG](../../assets/bosses_v9/pouncer_gears4_fullbody.png) |
| Silverback | Gears of War 3 — exosquelette seul, sans pilote | [PNG](../../assets/bosses_v9/silverback_gears3_fullbody.png) |
| Aaron Griffin | Gears of War 3 — tenue originale du modèle Mike Kime (2011) | [PNG](../../assets/characters_v10/aaron_griffin.png) |
| Oscar Diaz | Last Stand Oscar — Operation 8 Drop 2 (2021) | [PNG](../../assets/characters_v10/oscar_diaz.png) |
| Anthony Carmine | Original Anthony Carmine — référence figurine licenciée NECA SDCC 2008 | [PNG](../../assets/characters_v15/anthony_carmine.png) |
| Jace Stratton | Gears of War 3 | [PNG](../../assets/characters_v15/jace_stratton.png) |
| Minh Young Kim | Minh Young Kim — RAAM's Shadow (2011) | [PNG](../../assets/characters_v15/minh_young_kim.png) |
| Dominic Santiago | Gears of War (2006) — COG armor | [PNG](../../assets/characters_v5/dom_gow1_fullbody.png) |
| Général RAAM | Gears of War (2006 / portage PC original) | [PNG](../../assets/characters_v5/raam_gow1_fullbody.png) |
| Garde Theron | Theron Guard classique casqué, cible GoW 2006 ; édition exacte non validée | [PNG](../../assets/characters_v5/theron_gow1_fullbody.png) |
| Alicia Valera | Gears of War 3 — RAAM's Shadow, armure standard sans casque | [PNG](../../assets/characters_v6/alicia_valera_gow3_fullbody.png) |
| Boomer | Gears Tactics — Boomer standard avec Boomshot | [PNG](../../assets/characters_v6/boomer_tactics_fullbody.png) |
| Dizzy Wallin | Gears of War 2 — tenue de pilote de Betty | [PNG](../../assets/characters_v6/dizzy_gow2_fullbody.png) |
| Colonel Ezra Loomis | Gears of War: Judgment — uniforme de parade, bras croisés | [PNG](../../assets/characters_v7/ezra_loomis_judgment_fullbody.png) |
| Michael Barrick | Gears of War 3 — RAAM's Shadow, armure standard sans casque | [PNG](../../assets/characters_v7/michael_barrick_gow3_raams_shadow_fullbody.png) |
| Adam Fenix | Gears of War 3 — Soldier Adam, personnage multijoueur | [PNG](../../assets/characters_v8/adam_fenix_gow3_multiplayer_fullbody.png) |
| Alex Brand | Gears of War: Judgment — apparence multijoueur, personnage seul | [PNG](../../assets/characters_v8/alex_brand_judgment_fullbody.png) |
| Karn — état intact | Gears of War: Judgment — Karn intact, personnage seul sans Shibboleth | [PNG](../../assets/characters_v8/karn_judgment_intact_fullbody.png) |
| Bernadette « Bernie » Mataki — Armored Bernie | Gears 5 — Armored Bernie, pose de base fixe | [PNG](../../assets/characters_v9/bernie_armored_gears5_fullbody.png) |
| Hana Cole | Gears 5 — Scientist Hana, référence multijoueur Operation 7 à comparer à Hivebusters | [PNG](../../assets/characters_v9/hana_cole.png) |
| Ketor Vrol | Gears 5 — Ketor Vrol multijoueur Operation 8 | [PNG](../../assets/characters_v9/ketor_vrol.png) |
| Disciple locuste | Gears Tactics — Disciple standard tête nue, harnais à Imulsion | [PNG](../../assets/characters_v9/locust_disciple.png) |
| Sniper locuste | Gears Tactics — Sniper Drone standard avec Longshot | [PNG](../../assets/characters_v9/locust_sniper.png) |
| Zealot locuste | Gears Tactics — Zealot standard avec casque pointu | [PNG](../../assets/characters_v9/locust_zealot.png) |
| Damon Baird — Lieutenant (Judgment) | Lieutenant Baird — modèle original Judgment | [PNG](../../assets/costumes_v10/baird_skin_01.png) |
| Damon Baird — DB Industries (Gears 5) | DB Industries Baird — âgé, blouse de laboratoire (campagne et Operation 3) | [PNG](../../assets/costumes_v10/baird_skin_04.png) |
| Reine Myrrah — Black Steel Queen Myrrah | Gears 5 — Black Steel Queen Myrrah, pose fixe en pied | [PNG](../../assets/costumes_v10/myrrah_black_steel_gears5_fullbody.png) |
| Samantha Byrne — V-Day Sam | Gears 5 — V-Day Sam, pose fixe en pied | [PNG](../../assets/costumes_v10/sam_vday_gears5_fullbody.png) |
| Augustus Cole — Gears 5 Operation 3, variante multijoueur | Cole du rendu officiel multijoueur Operation 3 ; correspondance avec le vétéran de campagne non établie | [PNG](../../assets/costumes_v11/cole_skin_04.png) |
| Dominic Santiago — Campagne Gears of War 3 | Dom barbu de campagne, cuirasse sans manches | [PNG](../../assets/costumes_v11/dom_skin_04.png) |
| Kait Diaz — Outsider Gears of War 4 | Kait Outsider — veste courte brune, Gears of War 4 | [PNG](../../assets/costumes_v11/kait_skin_01.png) |
| Marcus Fenix — Campagne Gears of War 2006 | Marcus du premier Gears original, modèle du port PC ; équivalence Xbox 360 2006 à vérifier | [PNG](../../assets/costumes_v11/marcus_skin_02.png) |
| Marcus Fenix — Vétéran Gears 5 | Marcus âgé et barbu en armure Gears 5 | [PNG](../../assets/costumes_v11/marcus_skin_04.png) |
| Garron Paduk — Vétéran Gears 5 | Paduk âgé — armure UIR verte de campagne Gears 5 | [PNG](../../assets/costumes_v11/paduk_skin_02.png) |
| Clayton Carmine — modèle multijoueur Gears 5 Operation 3 | Modèle multijoueur Gears 5 Operation 3 montré par Xbox Wire le 31 mars 2020 | [PNG](../../assets/costumes_v12/clayton_gears5_operation3.png) |
| Del Walker — Outsider Gears 4, candidat de concept | Del Outsider — concept Goran Bukvic/Microsoft, corroboration partielle campagne | [PNG](../../assets/costumes_v12/del_skin_01.png) |
| Dominic Santiago — E-Day | Dom jeune — modèle de production E-Day | [PNG](../../assets/costumes_v12/dom_eday.png) |
| JACK — Gears Tactics | JACK Tactics — robot de soutien à quatre optiques, bras manipulateur et outil distincts | [PNG](../../assets/costumes_v12/jack_tactics.png) |
| JD Fenix — Outsider Gears 4, candidat de concept | JD Outsider — concept Microsoft avril 2016, corroboration partielle campagne | [PNG](../../assets/costumes_v12/jd_skin_01.png) |
| Marcus Fenix — E-Day | Marcus jeune — modèle de production E-Day | [PNG](../../assets/costumes_v12/marcus_eday.png) |
| Reine Reyna — Blood Red Queen Reyna | Blood Red Queen Reyna — skin multijoueur Operation 6, tentacules inférieurs reconstitués | [PNG](../../assets/costumes_v12/reyna_blood_red_g5.png) |
| Drone de l'Essaim — Gears 5 standard | Swarm Drone Rifleman — modèle standard Gears 5 | [PNG](../../assets/costumes_v12/swarm_drone_skin_02.png) |
| Drone de l'Essaim — Swarm Elite Drone UIR | UIR Elite Drone — skin multijoueur Gears 5 Operation 6 | [PNG](../../assets/costumes_v12/swarm_drone_uir_g5.png) |
| Zealot locuste — Collector's Zealot | Collector's Zealot — skin multijoueur Gears 5 Operation 6 | [PNG](../../assets/costumes_v12/zealot_collectors_g5.png) |
| Dizzy Wallin — standard Gears of War 3 | Dizzy standard Gears 3 — rendu Epic 2011, copie de diffusion | [PNG](../../assets/costumes_v13/dizzy_skin_02.png) |
| Victor Hoffman — campagne Gears of War 3 | Hoffman Gears 3 — modèle de production Epic | [PNG](../../assets/costumes_v13/hoffman_skin_02.png) |
| JD Fenix — CGU au début de Gears 5 | JD CGU non cicatrisé — début de campagne Gears 5 | [PNG](../../assets/costumes_v13/jd_skin_02.png) |
| Lahni — campagne Hivebusters / Brash Brigade | Brash Brigade Lahni — tenue en armure du début du DLC, modèle final | [PNG](../../assets/costumes_v13/lahni_skin_01.png) |
| Locust Drone — modèle multijoueur Gears of War: E-Day | Modèle multijoueur visible dans la galerie officielle E-Day | [PNG](../../assets/costumes_v13/locust_drone_eday_multiplayer.png) |
| Reyna Diaz humaine / Outsider — Gears of War 4 | Reyna Diaz humaine Outsider — modèle final Gears of War 4 | [PNG](../../assets/costumes_v14/reyna_human_g4_hairfix.png) |
| Keegan — Onyx Guard Gears 5 Hivebusters | Onyx Guard Keegan — modèle cinématique temps réel final du DLC | [PNG](../../assets/costumes_v15/keegan_skin_02.png) |
| Skorge — modèle multijoueur Gears 5 Opération 5 | Apparence multijoueur standard, Opération 5 | [PNG](../../assets/costumes_v15/skorge_skin_02.png) |
| Mac — Mechanic Mac | Gears 5 — Mechanic Mac (skin Hivebusters) | [PNG](../../assets/costumes_v6/mac_mechanic_gears5_fullbody.png) |
| Augustus Cole — Thrashball Cole | Gears of War 3 — Thrashball Cole | [PNG](../../assets/costumes_v7/cole_thrashball_gow3_fullbody.png) |
| Marcus Fenix — campagne Gears of War 3 | Gears of War 3 — armure de campagne | [PNG](../../assets/costumes_v8/marcus_campaign_gow3_fullbody.png) |
| Leech individuel — Gears 5 | Leech individuel — modèle final Gears 5, forme déployée | [PNG](../../assets/creatures_v14/leech_g5.png) |
| Ticker organique — Gears of War: E-Day | Ticker E-Day — modèle organique sans harnais ni bombe, partie inférieure du rendu final | [PNG](../../assets/creatures_v14/ticker_eday.png) |
| Wretch — modèle organique Gears of War: E-Day | Wretch E-Day — modèle organique sans armure publié par Antoine Verney-Carron | [PNG](../../assets/creatures_v14/wretch_eday.png) |
| Grenade fumigène — concept officiel C | Gears of War 4 — Smoke Grenade, variante C du concept Jarold Sng | [PNG](../../assets/projectiles_v10/smoke_grenade_gow4_concept_c.png) |
| Carrier Minion / Canker — Gears of War 4 | Carrier Minion / Canker — modèle final Gears of War 4 | [PNG](../../assets/projectiles_v14/canker_g4.png) |
| Buzzkill — lame circulaire | Gears of War 4 — projectile isolé, pose fixe | [PNG](../../assets/projectiles_v9/buzzkill_sawblade_gow4.png) |
| Dropshot — projectile foreuse | Gears of War 4 — projectile isolé, pose fixe | [PNG](../../assets/projectiles_v9/dropshot_drill_gow4.png) |
| Grenade Bolo / Frag | Gears of War 3 — projectile isolé, pose fixe | [PNG](../../assets/projectiles_v9/frag_grenade_gow3.png) |
| Azura — terrasse de Pinnacle Tower | Gears of War 3 — terrasse et fontaines devant Pinnacle Tower adaptées au combat latéral | [PNG](../../assets/stages_v10/azura_tower_gears3_terrace_master.png) |
| Lac des Hollows — pont du bateau locuste | Gears of War 2 — lac souterrain depuis un pont de bateau adapté au combat latéral | [PNG](../../assets/stages_v10/hollow_lake_gears2_boat_master.png) |
| Jacinto — au bord de la chute | Gears of War 2 — terrasses effondrées de Jacinto adaptées au combat latéral | [PNG](../../assets/stages_v10/jacinto_gears2_collapse_master.png) |
| New Hope — couloir gelé | Gears 5 — New Hope, couloir de recherche abandonné adapté au combat latéral | [PNG](../../assets/stages_v10/new_hope_gears5_corridor_master.png) |
| Ritual — cour du temple | Gears 5 — Ritual, cour adaptée au combat latéral | [PNG](../../assets/stages_v10/ritual_gears5_courtyard_master.png) |
| CNV Sovereign — pont jardiné | Gears of War 3 — pont extérieur jardiné du Sovereign adapté au combat latéral | [PNG](../../assets/stages_v10/sovereign_deck_gears3_master.png) |
| Forêt de Stromson — route et derrick | Gears of War 2 — lisière de Stromson avec derrick immobilisé, adaptée au combat latéral | [PNG](../../assets/stages_v10/stromson_forest_gears2_master.png) |
| Tomb — cour du cimetière | Gears 5 — Tomb, cour adaptée au combat latéral | [PNG](../../assets/stages_v10/tomb_gears5_cemetery_master.png) |
| Place de Halvo Bay — Plaza for the Tyran Dead | Gears of War: Judgment | [PNG](../../assets/stages_v11/halvo_plaza_judgment_courthouse_night_master.png) |
| Ilima — évacuation de Zeta | Gears of War 3 — RAAM's Shadow | [PNG](../../assets/stages_v11/ilima_raams_shadow_evacuation_square_master.png) |
| Laboratoire sous le mont Kadar — chambre de confinement gelée | Chambre à cuve sphérique du niveau Mt Kadar, adaptée en arène latérale | [PNG](../../assets/stages_v11/kadar_lab_gears5_containment_chamber_master.png) |
| Rempart de New Ephyra | Gears 5 — Act IV Chapter 2: The Fall | [PNG](../../assets/stages_v11/new_ephyra_gears5_final_battlement_master.png) |
| Settlement 5 — rue et portail de chantier | Rue du niveau Raid et portail de sécurité, adaptation latérale issue de captures finales | [PNG](../../assets/stages_v11/settlement5_gears4_security_gate_master.png) |
| Galangi — plage et lisière tropicale | Plage de Galangi — rivage endommagé, adaptation latérale de la cinématique | [PNG](../../assets/stages_v11/stage_galangi_beach.png) |
| Galangi — intérieur volcanique | Galangi — coulées de lave et corniche adaptée au combat latéral | [PNG](../../assets/stages_v11/stage_galangi_volcano.png) |
| Laboratoire d’Ukkon — concept de la finale | Laboratoire d’Ukkon — adaptation latérale du concept Act3Finale_ArenaFeedback de Malte Langheim | [PNG](../../assets/stages_v11/stage_tactics_lab.png) |
| Hangar d’entraînement — création du projet | Arène originale — hangar d’essai COG; matériaux inspirés de Training Grounds Gears 5 | [PNG](../../assets/stages_v11/stage_training_hangar.png) |
| Piste d’essai — création du projet | Arène originale — piste d’essai COG; matériaux inspirés de Training Grounds Gears 5 | [PNG](../../assets/stages_v11/stage_training_range.png) |
| Ruche de l’Essaim — chambre voûtée colonisée | Composition latérale originale d’un intérieur de ruche fondée sur les environnements Swarm finaux de Gears 4 | [PNG](../../assets/stages_v11/swarm_hive_gears4_infested_chamber_master.png) |
| Cour de ravitaillement — composition originale inspirée de Tactics | Création de cour logistique pour le projet à partir du biome COG Industrial ; aucun dépôt canonique nommé revendiqué | [PNG](../../assets/stages_v11/tactics_depot_cog_industrial_courtyard_master.png) |
| Tollen Dam — cour d’entrée du barrage | Façade et accès du barrage de Tollen recomposés pour une bande de combat latérale | [PNG](../../assets/stages_v11/tollen_dam_gears4_entrance_master.png) |
| Aéroport de Vasgar — terminal et contrôle de sécurité | Terminal de la carte Vasgar, composition latérale issue de deux vues de production finales | [PNG](../../assets/stages_v11/vasgar_airport_gears5_terminal_master.png) |
| Gridlock | Gears of War 4 — cadrage de combat 2D adapté | [PNG](../../assets/stages_v6/gridlock_gow4_master.png) |
| Dawn | Gears 5 — Operation 8, colonie minière adaptée au combat 2D | [PNG](../../assets/stages_v7/dawn_gears5_master.png) |
| Village | Gears 5 — Operation 8, intérieur cérémoniel adapté au combat 2D | [PNG](../../assets/stages_v7/village_gears5_master.png) |
| Nexus — galerie souterraine | Gears 5 — Operation 5, galerie souterraine adaptée au combat 2D | [PNG](../../assets/stages_v8/nexus_gears5_master.png) |
| Regency | Gears 5 — Operation 5, terrasse cérémonielle adaptée au combat 2D | [PNG](../../assets/stages_v8/regency_gears5_master.png) |
| Anvil Gate — cour de la porte 02 | Gears of War 3 — cour intérieure de la porte 02 adaptée au combat latéral | [PNG](../../assets/stages_v9/anvil_gate_gears3_master.png) |
| Clocktower | Gears 5 — Clocktower, terrasse nocturne adaptée au combat latéral | [PNG](../../assets/stages_v9/clocktower_gears5_master.png) |
| Haldane Hall — jardin du domaine Fenix | Gears of War 2006 — terrasse du jardin et escalier du domaine adaptés au combat latéral | [PNG](../../assets/stages_v9/fenix_estate_gow2006_garden_master.png) |
| House of Sovereigns | Gears of War (2006) — parvis extérieur adapté au combat latéral | [PNG](../../assets/stages_v9/house_of_sovereigns_gow2006_master.png) |
| River — taverne | Gears 5 — River, intérieur de taverne adapté au combat latéral | [PNG](../../assets/stages_v9/river_gears5_tavern_master.png) |
| Tyro Pillar — pont de fret | Gears of War 2006 — pont de fret adapté au combat latéral | [PNG](../../assets/stages_v9/tyro_pillar_gow2006_master.png) |

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
python src/consolidate_inventory.py --report-suffix V15
```

Cette commande vérifie les fichiers, recalcule empreintes, dimensions, alpha et comptes, réconcilie les références du roster, puis reconstruit l’inventaire et la galerie autonome. Elle lit les résultats des passes v5 et suivantes sans les modifier. `src/build_asset_manifest.py` appelle également ce recalcul avant de renouveler la file de production. `src/finalize_generation_v2.py` reste un script historique de v2, pas la commande courante de consolidation.

Ce rapport décrit les fichiers préparés. Il ne constitue pas une preuve de publication GitHub, qui doit être vérifiée séparément.
