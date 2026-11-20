> **Instantané historique du premier lot (19 novembre 2026).** Pour le corpus récupéré et les nouvelles images, consulter [l’état consolidé du 20 novembre](production/CONSOLIDATION_2026-11-20.md).

# État du premier lot

## Contenu de conception livré

La version 1 contient 36 fiches de combattants, 75 entrées de costume ou d'époque, 179 actions, 36 routes arcade et 24 propositions de combos pour les douze combattants du noyau. Les 179 actions se répartissent en 11 actions communes, 96 actions du noyau et 72 signatures des combattants d'extension. Les exécutions du noyau sont incluses dans ce décompte ; toutes les entrées ne sont donc pas des attaques utilisables pendant une manche.

Le catalogue Boss Battle comprend 24 rencontres et 72 phases décrites. Les 24 stages possèdent chacun six couches spécifiées, soit 144 calques à produire. La campagne présente 12 chapitres avec introduction, confrontation et conclusion. Les sources accompagnent les fiches et les propositions de gameplay sont identifiées comme des adaptations.

Les fichiers de données passent un contrôle des identifiants, des références entre roster, routes, boss, stages et chapitres, des valeurs de base et du budget d'animation. Ce contrôle ne certifie ni l'équilibrage en partie ni la fidélité visuelle.

## Prototype livré

Trois rencontres sont jouables : un duel de Marcus contre RAAM, une Berserker et une simulation contre un King Raven. Le joueur dispose du déplacement, de deux attaques de corps à corps, du tir, de la garde, de l'esquive, du rechargement actif et d'un spécial. Les boss ont trois phases, des attaques annoncées et des fenêtres de vulnérabilité. Le décor Ephyra est intégré comme master complet.

Le prototype utilise une manche par duel et une jauge spéciale unique. La campagne, les tournois, le roster complet, les exécutions, les animations dessinées image par image et le réseau restent des contenus spécifiés pour les étapes suivantes. Les personnages non illustrés gardent une représentation provisoire. Marcus utilise sa pose neutre détourée, animée par transformations de présentation ; elle ne constitue pas une animation dessinée image par image.

Le rechargement et la posture correspondent au profil décrit dans la bible. Le prototype n'implémente pas encore le verrouillage intermédiaire du chargeur, les projections, les annulations, les hauteurs d'attaque, la garde parfaite et l'endurance. Son compteur mesure des impacts rapprochés et ne garantit pas un combo sans échappatoire.

Quinze tests de logique ont été exécutés avec succès. Les contrôles portent notamment sur la garde, les bornes inclusives de recharge, le bonus limité, les vulnérabilités, les phases, les résultats, la pause et la séparation du hasard visuel. Le rendu du canvas des trois modes a été produit et inspecté. Les scripts et un appui tactile bref ont aussi été exercés dans un environnement JS. Le HUD HTML et CSS, le responsive dans un navigateur et la compatibilité avec une manette physique restent à vérifier, car l'ouverture du navigateur de test est bloquée dans cet environnement.

## Images produites et état artistique

Quatre compositions initiales ont été générées : Marcus Fenix en pose neutre, Kait Diaz en tenue hivernale en pose neutre, un décor d'Ephyra et un décor du Hollow. Les deux exports détourés sont également livrés et recensés dans le manifeste, soit six fichiers d'image. Ces dérivés des références de personnage ne comptent pas comme de nouvelles poses.

Les demandes initiales de sprites de combat pour Marcus, RAAM et la Berserker ont été refusées par le système d'image. Aucun résultat correspondant n'est déclaré livré. Les références neutres produites ensuite et les décors ont leur statut propre. Les détails de costume, les visages, les armes et les proportions devront être confrontés à des captures précises avant une validation de fidélité 1 pour 1.

Les décors sont des compositions inspirées des univers des épisodes indiqués. Ils ne reproduisent pas encore un emplacement photographié sous un angle exact et ne sont pas séparés en calques. Le suivi de production conserve les 144 couches à produire, sans les déclarer terminées à partir de deux images complètes.

## Prochain lot de production

Le lot suivant doit valider les références de Marcus et RAAM, puis dessiner leurs attentes, déplacements, gardes, impacts et premiers coups. La Berserker nécessite une silhouette de référence, une anticipation de charge, une charge, une collision et une récupération. Le King Raven nécessite le modèle exact de l'épisode choisi, ses moteurs et ses armes séparés. Les six couches du stage Ephyra doivent être préparées à la même origine et avec les zones masquées reconstruites.

Les animations individuelles, les parties de boss, les calques et les illustrations de fin représentent 240 entrées de suivi regroupées. Une entrée d'animation est un ensemble de clips, pas un seul dessin. Le budget indicatif complet représente 552 dessins par orientation pour un costume entièrement dessiné ; les reprises et réutilisations réellement possibles seront décidées après validation de chaque personnage.

Le classeur fournit des champs de contrôle artistique, technique et d'intégration. Une référence produite ne devient prête pour le jeu qu'après satisfaction de ces contrôles. Les choix de gameplay et les fichiers sources du prototype sont inclus pour que la suite puisse commencer à partir de cette version.
