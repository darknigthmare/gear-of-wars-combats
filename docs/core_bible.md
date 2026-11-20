# Gears of War Combats

## Bible de conception du mode de combat 2D

Version 1 du 19 novembre 2026. Projet de Darknigthmare. Cette bible définit un mode annexe autonome de combat de profil, compatible avec une future intégration dans un jeu Gears plus large. Elle couvre les systèmes de combat, les personnages, les parcours narratifs, les tournois, les exécutions, les arènes et les affrontements contre les créatures et les véhicules de grande taille.

Le résultat recherché est un jeu de combat lourd, précis et lisible, dont les personnages gardent leurs visages, leurs silhouettes, leurs armes et leur époque. La simulation tourne à 60 pas par seconde. Les tirs créent des décisions de distance et de rechargement ; le corps à corps convertit ces décisions en combos courts et violents. Les boss conservent leur présence monumentale grâce à un cadrage et à des objectifs spécifiques.

Trois statuts accompagnent le contenu : une référence canonique décrit ce qui provient des jeux ; une adaptation décrit une règle ou une scène écrite pour ce projet ; une réalisation décrit un fichier ou une fonctionnalité effectivement livré. Les nombres de frames, les dégâts, les jauges, les dialogues et les routes de combat de cette bible sont des propositions de conception. Ils ne constituent pas des données officielles des jeux Gears.

### Livrables et lecture

La bible principale présente les décisions et les règles. Les annexes détaillent le roster, les coups, les 36 parcours arcade, les 24 boss, les 24 stages et les 12 chapitres. Le classeur de production permet de filtrer les entrées et de suivre les assets. Les fichiers JSON constituent les données structurées. Le prototype HTML permet d'essayer un sous-ensemble des mécaniques ; la disponibilité de chaque fonction est indiquée dans son fichier de lecture.

Un combattant inscrit au roster n'est pas compté comme animé ou intégré. Un visuel généré n'est pas compté comme un costume terminé. Un décor complet ne vaut pas livraison de ses couches de parallaxe. Ces distinctions structurent le suivi de production et évitent de masquer le travail restant.

## 1 Vision et identité

### Un combat reconnaissable dès la silhouette

Le style visuel vise des sprites 2D UHD, grands à l'écran, aux matériaux réalistes : métal usé, tissu épais, peau marquée, masse des armures COG et anatomies locustes. Les proportions peuvent être transposées pour la lisibilité, mais ni le visage ni le dessin des armes ne doivent devenir génériques. Le zoom, les hitboxes et les règles changent avant de modifier l'identité d'un personnage.

L'ambiance garde le poids des Gears : pas de course aérienne flottante ni d'effets colorés qui cachent les corps. Les mouvements rapides proviennent des roulades, des changements d'appui et des déplacements courts. Une lourde attaque ratée doit se lire dans le retour de l'arme et le temps nécessaire pour retrouver la garde.

Les premiers jeux, leurs remasters et leurs rééditions fournissent des références distinctes. Une amélioration de résolution ne crée pas automatiquement un costume supplémentaire. L'âge de Marcus, le type de Lancer, les protections de Baird et les équipements de Kait restent attachés à une version explicitement nommée. La page officielle de la série et les pages des jeux servent de point d'entrée aux références [S01 à S07].

### Les quatre objectifs de production

- Un duel doit être agréable sans utiliser d'arme à feu : normals, garde, projection, punition et déplacements fonctionnent seuls.
- Les armes doivent apporter une cadence et un risque propres : aucune ne se résume à un projectile interchangeable.
- Chaque boss doit poser une question différente : provoquer une charge, dégager un point faible, casser un équipement, gérer l'altitude ou survivre à un déplacement du terrain.
- Chaque élément présenté comme fidèle doit disposer d'une référence d'épisode, d'un contrôle de silhouette et d'un état de validation consultable.

## 2 Périmètre de contenu

### Corpus et continuités

Le corpus de départ comprend Gears of War, Gears of War 2, Gears of War 3, Judgment, Gears of War 4, Gears 5, Hivebusters et Gears Tactics. Ultimate Edition et Reloaded servent de variantes de rendu du premier épisode. E-Day dispose d'une section de références dédiée ; seuls les personnages, armes, lieux et détails attestés entrent dans les fiches finalisées. L'annonce officielle situe E-Day quatorze ans avant le premier Gears [S02].

Les comics et romans peuvent alimenter des extensions documentées. Ils ne servent pas à inventer sans preuve la géométrie d'un costume qui n'a jamais été montré. Les apparitions promotionnelles, invités et collaborations restent dans une catégorie facultative, séparée du roster Gears. Un futur pack ne doit pas occuper la place d'une animation indispensable à un personnage déjà promis.

### Lots jouables

