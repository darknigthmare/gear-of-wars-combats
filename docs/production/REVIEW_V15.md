# Revue V15 — sélection visuelle et contrôle indépendant

**27 novembre 2026.** Cette revue rassemble les observations de sélection et deux contrôles indépendants. La validation finale exécutée et ses résultats sont consignés dans [VALIDATION_V15.json](VALIDATION_V15.json) ; le rapport technique ci-dessous décrit son propre périmètre au moment de la revue.

Les candidats restent statiques, sans fidélité 1:1 certifiée ni préparation à la production validée.

---

## Revue visuelle de sélection

Les cinq PNG actifs ont été comparés visuellement aux références locales déclarées dans leurs journaux. Les sorties natives sont conservées ; aucune retouche de pixels ni mise en animation n’a été réalisée. Cette revue sélectionne des références provisoires et ne certifie aucune fidélité 1:1.

| Candidat | Éléments observés | Limites maintenues |
| --- | --- | --- |
| Keegan — Onyx Guard, introduction Hivebusters | Tête rasée, moustache/favoris, menton dégagé, plaques carbone, disques pectoraux à centres triangulaires, cartouches sur épaule droite et holster sur cuisse droite cohérents avec le modèle final Bobylev. | Visage et détails fins reconstruits ; pose de trois quarts ; marges haute/basse réduites. L’alias intro désigne la même tenue par comparaison du concept Bradley avec le modèle final. |
| Skorge — Gears 5 Opération 5 | Casque segmenté, cordons, visage étroit, torse découvert, armure bronze/rouge-brun, deux mains et pied avant repris de la pose aérienne officielle. | Pied arrière occulté comme dans la source, éclairage promotionnel, détails fins approximatifs et marges très faibles. La source ne prouve pas toute l’anatomie cachée. |
| Anthony Carmine | Casque fermé à optiques bleues, armure bleue à deux disques, emplacement des sacoches et silhouette générale cohérents avec la figurine NECA photographiée. | Figurine sous licence et non modèle final du jeu de 2006. Proportions, articulations reconstruites et détails des matières non certifiés. Le candidat ne doit pas devenir une preuve exacte de l’édition 2006. |
| Jace Stratton — Gears 3 | Cornrows, barbe courte, col, plastron gris à deux disques, manches retroussées et avant-bras visibles cohérents avec le portrait promotionnel. | Visage, dessins des petites plaques et signes reconstruits ; jambes, poches, genoux et bottes extrapolés depuis une référence aux hanches. Cadrage vertical très serré. |
| Minh Young Kim — RAAM’s Shadow | Tête rasée, col haut, plastron bleu à deux disques, sangles et double ceinture cohérents avec la capture du DLC. | Visage, insigne et matières reconstruits ; partie inférieure absente de la source et extrapolée. Marges inférieures à celles demandées. |

### Rejet visuel Theron

Le PNG Theron issu du nouvel essai possède un casque ouvert à haute crête et des plaques d’armure interprétées. Ces éléments divergent de la cible standard. L’absence d’une référence finale complète prouvée pour 2006 empêche aussi sa validation d’édition. Le fichier est conservé dans `rejected_candidates/costumes_v15/`, sans chemin actif, sans rattachement de couverture et sans réduction des manquants.

Une photo de figurine NECA a été consultée après la génération pour contrôler la silhouette du casque. Cette source de revue n’a pas été donnée au générateur et ne constitue pas une preuve du modèle final 2006. La recherche d’un ancien rendu Epic a trouvé un lien de document, mais son image était indisponible ; les reconstructions de fans présentes sur la même page ne sont pas utilisées comme preuves canoniques.

### Transparence et cadrage

Les mesures d’alpha, les dimensions, les marges et les empreintes sont reportées dans les journaux et le rapport de validation. Un canal alpha réel ne signifie pas que le détourage est prêt pour la production : des résidus de très faible alpha subsistent, et les marges demandées ne sont pas toutes respectées. Aucun fond, aucune marge et aucun contour n’ont été corrigés après génération.

---

## Revue indépendante V15 — costumes

Date : 27 novembre 2026. Revue par l’agent `costume_references`, sur les fichiers présents dans le dépôt. Aucune modification des images, du catalogue ou des journaux de Keegan et du Theron.

### Décisions

