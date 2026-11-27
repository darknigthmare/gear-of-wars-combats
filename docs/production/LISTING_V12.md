# Listing V12 — images statiques réellement ajoutées

Date : **27 novembre 2026**. Base de comparaison : `370e49593ee6690076b4051afc7357d1e1707aad` (V11).

**12 nouveaux PNG natifs**, associés à leurs journaux individuels ; **148 PNG actifs uniques** après consolidation. Aucun sprite animé ni calque de parallaxe séparé n’est déclaré livré.

Les dimensions sont celles des fichiers présents. « Avec référence » signifie candidat statique consultable ; l’existence du fichier ne valide ni sa fidélité 1:1 ni une intégration jouable.

## Costumes

| Sujet | Édition / portion représentée | PNG | Dimensions natives | État | Journal |
|---|---|---|---|---|---|
| Clayton Carmine — modèle multijoueur Gears 5 Operation 3 | Modèle multijoueur Gears 5 Operation 3 montré par Xbox Wire le 31 mars 2020 | [Image](../../assets/costumes_v12/clayton_gears5_operation3.png) | 1151 × 1367 | candidate / edition_unverified | [Provenance et prompt](../../data/generation_v12/clayton_skin_02_record.json) |
| Del Walker — Outsider Gears 4, candidat de concept | Del Outsider — concept Goran Bukvic/Microsoft, corroboration partielle campagne | [Image](../../assets/costumes_v12/del_skin_01.png) | 1024 × 1536 | candidate / edition_unverified | [Provenance et prompt](../../data/generation_v12/del_skin_01_record.json) |
| Dominic Santiago — E-Day | Dom jeune — modèle de production E-Day | [Image](../../assets/costumes_v12/dom_eday.png) | 1024 × 1536 | candidate / target_version_candidate | [Provenance et prompt](../../data/generation_v12/dom_skin_01_record.json) |
| JACK — Gears Tactics | JACK Tactics — robot de soutien à quatre optiques, bras manipulateur et outil distincts | [Image](../../assets/costumes_v12/jack_tactics.png) | 1363 × 1154 | candidate / target_version_candidate | [Provenance et prompt](../../data/generation_v12/jack_skin_02_record.json) |
| JD Fenix — Outsider Gears 4, candidat de concept | JD Outsider — concept Microsoft avril 2016, corroboration partielle campagne | [Image](../../assets/costumes_v12/jd_skin_01.png) | 1024 × 1536 | candidate / edition_unverified | [Provenance et prompt](../../data/generation_v12/jd_skin_01_record.json) |
| Marcus Fenix — E-Day | Marcus jeune — modèle de production E-Day | [Image](../../assets/costumes_v12/marcus_eday.png) | 1024 × 1536 | candidate / target_version_candidate | [Provenance et prompt](../../data/generation_v12/marcus_skin_01_record.json) |
| Reine Reyna — Blood Red Queen Reyna | Blood Red Queen Reyna — skin multijoueur Operation 6, tentacules inférieurs reconstitués | [Image](../../assets/costumes_v12/reyna_blood_red_g5.png) | 1024 × 1536 | candidate / target_version_candidate | [Provenance et prompt](../../data/generation_v12/reyna_blood_red_g5_record.json) |
| Drone de l'Essaim — Gears 5 standard | Swarm Drone Rifleman — modèle standard Gears 5 | [Image](../../assets/costumes_v12/swarm_drone_skin_02.png) | 1199 × 1312 | candidate / target_version_candidate | [Provenance et prompt](../../data/generation_v12/swarm_drone_skin_02_record.json) |
| Drone de l'Essaim — Swarm Elite Drone UIR | UIR Elite Drone — skin multijoueur Gears 5 Operation 6 | [Image](../../assets/costumes_v12/swarm_drone_uir_g5.png) | 1159 × 1357 | candidate / target_version_candidate | [Provenance et prompt](../../data/generation_v12/swarm_drone_uir_g5_record.json) |
| Zealot locuste — Collector's Zealot | Collector's Zealot — skin multijoueur Gears 5 Operation 6 | [Image](../../assets/costumes_v12/zealot_collectors_g5.png) | 1024 × 1536 | candidate / target_version_candidate | [Provenance et prompt](../../data/generation_v12/zealot_collectors_g5_record.json) |

## Boss, créatures et machines

