# Revues croisées V13

**27 novembre 2026 · Gears of War Combats · Baseline `3d12276302c040f05e5452de073dc3a67470554f`.**

Trois revues complémentaires ont vérifié l’inventaire et les historiques, deux sorties visuelles, puis les documents et la bible. Leurs auteurs ont travaillé en lecture seule sur le dépôt ; les corrections ci-dessous ont été appliquées par le responsable de consolidation. Cette synthèse décrit ce qui a effectivement été contrôlé. Elle ne certifie pas la fidélité 1:1 et ne remplace pas les réserves de chaque journal.

## Inventaire et conservation

Le relevé indépendant final confirme les **26 journaux V13** : six PNG, deux nouveaux refus, un refus historique retrouvé et 17 recherches sans génération. Les 15 autres refus antérieurs sont conservés sans relance. Les **41 fiches initialement manquantes** sont toutes réconciliées ; six ont désormais un candidat et **35 restent sans référence attribuée**. Voir l’[audit complet](GAPS_AUDIT_V13.json).

Le calcul indépendant en mémoire donne **154 actifs, 154 SHA-256 distincts et 15 archives**. Il confirme 51/56 personnages, 63/85 costumes, 27/31 boss et rencontres, 34/34 stages et 4/8 projectiles. Les deux IDs intro de Lahni et Keegan ne sont pas couverts automatiquement et ne créent ni PNG supplémentaire ni nouveau refus.

Les six sorties ont été comparées octet pour octet à leurs originaux natifs ; dimensions, alpha et empreintes concordent avec les journaux. Les **444 empreintes historiques protégées** sont inchangées, dont 163 PNG de production et cinq captures QA du prototype. La bible V12 a aussi été comparée au blob de la baseline : identique, SHA-256 `460589dc411db0f7bdfaf7edd607cdc707a75661e4f2afb8e6b48f9aa4a0f1f7`.

### Trois risques techniques corrigés

| Risque constaté | Correction appliquée | Preuve de contrôle |
| --- | --- | --- |
| L’ancien point d’entrée du manifeste appelait la consolidation sans suffixe et pouvait écraser le rapport V12 du même jour. | L’appel sans argument conserve le suffixe courant et détermine une version pour une nouvelle passe du même jour. Le paramètre explicite reste disponible. | Test d’une passe du même jour, d’un appel explicite V13 et d’un nouvel appel implicite : rapport antérieur préservé. |
| Un journal supprimé après consolidation n’était plus parcouru et pouvait échapper au garde de fraîcheur de la bible. | Les chemins de journaux V13 déjà déclarés par la couverture sont vérifiés avant les journaux courants. | Suppression en fixture : construction rejetée. |
| Un PNG déclaré puis supprimé était ignoré par un contrôle conditionné à sa présence. | Tout chemin d’image déclaré mais absent entraîne une erreur explicite. | Journal à jour avec image supprimée : construction rejetée. |

La mutation d’un journal sans image le même jour est également détectée par son SHA-256. Deux tests ciblés ont été exécutés par la revue indépendante ; la suite complète de **16 tests** a passé lors de la validation finale. Voir le [journal des tests](INVENTORY_TESTS_V13.txt) et la [validation](VALIDATION_V13.json).

## Revue visuelle du Riftworm et de Lahni

Les deux sorties et cinq références raster ont été ouvertes et comparées. Les mesures d’alpha et les copies natives ont été vérifiées séparément. Aucun contresens matériel d’identité, d’édition ou de portée n’a été relevé dans ces deux dossiers ; les limites restent celles d’une reconstruction candidate.

### Riftworm — extérieur Gears of War 2

Un seul corps horizontal entier est visible, tête à droite et queue à gauche. La silhouette et les principales structures suivent l’aperçu communautaire du modèle. Le concept de James Hawkins est correctement traité comme corroboration de production, sans lui attribuer une preuve exhaustive de l’extérieur final. Les dents et reliefs fins sont reconstruits ; le rendu est plus clair que l’aperçu.

Le PNG ne livre ni intérieur, ni organes, ni niveau jouable. Ses marges du sujet au seuil alpha ≥128 sont de **33/151/31/172 px**, dans une image **2172 × 724**. Des pixels alpha 1 atteignent les bords gauche, haut et bas ; cela ne coupe pas le corps principal, mais confirme la réserve sur les franges. Il ne faut pas présenter cette image comme disposant d’une bordure entièrement vide au seuil alpha >0.

Voir le [journal Riftworm](../../data/generation_v13/boss_riftworm_g2_record.json).

### Lahni — Brash Brigade / Hivebusters

Une seule figure complète correspond au rendu final DLC de l’Art Director : armure à disques, marques jaunes, bandeau, dreadlocks, manches courtes, équipements et bottes hautes. Les principaux équipements asymétriques restent du bon côté. Aucun mélange visible avec la tenue Escape sans manches n’a été constaté. Le modèle final a priorité sur le concept intro.

Le visage, les tatouages, glyphes et attaches restent interprétés. Les marges au seuil alpha ≥128 sont de **246/19/234/32 px**, dans une image **1024 × 1536** ; la consigne de 10 % de marge verticale n’est pas satisfaite. Le halo à faible alpha et ces marges sont déjà signalés. La bordure de huit pixels est entièrement transparente, sans que cela suffise à valider tout le détourage pour la production.

Voir le [journal Lahni](../../data/generation_v13/lahni_skin_01_record.json).

## Revue documentaire et bible

La revue a recoupé README, listing, reprise, audit des manquants, registre de sources, manifeste de construction et sections pertinentes de la bible avec les 26 journaux. Elle n’a pas prétendu relire intégralement les 57 711 mots ni revérifier chaque ancienne citation externe.

Les chiffres et statuts concordent. Les trois guides originaux, les matrices CSV/JSON, l’adaptation des extensions, leur audit et la bible V12 sont inchangés. Dans V13, le chapitre de guide et les sections matrice/audit sont textuellement identiques à V12 : **68 rubriques**, **18 cas E01 et 22 cas E02**, tous uniques et toujours non exécutés. Les **neuf ancres du sommaire** correspondent à des titres existants ; les **13 entrées du manifeste de construction** ont des empreintes exactes.

Deux formulations ont été améliorées après revue :

- Les résumés de recherche privilégient désormais le motif précis du journal, notamment pour Grenadier 2006, Myrrah G5, RAAM’s Shadow et Theron Tactics.
- La source de Lahni intro précise qu’elle a servi à générer `lahni_skin_01` et qu’elle a seulement été consultée pour rapprocher l’ID intro. Aucune génération n’est revendiquée pour cet alias.

La vérification finale des liens et des fichiers centraux figure dans [VALIDATION_V13.json](VALIDATION_V13.json). Le contrôle de syntaxe et des données embarquées de la galerie est effectué ; **aucun rendu navigateur/mobile n’est revendiqué**.

## Limites de cette revue

Les six images restent des candidats non certifiés, sans animation, atlas ni nouvel élément jouable. La source Sire héritée de V11 conserve un ancien chemin de recherche absent de ce workspace ; son URL et son SHA historiques restent documentés et elle n’a pas servi à une génération V13. Le nouveau visuel Sire a été inspecté et jugé insuffisant pour produire un corps isolé fidèle.

La publication GitHub doit être vérifiée sur la branche et le commit après transfert. Ces revues et la validation décrivent les fichiers préparés, sans prétendre établir cette publication à elles seules.