| Entrée | Conclusion indépendante | Limite principale |
|---|---|---|
| `keegan_skin_02` | Candidat utilisable comme référence en attente de validation. La structure de la tenue Onyx Guard correspond au modèle final fourni par Alex Bobylev. | Visage et petits détails interprétés ; pose presque frontale et marges verticales serrées. Aucune fidélité 1:1 certifiée. |
| `keegan_hivebusters_intro` | Alias documentaire justifié vers `keegan_skin_02`. | Le rapprochement des appellations s’appuie sur le modèle final et le concept explicitement décrit comme tenue d’introduction. Il ne transforme pas le PNG généré en modèle canonique validé. |
| `theron_skin_01` | Rejet visuel et archivage confirmés. Cette image ne résout pas le costume 2006. | Casque ouvert et fortement crêté, silhouette du col, plastron et jupe non conformes au repère contrôlé. Référence finale 2006 toujours insuffisante. |

### Keegan Onyx Guard

Images réellement inspectées : `assets/costumes_v15/keegan_skin_02.png`, la planche finale face/dos `onyx_keegan_full_pair.jpg` et le concept d’introduction `keegan_intro_concept.jpg`. Les deux pages des artistes ont été relues pendant cette passe.

[Alex Bobylev — Keegan, Onyx Guard](https://alexbobylev.artstation.com/projects/Vg3qGR) décrit sa contribution au modèle cinématique temps réel final, aux textures et aux matériaux du DLC. Ce texte et la planche en pied constituent la preuve principale de la tenue. [Tyler Bradley — Hivebusters Keegan and Lahni](https://tylerthebradley.artstation.com/projects/ykrQgn) nomme explicitement les tenues d’introduction ; son image est un concept de production, utilisé pour rapprocher les deux appellations, pas pour remplacer les détails du modèle final.

Le candidat conserve les éléments distinctifs observables : crâne chauve, favoris et moustache épaisse avec menton central dégagé ; armure carbone noire/grise ; col haut ; grands disques pectoraux munis de petites marques triangulaires jaunes ; éclairages bleus sur le torse, les épaules et l’avant-bras ; cartouches à l’épaule anatomique droite ; holster à la cuisse droite ; protections longues des tibias. Il n’y a pas d’inversion globale des asymétries. Les mains sont vides et aucun accessoire majeur étranger n’a été ajouté.

Le visage est plus frontal et son rendu plus photographique que sur la planche finale. La forme des lèvres, l’épaisseur des favoris, les rides et la granularité de la peau ne sont pas une correspondance démontrée au modèle. Les coutures, attaches, petits reliefs de l’armure, usures et textures sont également interprétés. Je ne constate pas, dans les grandes pièces de la tenue, d’erreur d’identité assez nette pour rejeter l’ensemble ; ce constat ne vaut pas validation canonique du visage ou des microdétails.

La pose est essentiellement frontale avec une légère rotation vers la droite. Elle ne fournit pas un profil de combat strict. Un seul personnage entier est présent, chaussures comprises, sans texte ni panneau.

#### Alpha et cadrage mesurés

Le PNG est natif, 1024 × 1536, RGBA, 2 205 399 octets. SHA256 : `c07bb1a98955c0147ffb2d89cbbe185ffe8a9d1268b9eb73f197e2bfee52be62`.

L’alpha varie de 0 à 254. La boîte des pixels d’alpha supérieur à 8 est `[177, 30, 853, 1510]` ; celle d’alpha supérieur à 128 est `[178, 31, 852, 1509]` (bornes droites et basses exclusives). Les marges utiles sont donc d’environ 177 pixels à gauche, 171 à droite, 30 en haut et 26 en bas. Les 10 % de marge demandés ne sont pas atteints verticalement.

59,68 % des pixels ont un alpha nul ; 1,70 % ont un alpha de 1 à 8 ; 0,424 % ont un alpha de 9 à 127. Le large halo gris/brun visible dans l’aperçu brut ne doit pas être décrit comme un fond opaque : les échantillons `(100, 200)`, `(100, 500)`, `(900, 800)` et `(500, 15)` ont tous un alpha nul, malgré des composantes RGB parfois claires. Il reste des pixels de faible alpha en périphérie ; leur effet éventuel en composition et filtrage d’atlas reste un contrôle de production distinct. Aucun nettoyage raster n’a été effectué.

### Alias Keegan introduction Hivebusters

Le concept Bradley et la planche finale Bobylev partagent le col haut, les disques à triangles jaunes, les cartouches sur l’épaule droite, le holster droit et la protection des tibias. La relation entre « intro » et « Onyx Guard » est donc appuyée à la fois par le texte et par les formes de la tenue.

Le journal de l’alias expose `generation_attempt_count: 0`, `has_image: false`, `asset_path: null`, `reference_alias_of: keegan_skin_02` et le chemin partagé `assets/costumes_v15/keegan_skin_02.png`. Son hash de référence correspond au PNG inspecté. Cette entrée ne doit pas compter comme une seconde génération ni comme un deuxième PNG actif. Toutes les réserves de la référence partagée s’appliquent à l’alias ; `canonical_fidelity_validated` et `production_ready` restent faux.

### Theron 2006 archivé

Images inspectées : `rejected_candidates/costumes_v15/theron_skin_01.png` et la [photographie de figurine NECA publiée en 2008](https://toynewsi.com/139-13381), déjà utilisée par root pour le contrôle après génération. La figurine licenciée n’est pas une preuve suffisante du maillage final de jeu 2006 ; elle reste néanmoins un repère visuel explicite qui contredit nettement la sortie.

Le candidat expose les yeux sous un casque ouvert à haute crête. Le repère présente un casque fermé à fentes et une grande collerette rouge. Le candidat modifie aussi la structure du plastron, les plaques d’épaules et la découpe de la jupe. Ces écarts portent sur des formes de premier ordre, pas seulement sur la texture. Le maintien en archive est justifié. Aucune nouvelle tentative Theron n’a été effectuée par cette revue.

Le PNG est 1024 × 1536 RGBA, 2 297 876 octets, SHA256 `97b7d40b861501177ab6c7da3dc37b247f933722d86ea4eab471e2ea9e1ea2bd`. La boîte d’alpha supérieur à 8 est `[135, 0, 807, 1528]`, et celle d’alpha supérieur à 128 `[136, 6, 806, 1526]`. Le cadrage atteint donc presque le bord supérieur et laisse très peu de marge en bas. L’alpha est réel, de 0 à 254 ; plusieurs échantillons du halo brut ont un alpha nul. Cette transparence technique ne compense pas les erreurs de costume.

Le journal indique correctement une image produite mais écartée : `has_image: true`, `asset_path: null`, `archive_path` renseigné, `is_active_reference: false`. Le costume ne doit pas être déclaré couvert par ce PNG.

### Cinq nouvelles tentatives attribuées à cette passe

`dom_skin_03`, `baird_skin_02`, `cole_skin_01`, `kait_skin_03` et `fahz_hivebuster_g5` ont chacun fait l’objet d’un seul nouvel appel, autorisé par la demande utilisateur de réessayer les refusés. Les cinq ont été refusés au stade de sortie avec `moderation_blocked`, catégorie `other`, HTTP 400. Aucun PNG n’a été renvoyé. Les noms et les prompts précédents ont été conservés sans reformulation pour contourner la décision. Les anciens journaux restent intacts et les nouveaux journaux conservent les deux événements séparément.

Les champs `has_image: false`, `asset_path: null`, `output: null`, les identifiants de requête et les erreurs exactes sont cohérents avec ces résultats. Il n’y a aucun blob PNG à publier pour ces cinq entrées. La nouvelle référence secondaire Baird 2006 retrouvée après la recherche est une pièce de QA ; elle n’a pas été donnée au générateur et ne justifie pas un autre appel après le refus V15.

### Recherches complémentaires

Les dix costumes non refusés demandés sont documentés séparément dans `docs/references/remaining_costumes_review_v15.json`. Cette revue n’affirme pas que les recherches web sont exhaustives. Elle distingue les vues réellement inspectées, les résultats textuels, les pages inaccessibles et les images d’une autre édition. Un modèle complet classé PC pour le premier Gears constitue une piste Grenadier nouvelle, mais ne prouve pas à lui seul l’identité exacte du modèle Xbox 360 2006. Les costumes sans preuve complète de leur édition restent à compléter.

### Conclusion de contrôle

Les décisions Keegan candidat, Keegan intro alias et Theron archive sont cohérentes avec les preuves inspectées. Aucun des résultats examinés ne doit être présenté comme « 1:1 validé » ou prêt pour la production. Le principal travail restant pour Keegan concerne la comparaison détaillée au modèle en jeu, la pose et les marges ; pour le Theron, il faut d’abord obtenir une référence finale complète de l’édition ciblée.

---

## Revue technique indépendante V15

Date : 27 novembre 2026. Base publiée : `4eedf19b7d50a66b2b209a1d76445d6078dd7403`.

### Conclusion

La revue du code, des journaux et d’un recalcul indépendant en mémoire n’a pas identifié de défaut bloquant restant après les corrections apportées pendant la revue. La V15 conserve la distinction entre fichier produit, référence attribuée, édition cible et fidélité certifiée. L’intégration finale et la réussite des 27 tests restent à constater par l’exécution du validateur complet ; ce rapport ne les anticipe pas.

Cette revue a lu les helpers `build_v15_docs.py` et `validate_v15.py`, le consolidateur existant, les quatre modules de tests d’inventaire, les catalogues et mappings V15, les 20 journaux V15 et leurs références pertinentes. Aucune source, aucun catalogue, aucun manifeste ni aucune référence Git n’a été modifié par cette revue. Seul ce rapport a été écrit hors du dépôt.

### Vérifications indépendantes réalisées

Le consolidateur a été chargé sans exécuter sa fonction d’écriture. La collecte des actifs, les rattachements de costumes, la couverture et les aliases ont été recalculés en mémoire. Le résultat correspond à la consolidation V15 produite ensuite par l’intégrateur :

| Mesure | Constat |
| --- | ---: |
| PNG actifs | 164 |
| Empreintes SHA256 actives distinctes | 164 |
| PNG archivés | 18 |
| Entrées de catalogue | 219 |
| Entrées sans référence | 28 |
| Aliases documentés de costumes | 2 |
| Avertissements de collecte | 0 |
| Promotion de fidélité 1:1 | 0 |
| Ensemble d’animations terminé | 0 |

Les 36 lignes du roster de gameplay restent inchangées en mémoire. Anthony, Jace et Kim sont des extensions du catalogue de production ; leurs nouvelles images ne créent aucun combattant de gameplay.

Les journaux V15 comptent 19 appels déclarés, un par cible, répartis en cinq PNG actifs, un PNG produit puis archivé et treize refus. Le vingtième journal correspond à l’alias Keegan et déclare zéro génération. Les 19 empreintes de prompt sont présentes et correctes. Les 33 fichiers sources distincts référencés par ces tentatives ont été relus et comparés à leurs SHA256, sans écart.

La fonction corrigée de recherche du prompt antérieur a été exécutée isolément, sans lancer le générateur de documents. Les 19 cibles sont résolues : 17 prompts sont identiques aux tentatives effectives précédentes ; seuls Shock Grenade et Incendiary Grenade comportent les compléments décrits dans leurs journaux. Le rapport de reprise rend cette différence explicite au lieu de présenter les 19 appels comme des reprises littérales.

### Couverture et provenance

#### Anthony : référence de figurine conservée comme telle

Anthony reçoit `has_visual_reference=true`, mais garde la relation `licensed_figure_reference_candidate`. Son indicateur `target_version_candidate_available` reste faux et son chemin de candidat de l’édition cible reste nul. Le validateur contient désormais une assertion spécifique contre toute promotion erronée en modèle final 2006.

Cette distinction explique qu’Anthony réduise le compteur « sans référence » tout en restant non validé pour le modèle exact demandé. Les textes doivent continuer à parler de référence disponible et conserver cette réserve.

#### Keegan : deux entrées, un seul fichier

Les deux lignes `keegan_skin_02` et `keegan_hivebusters_intro` ont le même parent et l’édition normalisée `Gears 5: Hivebusters`. Le mapping explicite pointe vers le PNG canonique et son SHA256, son journal de génération et le journal de preuve de l’alias.

Le consolidateur vérifie les identités, l’édition, le candidat sélectionné, le chemin, les octets, la provenance, la présence de preuve et la justification avant toute copie de couverture. Les chaînes, cycles et aliases multiples sont rejetés. Seuls les champs de couverture sont partagés. Le journal propre à l’alias, les propriétés du PNG et ses statuts de qualité restent distincts et inchangés.

Le total de deux aliases comprend Lahni V14 et Keegan V15. Le nouvel alias Keegan n’ajoute aucun PNG physique.

#### Theron : image produite, identité rejetée, couverture manquante

Le journal a `has_image=true`, `asset_path=null`, un `archive_path` explicite et `is_active_reference=false`. La collecte n’intègre pas ce chemin dans les actifs. La ligne `theron_skin_01` demeure sans référence sélectionnée, et le dernier résultat conserve `generated_rejected_visual`.

Le validateur contrôle séparément la présence de l’archive, son exclusion des actifs et le maintien du costume dans la liste des manquants. Aucun succès du générateur n’est donc assimilé automatiquement à une résolution de cette identité.

#### Limites visuelles préservées

Les réserves de figurine d’Anthony, de bas du corps extrapolé pour Jace et Kim, de cadrage et de détails restant à contrôler sont présentes dans les journaux et remontent dans les notes d’inventaire. Les flags de fidélité canonique, de préparation à la production et d’animation restent faux.

Les copies natives d’Anthony, Jace et Kim ont été comparées aux octets retournés par l’outil et aux blobs GitHub. Elles sont intactes. Cette vérification technique ne certifie pas leurs formes, leurs visages ou leurs costumes.

### Anomalies détectées et corrigées pendant la revue

1. **Hashes de prompt absents pour Shock et Incendiary.** Ils auraient fait échouer le validateur. Ils sont désormais présents et concordent avec les textes effectifs.
2. **Sélection erronée du journal historique de Theron.** La première version du helper choisissait le suivi V13 sans prompt. La correction combine les chemins explicitement déclarés avec les fichiers découverts et ignore les suivis sans prompt. Le résultat vérifié pour Theron est `data/generation_v4/result_theron.json`, dont le prompt est identique à V15.
3. **Ambiguïté possible des chiffres de couverture d’Anthony.** Le validateur protège maintenant explicitement sa relation de figurine et l’absence de candidat de l’édition cible.

La protection de `data/roster.json` a été conservée. L’hypothèse initiale selon laquelle les trois nouveaux personnages modifieraient ce fichier a été écartée après examen de leur appartenance au catalogue de production et du recalcul en mémoire.

### Portée des tests et du validateur final

Les 27 tests existants portent sur la séparation roster/catalogue, les identités de costumes et projectiles, les rattachements documentés, les dates et rapports versionnés, ainsi que les aliases. Les tests d’alias couvrent notamment le partage d’un fichier, la préservation des QA et de la dernière tentative, les mauvais parents ou éditions, les hashes, la provenance, les preuves absentes, les cycles et l’absence de mutation partielle après un échec.

Le helper de validation relance réellement la suite, vérifie le code de sortie et la présence du compte de 27 tests avant d’écrire un résultat positif. La revue n’a pas relancé cette suite en parallèle de l’intégrateur.

Le validateur contrôle également les sorties natives, les SHA des actifs et archives, les 176 anciens PNG, les fichiers historiques protégés, les guides originaux, les données embarquées de la galerie, la syntaxe JavaScript et la reconstruction déterministe de la bible. Les 68 rubriques et 40 cas d’acceptation sont des contenus conservés ; les cas ne sont pas exécutés par cette passe.

Deux limites de portée doivent rester explicites :

- Les contrôles d’images mesurent le fichier et l’alpha ; ils ne démontrent ni la justesse des contours ni une fidélité visuelle 1:1.
- Les tests de liens portent sur l’existence des chemins locaux, pas sur les ancres ni sur un rendu navigateur/mobile. Le validateur annonce ces exclusions.

Le vérificateur de sources parcourt `sources` et `input_images`. Les `reference_inputs` de mon lot sont redondants avec ces sources ; la revue a aussi vérifié ces entrées, sans fichier fourni au générateur laissé hors du contrôle de hash. Toute future évolution du schéma devrait conserver ce rattachement explicite.

Après toute dernière modification de journal ou de mapping, la consolidation et les audits doivent être reconstruits avant le validateur : une égalité de compteurs ne remplace pas la fraîcheur des métadonnées. La publication doit ensuite utiliser exclusivement le commit immuable validé et comparer son arbre à l’arbre GitHub.

### Empreintes des helpers relus

| Helper | SHA256 |
| --- | --- |
| `build_v15_docs.py` | `4e75a225bbd5d7c450a30a1f6d25dc72dfccd0860f793c2fcab8c1296ddf6b99` |
| `validate_v15.py` | `e97e362130a2b72837c6c0e75322909df22bbf74823180a54f94b63391d1b935` |

Les helpers peuvent encore recevoir des ajustements de documentation par l’intégrateur ; ces empreintes identifient précisément la version examinée ici. Aucune publication n’a été effectuée par cette revue.
