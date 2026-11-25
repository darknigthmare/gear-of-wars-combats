# Consolidation — Gears of War Combats — 2026-11-25

## État vérifié des fichiers

Les anciennes passes ont été réunies avec les nouvelles sorties réellement présentes. Les nombres ci-dessous proviennent du recalcul de [l’inventaire](../../production/asset_manifest.json) et de [la couverture](../../production/coverage.json). Ils remplacent les chiffres des rapports historiques pour le suivi courant.

| Contenu | Quantité |
| --- | ---: |
| Personnages possédant au moins une référence | **36 / 36** |
| Personnages sans référence | **0** |
| Personnages supplémentaires du catalogue avec une référence | 13 / 20 |
| Costumes avec une attribution visuelle explicite | 38 / 85 |
| PNG actifs de personnages, alternatives et présentations incluses | 58 |
| PNG actifs classés comme costumes | 3 |
| Boss avec une référence | 13 / 31 |
| Fiches d’arènes associées à un master | 12 / 34 |
| Masters de décor, Ephyra complémentaire inclus | 13 |
| Projectiles avec une référence statique | 3 / 8 |
| PNG actifs de projectiles | 3 |
| PNG actifs uniques | 90 |
| Anciennes versions écartées conservées séparément | 12 |
| Personnages certifiés conformes 1:1 | **0** |
| Ensembles d’animations dessinées finalisés | **0** |

**Personnages encore sans image : Aucun personnage du roster sans référence.**

La présence d’un PNG signifie une référence statique disponible, pas un personnage jouable ni un costume certifié. [La galerie complète](../../Galerie_Personnages.html) affiche les 36 personnages du roster de conception, les 20 extensions de personnages, les 85 costumes, les 31 boss, les 34 arènes et les 8 projectiles, avec des cartes explicites pour les manquants. Les extensions de production ne modifient pas le roster du moteur. Ephyra reste un master complémentaire, sans attribution arbitraire à une arène précise. Une référence de projectile ne valide ni sa trajectoire, ni ses collisions, ni son effet à l’impact.

Les costumes hérités des fiches initiales restent sans attribution tant qu’un `costume_id` explicite n’est pas fourni. Cela signifie une liaison visuelle à vérifier, et non nécessairement une image à régénérer. Les mappings `data/costume_asset_links_v*.json` sont lus dans leur ordre numérique et conservent l’audit [V7](../../data/costume_asset_links_v7.json). Ils rattachent les images existantes à leur costume après vérification du personnage, de la provenance et de l’empreinte ; ils ne dupliquent aucun PNG et ne certifient aucune fidélité. Un master de décor ne vaut pas validation de ses calques de parallaxe séparés.

## Ce qui a été récupéré

- Le corpus initial : bible, prototype, données de conception, 16 personnages représentés et deux décors. Les fichiers copiés lors des deux premières passes sont identiques ; les doubles copies binaires n’augmentent pas les comptes.
- La passe v4 : neuf références de personnages et quatre boss. Kestrel était généré mais resté hors d’`assets` ; il est récupéré et contrôlé, avec [un constat distinct](../../data/generation_v4/recovery_kestrel_2026-11-20.json).
- Le lot de reprise : 14 références sélectionnées, ses sources, ses prompts et son rapport visuel. Clayton v02, Theron v02 et Ukkon v02 sont conservés ; leurs trois anciennes versions sont archivées dans `rejected_candidates/characters_20261119/`.
- Les six candidats v4 recouvrant des personnages du lot de reprise sont conservés et consultables comme alternatives. Ils ne sont pas six personnages supplémentaires.

## Nouvelles sorties présentes

| Sujet | Variante demandée | Fichier |
| --- | --- | --- |
| Matriarch | Gears 5 — modèle de campagne | [PNG](../../assets/bosses_v6/matriarch_gears5_fullbody.png) |
| Shibboleth seul — monture sans Karn | Gears of War: Judgment — monture seule ; Karn absent ; duo non complet | [PNG](../../assets/bosses_v7/shibboleth_judgment_mount_only_fullbody.png) |
| Berserker Lambent | Gears of War 3 — poitrine ouverte, pose de référence | [PNG](../../assets/bosses_v8/lambent_berserker_gow3_fullbody.png) |
| Tempest seul — monture sans Myrrah | Gears of War 3 — monture seule ; Myrrah absente ; duo non complet | [PNG](../../assets/bosses_v8/tempest_gow3_mount_only_fullbody.png) |
| Berserker | Gears of War (2006) — candidat guidé par promotion d'époque et artbook | [PNG](../../assets/bosses_v9/berserker_gears2006_fullbody.png) |
| DR-1 DeeBee | Gears of War 4 — DR-1 bleu avec Overkill | [PNG](../../assets/bosses_v9/dr1_gears4_fullbody.png) |
| Guardian DeeBee | Gears of War 4 — Guardian Tri-Shot, drone seul sans bouclier actif | [PNG](../../assets/bosses_v9/guardian_gears4_fullbody.png) |
| Pouncer | Gears of War 4 — Pouncer, pose fixe | [PNG](../../assets/bosses_v9/pouncer_gears4_fullbody.png) |
| Silverback | Gears of War 3 — exosquelette seul, sans pilote | [PNG](../../assets/bosses_v9/silverback_gears3_fullbody.png) |
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
| Mac — Mechanic Mac | Gears 5 — Mechanic Mac (skin Hivebusters) | [PNG](../../assets/costumes_v6/mac_mechanic_gears5_fullbody.png) |
| Augustus Cole — Thrashball Cole | Gears of War 3 — Thrashball Cole | [PNG](../../assets/costumes_v7/cole_thrashball_gow3_fullbody.png) |
| Marcus Fenix — campagne Gears of War 3 | Gears of War 3 — armure de campagne | [PNG](../../assets/costumes_v8/marcus_campaign_gow3_fullbody.png) |
| Buzzkill — lame circulaire | Gears of War 4 — projectile isolé, pose fixe | [PNG](../../assets/projectiles_v9/buzzkill_sawblade_gow4.png) |
| Dropshot — projectile foreuse | Gears of War 4 — projectile isolé, pose fixe | [PNG](../../assets/projectiles_v9/dropshot_drill_gow4.png) |
| Grenade Bolo / Frag | Gears of War 3 — projectile isolé, pose fixe | [PNG](../../assets/projectiles_v9/frag_grenade_gow3.png) |
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
python src/consolidate_inventory.py
```

Cette commande vérifie les fichiers, recalcule empreintes, dimensions, alpha et comptes, réconcilie les références du roster, puis reconstruit l’inventaire et la galerie autonome. Elle lit les résultats des passes v5 et suivantes sans les modifier. `src/build_asset_manifest.py` appelle également ce recalcul avant de renouveler la file de production. `src/finalize_generation_v2.py` reste un script historique de v2, pas la commande courante de consolidation.

Ce rapport décrit les fichiers préparés. Il ne constitue pas une preuve de publication GitHub, qui doit être vérifiée séparément.