Le noyau de conception contient Marcus, Dom, Baird, Cole, Anya, Kait, RAAM, Skorge, Myrrah, un Drone locuste, un Kantus et un Garde Theron. Ils couvrent les principaux besoins de combat : polyvalence, pression, mobilité, pose d'outils, charge, tirs préparés, commandement et contrôle de l'espace. Vingt-quatre combattants supplémentaires sont spécifiés dans l'annexe roster.

Le premier lot d'intégration doit se limiter à quatre combattants complètement animés, deux stages réellement découpés et deux boss complets. Il valide le langage du jeu avant l'extension à douze puis trente-six combattants. La priorité des sprites n'est donc pas le nombre de portraits : ce sont les poses de combat, les transitions, les impacts et les actions réellement utilisables.

### Familles de modes

| Mode | Structure prévue | Objectif principal |
| --- | --- | --- |
| Histoire | Anthologie en 12 chapitres | Rejouer les conflits en gardant leurs époques |
| Arcade | 5 duels, rival, boss, duel final, ending | Donner une route propre à chaque combattant |
| Versus | Local et IA, puis réseau | Duel 1 contre 1 aux règles stables |
| Tournoi | 8, 16 ou 32 entrants | Enchaîner les matchs et suivre le tableau |
| Boss Battle | Rencontre choisie | Maîtriser une créature ou un véhicule |
| Boss Rush | Suites de 3, 6 ou 12 rencontres | Gérer les ressources sur la durée |
| Horde Combat | Vagues sur une arène | Pression PvE et coopération |
| Défis | Combos, défense, rechargement | Apprendre une mécanique à la fois |
| Entraînement | Situation configurable | Tester une hypothèse de combat |
| Galerie | Costumes, scènes et sources | Consulter le contenu débloqué et ses versions |

## 3 Commandes et vocabulaire

### Schéma de combat cible

Quatre boutons principaux donnent accès au léger L, au moyen M, au lourd H et à l'action d'arme W. Un bouton de mobilité E déclenche l'esquive ou l'interaction de couverture selon le mode. R lance ou confirme le rechargement. L plus M effectue une projection ; M plus H dépense deux barres pour un briseur ; H plus W déclenche la super si ses conditions sont réunies. Des raccourcis reconfigurables reproduisent ces combinaisons.

La garde du jeu cible utilise la direction opposée à l'adversaire : arrière pour les attaques hautes et médianes, bas arrière pour les basses. Le prototype peut employer un bouton explicite de garde afin d'isoler le test de la défense ; cette différence doit rester visible dans ses commandes. Les directions sont toujours relatives au côté de l'adversaire.

La notation numérique suit le pavé de neuf directions : 5 neutre, 6 avant, 4 arrière, 2 bas, 8 haut. Une commande 236W signifie bas, diagonale avant, avant, puis arme. j.L signifie un léger aérien. Le symbole > représente une liaison après récupération, et xx représente une annulation. Une fiche de combo doit distinguer ces deux situations.

### Commandes modernes et techniques

Un schéma moderne donne un accès direction plus bouton aux spéciaux. Il produit les mêmes actions, avec les mêmes dégâts, délais et coûts. Les commandes techniques donnent accès aux variantes de trajectoire, sans bonus caché de puissance. Les macros d'accessibilité peuvent regrouper des entrées simultanées ; elles n'enchaînent pas automatiquement plusieurs décisions de combat.

Le clavier doit accepter ZQSD et WASD, les flèches et une remappage complet. Le tactile présente déplacement, garde, attaque, tir, esquive, rechargement et spécial avec des zones de contact distinctes. Les actions maintenues se relâchent sur perte de focus ou interruption du pointeur. La manette affiche les commandes de la famille détectée et prévoit une zone morte réglable.

## 4 Règles du duel

### Match et espace de jeu

Le réglage standard est deux manches gagnantes de 99 secondes. La vie est réinitialisée à chaque manche. La jauge de super est conservée dans le match, plafonnée à trois barres, puis réinitialisée au match suivant. L'égalité simultanée donne une manche aux deux joueurs ; si cela termine le match pour les deux, une manche de départage complète est jouée. Une égalité au temps compare le pourcentage de vie restante, puis déclenche le même départage si les valeurs sont identiques.

La simulation utilise une unité de distance commune et un plan de collision unique. La caméra suit le milieu des personnages, avec un zoom limité pour que les mains et les armes restent lisibles. Les joueurs ne peuvent pas sortir du cadre en reculant. Le sol reste horizontal ; les variations de relief du décor sont visuelles dans les stages de tournoi.

Les personnages ont une masse et une vitesse distinctes, mais aucun costume ne modifie une statistique. Un masque ou une cape n'élargit pas automatiquement la zone de dégâts. Les grandes armes possèdent leurs propres hitboxes et leurs propres zones exposées quand une punition est voulue. Les ailes ou montures des personnages ne deviennent pas invulnérables par simple choix de sprite.

### Attaques et garde

