# Revue indépendante V14 — technique, visuels et sélection

**27 novembre 2026.** Deux revues indépendantes ont contrôlé la provenance, les références, les fichiers, les identités d’édition et les comptes. La correction de coiffure de Reyna est retenue ; les limites de fidélité restent explicites.

Le [rapport de validation finale](VALIDATION_V14.json) et le [journal des tests](INVENTORY_TESTS_V14.txt) portent les résultats d’intégration. Les mentions « à exécuter » de la revue technique décrivent son instant de rédaction, avant ce dernier contrôle.

## Corrections après les constats de revue

- Coiffure Reyna : côté rasé inversé dans le candidat initial, correction ciblée sélectionnée après comparaison au modèle officiel. Les deux sorties antérieures sont archivées.
- Source héritée Reyna : la revue visuelle a repéré le lien Gears 5 Operation 6 dans les sources de couverture. Le catalogue V14 remplace ce champ par la source primaire Gears 4 et remplace aussi le libellé hérité de gameplay identique par une variante humaine distincte. Les anciens catalogues restent inchangés ; aucun pouvoir de Queen Reyna n’est transféré.
- Alias Lahni : le rapport de consolidation explique maintenant le rapprochement de deux appellations sans deuxième costume physique ni PNG supplémentaire.
- Comparatif Ticker : la note de recherche initiale « génération non effectuée » est replacée dans son contexte et complétée par le lien vers la sortie finale E-Day.

## Revue technique indépendante — V14

**Date : 27 novembre 2026.** Revue en lecture seule du dépôt `darknigthmare/gear-of-wars-combats`, avant le dernier recalcul et la validation globale. Aucun fichier source, journal ou PNG du dépôt n’a été modifié par cette revue.

### Conclusion

Aucun défaut technique bloquant identifié dans les éléments examinés. La sélection finale de Reyna pointe vers la correction ciblée de coiffure. Les deux sorties précédentes sont archivées et ne figurent plus parmi les références actives. Les décomptes, la galerie, la bible et les chaînes de provenance étaient cohérents au moment de cette revue.

**La reprise complète des 27 tests et le validateur final restent à exécuter par le responsable d’intégration.** Cette revue ne présente pas ces contrôles futurs comme déjà réussis. Les tests n’ont pas été relancés ici pour éviter une exécution concurrente redondante.

### Comptes recoupés

| Élément | Résultat |
| --- | ---: |
| PNG actifs | 159 |
| Empreintes SHA-256 actives uniques | 159 |
| Révisions archivées | 17 |
| Entrées de catalogue | 219 |
| Entrées sans référence attribuée | 34 |
| Personnages avec référence | 51 / 57 |
| Costumes avec référence | 65 / 85 |
| Boss, créatures et machines avec référence | 30 / 34 |
| Stages avec master | 34 / 34 |
| Projectiles avec référence | 5 / 9 |
| Alias de référence résolu | 1 |
| Certifications de fidélité 1:1 | 0 |
| Ensembles d’animations finalisés | 0 |

Les 35 entrées sans référence en V13 sont tracées dans l’audit V14. Deux sont résolues par attribution : Reyna par un nouveau candidat et Lahni par un alias documenté. Cinq identités sont ajoutées au catalogue, dont quatre illustrées. Le résultat est bien `35 − 2 + 1 = 34` entrées encore sans référence.

Le journal de la passe indique huit appels au générateur : cinq générations de nouveaux sujets réussies, deux éditions réussies de Reyna et un refus unique pour Mina Jinn. L’alias Lahni ne correspond à aucun appel. Le journal courant Reyna compte trois appels ; ses journaux de révision ne doivent pas être additionnés une seconde fois.

### Fichiers PNG et provenance

Les sept nouveaux PNG ont été relus et leurs tailles, SHA-256 et identifiants de blob Git comparés aux blobs créés pendant la récupération. Tous concordent :

