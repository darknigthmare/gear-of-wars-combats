# Sources et décisions visuelles — V14

**27 novembre 2026.** Les références tierces servent au contrôle et à la génération ; leurs images ne sont pas ajoutées au dépôt. Les URL, crédits, empreintes des entrées, prompts et limites sont conservés dans les journaux. Une référence finale documente la cible, sans certifier automatiquement la sortie générée.

## Références employées

| Cible | Source de production | Portée exacte |
| --- | --- | --- |
| Reyna humaine G4 | [Équipe personnages Gears 4](https://www.zbrushcentral.com/t/gears-of-war-4-art-dump/206321) · [Heber Alvarado](https://heber.artstation.com/projects/LxX6v) | Modèle final en trois vues ; Heber Alvarado pour le corps, Michelle Zhang pour la tête. Tenue humaine Outsider, sans pouvoirs de Queen Reyna G5. |
| Canker G4 | [Daniel Bohrer — Carrier Minion](https://www.zbrushcentral.com/t/gears-of-war-4-art-dump/206321) · [Guide officiel Prima](https://primagames.com/eguides/gears-of-war-4-eguide/enemy-forces/swarm) | Deux vues finales d’un projectile organique. Le guide du Carrier permet de relier Carrier Minion et Canker. |
| Leech G5 | [Bruno Melo](https://bmelo.net/projects/2xzmJB) · [ArtStation](https://www.artstation.com/artwork/2xzmJB) | Sculpture Bruno Melo, maillage/textures Can Etişkol, direction Aryan Hanbeck ; deux vues finales colorées, sujet individuel. |
| Wretch E-Day | [Antoine Verney-Carron](https://antoineverneycarron.artstation.com/projects/KR3KG4) | Modèle final complet wr01 et gros plan wr02 ; version organique sans armure. Le dos n’est pas entièrement documenté. |
| Ticker E-Day | [Antoine Verney-Carron](https://antoineverneycarron.artstation.com/projects/KR3KG4) | Partie inférieure de la planche tc : corps organique complet sans harnais ni bombe. Le Reaver supérieur est exclu. |
| Mina Jinn G4 | [Équipe personnages Gears 4](https://www.zbrushcentral.com/t/gears-of-war-4-art-dump/206321) | Modèle Jin_wide1 final avant/arrière inspecté, crédits Daniel Bohrer / Dan Roarty / Michelle Zhang. Génération refusée une fois. |
| Lahni intro / Brash Brigade | [Final Aryan Hanbeck](https://mediumrare.artstation.com/projects/oAdmNw) · [Concept Tyler Bradley](https://tylerthebradley.artstation.com/projects/ykrQgn) | Rapprochement inféré explicitement entre la tenue intro et le modèle final ; manches courtes noires du final prioritaires sur le concept. PNG V13 réutilisé. |

## Dernière passe sur les anciens manquants

Les recherches complémentaires n’ont pas établi de nouveaux corps finaux complets pour les onze costumes/projectiles et trois rencontres encore ouverts. Elles ne prouvent pas l’inexistence de telles références. Le [relevé de quatre costumes](costume_remaining_review_v14.json), la [revue de sept identités](remaining_identity_review_v14.json) et la [revue de trois rencontres](boss_remaining_review_v14.json) précisent les sources consultées, refus d’accès et exclusions.

Anya est explicitement rattachée à Contrôle Gears 2. Black Steel Anthony est bien attesté dans Gears 5 et ne doit pas être déplacé vers Gears 4 ; les pieds/jambières restent la lacune. Armored Gabe G5 ne reçoit pas la sculpture Hive Buster ou le costume Tactics. Les concepts E-Day de Tai et de Boomshot ne sont pas des modèles finaux de l’édition attendue. Le [comparatif Ticker](ticker_reference_notes_v14.json) conserve séparément la piste de matériaux Tactics.

## Sélection et transparence

Le nettoyage alpha de Reyna est archivé ; l’original est également conservé hors actifs après détection d’une latéralité de coiffure inversée. La correction de coiffure est sélectionnée après comparaison à la source officielle, avec les réserves de microdétails et de marges maintenues. Les RGB placés sous alpha 0 sont invisibles en composition correcte ; ils ne sont pas décrits comme un halo opaque. Les faibles alpha réels, dimensions, empreintes et marges utiles restent mesurés par fichier.

## Traçabilité de la reprise

L’environnement s’est temporairement déconnecté après génération. Les sorties natives ont été conservées dans leurs résultats et récupérées sous forme de blobs Git, sans régénération. Après retour de l’environnement, les fichiers locaux et empreintes ont été comparés, puis les scripts Python normaux ont servi à la consolidation finale. Aucun résultat du port JavaScript de secours ni environnement Vercel n’a été utilisé pour produire les inventaires finaux.

[Listing V14](../production/LISTING_V14.md) · [Manquants V14](../production/REPRISE_V14.md) · [Catalogue V14](../../data/production_catalog_v14.json).