Chaque coup possède démarrage, activité, récupération, dégâts, effet en garde, effet au contact, hauteur, portée, niveau d'armure et autorisations d'annulation. Une attaque rapide de référence démarre en 6 frames ; un lourd de punition démarre entre 16 et 22 frames. Ces valeurs servent à construire les premiers tests, puis sont ajustées à partir de parties enregistrées.

La garde bloque les coups de la hauteur correspondante et consomme une jauge de posture de 100 points. Après 45 frames sans attaque reçue ni garde tenue, cette jauge récupère à 15 points par seconde. Atteindre zéro provoque une rupture de 45 frames, puis rend 60 points. Le réglage évite de transformer chaque défense en défaite inévitable : la garde parfaite, disponible pendant les trois premières frames d'une garde correcte, réduit fortement la perte de posture sans donner une super garantie.

Les projectiles infligent au maximum 10 % de leurs dégâts en garde. Le chip ne tue pas en duel standard : il laisse un point de vie. Les coups de corps à corps ne font pas de chip sauf mention explicite d'un état renforcé. Le boss peut employer une autre règle si son contrat l'affiche avant le combat.

### Projection et défense rapprochée

La projection normale exige une courte distance, un démarrage de 8 frames et une fenêtre de déchoppe de 12 frames. Une saisie spéciale est plus lente, plus dommageable et ne partage pas nécessairement cette déchoppe ; elle doit posséder une réponse claire par saut, recul ou interruption. Un personnage au sol conserve une protection temporaire contre les projections pendant sa relevée.

Une roulade coûte 25 points d'endurance sur 100. Son déplacement couvre une longueur de corps, avec une brève fenêtre d'évitement au milieu et une récupération punissable. Elle n'annule pas gratuitement le début d'un gros coup. L'endurance commence à remonter 60 frames après la dernière dépense. Des frais supplémentaires ou une récupération longue empêchent les allers-retours invulnérables en boucle.

### Combos et limitation des boucles

La chaîne universelle L xx M xx H facilite l'entrée en matière. Les normals indiqués peuvent s'annuler en spécial, puis en super pour une dépense définie. Les autres liaisons doivent être prouvées par l'avantage au contact. Un avantage de +8 ne garantit qu'un coup suivant dont le démarrage tient dans cette fenêtre, avec portée suffisante et règles de recul compatibles.

L'échelle de dégâts proposée suit 100 %, 90 %, 80 %, 70 %, 60 %, 50 %, 40 %, puis 35 % pour le huitième impact et les suivants. Les dégâts de chaque paquet sont arrondis à l'entier le plus proche avant leur addition. Une super garde un plancher de 45 %. Une seule extension de rebond mural et une seule remise au sol relançable sont permises dans la même séquence. La gravité de juggle augmente à chaque lancement. Le système identifie la séquence, même si une animation de changement d'arme la traverse.

Un briseur coûte deux barres, agit après le premier impact confirmé et repousse les deux personnages vers le neutre. Il ne fonctionne pas pendant une projection, une exécution ou une cinématique de boss. Il donne une sortie coûteuse sans rendre tous les combos inutiles. Une option d'entraînement permet d'enregistrer la réponse du défenseur après chaque coup pour vérifier les vrais intervalles.

## 5 Armes et rechargement actif

### Traduire la sensation de Gears

L'arme est un engagement de rythme. Le Lancer pousse à moyenne distance, le Gnasher récompense la proximité, le Longshot impose une préparation, le Torque Bow menace après une charge lisible, le Boomshot punit les regroupements et le Hammer of Dawn demande une condition de ciblage. Les fiches fixent l'arme de référence du personnage ; un skin ne remplace pas discrètement un modèle par un autre.

Les chargeurs sont des valeurs de combat propres à l'adaptation. Une rafale de Lancer utilise une unité de munition de jeu, distincte du nombre de balles représentées à l'écran. Les nombres du HUD ne doivent donc jamais être présentés comme les capacités canoniques des armes. Les attaques sans munition conservent une solution de corps à corps ; le joueur n'est pas condamné à attendre.

### Fenêtre de rechargement

Le rechargement normal cible 72 frames. Une seconde pression sur R entre les frames 34 et 43 confirme la fenêtre parfaite ; les frames 27 à 33 et 44 à 50 constituent la fenêtre sûre. Une pression en dehors de ces fenêtres ajoute 30 frames de blocage. Les bornes sont inclusives et testées au pas de simulation, indépendamment du nombre d'images affichées.

La réussite parfaite termine le chargement à la frame 44 et renforce les deux prochaines actions d'arme avec un coefficient de dégâts de 1,10. La réussite sûre termine à la frame 60. Ne pas confirmer termine à la frame 72. Une tentative ratée ne peut pas être répétée pendant le même chargement. Aucun résultat n'augmente les points de vie ou la fréquence de simulation.

Être frappé pendant les 18 premières frames interrompt le rechargement sans remplir le chargeur. Une fois le chargeur verrouillé, un coup peut interrompre la pose mais conserve l'état de munition acquis. Les frames nécessaires à cette séparation sont explicitement enregistrées. Les coups renforcés perdus après avoir raté la cible ne sont pas remboursés.

