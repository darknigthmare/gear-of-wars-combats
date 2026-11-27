# Gears of War Combats — intégration du guide et des deux extensions

Version de conception V12 — 27 novembre 2026. Ce chapitre complète la [bible principale](core_bible.md). Il adapte le guide commun de Darknigthmare et ses extensions aux personnages, aux époques et aux règles de ce dépôt.

**État réel : sources intégrées et conception détaillée.** Les systèmes décrits ci-dessous ne sont pas ajoutés au moteur par ce chapitre. Les animations restent des besoins de production ; la passe courante poursuit les sprites fixes, les costumes, les projectiles, les ennemis et les masters de stages manquants. Un fichier présent, un contenu documenté, un contenu jouable et un contenu validé sont quatre résultats différents.

## 1. Documents de référence et décisions d'intégration

Les trois originaux sont conservés sans modification sous `docs/guides/combat/`. Leurs tailles, empreintes SHA-256 et liens Drive sont enregistrés dans [source_manifest.json](guides/combat/source_manifest.json). Le [rapport d'intégration](production/GUIDE_INTEGRATION_V12.md) consigne le point de départ et la vérification des copies.

| Référence | Rubriques | Rôle dans Gears Combats |
| --- | --- | --- |
| [Guide général v1.0](guides/combat/Combat_Games_Guide_General_v1.0.txt) | 00–29 | Socle de bible, fidélité, combat, récits, boss, arènes, production et validation |
| [Extension 01 v1.0](guides/combat/Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt) | 30–49 | Taunts, sélection, équipes, clashes, entités, bonus et exploration |
| [Extension 02 v1.0](guides/combat/Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt) | 50–67 | Contenus verrouillés, acquisitions, conditions et soutiens |

La [matrice de 68 rubriques](production/GUIDE_REQUIREMENTS_V12.csv) indique pour chacune sa prise en compte, sa preuve documentaire, son écart et son critère d'acceptation. Elle ne transforme pas l'intégration des documents en pourcentage de jeu terminé.

Les règles de duel de la bible restent la référence : simulation à 60 pas/s, super personnelle plafonnée à trois barres dans le jeu cible, munitions et posture distinctes. La jauge d'équipe ci-dessous est une nouvelle ressource conçue pour les modes d'équipe. Le prototype dispose encore d'une jauge spéciale unique et de trois rencontres ; il ne doit pas être présenté comme l'implémentation de ce nouveau profil.

## 2. Fidélité, périodes et statut de chaque création

Les contenus emploient désormais cinq statuts de fidélité : `canon_atteste`, `adaptation_jouable`, `original_compatible`, `alternatif_crossover` et `a_confirmer`. Le statut de production est enregistré séparément. Un costume absent n'est pas un costume à débloquer ; un contenu non vérifié ne devient pas canonique parce qu'il apparaît dans une galerie.

Chaque fiche doit fixer l'œuvre, la version du personnage, le costume, l'arme, la période, la source et les détails visuels encore à contrôler. La page qui confirme l'existence d'un personnage ne prouve pas la géométrie de son arme ou la disposition de ses sangles. Avant de marquer un sprite validé 1:1, comparer des captures déterminées avec visage, silhouette, armure, matériaux, asymétries et équipement visibles.

La campagne est une anthologie. Un partenaire n'intervient que lorsqu'il est présent, vivant, disponible et correctement équipé dans le chapitre choisi. Les équipes transversales du versus portent la mention « Simulation libre ». Aucun dialogue de ce mode n'ajoute un événement au récit officiel. Les séquences et noms d'attaques inventés dans ce document sont des créations de gameplay.

Les invités et collaborations, même lorsqu'ils ont existé dans un mode multijoueur officiel, restent des entrées `alternatif_crossover` pour la narration de ce projet. Leur disponibilité commerciale ou promotionnelle ne prouve aucune présence dans les événements de campagne. Aucun crossover n'est ajouté à une route canonique par les extensions ; tout mode alternatif éventuel affiche sa continuité propre.

### Associations prioritaires et bornes de lore

| Identifiants existants | Base attestée | Application conçue |
| --- | --- | --- |
| `marcus` + `dom` | La campagne du premier Gears les associe en coopération [GX01] | Duo de départ pour le tag ; versions Gears 1 cohérentes |
| `baird` + `cole` | Ils appartiennent avec Marcus et Dom à Delta [GX02] | Coordination couverture/approche ; les costumes Gears 3 du roster ne sont pas réemployés pour une scène Judgment |
| `baird`, `cole`, `paduk`, `sofia` | Kilo Squad réunit ces quatre personnages dans Judgment [GX03] | Paires de deux dans la route Judgment ; troisième ou quatrième membre seulement en présence narrative |
| `gabe` + `sid` | Sid accompagne Gabe au début de Tactics [GX04] | Relais soutien/assaut ; aucun pouvoir de téléportation ou d'invulnérabilité ajouté |
| `gabe` + `mikayla` | Le blog de Tactics présente leurs fonctions de soutien et de précision [GX04] | Paire après le point de rencontre de la route, à valider sur la scène du jeu |
| `jd`, `kait`, `del` | Le trio constitue le groupe central de Gears 4 [GX05] | Versions Outsider de Gears 4 requises pour cette route ; leur présence ne prouve pas l'existence de ces sprites |
| `lahni`, `keegan`, `mac` | Scorpio Squad et ses capacités sont décrits pour Hivebusters [GX06, GX07] | Paires de deux compatibles ; la troisième place n'est pas un membre caché gratuitement contrôlable |
| `jack` | Bot de soutien présenté pour la Horde de Gears 5 [GX08] | Choisir JACK combattant ou JACK entité liée à un kit ; bloquer sa duplication dans la même composition |

Les sources attestent les identités, les regroupements ou capacités cités. Elles n'attestent aucune super duo créée pour ce fan game. Les paires Locustes, les chaînes de commandement et les apparitions de Kryll demandent des fiches de scène distinctes avant une chorégraphie narrative. La présence de deux ennemis dans le même camp ne prouve pas qu'ils ont combattu ensemble à cette époque.

## 3. Taunts et présentation du combattant

Chaque combattant reçoit une fiche de provocation avec une action compatible avec son équipement : geste de défi, contrôle d'arme sans munition gratuite, attitude d'attente ou réponse de personnalité. Les premières fiches concernent Marcus, Dom, Baird, Cole, RAAM, Kait et Scorpio. Aucune réplique inventée n'est attribuée à un enregistrement officiel.

Le réglage initial proposé est un engagement de 60 frames, interrompu par un impact, sans gain de vie, de munition ou de super. Les 24 dernières frames peuvent permettre une sortie vers la garde si les tests le justifient. Une provocation de victoire est cosmétique ; une provocation pendant le duel possède une récupération punissable. Les commandes sont remappables et le taunt ne partage pas le bouton de rechargement.

Les fiches distinguent : entrée, maintien éventuel, sortie, interruption, retour à la pose neutre, son, texte et version à mouvement réduit. Le VFX d'une arme ne doit pas être dessiné deux fois, dans le sprite et dans l'émetteur du moteur. Une vérification visuelle exige qu'une arme portée, un chargeur et les protections restent du même côté.

## 4. Sélection, confirmation, désélection et annulation

Le cycle de présentation est `idle → focus_enter → focus_loop → confirm → ready`. Changer de case avant confirmation déclenche `focus_exit` puis la nouvelle entrée. Annuler une confirmation déclenche `deselect → idle`. Une fermeture de menu ou un changement de costume invalide tous les événements cosmétiques de la sélection précédente.

Le focus utilise immédiatement le portrait disponible, sans attendre une animation. Une entrée proposée de 18 frames et une sortie de 12 frames évitent de bloquer la navigation. Les clips sont interruptibles ; seule la sélection finale décide du personnage engagé. Un identifiant de session de sélection empêche qu'un son ou un effet retardé de l'ancien personnage se déclenche sur le suivant.

Le panneau montre nom, période, costume, rôle, statut d'accès et condition suivante utile. Un slot secret reçoit un dossier neutre ; le nom du personnage ne doit pas fuiter par le texte accessible, le son, un attribut HTML ou une miniature. Un contenu identifié mais verrouillé reste inspectable sans pouvoir être confirmé. La préférence de costume est sauvegardée séparément du droit de l'utiliser.

Les animations sont planifiées individuellement pour chaque version. Une rotation globale d'un PNG reste une transformation de présentation ; elle n'est pas comptée comme un clip dessiné.

## 5. Profils d'équipe, jauges et commandes

| Profil | Composition | Défaite et restrictions |
| --- | --- | --- |
| Duel classique | Un actif | Règles existantes ; aucun appel de partenaire |
| Assistance | Un actif + un soutien | KO de l'actif termine l'équipe ; soutien non contrôlable |
| Tag hybride | Un actif + une réserve | Deux vies distinctes ; défaite quand les deux sont KO |
| Boss coopératif | Deux joueurs actifs | Contrat de boss propre ; ce n'est pas le tag à un joueur |

Le profil Tag hybride est la cible de l'extension. Les équipes successives après KO restent un autre mode. Pas de doublon d'identité dans la même équipe : Marcus jeune et vétéran ne peuvent servir de deux membres distincts sans profil alternatif explicitement choisi. Les homologues adverses restent permis en versus libre, avec palette et HUD différenciés.

### Réglage initial proposé à éprouver

| Action | Coût proposé | Condition décisive |
| --- | --- | --- |
| Assistance | 25 points d'équipe | Réserve prête ; récupération de 360 frames après sortie |
| Tag volontaire | 25 points d'équipe | Actif en état autorisé ; réserve prête ; récupération de 300 frames |
| Relais après KO | Aucun | Un membre survivant disponible ; priorité aux règles de fin de manche |
| Super duo | 100 points d'équipe + 2 barres personnelles du meneur | Deux membres valides ; attaque initiale confirmée pour la séquence longue |
| Finisher d'équipe | Aucun coût supplémentaire après victoire | Victoire finale confirmée et deux participants présents dans la scène |

La jauge d'équipe va de 0 à 100, commence à 50 et récupère provisoirement 1 point toutes les 12 frames de simulation active. Elle ne se remplit ni en pause, ni pendant une cinématique verrouillée, ni à la faveur d'un changement de stage. Cette recharge est un paramètre de test ; mesurer les stratégies d'attente avant validation. Les super personnelles, munitions, chargeurs renforcés et objets restent attachés à leur propriétaire.

Actions logiques : `TAUNT`, `ASSIST`, `TAG_SWITCH`, `TEAM_SUPER`, `TEAM_FINISHER`, `ENTITY_ORDER`. Elles ont des touches distinctes par défaut. Un schéma appui court/maintien ne sera proposé qu'avec seuil explicite et commande de remplacement accessible. Le joueur voit jauge, récupération, vie de la réserve et cause d'indisponibilité.

Une commande rejetée ne dépense rien. Le moteur futur devra réserver la ressource et le partenaire dans une transaction unique, puis valider l'action. Deux demandes dans la même frame ne peuvent consommer deux fois les mêmes 25 points ou engager deux fois le même membre. Les priorités sont fixées par le profil et enregistrées dans le replay.

## 6. Assistance et tag : contrats de simulation

Une assistance suit `ready → entering → acting → exiting → cooldown → ready`. Les variantes `hit`, `ko` et `cancelled` ont une sortie définie. Le partenaire possède une zone de présence et une vulnérabilité annoncées ; son apparition ne téléporte pas arbitrairement l'adversaire et ne permet pas de couvrir les deux côtés sans signal.

Pour le profil initial, une assistance touchée interrompt son action et applique les dégâts à la vie propre de la réserve. Elle peut être mise KO ; l'équipe continue tant que l'actif survit. Un soutien déjà KO ne peut être rappelé. Son cooldown commence à sa sortie effective, pas au premier appui. Un signal de départ et un bord de scène dégagé rendent son arrivée lisible.

Le tag volontaire est possible depuis le neutre ou une fenêtre d'annulation explicitement portée par un coup. Il est interdit pendant garde subie, hitstun, projection, exécution, clash ou transition non terminée. Le prototype de réglage vise 18 frames de départ, 24 d'entrée et une protection limitée contre les impacts résiduels déjà consommés ; aucune invulnérabilité générale n'est acquise par le simple transfert de contrôle.

Le combo conserve son identifiant, son scaling, ses rebonds utilisés et sa gravité. Le tag ne remet pas à zéro les munitions, la super ni la récupération. Un relais après KO positionne le survivant sur une entrée annoncée, nettoie les effets terminés et ne demande jamais une jauge que le joueur ne peut plus obtenir. Si le dernier membre tombe, la fin de manche résout d'abord le résultat.

## 7. Supers combinées, finishers et scènes dramatiques

Les noms ci-dessous sont créés pour le projet. Les armes précises et prises de contact seront figées après examen des scènes de référence et des costumes retenus.

| Fiche de conception | Participants | Contribution et limite |
| --- | --- | --- |
| `duo_delta_crossfire` | Marcus + Dom, Gears 1 | L'un ouvre une ligne de tir, l'autre exploite le recul ; séquence courte si garde ou échec |
| `duo_delta_breach` | Baird + Cole, même épisode | Préparation de l'approche puis impact rapproché ; pas d'engin ou d'explosif absent du kit |
| `duo_kilo_relay` | Deux membres compatibles de Kilo | Progression couverte ; dialogue adapté à la relation ; costumes Judgment requis |
| `duo_tactics_opening` | Gabe + Sid | Créneau de soutien suivi d'une poussée de front ; bonus traduit en rythme 2D, pas en magie |
| `duo_tactics_precision` | Gabe + Mikayla | Couverture puis tir de précision ; disponibilité narrative vérifiée |
| `duo_scorpio_breach` | Lahni + Mac | Protection et approche mêlée ; Electroblade et Barrier renvoient à Hivebusters [GX07] |
| `duo_scorpio_supply` | Keegan + un membre de Scorpio | Réapprovisionnement encadré puis action commune ; pas de recharge infinie [GX07] |

Une super mobilise les deux participants jusqu'à sa sortie. La première attaque détermine touche, garde ou échec. La séquence longue ne démarre que sur cible compatible ; la version courte garde un coût et une récupération définis. Un boss géant utilise un point faible ou un module, jamais une saisie humanoïde agrandie. Une cible mécanique n'utilise pas un effet organique par défaut.

Le finisher d'équipe intervient après la victoire, dans la fenêtre de 180 frames déjà prévue par la bible. Il ne change ni gagnant, ni score compétitif. Une réserve KO n'est pas ressuscitée pour la scène : utiliser la finition solo ou une conclusion d'équipe non physique seulement si la fiche l'autorise. En confort ou tournoi, une variante courte produit le même résultat et reste disponible sans coût.

Une fin dramatique possède une table de conditions : vainqueur, perdant, duo éventuel, variantes, stage, chapitre, branche de récit et victoire finale. Si une seule condition échoue, revenir à une conclusion compatible. Une scène fidèle à un moment précis demande une référence de cette scène ; une nouvelle conclusion reçoit `adaptation_jouable` ou `alternatif_crossover`. Ne pas présenter comme canon une victoire hypothétique simplement parce qu'elle implique des personnages officiels.

## 8. Clashes et résolution accessible

Un clash n'est possible qu'entre actions listées comme compatibles, au même intervalle de collision et avec des équipements adaptés. La première fiche porte sur une opposition d'armes à contact dans une simulation ; son animation précise reste à référencer. Les balles ordinaires, les attaques de boss et les invocations ne deviennent pas automatiquement des confrontations de force.

Le profil spectacle peut utiliser un QTE court à trois entrées espacées, chacune avec fenêtre annoncée. Aucun martèlement obligatoire. Le profil confort permet maintien ou résolution automatique avec le même plafond de résultat. Le profil compétition emploie une résolution déterministe fondée sur les actions engagées, leurs ressources et leur priorité ; il ne mélange pas les classements de règles différentes.

Définir réussite, échec, égalité, absence de réponse, déconnexion et interruption par un tiers. La simulation conserve une seule vérité : les effets de caméra ne gèlent pas un projectile si les règles le font continuer. Un projectile tiers peut annuler le clash selon le contrat, sans déclencher simultanément la récompense du QTE. Les deux combattants retrouvent une position, une orientation, des ressources et une récupération déterminées.

## 9. Entités natives, objets posés et projectiles persistants

Une entité liée au moveset possède un propriétaire, un identifiant unique, un état, une durée de vie, un budget de présence et une règle de retrait. Elle ne remplit pas automatiquement un slot d'équipe. La capacité de soutien de JACK est attestée pour Gears 5 Horde [GX08] ; son rattachement à un kit de ce jeu demeure une adaptation à décider personnage par personnage.

| Famille | Contrat proposé | Limite de fidélité |
| --- | --- | --- |
| JACK de soutien | Un bot par propriétaire ; ordre, approche, action, retour ; interruptions prévues | Version Gears 5 distincte de la variante Tactics |
| Grenade posée | Un objet armé par type et propriétaire ; temporisation, collision, explosion unique | Type et modèle de grenade doivent correspondre au kit |
| Outil d'ingénieur | Objet dans la scène seulement si la fiche fournit source, montage et destruction | La profession de Baird ne justifie pas n'importe quelle tourelle |
| Effet attaché à une arme | Origine et propriétaire conservés ; sortie de zone et extinction définies | Ne pas ajouter un pouvoir surnaturel à une arme ordinaire |
| Projectile persistant | Trajet, durée, nombre de touches et collision distincts de l'image | Aucun reflet automatique des munitions sans mécanique approuvée |

Lors d'un tag, l'objet existant reste attribué à son propriétaire en réserve. Une règle par entité décide s'il persiste, se retire ou devient inactif ; le choix initial est retrait des drones contrôlés et maintien des grenades déjà armées jusqu'à leur résolution. Le KO du propriétaire ne remet pas leur temporisation à zéro. La fin de manche nettoie toutes les entités sans accorder d'impacts après le résultat.

Les projectiles conservent les champs `owner`, `team`, `source_action`, `spawn_frame`, `expiry_frame`, `hit_registry` et `lore_variant`. La destruction retire les collisions avant les particules. Une réflexion, lorsqu'elle est autorisée, modifie le propriétaire de dégâts de façon explicite et enregistre l'ancien pour la traçabilité ; aucune réflexion n'est activée simplement parce qu'une image opposée a été créée.

Après réflexion, l'attribution du KO et les conditions d'une éventuelle fin dramatique utilisent le propriétaire effectif et la règle de l'action, jamais le nom du sprite. Une victoire indirecte ne valide pas une scène exigeant un coup de signature différent. Le coût, les cibles déjà touchées et la durée restante ne sont pas réinitialisés sans règle explicite.

Une transition doit annoncer si les objets sont transférés avec positions relatives, consommés ou retirés. Le défaut proposé retire les objets de zone après résolution de la frame de départ, sans remboursement ; les projectiles déjà responsables d'un impact ne frappent pas à nouveau à l'arrivée. Un effet attaché suit son propriétaire uniquement si l'état reste compatible.

## 10. Stages bonus et liens avec les récits

Ces épreuves sont des adaptations pour le projet. Leur présence dans une route ne transforme pas leur objectif en événement officiel. Elles utilisent un `bonus_id`, un lieu, une version, des participants, un score déterministe, une condition de réussite, un échec jouable et une récompense idempotente.

| Épreuve proposée | Implantation | Objectif mesurable initial |
| --- | --- | --- |
| Démantèlement d'exercice | `stage_training_hangar` | Neutraliser trois modules inertes en 60 s ; aucune destruction gratuite de véhicule allié narratif |
| Couloir de horde | Arène de période validée | Trois vagues de six ennemis faibles ; maximum quatre simultanés ; fin après dernière vague |
| Ligne de précision | `stage_training_range` | Toucher 12 cibles, éviter 3 cibles interdites, 45 s |
| Recharge sous pression | Terrain de simulation | Cinq recharges parfaites sur huit essais ; munitions de test et score séparés |
| Extraction coordonnée | Zone de campagne vérifiée | Tenir deux positions à tour de rôle puis rejoindre une sortie réelle |
| Évacuation de ruche | Route Scorpio, lieu validé | Atteindre trois points de passage avant la menace ; aucun mélange Locuste/Essaim sans justification |
| Maîtrise du relais | Simulation Tag | Trois transferts sûrs et une assistance confirmée sans partenaire KO |
| Contrôle d'entité | Entraînement du kit retenu | Placer, ordonner puis rappeler l'entité sans doublon ni sortie de terrain |

La horde fragile traduit la référence arcade demandée ; elle n'implique pas que les ennemis de la campagne principale deviennent faibles. Les valeurs ci-dessus sont des réglages de première tranche à tester. Les ennemis exacts, leurs sprites et leurs attaques doivent être liés à l'épisode choisi.

La première visite peut être imposée pour l'apprentissage si elle ne bloque pas une situation narrative urgente. Les répétitions se lancent depuis l'entraînement ou l'espace d'archives. Échec : résultat enregistré, aucun coût irrécupérable indispensable, possibilité de reprendre ou de poursuivre la route. Les récompenses majeures possèdent une voie alternative lorsque l'épreuve est facultative.

## 11. Espace de déblocage : Archives de campagne

**« Archives de campagne » est un lieu d'interface original compatible, pas un site officiel ajouté au canon.** Sa première version cible une carte interactive reliée à la galerie ; un environnement explorable complet reste une étape ultérieure. Les dossiers représentent des périodes, sans prétendre qu'un soldat du premier Gears peut consulter des événements futurs.

Organisation proposée : accueil → terminal de missions → salle d'archives → casiers d'équipement. Le terminal donne accès au simulateur ; l'archive donne accès à la galerie. Un couloir représenté correspond à une connexion réelle, et chaque porte possède destination, condition, retour et état mémorisé. Le graphe sera vérifié avant une version jouable ; aucune porte décorative au milieu d'une salle ne représente un chargement arbitraire.

Les clés sont des autorisations de dossier ou des jetons d'exercice fictifs propres à la progression. Elles ne deviennent ni monnaies officielles de Sera ni ressources vendues sans décision explicite. Le joueur obtient un indice, remplit un objectif, revient au dossier et réclame un contenu identifié. Les acquisitions essentielles sont ciblées, sans tirage aléatoire imposé.

Le premier parcours conçu relie une épreuve de rechargement, un dossier de personnage, une récompense de présentation et une variante d'ambiance de simulation. Aucun prérequis ne dépend de l'objet qu'il ouvre. Le serveur ou la sauvegarde autoritaire enregistre l'identifiant de récompense avant l'animation de révélation, pour éviter perte ou duplication après interruption.

## 12. Slots verrouillés : quatre dimensions séparées

La présentation utilise un dossier militaire masqué et un verrou mécanique discret, avec silhouette noire lorsqu'elle est autorisée. Cette grammaire est une création UI. Elle ne prétend pas reproduire un menu officiel ni inventer un nouvel insigne canonique. Les familles Locustes et Essaim peuvent changer le matériau et le cadre ; l'état reste compréhensible sans couleur seule.

| Dimension | Valeurs minimales | Exemple d'explication |
| --- | --- | --- |
| Découverte | secret, indice, identifié | « Dossier non révélé » ou silhouette autorisée |
| Droit | aucun, à réclamer, permanent, temporaire, en attente, expiré | « Terminer l'épreuve » ou « Récompense disponible » |
| Installation | prêt, fichiers requis, erreur | « Contenu à installer » ; pas de faux verrou d'abonnement |
| Compatibilité | autorisé, interdit par règles | « Version incompatible avec ce chapitre » |

Ordre d'information : cacher les spoilers, expliquer l'obstacle qui empêche réellement la confirmation, proposer une action utile, puis rendre les autres conditions consultables. Un personnage non produit reste dans le catalogue de production et ne devient pas un faux contenu payant. Un costume obtenu avant le personnage reste acquis, avec dépendance visible. Le stage statique de confort ne doit pas être retiré au profit d'une version animée obligatoire.

Les catégories couvertes sont personnages, soutiens, costumes, palettes, stages, variantes, modes, défis, taunts et galerie. Le verrouillage d'un mode est limité aux routes narratives et défis avancés ; versus de base, réglages d'accessibilité, tutoriel et entraînement de base restent accessibles. La sélection d'un slot fermé ne bloque jamais la navigation ou le retour au menu.

## 13. Acquisitions, conditions ET/OU et sauvegarde

Chaque règle possède un identifiant stable, une description localisée, sa source de validation et une expression explicite de conditions. Les noms de ces règles sont des identifiants de conception nouveaux ; ils ne constituent pas encore des lignes du catalogue runtime.

| Règle proposée | Condition | Attribution |
| --- | --- | --- |
| `unlock.training.presentation` | Réussir la maîtrise de recharge OU terminer le tutoriel de remplacement | Présentation de simulation permanente |
| `unlock.delta.archive` | Finir une route Delta ET réclamer le dossier associé | Illustration originale compatible, permanente |
| `unlock.scorpio.challenge` | Terminer la route Scorpio | Défi bonus lié à la période |
| `unlock.simulation.ambience` | Gagner le défi de précision OU remplir un accomplissement équivalent | Variante de stage de simulation, collision inchangée |
| `unlock.supporter.cosmetic` | Acquisition permanente déjà obtenue OU droit temporaire valide du catalogue retenu | Même cosmétique, sources d'accès conservées séparément |

Les événements utiles contiennent `event_id`, `profile_id`, `rule_id`, `content_id`, version de règle et résultat. L'attribution est idempotente : répéter le même événement ne crée pas une seconde récompense et ne débite pas une seconde clé. Les conditions composites sont évaluées sans transformer un OU en ET. Les objectifs impossibles ou circulaires échouent au contrôle du catalogue.

La sauvegarde conserve découverte, progression, acquisitions et sources d'accès. Une annulation d'abonnement ne détruit ni une progression ni une acquisition définitive indépendante. Les migrations utilisent les identifiants stables ; renommer un costume ne le fait pas perdre. Une attribution rétroactive exige un événement réellement enregistré, sans inventer un historique de réussite.

## 14. Contenus de soutien et accès externe

La possibilité de contenus dédiés aux soutiens est retenue en conception. **Aucune offre commerciale, liaison Patreon, synchronisation de compte ou vérification de paiement n'est opérationnelle dans ce dépôt par cette livraison.** Les contenus précis et leur admissibilité restent à décider avant activation.

Trois modèles sont prévus : récompense permanente attribuée par événement confirmé ; catalogue temporaire utilisable pendant un droit valide ; lot de période doté de sa propre règle de permanence. Le texte affiché doit annoncer le modèle, les dépendances et les éventuelles autres voies d'obtention. Les récompenses de soutien conservent les mêmes statistiques, collisions et exigences de lisibilité que les autres costumes. Une création esthétique de soutien garde `original_compatible` ou `alternatif_crossover`, jamais `canon_atteste` par son seul accès.

Le client n'a pas autorité pour s'accorder un avantage. Une future intégration utilisera le parcours officiel du fournisseur, un service de confiance, des événements authentifiés et une réconciliation des doublons ou événements reçus dans le désordre. Le guide d'origine décrit cette architecture ; la documentation actuelle du fournisseur devra être vérifiée avant son implémentation. Aucun secret d'application n'appartient au jeu distribué.

État inconnu du fournisseur et droit expiré confirmé restent distincts. Une période payée encore valide ne cesse pas par supposition au clic d'annulation. Expirer une source temporaire laisse intactes les autres sources valides. Pour la première version future, l'accès hors ligne permanent reste disponible après acquisition ; un justificatif temporaire exigera une politique explicite et une durée à tester avant activation.

Annulation, déliaison, baisse de niveau, remboursement et suppression du compte du jeu sont des événements différents. Une déliaison arrête les vérifications futures selon la politique annoncée ; elle n'efface pas une récompense déjà acquise définitivement. Un remboursement confirmé ne retire que la source d'accès concernée selon la règle de l'offre : une seconde source permanente ou temporaire valide continue d'accorder l'accès. Une baisse de niveau s'applique à sa date effective vérifiée, sans révocation anticipée déduite d'un simple changement d'intitulé.

Un compte invité ne reçoit pas automatiquement les droits d'un autre profil présent sur l'appareil. Avant liaison, afficher le compte du jeu destinataire et la politique de transfert. Une même livraison permanente possède un identifiant d'attribution stable : déliaison, nouvelle liaison ou double événement ne peuvent la multiplier entre profils. Les transferts entre comptes restent interdits par défaut tant qu'une procédure explicite de récupération n'est pas définie. Ces règles sont des exigences de conception à tester, sans liaison active dans la livraison actuelle.

Une partie déjà autorisée conserve ses personnages, costumes et stage jusqu'au résultat. Le changement d'accès s'applique à la sélection suivante. Un costume devenu inaccessible reçoit un remplacement disponible avec explication ; sa préférence est gardée. En réseau, prévoir que l'adversaire puisse télécharger et afficher le stage choisi selon une politique de participation distincte du droit de le sélectionner. Sans cette distribution vérifiée, le stage ne peut entrer dans une rotation partagée.

## 15. Arènes connectées et transitions de boss

Chaque stage sépare quatre axes : présentation vivante/statique, interactions, dangers et transitions. Le réglage de confort ne désactive pas une collision en silence. Un danger conserve un signal lisible lorsqu'une animation est réduite. Le profil tournoi reste neutre selon la bible.

Une liaison possède `from_zone`, `to_zone`, point de départ, déclencheur, direction, état requis, positions d'arrivée, retour, coût et compatibilité. Deux fonds existants ne prouvent pas qu'ils sont physiquement adjacents. `stage_training_hangar` et `stage_training_range` peuvent former un lien original conçu dans le simulateur ; les lieux canoniques restent séparés tant qu'une référence topographique n'établit pas le passage.

Avant le départ : valider destination, assets, collision, droit de participation et configuration commune. Puis résoudre les impacts de la frame, figer la décision de transition, traiter les entités selon leur contrat et charger la zone. À l'arrivée : poser les deux membres actifs, conserver vie, munitions, jauges, compteurs de combo et temps selon les règles annoncées. Une destination absente annule le départ proprement avant prélèvement, avec retour jouable.

Un double déclenchement ne produit qu'une transition. Un KO simultané se résout selon le résultat du combat avant une coupe cosmétique. Une transition ne ressuscite pas une réserve et ne réarme pas une grenade déjà consommée. La présentation abrégée et le replay doivent retrouver le même état final.

Les boss gardent leurs contrats de taille et de phase. Une super d'équipe n'interrompt une phase que si la fenêtre de vulnérabilité l'autorise. Les modules détruits restent détruits, même après changement de caméra. Les simulations King Raven, Centaur et Silverback gardent leur statut non canonique de défi ; leur fin est une désactivation ou une fin d'exercice, comme prévu par la bible principale.

## 16. Fiches de production et suivi des assets

Les dix fiches de l'Extension 01 et les six de l'Extension 02 deviennent les modèles à remplir au fil de la production. Le présent chapitre fixe les contrats communs et les premières familles ; il ne prétend pas avoir rempli les fiches de chaque paire ou personnage.

| Fiche à ouvrir | Champs Gears indispensables | Livraison attendue |
| --- | --- | --- |
| Taunt/sélection | `character_id`, version, arme, côtés, interruption | Poses puis clips ; état séparé pour chaque étape |
| Assistance/relais | Participants, coût, états, dégâts réserve, sortie | Données et tests de simulation avant effets finaux |
| Duo/fin dramatique | Relation sourcée, époque, cible, stage, fallback | Storyboard, assets individuels, chorégraphie et critères |
| Entité/projectile | Propriétaire, variante, durée, collision, transition | Sprite indépendant puis comportement vérifié |
| Bonus/exploration | Lieux, graphe, objectif, reprise, récompense | Parcours mesurable et attribution unique |
| Slot/règle d'accès | Découverte, droits, fichiers, mode, ET/OU | Visuels et contrôle d'accès distingués |
| Offre/adaptateur | Modèle d'acquisition, événement, permanence | Contrat vérifié avant branchement externe |

Le nom de fichier proposé suit les conventions existantes avec sujet, version, costume, action et orientation. Les métadonnées gardent l'identifiant du catalogue, le prompt, les références, l'outil réellement utilisé, les dimensions, l'alpha, la révision et le statut de contrôle. Un sujet par image source ; pas de planche qui compterait simultanément comme six personnages finis.

Un master de stage ne clôt pas ses couches de parallaxe. Une pose ne clôt pas les animations de sélection ou de tag. Un slot avec cadenas ne clôt pas le combattant. Les statistiques distinguent conçu, produit, intégré, testé et validé visuellement ; le taux d'acquisition des joueurs est une autre métrique.

## 17. Acceptation et ordre des prochaines intégrations

Les scénarios ci-dessous sont des **tests à réaliser**, pas des tests exécutés dans V12. Ils complètent les 18 scénarios de l'Extension 01 et les 22 scénarios de l'Extension 02, conservés intégralement dans les sources. Le [rapport d'intégration](production/GUIDE_INTEGRATION_V12.md#traçabilité-des-40-cas-dacceptation-sources) associe explicitement chacun des 40 cas à une section de ce chapitre ; tous restent non exécutés dans ce sous-lot documentaire.

| Groupe | Cas bloquant avant livraison jouable |
| --- | --- |
| Sélection | Navigation rapide, annulation, costume changé, ancien son invalidé, aucun spoiler secret |
| Commandes | Assistance et tag simultanés ; dernière ressource dépensée une seule fois ; refus sans débit |
| Réserve | Soutien touché à l'arrivée, KO, retour, relais automatique gratuit, aucun membre dupliqué |
| Combo | Tag et objet posé conservent scaling/rebonds ; aucune boucle de recharge de kit |
| Super | Touche/garde/échec ; cible mécanique/géante ; partenaire indisponible ; sortie cohérente |
| Clash | Succès/échec/égalité, absence de réponse, variante accessible et projectile tiers |
| Transition | Destination absente, double départ, KO, objets persistants, replay et arrivée sûre |
| Bonus | Réussite/échec/reprise ; limite de quatre ennemis ; récompense unique |
| Déblocage | ET/OU, costume acquis avant personnage, assets manquants, sauvegarde interrompue |
| Accès externe | Expiration, source permanente restante, événement doublé, service indisponible, match en cours |
| Lore/visuel | Costume et époque corrects, source d'arme, asymétries, duo narrativement disponible |

Ordre de travail : poursuivre les manquants fixes contrôlés ; préparer les fiches de deux combattants et une arène ; intégrer leur cycle de sélection et un taunt ; valider une assistance et un relais ; ajouter une entité persistante ; éprouver une super duo et un clash ; construire un bonus et un dossier de déblocage ; étendre les paires et les routes après validation. Le réseau et les droits externes nécessitent des contrats d'autorité avant leurs premières intégrations, même si leur livraison vient plus tard.

Le premier objectif jouable de ces extensions est volontairement borné à Marcus/Dom en simulation avec une assistance, un tag, une super générique, un bonus de recharge et une récompense de présentation. Il reste un jalon à réaliser. La couverture des trois documents est acquise lorsque les copies et la matrice sont présentes ; la couverture des fonctionnalités ne l'est qu'après les intégrations et contrôles ci-dessus.

## 18. Sources officielles vérifiées pour ce chapitre

Consultation : 27 novembre 2026. Ces sources étayent les faits indiqués ; elles ne valident ni les règles chiffrées de l'adaptation, ni les assets générés, ni les nouvelles chorégraphies.

- **GX01** — The Coalition, [Gears of War](https://www.gearsofwar.com/en-us/games/gears-of-war/). Marcus et Dom en campagne coopérative ; finitions associées au combat de la série.
- **GX02** — The Coalition, [The 2020 Gearsmas Holiday Gift Guide](https://www.gearsofwar.com/en-us/news/2020-gearsmas-holiday-gift-guide/), 3 décembre 2020. Identification des quatre membres du groupe Delta original.
- **GX03** — The Coalition, [Gears of War Judgment](https://www.gearsofwar.com/en-us/games/gears-of-war-judgment/). Baird et Kilo Squad ; visuel nommé Baird, Cole, Paduk et Sofia.
- **GX04** — The Coalition, [Developer Blog: Characters](https://www.gearsofwar.com/en-us/news/dev-blog-characters/), 17 avril 2020. Gabe, Sid et Mikayla, relations de départ et fonctions dans Tactics.
- **GX05** — The Coalition, [Gears of War 4](https://www.gearsofwar.com/en-us/games/gears-of-war-4/). JD, Kait et Del dans la campagne.
- **GX06** — The Coalition, [Hivebusters DLC is Now Available](https://www.gearsofwar.com/en-us/news/hivebusters/), 14 décembre 2020. Scorpio, Galangi et distinction de son cadre de campagne.
- **GX07** — Xbox Wire, [Gears 5: Hivebusters Expansion Arrives December 15](https://news.xbox.com/en-us/2020/12/08/gears-5-hivebusters-arrives-december-15/), 8 décembre 2020. Electroblade de Lahni, Barrier de Mac et Resupply de Keegan dans la liste des accomplissements de campagne.
- **GX08** — Xbox Wire, [Gears 5 at gamescom 2019](https://news.xbox.com/en-us/2019/08/19/gears-5-at-gamescom-2019/), 19 août 2019. JACK de soutien dans la Horde ; les capacités décrites dans ce mode ne sont pas étendues automatiquement à toutes les périodes.

Les références et limites visuelles propres aux autres personnages restent dans `docs/references/` et les fiches de production. Toute nouvelle mécanique conserve sa mention d'adaptation, même lorsque tous ses acteurs sont canoniques.