| Sujet | Édition / portion représentée | PNG | Dimensions natives | État | Journal |
|---|---|---|---|---|---|
| Flock | Gears 5 — essaim de Leeches, formation collective recomposée | [Image](../../assets/bosses_v12/flock_gears5_swarm.png) | 1374 × 1145 | candidate / target_version_candidate | [Provenance et prompt](../../data/generation_v12/boss_flock_record.json) |
| Kraken | Gears 5 — tête et manteau exposés du Kraken, ensemble central seulement | [Image](../../assets/bosses_v12/kraken_gears5_head_mantle.png) | 1727 × 910 | candidate / target_version_candidate | [Provenance et prompt](../../data/generation_v12/boss_kraken_record.json) |

## Réserves de chaque nouvelle image

### Flock

Identifiant : `boss_flock`. [PNG](../../assets/bosses_v12/flock_gears5_swarm.png) · [Journal](../../data/generation_v12/boss_flock_record.json).

- Un seul Flock : plusieurs Leeches forment une entité collective, conformément à la nature du sujet ; il ne s'agit pas d'une planche de personnages.
- La révision a réduit la taille relative des organismes et diversifié leurs directions. La densité et le mouvement collectif restent une recomposition, pas la copie d'une frame de jeu.
- Le jeu montre des détails plus petits et moins séparables : disposition, nombre, proportions exactes, rigidité des manteaux et intensité des lumières internes restent à comparer.
- Marge minimale de 125 pixels à alpha >=128. Toutes les extrémités principales restent dans le cadre ; cible de 12 % non atteinte verticalement.
- Aucun effet de fumée, fond, interface ou géant central ajouté. Les Leeches ne sont pas des assets séparés livrés par ce PNG.
- Comparer le volume et la densité de l'essaim sur plusieurs captures Gears 5 ; vérifier que les couches ne ressemblent pas à un empilement rigide.
- Contrôler l'anatomie et les éléments fins de chaque Leech discernable, ainsi que les franges d'alpha avant utilisation.
- Aucune dispersion, recomposition, attaque, animation ou logique de boss produite.

### Kraken

Identifiant : `boss_kraken`. [PNG](../../assets/bosses_v12/kraken_gears5_head_mantle.png) · [Journal](../../data/generation_v12/boss_kraken_record.json).

- Référence partielle du Kraken : tête, manteau et bases des appendices seulement ; aucun corps complet revendiqué.
- Bouche verticale, crête centrale, carapace irrégulière et lumières internes orange reprises des rendus du créateur.
- Marge minimale finale mesurée de 117 pixels ; supérieur au seuil 10 % sur chaque bord mais consigne de 15 % non atteinte en bas.
- Réorientation légère et recadrage ont recomposé certains détails de dentition, crêtes et peau ; conformité 1:1 à contrôler.
- Comparer les volumes exacts, la dentition et les saccules à des vues orthographiques ou captures complémentaires.
- Produire séparément tendrils et langue, sans les considérer livrés par cette image.
- Contrôler les fines franges colorées avant atlas ; garder les octets natifs.

### Clayton Carmine — modèle multijoueur Gears 5 Operation 3

Identifiant : `clayton_skin_02`. [PNG](../../assets/costumes_v12/clayton_gears5_operation3.png) · [Journal](../../data/generation_v12/clayton_skin_02_record.json).

- Un seul personnage entier, casque, bras nus, protections et bottes dans le cadre ; arme tenue sans tir.
- Copie native sans réencodage ; alpha réel mesuré.
- Les effets de bouclier et le décor de la capture n'ont pas été repris.
- Les petits slogans, tatouages, gravures et détails de l'arme restent une interprétation générée, pas une copie certifiée.
- Marges verticales étroites (18 px en haut et 16 px en bas à alpha >=128), sans coupe du personnage.
- Franges de couleur fines sur quelques contours : inspection sur fond contrasté requise avant production.
- Correspondance avec le libellé interne « Vétéran Gears 5 » non prouvée : edition_unverified conservé.
- Valider la correspondance de la tenue demandée « Vétéran » avec ce modèle Opération 3 avant de considérer le slot couvert dans la bonne variante.
- Contrôler tatouages, inscriptions et asymétries sur des captures rapprochées de cette édition.
- Contrôler composants de l'arme et parties masquées par le bouclier dans la source.
- Contrôler bords alpha et marges, puis seulement préparer une future passe de production.
- Aucune animation, collision ni intégration moteur produite.

### Del Walker — Outsider Gears 4, candidat de concept