### Éviter le duel de tirs immobile

Les tirs présentent un départ et une récupération visibles. Reculer au fond de l'arène ne crée pas de munition supplémentaire. La garde, l'esquive et les trajectoires basses donnent plusieurs réponses. Les supers capables de traverser les projectiles ont un coût et une anticipation lisibles. Les grenades ne doivent pas ajouter un hasard imprévisible : leur arc, leur délai et leur zone d'explosion restent constants pour une entrée identique.

## 6 Exécutions et présentation des fins de combat

### Une conclusion liée au personnage

Chaque combattant reçoit deux exécutions de signature et une finition rapide. Les versions choisies se fondent sur son arme, sa force et sa personnalité. Le Lancer, le couteau, le Torque Bow, les outils lourds ou les pouvoirs locustes suivent des chorégraphies différentes. Les noms et séquences proposés pour ce jeu restent des créations d'adaptation même si l'inspiration vient d'exécutions connues [S03].

L'exécution n'est disponible qu'après la dernière manche gagnée, pendant une fenêtre de 180 frames. Le perdant est en état neutralisé, le vainqueur reçoit une indication discrète et peut choisir la finition ou une victoire immédiate. Rater la commande conclut le match normalement. Elle n'ajoute ni dégâts décisifs ni classement bonus compétitif.

Les rencontres de boss ont des finitions adaptées aux parties détruites. Un personnage ne doit pas soulever une créature géante comme un humanoïde. Le coup final peut déclencher une chute, l'arrêt d'un moteur, une retraite, un effondrement ou une destruction d'équipement. Les véhicules alliés d'entraînement concluent par une désactivation et une extraction.

### Caméra et options

La caméra conserve le profil jusqu'à l'impact confirmé. Une courte coupe permet la mise en scène, puis retourne à une pose de victoire cohérente. Les adversaires mécaniques, Locustes, Swarm et humains utilisent des points d'attache distincts. Les animations de saisie ne partagent pas un squelette unique sans adaptation de taille.

Un réglage de violence réduite remplace les détails graphiques par des effets de choc et une coupe de caméra sans modifier le gagnant ni la durée maximale. Un réglage de flash et de secousse réduit l'intensité des effets. Les deux joueurs peuvent demander de passer la séquence ; en tournoi, le profil peut imposer la finition courte pour conserver le rythme du tableau.

## 7 Histoire et parcours arcade

### Une anthologie jouable

L'histoire relie les jeux par des dossiers de bataille et des souvenirs datés. Chaque chapitre indique son époque, son point de vue et son objectif. Un combat d'entraînement entre alliés est nommé comme tel. Une rencontre impossible entre deux époques appartient à l'exhibition ou à une route alternative explicitement signalée. La campagne principale n'a pas besoin d'un voyage temporel inventé pour réunir son roster.

Les douze chapitres prévus sont détaillés dans l'annexe campagne. Chaque chapitre contient une introduction, une première situation de duel, un objectif différent, une confrontation personnelle, une rencontre majeure et une sortie de scène. Les cinématiques sont conçues en portraits et plans fixes animables pour rendre la production réaliste, avec possibilité de remplacer ensuite un passage par une séquence complète.

### Structure d'une route individuelle

Une route arcade comporte cinq duels de progression, dont une rencontre à contrainte, un rival, un boss, un duel final et un ending. Les huit combats peuvent traverser plusieurs époques dans ce mode hors continuité. Le rival bénéficie de deux répliques originales, d'une introduction contextualisée et d'une variante si le joueur a déjà terminé la route. La fin présente une conséquence personnelle et une image dédiée ; le résultat ne réécrit pas automatiquement le canon de la campagne.

Chaque route définit des opposants par identifiants, un costume compatible, une arène, un enjeu de rivalité et une fin. L'IA s'adapte aux actions apprises au cours de la route plutôt qu'à la lecture instantanée des boutons. La difficulté augmente le nombre de réponses et la qualité des décisions, avec un délai minimum documenté. Elle n'augmente pas silencieusement les dégâts adverses dans le profil compétitif.

Les 36 routes de l'annexe sont des synopsis prêts à développer en scripts de mise en scène. Les textes complets de doublage, les enregistrements audio et les illustrations d'ending ne sont pas marqués produits tant que leurs fichiers n'existent pas.

## 8 Tournois et jeu compétitif

### Gestion du tableau

Le joueur choisit 8, 16 ou 32 participants, humains locaux ou IA. Les doublons de personnage sont permis ; chaque entrant garde son identifiant de participant. Le seeding accepte l'ordre choisi, un mélange déterministe à graine ou un classement renseigné. Un forfait ne génère pas un faux combat ni un score de performance.

