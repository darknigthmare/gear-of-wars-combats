# Consolider le corpus Gears et ajouter Dom, RAAM et le Theron casqué

## Pourquoi

Les passes précédentes avaient produit la bible, le prototype et plusieurs lots d’images, mais ces fichiers n’étaient pas présents dans le dépôt distant. Des inventaires divergents signalaient encore comme absents des personnages déjà générés. Le Kestrel était resté hors du dossier d’assets.

## Changements

- Réunit le corpus initial et les deux passes de reprise, avec leur provenance et les anciennes révisions.
- Ajoute trois nouveaux PNG : Dominic Santiago, RAAM et un Theron casqué classique, un personnage entier par image.
- Porte la couverture visuelle à **35 personnages sur 36**, avec **50 PNG actifs** : 44 de personnages/variantes/présentations, quatre boss ou véhicules et deux décors. Conserve 12 révisions écartées hors de ces totaux.
- Récupère le Kestrel et conserve les variantes sans les compter comme de nouveaux personnages.
- Actualise le roster, le manifeste, la galerie et le rapport de couverture à partir des fichiers réellement présents.
- Intègre la référence statique de RAAM au duel existant ; le HTML autonome embarque Marcus, RAAM et Ephyra.
- Rend les chemins du générateur de classeur relatifs au dépôt et protège l’inventaire consolidé contre l’écrasement par le constructeur historique.

## Vérification

- 15 tests existants du moteur réussis.
- Validation des références entre personnages, rivaux, actions, routes, stages, boss et campagne : aucune erreur.
- PNG décodés et contrôlés par dimensions, canal alpha et SHA-256 ; nouvelles sorties inspectées visuellement.
- Rendu canvas des trois rencontres réussi ; duel Marcus/RAAM inspecté ; appui tactile bref et pause contrôlés dans le banc JS/canvas.
- Chromium tenté, bloqué avant ouverture de page par `socket() failed: Operation not permitted`. Aucun résultat responsive réel ni test matériel de manette n’est revendiqué.

## Limites explicites

Dizzy Wallin reste sans image après un nouveau refus du générateur. Les PNG sont des références statiques ; la fidélité 1:1, les animations, vues latérales, armes, pivots et hitboxes ne sont pas validés. Le Theron casqué vise le premier jeu, mais l’édition exacte demeure à confirmer à partir des références consultées. Les versions PDF, Word et Excel livrées sont les instantanés du 19 novembre ; la couverture actuelle est celle des JSON et de la galerie.

Le prototype conserve trois rencontres et ne rend pas jouable tout le roster. La campagne complète, les tournois, les exécutions et le réseau restent à développer.
