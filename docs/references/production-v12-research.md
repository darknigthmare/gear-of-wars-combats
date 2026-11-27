# Références visuelles et décisions de production — V12

Date : **27 novembre 2026**. Cette passe reprend les assets fixes manquants et intègre séparément les trois documents du guide de combat. Les fichiers tiers téléchargés pour comparaison restent hors du dépôt ; les URL, la portée constatée et les empreintes des références utilisées sont consignées dans les journaux.

## Règle de lecture

Chaque PNG actif est une copie de sortie native du générateur, sans retouche raster externe, agrandissement ni animation. La présence d’une référence ne certifie pas une fidélité 1:1, une édition finale, un corps complet ou une aptitude à la production. Les refus du générateur ne sont pas relancés ; une recherche sans référence suffisante ne devient pas une tentative de génération.

Les candidats de cadrage ou de correction écartés sont archivés sous `rejected_candidates/` et exclus de la couverture active. Les limites des passes précédentes restent valides.

## Guide et extensions

Les trois originaux et leur provenance sont dans le [dossier des guides](../guides/combat/README.md). Le [chapitre d’adaptation](../combat_extensions.md) et l’[audit de 68 rubriques et 40 cas d’acceptation](../production/GUIDE_INTEGRATION_V12.md) portent l’intégration documentaire. Les sources de lore citées dans ce chapitre ne servent pas automatiquement de preuves visuelles aux PNG ci-dessous.

## Journaux de la passe

**21 sujets suivis : 12 PNG actifs nouveaux, 4 refus du générateur et 5 recherches sans génération.** Les 3 révisions archivées restent hors couverture active.

### Damon Baird — campagne Gears of War 2006 — `baird_skin_02`