L'élimination simple nécessite N moins 1 matchs. La double élimination nécessite 2N moins 2 matchs sans réinitialisation de grande finale, et 2N moins 1 si le vainqueur du tableau bas inflige sa première défaite au vainqueur du tableau haut. Pour 16 entrants, cela donne 30 ou 31 matchs. Le moteur doit conserver deux compteurs de défaites et les dépendances de chaque rencontre, pas seulement afficher un arbre décoratif.

Les parties se jouent en deux manches gagnantes. Un set standard utilise deux matchs gagnants ; les finales peuvent en exiger trois. Le perdant peut changer de personnage. Le vainqueur conserve son personnage, sauf variante du règlement choisie avant l'événement. Les changements de costume ne modifient pas les hitboxes.

### Stages et intégrité d'une partie

Le profil tournoi impose une liste de stages sans dégâts de décor, sans objets aléatoires et sans avant-plan opaque. Le côté de départ alterne à chaque match. Les résultats enregistrent version du moteur, profil de règles, identifiants, seed et entrée de chaque joueur. Une mise à jour de la base de coups ne prétend pas conserver la compatibilité d'anciens replays si les règles ont changé.

Le réseau futur prévoit simulation déterministe et rollback. Le prototype livré reste local contre l'IA. La synchronisation réseau doit être une étape testée séparément : latence, rollback de hit-stop, projectiles, chargements et changements de phase ne sont pas résolus par la simple présence d'un bouton multijoueur.

## 9 Boss Battle

### Contrat d'une rencontre

Un boss possède une machine d'états distincte de celle d'un combattant. Le contrat définit l'échelle à l'écran, les zones attaquables, les points faibles, l'attaque en cours, sa préparation, les transitions et la fin. La caméra maintient un indicateur de l'attaque hors champ et garde le joueur visible. La grande taille ne se traduit jamais par une collision corporelle couvrant tout l'écran en permanence.

Une rencontre standard vise trois phases sans intervalle manquant : au-dessus de 66 %, au-dessus de 33 % et jusqu’à 66 %, puis à 33 % ou moins de vie. Ce découpage est une règle d'adaptation et peut varier pour un combat à objectifs. La transition donne un bref moment de lecture, retire les anciens marqueurs et prépare une nouvelle menace. Elle ne peut pas interrompre arbitrairement un combo de récompense sans prévenir le joueur.

Les attaques létales disposent d'une anticipation d'au moins 45 frames en difficulté normale. Une attaque rapide mineure peut avoir un signal plus court, mais ne doit pas demander une esquive impossible. Chaque menace combine une forme au sol, un mouvement du boss et un son ; la couleur seule n'est jamais l'unique indication.

### Créatures géantes

La Berserker impose d'appâter sa charge, d'esquiver et de profiter d'une exposition définie. Le Corpser utilise des pattes et des zones de frappe clairement séparées. Le Brumak présente des armes et parties ciblables. Le Reaver change d'altitude. Le Swarmak expose des zones vulnérables. Le Kraken utilise plusieurs éléments du décor pour renouveler le combat. Chaque fiche précise les écarts entre la référence canonique et la règle 2D retenue.

Le blog officiel de Gears Tactics décrit le principe des boss comme des problèmes de positionnement, avec des attaques annoncées, des parties protégées et des changements de phase [S08]. Cette inspiration convient à l'adaptation, sans recopier automatiquement la durée d'un tour dans un moteur de combat en temps réel.

### Véhicules et machines

Un adversaire aérien dispose d'un point de visée accessible au tir, d'un passage bas punissable au corps à corps et d'une séquence d'équipement à neutraliser. Les attaques de missiles et de mitraillage occupent des zones distinctes. Détruire une arme réduit la menace correspondante ; l'interface reflète immédiatement cette conséquence.

Le King Raven, le Centaur et le Silverback peuvent être sélectionnés en simulation. Leur opposition à un Gear n'est pas présentée comme un fait de la campagne. Les silhouettes, moteurs, armes et points d'accès doivent venir de leur version de jeu, tandis que les patterns d'entraînement sont créés pour ce mode. Les dégâts fictifs se concluent par un arrêt des systèmes ou un abandon de l'exercice.

### Solo et coopération

Le solo offre toutes les réponses indispensables, y compris les interactions initialement imaginées pour plusieurs joueurs. Le coopératif à deux partage les consommables de rencontre et permet une réanimation limitée. La vie cible du boss passe à 1,65 fois la valeur solo ; les dégâts des attaques restent identiques. Les menaces parallèles augmentent la coordination sans supprimer les ouvertures.

Une saisie coopérative comporte un temps d'intervention suffisamment long pour le partenaire. En solo, la même attaque devient une épreuve d'esquive ou une fuite par action lisible, jamais une mort automatique faute de second joueur. Un nombre maximum d'ennemis supplémentaires évite la saturation visuelle.

### Contrats et récompenses

Les contrats proposent victoire simple, absence de mise à terre, parties détruites dans un ordre choisi ou temps cible. La note associe temps, dégâts reçus et objectifs remplis avec des poids visibles. Les rechargements parfaits n'accordent un bonus que s'ils participent à des actions pertinentes ; répéter une action sans danger ne permet pas de cultiver un score infini.

