# Listing V13 — assets fixes et fidélité documentaire

**27 novembre 2026 · Darknigthmare · Gears of War Combats**

**6 nouveaux PNG actifs**, **2 nouveaux refus**, **1 refus historique retrouvé** et **17 recherches sans génération**, dans **26 journaux V13**. Les **15 autres refus antérieurs** restent conservés sans relance. Les 41 manquants de départ ont tous un état traçable.

Un sujet par PNG, dimensions et octets natifs. Les images visent la fidélité à l’édition documentée ; **aucune n’est certifiée 1:1**. Le moteur, les animations et les PDF/DOCX V1 ne sont pas modifiés par cette passe.

## Nouveaux candidats

| Sujet | Édition et portée | Fichier | Dimensions natives | Traçabilité |
| --- | --- | --- | --- | --- |
| Riftworm — extérieur Gears of War 2 | Riftworm Gears of War 2 — corps extérieur complet, vue latérale de modèle | [PNG](../../assets/bosses_v13/riftworm_g2_exterior.png) | 2172 × 724 · RGBA | [Sources, prompt et QA](../../data/generation_v13/boss_riftworm_g2_record.json) |
| Dizzy Wallin — standard Gears of War 3 | Dizzy standard Gears 3 — rendu Epic 2011, copie de diffusion | [PNG](../../assets/costumes_v13/dizzy_skin_02.png) | 1024 × 1536 · RGBA | [Sources, prompt et QA](../../data/generation_v13/dizzy_skin_02_record.json) |
| Victor Hoffman — campagne Gears of War 3 | Hoffman Gears 3 — modèle de production Epic | [PNG](../../assets/costumes_v13/hoffman_skin_02.png) | 1024 × 1536 · RGBA | [Sources, prompt et QA](../../data/generation_v13/hoffman_skin_02_record.json) |
| JD Fenix — CGU au début de Gears 5 | JD CGU non cicatrisé — début de campagne Gears 5 | [PNG](../../assets/costumes_v13/jd_skin_02.png) | 1024 × 1536 · RGBA | [Sources, prompt et QA](../../data/generation_v13/jd_skin_02_record.json) |
| Lahni — campagne Hivebusters / Brash Brigade | Brash Brigade Lahni — tenue en armure du début du DLC, modèle final | [PNG](../../assets/costumes_v13/lahni_skin_01.png) | 1024 × 1536 · RGBA | [Sources, prompt et QA](../../data/generation_v13/lahni_skin_01_record.json) |
| Locust Drone — modèle multijoueur Gears of War: E-Day | Modèle multijoueur visible dans la galerie officielle E-Day | [PNG](../../assets/costumes_v13/locust_drone_eday_multiplayer.png) | 1024 × 1536 · RGBA | [Sources, prompt et QA](../../data/generation_v13/locust_drone_skin_02_record.json) |

### Riftworm — extérieur Gears of War 2

`boss_riftworm_g2` · SHA-256 `7a56659e9ed8ef1bf9636c33a73ebcbf99e88c6cf5e5c3f265b4d8a05ce2cd2f`.

- Un seul ver entier de profil vers la droite ; tête et queue à l’intérieur du cadre, relief dorsal et ventre segmenté présents.
- Le rendu conserve la silhouette générale de l’aperçu, mais l’éclairage est plus clair ; la granularité du relief et l’arrangement exact des dents restent une reconstruction générative.
- Transparence native réelle ; 61,60 % de pixels alpha=0. Marges alpha≥128 de 33/151/31/172 px : côtés étroits, corps complet non recadré.
- Cette image documente uniquement l’extérieur. Elle ne représente pas le niveau Intestinal Fortitude, ses coupes, ses organes ou son échelle jouable.

Contrôles restants :

- Comparer nombre et position des dents, reliefs, creux et asymétries à un modèle final authentifié.
- Contrôler les franges de faible alpha et les marges latérales dans le pipeline ; aucune retouche ou mise à l’échelle appliquée.
- Documenter séparément l’intérieur et les éléments de rencontre environnementale sans prétendre qu’ils sont livrés.