- Journal : [baird_skin_02_record.json](../../data/generation_v12/baird_skin_02_record.json).
- État : `blocked_generator_refusal` ; génération tentée : non.
- Aucun PNG ajouté pour cette cible.
- [first_party_developer_interview_promotional_capture_rehosted_by_press](https://www.xboxgazette.com/interview_gears_of_war_cliffyb_en.php) — Entretien de Cliff Bleszinski du 16 juin 2006, images créditées Epic/Microsoft. La légende identifie de gauche à droite Baird, Cole, Marcus et Dom. Baird est visible en pied à gauche ; capture prépublication 1024 × 576, détails sombres et bras partiellement masqué. Il ne s'agit pas d'Ultimate Edition.
- [secondary_development_comparison_excluded](https://www.levelup.com/noticias/the-coalition-muestra-arte-conceptual-de-gears-of-war-4/) — Rendu complet de développement lié à Ultimate Edition, examiné puis exclu. Ne confirme pas le corps exact du modèle de campagne 2006 et n'a pas été transmis au générateur.

**Constats et limites**

- Référence promotionnelle authentique de la période originale 2006 retrouvée en pied ; elle permet de distinguer le costume d'Ultimate Edition, mais ne certifie pas chaque détail du modèle final.
- Les images de comparaison Ultimate Edition ont été inspectées puis exclues afin d'éviter le mélange d'éditions.
- Une seule tentative avec la capture de 2006 : refus au stade sortie, aucun PNG reçu et aucun réessai.

### Flock — `boss_flock`

- Journal : [boss_flock_record.json](../../data/generation_v12/boss_flock_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [flock_gears5_swarm.png](../../assets/bosses_v12/flock_gears5_swarm.png).
- Portée : `reference_collective_swarm` ; relation d’édition : `target_version_candidate`.
- [secondary_publisher_in_game_screenshot](https://www.gamepressure.com/gears-5/act-2-chapter-4-the-source-of-it-all-walkthrough/z2c8fa) — Capture Gears 5 dans les ruines enneigées montrant deux Flocks. Utilisée pour la densité, la silhouette et la couleur de l'essaim ; une seule formation générée. La capture ne fixe pas un nombre canonique de Leeches.
- [production_artist_final_model](https://www.artstation.com/artwork/2xzmJB) — Bruno Melo : highpoly du Leech ; gamemesh et textures crédités à Can Etiskol. Vues du modèle de production. Preuve anatomique de l'organisme individuel, pas d'une formation déterminée.
- [production_artist_final_model](https://www.artstation.com/artwork/2xzmJB) — Deux vues du Leech en posture de déplacement ; manteau aplati, gueule en entonnoir, épines et appendices effilés.

**Constats et limites**

- Un seul Flock : plusieurs Leeches forment une entité collective, conformément à la nature du sujet ; il ne s'agit pas d'une planche de personnages.
- La révision a réduit la taille relative des organismes et diversifié leurs directions. La densité et le mouvement collectif restent une recomposition, pas la copie d'une frame de jeu.
- Le jeu montre des détails plus petits et moins séparables : disposition, nombre, proportions exactes, rigidité des manteaux et intensité des lumières internes restent à comparer.
- Marge minimale de 125 pixels à alpha >=128. Toutes les extrémités principales restent dans le cadre ; cible de 12 % non atteinte verticalement.
- Aucun effet de fumée, fond, interface ou géant central ajouté. Les Leeches ne sont pas des assets séparés livrés par ce PNG.

### Hydra de Skorge — `boss_hydra_skorge`

- Journal : [boss_hydra_skorge_record.json](../../data/generation_v12/boss_hydra_skorge_record.json).
- État : `reference_research_pending` ; génération tentée : non.
- Aucun PNG ajouté pour cette cible.
- [production_artist_concept](https://hawkprey.artstation.com/projects/Zex3m) — Concept GOW Uber Reaver par James Hawkins. Une origine de design, sans preuve suffisante des détails finaux de la monture Gears 2.
- [first_party_technical_presentation](https://de45xmedrsdbp.cloudfront.net/Resources/files/GDC09_Smedberg_RenderingTechniques-1415210295.pdf) — Rendering Techniques in Gears of War 2, Niklas Smedberg et Daniel Wright, Epic Games, GDC 2009, page 12 (index 11). Planche de modèle éclaté endommagé Uber Reaver. Crédit modèle Kevin Lanning ; texture Chris Perna et Mike Buck. Pas de vue intacte complète ni cavalier Skorge.

**Constats et limites**

- La présentation Epic relie un modèle réel à Gears 2 ; la planche montre principalement des états endommagés et morceaux séparés.
- Le concept du premier Gears et le modèle éclaté de Gears 2 ne sont pas fusionnés en un faux modèle final intégral. Aucun PNG de l’Hydra ni du duo avec Skorge produit.

### Kraken — `boss_kraken`

- Journal : [boss_kraken_record.json](../../data/generation_v12/boss_kraken_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [kraken_gears5_head_mantle.png](../../assets/bosses_v12/kraken_gears5_head_mantle.png).
- Portée : `reference_partial` ; relation d’édition : `target_version_candidate`.
- [production_artist_final_model](https://toninio.artstation.com/projects/3on4GY) — Antoine Di Lorenzo, auteur du modèle, textures et intégration du corps et des tendrils du Kraken. Rendu frontal de l'ensemble tête/manteau. Les longues extensions et le corps complet ne sont pas documentés par ce seul cadrage.
- [production_artist_final_model](https://toninio.artstation.com/projects/3on4GY) — Même modèle sous un autre angle ; volumes, bouche, crête et texture du manteau.

**Constats et limites**

- Référence partielle du Kraken : tête, manteau et bases des appendices seulement ; aucun corps complet revendiqué.
- Bouche verticale, crête centrale, carapace irrégulière et lumières internes orange reprises des rendus du créateur.
- Marge minimale finale mesurée de 117 pixels ; supérieur au seuil 10 % sur chaque bord mais consigne de 15 % non atteinte en bas.
- Réorientation légère et recadrage ont recomposé certains détails de dentition, crêtes et peau ; conformité 1:1 à contrôler.

### Riftworm — rencontre environnementale — `boss_riftworm_g2`

- Journal : [boss_riftworm_g2_record.json](../../data/generation_v12/boss_riftworm_g2_record.json).
- État : `reference_research_pending` ; génération tentée : non.
- Aucun PNG ajouté pour cette cible.
- [production_artist_concept](https://hawkprey.artstation.com/projects/LexBR) — GOW2 Riftworm par James Hawkins : tête et partie émergée dans un concept. Ni turnaround du corps entier ni preuve exhaustive du modèle final.
- [first_party_technical_presentation](https://de45xmedrsdbp.cloudfront.net/Resources/files/GDC09_Smedberg_RenderingTechniques-1415210295.pdf) — Présentation Epic sur les techniques de rendu Gears 2, sections intérieures du Riftworm et chambres cardiaques ; contexte de rencontre environnementale, pas silhouette extérieure complète.

**Constats et limites**

- La silhouette émergée de concept est documentée, mais produire un ver entier imposerait de reconstruire une anatomie non montrée.
- La fiche reste une rencontre environnementale. Un corps miniature ou une arène réinventée ne remplace pas les coupes, hazards et espaces réellement à produire.

### Wakaatu — `boss_wakaatu`

- Journal : [boss_wakaatu_record.json](../../data/generation_v12/boss_wakaatu_record.json).
- État : `reference_research_pending` ; génération tentée : non.
- Aucun PNG ajouté pour cette cible.
- [production_artist_concept](https://tylerthebradley.artstation.com/projects/Krb5LB) — Concept gris multi-angle de Tyler Bradley. Géométrie de concept visible, pas un modèle final complet en couleurs.
- [secondary_publisher_in_game_screenshot](https://www.noobfeed.com/articles/gears-5-hivebusters-how-to-defeat-wakaatu-insane) — Capture de tête au sol : plumage sombre et œil jaune visibles ; corps absent, flou de mouvement et interface. Ne résout pas la palette du corps entier.
- [official_game_announcement](https://www.gearsofwar.com/en-us/news/hivebusters/) — Atteste le contexte Hivebusters et Galangi ; ne donne pas un turnaround de modèle.

**Constats et limites**

- La recherche V12 retrouve un concept primaire et une capture finale de tête. Ces références ne suffisent pas à valider les couleurs, la morphologie et les asymétries du corps entier.
- Les images Greg Mitchell identifiées par une légende secondaire comme Wakaatu montrent en réalité Scorpio ou un Snatcher après inspection ; elles ne sont pas retenues pour cette créature.

### Clayton Carmine — modèle multijoueur Gears 5 Operation 3 — `clayton_skin_02`

- Journal : [clayton_skin_02_record.json](../../data/generation_v12/clayton_skin_02_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [clayton_gears5_operation3.png](../../assets/costumes_v12/clayton_gears5_operation3.png).
- Portée : `reference_fullbody` ; relation d’édition : `edition_unverified`.
- [official_game_promotional_screenshot](https://news.xbox.com/en-us/2020/03/31/gears-5-operation-3-gridiron-available-today-for-all-players/) — Capture officielle du modèle multijoueur Clayton Carmine pour Gears 5 Operation 3, silhouette complète avec arme lourde. Les effets de bouclier masquent certains détails. Ne prouve ni un nom de skin « Vétéran » ni une variante de campagne.

**Constats et limites**

- Un seul personnage entier, casque, bras nus, protections et bottes dans le cadre ; arme tenue sans tir.
- Copie native sans réencodage ; alpha réel mesuré.
- Les effets de bouclier et le décor de la capture n'ont pas été repris.
- Les petits slogans, tatouages, gravures et détails de l'arme restent une interprétation générée, pas une copie certifiée.
- Marges verticales étroites (18 px en haut et 16 px en bas à alpha >=128), sans coupe du personnage.
- Franges de couleur fines sur quelques contours : inspection sur fond contrasté requise avant production.
- Correspondance avec le libellé interne « Vétéran Gears 5 » non prouvée : edition_unverified conservé.

### Del Walker — Outsider Gears 4, candidat de concept — `del_skin_01`

- Journal : [del_skin_01_record.json](../../data/generation_v12/del_skin_01_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [del_skin_01.png](../../assets/costumes_v12/del_skin_01.png).
- Portée : `reference_fullbody` ; relation d’édition : `edition_unverified`.
- [publisher_released_preproduction_concept_rehosted_by_press](https://www.gamempire.it/gears-of-war-4-rilasciate-nuove-immagini/) — Concept Microsoft en pied de Del Outsider publié en avril 2016. Silhouette complète ; visage et couleurs du haut du corps varient par rapport à la capture de campagne. Ce n'est pas un rendu final.
- [first_party_concept_artist_development_sheet](https://crazybrush.artstation.com/projects/5ZNDw) — Planche Gears 4 de Goran Bukvic : figures colorées avant/arrière de Del à droite, utilisée pour la géométrie complète du vêtement et des bottes. Document de développement, pas modèle final.
- [secondary_press_in_game_campaign_capture](https://www.gamespot.com/articles/gears-of-war-4s-campaign-mixes-guns-and-gore-with-/1100-6443693/) — Capture de campagne Gears of War 4 à l'armurerie de Marcus : JD deuxième depuis la gauche, Del à l'extrême droite. Visages, couleurs et accessoires visibles comparés aux concepts ; bas des bottes hors cadre.
- [secondary_in_game_cutscene_thumbnail](https://www.youtube.com/watch?v=oubS8ZB5Ias) — Vignette de cinématique Comic-Con 2016 consultée uniquement pour corroborer vestes, couleurs et harnais Outsider de JD/Del ; seule la vignette a été inspectée, pas la vidéo complète. Pieds hors cadre. Non transmise au générateur.

**Constats et limites**

- Un seul Del en pied, regard et bottes vers la droite ; veste brun rouille, lunettes jaunes au cou, harnais à lumière bleue, haut à manches superposées, pantalon côtelé sombre et bottes lacées présents.
- La coupe de cheveux, le visage et la barbe sont interprétés ; la barbe générée est plus marquée que celle de la capture de campagne. Les manches supérieures olive restent à comparer à la teinte moutarde du jeu.
- Le vêtement complet dérive des concepts avant/arrière ; la capture finale corrobore seulement les parties visibles, sans certifier le bas du corps.
- Pose surtout de trois-quarts frontal, mains ouvertes : adaptation à la garde latérale encore à valider.
- RGBA 1024 × 1536, 70,73 % alpha=0. Bordure de 8 px alpha maximum 1.
- Silhouette complète ; marges alpha >=128 [196,86,218,48] px. L'objectif de 10 % de marge verticale n'est pas atteint.

### Dominic Santiago — E-Day — `dom_skin_01`

- Journal : [dom_skin_01_record.json](../../data/generation_v12/dom_skin_01_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [dom_eday.png](../../assets/costumes_v12/dom_eday.png).
- Portée : `reference_fullbody` ; relation d’édition : `target_version_candidate`.
- [production_character_artist_render](https://vincerizzi.artstation.com/projects/xddAmR) — Modèle final texturé en pied, vue trois-quarts ; bottes et équipement de jambe visibles.
- [production_character_artist_render](https://vincerizzi.artstation.com/projects/xddAmR) — Deuxième vue en pied, orientation vers la droite ; asymétries, tatouage et deux bottes visibles.
- [production_character_artist_render](https://vincerizzi.artstation.com/projects/xddAmR) — Vue rapprochée du torse, des mains, du couteau, de la lampe, de la ceinture et de la poche.
- [production_character_artist_render](https://vincerizzi.artstation.com/projects/xddAmR) — Gros plan de la tête, cheveux, barbe, armure et lampe du même modèle.

**Constats et limites**

- Une seule silhouette complète ; casque absent conformément au modèle, cheveux courts, barbe, boucle d'oreille, tenue camouflage et armure à disques pectoraux.
- Couteau conservé sur le côté droit anatomique du torse, lampe au col gauche, munitions à l'avant-bras gauche et poche à la hanche gauche ; pas de miroir global du personnage.
- Références de production complètes jusqu'aux deux semelles ; aucune substitution depuis les éditions 2006, Gears 2 ou Gears 3.
- Tatouage, camouflage, rayures, rivets et petits composants sont recomposés et demandent une comparaison détaillée.
- Sortie native conservée sans recadrage, redimensionnement ni réencodage.
- Transparence réelle mesurée : 58.39% de pixels alpha=0 ; maximum alpha=254.
- Marges à alpha >=128 : [114, 121, 110, 41] px ; corps entièrement dans le cadre, mais objectif de 12 % vertical non atteint.

### Fahz Chutani — Hivebuster Fahz — `fahz_hivebuster_g5`

- Journal : [fahz_hivebuster_g5_record.json](../../data/generation_v12/fahz_hivebuster_g5_record.json).
- État : `blocked_generator_refusal` ; génération tentée : non.
- Aucun PNG ajouté pour cette cible.
- [first_party_publisher_announcement](https://store.steampowered.com/news/posts/?appids=1097840&enddate=1615235906&feed=steam_community_announcements) — Annonce officielle Gears 5 Operation 6 du 1 mars 2021 ; skin Hivebuster Fahz nommé et illustré dans la carte Sergeant de la planche Tour of Duty. Le portrait montre surtout le torse.
- [secondary_in_game_capture_thumbnail](https://www.youtube.com/watch?v=53GczcfTpH0) — Vignette de SASxSH4DOWZ, vidéo Hivebuster Fahz du 5 mars 2021 : modèle du costume en gros plan, torse et tête. Vidéo non visionnée intégralement, seule la vignette a été inspectée.
- [first_party_character_artist](https://kend.artstation.com/projects/e0rE5D) — Rendu en pied de Fahz par Kenneth Doyle, artiste du corps/textures. Modèle standard Gears 5 utilisé seulement pour identité, proportions et jambe droite prothétique, pas comme preuve de la tenue Hivebuster.

**Constats et limites**

- Sources officielles et vignette de capture du costume inspectées avant l'unique appel.
- Refus au stade sortie : aucun PNG reçu ; aucun réessai ni reformulation.
- Le modèle standard ne certifie pas les éventuelles différences du bas du costume Hivebuster.

### JACK — Gears Tactics — `jack_skin_02`

- Journal : [jack_skin_02_record.json](../../data/generation_v12/jack_skin_02_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [jack_tactics.png](../../assets/costumes_v12/jack_tactics.png).
- Portée : `reference_fullbody` ; relation d’édition : `target_version_candidate`.
- [third_party_republished_render](https://www.pngaaa.com/detail/5767279) — Rendu complet attribué par le site au Developer Blog JACK Tactics ; origine éditoriale indépendante non prouvée par ce miroir seul. Construction et silhouette corroborées par l'image officielle Tactics.
- [official_game_promotional_screenshot](https://www.gearsofwar.com/en-us/games/gears-tactics/) — Capture officielle de la section New Content : JACK entier dans le quart supérieur gauche ; quatre optiques, carrosserie, antenne et deux bras distincts visibles. Confirme l'édition Tactics du modèle, mais pas tous les petits détails cachés.
- [official_developer_blog](https://www.gearsofwar.com/en-us/news/developer-blog-jack-skills/) — Annonce du 3 novembre 2020 confirmant JACK comme ajout de Gears Tactics ; texte et icône/arbre de compétences, sans preuve complète du modèle à partir de cette page seule.

**Constats et limites**

- Un seul robot complet : quatre grandes optiques bleues, antenne, plaque supérieure et deux bras/outils distincts.
- Transparence réelle mesurée ; absence du damier de la référence.
- Copie native conservée sans recadrage, redimensionnement ni réencodage.
- Silhouette et composants principaux cohérents avec la capture officielle Tactics ; fidélité microscopique non validée.
- Marge basse étroite : 17 px à alpha >=128 ; toutes les griffes restent dans le cadre.
- De minces franges colorées sont visibles sur certains bords métalliques : contrôle à fond clair et correction future requise avant production.

### JD Fenix — Outsider Gears 4, candidat de concept — `jd_skin_01`

- Journal : [jd_skin_01_record.json](../../data/generation_v12/jd_skin_01_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [jd_skin_01.png](../../assets/costumes_v12/jd_skin_01.png).
- Portée : `reference_fullbody` ; relation d’édition : `edition_unverified`.
- [publisher_released_preproduction_concept_rehosted_by_press](https://www.gamempire.it/gears-of-war-4-rilasciate-nuove-immagini/) — Concept Microsoft en pied de JD Outsider publié en avril 2016 : habit, harnais, pantalon, holster et bottes complets. Ce n'est pas un rendu du modèle final. La sortie Microsoft de concepts et captures est également rapportée par GameSpot.
- [secondary_press_in_game_campaign_capture](https://www.gamespot.com/articles/gears-of-war-4s-campaign-mixes-guns-and-gore-with-/1100-6443693/) — Capture de campagne Gears of War 4 à l'armurerie de Marcus : JD deuxième depuis la gauche, Del à l'extrême droite. Visages, couleurs et accessoires visibles comparés aux concepts ; bas des bottes hors cadre.
- [secondary_in_game_cutscene_thumbnail](https://www.youtube.com/watch?v=oubS8ZB5Ias) — Vignette de cinématique Comic-Con 2016 consultée uniquement pour corroborer vestes, couleurs et harnais Outsider de JD/Del ; seule la vignette a été inspectée, pas la vidéo complète. Pieds hors cadre. Non transmise au générateur.
- [press_attestation_of_microsoft_release](https://www.gamespot.com/articles/look-at-all-these-gears-of-war-4-campaign-high-res/1100-6439201/) — Article décrivant le lot d'images fourni par Microsoft, dont les concepts de personnages. Attribution et contexte de préproduction, pas référence de modèle final.

**Constats et limites**

- Un seul jeune JD blond en pied, tourné à droite en trois-quarts ; veste brune, foulard olive, couche grise à capuche, manches sombres, harnais diagonal à lumière bleue, pantalon beige et holster à la cuisse droite présents.
- La capture de campagne corroborait ces éléments du haut du corps ; le visage généré et les finitions du vêtement restent interprétés, sans validation du modèle final.
- Le rendu est surtout frontal de trois-quarts, mains ouvertes et garde peu marquée ; ce n'est pas encore la pose latérale cible.
- RGBA 1024 × 1536, 69,19 % alpha=0, bordure de 8 px entièrement transparente. Les couleurs de fond visibles dans certains aperçus ne prouvent pas un fond opaque.
- Silhouette entière ; marges alpha >=128 [195,93,220,50] px. L'objectif de 10 % de marge verticale n'est pas atteint.

### Kait Diaz — Désert Gears 5 — `kait_skin_03`

- Journal : [kait_skin_03_record.json](../../data/generation_v12/kait_skin_03_record.json).
- État : `blocked_generator_refusal` ; génération tentée : non.
- Aucun PNG ajouté pour cette cible.
- [first_party_art_director_production_turnaround](https://mediumrare.artstation.com/projects/OyVRz8) — Trois vues officielles en pied de Kait Désert Gears 5, Aryan Hanbeck / The Coalition, 19 septembre 2019 : lunettes rondes, foulard sable, bras nus avec tatouage gauche, bottes sanglées. Image entière inspectée avant l'unique tentative ; autres variantes du même portfolio exclues.

**Constats et limites**

- Référence primaire spécifique en pied avant/arrière du costume trouvée et inspectée.
- Les images Bruno Melo regular et Hanbeck hiver/standard ont été comparées puis exclues pour éviter de mélanger les variantes.
- L'unique appel a été refusé au stade sortie : aucun PNG reçu, aucun réessai ni reformulation.

### Kantus — Gears Tactics — `kantus_skin_02`

- Journal : [kantus_skin_02_record.json](../../data/generation_v12/kantus_skin_02_record.json).
- État : `blocked_generator_refusal` ; génération tentée : oui.
- Aucun PNG ajouté pour cette cible.
- [production_artist_final_model](https://darkmummy.artstation.com/projects/xza2QW) — Rendu couleur du modèle complet : face et deux vues trois-quarts ; tenue, proportions, griffes et ourlet.
- [production_artist_final_model](https://darkmummy.artstation.com/projects/xza2QW) — Rendu couleur de profil droit et gauche complet : casque, dos et robe.
- [production_artist_final_model](https://darkmummy.artstation.com/projects/xza2QW) — Gros plans couleur du visage et du casque.

**Constats et limites**

- Trois références couleur du modèle de production Tactics contrôlées avant génération.
- Aucune image livrée : rejet de sécurité lors de la génération de sortie.
- Aucun contournement, aucune nouvelle tentative après le refus.

### Drone locuste — E-Day — `locust_drone_skin_02`

- Journal : [locust_drone_skin_02_record.json](../../data/generation_v12/locust_drone_skin_02_record.json).
- État : `reference_research_pending` ; génération tentée : non.
- Aucun PNG ajouté pour cette cible.
- [first_party_art_director_production_render](https://www.artstation.com/artwork/xddAaO) — Portrait du modèle en jeu : tête et peau visibles, mais pas le corps, les jambes ou l'équipement complet.
- [production_character_artist_portfolio](https://www.artstation.com/artwork/KR3KG4) — La page crédite les parties organiques du Drone. Les trois images dr01/dr02/dr03 identifiées par les métadonnées publiques n'ont pas pu être téléchargées (HTTP 403). Elles n'ont donc pas été inspectées et ne prouvent pas ici une référence en pied.
- [production_concept_artist_portfolio](https://giorgiobaroni.artstation.com/projects/mOOgBZ) — Explorations anatomiques précoces, identifiées comme concepts par l'auteur ; ne remplacent pas une vue du modèle final habillé.

**Constats et limites**

- La tête de l'édition cible est établie par un rendu de production, mais pas le costume entier.
- Aucun corps de Drone 2006, Ultimate Edition ou d'une autre édition n'a été substitué.
- Aucun appel de génération effectué pour cette cible pendant V12.

### Marcus Fenix — E-Day — `marcus_skin_01`

- Journal : [marcus_skin_01_record.json](../../data/generation_v12/marcus_skin_01_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [marcus_eday.png](../../assets/costumes_v12/marcus_eday.png).
- Portée : `reference_fullbody` ; relation d’édition : `target_version_candidate`.
- [production_character_artist_render](https://www.artstation.com/artwork/Z00gZ1) — Rendu texturé de face, tête, torse, bras et cuisses ; les bottes ne sont pas dans cette vue.
- [production_character_artist_render](https://www.artstation.com/artwork/Z00gZ1) — Construction avant/arrière du torse ; la vue ne couvre pas le corps entier.
- [production_character_artist_render](https://www.artstation.com/artwork/Z00gZ1) — Bottes du même modèle, vues avant/arrière et trois-quarts.
- [production_character_artist_render](https://www.artstation.com/artwork/Z00gZ1) — Géométrie haute définition du corps et des jambes en deux poses accroupies ; matériau gris de sculpture, pas couleur du costume.
- [production_character_artist_render](https://www.artstation.com/artwork/Z00gZ1) — Gros plan texturé de la tête et du bandana du modèle de production.

**Constats et limites**

- Modèle jeune, bandana, armure à disques pectoraux, manches et protections complètes, deux poches et bottes comparés aux cinq vues du même modèle E-Day.
- Une seule silhouette complète ; sortie native conservée sans recadrage ni réencodage.
- Transparence réelle mesurée ; le maximum alpha de la sortie est 254 et de faibles valeurs alpha persistent autour de certains contours.
- Marges verticales de 68 et 70 px : l'objectif de 12 % n'est pas atteint, mais tête et semelles restent entièrement dans le cadre.
- Pose recomposée et détails fins interprétés : ne vaut pas une certification de fidélité 1:1.

### Reine Reyna — Blood Red Queen Reyna — `reyna_blood_red_g5`

- Journal : [reyna_blood_red_g5_record.json](../../data/generation_v12/reyna_blood_red_g5_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [reyna_blood_red_g5.png](../../assets/costumes_v12/reyna_blood_red_g5.png).
- Portée : `reference_fullbody` ; relation d’édition : `target_version_candidate`.
- [first_party_publisher_announcement](https://store.steampowered.com/news/posts/?appids=1097840&enddate=1615235906&feed=steam_community_announcements) — Planche Tour of Duty Operation 6 : carte General Blood Red Queen Reyna, skin nommément attesté dans le tableau officiel.
- [secondary_in_game_capture_thumbnail](https://www.youtube.com/watch?v=6qjLRKGjoXk) — Vignette de SASxSH4DOWZ, Blood Red Queen Reyna, publiée le 7 mars 2021. Couleurs et détails tête/torse du skin ; seule la vignette a été inspectée, pas la vidéo complète.
- [first_party_publisher_promotional_render](https://store.steampowered.com/news/posts/?appgroupname=Gears+5&appids=1097840&enddate=1617721047&feed=steam_community_announcements) — Rendu Queen Reyna standard, Reveal Operation 6 du 23 février 2021 ; complément pour géométrie des plaques et tentacules visibles, pas preuve de couleur Blood Red ni des extrémités inférieures.
- [secondary_model_preview](https://www.deviantart.com/jorn-k-nightmane/art/Queen-Reyna-Gears5-for-XPS-FBX-1014298182) — Aperçu XPS/FBX de Jorn-K-Nightmane retrouvé par recherche d'images ; variantes standard et Blood Red côte à côte, seule la droite est utilisée. Image téléchargée et inspectée, texte de la page inaccessible (403) ; provenance d'export non certifiée. Bas des tentacules hors cadre.

**Constats et limites**

- Une seule Reyna, face et silhouette tournées à droite en trois-quarts ; peau charbon, fissures rouges, cheveux noirs, cristaux rouges et grandes plaques organiques d'épaules cohérents avec les références visibles.
- Référence primaire de la variante limitée au portrait ; le rendu standard et deux sources secondaires complètent la géométrie du torse.
- Les extrémités inférieures et l'agencement des longs tentacules sont reconstitués ; aucun pied ni corps inférieur canonique complet n'est certifié.
- La géométrie exacte des cristaux, le visage, les fissures et asymétries restent à comparer au modèle de jeu.
- PNG RGBA réel : 56,10 % de pixels alpha=0 ; le halo rouge visible dans certains aperçus est contenu dans des couleurs RGB de pixels alpha=0 aux points sondés, sans fond opaque à ces endroits.
- Marges alpha >=128 : gauche 71, haut 65, droite 68, bas 41 px. Silhouette entière, mais marges cibles de 10 % non atteintes.

### Drone de l'Essaim — Gears 5 standard — `swarm_drone_skin_02`

- Journal : [swarm_drone_skin_02_record.json](../../data/generation_v12/swarm_drone_skin_02_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [swarm_drone_skin_02.png](../../assets/costumes_v12/swarm_drone_skin_02.png).
- Portée : `reference_fullbody` ; relation d’édition : `target_version_candidate`.
- [first_party_art_director_production_render](https://mediumrare.artstation.com/projects/6aoByW?album_id=1597441) — Gears 5 Drone Swarm Rifleman : rendu officiel avant/arrière en pied, par Aryan Hanbeck / The Coalition. Référence spécifique du costume Gears 5 standard ; pas de pièces UIR.

**Constats et limites**

- Un Drone entier tourné vers la droite en trois-quarts, peau épaisse brun-orangé, plaques de métal gris irrégulières, chaînes, pagne frangé et pieds griffus cohérents avec le modèle officiel Gears 5.
- La première sortie inversait le côté anatomique du harnais ; une édition ciblée avec le rendu officiel a remis l'attache haute à l'épaule gauche anatomique et l'attache basse à la hanche droite. Le personnage entier n'a pas été retourné.
- Le modèle officiel est complet en pied ; la pose latérale et les surfaces nouvellement visibles restent une interprétation générative.
- RGBA natif 1199 × 1312, 66,56 % alpha=0. Copie de la sortie finale sans retouche raster.
- Marges alpha >=128 : [236, 104, 247, 49] px ; silhouette complète, mais objectif de 10 % de marge verticale non atteint.

### Drone de l'Essaim — Swarm Elite Drone UIR — `swarm_drone_uir_g5`

- Journal : [swarm_drone_uir_g5_record.json](../../data/generation_v12/swarm_drone_uir_g5_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [swarm_drone_uir_g5.png](../../assets/costumes_v12/swarm_drone_uir_g5.png).
- Portée : `reference_fullbody` ; relation d’édition : `target_version_candidate`.
- [first_party_publisher_announcement](https://store.steampowered.com/news/posts/?appids=1097840&enddate=1615235906&feed=steam_community_announcements) — Planche officielle Tour of Duty Operation 6 : carte Private UIR Elite Drone ; tableau nommé Swarm Elite Drone UIR. Modèle Elite, distinct du Drone de base.
- [secondary_in_game_model_thumbnail](https://www.youtube.com/watch?v=pPsR_3vJm9s) — Vignette SASxSH4DOWZ du 14 mars 2021 présentant exactement UIR Elite Swarm Drone : plaques vert olive de casque/torse, harnais et cartouche. Seule la vignette a été inspectée.
- [first_party_art_director_production_render](https://mediumrare.artstation.com/projects/6aoByW?album_id=1597441) — Rendu officiel en pied avant/arrière Gears 5 Drone Swarm Rifleman, Aryan Hanbeck, The Coalition. Appui anatomie et silhouette du bas du corps ; ne certifie pas les détails UIR des zones hors référence du skin.

**Constats et limites**

- Un Drone massif entier tourné à droite en trois-quarts ; plaque de casque verte asymétrique, fragment de torse olive, harnais segmenté, voyants orange-rouge et cartouche jaune/noire cohérents avec la capture du skin.
- La référence officielle en pied du rifleman sert au bas du corps, mais ne certifie pas les éventuelles différences UIR des jambes/plaques.
- Les détails de visage, dents, motifs, attaches, chaînes et plaques sont des approximations génératives à valider.
- RGBA réel : 59,96 % alpha=0 ; dimensions natives 1159 × 1357, sans mise à l'échelle.
- Marges alpha >=128 : [150, 73, 177, 45] px ; silhouette entière, mais marges verticales de 10 % non atteintes.

### Garde Theron — Gears Tactics — `theron_skin_02`

- Journal : [theron_skin_02_record.json](../../data/generation_v12/theron_skin_02_record.json).
- État : `reference_research_pending` ; génération tentée : non.
- Aucun PNG ajouté pour cette cible.
- [official_developer_blog_partial_render](https://www.gearsofwar.com/en-us/news/dev-blog-enemies/) — La page officielle situe Theron dans Tactics ; le visuel montre une tête nue et l'armure jusqu'aux genoux, avec mollets et pieds hors cadre. Cette illustration de blog ne suffit pas à attester tous les détails du modèle final en pied.
- [third_party_gameplay_screenshot](https://www.jeuxvideo.com/wikis-soluce-astuces/1235733/chapitre-5-contrebande.htm) — Capture de l'introduction en jeu, titrée GARDE THERON, confirmant tête nue, haut d'armure et panneaux orange. Gros plan coupé au torse ; pas de jambes ni de pieds. Sert à contrôler l'édition, pas à compléter arbitrairement le corps.
- [third_party_gameplay_screenshot](https://www.jeuxvideo.com/wikis-soluce-astuces/1235733/chapitre-5-contrebande.htm) — Vue tactique éloignée de la mission ; les sujets et bas de corps sont trop petits pour établir une référence de costume détaillée.
- [third_party_gameplay_video_index](https://www.youtube.com/watch?v=6sjDDwzKuvg) — Description consultée : introduction du Theron à 02:50. Vidéo non visionnée ; aucune image non inspectée utilisée comme preuve.

**Constats et limites**

- L'identité Garde Theron et sa présence dans Gears Tactics sont attestées.
- Aucune vue complète suffisamment détaillée de la bonne édition n'a été réunie dans cette recherche.
- Le visuel officiel partiel et le gros plan en jeu ne prouvent pas les mollets, pieds, dos, asymétries et position exacte de l'arc.
- Aucune génération à partir du nom seul ; aucun mélange avec Theron Gears 5, Theron 2006 ou Sentinelle.

### Zealot locuste — Collector's Zealot — `zealot_collectors_g5`

- Journal : [zealot_collectors_g5_record.json](../../data/generation_v12/zealot_collectors_g5_record.json).
- État : `generated_reference_pending_validation` ; génération tentée : oui.
- PNG actif : [zealot_collectors_g5.png](../../assets/costumes_v12/zealot_collectors_g5.png).
- Portée : `reference_fullbody` ; relation d’édition : `target_version_candidate`.
- [first_party_publisher_announcement](https://store.steampowered.com/news/posts/?appids=1097840&enddate=1615235906&feed=steam_community_announcements) — Planche Tour of Duty Operation 6 : Collector's Zealot, carte Recruit. Nom et palette de variante attestés, cadrage tête/torse.
- [secondary_in_game_card_thumbnail](https://www.youtube.com/watch?v=VahwszbRItk) — Vignette SASxSH4DOWZ du 2 mars 2021, carte agrandie explicitement étiquetée Collector's Zealot. Tête et haut de l'armure ; vidéo complète non visionnée.
- [first_party_publisher_promotional_render](https://store.steampowered.com/news/posts/?appgroupname=Gears+5&appids=1097840&enddate=1617721047&feed=steam_community_announcements) — Zealot standard Gears 5, annonce Reveal Operation 6 du 23 février 2021. Référence de géométrie casque/torse/tassets, pas preuve du motif Collector's sur les zones non montrées. Bas des jambes et pieds hors cadre.

**Constats et limites**

- Un Zealot entier, trois-quarts orienté à droite, casque pointu à crête, plaques sombres à bordures métalliques, harnais et composants jaunes cohérents avec le portrait Collector's.
- La silhouette du casque, les lignes rouges et les motifs du harnais sont des approximations génératives à comparer au modèle exact.
- Le rendu officiel standard Gears 5 ne montre pas les chevilles/pieds ; ces éléments et certains détails des tassets ont été reconstitués. Aucun rendu Tactics n'a servi à cette génération.
- RGBA réel : 64,77 % de pixels alpha=0 ; le halo d'aperçu ne doit pas être interprété comme un fond opaque.
- Marges alpha >=128 : [154, 33, 162, 42] px ; corps et pieds entiers, mais marges verticales de 10 % non atteintes.

## Ce que cette passe ne valide pas

Les PNG ne créent aucun personnage jouable, aucune hitbox, aucune animation, aucun calque de parallaxe et aucun comportement des extensions. Les comparaisons d’édition, de visage, d’équipement, d’asymétrie et de silhouette restent des validations artistiques par sujet. Les nombres de fichiers actifs, d’archives, de refus et de manques exacts sont donnés dans le [listing V12](../production/LISTING_V12.md) et la [reprise V12](../production/REPRISE_V12.md).