Les récompenses sont des illustrations, variantes esthétiques, entrées de galerie et titres. Elles n'augmentent pas les dégâts en versus. Le Boss Rush conserve une fraction de vie et offre un choix entre soin, réserve de munitions ou récupération de jauge ; les décisions et les effets sont affichés avant confirmation.

## 10 Arènes en parallaxe

### Structure d'un stage

Chaque arène se compose de six couches : ciel, horizon, architecture, plan moyen, sol jouable et avant-plan. Les effets sont gérés séparément par le moteur. Les facteurs de déplacement typiques sont 0,04 ; 0,15 ; 0,36 ; 0,65 ; 1,00 ; 1,12. Ils décrivent le déplacement relatif à la caméra et non une profondeur physique mesurée dans l'univers.

La version tournoi garde le plan de jeu dégagé et réduit les éléments passants. La version spectacle peut présenter un événement déterministe : effondrement lointain, passage de véhicule, changement de lumière ou pluie. Les collisions de danger ne sont actives que dans les modes qui les annoncent. L'évolution visuelle d'une manche ne modifie pas la géométrie compétitive.

Chaque couche exportée garde les mêmes dimensions logiques, le même horizon et la même origine. Les débords latéraux sont prévus dès la composition. Une image aplatie peut servir d'illustration ou de prototype ; les six couches doivent être exportées séparément pour fournir une profondeur indépendante. Les zones cachées derrière un objet doivent être redessinées pour permettre une vraie parallaxe.

### Familles d'environnements

Le catalogue couvre les ruines urbaines d'Ephyra, les installations de la COG, les souterrains locustes, les forteresses, les combats sur transport, les zones gelées, les étendues désertiques et les îles volcaniques de Galangi. Les 24 fiches donnent épisode, heure, ambiance, couches et traitement tournoi. Le décor de chaque boss prend en charge ses points faibles sans réutiliser automatiquement un stage de duel trop petit.

Les contrastes sont contrôlés sur des silhouettes COG bleues, locustes sombres et Swarm rougeâtres. La poussière, la pluie et la fumée ne doivent pas cacher le démarrage d'un coup. Le réglage d'accessibilité renforce le contour des combattants et réduit les particules, sans modifier leurs positions ni leurs fenêtres d'attaque.

## 11 Direction artistique et fidélité

### Validation par version

Une fiche de référence comporte personnage, épisode, scène ou skin, angle, arme, source et date d'accès. Pour valider un asset, on contrôle le visage, la silhouette, l'armure, l'arme, les matériaux, les proportions relatives et la lisibilité de profil. Une image séduisante qui change la forme du Lancer ou l'âge du personnage reste à corriger.

Le terme fidélité 1 pour 1 exprime l'objectif de correspondance avec la référence choisie. Une génération ne prouve pas à elle seule cette correspondance. Les premiers visuels livrés portent donc le statut « généré, contrôle canon à finaliser ». La validation finale demande une comparaison côte à côte avec des captures déterminées, puis une correction ciblée de chaque écart.

La source d'un personnage ne suffit pas à certifier tous ses détails. Une page qui confirme la présence de Lahni dans Hivebusters ne valide pas les coutures exactes de son uniforme. Les cases de source distinguent identité confirmée, équipement confirmé et détail visuel à contrôler.

### Un asset par image

Chaque image de personnage contient un seul personnage, une seule pose et un seul costume. Les variantes casque, sans casque, arme différente et côté opposé sont des fichiers distincts. Un atlas de runtime peut regrouper les fichiers après validation, mais les originaux restent individuels.

Une pose isolée n'est pas une animation. L'animation exige des transitions cohérentes, une trajectoire des mains, un déplacement du poids et des points d'appui constants. Une translation ou une rotation globale de l'image permet de tester une sensation, sans être comptée comme un nouveau dessin d'animation.

Le retournement horizontal n'est pas la solution finale pour les tatouages, épaulières, mains dominantes ou mécanismes asymétriques. Les métadonnées indiquent si le miroir est autorisé. Les personnages majeurs nécessitent une série pour chaque orientation dès qu'une asymétrie significative est visible.

### Tailles et export

Les masters de combattants visent un canevas de 1536 par 1536 ou 1024 par 1536 selon la silhouette. Le runtime utilise un pivot aux pieds, un rectangle de cadrage et une hauteur logique propres au personnage. Un géant ne doit pas être réduit à la hauteur d'un soldat pour partager le même canevas visible. Les mesures réelles des premiers fichiers sont inscrites dans le manifeste.

Les exports PNG conservent l'alpha. Le contour ne porte ni halo blanc ni ombre de sol peinte qui flotterait pendant un saut. Les VFX de tir, fumée, sang optionnel, kryll ou électricité sont des assets séparés. Les empreintes et ombres au sol appartiennent au moteur.