- Cinq fichiers actifs : coiffure Reyna corrigée, Canker G4, Leech G5, Wretch E-Day et Ticker E-Day.
- Deux fichiers archivés : Reyna initiale et premier essai de nettoyage.
- Reyna sélectionnée : `assets/costumes_v14/reyna_human_g4_hairfix.png`, SHA-256 `2f286efc3e8da89109c2008f86c5a5fb3222cb2fcbff8c6726ade2e60b90cff1`.
- Reyna initiale : `rejected_candidates/costumes_v14/reyna_human_g4_initial.png`, SHA-256 `21adc45fa2889c4dd72e6959e0f97653eb83b5c471ff7514b52ac40569da6715`.
- Nettoyage non sélectionné : `rejected_candidates/costumes_v14/reyna_human_g4_clean.png`, SHA-256 `9a556bfb42c72d72d37c40276791bf784339b8fb1793c0b0f1949354b8c1fa99`.

Les chemins actifs correspondent aux journaux courants. Les réserves concernant détails génératifs, cadrage, profils et alpha restent explicites. L’ensemble des actifs du manifeste conserve `canonical_fidelity_validated=false` et `production_ready=false`. Cette revue technique ne constitue pas une certification visuelle 1:1.

### Alias Lahni

Les deux entrées ont le même parent `lahni` et la même édition exacte `Gears 5: Hivebusters`. L’alias `lahni_hivebusters_intro` et le costume canonique `lahni_skin_01` sélectionnent le même identifiant physique et le même PNG V13.

Les empreintes enregistrées dans `reference_resolution` concordent avec les quatre fichiers réellement présents : mapping, provenance V13, preuve V14 et PNG. La preuve décrit le rapprochement comme une inférence fondée sur le concept intro de Tyler Bradley et le modèle final publié par Aryan Hanbeck. Le modèle final à manches courtes a priorité ; la tenue Escape reste distincte.

Le code vérifie explicitement identité, édition, candidat sélectionné, propriété de l’actif, chemin, octets et provenance. Il rejette duplications d’alias, chaînes et cycles avant toute modification de couverture. Il ne copie ni les états de qualité ni le dernier journal propre à l’alias, et ne duplique aucun actif physique.

Les onze tests ciblés d’alias ont été exécutés avec succès avant l’intégration finale. Le fichier original de tests a survécu à l’indisponibilité temporaire ; il n’a pas été remplacé par la reconstruction provisoire préparée en cache. Les changements postérieurs du consolidator portent aussi sur l’explication et le compteur d’alias dans le rapport ; la suite globale de 27 tests doit donc être reprise sur les sources finales.

### Inventaires, galerie et bible

Les contrôles de lecture ont établi :

1. Égalité des compteurs de `production/coverage.json` et `production/asset_manifest.json`.
2. Égalité du contenu intégré dans `Galerie_Personnages.html` avec la couverture, les actifs et les archives des JSON courants.
3. Présence du lien vers la Bible V14 dans la galerie.
4. Concordance de l’empreinte du fichier Bible avec `BIBLE_BUILD_V14.json`.
5. Concordance de tous les fichiers d’entrée déclarés par ce manifeste avec leurs empreintes.
6. Présence des sept chapitres, des trois guides originaux, des 68 rubriques et des 40 cas d’acceptation sans affirmation d’implémentation moteur.

Un contrôle des chemins locaux dans les documents modifiés et la galerie a parcouru 789 occurrences de liens, template compris. Les liens du template doivent être résolus depuis la racine où la galerie est rendue. Les seuls documents encore attendus à l’instant du contrôle étaient `docs/production/REVIEW_V14.md` et `docs/production/VALIDATION_V14.json`, annoncés par le responsable d’intégration. Ils doivent exister avant le commit final.

Les anciens guides, journaux V1–V13, PNG historiques et livrables binaires ne figurent pas parmi les changements du dépôt. Les refus antérieurs restent conservés ; aucune réutilisation sous un autre nom ne les remplace.

### Recherche des anciens manquants

La revue des sept cibles `theron_skin_02`, `tai_skin_02`, `gabe_skin_02`, `deebee_skin_02`, `grenadier_skin_02`, `anthony_black_steel_g5` et `projectile_boomshot_shell_g4` est conservée dans `docs/references/remaining_identity_review_v14.json`.

