# Audit d'intégration du guide de combat — V12

Date : **27 novembre 2026**. Projet : **Gears of War Combats**. Périmètre : guide général et deux extensions demandées, leur rattachement à la bible et leurs écarts de production.

## Résultat

Les **trois originaux v1.0 sont intégrés sans modification**, avec leur provenance et leurs empreintes. Un [chapitre d'adaptation à Gears](../combat_extensions.md) les relie aux personnages, aux périodes et aux règles déjà définies. La [bible principale](../core_bible.md) renvoie à ce chapitre et rappelle la priorité actuelle aux assets fixes.

Cette passe intègre de la documentation et un suivi d'exigences. Elle n'ajoute au prototype ni animation dessinée, ni tag, ni système d'abonnement. Les limites sont explicites dans chaque document et dans la matrice.

## Point de départ vérifié

Référence contrôlée : commit `370e49593ee6690076b4051afc7357d1e1707aad`, branche `codex/gears-static-assets-v9-20261125` de `darknigthmare/gear-of-wars-combats`.

L'arbre Git de cette révision ne contient aucun des trois fichiers originaux. Le contrôle compare également le SHA-1 Git du contenu de chaque original à tous les blobs suivis : aucune copie identique sous un autre nom n'est retrouvée. Cela prouve l'absence des copies exactes à cette révision ; cela ne signifie pas que tous leurs concepts étaient absents.

La bible existante décrivait déjà la provocation, la sélection, des récompenses, les récits, les boss, les armes et des budgets d'animation. `prototype/README.md`, `prototype/engine.js` et `prototype/app.js` exposent trois rencontres : duel Marcus/RAAM, Berserker et King Raven de simulation. Le moteur inspecté ne contient pas de profil d'équipe actif/réserve ni de gestion de droits Patreon. Les tests historiques du prototype ne sont pas présentés comme des tests des nouvelles extensions.

## Sources récupérées et contrôle des copies

| Source | Version déclarée | Octets | Copie exacte |
| --- | --- | ---: | --- |
| Guide général | 1.0 — 25/11/2026 | 55 172 | Oui |
| Extension 01 | 1.0 — 26/11/2026 | 60 589 | Oui |
| Extension 02 | 1.0 — 27/11/2026 | 47 334 | Oui |

Les fichiers sont retrouvés sur Drive le 27 novembre 2026. Le [manifeste des sources](../guides/combat/source_manifest.json) conserve noms, URL, identifiants de source, dates de dépôt, SHA-256, SHA-1 Git et résultat de comparaison à la révision initiale. La version imprimée dans le document est préservée, même lorsque son horodatage de dépôt UTC correspond à la veille.

Les copies sont accessibles depuis le [dossier des guides](../guides/combat/README.md). Aucune adaptation, traduction ou correction n'est insérée dans ces originaux ; les décisions spécifiques au projet restent dans le chapitre V12.

## Couverture documentaire

| Ensemble | Rubriques tracées | Traitement |
| --- | ---: | --- |
| Guide général | 30 : 00–29 | Raccord à la bible et aux inventaires existants ; écarts conservés |
| Extension 01 | 20 : 30–49 | Contrats d'équipe, présentation, clashes, entités, bonus et exploration |
| Extension 02 | 18 : 50–67 | Modèle d'accès, présentation des verrous, acquisitions et validation |
| **Total** | **68** | Aucune rubrique de sommaire omise |

Ce total est un nombre de **rubriques sources suivies**. Il n'est ni le nombre de fonctionnalités jouables, ni une liste atomique exhaustive de tous les tests, ni un taux d'avancement global du jeu.

La matrice comprend 57 rubriques retenues, 8 adaptées, 2 différées et 1 soumise au choix d'offre avant activation. « Différée » conserve une exigence et son critère ; cela ne la supprime pas. Le réseau reste une décision d'architecture à préparer tôt, même si la livraison vient plus tard. L'adaptateur d'abonnement et la définition de l'offre restent hors fonctionnement actuel.

- [Matrice CSV](GUIDE_REQUIREMENTS_V12.csv) : identifiant, source, section, décision, priorité, preuve initiale, documentation après intégration, état runtime, manque et critère d'acceptation.
- [Même matrice en JSON](GUIDE_REQUIREMENTS_V12.json) : version du schéma, périmètre et 68 entrées identiques.

## Adaptations propres à Gears

Les associations prioritaires s'appuient sur des sources officielles citées dans le chapitre : Marcus/Dom, Delta, Kilo, les héros de Tactics, le groupe de Gears 4 et Scorpio. Les noms de supers, règles de tag, valeurs de jauge, bonus et Archives sont des créations du projet. Les sources des personnages ne leur confèrent pas un statut canonique.

Les règles empêchent de confondre la variante Gears 3 de Baird/Cole avec leurs versions Judgment, les versions du groupe de Gears 4 avec celles de Gears 5, JACK Gears 5 avec JACK Tactics, ou une équipe libre avec un événement de campagne. Chaque duo narratif réclame un contrôle de scène et de disponibilité.

Le chapitre couvre aussi les points qui dépassaient le résumé initial de la demande : clashes et QTE accessibles, objets posés, propriétaires des projectiles persistants, parties de boss, transitions de zones, destination non installée, réserve KO, conservation des compteurs de combo et fins dramatiques incompatibles.

Les verrous distinguent découverte, droits, installation et compatibilité. Un asset manquant reste un manque de production. Une acquisition permanente et un droit temporaire restent deux sources séparées. L'Archives de campagne est un espace d'interface original compatible, sans ajout d'un lieu officiel au lore.

## Travail restant visible

Les 10 modèles de production de l'Extension 01 et les 6 de l'Extension 02 sont intégralement préservés dans les sources. Le chapitre définit les contrats et premières familles ; les fiches détaillées de chaque personnage, paire, scène, bonus ou récompense restent à remplir à mesure de leur production. Un modèle copié n'est pas déclaré fiche terminée.

Les 18 scénarios d'acceptation de l'Extension 01 et les 22 de l'Extension 02 restent à exécuter dans leurs futurs systèmes. Les résumés du chapitre n'effacent aucun scénario des originaux. Ce sous-lot n'exécute pas de tests runtime des extensions, puisqu'il ne les implémente pas.

La phase actuelle privilégie toujours **les personnages/costumes fixes manquants, ennemis, machines, projectiles et stages**. Les animations de taunt, sélection, tag, supers et déblocage sont planifiées ; aucun PNG fixe n'est compté comme une animation. Les layers de parallaxe, poses alternatives, clips et contrôle canon détaillé restent suivis séparément.

## Vérification documentaire réalisée

- Les tailles et SHA-256 des trois copies correspondent aux fichiers téléchargés.
- Les trois contenus complets sont absents de l'arbre de la révision initiale, y compris sous un autre nom.
- Les sections 00 à 67 apparaissent une seule fois dans la matrice ; CSV et JSON partagent les mêmes 68 identifiants.
- Les chemins documentaires relatifs ajoutés pointent vers les fichiers prévus.
- Les nouveaux documents gardent les statuts de conception et de fonctionnement séparés.

Le contrôle ci-dessus confirme l'intégration documentaire. La qualité visuelle 1:1, l'équilibrage, le réseau et l'accès externe demandent leurs validations propres ; aucune de ces validations n'est déduite de la présence de ce rapport.

## Traçabilité des 40 cas d’acceptation sources

Cette table reprend les **40 cas sources complets** (18 de l’Extension 01, section 47 ; 22 de l’Extension 02, section 64). Les identifiants `E01-01` à `E01-18` et `E02-01` à `E02-22` appartiennent au suivi de validation ; ils ne remplacent pas les rubriques `CG-00` à `CG-67`.

**État de chaque ligne : `non_execute` dans l’intégration documentaire V12.** Le rattachement indique où les règles et attentes sont conçues, pas où un test a réussi. Les sections citées renvoient au [chapitre d’adaptation](../combat_extensions.md).

| Cas source | Condition à vérifier | Rattachement Gears |
| --- | --- | --- |
| `E01-01` | Navigation rapide puis confirmation et désélection sans effets résiduels. | §4 |
| `E01-02` | Taunt interrompu et retour au contrôle selon les fenêtres annoncées. | §3 |
| `E01-03` | Assistance et relais demandés au même instant pour un partenaire unique. | §5–6 |
| `E01-04` | Deux actions tentant de dépenser la dernière portion de jauge. | §5 |
| `E01-05` | Soutien touché ou KO pendant son arrivée ; état de l'équipe cohérent. | §6 |
| `E01-06` | Super duo demandée pendant la sortie d'une assistance. | §6–7 |
| `E01-07` | Attaque initiale du super bloquée ou ratée ; résolution correcte. | §7 |
| `E01-08` | Fin dramatique avec version, lieu ou partenaire incompatible ; remplacement. | §2 et §7 |
| `E01-09` | Clash simultané avec projectile tiers, piège ou assistance. | §8–9 |
| `E01-10` | Réussite, échec, égalité, absence de réponse et déconnexion pendant un QTE. | §8 |
| `E01-11` | Propriétaire en réserve ou KO avec une entité encore active. | §9 |
| `E01-12` | Transition d'arène pendant un combo utilisant un objet placé. | §9 et §15 |
| `E01-13` | Réflexion de projectile puis dégâts, attribution et éventuelle fin dramatique. | §9 et §7 |
| `E01-14` | Tentative de boucle infinie combinant pièges, relais et assistances. | §6 et §9 |
| `E01-15` | Horde à la limite de présence : performance, lisibilité et issues accessibles. | §10 |
| `E01-16` | Bonus réussi ou raté : bonne progression, ressources et récompenses. | §10 et §13 |
| `E01-17` | Déblocage, sauvegarde et rechargement : contenu conservé sans doublon. | §13 |
| `E01-18` | Passage abrégé d'une scène et correction réseau : même état de combat. | §8, §15 et §17 |
| `E02-01` | Personnage secret : nom, silhouette, voix et texte accessible ne le trahissent pas. | §4 et §12 |
| `E02-02` | Slot verrouillé : navigation et condition lisibles, confirmation non bloquante. | §4 et §12 |
| `E02-03` | Déblocage automatique ou à réclamer : bon état, bonne animation, bon contenu. | §11–13 |
| `E02-04` | Condition ET / OU : branches correctes, progression et alternatives explicites. | §13 |
| `E02-05` | Récompense réclamée deux fois ou sauvegarde interrompue : attribution unique. | §13 |
| `E02-06` | Costume acquis avant le personnage : récompense conservée, dépendance indiquée. | §12–13 |
| `E02-07` | Costume gagné définitivement puis abonnement expiré : accès permanent conservé. | §13–14 |
| `E02-08` | Catalogue temporaire expiré : source retirée, préférences et progression préservées. | §14 |
| `E02-09` | Annulation avec accès encore valide : aucune révocation anticipée injustifiée. | §14 |
| `E02-10` | Service indisponible : état inconnu et politique hors ligne correctement appliqués. | §14 |
| `E02-11` | Droit valide mais assets absents : message d'installation, pas faux verrou de paiement. | §12 et §15 |
| `E02-12` | Remboursement d'une source et seconde source valide : bon accès final. | §14 |
| `E02-13` | Stage abonné contre joueur non abonné : chargement, participation et choix conformes. | §14–15 |
| `E02-14` | Transition vers un stage lié : destination et assets disponibles pour la partie. | §15 |
| `E02-15` | Expiration pendant un match : résultat valide et changement au moment prévu. | §14 |
| `E02-16` | Costume ou partenaire équipé devenu inaccessible : remplacement sans perte de profil. | §12–14 |
| `E02-17` | Variante vivante ou statique : choix de confort disponible selon la règle annoncée. | §12 et §15 |
| `E02-18` | Mode verrouillé : aucune boucle de prérequis et progression récupérable. | §11–13 |
| `E02-19` | Compte invité, double liaison ou changement de niveau : droits attribués au bon profil. | §14 |
| `E02-20` | Événements externes doublés ou désordonnés : état final cohérent, pas de double lot. | §13–14 |
| `E02-21` | Clavier, manette, lecteur d'écran et mouvement réduit : états compréhensibles. | §4, §8 et §12 |
| `E02-22` | Migration, resynchronisation et restauration : acquisitions et sources conservées. | §13–14 |

L’inventaire des cas est contrôlé contre les lignes numérotées des deux sources intégrales. La réflexion de projectile, les changements de compte et de niveau, le remboursement d’une source, la déliaison et les sources d’accès multiples sont explicités dans le chapitre après relecture. Aucun comportement externe n’est déclaré opérationnel.