## 12 Programme d'animation

### États indispensables par combattant

Le lot d'animation complet vise 26 états de locomotion et de combat communs : entrée, attente, marche avant, marche arrière, départ de course, course, arrêt, accroupissement, saut, chute, atterrissage, roulade, garde haute, garde basse, impact léger, impact lourd, chute au sol, relevée, étourdissement, projection, déchoppe, rechargement, raté de rechargement, provocation, victoire et défaite. Les normals et spéciaux ajoutent leurs propres états.

La priorité est l'anticipation, l'action, la récupération et le retour à la pose neutre. Un lourd spectaculaire sans récupération visible est injouable. Les armes attachées aux mains gardent leurs points de contact. Les douilles, chargeurs et projectiles reviennent au moteur comme événements, afin de ne pas dupliquer un objet déjà dessiné dans l'image.

Le budget indicatif du profil complet est de 272 dessins pour les actions communes, 96 pour les normals, 72 pour les quatre spéciaux, 48 pour deux supers et 64 pour deux exécutions : 552 dessins par orientation et par costume entièrement redessiné. Cette estimation doit être recalculée à partir du plan réel de chaque personnage. Une reprise partielle de costume ne vaut pas duplication automatique du budget complet.

### Événements d'animation

Chaque clip associe un numéro de frame à ses événements : apparition de hitbox, ouverture d'annulation, émission de projectile, consommation de munition, validation de chargeur, effet sonore, déplacement et fin. Les hitboxes n'ont pas besoin de correspondre au nombre de dessins ; un dessin peut durer plusieurs pas de simulation.

Le fichier d'animation décrit fréquence, boucle, pivots, rectangles de source et événements. Les noms restent stables : personnage, version, costume, côté, action, numéro. Les corrections remplacent une version d'asset par une nouvelle révision ; elles ne changent pas l'identifiant de gameplay.

## 13 Son et mise en scène

Le mix distingue attaque légère, métal, chair, pierre, mécanique, armes et signaux de boss. Les sons indispensables à la décision restent audibles sous la musique et les dialogues. Une limite de voix simultanées réserve des canaux au rechargement et aux alertes majeures. Les directions hors champ sont indiquées par spatialisation et sous-titres d'action optionnels.

Les thèmes musicaux sont à produire ou à importer depuis des fichiers autorisés fournis pour le projet. Le pack initial ne prétend pas contenir les enregistrements officiels. Les textes originaux de rivalité peuvent être sous-titrés avant tout doublage. Une voix ne doit pas être attribuée à un acteur officiel sans enregistrement correspondant.

Chaque personnage reçoit des sons de déplacement, d'effort, de douleur, de provocation, de victoire et d'exécution. Les boss ont un signal sonore propre à chaque grande attaque. Le rechargement parfait possède une confirmation nette, accompagnée d'un indicateur visuel pour les personnes jouant sans son.

## 14 Interface et accessibilité

La sélection affiche personnage, variante d'époque, costume, difficulté d'apprentissage, style de combat et source d'équipement. Le même portrait ne sert pas à faire croire que toutes les variantes sont illustrées. Les éléments non produits restent consultables dans le catalogue avec leur statut, puis accessibles dans le jeu seulement lorsqu'ils fonctionnent.

Le HUD de duel contient vie, jauge de super, munitions, posture, manches et temps. Le HUD de boss ajoute phase, objectif courant et état des parties, en retirant les informations inutiles au mode. Les textes de commande utilisent des icônes et mots cohérents entre tutoriel, pause et fiche de personnage.

L'entraînement comprend affichage des entrées, portée, hitboxes, frame advantage, options de garde, réveil programmé, contre-attaque enregistrée, restauration de vie et munitions. Une fonction pas à pas aide à distinguer un vrai combo d'une séquence qui laisse une ouverture.

Les options comprennent taille des sous-titres, vitesse de lecture, sous-titrage des sons, contraste des silhouettes, motifs pour les dangers, vibration, secousses, flashs, remappage et maintien simplifié. Les réglages de temps qui modifient la difficulté restent réservés aux profils assistés et ne partagent pas leur classement avec le profil standard.

## 15 Données et intégration

### Séparer simulation et présentation

Le moteur de combat ne lit pas la couleur d'un pixel pour déterminer un impact. Il utilise des entités, positions, états, rectangles et événements de frame. Le rendu choisit les images correspondantes. Cette séparation permet de remplacer un sprite provisoire sans changer les règles du combat ni casser les replays.

Les données portent des identifiants explicites pour combattants, mouvements, costumes, stages, boss, chapitres et assets. Une référence inconnue doit produire une erreur de validation visible au démarrage de développement. Elle ne doit pas être remplacée silencieusement par le premier élément de la liste.

Un enregistrement de partie conserve version des données, seed, schéma de règles et entrées par frame. Les nombres de simulation utilisent des entiers ou des valeurs fixes maîtrisées. Les animations cosmétiques, particules et caméras ne modifient pas le résultat du combat.

