# Listing V7 — identités, costumes et nouveaux assets

Passe clôturée le **20 novembre 2026**. Ce listing distingue les ajouts de fiches, les nouvelles images et les liens ajoutés à des images déjà présentes. Les comptes proviennent de la [couverture finale](../../production/coverage.json) ; les preuves de version figurent dans les journaux et dans l’[audit des costumes](AUDIT_COSTUMES_V7.md).

## Delta de catalogue

| Catégorie | Total après V6 | Ajouts nets V7 | Total après V7 |
| --- | ---: | ---: | ---: |
| Personnages | 53 | 3 | 56 |
| Costumes | 85 | 0 | 85 |
| Boss / rencontres | 31 | 0 | 31 |
| Stages | 34 | 0 | 34 |

Le fichier [production_catalog_v7.json](../../data/production_catalog_v7.json) conserve les quatre tableaux attendus. Seul `characters` contient trois ajouts. Les six nouvelles images concernent des fiches déjà présentes ; elles ne créent aucun personnage ou costume en double.

### Trois nouvelles identités

| Identifiant | Personnage | Édition / cible | Preuve primaire |
| --- | --- | --- | --- |
| `adam_fenix` | Adam Fenix | Gears of War 3 — apparence du personnage multijoueur Adam Fenix | [Source](https://www.xbox.com/en-us/games/store/adam-fenix-multiplayer-character/btt6glfffmlv) |
| `alex_brand` | Alex Brand | Gears of War: Judgment — apparence multijoueur Alex Brand | [Source](https://news.xbox.com/en-us/2012/11/07/gears-of-war-judgment-pre-orders-kickoff-today/) |
| `karn` | Karn | Gears of War: Judgment — modèle de Karn, personnage distinct de sa monture Shibboleth | [Source](https://pseudopod.artstation.com/projects/gVB5E) |

Ces trois fiches restent sans image. Les [sources et réserves détaillées](../references/production-v7-catalog.md) comprennent la fiche Xbox d’Adam Fenix, l’annonce Xbox et le portfolio Mike Kime pour Alex Brand, ainsi que les crédits Kime / Morgan et l’entretien Epic / PCF pour Karn. Le personnage `karn` est distinct de la rencontre existante `boss_shibboleth` ; aucun deuxième boss n’est ajouté. Toutes les fiches gardent `canonical_fidelity_validated: false`.

## Six PNG supplémentaires

| Sujet | Édition | Fichier et preuve | Portée |
| --- | --- | --- | --- |
| Michael Barrick | Gears of War 3 — RAAM’s Shadow | [PNG](../../assets/characters_v7/michael_barrick_gow3_raams_shadow_fullbody.png) · [journal](../../data/generation_v7/michael_barrick_record.json) | `alternate_version` ; cible Gears 5 à produire |
| Ezra Loomis | Gears of War: Judgment | [PNG](../../assets/characters_v7/ezra_loomis_judgment_fullbody.png) · [journal](../../data/generation_v7/ezra_loomis_record.json) | Candidat de l’édition cible ; pose bras croisés |
| Thrashball Cole | Gears of War 3 | [PNG](../../assets/costumes_v7/cole_thrashball_gow3_fullbody.png) · [journal](../../data/generation_v7/cole_thrashball_record.json) | Costume `cole_skin_03` ; orientation et détails à contrôler |
| Shibboleth | Gears of War: Judgment | [PNG](../../assets/bosses_v7/shibboleth_judgment_mount_only_fullbody.png) · [journal](../../data/generation_v7/shibboleth_record.json) | Monture seule ; Karn absent, rencontre incomplète |
| Village | Gears 5 — Operation 8 | [PNG](../../assets/stages_v7/village_gears5_master.png) · [journal](../../data/generation_v7/village_record.json) | Master aplati ; cadrage de combat 2D adapté |
| Dawn | Gears 5 — Operation 8 Drop 2 | [PNG](../../assets/stages_v7/dawn_gears5_master.png) · [journal](../../data/generation_v7/dawn_record.json) | Master aplati ; cadrage de combat 2D adapté |

Alicia Valera V6 et Michael Barrick V7 restent ciblés en version Gears 5 dans le catalogue. Leurs PNG Gears 3 constituent des références historiques `alternate_version`. Shibboleth est une monture seule : Karn demeure absent du duo. La présence d’un candidat de la bonne édition pour Loomis ou Cole ne vaut pas certification visuelle.

## 34 liens audités vers des PNG existants

Le [mapping V7](../../data/costume_asset_links_v7.json) ajoute un `costume_id` documenté à chacune des 34 images suivantes. Il conserve leur catégorie de personnage, leur identité de base, leur statut et leur fichier. L’empreinte SHA-256, le parent et la provenance doivent correspondre lors de chaque consolidation. Les motivations, sources, journaux et réserves complètes restent dans le mapping et son [audit](AUDIT_COSTUMES_V7.md).

| Costume | Intitulé | Référence existante | Statut artistique conservé |
| --- | --- | --- | --- |
| `dom_skin_02` | Dominic Santiago — Campagne Gears of War 2006 | [PNG](../../assets/characters_v5/dom_gow1_fullbody.png) | `candidate` |
| `baird_skin_03` | Damon Baird — Campagne Gears of War 3 | [PNG](../../assets/characters_v2/baird_reference_v3.png) | `candidate` |
| `cole_skin_02` | Augustus Cole — Campagne Gears of War 3 | [PNG](../../assets/characters_v4/cole_reference_v4.png) | `candidate` |
| `anya_skin_02` | Anya Stroud — Combat de campagne Gears of War 3 | [PNG](../../assets/characters/anya_stroud/gears3/reference_fullbody_v01.png) | `candidate` |
| `kait_skin_02` | Kait Diaz — Hiver Gears 5 | [PNG](../../assets/kait_neutral_cutout.png) | `candidate` |
| `raam_skin_01` | Général RAAM — Combat final Gears of War 2006 | [PNG](../../assets/characters_v5/raam_gow1_fullbody.png) | `candidate` |
| `skorge_skin_01` | Skorge — Palais Gears of War 2 | [PNG](../../assets/characters_v2/skorge_reference_v3.png) | `correction_required` |
| `myrrah_skin_01` | Reine Myrrah — Armure royale Gears of War 3 | [PNG](../../assets/characters/myrrah/gears3/reference_fullbody_v01.png) | `candidate` |
| `locust_drone_skin_01` | Drone locuste — Drone Gears of War 2006 | [PNG](../../assets/characters_v2/locust_drone_reference_v2.png) | `candidate` |
| `kantus_skin_01` | Kantus — Kantus Gears of War 2 | [PNG](../../assets/characters_v2/kantus_reference_v3.png) | `candidate` |
| `jd_skin_03` | JD Fenix — CGU Gears 5 après ellipse | [PNG](../../assets/characters_v2/jd_reference_v2.png) | `candidate` |
| `del_skin_02` | Del Walker — Campagne Gears 5 | [PNG](../../assets/characters_v2/del_reference_v3.png) | `correction_required` |
| `fahz_skin_01` | Fahz Chutani — Campagne Gears 5 | [PNG](../../assets/characters/fahz_chutani/gears5/reference_fullbody_v01.png) | `candidate` |
| `clayton_skin_01` | Clayton Carmine — Campagne Gears of War 3 | [PNG](../../assets/characters/clayton_carmine/gears3/reference_fullbody_v02.png) | `candidate` |
| `lizzie_skin_01` | Lizzie Carmine — Campagne Gears 5 | [PNG](../../assets/characters_v2/lizzie_reference_v2.png) | `correction_required` |
| `hoffman_skin_01` | Victor Hoffman — Hoffman en armure Gears 5 | [PNG](../../assets/characters_v4/hoffman_reference_v4.png) | `candidate` |
| `tai_skin_01` | Tai Kaliso — Campagne Gears of War 2 | [PNG](../../assets/characters/tai_kaliso/gears2/reference_fullbody_v01.png) | `candidate` |
| `dizzy_skin_01` | Dizzy Wallin — Pilote Gears of War 2 | [PNG](../../assets/characters_v6/dizzy_gow2_fullbody.png) | `candidate` |
| `sam_skin_01` | Samantha Byrne — Campagne Gears of War 3 | [PNG](../../assets/characters/samantha_byrne/gears3/reference_fullbody_v01.png) | `candidate` |
| `paduk_skin_01` | Garron Paduk — Kilo Squad Judgment | [PNG](../../assets/characters_v2/paduk_reference_v3.png) | `candidate` |
| `sofia_skin_01` | Sofia Hendrik — Kilo Squad Judgment | [PNG](../../assets/characters_v2/sofia_reference_v3.png) | `candidate` |
| `gabe_skin_01` | Gabe Diaz — Tenue de base Gears Tactics | [PNG](../../assets/characters/gabriel_diaz/tactics/reference_fullbody_v01.png) | `candidate` |
| `sid_skin_01` | Sid Redburn — Tenue de base Gears Tactics | [PNG](../../assets/characters_v2/sid_reference_v3.png) | `candidate` |
| `mikayla_skin_01` | Mikayla Dorn — Tenue de base Gears Tactics | [PNG](../../assets/characters/mikayla_dorn/tactics/reference_fullbody_v01.png) | `candidate` |
| `reyna_skin_01` | Reine Reyna — Reine Reyna Gears 5 | [PNG](../../assets/characters_v2/reyna_reference_v3.png) | `correction_required` |
| `lahni_skin_02` | Lahni Kaliso — Tenue Escape Gears 5 | [PNG](../../assets/characters/lahni_kaliso/gears5_hivebuster/reference_fullbody_v01.png) | `candidate` |
| `keegan_skin_01` | Keegan — Campagne Hivebusters | [PNG](../../assets/characters_v4/keegan_reference_v4.png) | `candidate` |
| `mac_skin_01` | Mac — Campagne Hivebusters | [PNG](../../assets/characters_v4/mac_reference_v4.png) | `candidate` |
| `jack_skin_01` | JACK — JACK Gears 5 | [PNG](../../assets/characters_v2/jack_reference_v3.png) | `candidate` |
| `deebee_skin_01` | DeeBee — Shepherd Gears of War 4 | [PNG](../../assets/characters_v4/deebee_reference_v4.png) | `candidate` |
| `warden_skin_01` | Warden — Warden Gears 5 | [PNG](../../assets/characters/warden/gears5/reference_fullbody_v01.png) | `candidate` |
| `swarm_drone_skin_01` | Drone de l’Essaim — Drone Gears of War 4 | [PNG](../../assets/characters_v2/swarm_drone_reference_v2.png) | `candidate` |
| `ukkon_skin_01` | Ukkon — Campagne Gears Tactics | [PNG](../../assets/characters/ukkon/tactics/reference_fullbody_v02.png) | `candidate` |
| `grenadier_skin_01` | Grenadier locuste — Grenadier Gears Tactics | [PNG](../../assets/characters_v2/grenadier_reference_v2.png) | `candidate` |

Ces liens n’ajoutent aucune image. Avec Mechanic Mac (`mac_skin_02`, V6) et Thrashball Cole (`cole_skin_03`, V7), **36 costumes sur 85** disposent désormais d’une référence explicite. Les 49 autres sont listés sans omission dans la [reprise V7](REPRISE_V7.md).

### Correspondances non retenues

Marcus Ultimate Edition n’a pas été attribué au costume du jeu 2006. Le Theron historique garde une édition à préciser et ne remplit ni le slot 2006 ni Tactics par simple ressemblance. Les variantes de campagne, d’introduction, Black Steel, V-Day, Hivebuster et Blood Red ne sont pas déduites d’un modèle standard. Les images de présentation ne sont pas utilisées pour compléter un costume.

## Couverture finale et limites

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

Les listes exactes des **16 identités sans image, 49 costumes sans lien, 25 boss sans référence et 30 stages sans master** figurent dans la [reprise V7](REPRISE_V7.md). Ce sont des manques du catalogue du projet ; le listing ne revendique pas l’exhaustivité de tous les jeux, romans, comics et contenus cosmétiques de la franchise.

La consolidation ne signale aucune alerte et les **8 tests d’inventaire ont réussi**. Les références statiques, les états `correction_required`, les éditions alternatives et les sources partielles restent identifiés. La validation artistique 1:1, les animations et les calques de parallaxe demeurent ouverts.

Le [rapport de validation V7](VALIDATION_V7.json) conserve les preuves des contrôles sur les 74 PNG, les journaux et les rattachements de costumes.

La passe poursuit la [PR #1](https://github.com/darknigthmare/gear-of-wars-combats/pull/1) sur la même branche. Les [rapports V6](REPRISE_V6.md) restent conservés comme état historique.