Identifiant : `del_skin_01`. [PNG](../../assets/costumes_v12/del_skin_01.png) · [Journal](../../data/generation_v12/del_skin_01_record.json).

- Candidat de concept Outsider, corroboré seulement sur les parties visibles dans des captures de campagne. Le modèle final complet n'est pas validé ; édition à vérifier, fidélité 1:1 non certifiée.
- Les détails des jambes et bottes proviennent principalement du concept de préproduction. Aucune confusion avec les rendus COG Armoured, explicitement exclus.
- Une seule tentative imagegen. PNG natif copié octet pour octet, sans retouche, agrandissement, animation ni spritesheet.
- Un seul Del en pied, regard et bottes vers la droite ; veste brun rouille, lunettes jaunes au cou, harnais à lumière bleue, haut à manches superposées, pantalon côtelé sombre et bottes lacées présents.
- La coupe de cheveux, le visage et la barbe sont interprétés ; la barbe générée est plus marquée que celle de la capture de campagne. Les manches supérieures olive restent à comparer à la teinte moutarde du jeu.
- Le vêtement complet dérive des concepts avant/arrière ; la capture finale corrobore seulement les parties visibles, sans certifier le bas du corps.
- Pose surtout de trois-quarts frontal, mains ouvertes : adaptation à la garde latérale encore à valider.
- RGBA 1024 × 1536, 70,73 % alpha=0. Bordure de 8 px alpha maximum 1.
- Silhouette complète ; marges alpha >=128 [196,86,218,48] px. L'objectif de 10 % de marge verticale n'est pas atteint.
- Comparer et corriger si nécessaire la ressemblance du visage, la longueur des cheveux et la barbe par rapport au modèle final Gears 4.
- Vérifier les couleurs, la disposition exacte des bretelles, le fourreau, les coutures et les bottes sur le modèle final complet.
- Valider la pose latérale de combat, les marges et le rendu des contours alpha dans le moteur.

### Dominic Santiago — E-Day

Identifiant : `dom_skin_01`. [PNG](../../assets/costumes_v12/dom_eday.png) · [Journal](../../data/generation_v12/dom_skin_01_record.json).

- Une seule silhouette complète ; casque absent conformément au modèle, cheveux courts, barbe, boucle d'oreille, tenue camouflage et armure à disques pectoraux.
- Couteau conservé sur le côté droit anatomique du torse, lampe au col gauche, munitions à l'avant-bras gauche et poche à la hanche gauche ; pas de miroir global du personnage.
- Références de production complètes jusqu'aux deux semelles ; aucune substitution depuis les éditions 2006, Gears 2 ou Gears 3.
- Tatouage, camouflage, rayures, rivets et petits composants sont recomposés et demandent une comparaison détaillée.
- Sortie native conservée sans recadrage, redimensionnement ni réencodage.
- Transparence réelle mesurée : 58.39% de pixels alpha=0 ; maximum alpha=254.
- Marges à alpha >=128 : [114, 121, 110, 41] px ; corps entièrement dans le cadre, mais objectif de 12 % vertical non atteint.
- Comparer le visage, le tatouage, le nombre exact de munitions et les petites attaches au modèle de production.
- Contrôler les franges et les pixels à faible alpha sur fonds clair et sombre avant toute intégration.
- Valider l'échelle et une pose latérale cohérente avec les autres candidats.
- Aucune animation, collision ni intégration moteur réalisée.

### JACK — Gears Tactics

Identifiant : `jack_skin_02`. [PNG](../../assets/costumes_v12/jack_tactics.png) · [Journal](../../data/generation_v12/jack_skin_02_record.json).

- Un seul robot complet : quatre grandes optiques bleues, antenne, plaque supérieure et deux bras/outils distincts.
- Transparence réelle mesurée ; absence du damier de la référence.
- Copie native conservée sans recadrage, redimensionnement ni réencodage.
- Silhouette et composants principaux cohérents avec la capture officielle Tactics ; fidélité microscopique non validée.
- Marge basse étroite : 17 px à alpha >=128 ; toutes les griffes restent dans le cadre.
- De minces franges colorées sont visibles sur certains bords métalliques : contrôle à fond clair et correction future requise avant production.
- Comparer les petits joints, gravures, attaches et asymétries aux captures complètes du jeu Tactics.
- Vérifier contours sur fonds clair/sombre et uniformiser les marges dans une passe autorisée distincte.
- Validation manuelle de l'identité de l'édition et des matériaux ; aucune certification 1:1.
- Aucune animation, collision ni intégration moteur produite.