### Dizzy Wallin — standard Gears of War 3

`dizzy_skin_02` · SHA-256 `8da3482a91492596108febeb80ef48de036a4aad2e8ff3aeeae6db11275558a9`.

- Un seul Dizzy entier, tourné vers la droite, chapeau de cowboy, barbe grisonnante, bras nus tatoués, armure gris-vert, cartouchière, ceinture à boucle ronde, poche de cuisse, genouillères et bottes visibles.
- Les grandes formes du costume suivent le rendu Gears 3. Les motifs exacts des tatouages, le visage, les attaches et les reliefs restent interprétés ; la petite référence et son filigrane limitent leur vérification.
- La sortie reste en trois-quarts frontal, mains basses ; la garde latérale de jeu stricte n'est pas obtenue.
- PNG RGBA natif, 63,02 % alpha=0, alpha maximal 254 ; quelques pixels alpha=1 atteignent la bande de 8 px. Les marges haut/bas 47/29 px n'atteignent pas la cible de 10 %.

Contrôles restants :

- Comparer précisément visage, tatouages, plaques, poches et attaches à un original Gears 3 de meilleure résolution.
- Contrôler les couleurs et les contours par composition dans le moteur, dont les pixels alpha très faible.
- Valider la pose latérale et les marges du sprite avant utilisation en jeu.

### Victor Hoffman — campagne Gears of War 3

`hoffman_skin_02` · SHA-256 `10329a5b417ce923a2eef32458c784062243a0d4dd01fe5df780358bc90554cd`.

- Un seul Hoffman entier vers la droite, visage âgé glabre, casquette à courte visière, bras nus, médaillons d'armure et équipement Gears 3 reconnaissables.
- L'armure sombre, les lumières bleu-blanc, les bottes et le système de ceinture suivent le modèle fourni ; les petits reliefs et proportions ne sont pas certifiés exacts.
- Le corps reste principalement en trois-quarts frontal, mains basses ; la garde de combat latérale stricte reste à valider.
- RGBA natif, 69,73 % alpha=0 et bordure 8 px entièrement transparente. Silhouette complète ; marges haut/bas 69/85 px, inférieures à la cible de 10 %.

Contrôles restants :

- Comparer le profil du visage, le volume des bras et les asymétries des poches au modèle low-poly final.
- Vérifier les reliefs des deux médaillons, les insignes, les coutures et toutes les pièces de jambière.
- Valider la pose latérale, les marges et les contours dans le moteur.

### JD Fenix — CGU au début de Gears 5

`jd_skin_02` · SHA-256 `bbee0761a88c20e2aac82ee921a65cf4351bb2da601c73235d0ba6a3d1d5b339`.

- Un seul JD entier, cheveux courts, sans barbe épaisse ni manchon médical, correspondant à la phase initiale Gears 5.
- Armure CGU à disques circulaires, éclairages bleus aux épaules, manches longues beige-gris, holster de cuisse droite, genouillères et bottes cohérents avec la référence officielle.
- La ressemblance faciale, la coiffure et certains petits détails du métal restent interprétés. Pose de trois-quarts, plus frontale que la vue latérale demandée, mains abaissées.
- RGBA natif, 62,44 % alpha=0 ; bordure 8 px alpha maximum 1. Personnage complet, mais marges haut/bas 45/30 px : cible de 10 % non atteinte.

Contrôles restants :

- Comparer précisément visage, coiffure, insigne de poitrine, chevrons et architecture des attaches au modèle officiel.
- Contrôler emplacement et dimensions des canisters, pouches et pièces de jambières.
- Valider pose latérale de combat, marges verticales et franges alpha dans le moteur.

### Lahni — campagne Hivebusters / Brash Brigade

`lahni_skin_01` · SHA-256 `1e9359c427ca81256b92aa011e6b838b7e44889ae55309ec38c0ac48527e11f4`.