### Connexion à un projet principal

Le module expose ouvrir le mode, transmettre le profil, charger la sélection, terminer une rencontre et renvoyer les récompenses. Les récompenses validées ont des identifiants persistants ; réouvrir le résultat ne les distribue pas une seconde fois. Les sauvegardes déclarent leur version et disposent d'une migration vers la suivante.

Le lot livré contient un prototype autonome afin de tester les règles sans dépendre d'un dépôt non identifié. Son intégration définitive demande le moteur et les conventions du projet hôte. Les dossiers de conception et les données sont préparés pour être déplacés dans un module dédié, avec une séparation nette entre personnages, stages et boss.

## 16 Validation et étapes de production

### Conditions pour déclarer un combattant terminé

Le personnage doit posséder toutes ses actions jouables, des hitboxes cohérentes dans les deux orientations, un rechargement ou une ressource équivalente, ses coups et combos testés, son introduction, son rival, son ending et ses finitions. Les assets doivent correspondre à la version choisie. Il ne suffit pas que sa fiche existe dans un menu.

Les tests importants couvrent garde et côté, consommation de munitions, bornes des fenêtres de rechargement, interruption, mise à terre, absence de combo infini et transitions de fin de manche. Un test de hitbox compare un coup qui doit toucher et un coup qui doit manquer. Le journal de test doit indiquer ce qui a été réellement exécuté.

### Conditions pour déclarer un boss terminé

Les trois phases doivent pouvoir être atteintes, comprises et vaincues sans outil de développement. Chaque attaque majeure possède une réponse atteignable. Les parties détruites ne redeviennent pas actives sans règle annoncée. Les transitions ne bloquent ni les animations ni la sauvegarde. Le solo reste possible sans assistance coopérative cachée.

Le contrôle visuel compare l'échelle perçue, la silhouette, les armes, la trajectoire et les points faibles avec la référence. Les noms des mécaniques créées pour le jeu restent distincts des descriptions canoniques. Le test inclut défaite, reprise, changement de difficulté et sortie vers le menu.

### Jalons

Le jalon 1 valide Marcus contre RAAM, le rechargement, la garde, les combos simples et un stage. Le jalon 2 valide Berserker et une simulation de véhicule, avec phases et télégraphes. Le jalon 3 termine quatre combattants, deux arènes en couches et les premières routes arcade. Le jalon 4 étend le contenu au noyau de douze, ajoute l'entraînement complet et les tournois. Les jalons suivants ajoutent les campagnes, les 36 combattants, les 24 boss et le réseau après validation du déterminisme.

L'ordre des prochaines images est Marcus en actions essentielles, RAAM en actions essentielles, la Berserker en charge et récupération, puis les couches du stage initial. Les costumes supplémentaires suivent après stabilisation des silhouettes. Ce choix réduit les reprises et transforme les images en contenu effectivement jouable.

### Sources de cadrage

[S01] The Coalition, portail officiel Gears of War, https://www.gearsofwar.com/fr-fr/ ; consulté le 19 novembre 2026. Périmètre des épisodes et identités principales.

[S02] The Coalition, Gears of War E-Day, https://www.gearsofwar.com/en-us/games/gears-of-war-eday/ ; consulté le 19 novembre 2026. Cadre chronologique et personnages annoncés. Aucun détail non publié déduit.

[S03] The Coalition, Gears of War, https://www.gearsofwar.com/en-us/games/gears-of-war/ ; consulté le 19 novembre 2026. Marcus, Dom, opposition humains et Locustes, finitions au Lancer.

[S04] Xbox, Gears 5 Hivebusters, https://www.xbox.com/en-us/games/store/Gears-5-Hivebusters/9NB77CW5J1TT ; consulté le 19 novembre 2026. Scorpio, Lahni, Keegan, Mac et Galangi.

[S05] The Coalition, Hivebusters DLC is Now Available, https://www.gearsofwar.com/en-us/news/hivebusters/ ; 14 décembre 2020, consulté le 19 novembre 2026. Wakaatu, Galangi, capacités des héros.

[S06] Xbox, Gears Triple Bundle, https://www.xbox.com/en-US/games/store/gears-triple-bundle/9pcvn6lrvv13 ; consulté le 19 novembre 2026. Gears Tactics, Gabe Diaz, Ukkon et position chronologique.

[S07] Xbox, série Gears, https://www.xbox.com/en-GB/games/gears ; consulté le 19 novembre 2026. Références de série, Reloaded, Tactics et Gears 5.

[S08] The Coalition, Developer Blog Bosses, https://www.gearsofwar.com/en-us/news/dev-blog-bosses/ ; 10 avril 2020, consulté le 19 novembre 2026. Brumak, Corpser, Reaver, parties protégées, anticipation et phases dans Tactics.

Les annexes conservent leurs sources propres au niveau des entrées. Les règles proposées ici constituent le design original du mode 2D.