### JD Fenix — Outsider Gears 4, candidat de concept

Identifiant : `jd_skin_01`. [PNG](../../assets/costumes_v12/jd_skin_01.png) · [Journal](../../data/generation_v12/jd_skin_01_record.json).

- Candidat de concept Outsider, corroboré seulement sur les parties visibles dans des captures de campagne. Le modèle final complet n'est pas validé ; édition à vérifier, fidélité 1:1 non certifiée.
- Les détails des jambes et bottes proviennent principalement du concept de préproduction. Aucune confusion avec les rendus COG Armoured, explicitement exclus.
- Une seule tentative imagegen. PNG natif copié octet pour octet, sans retouche, agrandissement, animation ni spritesheet.
- Un seul jeune JD blond en pied, tourné à droite en trois-quarts ; veste brune, foulard olive, couche grise à capuche, manches sombres, harnais diagonal à lumière bleue, pantalon beige et holster à la cuisse droite présents.
- La capture de campagne corroborait ces éléments du haut du corps ; le visage généré et les finitions du vêtement restent interprétés, sans validation du modèle final.
- Le rendu est surtout frontal de trois-quarts, mains ouvertes et garde peu marquée ; ce n'est pas encore la pose latérale cible.
- RGBA 1024 × 1536, 69,19 % alpha=0, bordure de 8 px entièrement transparente. Les couleurs de fond visibles dans certains aperçus ne prouvent pas un fond opaque.
- Silhouette entière ; marges alpha >=128 [195,93,220,50] px. L'objectif de 10 % de marge verticale n'est pas atteint.
- Comparer le visage, les proportions et les détails du harnais au modèle final de campagne Gears 4.
- Vérifier pantalon, holster, bottes et accessoires sur un rendu final complet ; le concept ne certifie pas leur identité finale.
- Valider ou corriger la pose latérale de combat et la marge verticale ; contrôler les contours dans le moteur.

### Marcus Fenix — E-Day

Identifiant : `marcus_skin_01`. [PNG](../../assets/costumes_v12/marcus_eday.png) · [Journal](../../data/generation_v12/marcus_skin_01_record.json).

- Modèle jeune, bandana, armure à disques pectoraux, manches et protections complètes, deux poches et bottes comparés aux cinq vues du même modèle E-Day.
- Une seule silhouette complète ; sortie native conservée sans recadrage ni réencodage.
- Transparence réelle mesurée ; le maximum alpha de la sortie est 254 et de faibles valeurs alpha persistent autour de certains contours.
- Marges verticales de 68 et 70 px : l'objectif de 12 % n'est pas atteint, mais tête et semelles restent entièrement dans le cadre.
- Pose recomposée et détails fins interprétés : ne vaut pas une certification de fidélité 1:1.
- Comparer le visage, les proportions, les attaches, inscriptions et rayures aux vues de production et aux captures du jeu.
- Vérifier les faibles pixels alpha et les franges sur fonds clair et sombre avant production.
- Définir une pose latérale cohérente avec les autres combattants dans une passe distincte.
- Aucune animation, collision ni intégration moteur réalisée.

### Reine Reyna — Blood Red Queen Reyna

Identifiant : `reyna_blood_red_g5`. [PNG](../../assets/costumes_v12/reyna_blood_red_g5.png) · [Journal](../../data/generation_v12/reyna_blood_red_g5_record.json).

- Candidat statique du skin multijoueur officiel ; aucune nouvelle histoire ou pouvoir canonique présumé.
- Un PNG natif copié sans retouche, extraction raster ni agrandissement.
- Une seule Reyna, face et silhouette tournées à droite en trois-quarts ; peau charbon, fissures rouges, cheveux noirs, cristaux rouges et grandes plaques organiques d'épaules cohérents avec les références visibles.
- Référence primaire de la variante limitée au portrait ; le rendu standard et deux sources secondaires complètent la géométrie du torse.
- Les extrémités inférieures et l'agencement des longs tentacules sont reconstitués ; aucun pied ni corps inférieur canonique complet n'est certifié.
- La géométrie exacte des cristaux, le visage, les fissures et asymétries restent à comparer au modèle de jeu.
- PNG RGBA réel : 56,10 % de pixels alpha=0 ; le halo rouge visible dans certains aperçus est contenu dans des couleurs RGB de pixels alpha=0 aux points sondés, sans fond opaque à ces endroits.
- Marges alpha >=128 : gauche 71, haut 65, droite 68, bas 41 px. Silhouette entière, mais marges cibles de 10 % non atteintes.
- Comparer le bas des tentacules et le corps inférieur au modèle original Gears 5.
- Valider la vue latérale de combat, la topologie des plaques et les détails du visage/skin.
- Vérifier les franges à très faible alpha dans le moteur sur fond clair et sombre.