- Une Lahni entière en armure DLC, bandeau olive, dreadlocks, deux disques thoraciques, marquages jaunes, manchettes asymétriques, poche de cuir et deux canisters ; tenue distincte du PNG Escape existant.
- Copie native exacte du PNG encodé dans la data URL retournée ; aucun recadrage, agrandissement, peinture, effacement ou correction alpha.
- RGBA 1024 × 1536 ; 69,57 % de pixels alpha=0 ; alpha maximal natif 254 ; contour alpha>=128 [246,19,790,1504].
- Marges au seuil alpha>=128 : gauche 246, haut 19, droite 234, bas 32 px. La silhouette est entière, mais les 10 % de marge demandés ne sont pas respectés verticalement.
- Halo diffus à faible alpha autour de la silhouette : contour alpha>0 [65,15,984,1507] plus large que le contour principal ; les huit pixels périphériques sont toutefois transparents.
- Les motifs des tatouages, les glyphes du plastron, le visage, les attaches et détails de cuir demeurent une interprétation générative. Orientation principalement trois-quarts frontal, pas profil de combat validé.

Contrôles restants :

- Comparer précisément visage, tatouages, glyphes et attaches au modèle final du DLC.
- Valider un détourage sans halo et une marge de production suffisante lors d’une future passe expressément dédiée.
- Vérifier lisibilité de la pose et import alpha dans le moteur ; aucune animation ni certification 1:1.

### Locust Drone — modèle multijoueur Gears of War: E-Day

`locust_drone_skin_02` · SHA-256 `b4dab7cad506e2b989a2758c2fbfbcd3f67bb4a226a0ee290f862ab439dcf015`.

- Tête, deux mains et deux bottes visibles ; un seul Drone statique, sans arme ni autres personnages.
- Pose recomposée ; face plus fermée et dentition réinterprétée par rapport au portrait Hanbeck.
- Poitrine, sangles, segmentations et petits motifs d’armure réinterprétés ; l’occlusion dans la source empêche d’établir certains détails.
- Marge alpha ≥128 mesurée gauche/haut/droite/bas : 137/58/149/38 px. Haut 3,78 % et bas 2,47 % de la hauteur : consigne 14 % non atteinte ; toute la silhouette principale reste cadrée. Quelques pixels alpha 1 touchent les bords bas/gauche. Aucune retouche ni deuxième tentative.
- PNG RGBA natif : alpha 0–254, 59,53 % de pixels totalement transparents ; aucun pixel alpha 255. Le fond sombre visible dans certains lecteurs correspond au RGB natif sous transparence, à contrôler en composition.

Contrôles restants :

- Comparer armure de poitrine, dispositifs lumineux, attaches et bottes à des vues complémentaires du modèle multijoueur E-Day.
- Vérifier en compositing les bords et réserver de nouvelles marges lors d’une future préparation atlas autorisée.
- Aucune certification 1:1, canon ou état prêt production.

## Refus de cette passe et refus retrouvé

| Cible | État | Journal |
| --- | --- | --- |
| Keegan — Onyx Guard Gears 5 Hivebusters | Nouveau refus ; aucune relance | [keegan_skin_02_record.json](../../data/generation_v13/keegan_skin_02_record.json) |
| Skorge — modèle multijoueur Gears 5 Opération 5 | Nouveau refus ; aucune relance | [skorge_skin_02_record.json](../../data/generation_v13/skorge_skin_02_record.json) |
| Garde Theron — original 2006 | Refus historique, aucune relance | [theron_skin_01_record.json](../../data/generation_v13/theron_skin_01_record.json) |

## Recherches sans image