Aucune référence finale complète supplémentaire n’a été établie pour ces sept entrées. Anthony Black Steel reste correctement rattaché à Gears 5. Les limitations d’accès et de cadrage sont documentées ; aucun concept ni aucune autre édition n’a été substitué. Ce constat ciblé ne prétend pas épuiser toute la franchise.

### Publication

La branche distante a été vérifiée sur `b13c29a549d5768deec51191bb43a12ece41e812`, arbre `2b78f938151d50901cdc304ee8404ba8c958e6ad`. Les sept blobs PNG nécessaires sont déjà disponibles dans GitHub.

La publication doit lire exclusivement le futur commit immuable validé, réutiliser uniquement les blobs dont le SHA correspond exactement, vérifier l’égalité de l’arbre Git construit avec l’arbre local, puis déplacer la branche sans force et avec contrôle du parent attendu. Aucun changement de ref ni commit distant V14 n’a été effectué pendant cette revue.


## Revue finale visuelle et documentaire — V14

**Date : 27 novembre 2026.** Périmètre : cinq candidats actifs V14, deux versions Reyna archivées et alias Lahni. Dépôt examiné : `/workspace/scratch/3c791759fb15/gear-of-wars-combats`.

### Conclusion

Les cinq PNG peuvent être publiés comme **références candidates en attente de validation**. Aucun ne peut être présenté comme une reproduction 1:1 certifiée, une animation achevée ou un élément déjà intégré au gameplay.

La revue a identifié une inversion du côté rasé de Reyna dans le premier PNG. Une unique édition ciblée, autorisée pendant la revue, a rétabli les cheveux sur la tempe droite anatomique visible. Après comparaison au modèle officiel, le candidat `reyna_human_g4_hairfix.png` est recommandé et a été sélectionné par root. Aucune régression canonique précise justifiant de conserver le rasage inversé n'a été identifiée. Le visage, les tatouages, les motifs textiles et plusieurs accessoires restent néanmoins des interprétations génératives.

Le dernier état des données et des fichiers a été relu après cette sélection :

| Contrôle | Résultat vérifié |
|---|---:|
| PNG actifs présents | 159 |
| SHA256 distincts parmi les PNG actifs | 159 |
| PNG archivés | 17 |
| Entrées de catalogue | 219 |
| Entrées encore sans référence | 34 |
| Nouveaux PNG actifs V14 | 5 |
| Aliases de référence de costume | 1 |
| Fidélités canoniques validées | 0 |
| Ensembles d'animations achevés | 0 |

Les cinq empreintes PNG correspondent aux journaux finaux. Le manifeste compte exactement 159 entrées. L'alias Lahni ne crée aucun fichier supplémentaire. Le passage de 16 à 17 archives provient de la conservation de l'original Reyna après sélection de la correction coiffure.

### Méthode et limites de cette revue

Les images natives ont été ouvertes, ainsi que leurs références locales complètes. Les textes des portfolios conservés localement ont été lus pour contrôler l'édition et les crédits. Les SHA256 des huit références V14 documentées correspondent aux journaux ; ceux des trois références Lahni correspondent aussi au journal V13.

Les dimensions, le canal alpha, les marges, les empreintes et la correspondance avec les sorties natives ont été recalculés en lecture seule. Aucun recadrage, remplissage, redimensionnement ou nettoyage logiciel des PNG n'a été appliqué. La seule nouvelle image produite pendant la revue est l'édition native ciblée de la coiffure de Reyna.

Aucune consultation de navigateur ni nouvelle recherche web n'a été effectuée. Les liens ci-dessous désignent les sources primaires déjà téléchargées ; cette revue ne prétend pas avoir revérifié leur disponibilité en ligne. Il n'y a pas de modèle 3D officiel chargé, de comparaison orthographique exhaustive ni d'essai dans le moteur. Les différences de pose et de lumière limitent les comparaisons de proportions et de matériaux.

### 1. Reyna humaine Outsider — Gears of War 4