### Drone de l'Essaim — Gears 5 standard

Identifiant : `swarm_drone_skin_02`. [PNG](../../assets/costumes_v12/swarm_drone_skin_02.png) · [Journal](../../data/generation_v12/swarm_drone_skin_02_record.json).

- PNG candidat statique ; fidélité 1:1 non certifiée. Aucun ajout au lore ni kit de combat déduit.
- La première sortie native est conservée à son emplacement scratch et archivée sans retouche dans rejected_candidates/costumes_v12/swarm_drone_skin_02_mirrored_bandolier.png, avec son journal et SHA-256 ; seule l'édition corrigée est sélectionnée dans assets/costumes_v12.
- Aucune animation, spritesheet, mise à l'échelle, retouche de découpe ou postproduction.
- Un Drone entier tourné vers la droite en trois-quarts, peau épaisse brun-orangé, plaques de métal gris irrégulières, chaînes, pagne frangé et pieds griffus cohérents avec le modèle officiel Gears 5.
- La première sortie inversait le côté anatomique du harnais ; une édition ciblée avec le rendu officiel a remis l'attache haute à l'épaule gauche anatomique et l'attache basse à la hanche droite. Le personnage entier n'a pas été retourné.
- Le modèle officiel est complet en pied ; la pose latérale et les surfaces nouvellement visibles restent une interprétation générative.
- RGBA natif 1199 × 1312, 66,56 % alpha=0. Copie de la sortie finale sans retouche raster.
- Marges alpha >=128 : [236, 104, 247, 49] px ; silhouette complète, mais objectif de 10 % de marge verticale non atteint.
- Vérifier les formes exactes des fragments de casque, épaulières, plaques de jambe et ceinture par rapport au modèle Gears 5.
- Contrôler le nombre et la disposition exacte des modules de harnais et l'asymétrie du corps dans les autres vues.
- Valider la pose principalement de trois-quarts et les contours alpha dans le moteur.

### Drone de l'Essaim — Swarm Elite Drone UIR

Identifiant : `swarm_drone_uir_g5`. [PNG](../../assets/costumes_v12/swarm_drone_uir_g5.png) · [Journal](../../data/generation_v12/swarm_drone_uir_g5_record.json).

- Candidat statique d'une variante multijoueur officielle, sans modification du kit ou de la chronologie canonique présumée.
- PNG natif copié sans traitement raster, agrandissement ou fabrication de spritesheet.
- Un Drone massif entier tourné à droite en trois-quarts ; plaque de casque verte asymétrique, fragment de torse olive, harnais segmenté, voyants orange-rouge et cartouche jaune/noire cohérents avec la capture du skin.
- La référence officielle en pied du rifleman sert au bas du corps, mais ne certifie pas les éventuelles différences UIR des jambes/plaques.
- Les détails de visage, dents, motifs, attaches, chaînes et plaques sont des approximations génératives à valider.
- RGBA réel : 59,96 % alpha=0 ; dimensions natives 1159 × 1357, sans mise à l'échelle.
- Marges alpha >=128 : [150, 73, 177, 45] px ; silhouette entière, mais marges verticales de 10 % non atteintes.
- Comparer les plaques et le pagne du bas du corps à une capture en pied UIR Elite Drone.
- Valider les côtés anatomiques, l'ordre des cartouches et la forme du fragment de casque.
- Vérifier la découpe alpha et le profil de combat dans le moteur.

### Zealot locuste — Collector's Zealot

Identifiant : `zealot_collectors_g5`. [PNG](../../assets/costumes_v12/zealot_collectors_g5.png) · [Journal](../../data/generation_v12/zealot_collectors_g5_record.json).