| Cible | Point à résoudre | Journal |
| --- | --- | --- |
| Anthony Carmine Black Steel — Gears 5 | L'existence exacte de Black Steel Anthony Carmine dans Gears 5 est confirmée par la fiche Xbox (Works with Gears 5, sortie 1 juin 2021) et le rigueur crédité chez The Coalition. Cependant les deux rendus officiels de l'artiste et l'image Xbox inspectés sont coupés à la taille ou aux cuisses. Les genoux, les bottes et les matériaux du bas de ce skin Gears 5 restent non documentés par une vue complète. Aucun modèle Gears 4 n'est substitué. | [anthony_black_steel_g5_record.json](../../data/generation_v13/anthony_black_steel_g5_record.json) |
| Anya Stroud — Contrôle Gears of War 2 | La version Contrôle de Gears of War 2 est retenue explicitement. La capture de campagne retrouvée documente le visage, la coiffure et le haut de l'uniforme, mais s'arrête à la taille. Aucune vue finale complète de cette édition n'a été établie pour les jambes, les chaussures et les proportions du corps. Une tenue Gears 1, un concept ancien ou Civilian Anya de Gears 3 ne permet pas de compléter fidèlement le modèle Gears 2. | [anya_skin_01_record.json](../../data/generation_v13/anya_skin_01_record.json) |
| Hydra de Skorge | Vue finale G2 complète avec tous les appendices, tourelle, attaches et emplacement du cavalier ; angles complémentaires vérifiables. | [boss_hydra_skorge_record.json](../../data/generation_v13/boss_hydra_skorge_record.json) |
| Sire — épreuve de capture | Obtenir une vue finale G5 complète sans personnage superposé, avec pieds, mains, visage et toutes les contentions visibles ; vérifier le dos séparément. | [boss_sire_g5_record.json](../../data/generation_v13/boss_sire_g5_record.json) |
| Wakaatu | Modèle final de Wakaatu en couleurs ou vues de jeu montrant ensemble ailes, abdomen, queue, pattes et dos ; correspondance avec le concept à contrôler. | [boss_wakaatu_record.json](../../data/generation_v13/boss_wakaatu_record.json) |
| DeeBee — multijoueur Gears 5 | Obtenir une capture de personnalisation ou un rendu officiel complet du skin Shepherd DeeBee standard dans Gears 5. / Vérifier la répartition des plaques, les capteurs et les marquages ainsi que les pieds avant toute génération. | [deebee_skin_02_record.json](../../data/generation_v13/deebee_skin_02_record.json) |
| Gabe — Armored Gabe Gears 5 | Obtenir une capture ou un rendu final complet Armored Gabe Gears 5, idéalement face/profil/dos. / Contrôler la révision du visage avant d’employer les images de lancement de novembre 2020. / Comparer au costume Gears Tactics existant sans supposer que le modèle est identique. | [gabe_skin_02_record.json](../../data/generation_v13/gabe_skin_02_record.json) |
| Grenadier Locuste — original 2006 | Aucune vue complète et attribuée de façon suffisamment sûre au modèle final standard de 2006 n’a été établie. Les pistes complètes renvoient à Gears 3, Tactics, Ultimate Edition, à une figurine ou à une illustration non datée ; les crédits d’artiste seuls n’établissent pas la variante visible. Pas de génération à partir du nom ni de substitution d’édition. | [grenadier_skin_02_record.json](../../data/generation_v13/grenadier_skin_02_record.json) |
| Keegan — tenue intro Hivebusters | Valider la relation d’alias et la portée exacte de l’ID avant toute attribution de PNG au catalogue. | [keegan_hivebusters_intro_record.json](../../data/generation_v13/keegan_hivebusters_intro_record.json) |
| Lahni — tenue intro Hivebusters | Valider la relation d’alias et la portée exacte de l’ID avant toute attribution de PNG au catalogue. | [lahni_hivebusters_intro_record.json](../../data/generation_v13/lahni_hivebusters_intro_record.json) |
| Queen Myrrah — Gears 5 Opération 3 | L’annonce officielle Gears 5 confirme la cible et montre le casque, le visage et le haut du costume. La capture s’arrête sous la taille ; jambes, bottes et tenue basse complète non documentées. Aucun corps complet de la variante standard Gears 5 n’a été établi ; les modèles Gears 3, Ultimate Edition et Black Steel ne sont pas substitués. | [myrrah_skin_02_record.json](../../data/generation_v13/myrrah_skin_02_record.json) |
| Obus de Boomshot — Gears of War 4 | Gros plan ou extraction visuelle documentée du projectile final G4 : corps, culot et tête visibles ; distinguer obus chargé, projectile en vol et effet d’impact. | [projectile_boomshot_shell_g4_record.json](../../data/generation_v13/projectile_boomshot_shell_g4_record.json) |
| RAAM — RAAM’s Shadow | Les captures spécifiques au DLC consultées montrent le haut du corps et les cuisses/genoux, sans vue exploitable des jambes basses et des pieds. Aucune référence complète de cette édition n’a été établie ; pas de génération à partir du nom ni de substitution par RAAM 2006, Ultimate Edition, Gears 5 ou Killer Instinct. | [raam_skin_02_record.json](../../data/generation_v13/raam_skin_02_record.json) |
| Reyna — version humaine future à définir | Définir explicitement quelle Reyna humaine canonique, de quel jeu et de quelle tenue, cet ID doit représenter. / Réunir ensuite des vues complètes du modèle final exact et clarifier le kit de gameplay distinct déjà mentionné par le catalogue. | [reyna_skin_02_record.json](../../data/generation_v13/reyna_skin_02_record.json) |
| Samantha Byrne — vétérane Gears of War 4 | Le costume demandé est Sam vétérane/pilote dans la campagne Gears of War 4. La source Gears 3 du catalogue, les modèles de Sam Gears 3 et les skins Gears 5 ne documentent pas cette tenue exacte. La recherche n'a pas établi de modèle final Gears 4 en pied ; visage âgé, tenue de pilote, bas du corps et bottes restent insuffisamment documentés. Aucune génération ne remplace cette cible par une autre édition. | [sam_skin_02_record.json](../../data/generation_v13/sam_skin_02_record.json) |
| Tai Kaliso — campagne E-Day | La présence de Tai dans Gears of War: E-Day est confirmée par Xbox. Un concept officiel complet avant/arrière est accessible, mais sa publication précise qu'il s'agit d'un travail de concept. Aucun modèle final de campagne en pied permettant de vérifier les changements entre concept et jeu n'a été établi. Ce concept n'est donc pas utilisé comme modèle final ; la variante promotionnelle Bloodied Hunter n'est pas substituée au costume de campagne. | [tai_skin_02_record.json](../../data/generation_v13/tai_skin_02_record.json) |
| Garde Theron — Gears Tactics | La référence officielle Tactics est cadrée de la tête aux genoux ; pieds et bas des jambes restent hors champ. La reprise officielle Steam pointe sur le même visuel c2fcd853880fcada1996def87bfd8bea45d0ee83.png. Les autres captures identifiées ne complètent pas la vue exploitable des pieds. Aucun PNG ni tentative V13. | [theron_skin_02_record.json](../../data/generation_v13/theron_skin_02_record.json) |