**Fichier actif :** `assets/costumes_v14/reyna_human_g4_hairfix.png`
**Journal actif :** `data/generation_v14/reyna_skin_02_record.json`

La planche finale montre trois vues complètes de Reyna Diaz Outsider. Le corps est crédité à Heber Alvarado et la tête à Michelle Zhang. La référence est bien celle de **Gears of War 4**. Le libellé ancien « version humaine future » est explicitement résolu dans l'annexe V14 ; aucune nouvelle forme future canonique n'est revendiquée.

Sources : [publication de l'équipe Gears of War 4](https://www.zbrushcentral.com/t/gears-of-war-4-art-dump/206321), [image exacte du modèle](https://www.zbrushcentral.com/uploads/default/original/3X/3/3/33ce37a0270d862ad45ef6131e76f2b24e56380f.jpeg), [portfolio de Heber Alvarado](https://heber.artstation.com/projects/LxX6v).

#### Écart identifié et correction

Sur la vue frontale officielle, le côté rasé est le **gauche anatomique** ; la natte retombe sur l'épaule **droite anatomique**. L'original généré montrait un rasage sur le côté droit visible malgré une natte et un tatouage correctement placés. L'édition coiffure remplit cette tempe visible de cheveux bruns. Le côté gauche éloigné reste essentiellement caché : sa forme exacte ne peut pas être contrôlée dans cette seule pose.

Le nouveau candidat conserve la natte droite, le tatouage gauche, le haut écru et olive asymétrique, les sangles, le collier, les ceintures, les gants, le couteau et les bottes. Ces invariants correspondent globalement à la planche finale. Le générateur a également repeint des motifs, des coutures et certaines nuances du visage ; il ne s'agit pas d'une modification strictement limitée aux pixels du cuir chevelu. Cette différence de pixels ne constitue pas, à elle seule, la preuve d'une régression canonique. La comparaison au modèle officiel motive la sélection du candidat corrigé.

#### Réserves maintenues

- Visage, dessin exact du tatouage, arabesques textiles, bijoux, attaches et détails de lame non certifiés identiques.
- Vue principalement frontale/trois-quarts, sans profil orthographique de combat validé.
- Marges utiles très faibles en hauteur : 26 px en haut et 10 px en bas au seuil alpha > 8.
- Faibles alpha périphériques et alpha maximal 254 conservés dans la sortie native.
- Le catalogue conserve le parent technique `reyna`, mais le journal porte `requires_distinct_gameplay_variant: true`. L'annexe impose explicitement un gameplay humain distinct et n'attribue pas les pouvoirs de la Reine de l'Essaim à cette image.

Un lien hérité vers le bundle Operation 6 de Gears 5 apparaît encore dans les sources de couverture du costume. Il ne doit pas servir de preuve visuelle de la tenue humaine Gears 4 ; la cible et les références effectivement utilisées sont, elles, explicitement Gears 4.

### 2. Canker / Carrier Minion — Gears of War 4

**Fichier :** `assets/projectiles_v14/canker_g4.png`
**Journal :** `data/generation_v14/projectile_canker_g4_record.json`

La planche officielle est titrée Carrier Minion et créditée à Daniel Bohrer. Le PNG retient un seul sujet horizontal, avec le sac globulaire à droite et les appendices allongés vers la gauche. Les lobes brun rouge, l'enveloppe translucide veinée et le noyau lumineux sont reconnaissables. Aucun membre ou équipement supplémentaire n'a été ajouté.

Sources : [publication de l'équipe Gears of War 4](https://www.zbrushcentral.com/t/gears-of-war-4-art-dump/206321), [image exacte Carrier Minion](https://www.zbrushcentral.com/uploads/default/original/3X/5/3/534d1585fd40bdef40e31586b71ef08c82a7ad98.png). Le rapprochement avec l'appellation Canker est documenté par root à partir du [guide officiel Prima, section Swarm](https://primagames.com/eguides/gears-of-war-4-eguide/enemy-forces/swarm) ; cette page n'a pas été rouverte pendant la revue.

La silhouette utile est entièrement contenue. Les marges horizontales sont insuffisantes pour les 8 % demandés. Les formes précises des lobes, les nervures et les appendices ont été interprétées ; la luminosité intérieure est plus accentuée. Le classement en projectile évite de créer une seconde entrée visuelle d'ennemi pour le même PNG. Aucun effet d'explosion, feu au sol ou mouvement n'est livré.

### 3. Leech individuel — Gears 5

**Fichier :** `assets/creatures_v14/leech_g5.png`
**Journal :** `data/generation_v14/creature_leech_g5_record.json`

Les deux planches en couleur montrent le modèle final de Gears 5 en postures déployées. Le texte du portfolio local crédite Bruno Melo pour la sculpture, Can Etişkol pour le maillage de jeu et les textures, et Aryan Hanbeck pour la direction artistique.

Sources : [portfolio de Bruno Melo](https://bmelo.net/projects/2xzmJB), [publication ArtStation](https://www.artstation.com/artwork/2xzmJB).

Le PNG possède un seul corps complet, un manteau bordeaux texturé, une bouche plissée, une bordure d'épines et les appendices arrière regroupés. La bouche est plus ouverte que dans la vue supérieure horizontale de référence ; l'autre vue source documente cette anatomie ouverte. La surface dorsale demeure visible : la projection n'est pas un profil orthographique strict.

Les dents et les épines ne sont pas contrôlées une à une. Les marges latérales restent d'environ 3 à 4 %, malgré une marge généreuse demandée. Un résidu alpha 1 atteint le bord gauche ; le contour utile reste contenu. Leech individuel et Flock collectif sont clairement séparés dans les données et le chapitre V14.

### 4. Wretch — Gears of War: E-Day

**Fichier :** `assets/creatures_v14/wretch_eday.png`
**Journal :** `data/generation_v14/creature_wretch_eday_record.json`

L'édition est vérifiée par le titre du portfolio local, le texte de l'artiste et les logos imprimés sur les deux planches. Il s'agit de **Gears of War: E-Day**. Les crédits indiquent une contribution partielle d'Antoine Verney-Carron à la sculpture et son travail de texturage. La source en pied et le gros plan ont été inspectés ; aucune planche Tactics ne leur est substituée.

Source : [Antoine Verney-Carron — Gears of War: E-Day](https://antoineverneycarron.artstation.com/projects/KR3KG4), images `wr01` et `wr02`.

Le candidat conserve les longs avant-bras, les grandes mains, les pieds griffus, les bourrelets du front, l'œil pâle, les dents fines et la peau gris beige piquetée. Le corps est entier et la posture est plus penchée en avant que la référence. L'absence de vue arrière impose une extrapolation des reliefs et épines dorsales. Le détail des doigts, pores, dents et petites épines n'est pas certifié.

La vue est trois-quarts vers la droite ; le journal le reconnaît explicitement. Les marges sont les plus confortables des cinq candidats, mais la silhouette occupe environ 80 % de la hauteur, au-delà des 72 % visés par le prompt. Le bord inférieur ne porte que des résidus alpha 1 hors silhouette utile. Le regroupement dans les rencontres/boss de production ne transforme pas le Wretch en boss géant.

### 5. Ticker organique — Gears of War: E-Day

**Fichier :** `assets/creatures_v14/ticker_eday.png`
**Journal :** `data/generation_v14/creature_ticker_eday_record.json`

La même page primaire nomme les travaux E-Day et légende la planche « Ticker/Reaver: texturing ». La partie inférieure contient le Ticker entier ; la partie supérieure représente le Reaver. Le PNG reprend exclusivement la créature inférieure.

Sources : [portfolio E-Day](https://antoineverneycarron.artstation.com/projects/KR3KG4), [planche exacte](https://cdna.artstation.com/p/assets/images/images/103/353/664/large/antoine-verney-carron-tc.jpg?1792435473).

La tête en coin, le dos segmenté, les plis du cou, les épaules poreuses et les longs membres antérieurs restent cohérents. La patte arrière éloignée est partiellement occultée comme dans la référence ; il manque une vue indépendante de l'arrière pour contrôler toute son anatomie.

Aucun Reaver, tentacule, harnais, bombe ou équipement ne figure dans le PNG. L'entrée est explicitement E-Day et n'est pas présentée comme le modèle Tactics. Les proportions exactes, les dents, les pores et les épines restent à contrôler. Les marges demandées ne sont pas atteintes et des pixels alpha 1 touchent les bords supérieur et gauche.

### 6. Mesures de transparence et de cadrage

Les nombres ci-dessous proviennent des PNG natifs. La « silhouette utile » est définie ici par **alpha > 8** ; ce seuil sert à distinguer les pixels presque transparents du contour principal et ne constitue pas un nettoyage du fichier. Ordre des marges : gauche / haut / droite / bas.

| Image | Dimensions natives | Alpha min–max | Marges utiles en pixels | Réserve principale |
|---|---:|---:|---|---|
| Reyna coiffure corrigée, active | 1024 × 1536 | 0–254 | 76 / 26 / 144 / 10 | Marges verticales très faibles |
| Canker | 1877 × 838 | 0–255 | 63 / 128 / 49 / 83 | Marges latérales étroites |
| Leech | 2172 × 724 | 0–255 | 80 / 101 / 69 / 78 | Marges latérales étroites |
| Wretch E-Day | 1024 × 1536 | 0–254 | 112 / 197 / 124 / 114 | Trois-quarts et détails dorsaux extrapolés |
| Ticker E-Day | 1774 × 887 | 0–255 | 113 / 52 / 112 / 35 | Toutes les marges sous 8 % |
| Reyna initiale, archivée | 1024 × 1536 | 0–254 | 78 / 26 / 145 / 11 | Côté rasé inversé |
| Reyna nettoyage, archivée | 1024 × 1536 | 0–254 | 75 / 32 / 144 / 10 | Gain de marge insuffisant, coiffure toujours erronée |
| Lahni V13 réutilisée | 1024 × 1536 | 0–254 | 245 / 17 / 233 / 31 | Marges verticales insuffisantes |

Les dimensions doivent être annoncées telles quelles. Ces fichiers ne sont pas des sorties UHD 4K ; aucune mise à l'échelle n'a été effectuée.

#### RGB invisibles et alpha réellement présent

L'aperçu de certaines images montre un halo brun prononcé. Il ne faut pas le décrire automatiquement comme un fond opaque : les valeurs RGB existent même sous alpha nul. Les six points périphériques contrôlés sur les trois versions de Reyna ont tous **alpha = 0** ; leur couleur stockée disparaît en composition alpha correcte.

De vrais faibles alpha subsistent. Dans le hairfix, 21 582 pixels sont compris entre alpha 1 et 8 et 6 845 entre alpha 9 et 127. Le bord inférieur atteint alpha 1 ; les autres bords sont à 0. Dans l'original, les valeurs étaient respectivement 25 974 et 7 007. Ces mesures ne certifient pas à elles seules un détourage parfait. Un contrôle de rendu dans le moteur reste nécessaire.

### 7. Historique Reyna et décision de sélection

| Version | Destination finale | Décision |
|---|---|---|
| Initiale | `rejected_candidates/costumes_v14/reyna_human_g4_initial.png` | Conservée pour traçabilité ; côté rasé inversé |
| Nettoyage alpha/marges | `rejected_candidates/costumes_v14/reyna_human_g4_clean.png` | Écartée ; marges insuffisantes et détails repeints |
| Correction coiffure | `assets/costumes_v14/reyna_human_g4_hairfix.png` | Sélectionnée comme candidate, réserves maintenues |

Les trois journaux de révision sont sous `docs/production/revisions_v14/`. Seul le journal actif `data/generation_v14/reyna_skin_02_record.json` alimente le catalogue. La correction coiffure utilise l'original comme cible et la planche officielle comme référence d'invariance ; elle ne reprend pas l'édition de nettoyage.

Le nouvel actif a le SHA256 `2f286efc3e8da89109c2008f86c5a5fb3222cb2fcbff8c6726ade2e60b90cff1`. Son blob GitHub `60af638847c9f9c6f946c63a36e79b6c9a42fc7e` correspond exactement au SHA Git recalculé sur le fichier local. La revue n'a créé aucun commit ni modifié de référence Git.

### 8. Alias Lahni : une référence partagée, aucun doublon de PNG

**Alias :** `lahni_hivebusters_intro` → `lahni_skin_01`
**Fichier partagé :** `assets/costumes_v13/lahni_skin_01.png`
**Mapping :** `data/costume_reference_aliases_v14.json`

La page locale de Tyler Bradley décrit explicitement les tenues d'introduction de Keegan et Lahni pour le DLC Hivebusters. Le rapprochement entre ce concept et le modèle final publié par Aryan Hanbeck est documenté comme une inférence de catalogue. La comparaison visuelle montre les mêmes familles de plastron à deux disques, épaulières, bandeau, dreadlocks, manchettes asymétriques, poches, canisters, genouillères et bottes.

Sources : [concept de Tyler Bradley](https://tylerthebradley.artstation.com/projects/ykrQgn), [modèle final Hivebusters de Hanbeck](https://mediumrare.artstation.com/projects/oAdmNw), [modèle final Escape utilisé pour la distinction](https://mediumrare.artstation.com/projects/GXKLDB).

Le modèle final a des manches courtes sombres, contrairement aux hauts de bras nus du concept. Le PNG V13 reproduit cette structure finale. La tenue Escape, avec son gilet olive sans manches, ses jambes partiellement découvertes et ses bottes plus courtes, est visuellement distincte et n'est pas liée à cet alias.

La couverture pointe les deux IDs vers le même chemin et le même actif. Le manifeste ne contient qu'une entrée pour ce PNG, dont le SHA256 est `1e9359c427ca81256b92aa011e6b838b7e44889ae55309ec38c0ac48527e11f4`. Le journal d'alias indique zéro tentative et aucun fichier propre. Les deux références de catalogue ne doivent donc pas être annoncées comme deux nouvelles images.

Les réserves V13 restent valables : visage, tatouages, glyphes, cuirs et attaches non certifiés ; vue trois-quarts ; marges verticales trop faibles. Le rapprochement documentaire ne valide pas rétroactivement ces microdétails.

### 9. Refus, comptage des tentatives et honnêteté documentaire

Mina Jinn reste sans PNG, avec un seul refus enregistré, zéro réessai et le statut `blocked_generator_refusal`. Les cinq cibles actives V14 ne reprennent aucun des sujets refusés dans les anciens journaux. Aucun fichier des générations antérieures à V14 n'apparaît modifié par rapport au commit de référence `b13c29a549d5768deec51191bb43a12ece41e812`.

Le total de cette passe est de **huit appels au générateur** : cinq générations initiales réussies, une génération Jinn refusée, une édition Reyna de nettoyage et une édition Reyna de coiffure. L'alias Lahni n'est pas un appel supplémentaire. Les deux éditions concernent un succès antérieur et ne relancent aucun sujet refusé.

Dans les sept journaux actifs V14, les drapeaux `canonical_fidelity_validated`, `fidelity_1to1_certified`, `production_ready` et `animation` sont tous faux. Le chapitre `CAST_AND_CREATURES_V14.md` sépare correctement les références de production, les propositions de gameplay et les fonctionnalités effectivement implémentées.

### 10. Éléments encore hors validation

La publication de ces références candidates est cohérente avec l'état des preuves. Il reste à contrôler les détails fins, les marges et le rendu alpha dans l'application avant une utilisation de production. La vue arrière, le profil strict et les systèmes de combat n'ont pas été livrés par cette passe. Les 34 entrées sans référence demeurent explicitement manquantes.

Cette revue ne valide pas les modifications de LISTING, REPRISE, README ou de la Bible qui pourraient intervenir après son écriture. Les comptages, les sélections d'assets et les journaux cités ont été contrôlés après intégration du hairfix par root.