- Candidat statique d'une variante multijoueur officielle, sans modification du kit ou de la chronologie canonique présumée.
- PNG natif copié sans traitement raster, agrandissement ou fabrication de spritesheet.
- Un Zealot entier, trois-quarts orienté à droite, casque pointu à crête, plaques sombres à bordures métalliques, harnais et composants jaunes cohérents avec le portrait Collector's.
- La silhouette du casque, les lignes rouges et les motifs du harnais sont des approximations génératives à comparer au modèle exact.
- Le rendu officiel standard Gears 5 ne montre pas les chevilles/pieds ; ces éléments et certains détails des tassets ont été reconstitués. Aucun rendu Tactics n'a servi à cette génération.
- RGBA réel : 64,77 % de pixels alpha=0 ; le halo d'aperçu ne doit pas être interprété comme un fond opaque.
- Marges alpha >=128 : [154, 33, 162, 42] px ; corps et pieds entiers, mais marges verticales de 10 % non atteintes.
- Comparer les pieds, le profil de la crête et les tassets au skin Collector's dans Gears 5.
- Valider les teintes exactes des réserves d'Imulsion, les veines et les petits motifs.
- Vérifier la découpe alpha sur fonds clair/sombre dans le moteur.

## Recherches ou essais sans PNG

| Sujet | État constaté | Journal |
|---|---|---|
| Damon Baird — campagne Gears of War 2006 | `blocked_generator_refusal` | [Journal](../../data/generation_v12/baird_skin_02_record.json) |
| Hydra de Skorge | `reference_research_pending` | [Journal](../../data/generation_v12/boss_hydra_skorge_record.json) |
| Riftworm — rencontre environnementale | `reference_research_pending` | [Journal](../../data/generation_v12/boss_riftworm_g2_record.json) |
| Wakaatu | `reference_research_pending` | [Journal](../../data/generation_v12/boss_wakaatu_record.json) |
| Fahz Chutani — Hivebuster Fahz | `blocked_generator_refusal` | [Journal](../../data/generation_v12/fahz_hivebuster_g5_record.json) |
| Kait Diaz — Désert Gears 5 | `blocked_generator_refusal` | [Journal](../../data/generation_v12/kait_skin_03_record.json) |
| Kantus — Gears Tactics | `blocked_generator_refusal` | [Journal](../../data/generation_v12/kantus_skin_02_record.json) |
| Drone locuste — E-Day | `reference_research_pending` | [Journal](../../data/generation_v12/locust_drone_skin_02_record.json) |
| Garde Theron — Gears Tactics | `reference_research_pending` | [Journal](../../data/generation_v12/theron_skin_02_record.json) |

Ces entrées n’augmentent pas le nombre d’images disponibles.

## Révisions V12 conservées hors total actif

- [flock_density_candidate.png](../../rejected_candidates/bosses_v12/flock_density_candidate.png) : Première sortie Flock V12 : Leeches trop grosses et trop alignées pour la masse collective visée ; remplacée par assets/bosses_v12/flock_gears5_swarm.png après révision de densité. Conservée comme révision, hors total actif ; aucune conformité 1:1 certifiée.
- [kraken_framing_candidate.png](../../rejected_candidates/bosses_v12/kraken_framing_candidate.png) : Première sortie Kraken V12 : marges insuffisantes autour de la tête et du manteau ; remplacée par assets/bosses_v12/kraken_gears5_head_mantle.png après correction de cadrage par le générateur. Conservée comme révision, hors total actif ; aucune conformité 1:1 certifiée.
- [swarm_drone_skin_02_mirrored_bandolier.png](../../rejected_candidates/costumes_v12/swarm_drone_skin_02_mirrored_bandolier.png) : Première sortie du Drone de l’Essaim standard Gears 5 V12 : orientation anatomique du harnais inversée ; remplacée par assets/costumes_v12/swarm_drone_skin_02.png après correction par le générateur. Conservée comme révision, hors total actif ; aucune conformité 1:1 certifiée.

## Vérification technique et historique

- Les **148 PNG antérieurs** (136 actifs et 12 archives) conservent leurs SHA-256.
- Les **270 journaux et documents historiques** contrôlés restent identiques.
- Les nouveaux fichiers sont décodés et leurs dimensions, alpha et empreintes figurent dans le manifeste consolidé.
- Aucun fichier sans journal n’est utilisé pour compléter automatiquement une identité du catalogue.
- Les sources, concepts éventuels, parties masquées ou reconstruites et comparaisons restant à effectuer figurent dans les journaux liés.

[État de reprise V12](REPRISE_V12.md) · [Manifeste complet](../../production/asset_manifest.json) · [Galerie](../../Galerie_Personnages.html)