## Couverture courante

| Catégorie | Avec référence | Catalogue | Sans référence |
| --- | --- | --- | --- |
| Personnages | 51 | 56 | 5 |
| Costumes | 63 | 85 | 22 |
| Boss, créatures et machines | 27 | 31 | 4 |
| Stages | 34 | 34 | 0 |
| Projectiles | 4 | 8 | 4 |

**154 PNG actifs uniques + 15 archives**, sans doublage par les rattachements. 0 certification 1:1, 0 ensemble d’animations complet. Le Riftworm, lorsqu’illustré, ne couvre que son extérieur ; les rencontres environnementales et corps partiels restent explicitement limités.

Les deux IDs « intro Hivebusters » sont conservés en attente de revue d’alias : aucun second PNG, aucun partage implicite de couverture, aucune relance de Keegan sous un autre intitulé.

La bible V13 reprend les trois guides et l’adaptation V12 sans changer leurs originaux : 68 rubriques et 40 cas d’acceptation conservés, ces derniers toujours non exécutés.

Voir la [reprise V13](REPRISE_V13.md), les [sources](../references/production-v13-research.md), les [revues croisées](REVIEW_V13.md), la [validation](VALIDATION_V13.json) et la [bible V13](../../livrables/Gears_of_War_Combats_Bible_v13.md).
