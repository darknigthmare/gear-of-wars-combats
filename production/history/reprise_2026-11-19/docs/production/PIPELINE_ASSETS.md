# Production des personnages et animations

Le [roster](../../production/roster.json) suit 36 personnages. Les 16 visuels évoqués dans la conversation antérieure restent une **affirmation historique non vérifiée** tant que leurs fichiers n'ont pas été récupérés. Les 20 autres entrées sont initialisées à `pending_current_pass` : ce statut ne prouve ni une génération réussie ni la présence d'un fichier.

## Trois niveaux de livrable

| Niveau | Ce qui est établi | Ce qui reste à faire |
| --- | --- | --- |
| Référence | Identité, édition, tenue et traits observables, avec provenance | Créer une image exploitable sans inventer les détails occultés. |
| Pose de base générée | Une image individuelle effectivement produite et inspectée | Corriger les écarts, définir le cadrage de jeu et produire les transitions. |
| Frames de combat validées | Images d'une action vérifiées en séquence, avec durée, origine et état de jeu | Vérifier l'intégration et la lisibilité dans le moteur. |

Une référence officielle ou un beau rendu immobile n'est pas automatiquement une frame de combattant prête pour le jeu. Une seule pose ne suffit pas à déclarer un personnage animé.

## Flux de travail

1. **Verrouiller l'identité et la variante.** Associer au personnage un jeu précis, une tenue, une version de l'armure et les armes retenues. Consigner les sources et les parties invisibles dans le registre des références. Les [notes de sources](../references/locust-and-tactics.md) séparent captures officielles, rendus relayés, figurines et sources communautaires.
2. **Produire une pose de base individuelle.** Une image contient un personnage et une pose. Conserver la tête, les pieds, les armes et les appendices dans le cadre, avec une marge suffisante. Les vues alternatives, variantes et frames d'animation sont des fichiers distincts ; une planche de plusieurs personnages ne remplace pas ces fichiers.
3. **Inspecter l'image obtenue.** Vérifier visage, silhouette, anatomie, casque, tatouages, plaques, sangles, arme, couleurs et matière contre les références de la variante. Documenter ce qui reste incertain. Une génération refusée ou échouée ne crée aucun asset et ne devient jamais un statut de disponibilité.
4. **Préparer le cadrage de jeu.** Employer un fond transparent lorsque nécessaire, vérifier le canal alpha réel, garder une échelle cohérente, une ligne de sol stable et un point d'origine documenté. Éviter les parties coupées et les ombres opaques indésirables. Préserver les proportions de chaque personnage ; ne pas ramener un Warden à la taille d'un humain.
5. **Construire chaque action avec ses transitions.** Produire anticipation, action lisible et retour vers une pose compatible. Documenter la durée des frames, les événements utiles et l'origine des images. Une arme qui tire ou frappe doit rester alignée avec l'action visuelle.
6. **Vérifier en séquence puis dans le jeu.** Observer la lecture à la taille réelle, les contacts au sol, les déplacements, les raccords de boucle et les changements d'état. Vérifier que les boîtes de contact et les événements de jeu correspondent au mouvement. Aucun test d'intégration n'est supposé acquis par la seule présence des images.
7. **Mettre à jour le suivi d'après les fichiers réels.** Ajouter des chemins relatifs exacts dans `asset_paths`, préciser le résultat dans `visual_status` et conserver `animation_status: not_verified` tant que les séquences n'ont pas été contrôlées. L'existence d'une branche ou d'un dossier ne prouve pas la publication des assets.

## Versions canoniques et asymétries

Le Theron actuellement documenté est le **garde sans casque de Gears of War 3**. Le rendu classique de RAAM possède une édition encore incertaine. Mikayla porte sa tenue de milicienne Gears Tactics ; la version de Myrrah documentée porte son armure de guerre Gears 3. Ces limites figurent dans le [registre des références](../../production/references/locust-and-tactics.json).

Les côtés gauche et droit désignent le corps du personnage. **Ne pas retourner automatiquement une image pour fabriquer l'autre orientation** : cela inverserait notamment tatouages, prothèses, épauliers, accessoires, inscriptions et main portant l'arme. Examiner chaque personnage, conserver ses asymétries canoniques et créer ou corriger une vue opposée lorsqu'un miroir les dénaturerait. Une exception de rendu éventuelle doit être identifiée et validée explicitement, sans devenir une règle globale.

Une figurine sous licence peut documenter une forme, mais ses jointures, attaches et matériaux plastiques ne sont pas des éléments du personnage. Un rendu coupé aux cuisses ne valide pas le dessin des bottes.

## Ordre utile pour les prochaines animations

Il s'agit d'un **ordre de production proposé**, pas de l'affirmation que ces animations existent, ni d'un moveset officiel Gears de jeu de combat.

| Priorité | Séquences | Vérification déterminante |
| --- | --- | --- |
| 1 — socle | Neutre respiré, entrée/sortie du neutre, marche avant/arrière, arrêt | Boucle sans saut de pose, taille stable et pieds cohérents. |
| 2 — déplacements du mode | Ruée et freinage ; saut/décollage/réception ou autre mouvement seulement si prévu dans les règles | Trajectoire et déplacement visuel accordés au mouvement du jeu. |
| 3 — défense et réactions | Garde et sortie de garde, impacts légers/lourds, chute, récupération, défaite | Réactions lisibles, transitions vers les états réellement implémentés. |
| 4 — armes retenues | Épaulé, tir et recul, rechargement, anticipation/contact/récupération du corps-à-corps | Arme fidèle, main correcte, canon ou zone de frappe stable, événements synchronisés. |
| 5 — identité jouable | Actions propres au personnage retenues par la conception, provocation, victoire, entrée | Respect des références et raccords complets ; distinguer adaptation du jeu de combat et fait canonique. |
| 6 — scènes spécifiques | Introduction, rivalité, fin de parcours ; séquences de boss ou de finisher prévues par le design | Cadrage, accessoires et transitions adaptés à la scène effectivement implémentée. |

Pour JACK, remplacer les exigences de pas par une référence stable de hauteur et des transitions de vol. Pour les silhouettes très volumineuses, capes, tuyaux et masses doivent rester cohérents d'une frame à l'autre. Aucun nombre de frames ni timing compétitif n'est présenté comme officiel : ils seront fixés et vérifiés par la conception du mode.
