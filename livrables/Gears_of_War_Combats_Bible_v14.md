# Gears of War Combats — Bible de conception V14

**Darknigthmare · Consolidation du 2026-11-27 · Guide général et deux extensions inclus dans la conception.**

Cette édition rassemble les chapitres de conception existants, le chapitre d'adaptation des guides, le catalogue visuel courant, les 68 rubriques de suivi et les 40 scénarios d'acceptation des extensions. Les copies exactes des trois guides sont conservées séparément avec leurs empreintes. Ce document ne remplace pas leurs originaux.

## Lecture et perimetre

La priorité de production actuelle reste les **assets fixes manquants, un sujet par image**. Les règles, valeurs, routes et chorégraphies proposées sont des adaptations pour un jeu de combat 2D. Les animations futures sont spécifiées dans les chapitres historiques et dans les extensions ; elles ne sont pas déclarées produites.

Les chapitres initiaux décrivent le noyau de conception V1 : 36 personnages, 24 rencontres et 24 arènes. Le catalogue courant ci-dessous inclut les extensions de production postérieures. Les tableaux historiques gardent leur date et ne doivent pas être utilisés comme état courant.

Le prototype conserve trois rencontres : Marcus contre RAAM, Berserker et King Raven de simulation. Les nouvelles assistances, le tag, les supers d'équipe et les règles d'accès décrites ici sont **conçus, pas implémentés ni testés dans le moteur par cette passe**. Le [README du prototype](../prototype/README.md) précise les fonctions réellement disponibles.

## Sommaire

- [État courant](#etat-courant)
- [Vision et systèmes](#vision-et-systemes-de-combat)
- [Roster, armes et movesets](#roster-armes-et-movesets)
- [Boss, arènes et campagne](#boss-arenes-et-campagne)
- [Guide et extensions adaptés à Gears](#guide-commun-et-deux-extensions-adaptes-a-gears)
- [Personnages et créatures complémentaires V14](#personnages-et-creatures-complementaires-v14)
- [Catalogue de production](#catalogue-courant-de-production)
- [Matrice des 68 rubriques](#matrice-complete-des-68-rubriques)
- [Audit et 40 cas d'acceptation](#audit-et-cas-dacceptation-des-extensions)
- [Premier lot historique](#annexe-historique-du-premier-lot)

## Etat courant

| Catégorie | Avec référence | Catalogue | Sans référence |
| --- | --- | --- | --- |
| Personnages | 51 | 57 | 6 |
| Costumes | 65 | 85 | 20 |
| Boss, créatures et machines | 30 | 34 | 4 |
| Stages | 34 | 34 | 0 |
| Projectiles | 5 | 9 | 4 |

**159 PNG actifs uniques** ; **17 révisions archivées** hors total actif. **0 fidélités 1:1 certifiées** et **0 jeux d'animations complets**. Les catégories mesurent la présence d'au moins une référence, y compris partielle ou d'une autre édition ; elles ne mesurent pas la conformité finale. Ephyra reste un décor complémentaire, en dehors des 34 fiches de stages.

La provenance et les réserves figurent dans la [couverture courante](../production/coverage.json), le [manifeste des images](../production/asset_manifest.json), la [galerie](../Galerie_Personnages.html), le [listing V14](../docs/production/LISTING_V14.md) et la [reprise V14](../docs/production/REPRISE_V14.md). Les PDF, DOCX et classeurs V1 restent des livrables historiques ; cette bible V14 est l'édition Markdown consolidée.

### Trois sources originales conservees

| Document | Octets | SHA-256 |
| --- | --- | --- |
| [Combat_Games_Guide_General_v1.0.txt](../docs/guides/combat/Combat_Games_Guide_General_v1.0.txt) | 55172 | `4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7` |
| [Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt](../docs/guides/combat/Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt) | 60589 | `330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f` |
| [Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt](../docs/guides/combat/Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt) | 47334 | `08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b` |

## Vision et systemes de combat

Source complète : [core_bible.md](../docs/core_bible.md).

Chapitre de conception conservé : ses nombres de contenu décrivent le noyau V1, sauf mentions V12 explicites.

### Gears of War Combats

#### Bible de conception du mode de combat 2D

Version 1 du 19 novembre 2026. Projet de Darknigthmare. Cette bible définit un mode annexe autonome de combat de profil, compatible avec une future intégration dans un jeu Gears plus large. Elle couvre les systèmes de combat, les personnages, les parcours narratifs, les tournois, les exécutions, les arènes et les affrontements contre les créatures et les véhicules de grande taille.

Le résultat recherché est un jeu de combat lourd, précis et lisible, dont les personnages gardent leurs visages, leurs silhouettes, leurs armes et leur époque. La simulation tourne à 60 pas par seconde. Les tirs créent des décisions de distance et de rechargement ; le corps à corps convertit ces décisions en combos courts et violents. Les boss conservent leur présence monumentale grâce à un cadrage et à des objectifs spécifiques.

Trois statuts accompagnent le contenu : une référence canonique décrit ce qui provient des jeux ; une adaptation décrit une règle ou une scène écrite pour ce projet ; une réalisation décrit un fichier ou une fonctionnalité effectivement livré. Les nombres de frames, les dégâts, les jauges, les dialogues et les routes de combat de cette bible sont des propositions de conception. Ils ne constituent pas des données officielles des jeux Gears.

##### Livrables et lecture

**Mise à jour V12 — 27 novembre 2026.** Le [chapitre d'intégration du guide et des deux extensions](../docs/combat_extensions.md) rattache les trois sources communes à cette bible : taunts et sélection, assistances et tag, supers/finishers d'équipe, clashes, entités persistantes, stages bonus, espace d'archives, slots verrouillés et règles de déblocage. Les [originaux et leur provenance](../docs/guides/combat/README.md), le [rapport d'écart](../docs/production/GUIDE_INTEGRATION_V12.md) et la [matrice des 68 rubriques](../docs/production/GUIDE_REQUIREMENTS_V12.csv) distinguent documentation, production et fonctionnement vérifié.

La phase courante reste la production des **assets fixes manquants**. Les animations des extensions sont spécifiées pour la suite ; leur présence dans les guides ne les rend pas produites ou jouables. Les jalons d'animation décrits plus bas restent des objectifs futurs. Les nouveaux contrats d'équipe et d'accès sont des adaptations conçues pour ce mode, avec les restrictions d'époque et de lore exposées dans le chapitre V12.

La bible principale présente les décisions et les règles. Les annexes détaillent le roster, les coups, les 36 parcours arcade, les 24 boss, les 24 stages et les 12 chapitres. Le classeur de production permet de filtrer les entrées et de suivre les assets. Les fichiers JSON constituent les données structurées. Le prototype HTML permet d'essayer un sous-ensemble des mécaniques ; la disponibilité de chaque fonction est indiquée dans son fichier de lecture.

Un combattant inscrit au roster n'est pas compté comme animé ou intégré. Un visuel généré n'est pas compté comme un costume terminé. Un décor complet ne vaut pas livraison de ses couches de parallaxe. Ces distinctions structurent le suivi de production et évitent de masquer le travail restant.

#### 1 Vision et identité

##### Un combat reconnaissable dès la silhouette

Le style visuel vise des sprites 2D UHD, grands à l'écran, aux matériaux réalistes : métal usé, tissu épais, peau marquée, masse des armures COG et anatomies locustes. Les proportions peuvent être transposées pour la lisibilité, mais ni le visage ni le dessin des armes ne doivent devenir génériques. Le zoom, les hitboxes et les règles changent avant de modifier l'identité d'un personnage.

L'ambiance garde le poids des Gears : pas de course aérienne flottante ni d'effets colorés qui cachent les corps. Les mouvements rapides proviennent des roulades, des changements d'appui et des déplacements courts. Une lourde attaque ratée doit se lire dans le retour de l'arme et le temps nécessaire pour retrouver la garde.

Les premiers jeux, leurs remasters et leurs rééditions fournissent des références distinctes. Une amélioration de résolution ne crée pas automatiquement un costume supplémentaire. L'âge de Marcus, le type de Lancer, les protections de Baird et les équipements de Kait restent attachés à une version explicitement nommée. La page officielle de la série et les pages des jeux servent de point d'entrée aux références [S01 à S07].

##### Les quatre objectifs de production

- Un duel doit être agréable sans utiliser d'arme à feu : normals, garde, projection, punition et déplacements fonctionnent seuls.
- Les armes doivent apporter une cadence et un risque propres : aucune ne se résume à un projectile interchangeable.
- Chaque boss doit poser une question différente : provoquer une charge, dégager un point faible, casser un équipement, gérer l'altitude ou survivre à un déplacement du terrain.
- Chaque élément présenté comme fidèle doit disposer d'une référence d'épisode, d'un contrôle de silhouette et d'un état de validation consultable.

#### 2 Périmètre de contenu

##### Corpus et continuités

Le corpus de départ comprend Gears of War, Gears of War 2, Gears of War 3, Judgment, Gears of War 4, Gears 5, Hivebusters et Gears Tactics. Ultimate Edition et Reloaded servent de variantes de rendu du premier épisode. E-Day dispose d'une section de références dédiée ; seuls les personnages, armes, lieux et détails attestés entrent dans les fiches finalisées. L'annonce officielle situe E-Day quatorze ans avant le premier Gears [S02].

Les comics et romans peuvent alimenter des extensions documentées. Ils ne servent pas à inventer sans preuve la géométrie d'un costume qui n'a jamais été montré. Les apparitions promotionnelles, invités et collaborations restent dans une catégorie facultative, séparée du roster Gears. Un futur pack ne doit pas occuper la place d'une animation indispensable à un personnage déjà promis.

##### Lots jouables

Le noyau de conception contient Marcus, Dom, Baird, Cole, Anya, Kait, RAAM, Skorge, Myrrah, un Drone locuste, un Kantus et un Garde Theron. Ils couvrent les principaux besoins de combat : polyvalence, pression, mobilité, pose d'outils, charge, tirs préparés, commandement et contrôle de l'espace. Vingt-quatre combattants supplémentaires sont spécifiés dans l'annexe roster.

Le premier lot d'intégration doit se limiter à quatre combattants complètement animés, deux stages réellement découpés et deux boss complets. Il valide le langage du jeu avant l'extension à douze puis trente-six combattants. La priorité des sprites n'est donc pas le nombre de portraits : ce sont les poses de combat, les transitions, les impacts et les actions réellement utilisables.

##### Familles de modes

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

#### 3 Commandes et vocabulaire

##### Schéma de combat cible

Quatre boutons principaux donnent accès au léger L, au moyen M, au lourd H et à l'action d'arme W. Un bouton de mobilité E déclenche l'esquive ou l'interaction de couverture selon le mode. R lance ou confirme le rechargement. L plus M effectue une projection ; M plus H dépense deux barres pour un briseur ; H plus W déclenche la super si ses conditions sont réunies. Des raccourcis reconfigurables reproduisent ces combinaisons.

La garde du jeu cible utilise la direction opposée à l'adversaire : arrière pour les attaques hautes et médianes, bas arrière pour les basses. Le prototype peut employer un bouton explicite de garde afin d'isoler le test de la défense ; cette différence doit rester visible dans ses commandes. Les directions sont toujours relatives au côté de l'adversaire.

La notation numérique suit le pavé de neuf directions : 5 neutre, 6 avant, 4 arrière, 2 bas, 8 haut. Une commande 236W signifie bas, diagonale avant, avant, puis arme. j.L signifie un léger aérien. Le symbole > représente une liaison après récupération, et xx représente une annulation. Une fiche de combo doit distinguer ces deux situations.

##### Commandes modernes et techniques

Un schéma moderne donne un accès direction plus bouton aux spéciaux. Il produit les mêmes actions, avec les mêmes dégâts, délais et coûts. Les commandes techniques donnent accès aux variantes de trajectoire, sans bonus caché de puissance. Les macros d'accessibilité peuvent regrouper des entrées simultanées ; elles n'enchaînent pas automatiquement plusieurs décisions de combat.

Le clavier doit accepter ZQSD et WASD, les flèches et une remappage complet. Le tactile présente déplacement, garde, attaque, tir, esquive, rechargement et spécial avec des zones de contact distinctes. Les actions maintenues se relâchent sur perte de focus ou interruption du pointeur. La manette affiche les commandes de la famille détectée et prévoit une zone morte réglable.

#### 4 Règles du duel

##### Match et espace de jeu

Le réglage standard est deux manches gagnantes de 99 secondes. La vie est réinitialisée à chaque manche. La jauge de super est conservée dans le match, plafonnée à trois barres, puis réinitialisée au match suivant. L'égalité simultanée donne une manche aux deux joueurs ; si cela termine le match pour les deux, une manche de départage complète est jouée. Une égalité au temps compare le pourcentage de vie restante, puis déclenche le même départage si les valeurs sont identiques.

La simulation utilise une unité de distance commune et un plan de collision unique. La caméra suit le milieu des personnages, avec un zoom limité pour que les mains et les armes restent lisibles. Les joueurs ne peuvent pas sortir du cadre en reculant. Le sol reste horizontal ; les variations de relief du décor sont visuelles dans les stages de tournoi.

Les personnages ont une masse et une vitesse distinctes, mais aucun costume ne modifie une statistique. Un masque ou une cape n'élargit pas automatiquement la zone de dégâts. Les grandes armes possèdent leurs propres hitboxes et leurs propres zones exposées quand une punition est voulue. Les ailes ou montures des personnages ne deviennent pas invulnérables par simple choix de sprite.

##### Attaques et garde

Chaque coup possède démarrage, activité, récupération, dégâts, effet en garde, effet au contact, hauteur, portée, niveau d'armure et autorisations d'annulation. Une attaque rapide de référence démarre en 6 frames ; un lourd de punition démarre entre 16 et 22 frames. Ces valeurs servent à construire les premiers tests, puis sont ajustées à partir de parties enregistrées.

La garde bloque les coups de la hauteur correspondante et consomme une jauge de posture de 100 points. Après 45 frames sans attaque reçue ni garde tenue, cette jauge récupère à 15 points par seconde. Atteindre zéro provoque une rupture de 45 frames, puis rend 60 points. Le réglage évite de transformer chaque défense en défaite inévitable : la garde parfaite, disponible pendant les trois premières frames d'une garde correcte, réduit fortement la perte de posture sans donner une super garantie.

Les projectiles infligent au maximum 10 % de leurs dégâts en garde. Le chip ne tue pas en duel standard : il laisse un point de vie. Les coups de corps à corps ne font pas de chip sauf mention explicite d'un état renforcé. Le boss peut employer une autre règle si son contrat l'affiche avant le combat.

##### Projection et défense rapprochée

La projection normale exige une courte distance, un démarrage de 8 frames et une fenêtre de déchoppe de 12 frames. Une saisie spéciale est plus lente, plus dommageable et ne partage pas nécessairement cette déchoppe ; elle doit posséder une réponse claire par saut, recul ou interruption. Un personnage au sol conserve une protection temporaire contre les projections pendant sa relevée.

Une roulade coûte 25 points d'endurance sur 100. Son déplacement couvre une longueur de corps, avec une brève fenêtre d'évitement au milieu et une récupération punissable. Elle n'annule pas gratuitement le début d'un gros coup. L'endurance commence à remonter 60 frames après la dernière dépense. Des frais supplémentaires ou une récupération longue empêchent les allers-retours invulnérables en boucle.

##### Combos et limitation des boucles

La chaîne universelle L xx M xx H facilite l'entrée en matière. Les normals indiqués peuvent s'annuler en spécial, puis en super pour une dépense définie. Les autres liaisons doivent être prouvées par l'avantage au contact. Un avantage de +8 ne garantit qu'un coup suivant dont le démarrage tient dans cette fenêtre, avec portée suffisante et règles de recul compatibles.

L'échelle de dégâts proposée suit 100 %, 90 %, 80 %, 70 %, 60 %, 50 %, 40 %, puis 35 % pour le huitième impact et les suivants. Les dégâts de chaque paquet sont arrondis à l'entier le plus proche avant leur addition. Une super garde un plancher de 45 %. Une seule extension de rebond mural et une seule remise au sol relançable sont permises dans la même séquence. La gravité de juggle augmente à chaque lancement. Le système identifie la séquence, même si une animation de changement d'arme la traverse.

Un briseur coûte deux barres, agit après le premier impact confirmé et repousse les deux personnages vers le neutre. Il ne fonctionne pas pendant une projection, une exécution ou une cinématique de boss. Il donne une sortie coûteuse sans rendre tous les combos inutiles. Une option d'entraînement permet d'enregistrer la réponse du défenseur après chaque coup pour vérifier les vrais intervalles.

#### 5 Armes et rechargement actif

##### Traduire la sensation de Gears

L'arme est un engagement de rythme. Le Lancer pousse à moyenne distance, le Gnasher récompense la proximité, le Longshot impose une préparation, le Torque Bow menace après une charge lisible, le Boomshot punit les regroupements et le Hammer of Dawn demande une condition de ciblage. Les fiches fixent l'arme de référence du personnage ; un skin ne remplace pas discrètement un modèle par un autre.

Les chargeurs sont des valeurs de combat propres à l'adaptation. Une rafale de Lancer utilise une unité de munition de jeu, distincte du nombre de balles représentées à l'écran. Les nombres du HUD ne doivent donc jamais être présentés comme les capacités canoniques des armes. Les attaques sans munition conservent une solution de corps à corps ; le joueur n'est pas condamné à attendre.

##### Fenêtre de rechargement

Le rechargement normal cible 72 frames. Une seconde pression sur R entre les frames 34 et 43 confirme la fenêtre parfaite ; les frames 27 à 33 et 44 à 50 constituent la fenêtre sûre. Une pression en dehors de ces fenêtres ajoute 30 frames de blocage. Les bornes sont inclusives et testées au pas de simulation, indépendamment du nombre d'images affichées.

La réussite parfaite termine le chargement à la frame 44 et renforce les deux prochaines actions d'arme avec un coefficient de dégâts de 1,10. La réussite sûre termine à la frame 60. Ne pas confirmer termine à la frame 72. Une tentative ratée ne peut pas être répétée pendant le même chargement. Aucun résultat n'augmente les points de vie ou la fréquence de simulation.

Être frappé pendant les 18 premières frames interrompt le rechargement sans remplir le chargeur. Une fois le chargeur verrouillé, un coup peut interrompre la pose mais conserve l'état de munition acquis. Les frames nécessaires à cette séparation sont explicitement enregistrées. Les coups renforcés perdus après avoir raté la cible ne sont pas remboursés.

##### Éviter le duel de tirs immobile

Les tirs présentent un départ et une récupération visibles. Reculer au fond de l'arène ne crée pas de munition supplémentaire. La garde, l'esquive et les trajectoires basses donnent plusieurs réponses. Les supers capables de traverser les projectiles ont un coût et une anticipation lisibles. Les grenades ne doivent pas ajouter un hasard imprévisible : leur arc, leur délai et leur zone d'explosion restent constants pour une entrée identique.

#### 6 Exécutions et présentation des fins de combat

##### Une conclusion liée au personnage

Chaque combattant reçoit deux exécutions de signature et une finition rapide. Les versions choisies se fondent sur son arme, sa force et sa personnalité. Le Lancer, le couteau, le Torque Bow, les outils lourds ou les pouvoirs locustes suivent des chorégraphies différentes. Les noms et séquences proposés pour ce jeu restent des créations d'adaptation même si l'inspiration vient d'exécutions connues [S03].

L'exécution n'est disponible qu'après la dernière manche gagnée, pendant une fenêtre de 180 frames. Le perdant est en état neutralisé, le vainqueur reçoit une indication discrète et peut choisir la finition ou une victoire immédiate. Rater la commande conclut le match normalement. Elle n'ajoute ni dégâts décisifs ni classement bonus compétitif.

Les rencontres de boss ont des finitions adaptées aux parties détruites. Un personnage ne doit pas soulever une créature géante comme un humanoïde. Le coup final peut déclencher une chute, l'arrêt d'un moteur, une retraite, un effondrement ou une destruction d'équipement. Les véhicules alliés d'entraînement concluent par une désactivation et une extraction.

##### Caméra et options

La caméra conserve le profil jusqu'à l'impact confirmé. Une courte coupe permet la mise en scène, puis retourne à une pose de victoire cohérente. Les adversaires mécaniques, Locustes, Swarm et humains utilisent des points d'attache distincts. Les animations de saisie ne partagent pas un squelette unique sans adaptation de taille.

Un réglage de violence réduite remplace les détails graphiques par des effets de choc et une coupe de caméra sans modifier le gagnant ni la durée maximale. Un réglage de flash et de secousse réduit l'intensité des effets. Les deux joueurs peuvent demander de passer la séquence ; en tournoi, le profil peut imposer la finition courte pour conserver le rythme du tableau.

#### 7 Histoire et parcours arcade

##### Une anthologie jouable

L'histoire relie les jeux par des dossiers de bataille et des souvenirs datés. Chaque chapitre indique son époque, son point de vue et son objectif. Un combat d'entraînement entre alliés est nommé comme tel. Une rencontre impossible entre deux époques appartient à l'exhibition ou à une route alternative explicitement signalée. La campagne principale n'a pas besoin d'un voyage temporel inventé pour réunir son roster.

Les douze chapitres prévus sont détaillés dans l'annexe campagne. Chaque chapitre contient une introduction, une première situation de duel, un objectif différent, une confrontation personnelle, une rencontre majeure et une sortie de scène. Les cinématiques sont conçues en portraits et plans fixes animables pour rendre la production réaliste, avec possibilité de remplacer ensuite un passage par une séquence complète.

##### Structure d'une route individuelle

Une route arcade comporte cinq duels de progression, dont une rencontre à contrainte, un rival, un boss, un duel final et un ending. Les huit combats peuvent traverser plusieurs époques dans ce mode hors continuité. Le rival bénéficie de deux répliques originales, d'une introduction contextualisée et d'une variante si le joueur a déjà terminé la route. La fin présente une conséquence personnelle et une image dédiée ; le résultat ne réécrit pas automatiquement le canon de la campagne.

Chaque route définit des opposants par identifiants, un costume compatible, une arène, un enjeu de rivalité et une fin. L'IA s'adapte aux actions apprises au cours de la route plutôt qu'à la lecture instantanée des boutons. La difficulté augmente le nombre de réponses et la qualité des décisions, avec un délai minimum documenté. Elle n'augmente pas silencieusement les dégâts adverses dans le profil compétitif.

Les 36 routes de l'annexe sont des synopsis prêts à développer en scripts de mise en scène. Les textes complets de doublage, les enregistrements audio et les illustrations d'ending ne sont pas marqués produits tant que leurs fichiers n'existent pas.

#### 8 Tournois et jeu compétitif

##### Gestion du tableau

Le joueur choisit 8, 16 ou 32 participants, humains locaux ou IA. Les doublons de personnage sont permis ; chaque entrant garde son identifiant de participant. Le seeding accepte l'ordre choisi, un mélange déterministe à graine ou un classement renseigné. Un forfait ne génère pas un faux combat ni un score de performance.

L'élimination simple nécessite N moins 1 matchs. La double élimination nécessite 2N moins 2 matchs sans réinitialisation de grande finale, et 2N moins 1 si le vainqueur du tableau bas inflige sa première défaite au vainqueur du tableau haut. Pour 16 entrants, cela donne 30 ou 31 matchs. Le moteur doit conserver deux compteurs de défaites et les dépendances de chaque rencontre, pas seulement afficher un arbre décoratif.

Les parties se jouent en deux manches gagnantes. Un set standard utilise deux matchs gagnants ; les finales peuvent en exiger trois. Le perdant peut changer de personnage. Le vainqueur conserve son personnage, sauf variante du règlement choisie avant l'événement. Les changements de costume ne modifient pas les hitboxes.

##### Stages et intégrité d'une partie

Le profil tournoi impose une liste de stages sans dégâts de décor, sans objets aléatoires et sans avant-plan opaque. Le côté de départ alterne à chaque match. Les résultats enregistrent version du moteur, profil de règles, identifiants, seed et entrée de chaque joueur. Une mise à jour de la base de coups ne prétend pas conserver la compatibilité d'anciens replays si les règles ont changé.

Le réseau futur prévoit simulation déterministe et rollback. Le prototype livré reste local contre l'IA. La synchronisation réseau doit être une étape testée séparément : latence, rollback de hit-stop, projectiles, chargements et changements de phase ne sont pas résolus par la simple présence d'un bouton multijoueur.

#### 9 Boss Battle

##### Contrat d'une rencontre

Un boss possède une machine d'états distincte de celle d'un combattant. Le contrat définit l'échelle à l'écran, les zones attaquables, les points faibles, l'attaque en cours, sa préparation, les transitions et la fin. La caméra maintient un indicateur de l'attaque hors champ et garde le joueur visible. La grande taille ne se traduit jamais par une collision corporelle couvrant tout l'écran en permanence.

Une rencontre standard vise trois phases sans intervalle manquant : au-dessus de 66 %, au-dessus de 33 % et jusqu’à 66 %, puis à 33 % ou moins de vie. Ce découpage est une règle d'adaptation et peut varier pour un combat à objectifs. La transition donne un bref moment de lecture, retire les anciens marqueurs et prépare une nouvelle menace. Elle ne peut pas interrompre arbitrairement un combo de récompense sans prévenir le joueur.

Les attaques létales disposent d'une anticipation d'au moins 45 frames en difficulté normale. Une attaque rapide mineure peut avoir un signal plus court, mais ne doit pas demander une esquive impossible. Chaque menace combine une forme au sol, un mouvement du boss et un son ; la couleur seule n'est jamais l'unique indication.

##### Créatures géantes

La Berserker impose d'appâter sa charge, d'esquiver et de profiter d'une exposition définie. Le Corpser utilise des pattes et des zones de frappe clairement séparées. Le Brumak présente des armes et parties ciblables. Le Reaver change d'altitude. Le Swarmak expose des zones vulnérables. Le Kraken utilise plusieurs éléments du décor pour renouveler le combat. Chaque fiche précise les écarts entre la référence canonique et la règle 2D retenue.

Le blog officiel de Gears Tactics décrit le principe des boss comme des problèmes de positionnement, avec des attaques annoncées, des parties protégées et des changements de phase [S08]. Cette inspiration convient à l'adaptation, sans recopier automatiquement la durée d'un tour dans un moteur de combat en temps réel.

##### Véhicules et machines

Un adversaire aérien dispose d'un point de visée accessible au tir, d'un passage bas punissable au corps à corps et d'une séquence d'équipement à neutraliser. Les attaques de missiles et de mitraillage occupent des zones distinctes. Détruire une arme réduit la menace correspondante ; l'interface reflète immédiatement cette conséquence.

Le King Raven, le Centaur et le Silverback peuvent être sélectionnés en simulation. Leur opposition à un Gear n'est pas présentée comme un fait de la campagne. Les silhouettes, moteurs, armes et points d'accès doivent venir de leur version de jeu, tandis que les patterns d'entraînement sont créés pour ce mode. Les dégâts fictifs se concluent par un arrêt des systèmes ou un abandon de l'exercice.

##### Solo et coopération

Le solo offre toutes les réponses indispensables, y compris les interactions initialement imaginées pour plusieurs joueurs. Le coopératif à deux partage les consommables de rencontre et permet une réanimation limitée. La vie cible du boss passe à 1,65 fois la valeur solo ; les dégâts des attaques restent identiques. Les menaces parallèles augmentent la coordination sans supprimer les ouvertures.

Une saisie coopérative comporte un temps d'intervention suffisamment long pour le partenaire. En solo, la même attaque devient une épreuve d'esquive ou une fuite par action lisible, jamais une mort automatique faute de second joueur. Un nombre maximum d'ennemis supplémentaires évite la saturation visuelle.

##### Contrats et récompenses

Les contrats proposent victoire simple, absence de mise à terre, parties détruites dans un ordre choisi ou temps cible. La note associe temps, dégâts reçus et objectifs remplis avec des poids visibles. Les rechargements parfaits n'accordent un bonus que s'ils participent à des actions pertinentes ; répéter une action sans danger ne permet pas de cultiver un score infini.

Les récompenses sont des illustrations, variantes esthétiques, entrées de galerie et titres. Elles n'augmentent pas les dégâts en versus. Le Boss Rush conserve une fraction de vie et offre un choix entre soin, réserve de munitions ou récupération de jauge ; les décisions et les effets sont affichés avant confirmation.

#### 10 Arènes en parallaxe

##### Structure d'un stage

Chaque arène se compose de six couches : ciel, horizon, architecture, plan moyen, sol jouable et avant-plan. Les effets sont gérés séparément par le moteur. Les facteurs de déplacement typiques sont 0,04 ; 0,15 ; 0,36 ; 0,65 ; 1,00 ; 1,12. Ils décrivent le déplacement relatif à la caméra et non une profondeur physique mesurée dans l'univers.

La version tournoi garde le plan de jeu dégagé et réduit les éléments passants. La version spectacle peut présenter un événement déterministe : effondrement lointain, passage de véhicule, changement de lumière ou pluie. Les collisions de danger ne sont actives que dans les modes qui les annoncent. L'évolution visuelle d'une manche ne modifie pas la géométrie compétitive.

Chaque couche exportée garde les mêmes dimensions logiques, le même horizon et la même origine. Les débords latéraux sont prévus dès la composition. Une image aplatie peut servir d'illustration ou de prototype ; les six couches doivent être exportées séparément pour fournir une profondeur indépendante. Les zones cachées derrière un objet doivent être redessinées pour permettre une vraie parallaxe.

##### Familles d'environnements

Le catalogue couvre les ruines urbaines d'Ephyra, les installations de la COG, les souterrains locustes, les forteresses, les combats sur transport, les zones gelées, les étendues désertiques et les îles volcaniques de Galangi. Les 24 fiches donnent épisode, heure, ambiance, couches et traitement tournoi. Le décor de chaque boss prend en charge ses points faibles sans réutiliser automatiquement un stage de duel trop petit.

Les contrastes sont contrôlés sur des silhouettes COG bleues, locustes sombres et Swarm rougeâtres. La poussière, la pluie et la fumée ne doivent pas cacher le démarrage d'un coup. Le réglage d'accessibilité renforce le contour des combattants et réduit les particules, sans modifier leurs positions ni leurs fenêtres d'attaque.

#### 11 Direction artistique et fidélité

##### Validation par version

Une fiche de référence comporte personnage, épisode, scène ou skin, angle, arme, source et date d'accès. Pour valider un asset, on contrôle le visage, la silhouette, l'armure, l'arme, les matériaux, les proportions relatives et la lisibilité de profil. Une image séduisante qui change la forme du Lancer ou l'âge du personnage reste à corriger.

Le terme fidélité 1 pour 1 exprime l'objectif de correspondance avec la référence choisie. Une génération ne prouve pas à elle seule cette correspondance. Les premiers visuels livrés portent donc le statut « généré, contrôle canon à finaliser ». La validation finale demande une comparaison côte à côte avec des captures déterminées, puis une correction ciblée de chaque écart.

La source d'un personnage ne suffit pas à certifier tous ses détails. Une page qui confirme la présence de Lahni dans Hivebusters ne valide pas les coutures exactes de son uniforme. Les cases de source distinguent identité confirmée, équipement confirmé et détail visuel à contrôler.

##### Un asset par image

Chaque image de personnage contient un seul personnage, une seule pose et un seul costume. Les variantes casque, sans casque, arme différente et côté opposé sont des fichiers distincts. Un atlas de runtime peut regrouper les fichiers après validation, mais les originaux restent individuels.

Une pose isolée n'est pas une animation. L'animation exige des transitions cohérentes, une trajectoire des mains, un déplacement du poids et des points d'appui constants. Une translation ou une rotation globale de l'image permet de tester une sensation, sans être comptée comme un nouveau dessin d'animation.

Le retournement horizontal n'est pas la solution finale pour les tatouages, épaulières, mains dominantes ou mécanismes asymétriques. Les métadonnées indiquent si le miroir est autorisé. Les personnages majeurs nécessitent une série pour chaque orientation dès qu'une asymétrie significative est visible.

##### Tailles et export

Les masters de combattants visent un canevas de 1536 par 1536 ou 1024 par 1536 selon la silhouette. Le runtime utilise un pivot aux pieds, un rectangle de cadrage et une hauteur logique propres au personnage. Un géant ne doit pas être réduit à la hauteur d'un soldat pour partager le même canevas visible. Les mesures réelles des premiers fichiers sont inscrites dans le manifeste.

Les exports PNG conservent l'alpha. Le contour ne porte ni halo blanc ni ombre de sol peinte qui flotterait pendant un saut. Les VFX de tir, fumée, sang optionnel, kryll ou électricité sont des assets séparés. Les empreintes et ombres au sol appartiennent au moteur.

#### 12 Programme d'animation

##### États indispensables par combattant

Le lot d'animation complet vise 26 états de locomotion et de combat communs : entrée, attente, marche avant, marche arrière, départ de course, course, arrêt, accroupissement, saut, chute, atterrissage, roulade, garde haute, garde basse, impact léger, impact lourd, chute au sol, relevée, étourdissement, projection, déchoppe, rechargement, raté de rechargement, provocation, victoire et défaite. Les normals et spéciaux ajoutent leurs propres états.

La priorité est l'anticipation, l'action, la récupération et le retour à la pose neutre. Un lourd spectaculaire sans récupération visible est injouable. Les armes attachées aux mains gardent leurs points de contact. Les douilles, chargeurs et projectiles reviennent au moteur comme événements, afin de ne pas dupliquer un objet déjà dessiné dans l'image.

Le budget indicatif du profil complet est de 272 dessins pour les actions communes, 96 pour les normals, 72 pour les quatre spéciaux, 48 pour deux supers et 64 pour deux exécutions : 552 dessins par orientation et par costume entièrement redessiné. Cette estimation doit être recalculée à partir du plan réel de chaque personnage. Une reprise partielle de costume ne vaut pas duplication automatique du budget complet.

##### Événements d'animation

Chaque clip associe un numéro de frame à ses événements : apparition de hitbox, ouverture d'annulation, émission de projectile, consommation de munition, validation de chargeur, effet sonore, déplacement et fin. Les hitboxes n'ont pas besoin de correspondre au nombre de dessins ; un dessin peut durer plusieurs pas de simulation.

Le fichier d'animation décrit fréquence, boucle, pivots, rectangles de source et événements. Les noms restent stables : personnage, version, costume, côté, action, numéro. Les corrections remplacent une version d'asset par une nouvelle révision ; elles ne changent pas l'identifiant de gameplay.

#### 13 Son et mise en scène

Le mix distingue attaque légère, métal, chair, pierre, mécanique, armes et signaux de boss. Les sons indispensables à la décision restent audibles sous la musique et les dialogues. Une limite de voix simultanées réserve des canaux au rechargement et aux alertes majeures. Les directions hors champ sont indiquées par spatialisation et sous-titres d'action optionnels.

Les thèmes musicaux sont à produire ou à importer depuis des fichiers autorisés fournis pour le projet. Le pack initial ne prétend pas contenir les enregistrements officiels. Les textes originaux de rivalité peuvent être sous-titrés avant tout doublage. Une voix ne doit pas être attribuée à un acteur officiel sans enregistrement correspondant.

Chaque personnage reçoit des sons de déplacement, d'effort, de douleur, de provocation, de victoire et d'exécution. Les boss ont un signal sonore propre à chaque grande attaque. Le rechargement parfait possède une confirmation nette, accompagnée d'un indicateur visuel pour les personnes jouant sans son.

#### 14 Interface et accessibilité

La sélection affiche personnage, variante d'époque, costume, difficulté d'apprentissage, style de combat et source d'équipement. Le même portrait ne sert pas à faire croire que toutes les variantes sont illustrées. Les éléments non produits restent consultables dans le catalogue avec leur statut, puis accessibles dans le jeu seulement lorsqu'ils fonctionnent.

Le HUD de duel contient vie, jauge de super, munitions, posture, manches et temps. Le HUD de boss ajoute phase, objectif courant et état des parties, en retirant les informations inutiles au mode. Les textes de commande utilisent des icônes et mots cohérents entre tutoriel, pause et fiche de personnage.

L'entraînement comprend affichage des entrées, portée, hitboxes, frame advantage, options de garde, réveil programmé, contre-attaque enregistrée, restauration de vie et munitions. Une fonction pas à pas aide à distinguer un vrai combo d'une séquence qui laisse une ouverture.

Les options comprennent taille des sous-titres, vitesse de lecture, sous-titrage des sons, contraste des silhouettes, motifs pour les dangers, vibration, secousses, flashs, remappage et maintien simplifié. Les réglages de temps qui modifient la difficulté restent réservés aux profils assistés et ne partagent pas leur classement avec le profil standard.

#### 15 Données et intégration

##### Séparer simulation et présentation

Le moteur de combat ne lit pas la couleur d'un pixel pour déterminer un impact. Il utilise des entités, positions, états, rectangles et événements de frame. Le rendu choisit les images correspondantes. Cette séparation permet de remplacer un sprite provisoire sans changer les règles du combat ni casser les replays.

Les données portent des identifiants explicites pour combattants, mouvements, costumes, stages, boss, chapitres et assets. Une référence inconnue doit produire une erreur de validation visible au démarrage de développement. Elle ne doit pas être remplacée silencieusement par le premier élément de la liste.

Un enregistrement de partie conserve version des données, seed, schéma de règles et entrées par frame. Les nombres de simulation utilisent des entiers ou des valeurs fixes maîtrisées. Les animations cosmétiques, particules et caméras ne modifient pas le résultat du combat.

##### Connexion à un projet principal

Le module expose ouvrir le mode, transmettre le profil, charger la sélection, terminer une rencontre et renvoyer les récompenses. Les récompenses validées ont des identifiants persistants ; réouvrir le résultat ne les distribue pas une seconde fois. Les sauvegardes déclarent leur version et disposent d'une migration vers la suivante.

Le lot livré contient un prototype autonome afin de tester les règles sans dépendre d'un dépôt non identifié. Son intégration définitive demande le moteur et les conventions du projet hôte. Les dossiers de conception et les données sont préparés pour être déplacés dans un module dédié, avec une séparation nette entre personnages, stages et boss.

#### 16 Validation et étapes de production

##### Conditions pour déclarer un combattant terminé

Le personnage doit posséder toutes ses actions jouables, des hitboxes cohérentes dans les deux orientations, un rechargement ou une ressource équivalente, ses coups et combos testés, son introduction, son rival, son ending et ses finitions. Les assets doivent correspondre à la version choisie. Il ne suffit pas que sa fiche existe dans un menu.

Les tests importants couvrent garde et côté, consommation de munitions, bornes des fenêtres de rechargement, interruption, mise à terre, absence de combo infini et transitions de fin de manche. Un test de hitbox compare un coup qui doit toucher et un coup qui doit manquer. Le journal de test doit indiquer ce qui a été réellement exécuté.

##### Conditions pour déclarer un boss terminé

Les trois phases doivent pouvoir être atteintes, comprises et vaincues sans outil de développement. Chaque attaque majeure possède une réponse atteignable. Les parties détruites ne redeviennent pas actives sans règle annoncée. Les transitions ne bloquent ni les animations ni la sauvegarde. Le solo reste possible sans assistance coopérative cachée.

Le contrôle visuel compare l'échelle perçue, la silhouette, les armes, la trajectoire et les points faibles avec la référence. Les noms des mécaniques créées pour le jeu restent distincts des descriptions canoniques. Le test inclut défaite, reprise, changement de difficulté et sortie vers le menu.

##### Jalons

Le jalon 1 valide Marcus contre RAAM, le rechargement, la garde, les combos simples et un stage. Le jalon 2 valide Berserker et une simulation de véhicule, avec phases et télégraphes. Le jalon 3 termine quatre combattants, deux arènes en couches et les premières routes arcade. Le jalon 4 étend le contenu au noyau de douze, ajoute l'entraînement complet et les tournois. Les jalons suivants ajoutent les campagnes, les 36 combattants, les 24 boss et le réseau après validation du déterminisme.

L'ordre des prochaines images est Marcus en actions essentielles, RAAM en actions essentielles, la Berserker en charge et récupération, puis les couches du stage initial. Les costumes supplémentaires suivent après stabilisation des silhouettes. Ce choix réduit les reprises et transforme les images en contenu effectivement jouable.

##### Sources de cadrage

[S01] The Coalition, portail officiel Gears of War, https://www.gearsofwar.com/fr-fr/ ; consulté le 19 novembre 2026. Périmètre des épisodes et identités principales.

[S02] The Coalition, Gears of War E-Day, https://www.gearsofwar.com/en-us/games/gears-of-war-eday/ ; consulté le 19 novembre 2026. Cadre chronologique et personnages annoncés. Aucun détail non publié déduit.

[S03] The Coalition, Gears of War, https://www.gearsofwar.com/en-us/games/gears-of-war/ ; consulté le 19 novembre 2026. Marcus, Dom, opposition humains et Locustes, finitions au Lancer.

[S04] Xbox, Gears 5 Hivebusters, https://www.xbox.com/en-us/games/store/Gears-5-Hivebusters/9NB77CW5J1TT ; consulté le 19 novembre 2026. Scorpio, Lahni, Keegan, Mac et Galangi.

[S05] The Coalition, Hivebusters DLC is Now Available, https://www.gearsofwar.com/en-us/news/hivebusters/ ; 14 décembre 2020, consulté le 19 novembre 2026. Wakaatu, Galangi, capacités des héros.

[S06] Xbox, Gears Triple Bundle, https://www.xbox.com/en-US/games/store/gears-triple-bundle/9pcvn6lrvv13 ; consulté le 19 novembre 2026. Gears Tactics, Gabe Diaz, Ukkon et position chronologique.

[S07] Xbox, série Gears, https://www.xbox.com/en-GB/games/gears ; consulté le 19 novembre 2026. Références de série, Reloaded, Tactics et Gears 5.

[S08] The Coalition, Developer Blog Bosses, https://www.gearsofwar.com/en-us/news/dev-blog-bosses/ ; 10 avril 2020, consulté le 19 novembre 2026. Brumak, Corpser, Reaver, parties protégées, anticipation et phases dans Tactics.

Les annexes conservent leurs sources propres au niveau des entrées. Les règles proposées ici constituent le design original du mode 2D.

## Roster, armes et movesets

Source complète : [roster_movesets.md](../docs/roster_movesets.md).

Chapitre de conception conservé : ses nombres de contenu décrivent le noyau V1, sauf mentions V12 explicites.

### Personnages armes et routes de combat

#### Périmètre des fiches

Le catalogue définit 36 combattants, répartis en un noyau de 12 et une extension de 24, ainsi que 75 variantes de costume à documenter. Il contient 179 fiches d’action et 36 parcours arcade. Ce nombre mesure la conception écrite. Il ne mesure ni les sprites terminés ni les combattants intégrés.

Les identités et les épisodes renvoient à Gears of War. Les archétypes, jauges, frames, dégâts, combos, dialogues et fins décrits ici sont créés pour cette adaptation. Les armes attribuées à un kit peuvent provenir de l’arsenal du jeu sans constituer l’arme personnelle canonique de ce personnage. Une rencontre d’arcade entre personnages d’époques différentes ne devient pas un événement de la campagne.

Les pages officielles confirment notamment Kilo Squad dans Judgment, les rôles de Gabe, Sid et Mikayla dans Tactics, ainsi que Scorpio et ses capacités dans Hivebusters. Les détails précis de couture, de cicatrice, d’épaulière et de côté d’une prothèse exigent encore des captures définies. Le champ source_scope de chaque combattant conserve cette différence de niveau de preuve.

#### Références de fidélité

Une variante reçoit son propre identifiant, son épisode, son costume et sa feuille de contrôle. Le bandana de Marcus, la pilosité de Dom, les lunettes de Baird, le casque de Clayton et les tatouages de Tai ne doivent pas devenir des accessoires interchangeables. Le personnage conserve les formes et les matériaux du costume choisi. Les armes sont contrôlées avec la même exigence que le visage.

E-Day dispose de références officielles décrivant Marcus, Dom et Tai. Ses variantes restent liées à ces références et à des captures du costume visé. Aucune arme moderne, cicatrice tardive ou pièce d’armure d’une autre époque ne leur est ajoutée par défaut. Ultimate Edition et Reloaded sont des références de présentation du premier jeu, pas automatiquement de nouveaux costumes.

Myrrah, Reine Reyna et Ukkon demandent une validation particulière : leur présence comme combattants directs et l’organisation de leurs coups sont une adaptation. RAAM et le Warden gardent une catégorie de taille élevée. Une créature géante ne devient pas un skin de soldat. JACK garde un corps flottant avec une zone vulnérable accessible ; son vol ne supprime pas les interactions du duel.

Les personnages invités, acteurs jouant un skin promotionnel et collaborations ne sont pas comptés parmi les 36. Anthony Carmine, Benjamin Carmine, Minh Young Kim, Jace, Barrick, Valera, Alicia, Sraak, Jermad, Karn et d’autres candidats pourront recevoir des fiches d’extension. Ils ne sont ni implicitement produits ni assimilés à des recolorations du roster existant.

#### Commandes et lecture des données

L, M et H désignent les attaques légère, moyenne et lourde. E désigne la mobilité ; R le rechargement. Les directions utilisent la notation numérique relative à l’adversaire, avec 5 au neutre, 6 vers l’avant et 2 vers le bas. Une entrée 236M signifie bas, diagonale avant, avant, puis moyen. Les raccourcis modernes doivent appeler exactement la même action que cette entrée technique.

Le symbole > désigne une liaison après récupération. Le symbole xx désigne une annulation. La chaîne d’annulations commune est L xx M xx H. Toutes les séquences suivent les autorisations de leur fiche ; la notation n’autorise pas à ignorer une récupération. Les valeurs de frame sont calculées à 60 Hz et mesurées au premier contact possible, hors hitstop. Pour une attaque au sol, avantage = hitstun moins les frames actives restantes moins la récupération. Un projectile éloigné, un impact tardif et une attaque aérienne demandent une mesure distincte.

Les nombres de dégâts partent d’une vie de référence de 1000. Le premier, deuxième et troisième coups d’une séquence utilisent 100 %, 90 % et 80 % de leur valeur. Les estimations des deux combos noyau arrondissent chaque paquet de dégâts à l’entier le plus proche. Elles ne comptent ni bonus de rechargement ni compteur de dégâts additionnel. Le compteur de combo ne peut pas être réinitialisé artificiellement par une animation.

#### Normals et actions communes

Les poses sont propres à chaque personnage, tandis que ce premier socle partage les mêmes fenêtres pour rendre les premiers tests comparables. Une grosse arme n’obtient pas automatiquement une hitbox sur toute sa décoration. Les modifications futures de portée et de frames doivent déclencher une nouvelle vérification des combos.

| Code | Démarrage activité récupération | Dégâts | Garde | Contact |
| --- | --- | --- | --- | --- |
| 5L | 6 / 3 / 10 | 40 | -1 | 6 |
| 2L | 7 / 3 / 11 | 35 | -1 | 6 |
| 5M | 10 / 3 / 16 | 65 | -4 | 5 |
| 2M | 11 / 3 / 17 | 60 | -6 | 3 |
| 5H | 16 / 4 / 23 | 95 | -7 | 10 |
| 2H | 13 / 4 / 25 | 85 | -10 | Variable |
| 6M | 21 / 3 / 21 | 70 | -9 | 3 |
| jM | 9 / 5 / 0 | 60 | Variable | Variable |
| TH | 8 / 2 / 28 | 110 | Variable | Variable |
| ROLL | 5 / 18 / 16 | 0 | Variable | Variable |
| RELOAD | 1 / 0 / 71 | 0 | Variable | Variable |

La projection normale démarre en 8 frames et offre 12 frames de déchoppe. Une projection spéciale démarre ici en 12 frames, échoue sur une cible aérienne ou déjà en hitstun et reste punissable à vide. Le launcher 2H crée un état de chute spécifique ; ses 42 frames de trajectoire ne sont pas un avantage au sol. j.M possède 6 frames d’atterrissage, son avantage dépend de la hauteur.

Le rechargement normal dure 72 frames. La fenêtre parfaite couvre 34 à 43 incluses et termine le chargement à la frame 44. Les fenêtres sûres couvrent 27 à 33 puis 44 à 50, avec fin à 60. Un échec ajoute 30 frames et ne permet pas de retenter pendant la même action. Le bonus parfait concerne les deux prochaines actions d’arme et vaut 10 %. La roulade consomme 25 points d’endurance. Son évitement des projectiles hauts ne protège pas contre une attaque basse ou une projection.

#### Les douze combattants du noyau

Chaque fiche propose quatre spéciaux, deux supers et deux exécutions. Une super de niveau 1 coûte 100 points, une super de niveau 2 coûte 200. Les exécutions ont lieu après la dernière manche gagnée ; leurs colonnes de dégâts et de frames de combat restent sans objet. Elles ne se combinent pas à un combo pour tuer automatiquement une cible encore active.

##### Marcus Fenix

Référence : Gears of War 2006. Costume de base : Armure de campagne du premier jeu et bandana noir. Archétype : polyvalent à confirmation. Armes prévues : Lancer Mk II; Gnasher.

Principe de jeu : Alternance Lancer et Gnasher pour contrôler la moyenne distance puis convertir au contact; rechargement parfait commun donnant 10 pour cent de dégâts sur les deux prochaines actions d’arme.. Contrôle visuel : Bandana, visage massif, armure segmentée, masses des épaules et baïonnette tronçonneuse.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Rafale Lancer courte | 236L | 12 / 4 / 18 | 85 | -8 / 4 |
| S2 Gnasher de rupture | 214M | 18 / 3 / 25 | 115 | -16 / Variable |
| S3 Percée à la tronçonneuse | 236H | 23 / 6 / 29 | 130 | -20 / Variable |
| S4 Sortie de couvert | 214E | 20 / 1 / 16 | 0 | Variable / Variable |
| U1 Percée Delta | 236236M | 9 / 5 / 36 | 240 | -23 / Variable |
| U2 Désignation orbitale | 236236H | 30 / 12 / 44 | 340 | -25 / Variable |
| E1 Baïonnette tronçonneuse | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 Fin de service | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Trois impacts au contact traités comme un paquet de combo; les projectiles plus loin modifient les avantages. Ressource : 1 munition.

**S2** — Forte portée proche, faible dégâts après la distance optimale; recul lourd sans mur infini. Ressource : 1 munition.

**S3** — Course courte engagée; vulnérable aux projections et aux coups bas; animation complète si échec. Ressource : Aucune.

**S4** — Recul d’un demi-corps puis choix tir ou garde; aucun objet nouveau ajouté au décor classé. Ressource : Aucune.

**U1** — Frappe de crosse d’ouverture puis rafale rapprochée. Le premier coup touche au sol et peut conclure un combo. Ressource : 100 jauge.

**U2** — Marteau de l’Aube signalé au sol; disponible seulement avec satellite autorisé par le ruleset; variante classée en salve cinématique extérieure. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 139 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 12 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 346 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 9 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Marcus vérifie le chargeur près d’un abri effondré. Réplique : « On ouvre un passage. Après, on rentre. »

Rival : Général RAAM. RAAM barre la sortie; Marcus désigne le corridor derrière lui.

Fin originale hors continuité : Marcus laisse la route ouverte pour les survivants et rejoint Delta avant l’aube.

Référence de corpus : https://www.gearsofwar.com/en-us/games/gears-of-war/

##### Dominic Santiago

Référence : Gears of War 2006. Costume de base : Armure de campagne du premier jeu. Archétype : pression rapprochée et secours. Armes prévues : Gnasher; Lancer Mk II.

Principe de jeu : La roulade ouvre une unique transition offensive; récupération punissable si elle est anticipée. Contrôle visuel : Visage et pilosité du premier épisode, plaques de poitrine et proportions distinctes de Marcus.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Gnasher de contact | 236L | 11 / 3 / 17 | 90 | -7 / 5 |
| S2 Roulade offensive | 214M | 17 / 5 / 23 | 105 | -12 / Variable |
| S3 Crochet de sauvetage | 623M | 9 / 4 / 29 | 95 | -18 / Variable |
| S4 Fumigène de progression | 214H | 25 / 1 / 21 | 0 | Variable / Variable |
| U1 Retour à la ligne | 236236M | 8 / 5 / 35 | 235 | -22 / Variable |
| U2 Pour l’escouade | 236236H | 13 / 6 / 43 | 335 | -27 / Variable |
| E1 Dégagement brutal | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 Dernière couverture | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Tir court qui conserve Dom près de sa cible; très faible conversion à longue portée. Ressource : 1 munition.

**S2** — Roulade puis frappe; choix de freinage interdit après la première frame offensive. Ressource : Aucune.

**S3** — Anti-air de proximité; invulnérable aux attaques aériennes frames 5 à 12, pas aux tirs au sol. Ressource : Aucune.

**S4** — Nuage non opaque avec contours de combattants visibles. Réduit la lisibilité des préparations sans masquer les hitboxes. Ressource : 1 grenade.

**U1** — Frappe montante, déplacement court et tir de Gnasher; ouverture compatible avec hitstun. Ressource : 100 jauge.

**U2** — Percée au fusil à pompe terminée par une projection scénarisée, seulement si le premier coup touche. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 143 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 11 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 342 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 8 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Dom relève un casque dans les gravats puis le repose. Réplique : « Je ne laisse personne derrière cette ligne. »

Rival : Skorge. Skorge coupe la retraite; Dom avance pour offrir une fenêtre à son escouade.

Fin originale hors continuité : Dom compte les survivants à l’abri. Le dernier siège du transport reste réservé à celui qui manque.

Référence de corpus : https://www.gearsofwar.com/en-us/games/gears-of-war/

##### Damon Baird

Référence : Gears of War 3. Costume de base : Tenue de campagne Gears of War 3. Archétype : pièges mécaniques et contrôle. Armes prévues : Lancer Mk II; grenades fragmentation.

Principe de jeu : Deux emplacements de grenade maximum; préparation visible; l’adversaire peut détruire un piège. Contrôle visuel : Cheveux blonds, lunettes sur le front, tenue de campagne du même épisode que les armes.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Rafale de contrôle | 236L | 13 / 4 / 18 | 80 | -7 / 4 |
| S2 Grenade fixée | 214M | 27 / 1 / 20 | 120 | Variable / Variable |
| S3 Déclencheur | 236M | 8 / 2 / 22 | 90 | -13 / Variable |
| S4 Réglage mécanique | 214E | 24 / 1 / 15 | 0 | Variable / Variable |
| U1 Mauvaise connexion | 236236M | 10 / 5 / 36 | 230 | -24 / Variable |
| U2 Chaîne de démolition | 236236H | 17 / 10 / 40 | 330 | -25 / Variable |
| E1 Dernier réglage | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 Circuit fermé | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Rafale horizontale à trajectoire fixe; le joueur doit tenir la bonne distance. Ressource : 1 munition.

**S2** — Arme un piège après 30 frames supplémentaires; deux pièges maximum, destructibles par un coup. Ressource : 1 grenade.

**S3** — Déclenche le piège le plus ancien. Sans piège, geste vide de 32 frames; aucun coup instantané sans signal. Ressource : Piège déjà armé.

**S4** — Réglage du prochain rechargement : normal 72 vers 64 frames, sûr 60 vers 52 ; parfait reste à 44. Les fenêtres de confirmation ne changent pas. Effet perdu à la première interruption. Ressource : Aucune.

**U1** — Coup de crosse initial puis explosion dirigée d’une grenade propulsée; ne demande pas un piège préparé. Ressource : 100 jauge.

**U2** — Trois détonations successives signalées; ne crée pas une chaîne récursive avec les pièges déjà actifs. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 135 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 13 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 338 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 10 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Baird démonte un déclencheur défectueux sans quitter l’adversaire des yeux. Réplique : « Laisse-moi deviner. Encore un problème de conception. »

Rival : Ukkon. Ukkon réclame le terrain; Baird détruit un dispositif avant de répondre.

Fin originale hors continuité : Baird rétablit un relais avec des pièces récupérées, puis efface le plan de sa démonstration.

Référence de corpus : https://news.xbox.com/en-us/2019/12/11/gears-5-operation-2-free-for-all-available-today-for-all-players/

##### Augustus Cole

Référence : Gears of War 3. Costume de base : Tenue de campagne Gears of War 3. Archétype : rush et projections. Armes prévues : Gnasher; Lancer Mk II.

Principe de jeu : Élan construit par déplacement vers l’avant; perdu sur garde prolongée ou coup reçu. Contrôle visuel : Visage de Cole, gabarit puissant, équipement de campagne; tenue thrashball traitée séparément.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Percussion Cole | 236L | 12 / 4 / 16 | 90 | -6 / 6 |
| S2 Percée de mêlée | 236H | 22 / 7 / 28 | 130 | -19 / Variable |
| S3 Envol de ligne | 623M | 10 / 4 / 29 | 100 | -18 / Variable |
| S4 Contact décisif | 63214H | 12 / 2 / 33 | 135 | Variable / Variable |
| U1 Passage en force | 236236M | 9 / 6 / 35 | 245 | -23 / Variable |
| U2 Cole Train | 236236H | 14 / 8 / 42 | 345 | -27 / Variable |
| E1 Plaquage final | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 La ligne tient | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Épaule au contact; bonus de distance avec élan, mais mêmes frames de démarrage et aucun bonus de dégâts. Ressource : Aucune.

**S2** — Charge rectiligne avec un impact d’armure frames 10 à 18; les projections ignorent l’armure. Ressource : Élan.

**S3** — Anti-air au bras et à l’épaule; animation calée sur son poids sans double saut. Ressource : Aucune.

**S4** — Projection spéciale; ne prend jamais une cible en hitstun ou en blockstun. Démarrage de 12 frames, plus lent que la projection normale; réponse par saut ou recul. Ressource : Aucune.

**U1** — Frappe initiale puis enchaînement de charges; ouverture de type frappe, pas une projection de commande. Ressource : 100 jauge.

**U2** — Course cinématique et projection après confirmation; traînée stylisée réservée au super de cette adaptation. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 143 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 12 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 350 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 9 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Cole frappe son épaulière et avance vers la ligne. Réplique : « Cette ligne-là, on la tient ensemble. »

Rival : Warden. Le Warden abat ses masses; Cole lui indique l’espace qu’il devra traverser.

Fin originale hors continuité : Cole transforme un poste de secours en lieu de rassemblement. Il garde la porte pendant que les autres soufflent.

Référence de corpus : https://news.xbox.com/en-us/2020/03/31/gears-5-operation-3-gridiron-available-today-for-all-players/

##### Anya Stroud

Référence : Gears of War 3. Costume de base : Tenue de combat de campagne. Archétype : tirs précis et contre-attaque. Armes prévues : Lancer Mk II; Snub.

Principe de jeu : Marquage bref créé par une attaque confirmée; donne un suivi tactique visible sans visée automatique. Contrôle visuel : Chevelure blonde et armure de terrain Gears of War 3; ne pas fusionner avec sa tenue de contrôle.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Rafale mesurée | 236L | 12 / 3 / 18 | 80 | -7 / 5 |
| S2 Snub d’interception | 623M | 10 / 3 / 26 | 90 | -15 / Variable |
| S3 Tir de couverture | 214M | 20 / 4 / 25 | 105 | -14 / Variable |
| S4 Lecture tactique | 214E | 6 / 12 / 27 | 0 | Variable / Variable |
| U1 Ligne de feu | 236236M | 9 / 4 / 36 | 230 | -23 / Variable |
| U2 Ordre confirmé | 236236H | 18 / 9 / 41 | 325 | -25 / Variable |
| E1 Dernier ordre | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 Canal fermé | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Rafale courte sans auto-aim; un hit crée une marque de 120 frames. Ressource : 1 munition.

**S2** — Tir diagonal anti-air; ne suit pas une cible après le départ du projectile. Ressource : 1 munition.

**S3** — Tir reculé qui consomme la marque pour un déplacement supplémentaire, sans dégâts additionnels. Ressource : Marque facultative.

**S4** — Fenêtre de contre de projectile; si le timing réussit, annule le projectile et recule. Échec entièrement punissable. Ressource : Aucune.

**U1** — Frappe de crosse suivie de tirs concentrés; au contact, conclut un combo sans marque préalable. Ressource : 100 jauge.

**U2** — Marquage visuel puis salve cadrée à l’extérieur; ordre cinématique original, pas pouvoir canonique personnel. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 135 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 12 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 338 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 9 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Anya coupe une transmission et prend place au premier rang. Réplique : « Message reçu. Je suis déjà sur place. »

Rival : Reine Myrrah. Myrrah ordonne le retrait humain; Anya refuse de transmettre cet ordre.

Fin originale hors continuité : Anya rallume une balise d’évacuation et reste jusqu’au passage du dernier véhicule.

Référence de corpus : https://news.xbox.com/en-us/2020/11/17/gears-5-operation-5/amp/

##### Kait Diaz

Référence : Gears 5. Costume de base : Tenue hivernale du chapitre enneigé. Archétype : mobilité et ambiguïté visuelle. Armes prévues : Gnasher; Lancer Mk II.

Principe de jeu : Dissimulation courte inspirée de sa capacité Horde; silhouette et signe de départ restent visibles en duel. Contrôle visuel : Bonnet, cheveux, veste hivernale et accessoires provenant du même costume; aucune combinaison de tenues.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Gnasher oblique | 236L | 11 / 3 / 17 | 85 | -7 / 5 |
| S2 Frappe furtive | 214M | 20 / 4 / 24 | 110 | -14 / Variable |
| S3 Pas latéral | 214E | 8 / 12 / 18 | 0 | Variable / Variable |
| S4 Couteau de proximité | 623M | 10 / 4 / 26 | 95 | -16 / Variable |
| U1 Traque rapprochée | 236236M | 8 / 5 / 36 | 235 | -23 / Variable |
| U2 Silence de l’Essaim | 236236H | 15 / 7 / 42 | 335 | -26 / Variable |
| E1 À portée de lame | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 Choisir sa voie | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Pas offensif court et tir proche; la direction est fixée avant le flash de bouche. Ressource : 1 munition.

**S2** — Courte transition de dissimulation; une silhouette de bord conserve la position lisible. Ressource : 1 charge de furtivité.

**S3** — Déplacement latéral sur l’axe 2D; traverse uniquement les projectiles hauts au milieu du mouvement. Ressource : 1 charge de furtivité.

**S4** — Anti-air bref sans poursuite automatique ni saut supplémentaire. Ressource : Aucune.

**U1** — Frappe initiale visible puis Gnasher; aucun cross-up automatique à l’activation. Ressource : 100 jauge.

**U2** — Enchaînement original de déplacements furtifs et de tirs; aucune autorité mentale sur l’Essaim attribuée à la joueuse. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 139 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 11 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 342 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 8 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Kait serre son équipement et observe le mouvement de la ruche au loin. Réplique : « Je choisis moi-même la direction. »

Rival : Reine Myrrah. Myrrah tente de définir sa place; Kait répond en avançant.

Fin originale hors continuité : Kait referme son carnet de piste. La route qu’elle trace appartient à ceux qui la suivent librement.

Référence de corpus : https://www.gearsofwar.com/en-us/games/gears-5/

##### Général RAAM

Référence : Gears of War 2006. Costume de base : Armure du combat final du premier jeu. Archétype : colosse de proximité et kryll. Armes prévues : Lame de RAAM; Troïka comme super.

Principe de jeu : Les Kryll protègent brièvement ou attaquent; ces deux états sont mutuellement exclusifs. Contrôle visuel : Armure noire à rivets, silhouette massive, lame et proportions de la tête du premier jeu.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Lame du général | 236L | 14 / 4 / 19 | 100 | -8 / 5 |
| S2 Poigne du général | 63214H | 12 / 2 / 35 | 155 | Variable / Variable |
| S3 Nuée de Kryll | 236M | 24 / 8 / 25 | 110 | -16 / Variable |
| S4 Manteau de Kryll | 214E | 18 / 30 / 18 | 0 | Variable / Variable |
| U1 Marche d’exécution | 236236M | 11 / 5 / 37 | 255 | -25 / Variable |
| U2 Feu de Troïka | 236236H | 24 / 18 / 44 | 360 | -28 / Variable |
| E1 Lame du commandant | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 La Horde avance | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Entaille de portée moyenne; frappe simple compatible avec un hit confirmé de 5L. Ressource : Aucune.

**S2** — Projection de commande à portée courte; échoue contre saut et hitstun. Démarrage de 12 frames, plus lent que la projection normale; réponse par saut ou recul. Ressource : Aucune.

**S3** — Les Kryll quittent RAAM et suivent une trajectoire annoncée; il perd leur protection jusqu’au retour. Ressource : 1 charge de nuée.

**S4** — Protège d’un seul impact balistique; les coups de mêlée et projections ignorent l’effet. Ressource : 1 charge de nuée.

**U1** — Frappe de lame initiale puis saisie cinématique; une saisie autonome ne serait pas autorisée pendant hitstun. Ressource : 100 jauge.

**U2** — Arme lourde mise en batterie avec grande anticipation; aucune marche pendant la rafale. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 151 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 14 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 358 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 11 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : RAAM entre dans la lumière; les Kryll restent dans son ombre. Réplique : « La surface cédera. »

Rival : Marcus Fenix. Marcus garde le dernier passage; RAAM abaisse sa lame.

Fin originale hors continuité : Dans cette fin alternative, la bannière locuste apparaît sur une place silencieuse; aucune victoire canonique n’est réécrite.

Référence de corpus : https://news.xbox.com/en-us/2019/10/16/all-new-heroes-and-villains-are-available-today-in-gears-5/

##### Skorge

Référence : Gears of War 2. Costume de base : Équipement du duel dans le palais. Archétype : allonge et pression aérienne limitée. Armes prévues : Bâton à double tronçonneuse; Gorgon.

Principe de jeu : Bâton à deux tronçonneuses; saut offensif avec trajectoire engagée; pas de téléportation. Contrôle visuel : Crête, silhouette Kantus, bâton entier à deux extrémités; pas deux épées sans justification de pose.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Balayage du bâton | 236L | 13 / 4 / 18 | 85 | -7 / 5 |
| S2 Descente tranchante | 214M | 24 / 5 / 27 | 115 | -17 / Variable |
| S3 Rotation de défense | 623M | 11 / 5 / 30 | 100 | -20 / Variable |
| S4 Poison du prêtre | 214H | 26 / 1 / 22 | 70 | Variable / Variable |
| U1 Duel des deux lames | 236236M | 10 / 6 / 36 | 245 | -24 / Variable |
| U2 Fureur du Kantus | 236236H | 16 / 10 / 42 | 345 | -28 / Variable |
| E1 Bâton scellé | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 Appel de la Horde | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Une seule extrémité de la double tronçonneuse touche; portée bornée et pas de hitbox sur toute la rotation. Ressource : Aucune.

**S2** — Petit bond puis attaque haute; la trajectoire est fixe et lisible. Ressource : Aucune.

**S3** — Anti-air à grande allonge; aucun blocage automatique des projectiles. Ressource : Aucune.

**S4** — Grenade avec zone de danger de 90 frames; dégâts plafonnés à une application par cible. Ressource : 1 grenade.

**U1** — Frappe initiale de bâton puis succession de coupes; animation originale avec arme intégrale. Ressource : 100 jauge.

**U2** — Deux passages à hauteur différente avec intervalle visible; pas de téléportation. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 139 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 13 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 350 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 10 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Skorge fait tourner son bâton sans toucher le sol. Réplique : « La Horde entend vos pas. »

Rival : Dominic Santiago. Dom refuse de reculer; le bâton cesse de tourner un instant.

Fin originale hors continuité : Dans cette fin alternative, Skorge rejoint les profondeurs pendant qu’une porte monumentale se referme.

Référence de corpus : https://news.xbox.com/en-us/2020/11/17/gears-5-operation-5/amp/

##### Reine Myrrah

Référence : Gears of War 3. Costume de base : Armure royale de Gears of War 3. Archétype : commandement et occupation de l’espace. Armes prévues : Boltok de l’arsenal multijoueur; commandes Locustes.

Principe de jeu : Ordres rythmés matérialisés par signaux de Locustes; une aide active maximum et interruption possible. Contrôle visuel : Visage, chevelure et armure royale; Tempest demeure un boss séparé à son échelle.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Boltok royal | 236L | 12 / 3 / 18 | 80 | -7 / 5 |
| S2 Ordre de barrage | 236M | 25 / 7 / 26 | 110 | -17 / Variable |
| S3 Repli souverain | 214E | 9 / 12 / 21 | 0 | Variable / Variable |
| S4 Ordre de siège | 214H | 29 / 6 / 28 | 120 | -18 / Variable |
| U1 Sentence royale | 236236M | 10 / 5 / 36 | 235 | -24 / Variable |
| U2 Ombre de Tempest | 236236H | 26 / 12 / 45 | 350 | -29 / Variable |
| E1 Sentence exécutée | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 Dernier sujet | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Arme issue du sandbox multijoueur; son attribution à ce kit n’affirme pas une arme personnelle en campagne. Ressource : 1 munition.

**S2** — Un auxiliaire locuste apparaît brièvement à une entrée fixe; pas d’invocation supplémentaire tant qu’il est actif. Ressource : 1 ordre.

**S3** — Recul avec garde seulement après la fin de la pose; ne traverse pas l’adversaire. Ressource : Aucune.

**S4** — Signal au sol avant projectile en cloche; l’ordre peut être interrompu et n’attaque pas depuis une zone invisible. Ressource : 1 ordre.

**U1** — Coup de crosse initial puis salve coordonnée; première frappe personnelle pour garantir une confirmation de combo. Ressource : 100 jauge.

**U2** — Passage de Tempest hors de l’axe jouable et tir signalé. Le boss complet conserve un autre ruleset et ses propres dimensions. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 135 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 12 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 342 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 10 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Myrrah observe les ruines depuis le bord de l’arène. Réplique : « Un ordre suffit lorsque chacun connaît sa place. »

Rival : Anya Stroud. Anya conteste son ordre de soumission; Myrrah appelle son garde.

Fin originale hors continuité : Dans cette fin alternative, Myrrah contemple une ville conquise. Le tableau reste celui de l’arcade hors continuité.

Référence de corpus : https://news.xbox.com/en-us/2020/03/31/gears-5-operation-3-gridiron-available-today-for-all-players/

##### Drone locuste

Référence : Gears of War 2006. Costume de base : Drone de base du premier jeu. Archétype : pression stable et rafales. Armes prévues : Hammerburst; grenades fragmentation.

Principe de jeu : Hammerburst de l’épisode retenu; rafales courtes, pas une cadence hybride entre variantes d’arme. Contrôle visuel : Peau, dents, torse, protections et arme du Drone de base; distinguer Disciple et Grenadier.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Hammerburst court | 236L | 12 / 4 / 18 | 85 | -8 / 4 |
| S2 Charge locuste | 236H | 22 / 6 / 28 | 120 | -18 / Variable |
| S3 Grenade de secteur | 214M | 27 / 1 / 22 | 110 | Variable / Variable |
| S4 Coup de crosse montant | 623M | 10 / 4 / 28 | 95 | -17 / Variable |
| U1 Avancée de la Horde | 236236M | 10 / 5 / 36 | 235 | -23 / Variable |
| U2 Secteur anéanti | 236236H | 20 / 12 / 43 | 330 | -27 / Variable |
| E1 Brutalité de la Horde | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 Terrain conquis | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Rafale horizontale, cadence verrouillée à l’arme de l’épisode choisi. Ressource : 1 munition.

**S2** — Percée à la crosse avec récupération longue; aucune immunité aux tirs. Ressource : Aucune.

**S3** — Lancer en cloche avec trajectoire déterministe et rebond unique. Ressource : 1 grenade.

**S4** — Anti-air court qui perd contre coups au sol à bonne distance. Ressource : Aucune.

**U1** — Crosse initiale puis rafales alternées; pas de renfort supplémentaire imposé au match. Ressource : 100 jauge.

**U2** — Grenade et rafale prolongée, signal d’explosion unique et plafonnement des impacts. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 139 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 12 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 342 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 10 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Le Drone ajuste son Hammerburst dans les gravats. Réplique : « La voie est à nous. »

Rival : Damon Baird. Baird neutralise son accès; le Drone se tourne vers lui.

Fin originale hors continuité : Le Drone rejoint sa colonne et disparaît dans une brèche. Le statut individuel reste celui d’un soldat anonyme.

Référence de corpus : https://news.xbox.com/en-us/2019/12/11/gears-5-operation-2-free-for-all-available-today-for-all-players/

##### Kantus

Référence : Gears of War 2. Costume de base : Prêtre Kantus standard. Archétype : déni de zone et rituel. Armes prévues : Gorgon; grenade empoisonnée.

Principe de jeu : Chant vulnérable; en duel produit une charge temporaire, en coopération un soutien plafonné. Contrôle visuel : Morphologie élancée, cou et crâne, ornements du prêtre standard; pas l’armure du Kantus blindé.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Gorgon court | 236L | 12 / 4 / 18 | 75 | -7 / 5 |
| S2 Grenade toxique | 214M | 27 / 1 / 24 | 90 | Variable / Variable |
| S3 Cri de rupture | 623M | 16 / 6 / 26 | 90 | -17 / Variable |
| S4 Rituel de la Horde | 214E | 30 / 1 / 24 | 0 | Variable / Variable |
| U1 Chant de guerre | 236236M | 11 / 6 / 37 | 225 | -25 / Variable |
| U2 Liturgie du siège | 236236H | 24 / 14 / 44 | 320 | -28 / Variable |
| E1 Silence du profane | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 Rite terminé | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Rafale rapprochée qui sert de conversion fiable malgré sa faible puissance brute. Ressource : 1 munition.

**S2** — Zone toxique de 120 frames; une seule zone, dégâts limités et disparition au KO. Ressource : 1 grenade.

**S3** — Onde courte qui interrompt les attaques proches; traduction 2D originale du rôle de prêtre. Ressource : 1 charge de rite.

**S4** — Récupère une charge de rite si non interrompu. Pas de régénération de vie en duel classé. Ressource : Aucune.

**U1** — Impact initial de Gorgon puis onde rituelle scénarisée; première collision au sol au contact. Ressource : 100 jauge.

**U2** — Trois pulsations annoncées; une seule consommation de charge et pas de boucle de soin. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 131 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 12 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 334 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 11 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Le Kantus entame un chant bref au pied d’une porte. Réplique : « La Horde se relève. »

Rival : Gabe Diaz. Gabe coupe les lignes de soutien; le Kantus interrompt son rite.

Fin originale hors continuité : Le Kantus rassemble les survivants de sa cohorte dans une chambre souterraine.

Référence de corpus : https://www.gearsofwar.com/en-nz/news/dev-blog-enemies/

##### Garde Theron

Référence : Gears of War 2006. Costume de base : Garde Theron standard. Archétype : charge et punition à distance. Armes prévues : Torque Bow; lame de l’arc.

Principe de jeu : Arc à tension en trois paliers annoncés; les tirs chargés exposent l’utilisateur pendant la préparation. Contrôle visuel : Casque, plaques, jupe d’armure et forme de l’arc; garde et sentinelle ne sont pas mélangés.

| Action | Commande | Frames D A R | Dégâts | Garde et contact |
| --- | --- | --- | --- | --- |
| S1 Flèche courte | 236L | 14 / 3 / 19 | 90 | -8 / 5 |
| S2 Arc à tension | 236H maintenu | 32 / 3 / 30 | 150 | -21 / Variable |
| S3 Crochet de l’arc | 623M | 12 / 4 / 28 | 95 | -17 / Variable |
| S4 Flèche en cloche | 214M | 26 / 4 / 27 | 110 | -18 / Variable |
| U1 Garde du palais | 236236M | 11 / 5 / 37 | 240 | -24 / Variable |
| U2 Sentence à tension | 236236H | 25 / 7 / 45 | 345 | -28 / Variable |
| E1 Pointe du palais | L+H après victoire | Cinématique | Variable | Variable / Variable |
| E2 Dernière flèche | M+H après victoire | Cinématique | Variable | Variable / Variable |

**S1** — Tir non chargé à courte portée; temps de trajet au contact inclus dans le démarrage annoncé. Ressource : 1 flèche.

**S2** — Trois paliers à 32, 50 et 68 frames; dégâts 150, 170 et 190; signal sonore et visuel distinct à chaque palier. Ressource : 1 flèche.

**S3** — Frappe physique anti-air avec la lame de l’arc; pas de projectile instantané. Ressource : Aucune.

**S4** — Tir à courbe fixe qui force un déplacement, sans verrouillage automatique. Ressource : 1 flèche.

**U1** — Coup de lame d’ouverture puis flèche à bout portant; garantie de contact pour conclure une route. Ressource : 100 jauge.

**U2** — Flèche renforcée à grand signal d’armement; projectile esquivable à distance sans cinématique forcée. Ressource : 200 jauge.

**Combo 2L > 5L xx S1** — 143 dégâts estimés, coût de jauge 0 ; la munition ou ressource de S1 reste requise. 2L donne +6, 5L démarre à 6: lien juste. Annulation sur première frame active de 5L vers S1 à 14 frames, inférieur aux 18 frames de hitstun de 5L. Au contact et centre écran; trajet de projectile nul ou inclus dans S1.

**Combo 5H > 5M xx U1** — 346 dégâts estimés, coût de jauge 100 ; aucune munition supplémentaire pour U1. 5H donne +10, 5M démarre à 10: lien juste. Annulation sur première frame active de 5M vers U1 à 11 frames, inférieur aux 23 frames de hitstun de 5M. Coup lourd au contact; recul plafonné pour que 5M atteigne.

Introduction originale : Le Garde Theron tend son arc et immobilise sa visée. Réplique : « Le passage est fermé. »

Rival : Mikayla Dorn. Mikayla cherche un angle; le Theron répond par un nouveau point de garde.

Fin originale hors continuité : Le Theron reprend son poste devant une porte close, dans une vignette indépendante de l’issue des campagnes.

Référence de corpus : https://news.xbox.com/en-us/2020/03/31/gears-5-operation-3-gridiron-available-today-for-all-players/

#### Les vingt quatre combattants de l’extension

Ces combattants disposent chacun de trois signatures. Leur kit complet devra encore ajouter les spéciaux, supers secondaires, exécutions et routes de combo nécessaires au même niveau de finition que le noyau. Les mécaniques sont distinctes : soutien, charge, champ de contrôle, surchauffe, vol bas, barrière, longue portée et double arme ne partagent pas une unique fiche recolorée.

##### JD Fenix

Référence : Gears 5, tenue de campagne gears 5 après le prologue. Artilleur à fenêtre de tir. Marque une zone puis déclenche une salve annoncée; éviter les tirs gratuits hors écran.

- **Grenade GL balisée** (236M) : Projectile à courbe et zone annoncée; une seule marque. Démarrage 24 frames, dégâts 120, coût 0.
- **Recul de commandement** (214E) : Recul court consommant une marque pour réduire la récupération. Démarrage 9 frames, dégâts 0, coût 0.
- **Barrage orbital** (236236H) : Super 200, salves fixes successives, première zone toujours visible. Démarrage 28 frames, dégâts 335, coût 200.

Rival de parcours : Warden. Introduction originale : Je prends la responsabilité du tir.

Fin originale : JD démonte les marqueurs du champ de bataille et consigne chaque décision avant le retour de l’escouade.

##### Del Walker

Référence : Gears 5, tenue de campagne gears 5. Défense technique et surveillance. Balise qui informe puis protège une seule zone; pas de tourelle autonome permanente.

- **Balise de surveillance** (214M) : Pose destructible qui révèle le prochain déplacement proche. Démarrage 24 frames, dégâts 0, coût 0.
- **Rafale de réparation** (236L) : Tir confirmé recharge une fraction de la balise, jamais des PV gratuits. Démarrage 13 frames, dégâts 85, coût 0.
- **Couloir défendu** (236236H) : Super 200, salve bornée à une moitié d’écran annoncée. Démarrage 25 frames, dégâts 325, coût 200.

Rival de parcours : Drone locuste. Introduction originale : On garde une issue. Toujours.

Fin originale : Del utilise les pièces sauvées pour rétablir un poste de communication pour les réfugiés.

##### Fahz Chutani

Référence : Gears 5, tenue de campagne gears 5. Tireur à lecture. Précision acquise à l’arrêt; révélation de position par la visée; tir évitable par changement de hauteur.

- **Visée patiente** (214M) : Préparation immobile 30 frames; perd sa charge sur déplacement. Démarrage 30 frames, dégâts 0, coût 0.
- **Longshot direct** (236H) : Tir unique à signal visuel; hauteur haute esquivable accroupi. Démarrage 24 frames, dégâts 135, coût 0.
- **Tir calculé** (236236H) : Super 200, premier tir vers une position fixée avant le déclenchement. Démarrage 18 frames, dégâts 335, coût 200.

Rival de parcours : Garde Theron. Introduction originale : Bouge encore. J’apprends vite.

Fin originale : Fahz laisse le premier transport aux blessés et rejoint la garde arrière sans commentaire.

##### Clayton Carmine

Référence : Gears of War 3, tenue de campagne gears of war 3. Tank et riposte balistique. Absorption ponctuelle convertie en pression; aucun blindage permanent contre les projections.

- **Encaissement balistique** (214E) : Absorbe un projectile, jamais une projection; riposte exige nouvelle entrée. Démarrage 14 frames, dégâts 0, coût 0.
- **Mulcher en appui** (236H) : Rafale immobile; ventiler ensuite; ne se conserve pas en déplacement. Démarrage 26 frames, dégâts 145, coût 0.
- **Mur Carmine** (236236H) : Super 200, tir dévié puis charge; fenêtre de contre visible. Démarrage 16 frames, dégâts 350, coût 200.

Rival de parcours : Grenadier locuste. Introduction originale : Essayez de me faire bouger.

Fin originale : Clayton aligne plusieurs casques sur un établi, puis en prend un seul pour repartir.

##### Lizzie Carmine

Référence : Gears 5, tenue de campagne gears 5. Pilote mobile et pièges lourds. Gèle temporairement une trajectoire puis prépare un appel Silverback de courte durée.

- **Freinage tactique** (214M) : Glissade courte qui pose une zone de ralentissement annoncée. Démarrage 20 frames, dégâts 80, coût 0.
- **Salve de pilote** (236M) : Tir avec petit recul; consomme la charge de mobilité. Démarrage 14 frames, dégâts 90, coût 0.
- **Sortie Silverback** (236236H) : Super 200, insertion temporaire du véhicule; silhouette et sortie distinctes. Démarrage 30 frames, dégâts 345, coût 200.

Rival de parcours : Warden. Introduction originale : La route est fermée. Je vais la rouvrir.

Fin originale : Dans cette fin alternative hors continuité, Lizzie remet le moteur en route et ramène son convoi à l’abri.

##### Victor Hoffman

Référence : Gears 5 multijoueur, hoffman en armure du lot opération 6. Commandant à ordres limités. Choisit un ordre parmi discipline, couverture et repli; changement d’ordre punissable.

- **Ordre de discipline** (214L) : Choisit une prochaine rafale à faible recul, changement punissable. Démarrage 25 frames, dégâts 0, coût 0.
- **Boltok d’autorité** (236M) : Tir lent mais forte pression à portée moyenne. Démarrage 17 frames, dégâts 105, coût 0.
- **Ligne infranchissable** (236236H) : Super 200, ordre de barrage sur zone annoncée et temporisée. Démarrage 24 frames, dégâts 330, coût 200.

Rival de parcours : Général RAAM. Introduction originale : Un ordre clair. Une sortie pour chacun.

Fin originale : Hoffman marque une nouvelle route sur la carte et laisse une équipe contrôler les issues.

##### Tai Kaliso

Référence : Gears of War 2, tenue de campagne gears of war 2. Défenseur à lecture et punition. Garde de préparation qui résiste à un impact; perd contre projection et attaques répétées.

- **Garde du guerrier** (214E) : Encaisse un coup de mêlée hors projection durant une fenêtre brève. Démarrage 12 frames, dégâts 0, coût 0.
- **Retour de Gnasher** (236M) : Punition de proximité après une lecture; pas d’invulnérabilité. Démarrage 15 frames, dégâts 110, coût 0.
- **Résistance de Kaliso** (236236H) : Super 200, frappe lourde initiale et enchaînement d’armes de campagne. Démarrage 13 frames, dégâts 345, coût 200.

Rival de parcours : Skorge. Introduction originale : Je connais le poids de cette ligne.

Fin originale : Dans cette fin alternative, Tai dépose un signe de passage près de l’abri, puis rejoint ceux qu’il a protégés.

##### Dizzy Wallin

Référence : Gears of War 2, tenue de pilote de betty. Pièges de terrain et anti-rush. Piège fixé au sol et tir retardé; récompense la préparation sans immortalité de couvert.

- **Piège de conducteur** (214M) : Grenade fixée après délai; un seul dispositif destructible. Démarrage 28 frames, dégâts 115, coût 0.
- **Gnasher de dégagement** (236M) : Tir proche avec recul du tireur. Démarrage 16 frames, dégâts 105, coût 0.
- **Betty tient la route** (236236H) : Super 200, séquence thématique de défense d’un véhicule; véhicule seulement cinématique. Démarrage 27 frames, dégâts 330, coût 200.

Rival de parcours : Général RAAM. Introduction originale : Vous discuterez après le démarrage.

Fin originale : Dizzy remet une plaque sur le moteur et transforme le véhicule en transport pour les survivants.

##### Samantha Byrne

Référence : Gears of War 3, tenue de campagne gears of war 3. Tireuse mobile et changements d’angle. Pas court pendant l’armement d’un tir; deux trajectoires lisibles plutôt qu’un tir omnidirectionnel.

- **Pas de tir** (214M) : Déplacement bref préparant deux angles fixes à sélectionner. Démarrage 12 frames, dégâts 0, coût 0.
- **Longshot mobile** (236H) : Tir après le pas; interdit pendant la translation elle-même. Démarrage 22 frames, dégâts 125, coût 0.
- **Couverture croisée** (236236H) : Super 200, deux tirs de positions successives, aucune téléportation. Démarrage 18 frames, dégâts 330, coût 200.

Rival de parcours : Garde Theron. Introduction originale : Un angle libre. Ça me suffit.

Fin originale : Sam transmet un itinéraire dégagé et repart vérifier elle-même le dernier croisement.

##### Garron Paduk

Référence : Gears of War Judgment, tenue de kilo squad dans judgment. Duel à distance et intimidation. Les tirs de Markza récompensent l’espacement; intimidation réduit temporairement la garde sans dégâts gratuits.

- **Markza mesuré** (236M) : Tir semi-auto qui récompense une portée optimale. Démarrage 17 frames, dégâts 100, coût 0.
- **Intimidation UIR** (214M) : Cri court de proximité; retire un peu de jauge de garde, jamais de PV. Démarrage 24 frames, dégâts 0, coût 0.
- **Verdict de Kilo** (236236H) : Super 200, rafale précise puis percussion de crosse. Démarrage 14 frames, dégâts 335, coût 200.

Rival de parcours : Reine Myrrah. Introduction originale : Je ne combats pas pour vos décorations.

Fin originale : Paduk arrache un panneau militaire inutile et le remplace par une indication vers le refuge.

##### Sofia Hendrik

Référence : Gears of War Judgment, tenue de kilo squad dans judgment. Mobilité disciplinée et secours. Repositionnement en deux temps avec choix de couverture ou de contre; aucun soin infini.

- **Pas de cadette** (214E) : Deux sorties, garde ou contre, avec signe de posture distinct. Démarrage 10 frames, dégâts 0, coût 0.
- **Riposte disciplinée** (236M) : Crosse puis rafale; faible portée, bon retour au neutre. Démarrage 13 frames, dégâts 90, coût 0.
- **Protocole de Kilo** (236236H) : Super 200, ouverture de mêlée et tirs couvrant une évacuation imagée. Démarrage 12 frames, dégâts 325, coût 200.

Rival de parcours : Drone locuste. Introduction originale : Le protocole commence par ramener les vivants.

Fin originale : Sofia consigne le rapport de mission puis inscrit les noms des personnes évacuées avant les objectifs détruits.

##### Gabe Diaz

Référence : Gears Tactics, tenue de campagne de base avant personnalisation. Soutien offensif. Exécution confirmée procure un ordre utilisable une seule fois; pas de tour supplémentaire littéral dans un jeu temps réel.

- **Ordre offensif** (214M) : Prépare une ressource de support après 28 frames exposées. Démarrage 28 frames, dégâts 0, coût 0.
- **Lancer de soutien** (236M) : Rafale consomme l’ordre pour réduire le recul, pas de double dégât. Démarrage 14 frames, dégâts 95, coût 0.
- **Escouade ralliée** (236236H) : Super 200, percée personnelle suivie d’une courte assistance cadrée. Démarrage 15 frames, dégâts 335, coût 200.

Rival de parcours : Ukkon. Introduction originale : Une ouverture suffit. Préparez-vous.

Fin originale : Gabe distribue le matériel récupéré aux survivants et repart avant que le poste soit devenu confortable.

##### Sid Redburn

Référence : Gears Tactics, tenue de campagne de base. Vanguard et disruption. Intimidation à courte portée ouvre la garde; résistance active de durée limitée.

- **Intimidation Vanguard** (214M) : Courte zone de perturbation; requiert proximité et démarre lentement. Démarrage 23 frames, dégâts 70, coût 0.
- **Charge Retro** (236H) : Charge baïonnette, ligne fixe, récupération importante. Démarrage 24 frames, dégâts 135, coût 0.
- **Briser le front** (236236H) : Super 200, coup de crosse initial puis charge au Retro Lancer. Démarrage 13 frames, dégâts 345, coût 200.

Rival de parcours : Ukkon. Introduction originale : Cette fois, on termine la mission.

Fin originale : Sid range un dossier fermé et assure personnellement la garde de nuit.

##### Mikayla Dorn

Référence : Gears Tactics, tenue de campagne de base. Sniper et préparation. Position d’observation unique; quitter la pose annule la précision bonus.

- **Poste d’observation** (214E) : Pose stationnaire; une seule position active et aucune invisibilité. Démarrage 28 frames, dégâts 0, coût 0.
- **Longshot préparé** (236H) : Tir haut, forte récupération, bénéficie seulement de la pose active. Démarrage 25 frames, dégâts 140, coût 0.
- **Angle mort** (236236H) : Super 200, visée annoncée puis tir qui garde sa trajectoire de départ. Démarrage 20 frames, dégâts 340, coût 200.

Rival de parcours : Garde Theron. Introduction originale : Tu ne passeras pas vers les miens.

Fin originale : Mikayla rend aux civils une rue praticable et forme une nouvelle sentinelle à surveiller l’horizon.

##### Reine Reyna

Référence : Gears 5 multijoueur, reine reyna du lot opération 6. Contrôle organique et saisies. Extensions organiques séparées du hurtbox central; attaques de portée longue avec récupération élevée.

- **Fouet de l’Essaim** (236M) : Allonge organique avec hurtbox exposée sur l’appendice. Démarrage 19 frames, dégâts 115, coût 0.
- **Entrave organique** (214H) : Saisie de sol annoncée; échoue contre saut et contre cible en hitstun. Démarrage 30 frames, dégâts 140, coût 0.
- **Couronne de l’Essaim** (236236H) : Super 200, projections organiques sur zones signalées. Démarrage 26 frames, dégâts 350, coût 200.

Rival de parcours : Kait Diaz. Introduction originale : La ruche n’oublie aucune voix.

Fin originale : Dans cette fin alternative, une pulsation traverse la ruche. Aucun destin canonique de Kait n’est imposé par cet ending.

##### Lahni Kaliso

Référence : Gears 5 Hivebusters, tenue de campagne hivebusters. Mêlée et charge électrique. Electroblade dure un temps court avec consommation à chaque coup; pression puissante mais à faible portée.

- **Lame d’ouverture** (236L) : Percée de très courte portée au couteau. Démarrage 10 frames, dégâts 85, coût 0.
- **Electroblade** (214H) : Charge temporaire plafonnée; chaque attaque électrique consomme une unité. Démarrage 25 frames, dégâts 0, coût 0.
- **Arc de Scorpio** (236236H) : Super 200, premier coup de lame puis impulsions électriques de portée courte. Démarrage 9 frames, dégâts 340, coût 200.

Rival de parcours : Warden. Introduction originale : Je passe en premier. Restez près de moi.

Fin originale : Lahni retrouve Scorpio au point d’extraction et coupe sa charge électrique avant d’aider les blessés.

##### Keegan

Référence : Gears 5 Hivebusters, tenue de campagne hivebusters. Soutien de munitions et explosifs. Resupply crée une zone limitée; le combattant doit y rester exposé pour récupérer des ressources.

- **Resupply** (214M) : Zone de munitions à occupation requise, durée et rendement plafonnés. Démarrage 30 frames, dégâts 0, coût 0.
- **Boomshot de couverture** (236H) : Projectile lent en cloche, explosion annoncée à l’impact. Démarrage 27 frames, dégâts 135, coût 0.
- **Réserve de Scorpio** (236236H) : Super 200, tirs explosifs successifs sans recharge pendant la cinématique. Démarrage 23 frames, dégâts 345, coût 200.

Rival de parcours : Kantus. Introduction originale : Il reste de quoi ouvrir la sortie.

Fin originale : Keegan partage les réserves restantes avant de prendre sa propre part.

##### Mac

Référence : Gears 5 Hivebusters, tenue de campagne hivebusters. Bouclier mobile et arme de poing. Barrier s’oriente au déclenchement et s’épuise; les attaques arrière et projections restent une réponse.

- **Barrier** (214E) : Bouclier frontal orienté au départ; pas de rotation automatique. Démarrage 20 frames, dégâts 0, coût 0.
- **Boltok derrière la ligne** (236M) : Tir lent permis avec Barrier mais réduit sa durée. Démarrage 17 frames, dégâts 100, coût 0.
- **Avancée de Scorpio** (236236H) : Super 200, charge de bouclier comme première frappe puis tirs de Boltok. Démarrage 12 frames, dégâts 335, coût 200.

Rival de parcours : Drone de l’Essaim. Introduction originale : Cette fois, la barrière tient.

Fin originale : Mac observe le départ du transport, puis abaisse enfin sa barrière au milieu du silence.

##### JACK

Référence : Gears 5, robot de soutien de campagne. Vol bas et outils. Hauteur flottante limitée par une jauge; boîte de collision centrale persistante; pas de camping aérien.

- **Arc électrique** (236M) : Tir court avec distance maximale stricte. Démarrage 14 frames, dégâts 85, coût 0.
- **Décalage de vol** (214E) : Monte ou descend d’une seule hauteur; batterie drainée pendant la hauteur haute. Démarrage 12 frames, dégâts 0, coût 0.
- **Surcharge de soutien** (236236H) : Super 200, impulsion après signal; ne neutralise pas toutes les commandes adverses. Démarrage 21 frames, dégâts 320, coût 200.

Rival de parcours : DeeBee. Introduction originale : Signal sonore original sans imitation de voix.

Fin originale : JACK recharge sur un établi pendant que les voyants d’un poste de secours se rallument.

##### DeeBee

Référence : Gears of War 4, unité shepherd standard. Robot à surchauffe. Enforcer alimente une jauge de chaleur; ventilation forcée punitive si le joueur prolonge les rafales.

- **Enforcer en rafale** (236M) : Rafale augmente chaleur; interdite au seuil de surchauffe. Démarrage 13 frames, dégâts 95, coût 0.
- **Ventilation forcée** (214E) : Réduit chaleur avec une fenêtre de 46 frames entièrement punissable. Démarrage 24 frames, dégâts 0, coût 0.
- **Protocole de suppression** (236236H) : Super 200, rafale lourde puis ventilation imposée; pas d’autodestruction gratuite. Démarrage 19 frames, dégâts 330, coût 200.

Rival de parcours : JACK. Introduction originale : Périmètre contesté. Intervention en cours.

Fin originale : Le DeeBee classe la zone comme accessible et rejoint une colonne de réparation.

##### Warden

Référence : Gears 5, warden standard de campagne. Deux masses et rupture de garde. Deux armes lourdes alternent zones d’impact; casque segmenté visuel et armure temporaire limitée.

- **Masse gauche** (236M) : Frappe de sol à grand rayon; côté de frappe annoncé. Démarrage 22 frames, dégâts 135, coût 0.
- **Masse droite** (214H) : Overhead lent; peut casser une armure temporaire, pas une garde entière. Démarrage 28 frames, dégâts 145, coût 0.
- **Garde brisée** (236236H) : Super 200, coup initial lourd puis alternance des deux masses. Démarrage 17 frames, dégâts 360, coût 200.

Rival de parcours : Augustus Cole. Introduction originale : La ruche garde ce seuil.

Fin originale : Le Warden reprend sa place devant l’entrée de la ruche, comme un poste de garde redevenu silencieux.

##### Drone de l’Essaim

Référence : Gears of War 4, drone standard de campagne. Pression au sol et prises. Prise au contact puis recul; arme de référence et configuration exactes à verrouiller avant génération.

- **Rafale de l’Essaim** (236M) : Rafale au recul variable borné, trajectoire déterministe. Démarrage 15 frames, dégâts 95, coût 0.
- **Prise de chasse** (63214H) : Projection courte avec recul après succès; impossible pendant hitstun. Démarrage de 12 frames, plus lent que la projection normale; réponse par saut ou recul. Démarrage 12 frames, dégâts 135, coût 0.
- **Pression de ruche** (236236H) : Super 200, frappe puis tirs, sans contrôle mental ou téléportation ajoutés. Démarrage 14 frames, dégâts 335, coût 200.

Rival de parcours : Kait Diaz. Introduction originale : La prise revient à la ruche.

Fin originale : Le Drone rejoint une procession dans les profondeurs; l’ending montre sa fonction de troupe.

##### Ukkon

Référence : Gears Tactics, scientifique de campagne. Invocations limitées et zones. Un spécimen de petite taille actif à la fois; ses ordres ont une anticipation et une récupération visibles.

- **Spécimen libéré** (214M) : Une petite invocation destructible avec trajet annoncé; pas de boss miniature. Démarrage 30 frames, dégâts 95, coût 0.
- **Ordre d’expérience** (236M) : Donne une commande au spécimen; échec visible si aucune invocation. Démarrage 18 frames, dégâts 105, coût 0.
- **Expérience interdite** (236236H) : Super 200, laboratoire imagé en arrière-plan et attaque bornée au plan du duel. Démarrage 28 frames, dégâts 340, coût 200.

Rival de parcours : Gabe Diaz. Introduction originale : Chaque résistance apporte une donnée.

Fin originale : Dans cette fin alternative, Ukkon referme un carnet de résultats et disparaît dans son laboratoire.

##### Grenadier locuste

Référence : Gears Tactics, grenadier standard. Gnasher et rage contrôlée. Une jauge monte quand il subit des dégâts puis s’épuise pendant sa charge; résistance et contre ne se cumulent pas.

- **Gnasher en rage** (236M) : Tir proche, recul accru en mode rage mais aucune armure simultanée. Démarrage 14 frames, dégâts 110, coût 0.
- **Charge enragée** (236H) : Consomme jauge de rage pour progresser; pas de boucle de gain pendant charge. Démarrage 24 frames, dégâts 130, coût 0.
- **Brèche de l’assaut** (236236H) : Super 200, percussion puis tirs rapprochés; aucune grenade hors écran. Démarrage 15 frames, dégâts 345, coût 200.

Rival de parcours : Clayton Carmine. Introduction originale : Plus près.

Fin originale : Le Grenadier rassemble son groupe autour d’une brèche fraîche et repart vers la ligne suivante.

#### Armes et traduction en duel

Le choix d’une arme engage une forme, une animation et un rythme. Les capacités de chargeur de l’adaptation sont des unités de combat ; elles ne prétendent pas reproduire les capacités militaires de l’arme canonique. Les balles tracées dans une rafale ne doivent pas multiplier artificiellement le compteur de combo quand la fiche décrit un paquet de dégâts unique.

| Famille | Identité visuelle à conserver | Fonction de combat proposée | Réponse offerte au défenseur |
| --- | --- | --- | --- |
| Lancer Mk II | Fusil et baïonnette tronçonneuse de la version retenue | Rafale et engagement de mêlée | Garde, roulade haute, punition de récupération |
| Retro Lancer | Baïonnette rigide et silhouette propre | Charge engagée et forte pression proche | Saut ou recul avant engagement |
| Gnasher | Gabarit et mécanisme du fusil à pompe | Conversion de proximité | Espacement et punition à vide |
| Snub et Boltok | Deux armes de poing distinctes | Tirs courts versus coups plus lourds | Variation de hauteur et rythme |
| Hammerburst | Variante liée à un épisode | Rafale de portée moyenne | Approche entre deux séquences |
| Longshot | Silhouette du fusil de précision | Tir préparé à forte récupération | Accroupissement et attaque de la visée |
| Torque Bow | Arc, tension et projectile propres | Charge annoncée puis menace lourde | Interruption ou déplacement avant tir |
| Boomshot | Lanceur lourd et projectile en cloche | Explosion de zone | Sortie de zone signalée |
| Markza | Fusil distinct du Longshot | Tir semi-auto et espacement | Avancer entre les tirs |
| Enforcer | Arme de robot de la bonne génération | Rafale et surchauffe | Forcer une longue séquence puis punir |
| Lancer GL | Module lance-grenade spécifique | Tir en cloche et marquage | Quitter le marqueur avant impact |
| Troïka et Mulcher | Armes lourdes clairement séparées | Mise en batterie et rafale | Mobilité pendant installation |
| Bâton de Skorge | Deux tronçonneuses aux extrémités | Allonge et rotations engagées | Punition de l’extrémité manquée |
| Electroblade | Capacité de Lahni dans Hivebusters | Charge électrique de courte portée | Attendre l’épuisement ou contrôler la distance |
| Breaker Maces | Paire de masses du Warden | Alternance de zones lourdes | Lire le bras et exploiter le retour |
| Hammer of Dawn | Désignation et condition orbitale | Super à signal prolongé | Sortie de la zone et interruption du ciblage |

#### Routes individuelles et mise en scène

Chaque route comporte cinq duels, un rival, une rencontre Boss Battle et un duel final, suivis d’un ending indépendant. Les adversaires des duels sont tous distincts pour éviter une répétition involontaire. La route enregistre les identifiants, le besoin d’arène, l’introduction et les règles de chaque étape. La défaite au boss autorise une reprise au boss dans le réglage standard ; la variante d’endurance peut imposer d’autres ressources, annoncées avant le départ.

Les 36 introductions, scènes de rivalité et fins sont livrées comme synopsis originaux. Elles fournissent une direction de mise en scène et une phrase d’introduction. Elles ne constituent pas encore des scripts de doublage complets, des vidéos ou des dessins d’ending. Le texte prononcé par JACK demeure un signal sonore original ; on ne lui invente pas un acteur humain à imiter.

L’écran de fin conserve une image propre au personnage, un court épilogue et le retour au menu. Une version courte passe l’exécution et affiche directement le résultat. L’unlock récompense une illustration ou une entrée de galerie, sans modifier les dégâts du personnage en tournoi.

#### Tests des kits et réponses adverses

Les liens temporels des 24 combos du noyau satisfont les fenêtres inscrites : 2L à +6 vers 5L à 6 frames, puis annulation vers S1 dans les 18 frames de hitstun ; 5H à +10 vers 5M à 10 frames, puis annulation vers U1 dans les 23 frames de hitstun. Ces preuves restent conditionnées au contact réel, au recul et aux hitboxes. Le moteur doit tester défense enregistrée, contre attaque la plus rapide, saut et roulade à chaque liaison.

Les projections spéciales ne prennent pas une cible en hitstun. Un super qui conclut un combo possède donc une frappe d’ouverture, puis seulement une saisie cinématique. Les invocations de Myrrah et Ukkon ont une limite explicite, une arrivée signalée et un moyen d’interruption. Le chant du Kantus ne produit pas une boucle de soin en duel. L’armure de RAAM et Clayton ne couvre pas les projections. La furtivité de Kait conserve un indice de position. Ces règles sont des conditions de lisibilité, pas des capacités officiellement attribuées à ces personnages dans tous leurs épisodes.

Chaque kit doit réussir quatre essais avant validation : neutralité sans ressource, punition d’un spécial raté, réponse disponible à la mécanique dominante, puis combat entier sans boucle. L’intégration finale ajoute les tests de collisions pour les paires S contre XL et pour les saisies entre humain, Locuste, Essaim et robot.

#### Sources de référence des personnages

- Série et premier épisode : https://www.gearsofwar.com/en-us/games/gears-of-war/
- Kilo Squad dans Judgment : https://www.gearsofwar.com/en-gb/games/gears-of-war-judgment/
- Héros de Tactics : https://www.gearsofwar.com/en-nz/news/dev-blog-characters/
- Ennemis de Tactics : https://www.gearsofwar.com/en-nz/news/dev-blog-enemies/
- RAAM, DeeBee et Warden : https://news.xbox.com/en-us/2019/10/16/all-new-heroes-and-villains-are-available-today-in-gears-5/
- Baird, Lizzie et Drone locuste : https://news.xbox.com/en-us/2019/12/11/gears-5-operation-2-free-for-all-available-today-for-all-players/
- Cole, Clayton, Myrrah et Theron : https://news.xbox.com/en-us/2020/03/31/gears-5-operation-3-gridiron-available-today-for-all-players/
- Dom et Paduk : https://news.xbox.com/en-us/2020/07/14/gears-operation-4-brothers-in-arms/
- Anya, Tai, Dizzy et Skorge : https://news.xbox.com/en-us/2020/11/17/gears-5-operation-5/amp/
- Hoffman et Reine Reyna : https://www.xbox.com/fr-fr/games/store/gears-5-operation-6-bundle/9nblc6fv6spg
- Scorpio dans Hivebusters : https://www.gearsofwar.com/en-us/news/hivebusters/
- Capacités de Lahni, Keegan et Mac : https://news.xbox.com/en-us/2020/12/08/gears-5-hivebusters-arrives-december-15/
- Références E-Day : https://news.xbox.com/en-us/2026/06/07/gears-of-war-eday-direct-xbox-games-showcase-2026/

Références consultées le 19 novembre 2026. Elles établissent des identités, appartenances ou capacités selon le texte de chaque page. La fidélité détaillée des assets est un contrôle visuel séparé.

## Boss, arenes et campagne

Source complète : [boss_stages_story.md](../docs/boss_stages_story.md).

Chapitre de conception conservé : ses nombres de contenu décrivent le noyau V1, sauf mentions V12 explicites.

### Boss Battle arènes et campagne

Cette partie de la bible définit 24 rencontres de boss, 24 arènes décomposées en 144 calques et une anthologie de 12 chapitres. Elle sert de cahier de production : chaque rencontre possède une logique de contre-jeu, des parties ciblables et une issue. Les données chiffrées sont des propositions d’équilibrage à 60 images de simulation par seconde. Les fiches ne signifient pas que 24 combats ou 144 images ont déjà été produits.

La fidélité recherchée porte sur les silhouettes, les costumes, les armes, les matières et les événements de l’épisode retenu. Le passage au plan de combat 2D demande des cadrages et des mécanismes originaux. Le dossier signale ces créations au lieu de les attribuer aux jeux officiels. Les sources primaires établissent les faits qu’elles couvrent ; les détails renseignés depuis des guides ou un wiki doivent ensuite être confrontés à une capture du jeu de référence.

#### Principes du mode Boss Battle

Le joueur sélectionne son personnage, son costume, un boss et un règlement. Il peut lancer une chasse individuelle, un circuit de trois ou cinq rencontres, un siège d’objectif, un entraînement d’interception ou une session coopérative à deux. Les rencontres débloquées en histoire sont immédiatement disponibles en entraînement avec choix de phase. Le mode libre accepte le roster entier ; le mode Histoire conserve les personnages présents dans la scène de référence.

Une créature géante ne doit pas être ramenée arbitrairement à la taille d’un combattant humain. Les plus petits boss entrent entièrement dans le cadre, les géants présentent un corps au second plan avec membres et organes qui rejoignent le plan jouable, et les colosses utilisent une arène de siège. Les ratios de hauteur indiqués dans les fiches sont des outils de cadrage, jamais des tailles officielles de l’univers. Le zoom s’arrête dès que la lecture du personnage et de ses commandes devient trop difficile ; le reste du boss peut sortir du cadre.

Le joueur garde ses déplacements, sa garde, ses normales, ses spéciaux et ses ressources de duel. Un personnage orienté corps à corps doit pouvoir terminer chaque boss : une patte se pose, une tête descend, un module reste accessible ou un outil de stage crée l’ouverture. Les équipements de siège appartiennent au décor. Ils ne modifient pas rétroactivement le moveset canonique du personnage et ne remplacent pas les armes du personnage dans les autres modes.

##### Boucle de rencontre

Chaque séquence suit une lecture simple : observation, avertissement, attaque, récupération, punition. Un avertissement combine posture, signal sonore et forme au sol. La couleur seule n’est jamais le seul indice. La zone visée est verrouillée avant l’impact ; un boss ne suit pas instantanément le joueur pendant toute son esquive. Les attaques majeures laissent au moins une zone accessible sans dégâts, même si un partenaire se trouve de l’autre côté de l’écran.

Les trois phases sont prévues sur les bandes de santé 100 à 70 %, 70 à 35 % et 35 à 0 %. Le franchissement d’un seuil déclenche une transition à la fin de l’action active, avec un bref arrêt lisible. Les membres détruits et les objectifs accomplis restent détruits ou accomplis. Aucun seuil ne restaure des points de vie pour prolonger artificiellement la rencontre. Un super peut franchir un seuil, mais la phase suivante débute après son animation et les dégâts excédentaires restent comptés.

Les durées chiffrées sont des objectifs de prototype. Une alerte de 90 images dure 1,5 seconde à 60 Hz ; une fenêtre de punition de 120 images dure 2 secondes. La difficulté augmente d’abord la complexité des enchaînements et réduit l’aide à la visée. Elle ne supprime pas les avertissements ni les réponses possibles. Les invulnérabilités longues doivent se terminer par un retour à portée ou un outil utilisable, afin que le joueur ne passe pas la moitié du combat à attendre.

##### Parties du corps et réactions

Chaque boss expose une jauge centrale et au plus trois jauges de module simultanées. Les autres éléments sont indiqués dans le bestiaire, puis révélés lorsqu’ils deviennent pertinents. Toucher une surface blindée produit une réaction distincte, un faible gain de stabilité et aucun faux nombre de dégâts. Un organe vulnérable répond avec une animation nette. La destruction d’un canon supprime réellement son attaque des phases ultérieures ; elle ne se limite pas à un changement de texture.

Les grands boss ne subissent pas les projections de duel. Une prise sur une cible incompatible devient une courte attaque de stabilité, définie par personnage et annoncée dans sa fiche de commandes. Les supers gardent leur identité mais utilisent un cadrage adapté : pas de téléportation du Kraken dans une cinématique de corps à corps humain. La caméra ne change pas de côté au milieu d’un coup. Les coups des deux joueurs peuvent contribuer à la même ouverture sans multiplication incontrôlée du hitstop.

##### Solo et coopération

En solo, chaque capture possède une issue accessible au joueur capturé. Les interrupteurs et outils demandent une action simple, réalisable avec toutes les configurations de commandes. Une charge de matériel indispensable revient si elle a été consommée sans rendre la victoire possible. Le mode Histoire propose une reprise au seuil de phase ; les circuits de chasse reprennent au début de rencontre pour que le score reste comparable.

En coopération à deux, une base de PV multipliée par 1,65 sert de point de départ au réglage. Cette valeur doit être mesurée selon le boss. Les dégâts et le nombre de projectiles ne doublent pas mécaniquement. La cible d’une attaque est annoncée, les pièges ne se superposent pas en une zone inévitable et la caméra garde les deux joueurs visibles. Une mise à terre autorise un sauvetage limité ; le boss attend la fin de son signal avant de viser la zone d’un sauvetage, ce qui crée un choix de placement sans offrir une invulnérabilité gratuite.

##### Circuits et objectifs

| Circuit | Rencontres proposées | Compétence principale | Règlement |

|---|---|---|---|

| Première chasse | Berserker, Snatcher, Swarmak | Lire et punir | Trois rencontres, soin entre combats |

| Monstres des profondeurs | Reaver, Leviathan, Hydra de Skorge | Interception et portée | Score cumulé, outils de scène garantis |

| Fabrique d’Ukkon | Brumak, Corpser, Hydra d’Ukkon | Démontage de modules | Pas de réinitialisation des modules entre phases |

| Défense de Sera | Tempest, Hive Beast, Kraken | Objectif de siège | Jauge d’objectif séparée des PV |

| Interception CGU | Silverback, Centaur, King Raven | Mobilité et angles | Simulation, appareil neutralisé intact |

| Galangi | Flock, Carrier, Wakaatu | Contrôle du sol | Dossier libre hors continuité de campagne |

Le score additionne dégâts utiles, interruptions, destruction de modules et secours. Le temps reste un critère distinct afin qu’un joueur ne soit pas pénalisé deux fois pour la même erreur. Aucun bonus de dégâts permanent ne se débloque pour les modes de duel classé. Les récompenses sont des variantes de décor, poses, fiches de bestiaire, titres et options de visualisation. Les classements séparent solo, coopération, difficulté et assistance ; les simulations de véhicules ne sont pas présentées comme des victoires historiques contre la CGU.

#### Catalogue des rencontres

##### Berserker

**Référence** : Gears of War 2006. **Type** : Créature terrestre. **Priorité** : P0. **Échelle de cadrage** : 2,3 hauteurs humaines. Berserker et relation à la chaleur appuyées ici par une source secondaire ; page officielle pour le contexte du premier jeu. Sources [BB01], [BB02].

**Parties ciblables** : Face pendant le cri, pour détourner son attention; Torso et membres uniquement après exposition thermique.

**Phase 1 de 100 à 70 % — Écoute.** La tête se fige puis s’oriente vers la dernière action bruyante. Avertissement prévu : 72 images. Charge rectiligne sur la position mémorisée, une seule correction au début. Contre-jeu : Marcher pour éviter de signaler sa position ; tirer une fois pour provoquer puis esquiver latéralement dans le plan. Fenêtre de punition prévue : 90 images.

**Phase 2 de 70 à 35 % — Carapace chauffée.** Une sirène et un cercle au sol annoncent la disponibilité du Rayon de l’aube. Avertissement prévu : 90 images. Deux charges successives brisent une porte fictive de l’arène et révèlent une zone à ciel ouvert. Contre-jeu : L’attirer dans la zone découverte, maintenir le marqueur puis frapper la carapace chauffée. Le marqueur est un outil du stage accessible à tous. Fenêtre de punition prévue : 150 images.

**Phase 3 de 35 à 0 % — Dernière poursuite.** Cri plus long et griffes raclant le sol avant une charge triple. Avertissement prévu : 102 images. Triple charge avec repos obligatoire après le troisième passage. Contre-jeu : Ne pas rouler trop tôt ; employer le temps mort pour refroidir son arme ou engager un combo de contact sur le flanc. Fenêtre de punition prévue : 120 images.

**Victoire** : Vider la jauge après au moins une vulnérabilisation ; exécution contextuelle de 3 secondes avec coup final assisté du Rayon de l’aube. **Défaite** : Jauge du combattant à zéro ; pas de mort automatique sur une charge en difficulté normale.

**Solo** : Une balise fixe garantit que les personnages de mêlée peuvent créer l’ouverture ; la jauge thermique ne décroît pas pendant une cinématique. **Coopération** : Le bruit le plus récent fixe la cible ; indicateur de poursuite au-dessus du joueur visé. Les autres peuvent installer la balise.

**Contrôle visuel** : Ne pas lui ajouter d’yeux humains ni d’armure mécanique ; préserver sa silhouette et sa peau propres au premier jeu. **Récompense** : Emblème de chasse et scène de bestiaire, sans bonus de statistiques PvP.

##### Corpser

**Référence** : Gears Tactics. **Type** : Arachnide géant de siège. **Priorité** : P0. **Échelle de cadrage** : 7,0 hauteurs humaines. Sources officielles confirmant le Corpser, ses pattes blindées levées, impacts télégraphiés et mines dans Tactics. Sources [BB03], [BB04].

**Parties ciblables** : Dessous des pattes levées; Abdomen pendant le recul.

**Phase 1 de 100 à 70 % — Pattes dressées.** Deux pattes s’élèvent et des bandes texturées marquent leurs futurs impacts. Avertissement prévu : 84 images. Deux frappes séparées, le premier impact ne masque pas le deuxième. Contre-jeu : Sortir des bandes puis attaquer la face interne de la patte levée ; les armes courtes touchent une articulation avancée. Fenêtre de punition prévue : 90 images.

**Phase 2 de 70 à 35 % — Champ de mines.** Les mandibules vibrent ; trois silhouettes de mines apparaissent avant le dépôt. Avertissement prévu : 96 images. Mines à retardement et frappe d’une patte sur la dernière position du joueur. Contre-jeu : Détruire une mine pour ouvrir un passage ; se placer à portée de la patte sans rester dans son ombre. Fenêtre de punition prévue : 108 images.

**Phase 3 de 35 à 0 % — Abdomen exposé.** Le boss lève quatre pattes, découvre le centre et laisse une bande de sécurité visible. Avertissement prévu : 120 images. Série de frappes alternées, puis recul découvrant l’abdomen. Contre-jeu : Mémoriser gauche, droite, centre ; la dernière frappe crée une occasion d’approcher. Les mines disparaissent avant le grand impact. Fenêtre de punition prévue : 150 images.

**Victoire** : Détruire les protections et épuiser la jauge centrale ; effondrement hors de la zone du joueur. **Défaite** : PV nuls ; rester coincé entre deux membres ne doit jamais provoquer une collision sans sortie.

**Solo** : Deux pattes au maximum portent une zone active simultanément. **Coopération** : Un indicateur par cible ; le boss ne superpose jamais deux zones sans issue. PV ×1,65 à deux joueurs.

**Contrôle visuel** : Chaque patte doit garder une attache anatomique lisible ; vérifier le nombre, les articulations et les plaques sur les références Tactics. **Récompense** : Dossier Corpser et variante nocturne purement visuelle.

##### Brumak

**Référence** : Gears Tactics. **Type** : Créature armée de siège. **Priorité** : P0. **Échelle de cadrage** : 8,0 hauteurs humaines. Brumak et armement lourd confirmés par les blogs officiels ; positions fines des réservoirs à verrouiller sur capture Tactics. Sources [BB03], [BB04].

**Parties ciblables** : Canons de bras; Réservoirs dorsaux après rotation; Tête après désarmement.

**Phase 1 de 100 à 70 % — Barrage.** Les canons prennent de la vitesse et leur ligne de tir est dessinée au sol. Avertissement prévu : 78 images. Rafale horizontale basse suivie d’un piétinement proche. Contre-jeu : Se baisser derrière le couvert bas puis profiter de la surchauffe pour viser le canon le plus proche. Fenêtre de punition prévue : 96 images.

**Phase 2 de 70 à 35 % — Salve de roquettes.** Les rails dorsaux s’illuminent ; quatre marqueurs au sol apparaissent dans l’ordre des départs. Avertissement prévu : 108 images. Roquettes en quatre zones espacées, verrouillées avant le départ. Contre-jeu : Traverser les espaces libres et attirer la rotation du monstre pour rendre son dos accessible. Fenêtre de punition prévue : 132 images.

**Phase 3 de 35 à 0 % — Désarmé.** Le Brumak secoue ses bras endommagés et pousse un cri court. Avertissement prévu : 90 images. Deux coups de poing et une morsure basse ; les projectiles détruits restent désactivés. Contre-jeu : Punir la morsure manquée sur la tête ; la jauge de stabilité ouvre un combo complet après trois contres. Fenêtre de punition prévue : 156 images.

**Victoire** : Désactiver au moins un armement puis finir le corps ; la destruction des modules est conservée entre phases. **Défaite** : PV nuls ou objectif défendu détruit uniquement dans la variante Siège.

**Solo** : Un couvert se répare pendant le recul du boss ; aucun équipement obligatoire dans le moveset. **Coopération** : La cible des roquettes et celle du canon sont annoncées séparément ; couvrir le partenaire produit du score sans modifier les dégâts PvP.

**Contrôle visuel** : Conserver les proportions des bras, les supports d’armes et le montage des lance-roquettes de Tactics ; ne pas mélanger automatiquement le Brumak de Gears 1. **Récompense** : Trophée d’armement et visualiseur des modules.

##### Reaver

**Référence** : Gears of War 2. **Type** : Monture volante. **Priorité** : P1. **Échelle de cadrage** : 3,8 hauteurs humaines. Blog officiel pour l’identité du Reaver ; variante Gears 2 et comportement détaillé à confirmer par capture. Sources [BB04], [BB05].

**Parties ciblables** : Tête; Nacelle armée; Tentacule posé au sol.

**Phase 1 de 100 à 70 % — Approche.** Battements ralentis, nacelle tournée vers le combattant. Avertissement prévu : 72 images. Passage à hauteur de tête avec une rafale courte. Contre-jeu : Garde haute ou roulade sous le passage ; punition du tentacule qui se pose en fin de trajectoire. Fenêtre de punition prévue : 78 images.

**Phase 2 de 70 à 35 % — Atterrissage.** Les pattes cherchent le sol et l’ombre se stabilise. Avertissement prévu : 84 images. Atterrissage suivi d’une ruée et de tirs du cavalier. Contre-jeu : Faire manquer la ruée puis neutraliser la nacelle ; l’atterrissage donne une vraie phase de corps à corps. Fenêtre de punition prévue : 108 images.

**Phase 3 de 35 à 0 % — Fuite contrariée.** Le cavalier tente une montée lente, armement visible. Avertissement prévu : 96 images. Alternance entre balayage aérien et brève recharge au sol. Contre-jeu : Viser la nacelle pendant la montée ou interrompre le décollage par une attaque lourde à l’articulation. Fenêtre de punition prévue : 132 images.

**Victoire** : Faire tomber la monture en neutralisant sa jauge centrale ; le cavalier fuit ou est évacué dans la version à violence réduite. **Défaite** : PV nuls ; aucun échec lié au fait que le boss quitte temporairement l’écran.

**Solo** : Toutes les 6 secondes au plus, un membre ou la tête passe à portée de mêlée. **Coopération** : Le second joueur peut détruire un projectile sans être forcé de choisir un tireur.

**Contrôle visuel** : Distinguer Reaver, Hydra et Tempest ; ne pas employer la même silhouette recolorée. **Récompense** : Entrée Reaver du bestiaire.

##### Leviathan

**Référence** : Gears of War 2. **Type** : Créature aquatique. **Priorité** : P1. **Échelle de cadrage** : 9,0 hauteurs humaines. Créature et rencontre Gears 2 documentées ici par source secondaire ; le découpage en trois phases est original. Sources [BB06].

**Parties ciblables** : Tentacules accrochés au pont; Œil exposé; Gueule ouverte lors de la fenêtre dédiée.

**Phase 1 de 100 à 70 % — Abordage.** L’eau gonfle, puis deux silhouettes de tentacules se dessinent sous la surface. Avertissement prévu : 90 images. Prise des bords du pont et coup transversal. Contre-jeu : Frapper le tentacule fixé pour libérer la largeur de combat ; les rebords ne sont jamais des trous mortels. Fenêtre de punition prévue : 96 images.

**Phase 2 de 70 à 35 % — Face émergée.** L’œil se tourne vers la passerelle et la bouche commence à s’ouvrir. Avertissement prévu : 108 images. Jet d’eau repoussant et morsure ciblée sur une moitié du pont. Contre-jeu : Se maintenir dans la moitié sûre ; décharger pendant la fermeture lente de la gueule. Fenêtre de punition prévue : 132 images.

**Phase 3 de 35 à 0 % — Dernière immersion.** Un sillage courbe traverse le fond ; l’ombre annonce le retour à gauche ou à droite. Avertissement prévu : 120 images. Deux émergences puis prise prolongée du pont. Contre-jeu : Briser la prise et envoyer la charge contextuelle fournie par l’arène, quelle que soit l’arme personnelle. Fenêtre de punition prévue : 156 images.

**Victoire** : Trois déséquilibres donnent accès au final ; le dernier bouton déclenche une charge fictive de l’arène et non un QTE obligatoire rapide. **Défaite** : PV nuls ; la stabilité du pont baisse seulement dans le défi expert optionnel.

**Solo** : Plateforme stable, attaques toujours annoncées à l’écran. **Coopération** : Répartition gauche et droite suggérée mais jamais obligatoire ; les deux joueurs peuvent secourir une prise.

**Contrôle visuel** : Le pont reste horizontal : les vagues en arrière-plan ne déplacent ni caméra ni hitboxes. **Récompense** : Décor lac souterrain pour la galerie.

##### Hydra de Skorge

**Référence** : Gears of War 2. **Type** : Poursuite aérienne. **Priorité** : P1. **Échelle de cadrage** : 10,0 hauteurs humaines. Monture de Skorge et poursuite attestées par les deux sources secondaires ; arène 2D sur plateforme est une adaptation. Sources [BB07], [BB08].

**Parties ciblables** : Griffe agrippée à la plateforme; Gueule au terme du rugissement; Armement de la monture.

**Phase 1 de 100 à 70 % — Chasse.** La tête apparaît à une extrémité et une trajectoire courbe est dessinée par son sillage. Avertissement prévu : 84 images. Poursuite avec tirs et prise d’une griffe. Contre-jeu : Se déplacer sur la plateforme puis frapper la griffe immobilisée ; tous les personnages atteignent cette zone. Fenêtre de punition prévue : 96 images.

**Phase 2 de 70 à 35 % — Saisie.** Les deux griffes s’écartent et le souffle devient continu. Avertissement prévu : 108 images. Tentative de saisie du support et rafales latérales. Contre-jeu : Détruire la jauge de prise avant fermeture ; une saisie ratée étourdit brièvement la monture. Fenêtre de punition prévue : 132 images.

**Phase 3 de 35 à 0 % — Face à face.** Skorge se redresse et la bouche se charge. Avertissement prévu : 120 images. Attaque frontale en trois temps, puis gueule exposée. Contre-jeu : S’abriter au centre pendant les deux premiers tirs, se décaler au troisième, puis utiliser l’arme embarquée. Fenêtre de punition prévue : 156 images.

**Victoire** : Briser la dernière prise et épuiser la jauge ; conclusion séparée du duel de Skorge au sol. **Défaite** : PV nuls ; la chute du support est une animation de défaite, pas un événement aléatoire.

**Solo** : La plateforme volant sur rail reste un sol jouable stable. **Coopération** : L’un gère la griffe tandis que l’autre intercepte les salves ; rôles interchangeables.

**Contrôle visuel** : Pas de simple zoom du Reaver : modèle Hydra et présence de Skorge à contrôler. **Récompense** : Scène de poursuite et chronomètre personnel.

##### Brumak Lambent

**Référence** : Gears of War 2. **Type** : Colosse muté. **Priorité** : P2. **Échelle de cadrage** : 11,0 hauteurs humaines. Final de Gears 2 soutenu par les pages secondaires ; trois cycles prolongés sont une proposition de jeu. Sources [BB09], [BB10].

**Parties ciblables** : Excroissances accessibles au bord du sol; Noyau vulnérable sous désignation orbitale.

**Phase 1 de 100 à 70 % — Mutation.** Des zones lumineuses pulsent avant chaque croissance. Avertissement prévu : 96 images. Tentacule bas puis pluie de fragments inertes autour des zones sûres. Contre-jeu : Frapper les appendices arrivant sur le plan et protéger le marqueur de désignation. Fenêtre de punition prévue : 108 images.

**Phase 2 de 70 à 35 % — Contamination.** Une ligne orange se propage sur la peau et préfigure la prochaine attaque. Avertissement prévu : 120 images. Trois projections au sol, espacement fixé et couloirs sûrs visibles. Contre-jeu : Éviter les flaques puis maintenir la désignation durant une fenêtre garantie sans projectile. Fenêtre de punition prévue : 150 images.

**Phase 3 de 35 à 0 % — Point de rupture.** Toutes les excroissances baissent en luminosité avant une grande pulsation. Avertissement prévu : 144 images. Dernière vague puis immobilité prolongée du noyau. Contre-jeu : Déclencher le Rayon de l’aube au moment indiqué ; le placement préalable décide du score, pas un martèlement de touches. Fenêtre de punition prévue : 180 images.

**Victoire** : Terminer trois cycles de désignation ; la scène de fin représente la fin de cette rencontre d’anthologie. **Défaite** : PV nuls ou balise détruite dans le défi optionnel ; reprise au début de phase en mode histoire.

**Solo** : La désignation est une action de stage, disponible même aux combattants locustes en exhibition. **Coopération** : Maintien de balise partagé ; aucune double pression simultanée imposée.

**Contrôle visuel** : Ne pas transformer la mutation en variante cosmétique jouable du Brumak ; taille, silhouettes et transformations spécifiques. **Récompense** : Final Gears 2 dans les archives.

##### Berserker Lambent

**Référence** : Gears of War 3. **Type** : Créature de charge et contamination. **Priorité** : P1. **Échelle de cadrage** : 2,7 hauteurs humaines. Existence et épisode appuyés par une source secondaire ; règles de flaques et fenêtres sont propres à l’adaptation. Sources [BB11].

**Parties ciblables** : Cavité thoracique ouverte; Membres pendant le retour de charge.

**Phase 1 de 100 à 70 % — Poitrine fermée.** Cri et ouverture brève de la poitrine avant la ruée. Avertissement prévu : 72 images. Charge laissant une trace dangereuse temporaire. Contre-jeu : Attendre l’ouverture pour attaquer puis traverser la trace dans un espace sans dépôt ; son bord est toujours net. Fenêtre de punition prévue : 84 images.

**Phase 2 de 70 à 35 % — Terrain contaminé.** Les veines s’allument dans l’ordre de la prochaine série de charges. Avertissement prévu : 96 images. Deux ruées en angle dans le plan puis décharge proche. Contre-jeu : Leurrer la première vers l’extérieur, garder un couloir central, frapper la poitrine au second arrêt. Fenêtre de punition prévue : 120 images.

**Phase 3 de 35 à 0 % — Instabilité.** Une respiration prolongée fait gonfler la cavité puis arrête les dépôts. Avertissement prévu : 114 images. Charge courte, choc de zone et longue récupération. Contre-jeu : Garder la distance au choc, revenir au contact lorsque la poitrine reste ouverte. Fenêtre de punition prévue : 144 images.

**Victoire** : Vider la jauge et quitter une zone finale clairement marquée ; option d’animation automatique en histoire. **Défaite** : PV nuls ; les flaques ne peuvent recouvrir plus de 45 % du sol utile.

**Solo** : Les flaques anciennes disparaissent avant une nouvelle paire de charges. **Coopération** : La dernière attaque bruyante attire la prochaine charge, avec marqueur de cible.

**Contrôle visuel** : Garder sa poitrine ouverte distincte de la Berserker normale et de la Matriarch. **Récompense** : Entrée Lambent et variante de lumière Anvil Gate.

##### Leviathan Lambent

**Référence** : Gears of War 3. **Type** : Siège naval. **Priorité** : P2. **Échelle de cadrage** : 12,0 hauteurs humaines. Variante de Gears 3 confirmée par source secondaire ; déroulé 2D proposé. Sources [BB12].

**Parties ciblables** : Tentacules sur le pont; Nodules lumineux; Gueule lors de l’appui aérien.

**Phase 1 de 100 à 70 % — Saisie du navire.** Le pont grince et les prises apparaissent au bord. Avertissement prévu : 96 images. Tentacules qui coupent une ligne de déplacement et jet acide télégraphié. Contre-jeu : Libérer d’abord un passage puis briser un nodule ; le tir ne remplace pas la possibilité de frapper les prises. Fenêtre de punition prévue : 108 images.

**Phase 2 de 70 à 35 % — Émergence.** Deux nodules brillent à tour de rôle, jamais ensemble à l’arrière du décor. Avertissement prévu : 114 images. Alternance de morsure et projection de matière au sol. Contre-jeu : Provoquer la morsure dans une moitié du pont et viser le nodule opposé pendant le recul. Fenêtre de punition prévue : 144 images.

**Phase 3 de 35 à 0 % — Appui coordonné.** Signal radio, faisceau de repérage puis gueule largement ouverte. Avertissement prévu : 132 images. Dernière vague de tentacules avant l’opportunité de désignation. Contre-jeu : Neutraliser une prise, déclencher l’appui de stage et finir le nodule central. Fenêtre de punition prévue : 168 images.

**Victoire** : Rompre les trois ancrages puis réussir la désignation finale ; fin cinématique brève. **Défaite** : PV nuls ou integrité du navire à zéro dans Siège expert.

**Solo** : Appui disponible automatiquement après la séquence correcte ; aucun personnage imposé. **Coopération** : Deux prises ciblent des zones distinctes ; la jauge d’appui progresse par toute attaque pertinente.

**Contrôle visuel** : Les tentacules n’occulteront pas les pieds des joueurs ; éviter de recycler le Leviathan Gears 2 sans reconstruction. **Récompense** : Séquence du Sovereign et trophée de défense.

##### Tempest et Myrrah

**Référence** : Gears of War 3. **Type** : Monture volante de siège. **Priorité** : P1. **Échelle de cadrage** : 8,5 hauteurs humaines. Tempest monté par Myrrah et contexte Azura documentés par sources secondaires ; équilibrage de la tour original. Sources [BB13], [BB14].

**Parties ciblables** : Gueule après le souffle; Carapace après désignation; Pattes pendant l’attaque de la tour.

**Phase 1 de 100 à 70 % — Souffle.** La tête se penche et une ligne lumineuse dessine la trajectoire. Avertissement prévu : 90 images. Souffle horizontal puis vol stationnaire à basse hauteur. Contre-jeu : Passer sous la ligne ou se mettre dans l’abri annoncé ; riposter vers la gueule. Fenêtre de punition prévue : 108 images.

**Phase 2 de 70 à 35 % — Assaut de la tour.** Myrrah pointe la tour ; la caméra élargit sans réduire les personnages sous le seuil de lisibilité. Avertissement prévu : 114 images. Le Tempest s’accroche à une structure et prépare un choc de siège. Contre-jeu : Briser la prise par les pattes à portée ; activer la désignation pour ouvrir la carapace. Fenêtre de punition prévue : 150 images.

**Phase 3 de 35 à 0 % — Dernier barrage.** Rugissement continu, toutes les sorties d’attaque restent visibles. Avertissement prévu : 132 images. Deux souffles séparés d’une zone neutre puis une tentative de siège lente. Contre-jeu : Changer d’abri au bon instant et consacrer la dernière ouverture à une séquence de mêlée ou au tir. Fenêtre de punition prévue : 174 images.

**Victoire** : Vaincre la monture puis jouer une conclusion narrative distincte ; Myrrah au sol garde son traitement de personnage. **Défaite** : PV nuls ou tour détruite dans la variante histoire dédiée ; reprise au seuil de phase en difficulté accessible.

**Solo** : L’objectif de tour possède un délai généreux ; le Rayon de l’aube est fourni par le décor. **Coopération** : Une seule attaque d’objectif à la fois, avec possibilité de sauver le partenaire.

**Contrôle visuel** : Myrrah doit rester reconnaissable sur la monture sans devenir une silhouette géante ; leurs deux actifs sont séparés. **Récompense** : Conclusion Azura et panorama de la tour.

##### Karn sur Shibboleth

**Référence** : Gears of War Judgment. **Type** : Monture blindée terrestre. **Priorité** : P1. **Échelle de cadrage** : 6,0 hauteurs humaines. Monture et contexte confirmés ici par sources secondaires ; page officielle confirme Kilo et la période Judgment. Sources [BB15], [BB16], [BB17].

**Parties ciblables** : Patte mécanique; Points exposés lors du tir; Karn seulement pendant les transitions prévues.

**Phase 1 de 100 à 70 % — Encercler la place.** La patte mécanique s’ancre et le canon suit une moitié de la place. Avertissement prévu : 84 images. Tir de zone suivi d’une avancée diagonale figurée par un changement de profondeur visuel. Contre-jeu : Se déplacer sur le seul axe jouable ; la profondeur dessinée ne modifie pas les collisions. Fenêtre de punition prévue : 96 images.

**Phase 2 de 70 à 35 % — Ralliement.** Karn lève son arme, des arrivées sont marquées aux deux extrémités. Avertissement prévu : 108 images. Renforts limités et attaque souterraine de la patte. Contre-jeu : Éliminer le porteur de signal puis punir la patte figée ; les renforts cessent après deux vagues. Fenêtre de punition prévue : 132 images.

**Phase 3 de 35 à 0 % — Monture blessée.** Les plaques écartées révèlent un point vulnérable, accompagné d’un arrêt du canon. Avertissement prévu : 120 images. Charge lente puis frappe circulaire avec longue récupération. Contre-jeu : Contourner par une roulade tardive, frapper le flanc ouvert et finir la monture. Fenêtre de punition prévue : 156 images.

**Victoire** : Neutraliser la monture ; la conclusion de l’anthologie ne réécrit pas la scène canonique de Karn. **Défaite** : PV nuls ; aucune obstruction entre petits renforts et boss.

**Solo** : Deux renforts simultanés au maximum ; ils ne tirent pas pendant une grande charge. **Coopération** : Les renforts sont plafonnés à quatre et attaquent après leur entrée, jamais à l’apparition.

**Contrôle visuel** : La patte mécanique et la posture de Karn sont déterminantes pour distinguer Shibboleth d’un Corpser. **Récompense** : Médaillon Kilo et scène de Halvo Bay.

##### Hydra d’Ukkon

**Référence** : Gears Tactics. **Type** : Boss de laboratoire et artillerie. **Priorité** : P2. **Échelle de cadrage** : 9,0 hauteurs humaines. Ukkon confirmé par le blog officiel ; identification de l’Hydra finale soutenue par guide secondaire. Sources [BB04], [BB07], [BB18].

**Parties ciblables** : Lanceurs séparés; Conduites de l’arène; Tête après interruption.

**Phase 1 de 100 à 70 % — Artillerie.** Des rails sortent et trois zones d’impact se tracent au sol. Avertissement prévu : 96 images. Salves de missiles à délai fixe pendant qu’un générateur est activable. Contre-jeu : Ouvrir un chemin entre les impacts puis détruire le module de tir qui reste avancé. Fenêtre de punition prévue : 108 images.

**Phase 2 de 70 à 35 % — Production.** Les conduites s’ouvrent, un signal révèle de quel côté arriveront les renforts. Avertissement prévu : 120 images. Renfort biologique limité et rechargement d’un lanceur restant. Contre-jeu : Couper l’alimentation de l’arène pour gagner une ouverture sur la tête ; ce sabotage est une mécanique 2D originale. Fenêtre de punition prévue : 150 images.

**Phase 3 de 35 à 0 % — Dernier rempart.** Le boss déploie ses membres et cesse la production de renforts. Avertissement prévu : 132 images. Deux salves étagées suivies d’un piqué court à portée de mêlée. Contre-jeu : Profiter du piqué manqué ; tous les modules déjà détruits le restent. Fenêtre de punition prévue : 174 images.

**Victoire** : Vaincre l’Hydra puis conclure la chasse à Ukkon dans une vignette scénarisée ; pas de transformation géante inventée d’Ukkon. **Défaite** : PV nuls ; les renforts ne survivent pas aux transitions majeures.

**Solo** : Générateur activable par attaque de tout type ; le jeu n’exige pas Gabe. **Coopération** : Deux joueurs partagent un sabotage court plutôt que deux interrupteurs simultanés.

**Contrôle visuel** : Hydra Tactics distincte de celle de Skorge par son armement, ses pièces et le cadrage ; conserver Ukkon à son échelle. **Récompense** : Archives Tactics et vue éclatée de l’armement.

##### Swarmak

**Référence** : Gears of War 4. **Type** : Colosse de l’Essaim. **Priorité** : P0. **Échelle de cadrage** : 8,5 hauteurs humaines. Existence, épisode et présence en boss Horde confirmés par sources secondaires ; dispositif d’arène proposé. Sources [BB19], [BB20].

**Parties ciblables** : Poches luminescentes sur les membres; Poches latérales après la charge.

**Phase 1 de 100 à 70 % — Marche pesante.** La jambe se lève et la poche voisine devient plus lumineuse. Avertissement prévu : 90 images. Piétinement puis balayage du bras. Contre-jeu : Se glisser à l’extérieur du pied levé et toucher la poche basse, accessible aux coups courts. Fenêtre de punition prévue : 96 images.

**Phase 2 de 70 à 35 % — Surcharges.** Des arcs annoncent les équipements interactifs de l’arène. Avertissement prévu : 114 images. Rafales et avancée ; un dispositif expose temporairement une poche haute. Contre-jeu : Activer une borne de stage puis frapper les poches exposées ; aucune préférence obligatoire pour un tireur. Fenêtre de punition prévue : 144 images.

**Phase 3 de 35 à 0 % — Furie.** Le cri court interrompt les tirs avant une charge finale. Avertissement prévu : 126 images. Charge, effondrement sur un genou, reprise lente. Contre-jeu : Esquiver vers la zone sûre et monter un combo sur les poches latérales pendant l’agenouillement. Fenêtre de punition prévue : 168 images.

**Victoire** : Détruire les poches requises ; le corps principal sert d’indicateur global mais ne récompense pas les tirs inutiles sur blindage. **Défaite** : PV nuls ; l’écrasement a une forte poussée, pas de mort instantanée en normal.

**Solo** : Une borne utile se réactive à chaque phase. **Coopération** : Poches atteignables de chaque côté ; le boss ne peut coincer un joueur hors caméra.

**Contrôle visuel** : Ne pas réduire le Swarmak à un Brumak avec quelques taches ; excroissances et armure mutée à vérifier. **Récompense** : Trophée Essaim et palette de décor de barrage.

##### Snatcher

**Référence** : Gears of War 4. **Type** : Capture et bond. **Priorité** : P0. **Échelle de cadrage** : 3,4 hauteurs humaines. Snatcher de Gears 4 et boss Horde attestés secondairement ; règles de libération adaptées. Sources [BB21], [BB20].

**Parties ciblables** : Ventre durant le bond; Poche de capture; Queue après un tir.

**Phase 1 de 100 à 70 % — Traque.** Le ventre se contracte et la queue se redresse. Avertissement prévu : 72 images. Tir de queue suivi d’un bond court. Contre-jeu : Bloquer ou éviter le projectile puis passer sous le bond ; frapper le ventre à l’atterrissage. Fenêtre de punition prévue : 84 images.

**Phase 2 de 70 à 35 % — Capture.** La gueule ventrale s’ouvre et un cône au sol indique la zone dangereuse. Avertissement prévu : 90 images. Tentative d’absorption d’un joueur proche ou à terre. Contre-jeu : Sortir du cône ; si capturé, attaquer la poche de l’intérieur par une séquence simple sans martèlement. Fenêtre de punition prévue : 120 images.

**Phase 3 de 35 à 0 % — Retraite.** Le boss tourne le flanc et tente d’emporter une cible vers un bord. Avertissement prévu : 102 images. Bond arrière, tir puis pause de digestion. Contre-jeu : Interrompre la fuite en touchant la poche ; la sortie de capture donne une ouverture collective. Fenêtre de punition prévue : 144 images.

**Victoire** : Épuiser la jauge puis libérer automatiquement toute cible encore capturée. **Défaite** : PV nuls ; une capture seule ne termine pas la partie avant le délai affiché.

**Solo** : La poche possède une issue intérieure accessible par maintien d’une commande ; aucun verrou exigeant un allié. **Coopération** : Le partenaire peut accélérer la libération ; une seule capture simultanée.

**Contrôle visuel** : Le corps doit rester lisible pendant la capture ; aucune occultation prolongée du personnage. **Récompense** : Pose de victoire contre capture et entrée du bestiaire.

##### Carrier

**Référence** : Gears of War 4. **Type** : Artillerie organique. **Priorité** : P1. **Échelle de cadrage** : 3,9 hauteurs humaines. Carrier et place dans Horde 3.0 attestés secondairement ; statut miniboss de versions ultérieures ne modifie pas cette référence Gears 4. Sources [BB22], [BB20].

**Parties ciblables** : Poitrine ouverte; Avant-bras après impact.

**Phase 1 de 100 à 70 % — Incubation.** La poitrine se déploie avec un bruit distinct. Avertissement prévu : 84 images. Lancement de deux projectiles organiques destructibles. Contre-jeu : Détruire l’un pour avancer dans son couloir puis attaquer la poitrine encore ouverte. Fenêtre de punition prévue : 96 images.

**Phase 2 de 70 à 35 % — Écrasement.** Les bras se lèvent, ombres des poings au sol. Avertissement prévu : 96 images. Double frappe au sol et onde basse limitée. Contre-jeu : Saut court ou roulade sur le deuxième impact ; le bras reste accessible en sortie. Fenêtre de punition prévue : 120 images.

**Phase 3 de 35 à 0 % — Dernière salve.** Ouverture longue du thorax, tous les projectiles sont espacés. Avertissement prévu : 114 images. Trois projectiles suivis d’une tentative de prise lente. Contre-jeu : Approcher entre les trajectoires et punir la prise ratée sur le noyau. Fenêtre de punition prévue : 150 images.

**Victoire** : Détruire la jauge centrale ; aucun projectile résiduel ne frappe pendant le résultat. **Défaite** : PV nuls ; pas de cumul de prise et de projectile inévitable.

**Solo** : Deux projectiles actifs au maximum hors phase finale. **Coopération** : Trois projectiles au maximum, cibles annoncées ; PV ×1,65.

**Contrôle visuel** : Les Cankers doivent être des sprites séparés avec collisions propres, jamais un effet de décor sans logique. **Récompense** : Entrée Carrier et effet de projectile pour le visualiseur.

##### Kestrel

**Référence** : Gears of War 4. **Type** : Drone aérien armé. **Priorité** : P1. **Échelle de cadrage** : 4,4 hauteurs humaines. Drone CGU automatisé et confrontation Gears 4 documentés secondairement ; ses modules exacts restent à valider visuellement. Sources [BB23], [BB24].

**Parties ciblables** : Deux moteurs; Tourelle frontale; Train ou module bas pendant le stationnaire.

**Phase 1 de 100 à 70 % — Survol.** Le projecteur fixe sa cible et une ligne indique la rafale. Avertissement prévu : 84 images. Rafale horizontale puis déplacement au bord opposé. Contre-jeu : Passer derrière un couvert et frapper le module bas lorsqu’il stationne près du sol. Fenêtre de punition prévue : 96 images.

**Phase 2 de 70 à 35 % — Roquettes.** Les pods s’ouvrent et les points d’impact apparaissent dans l’ordre. Avertissement prévu : 108 images. Salve de roquettes alternant deux moitiés de l’arène. Contre-jeu : Ne pas poursuivre l’appareil ; préparer son prochain point de stationnaire et viser un moteur. Fenêtre de punition prévue : 132 images.

**Phase 3 de 35 à 0 % — Moteur en panne.** L’appareil penche du côté détruit ; alarme distincte. Avertissement prévu : 126 images. Une dernière rafale plus courte suivie d’un atterrissage forcé. Contre-jeu : Profiter de la panne pour un combo sur le moteur restant ou la tourelle. Fenêtre de punition prévue : 156 images.

**Victoire** : Désactiver les modules majeurs puis neutraliser le drone ; variante sans destruction dans le stand de tir. **Défaite** : PV nuls ; les couverts peuvent être détruits mais l’un reste disponible à chaque rafale.

**Solo** : Une borne d’interception met l’appareil à portée de toute arme de mêlée. **Coopération** : Pas d’obligation de répartir les joueurs ; un module ciblé donne des points de soutien au partenaire.

**Contrôle visuel** : Respecter le Kestrel automatisé de Gears 4 ; ne pas le confondre avec King Raven habité. **Récompense** : Plan de silhouette et emblème mécanique.

##### Hive Beast

**Référence** : Gears of War 4. **Type** : Siège colossal avec exoarmure de scène. **Priorité** : P2. **Échelle de cadrage** : 14,0 hauteurs humaines. Boss final Gears 4 identifié par source secondaire ; accessibilité des outils et montage du combat sont originaux. Sources [BB25], [BB26].

**Parties ciblables** : Tentacules et bases d’insertion; Poitrine ouverte après les ancrages.

**Phase 1 de 100 à 70 % — Ancrage.** Un tentacule se lève, ombre et contour au sol avant la frappe. Avertissement prévu : 108 images. Frappe d’un tentacule puis immobilisation de son extrémité. Contre-jeu : Attaquer l’extrémité et utiliser l’outil d’arrimage fourni par l’arène pour la maintenir. Fenêtre de punition prévue : 120 images.

**Phase 2 de 70 à 35 % — Contre-feu.** Le thorax s’ouvre, projectiles espacés visibles. Avertissement prévu : 126 images. Projectiles et balayage d’un second tentacule. Contre-jeu : Intercepter un projectile, arrimer le tentacule puis désigner sa base. Fenêtre de punition prévue : 156 images.

**Phase 3 de 35 à 0 % — Ouverture centrale.** Les attaches détruites tombent hors du sol de jeu, le noyau s’éclaire. Avertissement prévu : 144 images. Dernier balayage très large puis longue fenêtre de tir central. Contre-jeu : Garder le centre libre et déclencher l’appui aérien contextuel pendant l’ouverture. Fenêtre de punition prévue : 180 images.

**Victoire** : Neutraliser les tentacules nécessaires, terminer l’ouverture du noyau puis proposer une cinématique de conclusion fondée sur l’hélice du King Raven utilisée dans le jeu-source ; cette cinématique reste à vérifier et à produire. **Défaite** : PV nuls ; arrimage raté restitue une occasion, sans remise à zéro totale.

**Solo** : Outils de siège attribués automatiquement, avec une version d’assistance qui remplace les doubles commandes. **Coopération** : Arrimage plus rapide à deux mais réalisable seul ; un joueur ne peut être laissé sans cible utile.

**Contrôle visuel** : La silhouette doit dépasser le cadre sans cacher les télégraphes ; il faut des actifs par tentacule, pas une unique image redimensionnée. **Récompense** : Archive du final Gears 4 et galerie de construction des tentacules.

##### Matriarch

**Référence** : Gears 5. **Type** : Chasse sur glace. **Priorité** : P0. **Échelle de cadrage** : 2,8 hauteurs humaines. Identité et mécanisme glace puis dos décrits par sources secondaires ; durées et assistance visuelle originales. Sources [BB27], [BB28].

**Parties ciblables** : Dos pendant le gel; Épines après la charge.

**Phase 1 de 100 à 70 % — Écoute.** Silence bref, tête tournée vers la dernière source sonore. Avertissement prévu : 78 images. Charge sur la dernière position bruyante. Contre-jeu : Attirer le boss sur une zone de glace repérée, briser la glace et passer derrière le dos. Fenêtre de punition prévue : 120 images.

**Phase 2 de 70 à 35 % — Épines.** Dos arqué, plusieurs épines s’orientent avant le lancer. Avertissement prévu : 96 images. Projectile d’épine puis nouvelle charge avec correction limitée. Contre-jeu : Se déplacer après le verrouillage et utiliser une seconde zone de gel ; détacher une épine par maintien de commande si touché. Fenêtre de punition prévue : 144 images.

**Phase 3 de 35 à 0 % — Pression mentale.** Le décor vibre en périphérie, l’interface et les contours des dangers restent nets. Avertissement prévu : 114 images. Deux charges rapprochées suivies d’un arrêt prolongé. Contre-jeu : Conserver un îlot de glace disponible ; geler sur la dernière charge et vider sa ressource sur le dos. Fenêtre de punition prévue : 168 images.

**Victoire** : Briser le lien de cette rencontre en épuisant la jauge ; scène distincte selon parcours histoire ou exhibition. **Défaite** : PV nuls ; les trous de glace ne causent pas de chute fatale du joueur, ils poussent vers une zone sûre.

**Solo** : Une zone de gel réapparaît à chaque changement de phase, pas de blocage si les zones initiales sont consommées. **Coopération** : Le bruit du dernier joueur actif détermine la charge ; la capture d’un joueur ne bloque jamais le mécanisme de gel.

**Contrôle visuel** : Matriarch unique : proportions, dos, épines et couleur ne doivent pas devenir une simple Berserker recolorée. **Récompense** : Archive du laboratoire et variante glacée de scène.

##### Kraken

**Référence** : Gears 5. **Type** : Défense de rempart contre colosse. **Priorité** : P1. **Échelle de cadrage** : 16,0 hauteurs humaines. Boss final et défense du rempart appuyés secondairement ; construction du score et phases originales. Sources [BB29], [BB28].

**Parties ciblables** : Appendices entrant dans le plan; Points de la gueule révélés; Cible centrale pendant le tir de siège.

**Phase 1 de 100 à 70 % — Rempart.** Un appendice se plie et son impact est marqué sur une moitié du mur. Avertissement prévu : 108 images. Frappe et apparition de cibles lumineuses proches du sol. Contre-jeu : Frapper les appendices pour gagner une fenêtre d’utilisation du canon de rempart. Fenêtre de punition prévue : 132 images.

**Phase 2 de 70 à 35 % — Aspiration.** La gueule s’ouvre, flèches au sol et son grave continus. Avertissement prévu : 126 images. Aspiration horizontale ; sa force plafonne pour permettre le recul. Contre-jeu : Interrompre les points exposés ou se fixer au couvert ; les personnages de mêlée utilisent le canon commun. Fenêtre de punition prévue : 156 images.

**Phase 3 de 35 à 0 % — Dernière défense.** Deux cibles latérales s’éteignent et une cible centrale devient prioritaire. Avertissement prévu : 144 images. Balayage puis ouverture complète avant l’assaut final. Contre-jeu : Enchaîner deux interruptions et déclencher l’appui final fourni par la scène. Fenêtre de punition prévue : 192 images.

**Victoire** : Terminer la séquence de siège et la jauge du colosse ; la conclusion respecte le chapitre Gears 5 sélectionné. **Défaite** : PV nuls ou rempart détruit en Siège expert ; le jeu ne décide pas du choix narratif JD ou Del à la place du joueur.

**Solo** : Les armes de stage sont activables par une seule touche maintenue ; impossible de perdre la partie pour manque de munitions personnelles. **Coopération** : Les deux joueurs peuvent soutenir le canon ou protéger les appendices ; aucune place de spectateur imposée.

**Contrôle visuel** : Un Kraken gigantesque exige un cadrage de siège ; il ne devient jamais un combattant normal de trois mètres dans une arène duel. **Récompense** : Archive New Ephyra, chronométrage et médaille défense.

##### Flock

**Référence** : Gears 5. **Type** : Essaim volant. **Priorité** : P1. **Échelle de cadrage** : 5,0 hauteurs humaines. Flock figure dans les annonces officielles de Horde ; microstructure des individus à valider dans le jeu. Sources [BB30], [BB31].

**Parties ciblables** : Noyau collectif après dispersion; Nappe d’individus au contact d’un leurre.

**Phase 1 de 100 à 70 % — Nuage.** Le groupe se contracte en pointe, contour clair sur fond neutre. Avertissement prévu : 84 images. Passage horizontal puis dispersion lente. Contre-jeu : Roulade sous la trajectoire et attaque de la zone dense pendant la recomposition. Fenêtre de punition prévue : 96 images.

**Phase 2 de 70 à 35 % — Scission.** Deux branches se détachent avec deux sons distincts. Avertissement prévu : 108 images. Passages alternés haut et bas, jamais simultanément bloquants. Contre-jeu : Choisir garde ou déplacement d’après la hauteur ; utiliser un leurre d’arène pour forcer une descente. Fenêtre de punition prévue : 132 images.

**Phase 3 de 35 à 0 % — Concentration.** Le groupe regagne un seul centre et s’abaisse vers le sol. Avertissement prévu : 126 images. Spirale lente puis pause dense et vulnérable. Contre-jeu : Éviter la zone intérieure puis frapper le noyau groupé avec une attaque à zone ou un combo court. Fenêtre de punition prévue : 156 images.

**Victoire** : Épuiser une jauge partagée ; les unités décoratives disparaissent à la fin. **Défaite** : PV nuls ; aucun dégât provenant d’un individu purement décoratif.

**Solo** : La collision se limite à trois volumes déterministes ; pas de centaines de hitboxes aléatoires. **Coopération** : Leurres accessibles aux deux ; la scission garde toujours un côté libre.

**Contrôle visuel** : Limiter les particules, conserver la forme d’ensemble et ne pas masquer les silhouettes des joueurs. **Récompense** : Visualiseur de l’essaim et compteur d’interceptions.

##### Wakaatu

**Référence** : Gears 5 Hivebusters. **Type** : Prédateur volant et fouisseur. **Priorité** : P1. **Échelle de cadrage** : 5,5 hauteurs humaines. Source officielle confirmant le Wakaatu et Galangi ; caractéristiques de fouissement et de venin soutenues ici par référence secondaire. Sources [BB32], [BB33].

**Parties ciblables** : Gueule après émergence; Poches exposées pendant récupération; Pattes quand il se pose.

**Phase 1 de 100 à 70 % — Sous la terre.** Le sol se soulève dans une bande clairement circonscrite. Avertissement prévu : 96 images. Émergence sous la dernière position puis morsure. Contre-jeu : Sortir de la bande après le verrouillage et attaquer le flanc pendant la montée. Fenêtre de punition prévue : 108 images.

**Phase 2 de 70 à 35 % — Vol venimeux.** Un cri aigu précède l’ouverture des ailes et le crachat. Avertissement prévu : 114 images. Passage aérien et dépôt de venin limité au bord. Contre-jeu : Rejoindre le centre, attendre l’atterrissage imposé puis exploiter la gueule ouverte. Fenêtre de punition prévue : 150 images.

**Phase 3 de 35 à 0 % — Alternance.** Deux sillons au sol indiquent l’ordre des émergences. Avertissement prévu : 132 images. Émergence, vol bref, seconde émergence suivie d’une longue fatigue. Contre-jeu : Ne pas courir vers le premier sillon ; frapper les poches lors du repos final. Fenêtre de punition prévue : 174 images.

**Victoire** : Épuiser la jauge après avoir forcé les trois phases ; conclusion propre à Scorpio dans l’histoire. **Défaite** : PV nuls ; le venin n’occupe jamais le centre et les deux bords simultanément.

**Solo** : Une branche ou un sol stable garantit une cible proche à chaque cycle. **Coopération** : Le boss alterne ses cibles avec annonce ; aucune arrivée sous un joueur en train de relever l’autre sans délai.

**Contrôle visuel** : Employer les références Hivebusters pour tête, ailes, peau et proportions ; ne pas inventer un dragon générique. **Récompense** : Trophée Galangi et panorama volcanique.

##### King Raven de simulation

**Référence** : Gears of War 2006 pour la silhouette. **Type** : Véhicule allié en simulation. **Priorité** : P1. **Échelle de cadrage** : 5,0 hauteurs humaines. Véhicule CGU attesté secondairement ; son rôle de boss est intégralement une simulation non canonique. Sources [BB34].

**Parties ciblables** : Supports de tourelle factices; Capteurs d’exercice; Cible sous la cellule pendant le posé.

**Phase 1 de 100 à 70 % — Approche contrôlée.** Feux d’exercice blancs et annonce radio de début de passe. Avertissement prévu : 90 images. Tirs de simulation en lignes au sol, sans projectile imprévisible. Contre-jeu : Se déplacer entre les lignes puis marquer un capteur pendant le stationnaire. Fenêtre de punition prévue : 108 images.

**Phase 2 de 70 à 35 % — Extraction contestée.** Le treuil d’exercice descend avant un posé partiel. Avertissement prévu : 114 images. Une porte s’ouvre avec une cible mobile ; rotor seulement décoratif hors zone. Contre-jeu : Toucher la cible de porte ou le capteur bas, accessibles sans arme à distance. Fenêtre de punition prévue : 144 images.

**Phase 3 de 35 à 0 % — Immobilisation.** La radio annonce une dernière passe et un posé de 3 secondes. Avertissement prévu : 132 images. Rafale d’exercice puis immobilisation au centre de la scène. Contre-jeu : Désactiver les capteurs restants par un combo, puis sortir de la zone du décollage. Fenêtre de punition prévue : 180 images.

**Victoire** : Désactiver les cibles instrumentées ; appareil et équipage restent intacts. **Défaite** : PV d’exercice nuls ; redémarrage immédiat.

**Solo** : Cibles basses garanties ; rotor ne touche jamais le joueur. **Coopération** : Score d’équipe partagé et dégâts entre alliés désactivés.

**Contrôle visuel** : Le King Raven reste un transport CGU reconnaissable ; marquages d’exercice à part, sans inventer une variante officielle. **Récompense** : Brevet d’interception, sans scène canonique hostile.

##### Centaur de simulation

**Référence** : Gears of War 2. **Type** : Véhicule terrestre allié en simulation. **Priorité** : P1. **Échelle de cadrage** : 3,9 hauteurs humaines. Véhicule de Gears 2 documenté secondairement ; antagonisme et instruments de simulation inventés pour ce mode. Sources [BB35].

**Parties ciblables** : Roues instrumentées; Tourelle de tir factice; Capteur arrière.

**Phase 1 de 100 à 70 % — Tir de réglage.** La tourelle verrouille une zone avec un faisceau de simulation. Avertissement prévu : 84 images. Tir unique puis déplacement lent vers une extrémité. Contre-jeu : Sortir du faisceau et toucher une roue pour abaisser sa jauge de mobilité. Fenêtre de punition prévue : 108 images.

**Phase 2 de 70 à 35 % — Pivot.** Les roues changent d’angle avant la rotation de caisse. Avertissement prévu : 108 images. Pivot suivi de deux tirs d’exercice à hauteurs différentes. Contre-jeu : Passer derrière la caisse pendant la rotation puis marquer le capteur arrière. Fenêtre de punition prévue : 144 images.

**Phase 3 de 35 à 0 % — Test de résistance.** Un voyant signale une dernière accélération limitée. Avertissement prévu : 126 images. Course courte, freinage et arrêt prolongé. Contre-jeu : S’écarter de la trajectoire puis désactiver la tourelle par un combo. Fenêtre de punition prévue : 174 images.

**Victoire** : Couper les capteurs des trois systèmes ; aucune destruction narrative du blindé. **Défaite** : PV d’exercice nuls ; écrasement converti en forte pénalité d’exercice.

**Solo** : Trajectoire sur rail et capteurs proches ; le sol ne défile pas. **Coopération** : Tourelle et caisse visent des cibles annoncées différentes ; chaque attaque laisse un refuge commun.

**Contrôle visuel** : Centaur monté sur roues, pas un char à chenilles générique ; silhouette, suspension et canon à verrouiller sur Gears 2. **Récompense** : Brevet blindé et vue de la suspension.

##### Silverback de simulation

**Référence** : Gears of War 3 pour la silhouette. **Type** : Exoarmure alliée en simulation. **Priorité** : P1. **Échelle de cadrage** : 1,9 hauteurs humaines. Silverback et pilotage confirmés par Xbox Wire pour Lizzie ; silhouette Gears 3 à contrôler sur références de cet épisode. Sources [BB36], [BB37].

**Parties ciblables** : Articulations repérées; Arme de bras instrumentée; Cible du dos après ancrage.

**Phase 1 de 100 à 70 % — Mobilité.** Le pilote annonce une avancée et l’arme passe en sécurité visuelle. Avertissement prévu : 72 images. Deux pas lourds puis coup de bras lent d’exercice. Contre-jeu : Faire manquer le coup et attaquer l’articulation exposée. Fenêtre de punition prévue : 96 images.

**Phase 2 de 70 à 35 % — Ancrage.** Les stabilisateurs se déploient avec une sirène brève. Avertissement prévu : 96 images. Tirs de simulation en mode fixe ; rotation limitée. Contre-jeu : Contourner dans le plan au terme de la rafale et toucher le capteur arrière. Fenêtre de punition prévue : 132 images.

**Phase 3 de 35 à 0 % — Changement de mode.** Les stabilisateurs se replient, arme en surchauffe simulée. Avertissement prévu : 114 images. Un dernier pas, une rafale courte et une longue remise en position. Contre-jeu : Punir le changement de mode par une série complète au contact. Fenêtre de punition prévue : 156 images.

**Victoire** : Désactiver les capteurs ; le pilote sort et salue le combattant. **Défaite** : PV d’exercice nuls ; jamais de mise à mort d’un allié dans cette épreuve.

**Solo** : Le mode fixe dure assez longtemps pour que le combattant le plus lent puisse atteindre le dos. **Coopération** : Les joueurs peuvent partager les cibles ; le pilote ne change pas instantanément de côté entre deux coups.

**Contrôle visuel** : Éviter le corps de robot autonome : cockpit, pilote et stabilisateurs restent identifiables. **Récompense** : Brevet exoarmure et pose d’entraînement.

#### Production des arènes

Chaque arène reçoit un master de travail de 4096 × 2048 pixels, exportable à la taille utile. Les couches sont indépendantes et nommées par fonction ; leurs transparences ne remplacent pas un détourage contrôlé. Le moteur affiche un cadre cible de 1920 × 1080. Le sol possède une origine et une collision uniques, séparées des images. Les personnages ne sont jamais peints dans le décor. Les effets interactifs, projectiles et membres de boss sont eux aussi des actifs séparés.

| Couche | Facteur horizontal | Fonction | Collision |

|---|---:|---|---|

| Fond lointain | 0,04 | Ciel, obscurité ou brume | Non |

| Horizon | 0,15 | Reliefs et skyline | Non |

| Architecture | 0,36 | Repères du lieu | Non |

| Plan moyen | 0,65 | Éléments derrière les combattants | Non |

| Sol | 1,00 | Surface de combat et repère des pieds | Oui, géométrie indépendante |

| Avant plan | 1,12 | Cadre périphérique léger | Non |

La version Tournoi supprime les dommages de décor, les événements aléatoires, les variations de lumière pendant une manche et les secousses de caméra. Son sol est plat et ses bords fixes. L’avant-plan reste léger et ne traverse pas les bras, les armes ou les zones de pied. La version Spectacle garde le même cœur jouable, puis ajoute les événements spécifiés ci-dessous. Les dangers de scène sont réservés à un règlement explicitement choisi et leurs trajectoires sont reproductibles dans les replays.

La fidélité d’un lieu ne consiste pas à ajouter partout les mêmes caisses et les mêmes ruines. Chaque scène possède une silhouette architecturale, une gamme de matériaux et une lumière propres à sa référence. Les détails non vérifiés sont des tâches de validation, et non des éléments libres à inventer. Les compositions originales, comme les terrains de simulation, utilisent un vocabulaire CGU cohérent mais portent leur propre statut dans le menu.

##### House of Sovereigns

**Référence** : Gears of War 2006. **Lumière proposée** : Crépuscule froid. **Repère** : Façade monumentale et place éventrée. Sources [BB38], [BB39].

**Décomposition** : 1. Ciel couvert vide de silhouettes jouables ; 2. Silhouette des tours ruinées d’Ephyra ; 3. Façade de la House of Sovereigns d’après la référence choisie ; 4. Escaliers, balustrades et murs brisés derrière le plan de jeu ; 5. Dalles planes, joints et éclats sans obstacle vertical ; 6. Colonnes cassées sur les bords, poussière transparente.

**Spectacle** : Après le premier round, des débris tombent derrière le mur de combat ; la version Berserker ouvre visuellement un accès au ciel. **Lisibilité** : Le centre reste plus clair que les armures Locust ; aucun feu de même couleur qu’un télégraphe actif.

**Statut du lieu** : Lieu de Gears 1 confirmé secondairement ; cadrage latéral et plan de sol sont une adaptation.

##### Haldane Hall et domaine Fenix

**Référence** : Gears of War 2006. **Lumière proposée** : Pluie du soir. **Repère** : Maison et marches du domaine. Sources [BB40].

**Décomposition** : 1. Ciel d’orage faiblement animé ; 2. Arbres et reliefs au-delà du mur ; 3. Façade du domaine et fenêtres de la référence 2006 ; 4. Muret du jardin et piliers séparés du sol jouable ; 5. Terrasse plane de pierre mouillée ; 6. Branches des bords et filets de pluie.

**Spectacle** : Les éclairs éclairent seulement l’arrière-plan et peuvent être désactivés ; une fenêtre se brise au changement de round. **Lisibilité** : Aucune pluie opaque sur les bras ou armes ; reflets du sol plafonnés.

**Statut du lieu** : Le domaine Fenix correspond à Haldane Hall ; ne pas le confondre avec Stroud Estate de Gears 4.

##### Tyro Pillar

**Référence** : Gears of War 2006. **Lumière proposée** : Nuit en mouvement. **Repère** : Wagon de train et silhouette de la locomotive. Sources [BB41], [BB42].

**Décomposition** : 1. Ciel étoilé et nuages de nuit ; 2. Montagnes et pylônes distants ; 3. Paysage ferré défilant à vitesse de présentation ; 4. Parois de wagons et caisses sans collision ; 5. Toit ou pont de wagon plat avec repères fixes ; 6. Câbles et vapeur cantonnés aux bords.

**Spectacle** : Passage dans un tunnel au changement de round uniquement ; séquence de Kryll derrière une barrière de lumière, sans dommages en tournoi. **Lisibilité** : Les personnages et le sol restent fixes par rapport à la caméra ; la vitesse du fond n’ajoute pas de déplacement physique.

**Statut du lieu** : Train et confrontation finale de Gears 1 attestés secondairement ; architecture du wagon à valider sur la version 2006.

##### Les profondeurs

**Référence** : Gears of War 2. **Lumière proposée** : Éclairage souterrain. **Repère** : Cavernes monumentales et accès Locust. Sources [BB43], [BB44].

**Décomposition** : 1. Brume profonde sur fond sombre ; 2. Voûtes lointaines et reliefs étagés ; 3. Ponts Locust au second plan ; 4. Piliers de roche et matériel d’invasion ; 5. Corniche large sans trou de collision ; 6. Stalactites uniquement dans les coins hauts.

**Spectacle** : Un Grindlift traverse le fond avant l’entrée des combattants ; des Reavers très éloignés ne deviennent jamais des attaques. **Lisibilité** : Séparer la lumière Imulsion des indicateurs de dégâts et éviter les silhouettes de faux adversaires à hauteur de jeu.

**Statut du lieu** : Hollow présent sur la page officielle Gears 2 ; cette corniche est une composition latérale originale.

##### Lac des profondeurs

**Référence** : Gears of War 2. **Lumière proposée** : Nuit souterraine. **Repère** : Pont stable au-dessus d’un lac noir. Sources [BB06], [BB09].

**Décomposition** : 1. Brume de caverne très lointaine ; 2. Voûte et arches immergées ; 3. Rive distante et ruines ; 4. Surface de l’eau hors du sol jouable ; 5. Pont flottant large représenté sans roulis physique ; 6. Cordages et éclaboussures au bord inférieur.

**Spectacle** : Les vagues augmentent avec les phases du Leviathan ; le pont dessiné peut fléchir visuellement sans changer la collision. **Lisibilité** : Les tentacules actifs ont un contour dédié ; les reflets décoratifs ne reprennent pas leur couleur d’alerte.

**Statut du lieu** : Cadrage de rencontre adapté de Gears 2 ; « Lac des profondeurs » est un libellé descriptif, pas un nouveau toponyme canonique.

##### Forêt de Stromson

**Référence** : Gears of War 2. **Lumière proposée** : Aube voilée. **Repère** : Forêt et route de guerre en contrebas. Sources [BB45], [BB46], [BB07].

**Décomposition** : 1. Ciel d’aube pâle ; 2. Lignes de forêt lointaine ; 3. Falaises et route militaire ; 4. Arbres proches derrière la plateforme ; 5. Plateforme de poursuite stable ou chaussée de duel selon variante ; 6. Branches et fumée aux limites.

**Spectacle** : Convoi de fond et explosions lointaines ; la variante Hydra utilise un support volant à trajectoire visuelle fixe. **Lisibilité** : Les arbres ne traversent pas l’aire jouable ; leur contraste reste inférieur aux personnages.

**Statut du lieu** : Forêt attestée secondairement ; le support de combat latéral est une création pour la poursuite.

##### Jacinto au bord de la chute

**Référence** : Gears of War 2. **Lumière proposée** : Jour chargé de fumée. **Repère** : Ville en évacuation et rupture du plateau. Sources [BB47], [BB43].

**Décomposition** : 1. Ciel gris avec large zone calme ; 2. Skyline de Jacinto ; 3. Façades et grands contreforts ; 4. Débris d’évacuation et barrières ; 5. Promontoire plat sécurisé pour le jeu ; 6. Poussière et petits fragments sans collision.

**Spectacle** : L’effondrement monumental se déroule après le combat ou dans une boucle lente au fond ; aucun saut de caméra pendant une parade. **Lisibilité** : Éviter que le Brumak Lambent et les feux partagent la même valeur lumineuse.

**Statut du lieu** : Contexte de fin de Gears 2 ; géométrie de l’arène et position des bâtiments à vérifier sur captures.

##### Anvil Gate

**Référence** : Gears of War 3. **Lumière proposée** : Nuit sous projecteurs. **Repère** : Porte fortifiée et cours de défense. Sources [BB48], [BB49].

**Décomposition** : 1. Ciel nocturne peu contrasté ; 2. Collines et silhouettes de siège ; 3. Mur d’Anvil Gate et tour de guet ; 4. Sacs, caisses et atelier à l’arrière ; 5. Cour plane avec métal et poussière ; 6. Bord de rempart très bas et fumée fine.

**Spectacle** : Assaut lointain au premier round, Lambent visibles au second ; un projecteur suit le fond sans illuminer directement les joueurs. **Lisibilité** : Conserver une bande de valeur moyenne derrière les jambes ; flammes hors trajectoire des coups.

**Statut du lieu** : Lieu et bataille de Gears 3 documentés ; version latérale originale.

##### Pont du Sovereign

**Référence** : Gears of War 3. **Lumière proposée** : Aube maritime. **Repère** : Pont du navire et superstructure. Sources [BB12], [BB50].

**Décomposition** : 1. Ciel matinal doux ; 2. Mer et horizon horizontal ; 3. Superstructure et canots ; 4. Tuyaux, rails et éléments du pont ; 5. Pont large avec plaques métalliques ; 6. Cordages bas aux bords et embruns.

**Spectacle** : Vagues et mouvement du navire au fond ; l’attaque du Leviathan produit une gîte visuelle limitée seulement en transition. **Lisibilité** : Aucun roulis de caméra imposé ; les bords du pont sont fermés en duel.

**Statut du lieu** : Navire de Gears 3 et attaque identifiés secondairement ; composition latérale à contrôler.

##### Azura et la tour

**Référence** : Gears of War 3. **Lumière proposée** : Fin de journée. **Repère** : Tour et architecture d’Azura. Sources [BB14], [BB13].

**Décomposition** : 1. Ciel clair et nuages lents ; 2. Océan et îlots ; 3. Tour et bâtiments reconnaissables ; 4. Terrasse, balustrade et végétation ; 5. Dalles larges sans pente jouable ; 6. Fragments de colonne au bord inférieur.

**Spectacle** : La variante Tempest révèle la hauteur de la tour ; seuls les éléments non interactifs s’effondrent hors des fenêtres de combat. **Lisibilité** : Myrrah et le Tempest restent plus sombres que la pierre ; réduire le halo solaire derrière les télégraphes.

**Statut du lieu** : Lieu final de Gears 3 ; position précise des structures à valider dans le jeu.

##### Place de Halvo Bay

**Référence** : Gears of War Judgment. **Lumière proposée** : Jour de siège. **Repère** : Monument et place de la confrontation de Kilo. Sources [BB51], [BB17].

**Décomposition** : 1. Ciel couvert et fumée lointaine ; 2. Skyline de Halvo Bay ; 3. Monument et bâtiments de la place ; 4. Barricades rompues et marches derrière le plan ; 5. Place pavée libre de marche solide ; 6. Débris d’angle et drapeaux usés.

**Spectacle** : La façade subit des impacts entre les rounds ; Karn arrive sur Shibboleth en intro et non comme événement aléatoire de duel. **Lisibilité** : Les marches restent derrière les pieds ; aucun décalage de hauteur implicite.

**Statut du lieu** : Place finale documentée par source secondaire ; page officielle pour Kilo et le contexte Judgment.

##### Cour de ravitaillement

**Référence** : Gears Tactics. **Lumière proposée** : Jour voilé. **Repère** : Entrepôts et pont logistique. Sources [BB03], [BB52].

**Décomposition** : 1. Ciel pâle sans fort contraste ; 2. Reliefs désertiques et silhouette urbaine ; 3. Hangars et pont de ravitaillement ; 4. Caisses et conduites derrière le plan ; 5. Cour logistique plane ; 6. Grillage aux extrémités et poussière.

**Spectacle** : Un canon de Brumak détruit un hangar de fond après désarmement ; les destructions restent enregistrées. **Lisibilité** : La cour conserve un corridor central neutre pour distinguer explosions et points faibles.

**Statut du lieu** : Composition originale inspirée de Tactics ; aucun lieu canonique nommé inventé et aucun combat prétendu reproduit plan par plan.

##### Laboratoire d’Ukkon

**Référence** : Gears Tactics. **Lumière proposée** : Éclairage industriel intérieur. **Repère** : Installations de laboratoire et conduites. Sources [BB04], [BB53], [BB52].

**Décomposition** : 1. Ombre du volume intérieur ; 2. Portiques et mezzanines lointaines ; 3. Cuves et conduites du laboratoire ; 4. Consoles et structures derrière le boss ; 5. Sol industriel avec repères lisibles ; 6. Câbles périphériques et vapeur transparente.

**Spectacle** : Conduites coupées une à une selon l’objectif ; état visuel synchronisé sur les phases. **Lisibilité** : Les fluides lumineux restent derrière le boss et ne peuvent se confondre avec ses organes vulnérables.

**Statut du lieu** : Ukkon officiel ; localisation détaillée du laboratoire documentée secondairement. Corpser sur ce décor uniquement en exhibition, pas présenté comme son lieu canonique.

##### Settlement 5

**Référence** : Gears of War 4. **Lumière proposée** : Jour blanc. **Repère** : Architecture de colonie CGU et voies logistiques. Sources [BB54], [BB23].

**Décomposition** : 1. Ciel pâle de journée ; 2. Reliefs et murs éloignés ; 3. Bâtiments modulaires CGU ; 4. Barrières, jardinières et dépôt ; 5. Rue plane avec voies de circulation ; 6. Éléments de balustrade aux bords.

**Spectacle** : Arrivée d’un Kestrel en introduction ; déplacement de robots en fond hors des manches classées. **Lisibilité** : La lumière très claire ne doit pas effacer le contour bleu de l’armure CGU.

**Statut du lieu** : Colonie du début de Gears 4 à verrouiller sur captures ; pas de mélange avec District de Gears 5.

##### Ruche de l’Essaim

**Référence** : Gears of War 4. **Lumière proposée** : Lumière organique. **Repère** : Architecture envahie de matière organique. Sources [BB54], [BB21], [BB22].

**Décomposition** : 1. Brume sombre au fond du volume ; 2. Voûtes rocheuses et structures enfouies ; 3. Nids, poches et résine derrière le combat ; 4. Parois organiques lisibles et ouverture de tunnel ; 5. Plateforme de roche stable ; 6. Filaments périphériques transparents.

**Spectacle** : Les poches du fond pulsent lentement et les filaments se rétractent pendant le résultat. **Lisibilité** : Toutes les poches décoratives sont plus sombres que celles du Snatcher ou du Carrier.

**Statut du lieu** : Ruche comme type d’environnement de Gears 4 ; cette salle est un cadrage original.

##### Tollen Dam

**Référence** : Gears of War 4. **Lumière proposée** : Matin couvert. **Repère** : Barrage et accès de ruche. Sources [BB55], [BB25], [BB56].

**Décomposition** : 1. Ciel d’orage en retrait ; 2. Reliefs et masse d’eau ; 3. Barrage à grande échelle ; 4. Passerelles et ruche au-delà du plan ; 5. Tablier stable à sol continu ; 6. Éclaboussures et gravats d’angle.

**Spectacle** : La tempête de fond s’intensifie sans déplacer le personnage ; la variante Hive Beast utilise une caméra de siège et outils intégrés. **Lisibilité** : Le corps du boss reste séparé du béton ; aucun effet de pluie devant la jauge de point faible.

**Statut du lieu** : Barrage et ruche proches attestés secondairement ; vues d’affrontement recadrées pour 2D.

##### New Hope

**Référence** : Gears 5. **Lumière proposée** : Nuit neigeuse. **Repère** : Installation de recherche abandonnée. Sources [BB57], [BB58].

**Décomposition** : 1. Nuit neigeuse sans flash ; 2. Reliefs glacés lointains ; 3. Façade et couloirs du centre ; 4. Vitrages brisés et matériel éteint ; 5. Couloir ou cour plate avec neige fine ; 6. Glace en bordure et particules clairsemées.

**Spectacle** : Les néons se réactivent progressivement en introduction ; les Sires restent des silhouettes de fond uniquement hors tournoi. **Lisibilité** : Pas de flicker des lampes pendant le combat ; option météo désactivable.

**Statut du lieu** : Version Gears 5 distincte de New Hope Gears 2 ; détails architecturaux à vérifier sur capture.

##### Laboratoire sous le mont Kadar

**Référence** : Gears 5. **Lumière proposée** : Lumière froide intérieure. **Repère** : Chambre glacée de la Matriarch. Sources [BB27], [BB57].

**Décomposition** : 1. Ombre de la voûte ; 2. Volumes de glace arrière ; 3. Installations et réservoirs de la chambre ; 4. Banquises et conduites sans collision en duel ; 5. Glace plane avec zones de gel indépendantes en boss ; 6. Glace de bord et vapeur basse.

**Spectacle** : Les plaques se brisent uniquement dans Boss Battle ; en duel elles deviennent des animations sans trou ni ralentissement. **Lisibilité** : Les indicateurs des plaques doivent se lire sans distinguer bleu et cyan ; ajouter motifs et contours.

**Statut du lieu** : Chambre associée à la Matriarch dans Gears 5 ; géométrie et nombre des plaques sont de l’adaptation.

##### Aéroport de Vasgar

**Référence** : Gears 5. **Lumière proposée** : Soleil désertique. **Repère** : Aéroport englouti dans le sable rouge. Sources [BB59].

**Décomposition** : 1. Ciel clair sans flare central ; 2. Dunes de sable rouge ; 3. Terminal et structures d’aéroport ; 4. Dunes basses et carcasses éloignées ; 5. Piste plane de béton et sable compact ; 6. Barrières cassées aux bords.

**Spectacle** : Un mur de poussière traverse très lentement le fond entre les rounds ; les débris ne masquent pas les attaques. **Lisibilité** : Le sable reste mat ; contours sombres sur les personnages clairs et effets de Flock lisibles.

**Statut du lieu** : Source officielle pour Vasgar, aéroport et dunes rouges ; conversion de carte 3D à scène 2D originale.

##### Rempart de New Ephyra

**Référence** : Gears 5. **Lumière proposée** : Jour de bataille. **Repère** : Mur de défense et ville reconstruite. Sources [BB57], [BB29].

**Décomposition** : 1. Ciel couvert de fumée légère ; 2. Skyline de New Ephyra ; 3. Mur et structures défensives ; 4. Canons et obstacles derrière le plan ; 5. Chemin de rempart plat ; 6. Drapeaux et débris aux extrémités.

**Spectacle** : Le Kraken occupe l’espace au-delà du mur dans sa variante ; le duel conserve un fond sans créature active. **Lisibilité** : Le mur sert de ligne de sol immuable ; aspiration visible dans les effets au sol, pas par des secousses.

**Statut du lieu** : Défense finale Gears 5 attestée secondairement ; composition du rempart à vérifier sur séquence officielle.

##### Plage de Galangi

**Référence** : Gears 5 Hivebusters. **Lumière proposée** : Fin de matinée. **Repère** : Plage volcanique et lisière tropicale. Sources [BB32].

**Décomposition** : 1. Ciel tropical ; 2. Océan et îlots ; 3. Lisière et relief volcanique ; 4. Épaves ou éléments de plage confirmés par référence ; 5. Sable compact horizontal ; 6. Feuilles au bord et écume très basse.

**Spectacle** : Vagues et faune lointaine sans interaction ; arrivée de Scorpio dans une intro dédiée. **Lisibilité** : Pas de végétation dans le volume des attaques ; lumière uniforme sur les personnages.

**Statut du lieu** : Source officielle pour Galangi, jungle et plages ; disposition latérale originale.

##### Intérieur volcanique de Galangi

**Référence** : Gears 5 Hivebusters. **Lumière proposée** : Lumière volcanique. **Repère** : Corniche et lave derrière la zone de combat. Sources [BB32], [BB33].

**Décomposition** : 1. Brume chaude sombre ; 2. Parois volcaniques lointaines ; 3. Cascades de lave et arches de basalte ; 4. Rochers et racines brûlées derrière le sol ; 5. Corniche stable de roche mate ; 6. Cendres légères et bords de pierre.

**Spectacle** : Une coulée change de vitesse au passage de phase ; la lave reste hors du plan jouable, sauf défi explicitement sélectionné. **Lisibilité** : L’orange ne doit pas noyer le télégraphe du Wakaatu ; toutes les alertes combinent contour et son.

**Statut du lieu** : Galangi volcanique et Wakaatu confirmés officiellement ; détail de cette corniche créé pour l’adaptation.

##### Hangar de simulation CGU

**Référence** : Création pour Gears of War Combats. **Lumière proposée** : Éclairage technique constant. **Repère** : Portique d’essai et panneaux d’exercice. Sources [BB59].

**Décomposition** : 1. Ombre du volume de hangar ; 2. Poutres et plafond ; 3. Portiques industriels inspirés des matériaux CGU ; 4. Cibles et consoles d’exercice ; 5. Dalle plane avec graduation non textuelle ; 6. Garde-corps aux bords.

**Spectacle** : Les capteurs s’allument lorsqu’ils sont touchés et le véhicule s’arrête après le résultat ; pas d’explosion réelle. **Lisibilité** : Les panneaux explicites de simulation apparaissent dans l’interface et l’introduction, pas gravés comme un faux logo officiel.

**Statut du lieu** : Décor original ; la carte officielle Training Grounds prouve seulement l’existence d’installations d’essai DB, pas ce hangar.

##### Terrain de simulation CGU

**Référence** : Création pour Gears of War Combats. **Lumière proposée** : Jour neutre. **Repère** : Circuit d’essai balisé pour blindés. Sources [BB59], [BB35].

**Décomposition** : 1. Ciel pâle ; 2. Reliefs neutres ; 3. Murs de protection et miradors d’exercice ; 4. Cibles rabattables et panneaux abstraits ; 5. Piste plane avec limites fixes ; 6. Grillage et pneus hors zone de jeu.

**Spectacle** : Les cibles se rétractent après validation ; le Centaur rejoint son emplacement sans destruction. **Lisibilité** : Les lignes du sol désignent les attaques sans ressembler à des obstacles solides.

**Statut du lieu** : Composition originale de simulation ; ne prétend pas être une carte officielle existante.

#### Anthologie en douze chapitres

Le menu d’histoire présente des dossiers d’archives, avec le jeu d’origine, l’époque et les personnages autorisés. Les passages entre épisodes sont des transitions de menu ; il n’existe pas de tournoi canonique réunissant les morts, les versions jeunes et âgées et leurs descendants. Un joueur peut néanmoins composer librement ces rencontres dans Arcade, Tournoi et Exhibition. Les intros et endings ci-dessous sont des textes originaux pour l’adaptation, pas des citations ni des cinématiques déjà réalisées.

Chaque chapitre propose une introduction de 15 à 25 secondes, plusieurs rencontres courtes, une scène de rival, un affrontement majeur et un ending de 20 à 40 secondes. Les durées représentent une cible de production. Chaque vidéo est skippable après une première lecture et disponible ensuite dans la galerie. Une vignette de transition explique un saut de lieu ou de temps au lieu de déplacer implicitement une bataille canonique.

##### Chapitre 1 Le témoignage de Kilo

**Jeu de référence** : Gears of War Judgment. **Personnages proposés** : Damon Baird jeune, Augustus Cole jeune, Garron Paduk Judgment, Sofia Hendrik. **Rival** : Karn. Sources [BB17], [BB16].

**Introduction originale** : Carton « Archives de Halvo Bay ». La salle du tribunal reste en silhouette, puis la caméra rejoint la place assiégée. Baird : « On pourra discuter des ordres quand ces rues seront vides. » Sofia : « Alors il faut leur ouvrir un passage. »

**Déroulement** : 1. Apprentissage du déplacement et de la garde contre deux groupes Locust représentés par des duels successifs. 2. Duel contre Theron avec objectif facultatif de protection du couloir d’évacuation. 3. Confrontation scénarisée avec Karn, immédiatement suivie de Shibboleth en trois phases.

**Scène de rival originale** : Karn apparaît sur sa monture ; aucune descente inventée ne lui impose un duel humain. Paduk observe la patte mécanique. Baird : « C’est là qu’on commence. » L’interface présente les parties ciblables.

**Ending original** : La caméra s’éloigne des débris de la place. La conclusion rejoint le cadre du témoignage et la résolution de Judgment, sans faire de Baird l’auteur d’un geste attribué à Loomis dans le jeu. Une carte débloquée permet de revoir les choix de Kilo.

**Garde de continuité** : Judgment demeure un récit de Kilo. Marcus et Dom peuvent visiter ce décor uniquement en Exhibition. Le sort final de Karn reste celui du jeu-source.

**Objectif optionnel** : Terminer une phase sans laisser les renforts atteindre la sortie de la place. **Déblocage** : Scène de la place, chronologie Judgment et défi Karn.

##### Chapitre 2 La fabrique des monstres

**Jeu de référence** : Gears Tactics. **Personnages jouables proposés** : Gabe Diaz, Sid Redburn, Mikayla Dorn. Reyna Torres intervient ici comme personnage narratif ; sa version humaine jouable demanderait une fiche supplémentaire distincte de Reine Reyna. **Rival** : Ukkon. Sources [BB04], [BB03], [BB52].

**Introduction originale** : Une photographie de reconnaissance occupe le centre de l’écran. Gabe la retourne : la silhouette d’une installation est esquissée sur son dos. Gabe : « On coupe sa production ici. » Mikayla : « Et on n’oublie pas ceux qui restent à l’intérieur. »

**Déroulement** : 1. Duels de reconnaissance contre Drone, Grenadier et Kantus ; ordre libre parmi deux accès, rejoignant le même objectif. 2. Brumak dans la cour de ravitaillement en reconstitution de combat, puis transition d’archives. 3. Corpser dans une arène de Tactics à valider visuellement ; la variante de laboratoire reste réservée au mode libre. 4. Assaut du laboratoire et Hydra d’Ukkon ; fin de la chasse à Ukkon en vignette distincte.

**Scène de rival originale** : Ukkon se tient dans un poste protégé, à son échelle normale. Les conduites se mettent en marche. Gabe : « Il n’a plus d’endroit où envoyer ses créations. » Le duel verbal sert de transition vers le boss, sans mutation géante ajoutée.

**Ending original** : Le laboratoire se tait et l’escouade se rassemble. Les documents retrouvés rejoignent les archives ; le menu conserve l’issue de Tactics et ne prétend pas que cette opération a empêché les événements des épisodes suivants.

**Garde de continuité** : Le groupe appartient à l’époque Tactics. La Reyna de ce chapitre est Reyna Torres dans cette période, jamais la reine de l’Essaim. L’exécution narrative d’Ukkon est conservée dans le montage source à valider.

**Objectif optionnel** : Désactiver un module de chaque boss avant de franchir son premier seuil de phase. **Déblocage** : Dossiers des créations d’Ukkon et défis séparés des trois boss.

##### Chapitre 3 Les premières lignes de Delta

**Jeu de référence** : Gears of War 2006. **Personnages proposés** : Marcus Fenix Gears 1, Dominic Santiago Gears 1, Damon Baird Gears 1, Augustus Cole Gears 1. **Rival** : Theron Guard. Sources [BB02], [BB39], [BB40].

**Introduction originale** : Le bruit d’un Lancer en cours de vérification ouvre la scène. Delta traverse la cour de la House of Sovereigns. Dom : « Le prochain passage est couvert. » Marcus : « Alors on le dégage ensemble. »

**Déroulement** : 1. Trois duels pédagogiques : Drone pour la garde, Grenadier pour la distance, Theron pour les projectiles chargés. 2. Berserker dans une séquence de chasse avec mise à disposition du marqueur orbital. 3. Interlude au domaine Fenix, suivi d’un duel de contrôle d’espace contre un Theron.

**Scène de rival originale** : Un Theron se positionne derrière un mur brisé et arme son arc. Marcus observe l’ouverture entre deux colonnes. La caméra insiste sur la charge du Torque Bow pour annoncer le rythme du duel.

**Ending original** : Delta récupère les informations nécessaires à la poursuite de sa mission. Une transition de carte conduit vers le rail et le Tyro Pillar. L’ending montre le groupe quittant les lieux, sans ajouter une victoire définitive contre la Horde.

**Garde de continuité** : La House of Sovereigns et le domaine sont deux lieux distincts et séparés par une ellipse explicite. Les armures, visages et armes suivent la version Gears 1 choisie, pas un mélange de skins.

**Objectif optionnel** : Réussir un rechargement actif après avoir provoqué une charge de Berserker manquée. **Déblocage** : Défi de chasse Berserker et galerie du domaine Fenix.

##### Chapitre 4 Le dernier wagon

**Jeu de référence** : Gears of War 2006. **Personnages proposés** : Marcus Fenix Gears 1, Dominic Santiago Gears 1. **Rival** : Général RAAM. Sources [BB02], [BB42].

**Introduction originale** : Le paysage file sous la lune ; le personnage vérifie son arme, puis regarde la plateforme suivante. Dom : « Plus beaucoup de train devant nous. » Marcus : « Il nous reste le nécessaire. »

**Déroulement** : 1. Duel contre un Grenadier sur une plateforme stable. 2. Défi de déplacement entre zones de lumière, présenté comme exercice avant le combat principal. 3. Rival RAAM, avec protection Kryll spécifiée dans son moveset et sources du roster ; deux rounds de duel contre un boss humanoïde.

**Scène de rival originale** : RAAM apparaît à l’extrémité du wagon, sans dialogue obligatoire. Une lumière vacillante révèle son armure puis se stabilise. Marcus prend place ; le jeu rend immédiatement la main, sans long duel cinématique.

**Ending original** : Le train s’éloigne dans la séquence de conclusion choisie. Marcus et Dom se retrouvent dans le plan d’extraction ; le menu ferme le dossier du premier jeu et ouvre celui de l’offensive des profondeurs.

**Garde de continuité** : RAAM reste un boss de duel à taille de personnage élargie, pas un véhicule. Les Kryll et la lumière ne créent pas de dégâts aléatoires en tournoi. Le montage final ne remplace pas les événements de Gears 1.

**Objectif optionnel** : Finir le rival après avoir brisé sa défense Kryll selon la mécanique spécifiée, sans dégâts de lumière résiduels. **Déblocage** : Ending Delta et variante nuit du Tyro Pillar.

##### Chapitre 5 L’offensive des profondeurs

**Jeu de référence** : Gears of War 2. **Personnages proposés** : Marcus Fenix Gears 2, Dominic Santiago Gears 2, Damon Baird Gears 2, Augustus Cole Gears 2. **Rival** : Skorge. Sources [BB43], [BB06], [BB44].

**Introduction originale** : Un Grindlift perce la roche au fond, puis le cadre se fixe sur la corniche. Baird : « La descente était la partie facile. » Cole : « Tant mieux, on commençait à s’ennuyer. »

**Déroulement** : 1. Duels contre Kantus et Theron pour enseigner l’interruption des soutiens et la gestion de l’espace. 2. Boss Reaver avec première phase au sol, afin d’enseigner la punition après atterrissage. 3. Ellipse explicitement titrée vers le lac souterrain, puis Leviathan. 4. Apparition narrative de Skorge annonçant le chapitre suivant ; son duel complet se joue dans le dossier de la fuite.

**Scène de rival originale** : Skorge traverse une passerelle distante, son bâton tronçonneuse lisible en silhouette. Aucun combat impossible à distance ne commence ; le rival est annoncé dans l’archive et suivi par une transition de lieu.

**Ending original** : Le groupe franchit le lac et poursuit sa progression. L’image finale reste une porte ouverte vers la forteresse Locust ; elle ne montre pas une victoire anticipée sur Skorge.

**Garde de continuité** : La succession resserre la campagne Gears 2 et indique chaque ellipse. Les lieux ne sont pas présentés comme contigus. Les personnages absents de la séquence source ne sont autorisés qu’en reconstitution libre.

**Objectif optionnel** : Intercepter un projectile de Reaver puis libérer deux prises de Leviathan sans subir de dégâts. **Déblocage** : Décors des profondeurs et fiche d’étude des montures.

##### Chapitre 6 La fuite et la chute

**Jeu de référence** : Gears of War 2. **Personnages proposés** : Marcus Fenix Gears 2, Dominic Santiago Gears 2, Damon Baird Gears 2, Augustus Cole Gears 2. **Rival** : Skorge. Sources [BB07], [BB47], [BB09].

**Introduction originale** : Carton « Après l’assaut de Nexus ». La caméra montre un passage déchiré et le bruit de l’Hydra arrive hors champ. Dom : « Il nous a retrouvés. » Marcus : « Cette fois, on termine la poursuite. »

**Déroulement** : 1. Duel rival Skorge sur un cadrage de palais à produire ; utiliser le décor de forêt seulement dans la version d’exercice provisoire. 2. Boss Hydra de Skorge sur plateforme de poursuite stable. 3. Transition d’archives vers Jacinto, courte défense contre des Locusts, puis Brumak Lambent en siège.

**Scène de rival originale** : Le rival se conclut avant la poursuite. Skorge remonte sur sa monture dans la transition ; le combat change ensuite de cadrage et d’objectifs. Les deux rencontres restent dans des étapes séparées du menu.

**Ending original** : La chute de Jacinto se déroule après la réussite du siège. L’ending privilégie la foule en évacuation et le silence de Delta plutôt qu’une célébration inventée ; une archive rappelle le coût de l’opération.

**Garde de continuité** : Ne jamais déplacer le duel de Skorge canonique dans la forêt en mode Histoire. Le décor palais est une dépendance supplémentaire identifiée, hors des 24 scènes de cette première version.

**Objectif optionnel** : Terminer la poursuite avec au moins une intervention de soutien et réussir les trois désignations du siège. **Déblocage** : Final Gears 2 et variantes Hydra et Brumak Lambent.

##### Chapitre 7 Tenir la ligne

**Jeu de référence** : Gears of War 3. **Personnages proposés** : Marcus Fenix Gears 3, Dominic Santiago Gears 3, Anya Stroud Gears 3, Samantha Byrne. **Rival** : Berserker Lambent. Sources [BB49], [BB12], [BB48].

**Introduction originale** : Le soleil se lève sur un pont de navire. Anya vérifie une caisse de munitions pendant que Marcus surveille la mer. Anya : « On compte ceux qui peuvent encore se battre. » Marcus : « Et on veille sur les autres. »

**Déroulement** : 1. Défense du pont contre un groupe de formes Lambent adapté à la production disponible. 2. Leviathan Lambent en boss de siège, puis ellipse vers Anvil Gate. 3. Duel de soutien contre Mauler ou Grenadier, puis Berserker Lambent.

**Scène de rival originale** : La Berserker traverse une porte de fond et s’arrête assez longtemps pour montrer sa poitrine. Le tutoriel de phase annonce que l’ouverture visuelle compte davantage que la puissance brute.

**Ending original** : Anvil Gate tient pour cette rencontre. Le groupe se prépare à poursuivre sa route ; le carnet d’archives distingue cette défense des événements ultérieurs de Mercy, qui ne sont pas rejoués dans cette première sélection.

**Garde de continuité** : Dom est présent ici avant Mercy. Il ne doit jamais être ajouté comme vivant à l’assaut d’Azura dans la lecture Histoire. Le Leviathan Lambent n’est pas le Leviathan de Gears 2.

**Objectif optionnel** : Protéger la jauge du pont dans le défi optionnel puis éviter toute trace de charge contaminée. **Déblocage** : Archive Anvil Gate et dossier comparatif des variants Lambent.

##### Chapitre 8 La tour d’Azura

**Jeu de référence** : Gears of War 3. **Personnages proposés** : Marcus Fenix Gears 3, Anya Stroud Gears 3, Samantha Byrne, Clayton Carmine. **Rival** : Reine Myrrah. Sources [BB13], [BB14], [BB49].

**Introduction originale** : La tour apparaît derrière la terrasse. Le son des armes se tait une seconde, puis une ombre traverse le soleil. Anya : « Nous avons encore une fenêtre. » Marcus : « On la garde ouverte. »

**Déroulement** : 1. Duel contre Theron d’élite en approche de la tour. 2. Rivalité verbale avec Myrrah dans une vignette d’archives, sans duel au sol ajouté à cette chronologie. 3. Tempest et Myrrah en trois phases, avec protection d’objectif propre à cette mission.

**Scène de rival originale** : Myrrah reste sur le Tempest. La scène pose l’enjeu de la tour puis rend la main. Le choix de jouer Myrrah en personnage de duel demeure disponible dans Arcade et Exhibition, sans modifier cette scène.

**Ending original** : La fin rejoint la conclusion de Gears 3. Marcus dépose son arme ; Anya rejoint le cadre. Les images restent un montage original discret qui conserve les pertes et le résultat du jeu-source.

**Garde de continuité** : Pas de résurrection de Dom et pas de rencontre physique entre Kait et la Myrrah de Gears 3. Le combat de boss et la conclusion humaine de Myrrah sont deux étapes distinctes.

**Objectif optionnel** : Repousser chaque tentative de destruction de la tour avant la fin de son délai visible. **Déblocage** : Ending Azura et récompense visuelle de campagne sans bonus PvP.

##### Chapitre 9 Un nouvel ennemi

**Jeu de référence** : Gears of War 4. **Personnages proposés** : JD Fenix Gears 4, Kait Diaz Gears 4, Delmont Walker Gears 4. **Rival** : Snatcher. Sources [BB54], [BB23], [BB21].

**Introduction originale** : Une rue de colonie se ferme sous les ordres d’un système automatique. Del regarde les barrières. Del : « La sortie vient de changer de place. » JD : « Alors on lui en ouvre une autre. »

**Déroulement** : 1. Duels contre des DeeBees dans la colonie, suivis du Kestrel. 2. Ellipse explicite vers la recherche des disparus ; exploration en vignettes, sans inventer une liaison directe entre colonie et ruche. 3. Carrier comme introduction aux projectiles organiques, puis Snatcher et mécanique de libération.

**Scène de rival originale** : Le Snatcher traverse le fond avec une silhouette enfermée dans sa poche. Kait avance d’un pas. Kait : « Il ne repart pas avec quelqu’un d’autre. » Le jeu annonce immédiatement la possibilité de délivrer une cible.

**Ending original** : Les indices recueillis permettent de poursuivre vers le barrage. L’ending réserve la résolution de la quête de Reyna au chapitre suivant et n’invente pas de sauvetage réussi prématuré.

**Garde de continuité** : Les DeeBees et le Kestrel appartiennent à la période Gears 4. Le combat contre les véhicules CGU habités reste dans les simulations ; il ne se glisse pas dans ce récit.

**Objectif optionnel** : Intercepter une rafale du Kestrel puis sortir d’une capture de Snatcher sans assistance automatique. **Déblocage** : Bestiaire Essaim et variante de colonie.

##### Chapitre 10 Le barrage et la ruche

**Jeu de référence** : Gears of War 4. **Personnages proposés** : JD Fenix Gears 4, Kait Diaz Gears 4, Delmont Walker Gears 4, Marcus Fenix Gears 4. **Rival** : Hive Beast. Sources [BB55], [BB25], [BB54].

**Introduction originale** : Le barrage remplit le cadre. Une secousse détache de la poussière des passerelles. Marcus : « On sait maintenant ce qu’il y a derrière. » Kait : « Alors on continue. »

**Déroulement** : 1. Duel d’accès contre un Drone de l’Essaim puis boss Swarmak. 2. Interlude présentant les outils de siège et leurs commandes communes à tous les combattants. 3. Hive Beast en grand cadrage ; séquence d’ancrage des tentacules et appui contextuel.

**Scène de rival originale** : La Hive Beast apparaît derrière le barrage. L’interface ne la réduit pas à une cible humanoïde : deux tentacules entrent dans le plan, puis une consigne précise la première prise à neutraliser.

**Ending original** : Le récit rejoint les conséquences de la rencontre avec Reyna. Kait garde son point de vue, et l’archive ferme le chapitre sans prétendre résoudre les questions développées ensuite dans Gears 5.

**Garde de continuité** : Le geste final canonique contre la Hive Beast doit être vérifié sur la séquence du jeu avant réalisation de la cinématique. Le prototype de désignation est identifié comme mécanique de substitution, pas reconstitution 1:1 déjà validée.

**Objectif optionnel** : Détruire toutes les poches nécessaires du Swarmak puis arrimer chaque tentacule en une fenêtre. **Déblocage** : Final Gears 4 et galerie Tollen Dam.

##### Chapitre 11 Les liens de Kait

**Jeu de référence** : Gears 5. **Personnages proposés** : Kait Diaz Gears 5, Delmont Walker Gears 5, JD Fenix Gears 5 selon scène, Fahz Chutani selon scène. **Rival** : Matriarch puis confrontation à la reine de l’Essaim en vignette. Sources [BB57], [BB27], [BB29], [BB59].

**Introduction originale** : Une trace de givre traverse un ancien panneau de laboratoire. Kait pose sa main sur une porte fermée. Kait : « Les réponses sont toujours derrière un verrou. » Del : « Cette fois, on reste ensemble pour l’ouvrir. »

**Déroulement** : 1. Volet A : New Hope, duels de créatures et collecte d’archives, puis Matriarch au mont Kadar. 2. Volet B : changement d’époque interne signalé par carton Vasgar ; duel d’Essaim puis Flock en cadrage d’aéroport. 3. Volet C : nouvelle transition vers New Ephyra ; sélection explicite du choix narratif JD ou Del si le parcours reprend la fin de Gears 5. 4. Kraken en défense de rempart, après validation de la composition de l’escouade suivant le choix précédent.

**Scène de rival originale** : La Matriarch apparaît dans la chambre glacée ; les visions restent en périphérie. La scène de la reine de l’Essaim est séparée du combat et ne fusionne pas son apparence avec la Myrrah de Gears 3.

**Ending original** : La défense de New Ephyra s’achève dans la continuité du choix enregistré. Le menu affiche l’ending correspondant, permet de revoir l’autre en mode Archives, et ne désigne pas une branche comme seule fin canonique.

**Garde de continuité** : Pas de décision automatique sur JD ou Del ; pas de rencontre canonique entre Gears 5 Kait et RAAM. Le volet Kadar reste centré sur Kait et Del. Le sacrifice de Jack dans la conclusion source ne devient pas une victoire personnelle inventée d’un combattant libre.

**Objectif optionnel** : Geler la Matriarch sur trois zones distinctes, intercepter un Flock, puis repousser toutes les aspirations du Kraken. **Déblocage** : Deux versions d’archive de fin et dossiers Kadar, Vasgar et rempart.

##### Chapitre 12 L’opération Scorpio

**Jeu de référence** : Gears 5 Hivebusters. **Personnages proposés** : Lahni Kaliso, Jeremiah Keegan, Leslie Mac Macallister. **Rival** : Wakaatu. Sources [BB32].

**Introduction originale** : Les vagues arrivent sur une plage de Galangi. Mac vérifie son masque pendant que Lahni observe la lisière. Mac : « J’avais imaginé une arrivée moins discrète. » Keegan : « Gardons le bruit pour la sortie. »

**Déroulement** : 1. Duels d’Essaim dans la lisière et découverte des capacités de coopération. 2. Séquence d’évasion avec une limite de temps optionnelle ; sans temps imposé dans le mode histoire accessible. 3. Wakaatu dans le décor volcanique, avec maîtrise du fouissement et du passage aérien.

**Scène de rival originale** : Le Wakaatu perce la brume derrière le sol de combat. Lahni suit son ombre plutôt que sa tête. Lahni : « Attendez qu’il choisisse sa sortie. » Le premier sillon apparaît et le contrôle est rendu.

**Ending original** : Scorpio se regroupe à distance du danger. Une ultime image de Galangi referme le dossier, puis le joueur débloque un circuit de chasse coopératif libre avec les trois héros et tous les boss déjà rencontrés.

**Garde de continuité** : Scorpio reste Lahni, Keegan et Mac dans le récit. Les capacités d’Escape ne sont pas distribuées rétroactivement à tous les soldats de Gears 1. La chronologie relative à Gears 5 est indiquée comme dossier parallèle, sans date inventée.

**Objectif optionnel** : Sauver un partenaire d’une attaque ciblée ou, en solo, provoquer deux émergences manquées sans perdre de santé. **Déblocage** : Ending Scorpio, circuit Galangi et galerie Wakaatu.

#### Extension E Day et dépendances de continuité

E-Day dispose d’un dossier d’extension dans le plan de production. La page officielle vérifiée le 19 novembre 2026 présente Marcus Fenix et Dominic Santiago quatorze ans avant le premier Gears of War, lors de l’Émergence. Ce fait autorise le cadrage de l’époque ; il ne suffit pas à garantir le détail de chaque arme, ruelle, ennemi ou costume. L’extension doit verrouiller une séquence officielle précise, les variantes visuelles de Marcus et Dom et les noms des lieux avant d’écrire ses affrontements définitifs. Elle ne réemploie pas par défaut une cour d’Ephyra de Gears 1 comme si elle était le lieu exact de cette nouvelle histoire.

Source E-Day : https://www.gearsofwar.com/en-us/games/gears-of-war-eday/. Les nouveaux monstres visibles dans les médias officiels ne reçoivent pas de noms inventés. Une silhouette ressemblant à un Brumak ne devient pas automatiquement une variante déjà validée. Ce verrou de référence s’applique aussi aux exécutions ou aux capacités qui pourraient varier entre épisodes.

Deux compléments de décor restent nécessaires pour une mise en scène rigoureuse des dossiers proposés : le palais de Nexus pour le duel de Skorge et l’arène précise du Corpser de Tactics. Ils constituent des tâches supplémentaires au catalogue des 24 arènes détaillées, et non des images implicitement disponibles. En attendant, leurs rencontres restent accessibles comme exercices sur un décor de laboratoire ou de forêt marqué Exhibition. Le mode Histoire ne présente pas ces substituts comme des reconstitutions fidèles.

#### Validation artistique et fonctionnelle

Avant de déclarer un boss fidèle à sa référence, conserver au minimum une vue d’ensemble, une vue latérale exploitable, un détail de chaque arme ou organe important et une séquence montrant son déplacement. La validation vérifie d’abord la silhouette, puis la topologie des membres et des plaques, enfin les matières, couleurs et effets. Les appendices ne doivent pas changer de nombre entre les poses. Le miroir horizontal doit être contrôlé lorsqu’une arme ou une prothèse change la silhouette ; créer une orientation dédiée si le miroir inverse un élément canonique.

Le test d’une rencontre doit répondre à des questions concrètes : le personnage de mêlée le plus lent peut-il atteindre chaque ouverture, la garde et la roulade donnent-elles une réponse à toutes les attaques ordinaires, la capture se termine-t-elle en solo, les modules détruits restent-ils désactivés, et les deux joueurs restent-ils dans un cadrage utilisable ? Les valeurs doivent être modifiées d’après ces tests, pas parce qu’un tableau contient déjà un nombre. La lisibilité se contrôle en mouvement, sur une scène sombre comme sur une scène claire, et avec les effets réduits.

Les tests de circuit doivent vérifier la conservation de l’ordre des boss, des paramètres de difficulté et des récompenses. Une défaite peut relancer la rencontre sans dupliquer une récompense. Un changement d’accessibilité n’efface pas la progression. Les enregistrements stockent version des données, choix de phase, graine déterministe des événements autorisés et commandes ; ils ne dépendent pas des animations cosmétiques pour recalculer les collisions.

Les 24 fiches de boss et les 144 entrées de calques sont des éléments de production à réaliser. Le suivi distingue Spécifié, Généré, Contrôlé visuellement, Animé, Intégré et Testé. Un concept isolé ne passe pas directement au statut de sprite animé ; un panorama aplati ne passe pas au statut de scène en parallaxe. Le lot de génération doit respecter un sujet ou un calque par image et conserver le lien entre référence, prompt, fichier et résultat de validation.

#### Sources des boss des arènes et de la campagne

Les références officielles sont indiquées comme primaires. Les guides et pages de wiki servent à documenter les détails absents des pages officielles ; ils ne remplacent pas la comparaison visuelle au jeu. Consultation de travail le 19 novembre 2026. Aucune source ne fournit les chiffres d’équilibrage de ce mode 2D, qui sont des propositions propres au projet.

- [BB01] Source secondaire — https://gearsofwar.fandom.com/wiki/Berserker

- [BB02] Source primaire — https://www.gearsofwar.com/en-us/games/gears-of-war/

- [BB03] Source primaire — https://www.gearsofwar.com/en-us/news/dev-blog-bosses/

- [BB04] Source primaire — https://www.gearsofwar.com/en-us/news/dev-blog-enemies/

- [BB05] Source secondaire — https://gearsofwar.fandom.com/wiki/Reaver

- [BB06] Source secondaire — https://gearsofwar.fandom.com/wiki/Leviathan

- [BB07] Source secondaire — https://gearsofwar.fandom.com/wiki/Hydra

- [BB08] Source secondaire — https://primagames.com/eguides/gears-war-2-eguide/act-v-aftermath/chapter-1-escape

- [BB09] Source secondaire — https://gearsofwar.fandom.com/wiki/Gears_of_War_2

- [BB10] Source secondaire — https://gearsofwar.fandom.com/wiki/Lambent_Brumak

- [BB11] Source secondaire — https://gearsofwar.fandom.com/wiki/Lambent_Berserker

- [BB12] Source secondaire — https://gearsofwar.fandom.com/wiki/Lambent_Leviathan

- [BB13] Source secondaire — https://gearsofwar.fandom.com/wiki/Tempest

- [BB14] Source secondaire — https://gearsofwar.fandom.com/wiki/Battle_of_Azura

- [BB15] Source secondaire — https://gearsofwar.fandom.com/wiki/Shibboleth

- [BB16] Source secondaire — https://gearsofwar.fandom.com/wiki/Destruction_of_Halvo_Bay

- [BB17] Source primaire — https://www.gearsofwar.com/en-us/games/gears-of-war-judgment/

- [BB18] Source secondaire — https://primagames.com/gaming/gears-tactics-hydra-boss-guide

- [BB19] Source secondaire — https://gearsofwar.fandom.com/wiki/Swarmak

- [BB20] Source secondaire — https://primagames.com/eguides/gears-of-war-4-eguide/horde-30/overview

- [BB21] Source secondaire — https://gearsofwar.fandom.com/wiki/Snatcher

- [BB22] Source secondaire — https://gearsofwar.fandom.com/wiki/Carrier

- [BB23] Source secondaire — https://gearsofwar.fandom.com/wiki/Kestrel

- [BB24] Source secondaire — https://primagames.com/eguides/gears-of-war-4-eguide/enemy-forces/deebees

- [BB25] Source secondaire — https://gearsofwar.fandom.com/wiki/Hive_Beast

- [BB26] Source secondaire — https://gearsofwar.fandom.com/wiki/Rescue_of_Fort_Umson

- [BB27] Source secondaire — https://gearsofwar.fandom.com/wiki/Matriarch

- [BB28] Source secondaire — https://gamefaqs.gamespot.com/pc/241047-gears-5/faqs/77771/boss-fights

- [BB29] Source secondaire — https://gearsofwar.fandom.com/wiki/Kraken

- [BB30] Source secondaire — https://gearsofwar.fandom.com/wiki/Flock

- [BB31] Source primaire — https://steamcommunity.com/app/1097840/announcements/

- [BB32] Source primaire — https://www.gearsofwar.com/en-us/news/hivebusters/

- [BB33] Source secondaire — https://gearsofwar.fandom.com/wiki/Wakaatu

- [BB34] Source secondaire — https://gearsofwar.fandom.com/wiki/King_Raven

- [BB35] Source secondaire — https://gearsofwar.fandom.com/wiki/Centaur

- [BB36] Source secondaire — https://gearsofwar.fandom.com/wiki/Silverback

- [BB37] Source primaire — https://news.xbox.com/en-us/2019/12/11/gears-5-operation-2-free-for-all-available-today-for-all-players/

- [BB38] Source secondaire — https://gearsofwar.fandom.com/wiki/House_of_Sovereigns

- [BB39] Source secondaire — https://gearsofwar.fandom.com/wiki/Mission_to_House_of_Sovereigns

- [BB40] Source secondaire — https://gearsofwar.fandom.com/wiki/Haldane_Hall

- [BB41] Source secondaire — https://gearsofwar.fandom.com/wiki/Tyro_Pillar

- [BB42] Source secondaire — https://gearsofwar.fandom.com/wiki/Battle_on_the_Tyro_Pillar

- [BB43] Source primaire — https://www.gearsofwar.com/en-us/games/gears-of-war-2/

- [BB44] Source secondaire — https://gearsofwar.fandom.com/wiki/Hollow

- [BB45] Source secondaire — https://gearsofwar.fandom.com/wiki/Stromson_Forest

- [BB46] Source secondaire — https://gearsofwar.fandom.com/wiki/Battle_of_Stromson_Forest

- [BB47] Source secondaire — https://gearsofwar.fandom.com/wiki/Sinking_of_Jacinto_City

- [BB48] Source secondaire — https://gearsofwar.fandom.com/wiki/Battle_of_Anvil_Gate

- [BB49] Source primaire — https://www.gearsofwar.com/en-us/games/gears-of-war-3/

- [BB50] Source secondaire — https://gearsofwar.fandom.com/wiki/Gears_of_War_3

- [BB51] Source secondaire — https://gearsofwar.fandom.com/wiki/Plaza_for_the_Tyran_Dead_%28Chapter%29

- [BB52] Source secondaire — https://gearsofwar.fandom.com/wiki/Gears_Tactics

- [BB53] Source secondaire — https://gearsofwar.fandom.com/wiki/Ukkon

- [BB54] Source secondaire — https://gearsofwar.fandom.com/wiki/Gears_of_War_4

- [BB55] Source secondaire — https://gearsofwar.fandom.com/wiki/Tollen_Dam

- [BB56] Source secondaire — https://primagames.com/eguides/gears-of-war-4-eguide/campaign/act-4/chapter-4-powerless

- [BB57] Source secondaire — https://gearsofwar.fandom.com/wiki/Gears_5

- [BB58] Source secondaire — https://gearsofwar.fandom.com/wiki/New_Hope_Research_Facility

- [BB59] Source primaire — https://www.gearsofwar.com/en-us/news/gears-5-launch-maps/

## Guide commun et deux extensions adaptes a Gears

Source complète : [combat_extensions.md](../docs/combat_extensions.md).

Adaptation V12 complète. Les sources officielles étayent les identités et périodes ; les règles et chorégraphies nouvelles demeurent des créations du projet.

### Gears of War Combats — intégration du guide et des deux extensions

Version de conception V12 — 27 novembre 2026. Ce chapitre complète la [bible principale](../docs/core_bible.md). Il adapte le guide commun de Darknigthmare et ses extensions aux personnages, aux époques et aux règles de ce dépôt.

**État réel : sources intégrées et conception détaillée.** Les systèmes décrits ci-dessous ne sont pas ajoutés au moteur par ce chapitre. Les animations restent des besoins de production ; la passe courante poursuit les sprites fixes, les costumes, les projectiles, les ennemis et les masters de stages manquants. Un fichier présent, un contenu documenté, un contenu jouable et un contenu validé sont quatre résultats différents.

#### 1. Documents de référence et décisions d'intégration

Les trois originaux sont conservés sans modification sous `docs/guides/combat/`. Leurs tailles, empreintes SHA-256 et liens Drive sont enregistrés dans [source_manifest.json](../docs/guides/combat/source_manifest.json). Le [rapport d'intégration](../docs/production/GUIDE_INTEGRATION_V12.md) consigne le point de départ et la vérification des copies.

| Référence | Rubriques | Rôle dans Gears Combats |
| --- | --- | --- |
| [Guide général v1.0](../docs/guides/combat/Combat_Games_Guide_General_v1.0.txt) | 00–29 | Socle de bible, fidélité, combat, récits, boss, arènes, production et validation |
| [Extension 01 v1.0](../docs/guides/combat/Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt) | 30–49 | Taunts, sélection, équipes, clashes, entités, bonus et exploration |
| [Extension 02 v1.0](../docs/guides/combat/Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt) | 50–67 | Contenus verrouillés, acquisitions, conditions et soutiens |

La [matrice de 68 rubriques](../docs/production/GUIDE_REQUIREMENTS_V12.csv) indique pour chacune sa prise en compte, sa preuve documentaire, son écart et son critère d'acceptation. Elle ne transforme pas l'intégration des documents en pourcentage de jeu terminé.

Les règles de duel de la bible restent la référence : simulation à 60 pas/s, super personnelle plafonnée à trois barres dans le jeu cible, munitions et posture distinctes. La jauge d'équipe ci-dessous est une nouvelle ressource conçue pour les modes d'équipe. Le prototype dispose encore d'une jauge spéciale unique et de trois rencontres ; il ne doit pas être présenté comme l'implémentation de ce nouveau profil.

#### 2. Fidélité, périodes et statut de chaque création

Les contenus emploient désormais cinq statuts de fidélité : `canon_atteste`, `adaptation_jouable`, `original_compatible`, `alternatif_crossover` et `a_confirmer`. Le statut de production est enregistré séparément. Un costume absent n'est pas un costume à débloquer ; un contenu non vérifié ne devient pas canonique parce qu'il apparaît dans une galerie.

Chaque fiche doit fixer l'œuvre, la version du personnage, le costume, l'arme, la période, la source et les détails visuels encore à contrôler. La page qui confirme l'existence d'un personnage ne prouve pas la géométrie de son arme ou la disposition de ses sangles. Avant de marquer un sprite validé 1:1, comparer des captures déterminées avec visage, silhouette, armure, matériaux, asymétries et équipement visibles.

La campagne est une anthologie. Un partenaire n'intervient que lorsqu'il est présent, vivant, disponible et correctement équipé dans le chapitre choisi. Les équipes transversales du versus portent la mention « Simulation libre ». Aucun dialogue de ce mode n'ajoute un événement au récit officiel. Les séquences et noms d'attaques inventés dans ce document sont des créations de gameplay.

Les invités et collaborations, même lorsqu'ils ont existé dans un mode multijoueur officiel, restent des entrées `alternatif_crossover` pour la narration de ce projet. Leur disponibilité commerciale ou promotionnelle ne prouve aucune présence dans les événements de campagne. Aucun crossover n'est ajouté à une route canonique par les extensions ; tout mode alternatif éventuel affiche sa continuité propre.

##### Associations prioritaires et bornes de lore

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

#### 3. Taunts et présentation du combattant

Chaque combattant reçoit une fiche de provocation avec une action compatible avec son équipement : geste de défi, contrôle d'arme sans munition gratuite, attitude d'attente ou réponse de personnalité. Les premières fiches concernent Marcus, Dom, Baird, Cole, RAAM, Kait et Scorpio. Aucune réplique inventée n'est attribuée à un enregistrement officiel.

Le réglage initial proposé est un engagement de 60 frames, interrompu par un impact, sans gain de vie, de munition ou de super. Les 24 dernières frames peuvent permettre une sortie vers la garde si les tests le justifient. Une provocation de victoire est cosmétique ; une provocation pendant le duel possède une récupération punissable. Les commandes sont remappables et le taunt ne partage pas le bouton de rechargement.

Les fiches distinguent : entrée, maintien éventuel, sortie, interruption, retour à la pose neutre, son, texte et version à mouvement réduit. Le VFX d'une arme ne doit pas être dessiné deux fois, dans le sprite et dans l'émetteur du moteur. Une vérification visuelle exige qu'une arme portée, un chargeur et les protections restent du même côté.

#### 4. Sélection, confirmation, désélection et annulation

Le cycle de présentation est `idle → focus_enter → focus_loop → confirm → ready`. Changer de case avant confirmation déclenche `focus_exit` puis la nouvelle entrée. Annuler une confirmation déclenche `deselect → idle`. Une fermeture de menu ou un changement de costume invalide tous les événements cosmétiques de la sélection précédente.

Le focus utilise immédiatement le portrait disponible, sans attendre une animation. Une entrée proposée de 18 frames et une sortie de 12 frames évitent de bloquer la navigation. Les clips sont interruptibles ; seule la sélection finale décide du personnage engagé. Un identifiant de session de sélection empêche qu'un son ou un effet retardé de l'ancien personnage se déclenche sur le suivant.

Le panneau montre nom, période, costume, rôle, statut d'accès et condition suivante utile. Un slot secret reçoit un dossier neutre ; le nom du personnage ne doit pas fuiter par le texte accessible, le son, un attribut HTML ou une miniature. Un contenu identifié mais verrouillé reste inspectable sans pouvoir être confirmé. La préférence de costume est sauvegardée séparément du droit de l'utiliser.

Les animations sont planifiées individuellement pour chaque version. Une rotation globale d'un PNG reste une transformation de présentation ; elle n'est pas comptée comme un clip dessiné.

#### 5. Profils d'équipe, jauges et commandes

| Profil | Composition | Défaite et restrictions |
| --- | --- | --- |
| Duel classique | Un actif | Règles existantes ; aucun appel de partenaire |
| Assistance | Un actif + un soutien | KO de l'actif termine l'équipe ; soutien non contrôlable |
| Tag hybride | Un actif + une réserve | Deux vies distinctes ; défaite quand les deux sont KO |
| Boss coopératif | Deux joueurs actifs | Contrat de boss propre ; ce n'est pas le tag à un joueur |

Le profil Tag hybride est la cible de l'extension. Les équipes successives après KO restent un autre mode. Pas de doublon d'identité dans la même équipe : Marcus jeune et vétéran ne peuvent servir de deux membres distincts sans profil alternatif explicitement choisi. Les homologues adverses restent permis en versus libre, avec palette et HUD différenciés.

##### Réglage initial proposé à éprouver

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

#### 6. Assistance et tag : contrats de simulation

Une assistance suit `ready → entering → acting → exiting → cooldown → ready`. Les variantes `hit`, `ko` et `cancelled` ont une sortie définie. Le partenaire possède une zone de présence et une vulnérabilité annoncées ; son apparition ne téléporte pas arbitrairement l'adversaire et ne permet pas de couvrir les deux côtés sans signal.

Pour le profil initial, une assistance touchée interrompt son action et applique les dégâts à la vie propre de la réserve. Elle peut être mise KO ; l'équipe continue tant que l'actif survit. Un soutien déjà KO ne peut être rappelé. Son cooldown commence à sa sortie effective, pas au premier appui. Un signal de départ et un bord de scène dégagé rendent son arrivée lisible.

Le tag volontaire est possible depuis le neutre ou une fenêtre d'annulation explicitement portée par un coup. Il est interdit pendant garde subie, hitstun, projection, exécution, clash ou transition non terminée. Le prototype de réglage vise 18 frames de départ, 24 d'entrée et une protection limitée contre les impacts résiduels déjà consommés ; aucune invulnérabilité générale n'est acquise par le simple transfert de contrôle.

Le combo conserve son identifiant, son scaling, ses rebonds utilisés et sa gravité. Le tag ne remet pas à zéro les munitions, la super ni la récupération. Un relais après KO positionne le survivant sur une entrée annoncée, nettoie les effets terminés et ne demande jamais une jauge que le joueur ne peut plus obtenir. Si le dernier membre tombe, la fin de manche résout d'abord le résultat.

#### 7. Supers combinées, finishers et scènes dramatiques

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

#### 8. Clashes et résolution accessible

Un clash n'est possible qu'entre actions listées comme compatibles, au même intervalle de collision et avec des équipements adaptés. La première fiche porte sur une opposition d'armes à contact dans une simulation ; son animation précise reste à référencer. Les balles ordinaires, les attaques de boss et les invocations ne deviennent pas automatiquement des confrontations de force.

Le profil spectacle peut utiliser un QTE court à trois entrées espacées, chacune avec fenêtre annoncée. Aucun martèlement obligatoire. Le profil confort permet maintien ou résolution automatique avec le même plafond de résultat. Le profil compétition emploie une résolution déterministe fondée sur les actions engagées, leurs ressources et leur priorité ; il ne mélange pas les classements de règles différentes.

Définir réussite, échec, égalité, absence de réponse, déconnexion et interruption par un tiers. La simulation conserve une seule vérité : les effets de caméra ne gèlent pas un projectile si les règles le font continuer. Un projectile tiers peut annuler le clash selon le contrat, sans déclencher simultanément la récompense du QTE. Les deux combattants retrouvent une position, une orientation, des ressources et une récupération déterminées.

#### 9. Entités natives, objets posés et projectiles persistants

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

#### 10. Stages bonus et liens avec les récits

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

#### 11. Espace de déblocage : Archives de campagne

**« Archives de campagne » est un lieu d'interface original compatible, pas un site officiel ajouté au canon.** Sa première version cible une carte interactive reliée à la galerie ; un environnement explorable complet reste une étape ultérieure. Les dossiers représentent des périodes, sans prétendre qu'un soldat du premier Gears peut consulter des événements futurs.

Organisation proposée : accueil → terminal de missions → salle d'archives → casiers d'équipement. Le terminal donne accès au simulateur ; l'archive donne accès à la galerie. Un couloir représenté correspond à une connexion réelle, et chaque porte possède destination, condition, retour et état mémorisé. Le graphe sera vérifié avant une version jouable ; aucune porte décorative au milieu d'une salle ne représente un chargement arbitraire.

Les clés sont des autorisations de dossier ou des jetons d'exercice fictifs propres à la progression. Elles ne deviennent ni monnaies officielles de Sera ni ressources vendues sans décision explicite. Le joueur obtient un indice, remplit un objectif, revient au dossier et réclame un contenu identifié. Les acquisitions essentielles sont ciblées, sans tirage aléatoire imposé.

Le premier parcours conçu relie une épreuve de rechargement, un dossier de personnage, une récompense de présentation et une variante d'ambiance de simulation. Aucun prérequis ne dépend de l'objet qu'il ouvre. Le serveur ou la sauvegarde autoritaire enregistre l'identifiant de récompense avant l'animation de révélation, pour éviter perte ou duplication après interruption.

#### 12. Slots verrouillés : quatre dimensions séparées

La présentation utilise un dossier militaire masqué et un verrou mécanique discret, avec silhouette noire lorsqu'elle est autorisée. Cette grammaire est une création UI. Elle ne prétend pas reproduire un menu officiel ni inventer un nouvel insigne canonique. Les familles Locustes et Essaim peuvent changer le matériau et le cadre ; l'état reste compréhensible sans couleur seule.

| Dimension | Valeurs minimales | Exemple d'explication |
| --- | --- | --- |
| Découverte | secret, indice, identifié | « Dossier non révélé » ou silhouette autorisée |
| Droit | aucun, à réclamer, permanent, temporaire, en attente, expiré | « Terminer l'épreuve » ou « Récompense disponible » |
| Installation | prêt, fichiers requis, erreur | « Contenu à installer » ; pas de faux verrou d'abonnement |
| Compatibilité | autorisé, interdit par règles | « Version incompatible avec ce chapitre » |

Ordre d'information : cacher les spoilers, expliquer l'obstacle qui empêche réellement la confirmation, proposer une action utile, puis rendre les autres conditions consultables. Un personnage non produit reste dans le catalogue de production et ne devient pas un faux contenu payant. Un costume obtenu avant le personnage reste acquis, avec dépendance visible. Le stage statique de confort ne doit pas être retiré au profit d'une version animée obligatoire.

Les catégories couvertes sont personnages, soutiens, costumes, palettes, stages, variantes, modes, défis, taunts et galerie. Le verrouillage d'un mode est limité aux routes narratives et défis avancés ; versus de base, réglages d'accessibilité, tutoriel et entraînement de base restent accessibles. La sélection d'un slot fermé ne bloque jamais la navigation ou le retour au menu.

#### 13. Acquisitions, conditions ET/OU et sauvegarde

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

#### 14. Contenus de soutien et accès externe

La possibilité de contenus dédiés aux soutiens est retenue en conception. **Aucune offre commerciale, liaison Patreon, synchronisation de compte ou vérification de paiement n'est opérationnelle dans ce dépôt par cette livraison.** Les contenus précis et leur admissibilité restent à décider avant activation.

Trois modèles sont prévus : récompense permanente attribuée par événement confirmé ; catalogue temporaire utilisable pendant un droit valide ; lot de période doté de sa propre règle de permanence. Le texte affiché doit annoncer le modèle, les dépendances et les éventuelles autres voies d'obtention. Les récompenses de soutien conservent les mêmes statistiques, collisions et exigences de lisibilité que les autres costumes. Une création esthétique de soutien garde `original_compatible` ou `alternatif_crossover`, jamais `canon_atteste` par son seul accès.

Le client n'a pas autorité pour s'accorder un avantage. Une future intégration utilisera le parcours officiel du fournisseur, un service de confiance, des événements authentifiés et une réconciliation des doublons ou événements reçus dans le désordre. Le guide d'origine décrit cette architecture ; la documentation actuelle du fournisseur devra être vérifiée avant son implémentation. Aucun secret d'application n'appartient au jeu distribué.

État inconnu du fournisseur et droit expiré confirmé restent distincts. Une période payée encore valide ne cesse pas par supposition au clic d'annulation. Expirer une source temporaire laisse intactes les autres sources valides. Pour la première version future, l'accès hors ligne permanent reste disponible après acquisition ; un justificatif temporaire exigera une politique explicite et une durée à tester avant activation.

Annulation, déliaison, baisse de niveau, remboursement et suppression du compte du jeu sont des événements différents. Une déliaison arrête les vérifications futures selon la politique annoncée ; elle n'efface pas une récompense déjà acquise définitivement. Un remboursement confirmé ne retire que la source d'accès concernée selon la règle de l'offre : une seconde source permanente ou temporaire valide continue d'accorder l'accès. Une baisse de niveau s'applique à sa date effective vérifiée, sans révocation anticipée déduite d'un simple changement d'intitulé.

Un compte invité ne reçoit pas automatiquement les droits d'un autre profil présent sur l'appareil. Avant liaison, afficher le compte du jeu destinataire et la politique de transfert. Une même livraison permanente possède un identifiant d'attribution stable : déliaison, nouvelle liaison ou double événement ne peuvent la multiplier entre profils. Les transferts entre comptes restent interdits par défaut tant qu'une procédure explicite de récupération n'est pas définie. Ces règles sont des exigences de conception à tester, sans liaison active dans la livraison actuelle.

Une partie déjà autorisée conserve ses personnages, costumes et stage jusqu'au résultat. Le changement d'accès s'applique à la sélection suivante. Un costume devenu inaccessible reçoit un remplacement disponible avec explication ; sa préférence est gardée. En réseau, prévoir que l'adversaire puisse télécharger et afficher le stage choisi selon une politique de participation distincte du droit de le sélectionner. Sans cette distribution vérifiée, le stage ne peut entrer dans une rotation partagée.

#### 15. Arènes connectées et transitions de boss

Chaque stage sépare quatre axes : présentation vivante/statique, interactions, dangers et transitions. Le réglage de confort ne désactive pas une collision en silence. Un danger conserve un signal lisible lorsqu'une animation est réduite. Le profil tournoi reste neutre selon la bible.

Une liaison possède `from_zone`, `to_zone`, point de départ, déclencheur, direction, état requis, positions d'arrivée, retour, coût et compatibilité. Deux fonds existants ne prouvent pas qu'ils sont physiquement adjacents. `stage_training_hangar` et `stage_training_range` peuvent former un lien original conçu dans le simulateur ; les lieux canoniques restent séparés tant qu'une référence topographique n'établit pas le passage.

Avant le départ : valider destination, assets, collision, droit de participation et configuration commune. Puis résoudre les impacts de la frame, figer la décision de transition, traiter les entités selon leur contrat et charger la zone. À l'arrivée : poser les deux membres actifs, conserver vie, munitions, jauges, compteurs de combo et temps selon les règles annoncées. Une destination absente annule le départ proprement avant prélèvement, avec retour jouable.

Un double déclenchement ne produit qu'une transition. Un KO simultané se résout selon le résultat du combat avant une coupe cosmétique. Une transition ne ressuscite pas une réserve et ne réarme pas une grenade déjà consommée. La présentation abrégée et le replay doivent retrouver le même état final.

Les boss gardent leurs contrats de taille et de phase. Une super d'équipe n'interrompt une phase que si la fenêtre de vulnérabilité l'autorise. Les modules détruits restent détruits, même après changement de caméra. Les simulations King Raven, Centaur et Silverback gardent leur statut non canonique de défi ; leur fin est une désactivation ou une fin d'exercice, comme prévu par la bible principale.

#### 16. Fiches de production et suivi des assets

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

#### 17. Acceptation et ordre des prochaines intégrations

Les scénarios ci-dessous sont des **tests à réaliser**, pas des tests exécutés dans V12. Ils complètent les 18 scénarios de l'Extension 01 et les 22 scénarios de l'Extension 02, conservés intégralement dans les sources. Le [rapport d'intégration](../docs/production/GUIDE_INTEGRATION_V12.md#traçabilité-des-40-cas-dacceptation-sources) associe explicitement chacun des 40 cas à une section de ce chapitre ; tous restent non exécutés dans ce sous-lot documentaire.

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

#### 18. Sources officielles vérifiées pour ce chapitre

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

## Personnages et creatures complementaires V14

Source complète : [CAST_AND_CREATURES_V14.md](../docs/production/CAST_AND_CREATURES_V14.md).

Compléments V14 : références de modèles de production et propositions d'intégration, sans nouveau comportement moteur livré.

### Personnages et créatures complémentaires — V14

**27 novembre 2026.** Cette annexe poursuit la production des images fixes. Les modèles de production cités définissent les cibles visuelles ; les rôles proposés dans le mode combat restent des décisions de conception. Les fichiers effectivement produits et leurs réserves figurent dans le [listing V14](../docs/production/LISTING_V14.md).

#### Mina Jinn — Gears of War 4

La référence retenue est le modèle final de Gears of War 4 publié par Daniel Bohrer do Nascimento avec les contributions de Dan Roarty et Michelle Zhang. Les deux vues montrent le personnage complet, ses lunettes rectangulaires, sa coiffure courte, sa robe bleu nuit à manches longues, son panneau clair vertical et ses chaussures noires. Cette tenue est différente des représentations de Jinn sur un DeeBee ou un écran.

**Cible de production :** une figure isolée, en pied, pose calme, mains vides. Une seule tentative a été refusée par le générateur ; aucun PNG de Mina Jinn n’est livré et aucune relance n’a été effectuée. Aucun équipement militaire supplémentaire n'est inventé. Le personnage est ajouté au catalogue de production, sans être ajouté automatiquement aux 36 combattants du prototype.

**Usage proposé :** dialogues, présentation d'un chapitre CGU et galerie de personnages. Une confrontation où Jinn commande des DeeBees devra être explicitement identifiée comme une adaptation de gameplay ; l'image ne prouve ni un moveset personnel ni une présence physique sur chaque terrain. Sa silhouette verrouillée doit employer cette tenue précise et respecter les règles d'accès du guide commun.

Source primaire : [équipe personnages de The Coalition — Gears of War 4 Art Dump](https://www.zbrushcentral.com/t/gears-of-war-4-art-dump/206321), publication de Daniel Bohrer du 20 octobre 2016, image `Jin_wide1.png`.

#### Reyna humaine — résolution explicite de la cible

L'ancien libellé `reyna_skin_02`, « version humaine future », ne désignait aucune nouvelle forme canonique attestée. Cette passe choisit explicitement **Reyna Diaz humaine, tenue Outsider de Gears of War 4**, documentée en trois vues par Heber Alvarado et Michelle Zhang. Ce choix est une précision du catalogue de production ; les journaux V13 restent conservés et ne sont pas réécrits.

Les invariants sont la natte sur l'épaule anatomique droite, le tatouage sur le bras anatomique gauche, le vêtement écru asymétrique, le tissu olive, les sangles et ceintures, le panneau de jupe à motifs circulaires, les gants et les bottes hautes. La latéralité se contrôle sur les vues avant et arrière : retourner horizontalement une image ne constitue pas une seconde vue fidèle.

**Production :** une image fixe de cette tenue, avec l'accessoire présent dans la référence. La couleur de peau, le visage, le tatouage, les motifs et les accessoires doivent rester comparés au modèle final après génération.

**Conception :** cette version humaine exige une variante de gameplay distincte. La présence du fichier parmi les costumes de production n'autorise pas le moteur à lui attribuer les pouvoirs de la Reine de l'Essaim. Les récits humains, la forme transformée et les simulations libres doivent être séparés. Les paramètres de combat, les coups, les hitboxes et les transitions ne sont pas produits dans cette passe.

Sources primaires : [modèles Gears of War 4 de l'équipe](https://www.zbrushcentral.com/t/gears-of-war-4-art-dump/206321), images `outsider_reyna_body.jpg` et `outsider_reyna_head.jpg` ; [portfolio de Heber Alvarado](https://heber.artstation.com/projects/LxX6v). Les crédits distinguent le corps, la tête et les motifs du tissu.

#### Canker / Carrier Minion — Gears of War 4

Daniel Bohrer présente le modèle final sous le nom de **Carrier Minion**. Le guide officiel de Gears of War 4 nomme les projectiles du Carrier **Cankers**. Le modèle possède un volume organique lumineux, une enveloppe brun rouge et des appendices caudaux allongés. Il est enregistré une fois, dans les projectiles, sans créer un deuxième fichier d'ennemi.

**Production :** un Canker complet en vue horizontale, sac globulaire à droite et appendices vers la gauche, avec le volume lumineux intégré à sa matière. La planche source contient deux vues d'un modèle ; la sortie ne doit contenir qu'un sujet. L'effet d'explosion, le feu au sol et les étapes de lancement devront avoir leurs propres futurs fichiers.

**Adaptation de combat proposée :** un signal d'ouverture du Carrier précède le lancement ; le projectile peut être intercepté avant l'impact. Les fenêtres de ciblage, la vitesse, le guidage et les dégâts restent des paramètres à définir et tester dans le moteur. Aucune valeur de points de vie du TPS n'est transposée automatiquement au jeu de combat.

Sources : [modèle de Daniel Bohrer](https://www.zbrushcentral.com/t/gears-of-war-4-art-dump/206321), publication du 21 octobre 2016, image `CarrierMinion1.png` ; [guide officiel Prima — Swarm, section Carrier](https://primagames.com/eguides/gears-of-war-4-eguide/enemy-forces/swarm).

#### Leech individuel — Gears 5

Le **Leech individuel** constitue une cible distincte de la formation collective `boss_flock`. Les références de Bruno Melo créditent son travail de sculpture, Can Etişkol pour le maillage de jeu et les textures, et Aryan Hanbeck pour la direction artistique. Les deux vues en couleur servent à comparer la bouche lobée, les membranes, les épines, les appendices et les matériaux.

**Production :** une seule créature complète sur fond alpha, sans essaim, sans DeeBee et sans transition d'infection dessinée dans la même image. Une image individuelle ne complète pas les animations du Flock.

**Adaptation proposée :** conserver des entités séparées pour le Leech, le groupe Flock et une machine infectée. Le visuel du Leech peut préparer un défi d'ennemis faibles ou une séquence de menace, mais son comportement de déplacement, ses collisions et son interaction avec une machine restent à développer. Les animations d'attaque, de vol ou d'infection ne sont pas comptées comme livrées.

Sources primaires : [Bruno Melo — Gears 5 Leech](https://bmelo.net/projects/2xzmJB) ; [publication ArtStation correspondante](https://www.artstation.com/artwork/2xzmJB).

#### Wretch — Gears of War: E-Day

La cible est le modèle organique sans armure publié par Antoine Verney-Carron, chez Mighty Canvas, pour **Gears of War: E-Day**. La vue finale complète documente les très longs bras, les grandes mains, les pieds griffus, les bourrelets du front, les yeux pâles, les dents étroites et la peau grise piquetée. Le gros plan soutient le contrôle du visage et de la matière. Aucun nom officiel de sous-variante supplémentaire n'est inventé.

**Production :** une créature seule, entièrement visible, sur fond alpha. La sortie reste en trois-quarts vers la droite ; elle ne vaut pas un profil orthographique. Les épines du dos sont partiellement extrapolées faute de vue arrière et doivent être comparées avant un usage jouable. La couleur RGB stockée sous des pixels d'alpha nul est invisible en composition correcte ; les véritables résidus de faible alpha sont mesurés séparément.

**Adaptation proposée :** ennemi ordinaire d'une épreuve de combat, distinct d'un boss géant et des Wretches des autres opus. La rubrique « boss, créatures et machines » de l'inventaire est un regroupement de production. Elle ne fixe ni taille dans le moteur, ni dégâts, ni hitbox, ni comportement d'attaque.

Source primaire : [Antoine Verney-Carron — Gears of War: E-Day](https://antoineverneycarron.artstation.com/projects/KR3KG4), rendus finaux `wr01` et `wr02`, contributions à la sculpture et aux textures créditées par l'artiste.

#### Ticker organique — Gears of War: E-Day

La partie inférieure de la planche `tc` du même artiste montre un **Ticker organique entier**, avec sa carapace, ses plis et ses appendices. La partie supérieure montre un Reaver et ne fait pas partie de la cible. Le rendu de production ne porte ni bombe ni harnais : ces éléments ne sont pas ajoutés au PNG. Cette entrée est propre à E-Day ; les études de matériaux du Ticker Tactics ne lui sont pas substituées.

**Production :** un seul Ticker entier orienté vers la droite. Les marges alpha utiles restent inférieures aux 8 % demandés et de faibles pixels d'alpha 1 atteignent deux bords. Le fichier natif demeure un candidat à contrôler, sans recadrage ni modification des pixels.

**Adaptation proposée :** préparer un ennemi de déplacement bas au sol. Une éventuelle variante équipée d'explosifs devra posséder sa propre source d'édition, son propre visuel et une définition de gameplay. Le présent PNG organique ne prouve pas une animation de course ou une séquence d'explosion.

Source primaire : [Antoine Verney-Carron — Gears of War: E-Day](https://antoineverneycarron.artstation.com/projects/KR3KG4), [planche finale `tc`](https://cdna.artstation.com/p/assets/images/images/103/353/664/large/antoine-verney-carron-tc.jpg?1792435473).

#### Contrôles communs de fidélité

1. Verrouiller l'opus et le modèle avant génération ; une illustration de concept ne devient pas une preuve du modèle final.
2. Conserver un sujet et une pose par PNG. Mesurer dimensions, alpha, marges et empreinte du fichier natif.
3. Comparer le résultat aux références : silhouette, proportions, latéralité, visage, vêtements, nombre d'appendices et matières.
4. Distinguer les références statiques disponibles, les images à corriger, l'intégration moteur et les animations.
5. Conserver les refus enregistrés sans nouvelle tentative. L'ajout d'une créature différente ne change pas le statut d'un ancien sujet refusé.

Les guides général, Extension 01 et Extension 02 sont toujours présents dans leurs versions originales. Les 68 rubriques et les 40 cas d'acceptation restent traçables ; leur présence documentaire ne signifie pas que les systèmes correspondants sont implémentés.

## Catalogue courant de production

Ce catalogue inclut les ajouts postérieurs au noyau de conception. Une ligne documentée ne rend pas le personnage jouable. Les liens d'images renvoient à des candidats : édition, portion représentée, sources et limites doivent être lus dans les journaux de génération et dans la galerie.

Les variantes d'édition, références partielles et candidats à corriger restent visibles. Le nombre d'images est distinct du nombre d'entrées couvertes : un PNG peut servir de référence à un personnage et à son costume, sans être compté deux fois.

### Personnages

| Identifiant | Sujet | Édition de la référence ou cible | Fichier | État |
| --- | --- | --- | --- | --- |
| `marcus` | Marcus Fenix | Gears of War Ultimate Edition | [PNG](../assets/marcus_neutral_cutout.png) | reference_available · alternate_version |
| `dom` | Dominic Santiago | Gears of War (2006) — COG armor | [PNG](../assets/characters_v5/dom_gow1_fullbody.png) · [journal](../data/generation_v5/dom_record.json) | reference_available · target_version_candidate |
| `baird` | Damon Baird | Gears of War 3 | [PNG](../assets/characters_v2/baird_reference_v3.png) | reference_available · target_version_candidate |
| `cole` | Augustus Cole | Gears of War 3 | [PNG](../assets/characters_v4/cole_reference_v4.png) · [journal](../data/generation_v4/result_cole.json) | reference_available · target_version_candidate |
| `anya` | Anya Stroud | Gears of War 3 | [PNG](../assets/characters/anya_stroud/gears3/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_anya.json) | reference_available · target_version_candidate |
| `kait` | Kait Diaz | Gears 5 hiver | [PNG](../assets/kait_neutral_cutout.png) | reference_available · target_version_candidate |
| `raam` | Général RAAM | Gears of War (2006 / portage PC original) | [PNG](../assets/characters_v5/raam_gow1_fullbody.png) · [journal](../data/generation_v5/raam_record.json) | reference_available · target_version_candidate |
| `skorge` | Skorge | Gears of War 2 | [PNG](../assets/characters_v2/skorge_reference_v3.png) | reference_available · target_version_candidate |
| `myrrah` | Reine Myrrah | Gears of War 3 | [PNG](../assets/characters/myrrah/gears3/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_myrrah.json) | reference_available · target_version_candidate |
| `locust_drone` | Drone locuste | Gears of War 2006 | [PNG](../assets/characters_v2/locust_drone_reference_v2.png) | reference_available · target_version_candidate |
| `kantus` | Kantus | Gears of War 2 | [PNG](../assets/characters_v2/kantus_reference_v3.png) | reference_available · target_version_candidate |
| `theron` | Garde Theron | Theron Guard classique casqué, cible GoW 2006 ; édition exacte non validée | [PNG](../assets/characters_v5/theron_gow1_fullbody.png) · [journal](../data/generation_v5/theron_record.json) | reference_available · target_version_candidate |
| `jd` | JD Fenix | Gears 5 | [PNG](../assets/characters_v2/jd_reference_v2.png) | reference_available · target_version_candidate |
| `del` | Del Walker | Gears 5 | [PNG](../assets/characters_v2/del_reference_v3.png) | reference_available · target_version_candidate |
| `fahz` | Fahz Chutani | Gears 5 | [PNG](../assets/characters/fahz_chutani/gears5/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_fahz.json) | reference_available · target_version_candidate |
| `clayton` | Clayton Carmine | Gears of War 3 | [PNG](../assets/characters/clayton_carmine/gears3/reference_fullbody_v02.png) · [journal](../data/generation_v4/result_clayton.json) | reference_available · target_version_candidate |
| `lizzie` | Lizzie Carmine | Gears 5 | [PNG](../assets/characters_v2/lizzie_reference_v2.png) | reference_available · target_version_candidate |
| `hoffman` | Victor Hoffman | Armure classique | [PNG](../assets/characters/victor_hoffman/classic/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_hoffman.json) | reference_available · edition_unverified |
| `tai` | Tai Kaliso | Gears of War 2 | [PNG](../assets/characters/tai_kaliso/gears2/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_tai.json) | reference_available · target_version_candidate |
| `dizzy` | Dizzy Wallin | Gears of War 2 — tenue de pilote de Betty | [PNG](../assets/characters_v6/dizzy_gow2_fullbody.png) · [journal](../data/generation_v6/dizzy_record.json) | reference_available · target_version_candidate |
| `sam` | Samantha Byrne | Gears of War 3 | [PNG](../assets/characters/samantha_byrne/gears3/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_sam.json) | reference_available · target_version_candidate |
| `paduk` | Garron Paduk | Gears of War Judgment | [PNG](../assets/characters_v2/paduk_reference_v3.png) | reference_available · target_version_candidate |
| `sofia` | Sofia Hendrik | Gears of War Judgment | [PNG](../assets/characters_v2/sofia_reference_v3.png) | reference_available · target_version_candidate |
| `gabe` | Gabe Diaz | Gears Tactics | [PNG](../assets/characters/gabriel_diaz/tactics/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_gabe.json) | reference_available · target_version_candidate |
| `sid` | Sid Redburn | Gears Tactics | [PNG](../assets/characters_v2/sid_reference_v3.png) | reference_available · target_version_candidate |
| `mikayla` | Mikayla Dorn | Gears Tactics | [PNG](../assets/characters/mikayla_dorn/tactics/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_mikayla.json) | reference_available · target_version_candidate |
| `reyna` | Reine Reyna | Gears 5 multijoueur | [PNG](../assets/characters_v2/reyna_reference_v3.png) | reference_available · target_version_candidate |
| `lahni` | Lahni Kaliso | Gears 5 — Hivebuster / Escape | [PNG](../assets/characters/lahni_kaliso/gears5_hivebuster/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_lahni.json) | reference_available · target_version_candidate |
| `keegan` | Keegan | Gears 5 Hivebusters | [PNG](../assets/characters_v4/keegan_reference_v4.png) · [journal](../data/generation_v4/result_keegan.json) | reference_available · target_version_candidate |
| `mac` | Mac | Gears 5 — Hivebuster / Escape | [PNG](../assets/characters/mac_macallister/gears5_hivebuster/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_mac.json) | reference_available · target_version_candidate |
| `jack` | JACK | Gears 5 | [PNG](../assets/characters_v2/jack_reference_v3.png) | reference_available · target_version_candidate |
| `deebee` | DeeBee | Gears of War 4 | [PNG](../assets/characters_v4/deebee_reference_v4.png) · [journal](../data/generation_v4/result_deebee.json) | reference_available · target_version_candidate |
| `warden` | Warden | Gears 5 | [PNG](../assets/characters/warden/gears5/reference_fullbody_v01.png) · [journal](../data/generation_v4/result_warden.json) | reference_available · target_version_candidate |
| `swarm_drone` | Drone de l’Essaim | Gears of War 4 | [PNG](../assets/characters_v2/swarm_drone_reference_v2.png) | reference_available · target_version_candidate |
| `ukkon` | Ukkon | Gears Tactics | [PNG](../assets/characters/ukkon/tactics/reference_fullbody_v02.png) · [journal](../data/generation_v4/result_ukkon.json) | reference_available · target_version_candidate |
| `grenadier` | Grenadier locuste | Gears Tactics | [PNG](../assets/characters_v2/grenadier_reference_v2.png) | reference_available · target_version_candidate |
| `anthony_carmine` | Anthony Carmine | Gears of War (2006) | Absente · [journal](../data/generation_v10/anthony_carmine_record.json) | generation_blocked |
| `benjamin_carmine` | Benjamin Carmine | Gears of War 2 | Absente · [journal](../data/generation_v9/benjamin_carmine_record.json) | generation_blocked |
| `jace_stratton` | Jace Stratton | Gears of War 3 | Absente · [journal](../data/generation_v9/jace_stratton_record.json) | generation_blocked |
| `michael_barrick` | Michael Barrick | Gears of War 3 — RAAM's Shadow, armure standard sans casque | [PNG](../assets/characters_v7/michael_barrick_gow3_raams_shadow_fullbody.png) · [journal](../data/generation_v7/michael_barrick_record.json) | reference_available · alternate_version |
| `alicia_valera` | Alicia Valera | Gears of War 3 — RAAM's Shadow, armure standard sans casque | [PNG](../assets/characters_v6/alicia_valera_gow3_fullbody.png) · [journal](../data/generation_v6/alicia_valera_record.json) | reference_available · alternate_version |
| `minh_young_kim` | Minh Young Kim | Gears of War 3 — RAAM's Shadow | Absente · [journal](../data/generation_v10/minh_young_kim_record.json) | generation_blocked |
| `ezra_loomis` | Colonel Ezra Loomis | Gears of War: Judgment — uniforme de parade, bras croisés | [PNG](../assets/characters_v7/ezra_loomis_judgment_fullbody.png) · [journal](../data/generation_v7/ezra_loomis_record.json) | reference_available · target_version_candidate |
| `bernadette_mataki` | Bernadette « Bernie » Mataki | Gears 5 — Armored Bernie, pose de base fixe | [PNG](../assets/characters_v9/bernie_armored_gears5_fullbody.png) · [journal](../data/generation_v9/bernadette_mataki_record.json) | reference_available · target_version_candidate |
| `ketor_vrol` | Ketor Vrol | Gears 5 — Ketor Vrol multijoueur Operation 8 | [PNG](../assets/characters_v9/ketor_vrol.png) · [journal](../data/generation_v9/ketor_vrol_record.json) | reference_available · target_version_candidate |
| `oscar_diaz` | Oscar Diaz | Last Stand Oscar — Operation 8 Drop 2 (2021) | [PNG](../assets/characters_v10/oscar_diaz.png) · [journal](../data/generation_v10/oscar_diaz_record.json) | reference_available · target_version_candidate |
| `prescott` | Chairman Prescott | Gears 5 — Armored Prescott | Absente · [journal](../data/generation_v9/prescott_record.json) | generation_blocked |
| `hana_cole` | Hana Cole | Gears 5 — Scientist Hana, référence multijoueur Operation 7 à comparer à Hivebusters | [PNG](../assets/characters_v9/hana_cole.png) · [journal](../data/generation_v9/hana_cole_record.json) | reference_available · cross_mode_appearance_candidate |
| `aaron_griffin` | Aaron Griffin | Gears of War 3 — tenue originale du modèle Mike Kime (2011) | [PNG](../assets/characters_v10/aaron_griffin.png) · [journal](../data/generation_v10/aaron_griffin_record.json) | reference_available · target_version_candidate |
| `locust_disciple` | Disciple locuste | Gears Tactics — Disciple standard tête nue, harnais à Imulsion | [PNG](../assets/characters_v9/locust_disciple.png) · [journal](../data/generation_v9/locust_disciple_record.json) | reference_available · licensed_figure_reference_candidate |
| `locust_zealot` | Zealot locuste | Gears Tactics — Zealot standard avec casque pointu | [PNG](../assets/characters_v9/locust_zealot.png) · [journal](../data/generation_v9/locust_zealot_record.json) | reference_available · target_version_candidate |
| `locust_sniper` | Sniper locuste | Gears Tactics — Sniper Drone standard avec Longshot | [PNG](../assets/characters_v9/locust_sniper.png) · [journal](../data/generation_v9/locust_sniper_record.json) | reference_available · target_version_candidate |
| `boomer_tactics` | Boomer locuste | Gears Tactics — Boomer standard avec Boomshot | [PNG](../assets/characters_v6/boomer_tactics_fullbody.png) · [journal](../data/generation_v6/boomer_tactics_record.json) | reference_available · target_version_candidate |
| `adam_fenix` | Adam Fenix | Gears of War 3 — Soldier Adam, personnage multijoueur | [PNG](../assets/characters_v8/adam_fenix_gow3_multiplayer_fullbody.png) · [journal](../data/generation_v8/adam_fenix_record.json) | reference_available · target_version_candidate |
| `alex_brand` | Alex Brand | Gears of War: Judgment — apparence multijoueur, personnage seul | [PNG](../assets/characters_v8/alex_brand_judgment_fullbody.png) · [journal](../data/generation_v8/alex_brand_record.json) | reference_available · target_version_candidate |
| `karn` | Karn | Gears of War: Judgment — Karn intact, personnage seul sans Shibboleth | [PNG](../assets/characters_v8/karn_judgment_intact_fullbody.png) · [journal](../data/generation_v8/karn_record.json) | reference_available · target_version_candidate |
| `mina_jinn_g4` | Mina Jinn — Gears of War 4 | Gears of War 4 | Absente · [journal](../data/generation_v14/mina_jinn_g4_record.json) | generation_blocked |

### Costumes

| Identifiant | Sujet | Édition de la référence ou cible | Fichier | État |
| --- | --- | --- | --- | --- |
| `marcus_skin_01` | Marcus Fenix — Émergence E-Day | Marcus jeune — modèle de production E-Day | [PNG](../assets/costumes_v12/marcus_eday.png) · [journal](../data/generation_v12/marcus_skin_01_record.json) | reference_available · target_version_candidate |
| `marcus_skin_02` | Marcus Fenix — Campagne Gears of War 2006 | Marcus du premier Gears original, modèle du port PC ; équivalence Xbox 360 2006 à vérifier | [PNG](../assets/costumes_v11/marcus_skin_02.png) · [journal](../data/generation_v11/marcus_skin_02_record.json) | reference_available · original_pc_port_candidate_for_2006_target |
| `marcus_skin_03` | Marcus Fenix — Campagne Gears of War 3 | Gears of War 3 — armure de campagne | [PNG](../assets/costumes_v8/marcus_campaign_gow3_fullbody.png) · [journal](../data/generation_v8/marcus_campaign_record.json) | reference_available · target_version_candidate |
| `marcus_skin_04` | Marcus Fenix — Vétéran Gears 5 | Marcus âgé et barbu en armure Gears 5 | [PNG](../assets/costumes_v11/marcus_skin_04.png) · [journal](../data/generation_v11/marcus_skin_04_record.json) | reference_available · target_version_candidate |
| `dom_skin_01` | Dominic Santiago — Émergence E-Day | Dom jeune — modèle de production E-Day | [PNG](../assets/costumes_v12/dom_eday.png) · [journal](../data/generation_v12/dom_skin_01_record.json) | reference_available · target_version_candidate |
| `dom_skin_02` | Dominic Santiago — Campagne Gears of War 2006 | Gears of War (2006) — COG armor | [PNG](../assets/characters_v5/dom_gow1_fullbody.png) | reference_available · target_version_candidate |
| `dom_skin_03` | Dominic Santiago — Campagne Gears of War 2 | Campagne Gears of War 2 | Absente · [journal](../data/generation_v11/dom_skin_03_record.json) | generation_blocked |
| `dom_skin_04` | Dominic Santiago — Campagne Gears of War 3 | Dom barbu de campagne, cuirasse sans manches | [PNG](../assets/costumes_v11/dom_skin_04.png) · [journal](../data/generation_v11/dom_skin_04_record.json) | reference_available · target_version_candidate |
| `baird_skin_01` | Damon Baird — Lieutenant Judgment | Lieutenant Baird — modèle original Judgment | [PNG](../assets/costumes_v10/baird_skin_01.png) · [journal](../data/generation_v10/baird_skin_01_record.json) | reference_available · target_version_candidate |
| `baird_skin_02` | Damon Baird — Campagne Gears of War 2006 | Campagne Gears of War 2006 | Absente · [journal](../data/generation_v12/baird_skin_02_record.json) | generation_blocked |
| `baird_skin_03` | Damon Baird — Campagne Gears of War 3 | Gears of War 3 | [PNG](../assets/characters_v2/baird_reference_v3.png) | reference_available · target_version_candidate |
| `baird_skin_04` | Damon Baird — Ingénieur Gears 5 | DB Industries Baird — âgé, blouse de laboratoire (campagne et Operation 3) | [PNG](../assets/costumes_v10/baird_skin_04.png) · [journal](../data/generation_v10/baird_skin_04_record.json) | reference_available · target_version_candidate |
| `cole_skin_01` | Augustus Cole — Kilo Squad Judgment | Kilo Squad Judgment | Absente · [journal](../data/generation_v11/cole_skin_01_record.json) | generation_blocked |
| `cole_skin_02` | Augustus Cole — Campagne Gears of War 3 | Gears of War 3 | [PNG](../assets/characters_v4/cole_reference_v4.png) | reference_available · target_version_candidate |
| `cole_skin_03` | Augustus Cole — Tenue thrashball de référence | Gears of War 3 — Thrashball Cole | [PNG](../assets/costumes_v7/cole_thrashball_gow3_fullbody.png) · [journal](../data/generation_v7/cole_thrashball_record.json) | reference_available · target_version_candidate |
| `cole_skin_04` | Augustus Cole — Vétéran Gears 5 | Cole du rendu officiel multijoueur Operation 3 ; correspondance avec le vétéran de campagne non établie | [PNG](../assets/costumes_v11/cole_skin_04.png) · [journal](../data/generation_v11/cole_skin_04_record.json) | reference_available · alternate_version |
| `anya_skin_01` | Anya Stroud — Contrôle Gears of War 2 | Gears of War 2 | Absente · [journal](../data/generation_v13/anya_skin_01_record.json) | missing |
| `anya_skin_02` | Anya Stroud — Combat de campagne Gears of War 3 | Gears of War 3 | [PNG](../assets/characters/anya_stroud/gears3/reference_fullbody_v01.png) | reference_available · target_version_candidate |
| `kait_skin_01` | Kait Diaz — Outsider Gears of War 4 | Kait Outsider — veste courte brune, Gears of War 4 | [PNG](../assets/costumes_v11/kait_skin_01.png) · [journal](../data/generation_v11/kait_skin_01_record.json) | reference_available · target_version_candidate |
| `kait_skin_02` | Kait Diaz — Hiver Gears 5 | Gears 5 hiver | [PNG](../assets/kait_neutral_cutout.png) | reference_available · target_version_candidate |
| `kait_skin_03` | Kait Diaz — Désert Gears 5 | Désert Gears 5 | Absente · [journal](../data/generation_v12/kait_skin_03_record.json) | generation_blocked |
| `raam_skin_01` | Général RAAM — Combat final Gears of War 2006 | Gears of War (2006 / portage PC original) | [PNG](../assets/characters_v5/raam_gow1_fullbody.png) | reference_available · target_version_candidate |
| `raam_skin_02` | Général RAAM — RAAM’s Shadow à documenter séparément | RAAM’s Shadow à documenter séparément | Absente · [journal](../data/generation_v13/raam_skin_02_record.json) | missing |
| `skorge_skin_01` | Skorge — Palais Gears of War 2 | Gears of War 2 | [PNG](../assets/characters_v2/skorge_reference_v3.png) | reference_available · target_version_candidate |
| `skorge_skin_02` | Skorge — Aspect multijoueur Gears 5 | Aspect multijoueur Gears 5 | Absente · [journal](../data/generation_v13/skorge_skin_02_record.json) | generation_blocked |
| `myrrah_skin_01` | Reine Myrrah — Armure royale Gears of War 3 | Gears of War 3 | [PNG](../assets/characters/myrrah/gears3/reference_fullbody_v01.png) | reference_available · target_version_candidate |
| `myrrah_skin_02` | Reine Myrrah — Apparence multijoueur Gears 5 | Apparence multijoueur Gears 5 | Absente · [journal](../data/generation_v13/myrrah_skin_02_record.json) | missing |
| `locust_drone_skin_01` | Drone locuste — Drone Gears of War 2006 | Gears of War 2006 | [PNG](../assets/characters_v2/locust_drone_reference_v2.png) | reference_available · target_version_candidate |
| `locust_drone_skin_02` | Drone locuste — Drone E-Day à contrôler sur capture | Modèle multijoueur visible dans la galerie officielle E-Day | [PNG](../assets/costumes_v13/locust_drone_eday_multiplayer.png) · [journal](../data/generation_v13/locust_drone_skin_02_record.json) | reference_available · target_version_candidate |
| `kantus_skin_01` | Kantus — Kantus Gears of War 2 | Gears of War 2 | [PNG](../assets/characters_v2/kantus_reference_v3.png) | reference_available · target_version_candidate |
| `kantus_skin_02` | Kantus — Kantus Gears Tactics | Kantus Gears Tactics | Absente · [journal](../data/generation_v12/kantus_skin_02_record.json) | generation_blocked |
| `theron_skin_01` | Garde Theron — Garde Theron Gears of War 2006 | Garde Theron Gears of War 2006 | Absente · [journal](../data/generation_v13/theron_skin_01_record.json) | generation_blocked |
| `theron_skin_02` | Garde Theron — Garde Theron Gears Tactics | Garde Theron Gears Tactics | Absente · [journal](../data/generation_v13/theron_skin_02_record.json) | missing |
| `jd_skin_01` | JD Fenix — Outsider Gears of War 4 | JD Outsider — concept Microsoft avril 2016, corroboration partielle campagne | [PNG](../assets/costumes_v12/jd_skin_01.png) · [journal](../data/generation_v12/jd_skin_01_record.json) | reference_available · edition_unverified |
| `jd_skin_02` | JD Fenix — CGU Gears 5 prologue | JD CGU non cicatrisé — début de campagne Gears 5 | [PNG](../assets/costumes_v13/jd_skin_02.png) · [journal](../data/generation_v13/jd_skin_02_record.json) | reference_available · target_version_candidate |
| `jd_skin_03` | JD Fenix — CGU Gears 5 après ellipse | Gears 5 | [PNG](../assets/characters_v2/jd_reference_v2.png) | reference_available · target_version_candidate |
| `del_skin_01` | Del Walker — Outsider Gears of War 4 | Del Outsider — concept Goran Bukvic/Microsoft, corroboration partielle campagne | [PNG](../assets/costumes_v12/del_skin_01.png) · [journal](../data/generation_v12/del_skin_01_record.json) | reference_available · edition_unverified |
| `del_skin_02` | Del Walker — Campagne Gears 5 | Gears 5 | [PNG](../assets/characters_v2/del_reference_v3.png) | reference_available · target_version_candidate |
| `fahz_skin_01` | Fahz Chutani — Campagne Gears 5 | Gears 5 | [PNG](../assets/characters/fahz_chutani/gears5/reference_fullbody_v01.png) | reference_available · target_version_candidate |
| `clayton_skin_01` | Clayton Carmine — Campagne Gears of War 3 | Gears of War 3 | [PNG](../assets/characters/clayton_carmine/gears3/reference_fullbody_v02.png) | reference_available · target_version_candidate |
| `clayton_skin_02` | Clayton Carmine — Vétéran Gears 5 | Modèle multijoueur Gears 5 Operation 3 montré par Xbox Wire le 31 mars 2020 | [PNG](../assets/costumes_v12/clayton_gears5_operation3.png) · [journal](../data/generation_v12/clayton_skin_02_record.json) | reference_available · edition_unverified |
| `lizzie_skin_01` | Lizzie Carmine — Campagne Gears 5 | Gears 5 | [PNG](../assets/characters_v2/lizzie_reference_v2.png) | reference_available · target_version_candidate |
| `hoffman_skin_01` | Victor Hoffman — Hoffman en armure Gears 5 | Gears 5 multijoueur | [PNG](../assets/characters_v4/hoffman_reference_v4.png) | reference_available · target_version_candidate |
| `hoffman_skin_02` | Victor Hoffman — Commandant Gears of War 3 à documenter | Hoffman Gears 3 — modèle de production Epic | [PNG](../assets/costumes_v13/hoffman_skin_02.png) · [journal](../data/generation_v13/hoffman_skin_02_record.json) | reference_available · target_version_candidate |
| `tai_skin_01` | Tai Kaliso — Campagne Gears of War 2 | Gears of War 2 | [PNG](../assets/characters/tai_kaliso/gears2/reference_fullbody_v01.png) | reference_available · target_version_candidate |
| `tai_skin_02` | Tai Kaliso — E-Day sur références officielles | E-Day sur références officielles | Absente · [journal](../data/generation_v13/tai_skin_02_record.json) | missing |
| `dizzy_skin_01` | Dizzy Wallin — Pilote Gears of War 2 | Gears of War 2 — tenue de pilote de Betty | [PNG](../assets/characters_v6/dizzy_gow2_fullbody.png) | reference_available · target_version_candidate |
| `dizzy_skin_02` | Dizzy Wallin — Aspect Gears of War 3 à documenter | Dizzy standard Gears 3 — rendu Epic 2011, copie de diffusion | [PNG](../assets/costumes_v13/dizzy_skin_02.png) · [journal](../data/generation_v13/dizzy_skin_02_record.json) | reference_available · target_version_candidate |
| `sam_skin_01` | Samantha Byrne — Campagne Gears of War 3 | Gears of War 3 | [PNG](../assets/characters/samantha_byrne/gears3/reference_fullbody_v01.png) | reference_available · target_version_candidate |
| `sam_skin_02` | Samantha Byrne — Vétérane Gears of War 4 à documenter | Vétérane Gears of War 4 à documenter | Absente · [journal](../data/generation_v13/sam_skin_02_record.json) | missing |
| `paduk_skin_01` | Garron Paduk — Kilo Squad Judgment | Gears of War Judgment | [PNG](../assets/characters_v2/paduk_reference_v3.png) | reference_available · target_version_candidate |
| `paduk_skin_02` | Garron Paduk — Vétéran Gears 5 | Paduk âgé — armure UIR verte de campagne Gears 5 | [PNG](../assets/costumes_v11/paduk_skin_02.png) · [journal](../data/generation_v11/paduk_skin_02_record.json) | reference_available · target_version_candidate |
| `sofia_skin_01` | Sofia Hendrik — Kilo Squad Judgment | Gears of War Judgment | [PNG](../assets/characters_v2/sofia_reference_v3.png) | reference_available · target_version_candidate |
| `gabe_skin_01` | Gabe Diaz — Tenue de base Gears Tactics | Gears Tactics | [PNG](../assets/characters/gabriel_diaz/tactics/reference_fullbody_v01.png) | reference_available · target_version_candidate |
| `gabe_skin_02` | Gabe Diaz — Gabe Gears 5 | Gabe Gears 5 | Absente · [journal](../data/generation_v13/gabe_skin_02_record.json) | missing |
| `sid_skin_01` | Sid Redburn — Tenue de base Gears Tactics | Gears Tactics | [PNG](../assets/characters_v2/sid_reference_v3.png) | reference_available · target_version_candidate |
| `mikayla_skin_01` | Mikayla Dorn — Tenue de base Gears Tactics | Gears Tactics | [PNG](../assets/characters/mikayla_dorn/tactics/reference_fullbody_v01.png) | reference_available · target_version_candidate |
| `reyna_skin_01` | Reine Reyna — Reine Reyna Gears 5 | Gears 5 multijoueur | [PNG](../assets/characters_v2/reyna_reference_v3.png) | reference_available · target_version_candidate |
| `reyna_skin_02` | Reyna Diaz humaine — Outsider Gears of War 4 | Reyna Diaz humaine Outsider — modèle final Gears of War 4 | [PNG](../assets/costumes_v14/reyna_human_g4_hairfix.png) · [journal](../data/generation_v14/reyna_skin_02_record.json) | reference_available · target_version_candidate |
| `lahni_skin_01` | Lahni Kaliso — Brash Brigade, tenue finale du début de Hivebusters | Brash Brigade Lahni — tenue en armure du début du DLC, modèle final | [PNG](../assets/costumes_v13/lahni_skin_01.png) · [journal](../data/generation_v13/lahni_skin_01_record.json) | reference_available · target_version_candidate |
| `lahni_skin_02` | Lahni Kaliso — Tenue Escape Gears 5 | Gears 5 — Hivebuster / Escape | [PNG](../assets/characters/lahni_kaliso/gears5_hivebuster/reference_fullbody_v01.png) | reference_available · target_version_candidate |
| `keegan_skin_01` | Keegan — Campagne Hivebusters | Gears 5 Hivebusters | [PNG](../assets/characters_v4/keegan_reference_v4.png) | reference_available · target_version_candidate |
| `keegan_skin_02` | Keegan — Onyx Guard Keegan à documenter | Onyx Guard Keegan à documenter | Absente · [journal](../data/generation_v13/keegan_skin_02_record.json) | generation_blocked |
| `mac_skin_01` | Mac — Campagne Hivebusters | Gears 5 Hivebusters | [PNG](../assets/characters_v4/mac_reference_v4.png) | reference_available · target_version_candidate |
| `mac_skin_02` | Mac — Mechanic Mac | Gears 5 — Mechanic Mac (skin Hivebusters) | [PNG](../assets/costumes_v6/mac_mechanic_gears5_fullbody.png) · [journal](../data/generation_v6/mac_mechanic_record.json) | reference_available · target_version_candidate |
| `jack_skin_01` | JACK — JACK Gears 5 | Gears 5 | [PNG](../assets/characters_v2/jack_reference_v3.png) | reference_available · target_version_candidate |
| `jack_skin_02` | JACK — JACK Gears Tactics traité en variante séparée | JACK Tactics — robot de soutien à quatre optiques, bras manipulateur et outil distincts | [PNG](../assets/costumes_v12/jack_tactics.png) · [journal](../data/generation_v12/jack_skin_02_record.json) | reference_available · target_version_candidate |
| `deebee_skin_01` | DeeBee — Shepherd Gears of War 4 | Gears of War 4 | [PNG](../assets/characters_v4/deebee_reference_v4.png) | reference_available · target_version_candidate |
| `deebee_skin_02` | DeeBee — DeeBee multijoueur Gears 5 | DeeBee multijoueur Gears 5 | Absente · [journal](../data/generation_v13/deebee_skin_02_record.json) | missing |
| `warden_skin_01` | Warden — Warden Gears 5 | Gears 5 | [PNG](../assets/characters/warden/gears5/reference_fullbody_v01.png) | reference_available · target_version_candidate |
| `swarm_drone_skin_01` | Drone de l’Essaim — Drone Gears of War 4 | Gears of War 4 | [PNG](../assets/characters_v2/swarm_drone_reference_v2.png) | reference_available · target_version_candidate |
| `swarm_drone_skin_02` | Drone de l’Essaim — Drone Gears 5 | Swarm Drone Rifleman — modèle standard Gears 5 | [PNG](../assets/costumes_v12/swarm_drone_skin_02.png) · [journal](../data/generation_v12/swarm_drone_skin_02_record.json) | reference_available · target_version_candidate |
| `ukkon_skin_01` | Ukkon — Campagne Gears Tactics | Gears Tactics | [PNG](../assets/characters/ukkon/tactics/reference_fullbody_v02.png) | reference_available · target_version_candidate |
| `grenadier_skin_01` | Grenadier locuste — Grenadier Gears Tactics | Gears Tactics | [PNG](../assets/characters_v2/grenadier_reference_v2.png) | reference_available · target_version_candidate |
| `grenadier_skin_02` | Grenadier locuste — Grenadier Gears of War 2006 à documenter | Grenadier Gears of War 2006 à documenter | Absente · [journal](../data/generation_v13/grenadier_skin_02_record.json) | missing |
| `lahni_hivebusters_intro` | Lahni Kaliso — introduction Hivebusters (alias Brash Brigade) | Brash Brigade Lahni — tenue en armure du début du DLC, modèle final | [PNG](../assets/costumes_v13/lahni_skin_01.png) · [journal](../data/generation_v14/lahni_hivebusters_intro_record.json) | reference_available · target_version_candidate |
| `keegan_hivebusters_intro` | Keegan — Keegan — tenue d'introduction Hivebusters | Gears 5: Hivebusters | Absente · [journal](../data/generation_v13/keegan_hivebusters_intro_record.json) | missing |
| `anthony_black_steel_g5` | Anthony Carmine — Black Steel Anthony Carmine | Gears 5 | Absente · [journal](../data/generation_v13/anthony_black_steel_g5_record.json) | missing |
| `bernie_armored_g5` | Bernadette « Bernie » Mataki — Armored Bernie | Gears 5 — Armored Bernie, pose de base fixe | [PNG](../assets/characters_v9/bernie_armored_gears5_fullbody.png) | reference_available · target_version_candidate |
| `sam_vday_g5` | Samantha Byrne — V-Day Sam | Gears 5 — V-Day Sam, pose fixe en pied | [PNG](../assets/costumes_v10/sam_vday_gears5_fullbody.png) · [journal](../data/generation_v10/sam_vday_g5_record.json) | reference_available · target_version_candidate |
| `myrrah_black_steel_g5` | Reine Myrrah — Black Steel Queen Myrrah | Gears 5 — Black Steel Queen Myrrah, pose fixe en pied | [PNG](../assets/costumes_v10/myrrah_black_steel_gears5_fullbody.png) · [journal](../data/generation_v10/myrrah_black_steel_g5_record.json) | reference_available · target_version_candidate |
| `fahz_hivebuster_g5` | Fahz Chutani — Hivebuster Fahz | Gears 5 | Absente · [journal](../data/generation_v12/fahz_hivebuster_g5_record.json) | generation_blocked |
| `reyna_blood_red_g5` | Reine Reyna — Blood Red Queen Reyna | Blood Red Queen Reyna — skin multijoueur Operation 6, tentacules inférieurs reconstitués | [PNG](../assets/costumes_v12/reyna_blood_red_g5.png) · [journal](../data/generation_v12/reyna_blood_red_g5_record.json) | reference_available · target_version_candidate |
| `swarm_drone_uir_g5` | Drone de l’Essaim — Swarm Elite Drone UIR | UIR Elite Drone — skin multijoueur Gears 5 Operation 6 | [PNG](../assets/costumes_v12/swarm_drone_uir_g5.png) · [journal](../data/generation_v12/swarm_drone_uir_g5_record.json) | reference_available · target_version_candidate |
| `zealot_collectors_g5` | Zealot locuste — Collector's Zealot | Collector's Zealot — skin multijoueur Gears 5 Operation 6 | [PNG](../assets/costumes_v12/zealot_collectors_g5.png) · [journal](../data/generation_v12/zealot_collectors_g5_record.json) | reference_available · target_version_candidate |

### Boss, creatures et machines

| Identifiant | Sujet | Édition de la référence ou cible | Fichier | État |
| --- | --- | --- | --- | --- |
| `boss_berserker` | Berserker | Gears of War (2006) — candidat guidé par promotion d'époque et artbook | [PNG](../assets/bosses_v9/berserker_gears2006_fullbody.png) · [journal](../data/generation_v9/boss_berserker_record.json) | reference_available · target_version_candidate |
| `boss_corpser` | Corpser | Gears Tactics | [PNG](../assets/bosses_v4/boss_corpser_reference_v4.png) · [journal](../data/generation_v4/result_boss_corpser.json) | reference_available · target_version_candidate |
| `boss_brumak` | Brumak | Gears Tactics | [PNG](../assets/bosses_v4/boss_brumak_reference_v4.png) · [journal](../data/generation_v4/result_boss_brumak.json) | reference_available · target_version_candidate |
| `boss_reaver` | Reaver | Gears of War 2 — Reaver, pose fixe | [PNG](../assets/bosses_v10/reaver_gears2_mount_only_fullbody.png) · [journal](../data/generation_v10/boss_reaver_record.json) | reference_available · target_version_candidate |
| `boss_leviathan` | Leviathan | Gears of War 2 — Leviathan original, modèle recourbé et pose fixe | [PNG](../assets/bosses_v11/leviathan_gears2_fullbody.png) · [journal](../data/generation_v11/boss_leviathan_record.json) | reference_available · target_version_candidate |
| `boss_hydra_skorge` | Hydra de Skorge | Gears of War 2 | Absente · [journal](../data/generation_v13/boss_hydra_skorge_record.json) | missing |
| `boss_lambent_brumak` | Brumak Lambent | Gears of War 2 — Lambent Brumak final, assemblage statique du modèle attesté | [PNG](../assets/bosses_v11/lambent_brumak_gears2_model_assembly.png) · [journal](../data/generation_v11/boss_lambent_brumak_record.json) | reference_available · target_version_candidate |
| `boss_lambent_berserker` | Berserker Lambent | Gears of War 3 — poitrine ouverte, pose de référence | [PNG](../assets/bosses_v8/lambent_berserker_gow3_fullbody.png) · [journal](../data/generation_v8/lambent_berserker_record.json) | reference_available · target_version_candidate |
| `boss_lambent_leviathan` | Leviathan Lambent | Gears of War 3 — Lambent Leviathan, volume visible du modèle, pose fixe | [PNG](../assets/bosses_v11/lambent_leviathan_gears3_visible_model.png) · [journal](../data/generation_v11/boss_lambent_leviathan_record.json) | reference_available · target_version_candidate |
| `boss_tempest` | Tempest et Myrrah | Gears of War 3 — monture seule ; Myrrah absente ; duo non complet | [PNG](../assets/bosses_v8/tempest_gow3_mount_only_fullbody.png) · [journal](../data/generation_v8/tempest_record.json) | reference_available · target_version_candidate |
| `boss_shibboleth` | Karn sur Shibboleth | Gears of War: Judgment — monture seule ; Karn absent ; duo non complet | [PNG](../assets/bosses_v7/shibboleth_judgment_mount_only_fullbody.png) · [journal](../data/generation_v7/shibboleth_record.json) | reference_available · target_version_candidate |
| `boss_hydra_ukkon` | Hydra d’Ukkon | Gears Tactics — Hydra d’Ukkon, tête et torse supérieur attestés, sans cavalier | [PNG](../assets/bosses_v11/hydra_ukkon_tactics_upperbody_portion.png) · [journal](../data/generation_v11/boss_hydra_ukkon_record.json) | reference_available · target_version_candidate |
| `boss_swarmak` | Swarmak | Gears of War 4 — Swarmak, pose fixe | [PNG](../assets/bosses_v10/swarmak_gears4_fullbody.png) · [journal](../data/generation_v10/boss_swarmak_record.json) | reference_available · target_version_candidate |
| `boss_snatcher` | Snatcher | Gears of War 4 — Snatcher, pose fixe | [PNG](../assets/bosses_v10/snatcher_gears4_fullbody.png) · [journal](../data/generation_v10/boss_snatcher_record.json) | reference_available · target_version_candidate |
| `boss_carrier` | Carrier | Gears of War 4 — Carrier, pose fixe | [PNG](../assets/bosses_v10/carrier_gears4_fullbody.png) · [journal](../data/generation_v10/boss_carrier_record.json) | reference_available · target_version_candidate |
| `boss_kestrel` | Kestrel | Gears of War 4 | [PNG](../assets/bosses_v4/boss_kestrel_reference_v4.png) · [journal](../data/generation_v4/result_boss_kestrel.json) | reference_available · target_version_candidate |
| `boss_hive_beast` | Hive Beast | Gears of War 4 — Hive Beast, portion émergente attestée et quatre tentacules, pose fixe | [PNG](../assets/bosses_v11/hive_beast_gears4_visible_portion.png) · [journal](../data/generation_v11/boss_hive_beast_record.json) | reference_available · target_version_candidate |
| `boss_matriarch` | Matriarch | Gears 5 — modèle de campagne | [PNG](../assets/bosses_v6/matriarch_gears5_fullbody.png) · [journal](../data/generation_v6/matriarch_record.json) | reference_available · target_version_candidate |
| `boss_kraken` | Kraken | Gears 5 — tête et manteau exposés du Kraken, ensemble central seulement | [PNG](../assets/bosses_v12/kraken_gears5_head_mantle.png) · [journal](../data/generation_v12/boss_kraken_record.json) | reference_available · target_version_candidate |
| `boss_flock` | Flock | Gears 5 — essaim de Leeches, formation collective recomposée | [PNG](../assets/bosses_v12/flock_gears5_swarm.png) · [journal](../data/generation_v12/boss_flock_record.json) | reference_available · target_version_candidate |
| `boss_wakaatu` | Wakaatu | Gears 5 Hivebusters | Absente · [journal](../data/generation_v13/boss_wakaatu_record.json) | missing |
| `boss_king_raven` | King Raven de simulation | Gears of War (2006) | [PNG](../assets/bosses_v4/boss_king_raven_reference_v4.png) · [journal](../data/generation_v4/result_boss_king_raven.json) | reference_available · target_version_candidate |
| `boss_centaur` | Centaur de simulation | Gears of War 2 — Centaur, pose fixe | [PNG](../assets/bosses_v10/centaur_gears2_fullbody.png) · [journal](../data/generation_v10/boss_centaur_record.json) | reference_available · target_version_candidate |
| `boss_silverback` | Silverback de simulation | Gears of War 3 — exosquelette seul, sans pilote | [PNG](../assets/bosses_v9/silverback_gears3_fullbody.png) · [journal](../data/generation_v9/boss_silverback_record.json) | reference_available · target_version_candidate |
| `boss_pouncer_g4` | Pouncer | Gears of War 4 — Pouncer, pose fixe | [PNG](../assets/bosses_v9/pouncer_gears4_fullbody.png) · [journal](../data/generation_v9/boss_pouncer_g4_record.json) | reference_available · target_version_candidate |
| `boss_dr1_g4` | DeeBee DR-1 | Gears of War 4 — DR-1 bleu avec Overkill | [PNG](../assets/bosses_v9/dr1_gears4_fullbody.png) · [journal](../data/generation_v9/boss_dr1_g4_record.json) | reference_available · target_version_candidate |
| `boss_guardian_g4` | DeeBee Guardian | Gears of War 4 — Guardian Tri-Shot, drone seul sans bouclier actif | [PNG](../assets/bosses_v9/guardian_gears4_fullbody.png) · [journal](../data/generation_v9/boss_guardian_g4_record.json) | reference_available · target_version_candidate |
| `boss_scion_g4` | Scion | Gears of War 4 | Absente · [journal](../data/generation_v9/boss_scion_g4_record.json) | generation_blocked |
| `boss_rager_g5` | Rager — épreuve de combat | Rager normal de Gears 5 Op8 Drop2, échelle humanoïde, mains vides | [PNG](../assets/bosses_v11/rager_gears5_normal_fullbody.png) · [journal](../data/generation_v11/boss_rager_g5_record.json) | reference_available · target_version_candidate |
| `boss_riftworm_g2` | Riftworm — rencontre environnementale | Riftworm Gears of War 2 — corps extérieur complet, vue latérale de modèle | [PNG](../assets/bosses_v13/riftworm_g2_exterior.png) · [journal](../data/generation_v13/boss_riftworm_g2_record.json) | reference_available · target_version_candidate |
| `boss_sire_g5` | Sire — épreuve de capture | Gears 5 | Absente · [journal](../data/generation_v13/boss_sire_g5_record.json) | missing |
| `creature_leech_g5` | Leech individuel — Gears 5 | Leech individuel — modèle final Gears 5, forme déployée | [PNG](../assets/creatures_v14/leech_g5.png) · [journal](../data/generation_v14/creature_leech_g5_record.json) | reference_available · target_version_candidate |
| `creature_wretch_eday` | Wretch — Gears of War: E-Day | Wretch E-Day — modèle organique sans armure publié par Antoine Verney-Carron | [PNG](../assets/creatures_v14/wretch_eday.png) · [journal](../data/generation_v14/creature_wretch_eday_record.json) | reference_available · target_version_candidate |
| `creature_ticker_eday` | Ticker organique — Gears of War: E-Day | Ticker E-Day — modèle organique sans harnais ni bombe, partie inférieure du rendu final | [PNG](../assets/creatures_v14/ticker_eday.png) · [journal](../data/generation_v14/creature_ticker_eday_record.json) | reference_available · target_version_candidate |

### Stages

| Identifiant | Sujet | Édition de la référence ou cible | Fichier | État |
| --- | --- | --- | --- | --- |
| `stage_sovereigns` | House of Sovereigns | Gears of War (2006) — parvis extérieur adapté au combat latéral | [PNG](../assets/stages_v9/house_of_sovereigns_gow2006_master.png) · [journal](../data/generation_v9/stage_sovereigns_record.json) | reference_available · target_version_candidate |
| `stage_fenix_estate` | Haldane Hall et domaine Fenix | Gears of War 2006 — terrasse du jardin et escalier du domaine adaptés au combat latéral | [PNG](../assets/stages_v9/fenix_estate_gow2006_garden_master.png) · [journal](../data/generation_v9/stage_fenix_estate_record.json) | reference_available · target_version_candidate |
| `stage_tyro_pillar` | Tyro Pillar | Gears of War 2006 — pont de fret adapté au combat latéral | [PNG](../assets/stages_v9/tyro_pillar_gow2006_master.png) · [journal](../data/generation_v9/stage_tyro_pillar_record.json) | reference_available · target_version_candidate |
| `stage_hollow` | Les profondeurs | Gears of War 2 | [PNG](../assets/stage_hollow.png) | reference_available · target_version_candidate |
| `stage_hollow_lake` | Lac des profondeurs | Gears of War 2 — lac souterrain depuis un pont de bateau adapté au combat latéral | [PNG](../assets/stages_v10/hollow_lake_gears2_boat_master.png) · [journal](../data/generation_v10/stage_hollow_lake_record.json) | reference_available · target_version_candidate |
| `stage_stromson` | Forêt de Stromson | Gears of War 2 — lisière de Stromson avec derrick immobilisé, adaptée au combat latéral | [PNG](../assets/stages_v10/stromson_forest_gears2_master.png) · [journal](../data/generation_v10/stage_stromson_record.json) | reference_available · target_version_candidate |
| `stage_jacinto` | Jacinto au bord de la chute | Gears of War 2 — terrasses effondrées de Jacinto adaptées au combat latéral | [PNG](../assets/stages_v10/jacinto_gears2_collapse_master.png) · [journal](../data/generation_v10/stage_jacinto_record.json) | reference_available · target_version_candidate |
| `stage_anvil_gate` | Anvil Gate | Gears of War 3 — cour intérieure de la porte 02 adaptée au combat latéral | [PNG](../assets/stages_v9/anvil_gate_gears3_master.png) · [journal](../data/generation_v9/stage_anvil_gate_record.json) | reference_available · target_version_candidate |
| `stage_sovereign_deck` | Pont du Sovereign | Gears of War 3 — pont extérieur jardiné du Sovereign adapté au combat latéral | [PNG](../assets/stages_v10/sovereign_deck_gears3_master.png) · [journal](../data/generation_v10/stage_sovereign_deck_record.json) | reference_available · target_version_candidate |
| `stage_azura_tower` | Azura et la tour | Gears of War 3 — terrasse et fontaines devant Pinnacle Tower adaptées au combat latéral | [PNG](../assets/stages_v10/azura_tower_gears3_terrace_master.png) · [journal](../data/generation_v10/stage_azura_tower_record.json) | reference_available · target_version_candidate |
| `stage_halvo_plaza` | Place de Halvo Bay | Gears of War: Judgment | [PNG](../assets/stages_v11/halvo_plaza_judgment_courthouse_night_master.png) · [journal](../data/generation_v11/stage_halvo_plaza_record.json) | reference_available · target_version_candidate |
| `stage_tactics_depot` | Cour de ravitaillement | Création de cour logistique pour le projet à partir du biome COG Industrial ; aucun dépôt canonique nommé revendiqué | [PNG](../assets/stages_v11/tactics_depot_cog_industrial_courtyard_master.png) · [journal](../data/generation_v11/stage_tactics_depot_record.json) | reference_available · target_version_candidate |
| `stage_tactics_lab` | Laboratoire d’Ukkon | Laboratoire d’Ukkon — adaptation latérale du concept Act3Finale_ArenaFeedback de Malte Langheim | [PNG](../assets/stages_v11/stage_tactics_lab.png) · [journal](../data/generation_v11/stage_tactics_lab_record.json) | reference_available · concept_art_candidate |
| `stage_settlement5` | Settlement 5 | Rue du niveau Raid et portail de sécurité, adaptation latérale issue de captures finales | [PNG](../assets/stages_v11/settlement5_gears4_security_gate_master.png) · [journal](../data/generation_v11/stage_settlement5_record.json) | reference_available · target_version_candidate |
| `stage_swarm_hive` | Ruche de l’Essaim | Composition latérale originale d’un intérieur de ruche fondée sur les environnements Swarm finaux de Gears 4 | [PNG](../assets/stages_v11/swarm_hive_gears4_infested_chamber_master.png) · [journal](../data/generation_v11/stage_swarm_hive_record.json) | reference_available · target_version_candidate |
| `stage_tollen_dam` | Tollen Dam | Façade et accès du barrage de Tollen recomposés pour une bande de combat latérale | [PNG](../assets/stages_v11/tollen_dam_gears4_entrance_master.png) · [journal](../data/generation_v11/stage_tollen_dam_record.json) | reference_available · target_version_candidate |
| `stage_new_hope` | New Hope | Gears 5 — New Hope, couloir de recherche abandonné adapté au combat latéral | [PNG](../assets/stages_v10/new_hope_gears5_corridor_master.png) · [journal](../data/generation_v10/stage_new_hope_record.json) | reference_available · target_version_candidate |
| `stage_kadar_lab` | Laboratoire sous le mont Kadar | Chambre à cuve sphérique du niveau Mt Kadar, adaptée en arène latérale | [PNG](../assets/stages_v11/kadar_lab_gears5_containment_chamber_master.png) · [journal](../data/generation_v11/stage_kadar_lab_record.json) | reference_available · target_version_candidate |
| `stage_vasgar_airport` | Aéroport de Vasgar | Terminal de la carte Vasgar, composition latérale issue de deux vues de production finales | [PNG](../assets/stages_v11/vasgar_airport_gears5_terminal_master.png) · [journal](../data/generation_v11/stage_vasgar_airport_record.json) | reference_available · target_version_candidate |
| `stage_new_ephyra` | Rempart de New Ephyra | Gears 5 — Act IV Chapter 2: The Fall | [PNG](../assets/stages_v11/new_ephyra_gears5_final_battlement_master.png) · [journal](../data/generation_v11/stage_new_ephyra_record.json) | reference_available · target_version_candidate |
| `stage_galangi_beach` | Plage de Galangi | Plage de Galangi — rivage endommagé, adaptation latérale de la cinématique | [PNG](../assets/stages_v11/stage_galangi_beach.png) · [journal](../data/generation_v11/stage_galangi_beach_record.json) | reference_available · target_version_candidate |
| `stage_galangi_volcano` | Intérieur volcanique de Galangi | Galangi — coulées de lave et corniche adaptée au combat latéral | [PNG](../assets/stages_v11/stage_galangi_volcano.png) · [journal](../data/generation_v11/stage_galangi_volcano_record.json) | reference_available · target_version_candidate |
| `stage_training_hangar` | Hangar de simulation CGU | Arène originale — hangar d’essai COG; matériaux inspirés de Training Grounds Gears 5 | [PNG](../assets/stages_v11/stage_training_hangar.png) · [journal](../data/generation_v11/stage_training_hangar_record.json) | reference_available · target_version_candidate |
| `stage_training_range` | Terrain de simulation CGU | Arène originale — piste d’essai COG; matériaux inspirés de Training Grounds Gears 5 | [PNG](../assets/stages_v11/stage_training_range.png) · [journal](../data/generation_v11/stage_training_range_record.json) | reference_available · target_version_candidate |
| `stage_gridlock_gow4` | Gridlock | Gears of War 4 — cadrage de combat 2D adapté | [PNG](../assets/stages_v6/gridlock_gow4_master.png) · [journal](../data/generation_v6/gridlock_record.json) | reference_available · target_version_candidate |
| `stage_ritual_g5` | Ritual | Gears 5 — Ritual, cour adaptée au combat latéral | [PNG](../assets/stages_v10/ritual_gears5_courtyard_master.png) · [journal](../data/generation_v10/stage_ritual_g5_record.json) | reference_available · target_version_candidate |
| `stage_tomb_g5` | Tomb | Gears 5 — Tomb, cour adaptée au combat latéral | [PNG](../assets/stages_v10/tomb_gears5_cemetery_master.png) · [journal](../data/generation_v10/stage_tomb_g5_record.json) | reference_available · target_version_candidate |
| `stage_village_g5` | Village | Gears 5 — Operation 8, intérieur cérémoniel adapté au combat 2D | [PNG](../assets/stages_v7/village_gears5_master.png) · [journal](../data/generation_v7/village_record.json) | reference_available · target_version_candidate |
| `stage_dawn_g5` | Dawn | Gears 5 — Operation 8, colonie minière adaptée au combat 2D | [PNG](../assets/stages_v7/dawn_gears5_master.png) · [journal](../data/generation_v7/dawn_record.json) | reference_available · target_version_candidate |
| `stage_river_g5` | River | Gears 5 — River, intérieur de taverne adapté au combat latéral | [PNG](../assets/stages_v9/river_gears5_tavern_master.png) · [journal](../data/generation_v9/stage_river_g5_record.json) | reference_available · target_version_candidate |
| `stage_clocktower_g5` | Clocktower | Gears 5 — Clocktower, terrasse nocturne adaptée au combat latéral | [PNG](../assets/stages_v9/clocktower_gears5_master.png) · [journal](../data/generation_v9/stage_clocktower_g5_record.json) | reference_available · target_version_candidate |
| `stage_nexus_g5` | Nexus | Gears 5 — Operation 5, galerie souterraine adaptée au combat 2D | [PNG](../assets/stages_v8/nexus_gears5_master.png) · [journal](../data/generation_v8/nexus_record.json) | reference_available · target_version_candidate |
| `stage_regency_g5` | Regency | Gears 5 — Operation 5, terrasse cérémonielle adaptée au combat 2D | [PNG](../assets/stages_v8/regency_gears5_master.png) · [journal](../data/generation_v8/regency_record.json) | reference_available · target_version_candidate |
| `stage_ilima_raams_shadow` | Ilima — évacuation de Zeta | Gears of War 3 — RAAM's Shadow | [PNG](../assets/stages_v11/ilima_raams_shadow_evacuation_square_master.png) · [journal](../data/generation_v11/stage_ilima_raams_shadow_record.json) | reference_available · target_version_candidate |

### Projectiles

| Identifiant | Sujet | Édition de la référence ou cible | Fichier | État |
| --- | --- | --- | --- | --- |
| `projectile_frag_grenade_g3` | Grenade Bolo / Frag | Gears of War 3 — projectile isolé, pose fixe | [PNG](../assets/projectiles_v9/frag_grenade_gow3.png) · [journal](../data/generation_v9/projectile_frag_grenade_g3_record.json) | reference_available · target_version_candidate |
| `projectile_buzzkill_sawblade_g4` | Buzzkill — lame circulaire | Gears of War 4 — projectile isolé, pose fixe | [PNG](../assets/projectiles_v9/buzzkill_sawblade_gow4.png) · [journal](../data/generation_v9/projectile_buzzkill_sawblade_g4_record.json) | reference_available · text_reconstruction_candidate |
| `projectile_dropshot_drill_g4` | Dropshot — projectile foreuse | Gears of War 4 — projectile isolé, pose fixe | [PNG](../assets/projectiles_v9/dropshot_drill_gow4.png) · [journal](../data/generation_v9/projectile_dropshot_drill_g4_record.json) | reference_available · text_reconstruction_candidate |
| `projectile_torque_bow_bolt_g3` | Torque Bow — carreau | Gears of War 3 | Absente · [journal](../data/generation_v9/projectile_torque_bow_bolt_g3_record.json) | generation_blocked |
| `projectile_shock_grenade_g4` | Grenade Shock | Gears of War 4 | Absente · [journal](../data/generation_v9/projectile_shock_grenade_g4_record.json) | generation_blocked |
| `projectile_smoke_grenade_g4` | Grenade fumigène | Gears of War 4 — Smoke Grenade, variante C du concept Jarold Sng | [PNG](../assets/projectiles_v10/smoke_grenade_gow4_concept_c.png) · [journal](../data/generation_v10/projectile_smoke_grenade_g4_record.json) | reference_available · concept_art_candidate |
| `projectile_incendiary_grenade_g4` | Grenade incendiaire | Gears of War 4 | Absente · [journal](../data/generation_v10/projectile_incendiary_grenade_g4_record.json) | generation_blocked |
| `projectile_boomshot_shell_g4` | Boomshot — munition | Gears of War 4 | Absente · [journal](../data/generation_v13/projectile_boomshot_shell_g4_record.json) | missing |
| `projectile_canker_g4` | Canker / Carrier Minion — Gears of War 4 | Carrier Minion / Canker — modèle final Gears of War 4 | [PNG](../assets/projectiles_v14/canker_g4.png) · [journal](../data/generation_v14/projectile_canker_g4_record.json) | reference_available · target_version_candidate |

### Donnees detaillees de conception

Les fiches complètes sont conservées dans les données : [roster](../data/roster.json), [179 actions proposées](../data/movesets.json), [routes arcade](../data/arcade_routes.json), [campagne](../data/campaign.json), [boss](../data/bosses.json), [arènes](../data/stages.json) et [plan d'animation](../data/animation_plan.json). Les catalogues de production V6, V7 et V9 étendent ce périmètre sans modifier automatiquement ces fiches jouables.

## Matrice complete des 68 rubriques

Reprise intégrale du contenu de la matrice structurée, sans changement d'état. Les décisions documentaires, preuves et manques ci-dessous ne constituent pas un taux de fonctionnalités implémentées. Source : [GUIDE_REQUIREMENTS_V12.json](../docs/production/GUIDE_REQUIREMENTS_V12.json).

### CG-00 — Utilisation du guide et priorités

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-00 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 00 |
| title | Utilisation du guide et priorités |
| decision | retenue |
| priority | P0 |
| baseline_evidence | docs/core_bible.md §16 |
| documentation_after | docs/combat_extensions.md §1 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Maintenir priorités et états par lot |
| acceptance_criterion | Copies exactes et matrice sans rubrique omise |

### CG-01 — Identité du projet et périmètre

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-01 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 01 |
| title | Identité du projet et périmètre |
| decision | retenue |
| priority | P0 |
| baseline_evidence | docs/core_bible.md §1-2 |
| documentation_after | docs/combat_extensions.md §2 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Réviser le périmètre quand un opus est ajouté |
| acceptance_criterion | Périmètre, périodes et adaptations explicités |

### CG-02 — Fidélité au lore et sources

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-02 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 02 |
| title | Fidélité au lore et sources |
| decision | retenue |
| priority | P0 |
| baseline_evidence | docs/core_bible.md §11 |
| documentation_after | docs/combat_extensions.md §2 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Comparer chaque PNG à des références visuelles précises |
| acceptance_criterion | Identité et détails visuels contrôlés séparément sur captures |

### CG-03 — Roster, personnages, variantes et costumes

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-03 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 03 |
| title | Roster, personnages, variantes et costumes |
| decision | retenue |
| priority | P1 |
| baseline_evidence | data/roster.json; docs/roster_movesets.md |
| documentation_after | docs/combat_extensions.md §2 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | catalogue_existant |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Compléter les entrées visuelles et les fiches des variantes |
| acceptance_criterion | Personnage, variante, costume et palette distincts |

### CG-04 — Fondations du système de combat

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-04 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 04 |
| title | Fondations du système de combat |
| decision | retenue |
| priority | P0 |
| baseline_evidence | prototype/engine.js; docs/core_bible.md §3-4 |
| documentation_after | docs/combat_extensions.md §5 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | prototype_partiel_non_reteste |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Garde directionnelle, hauteurs, annulations et projections à compléter |
| acceptance_criterion | Garde, projections et annulations testées dans une vraie partie |

### CG-05 — Movesets, coups spéciaux et ressources

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-05 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 05 |
| title | Movesets, coups spéciaux et ressources |
| decision | retenue |
| priority | P0 |
| baseline_evidence | data/movesets.json; docs/core_bible.md §5 |
| documentation_after | docs/combat_extensions.md §5 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | prototype_partiel_non_reteste |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Rattacher tous les coups et ressources au moteur |
| acceptance_criterion | Coût, munition et émission appliqués une seule fois |

### CG-06 — Ultimes, finishers et conclusions de combat

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-06 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 06 |
| title | Ultimes, finishers et conclusions de combat |
| decision | retenue |
| priority | P1 |
| baseline_evidence | docs/core_bible.md §6 |
| documentation_after | docs/combat_extensions.md §7 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Produire chorégraphies et variantes de cible |
| acceptance_criterion | Finisher après victoire seulement et cible compatible |

### CG-07 — Présentation et relations entre personnages

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-07 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 07 |
| title | Présentation et relations entre personnages |
| decision | retenue |
| priority | P1 |
| baseline_evidence | docs/roster_movesets.md |
| documentation_after | docs/combat_extensions.md §2-4 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Compléter interactions et dialogues par version |
| acceptance_criterion | Réplique originale identifiée et relation sourcée |

### CG-08 — Histoire individuelle de chaque personnage

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-08 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 08 |
| title | Histoire individuelle de chaque personnage |
| decision | retenue |
| priority | P1 |
| baseline_evidence | data/arcade_routes.json; docs/core_bible.md §7 |
| documentation_after | docs/combat_extensions.md §10 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | catalogue_existant |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Rendre routes jouables et relier leurs bonus |
| acceptance_criterion | Intro, rival, conclusion et reprise d'une route vérifiés |

### CG-09 — Campagne globale distincte

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-09 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 09 |
| title | Campagne globale distincte |
| decision | retenue |
| priority | P1 |
| baseline_evidence | data/campaign.json; docs/core_bible.md §7 |
| documentation_after | docs/combat_extensions.md §2 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | catalogue_existant |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Rendre campagne jouable et vérifier chronologie |
| acceptance_criterion | Disponibilité des alliés et chronologie vérifiées par chapitre |

### CG-10 — Illustrations et cinématiques narratives

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-10 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 10 |
| title | Illustrations et cinématiques narratives |
| decision | retenue |
| priority | P1 |
| baseline_evidence | docs/core_bible.md §7 et §13 |
| documentation_after | docs/combat_extensions.md §7 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Produire storyboards, illustrations et cinématiques |
| acceptance_criterion | Scène abrégée conserve résultat et progression |

### CG-11 — Boss, machines et Boss Rush

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-11 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 11 |
| title | Boss, machines et Boss Rush |
| decision | retenue |
| priority | P1 |
| baseline_evidence | data/bosses.json; prototype/README.md |
| documentation_after | docs/combat_extensions.md §15 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | prototype_partiel_non_reteste |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Étendre les patterns du prototype au catalogue et aux parties destructibles |
| acceptance_criterion | Boss vainquable solo avec annonces, phases et parties cohérentes |

### CG-12 — Modes de jeu

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-12 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 12 |
| title | Modes de jeu |
| decision | adaptee |
| priority | P1 |
| baseline_evidence | docs/core_bible.md §2 et §8 |
| documentation_after | docs/combat_extensions.md §5 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | prototype_partiel_non_reteste |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Implémenter les modes retenus au-delà des trois rencontres actuelles |
| acceptance_criterion | Un bouton seul ne valide aucun mode de jeu |

### CG-13 — Arènes : lieux, composition et lisibilité

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-13 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 13 |
| title | Arènes : lieux, composition et lisibilité |
| decision | retenue |
| priority | P1 |
| baseline_evidence | data/stages.json; docs/core_bible.md §10 |
| documentation_after | docs/combat_extensions.md §15 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | masters_et_specification |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Contrôler topographie et produire calques séparés |
| acceptance_criterion | Sol, échelle, horizon et limites adaptés au profil |

### CG-14 — Arènes vivantes, statiques et événements

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-14 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 14 |
| title | Arènes vivantes, statiques et événements |
| decision | retenue |
| priority | P1 |
| baseline_evidence | docs/core_bible.md §10 |
| documentation_after | docs/combat_extensions.md §15 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Implémenter les quatre axes de règles indépendants |
| acceptance_criterion | Statique, interactions, dangers et transitions indépendants |

### CG-15 — Arènes connectées, transitions et interactions

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-15 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 15 |
| title | Arènes connectées, transitions et interactions |
| decision | adaptee |
| priority | P1 |
| baseline_evidence | docs/boss_stages_story.md |
| documentation_after | docs/combat_extensions.md §15 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Créer le graphe de zones et prouver chaque passage |
| acceptance_criterion | Destination réelle, installée et arrivée jouable |

### CG-16 — Ennemis, soutiens, véhicules et projectiles

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-16 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 16 |
| title | Ennemis, soutiens, véhicules et projectiles |
| decision | retenue |
| priority | P1 |
| baseline_evidence | data/bosses.json; docs/core_bible.md §9 |
| documentation_after | docs/combat_extensions.md §9-10 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | catalogue_existant |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Rattacher les ennemis et projectiles à leur période et moteur |
| acceptance_criterion | Source et propriétaire des projectiles distincts du rendu |

### CG-17 — Direction artistique et production des assets

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-17 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 17 |
| title | Direction artistique et production des assets |
| decision | retenue |
| priority | P0 |
| baseline_evidence | docs/core_bible.md §11; docs/production/PIPELINE_ASSETS.md |
| documentation_after | docs/combat_extensions.md §2 et 16 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | outillage_production_existant |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Poursuivre PNG fixes manquants et QA |
| acceptance_criterion | Un sujet par source, alpha et asymétries contrôlés |

### CG-18 — Animations, VFX, son et caméra

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-18 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 18 |
| title | Animations, VFX, son et caméra |
| decision | retenue |
| priority | P1 |
| baseline_evidence | docs/core_bible.md §12-13 |
| documentation_after | docs/combat_extensions.md §3-4 et 16 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Animations, VFX et sons à produire dans leurs phases respectives |
| acceptance_criterion | Transformation d'un PNG ne compte pas comme animation dessinée |

### CG-19 — Interface et expérience utilisateur

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-19 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 19 |
| title | Interface et expérience utilisateur |
| decision | retenue |
| priority | P0 |
| baseline_evidence | prototype/app.js; docs/core_bible.md §14 |
| documentation_after | docs/combat_extensions.md §4 et 12 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | prototype_partiel_non_reteste |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Sélection complète et motifs d’accès à intégrer |
| acceptance_criterion | Navigation accessible sans impasse ni motif de refus erroné |

### CG-20 — Tutoriels, entraînement et apprentissage

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-20 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 20 |
| title | Tutoriels, entraînement et apprentissage |
| decision | retenue |
| priority | P0 |
| baseline_evidence | docs/core_bible.md §14 |
| documentation_after | docs/combat_extensions.md §10 et 17 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Tutoriels des systèmes effectivement intégrés à construire |
| acceptance_criterion | Épreuve enseigne une mécanique réelle et propose reprise |

### CG-21 — IA et difficulté

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-21 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 21 |
| title | IA et difficulté |
| decision | retenue |
| priority | P0 |
| baseline_evidence | prototype/engine.js; docs/core_bible.md §7 |
| documentation_after | docs/combat_extensions.md §17 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | prototype_partiel_non_reteste |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Étendre IA avec temps de réaction documenté |
| acceptance_criterion | Difficulté et délai de réaction explicités par profil |

### CG-22 — Équilibrage et accessibilité

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-22 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 22 |
| title | Équilibrage et accessibilité |
| decision | retenue |
| priority | P0 |
| baseline_evidence | docs/core_bible.md §14 |
| documentation_after | docs/combat_extensions.md §8 et 17 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Tester confort et lisibilité dans les profils de jeu |
| acceptance_criterion | Couleur et martèlement ne sont jamais seuls moyens |

### CG-23 — Multijoueur, réseau et replays

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-23 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 23 |
| title | Multijoueur, réseau et replays |
| decision | differee |
| priority | P0 |
| baseline_evidence | docs/core_bible.md §15 |
| documentation_after | docs/combat_extensions.md §6 et 15 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Définir protocole réseau et rejouer des sessions déterministes |
| acceptance_criterion | Mêmes entrées rejouées produisent mêmes états et transactions |

### CG-24 — Progression, sauvegardes et rejouabilité

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-24 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 24 |
| title | Progression, sauvegardes et rejouabilité |
| decision | retenue |
| priority | P1 |
| baseline_evidence | docs/core_bible.md §15 |
| documentation_after | docs/combat_extensions.md §11-14 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Sauvegarde, migrations et acquisitions à implémenter |
| acceptance_criterion | Interruption ne perd ni ne double une récompense |

### CG-25 — Organisation, inventaires et statistiques

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-25 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 25 |
| title | Organisation, inventaires et statistiques |
| decision | retenue |
| priority | P0 |
| baseline_evidence | src/consolidate_inventory.py; docs/production/REPRISE_V11.md |
| documentation_after | docs/combat_extensions.md §16 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | outillage_production_existant |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Actualiser les compteurs depuis fichiers et validations réelles |
| acceptance_criterion | Conçu, produit, intégré, testé et acquis restent distincts |

### CG-26 — Critères de validation et ordre de production

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-26 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 26 |
| title | Critères de validation et ordre de production |
| decision | retenue |
| priority | P0 |
| baseline_evidence | docs/core_bible.md §16; prototype/tests.cjs |
| documentation_after | docs/combat_extensions.md §17 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | plan_de_test_non_execute |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Exécuter les critères à chaque future intégration |
| acceptance_criterion | Journal indique exactement les tests exécutés et leurs résultats |

### CG-27 — Fiches types à remplir

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-27 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 27 |
| title | Fiches types à remplir |
| decision | retenue |
| priority | P0 |
| baseline_evidence | docs/roster_movesets.md; docs/boss_stages_story.md |
| documentation_after | docs/combat_extensions.md §16 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | modeles_sources_copies |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Remplir les dix modèles généraux au niveau des contenus |
| acceptance_criterion | Dix fiches générales remplies pour les contenus nouveaux |

### CG-28 — Instruction prête à transmettre à un projet

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-28 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 28 |
| title | Instruction prête à transmettre à un projet |
| decision | retenue |
| priority | P0 |
| baseline_evidence | docs/core_bible.md |
| documentation_after | docs/combat_extensions.md §1 et 17 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Rattacher futurs lots aux décisions et écarts |
| acceptance_criterion | Décisions et écarts rattachés à la passe sans perte de périmètre |

### CG-29 — Références vérifiées et vocabulaire

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-29 |
| source_document | Combat_Games_Guide_General_v1.0.txt |
| source_sha256 | 4844584616072ac0d52d37c2fab4365e1ec489240f17a721ee216e223b0355b7 |
| source_section | 29 |
| title | Références vérifiées et vocabulaire |
| decision | retenue |
| priority | P0 |
| baseline_evidence | docs/references/; docs/core_bible.md Sources |
| documentation_after | docs/combat_extensions.md §18 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Ajouter références visuelles de détails |
| acceptance_criterion | Faits sourcés séparés des paramètres de gameplay |

### CG-30 — PORTÉE ET RATTACHEMENT AU GUIDE GÉNÉRAL

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-30 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 30 |
| title | PORTÉE ET RATTACHEMENT AU GUIDE GÉNÉRAL |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Original absent au commit de référence |
| documentation_after | docs/combat_extensions.md §1 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Étendre selon les modes et priorités retenus |
| acceptance_criterion | Extension reliée à la bible et aux identifiants existants |

### CG-31 — Taunts : provocations et réactions de personnalité

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-31 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 31 |
| title | Taunts : provocations et réactions de personnalité |
| decision | retenue |
| priority | P1 |
| baseline_evidence | docs/core_bible.md §12 mentionne la provocation |
| documentation_after | docs/combat_extensions.md §3 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Produire et intégrer taunts par version |
| acceptance_criterion | Interruption et récupération sans ressource gratuite |

### CG-32 — Animations de sélection, confirmation et désélection

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-32 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 32 |
| title | Animations de sélection, confirmation et désélection |
| decision | retenue |
| priority | P1 |
| baseline_evidence | docs/core_bible.md §14 décrit la sélection |
| documentation_after | docs/combat_extensions.md §4 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Produire clips de sélection, confirmation et désélection |
| acceptance_criterion | Navigation rapide ne laisse aucun son ou effet ancien |

### CG-33 — Profils d'équipe et catégories de partenaires

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-33 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 33 |
| title | Profils d'équipe et catégories de partenaires |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Aucun profil tag dans les modes du prototype |
| documentation_after | docs/combat_extensions.md §5 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Implémenter actif/réserve et conditions de défaite |
| acceptance_criterion | Deux membres valides sans doublon ni rôle contradictoire |

### CG-34 — Commandes, jauges et disponibilité

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-34 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 34 |
| title | Commandes, jauges et disponibilité |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Commandes du duel seulement dans le prototype |
| documentation_after | docs/combat_extensions.md §5 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Ajouter commandes et transaction atomique des coûts |
| acceptance_criterion | Deux actions simultanées ne dépensent pas la même ressource |

### CG-35 — Assistances ponctuelles

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-35 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 35 |
| title | Assistances ponctuelles |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Aucune assistance de roster dans le prototype |
| documentation_after | docs/combat_extensions.md §6 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Arrivée, action, sortie, récupération et vulnérabilité à implémenter |
| acceptance_criterion | Soutien touché ou KO ne reste pas rappelable |

### CG-36 — Tag : changement réel de combattant

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-36 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 36 |
| title | Tag : changement réel de combattant |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Aucun transfert actif/réserve dans le prototype |
| documentation_after | docs/combat_extensions.md §6 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Transfert de contrôle et conservation de l’état à implémenter |
| acceptance_criterion | Relais réel sans réinitialiser ressources et combo ; relais KO gratuit |

### CG-37 — Techniques combinées et supers d'équipe

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-37 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 37 |
| title | Techniques combinées et supers d'équipe |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Supers solo spécifiées dans la bible |
| documentation_after | docs/combat_extensions.md §7 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Storyboards duo, confirmations et sorties à produire |
| acceptance_criterion | Garde ou échec n'engage pas une longue capture de cible |

### CG-38 — Finishers d'équipe et fins dramatiques conditionnelles

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-38 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 38 |
| title | Finishers d'équipe et fins dramatiques conditionnelles |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Exécutions solo spécifiées dans la bible |
| documentation_after | docs/combat_extensions.md §7 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Conditions et remplacements des fins à implémenter |
| acceptance_criterion | Partenaire KO, époque ou stage incorrect utilisent un remplacement |

### CG-39 — Clashes et confrontations avec QTE

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-39 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 39 |
| title | Clashes et confrontations avec QTE |
| decision | adaptee |
| priority | P1 |
| baseline_evidence | Aucun clash/QTE dans le prototype |
| documentation_after | docs/combat_extensions.md §8 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Table de clashes et résolution accessible à implémenter |
| acceptance_criterion | Égalité, silence, accessibilité et projectile tiers résolus |

### CG-40 — Movesets à entités indépendantes et objets placés

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-40 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 40 |
| title | Movesets à entités indépendantes et objets placés |
| decision | adaptee |
| priority | P1 |
| baseline_evidence | Entités de projectile simples dans le prototype |
| documentation_after | docs/combat_extensions.md §9 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Kits d’entités autorisés à documenter puis produire |
| acceptance_criterion | Propriétaire, budget et retrait définis ; JACK jamais dupliqué |

### CG-41 — Projectiles persistants et règles communes aux entités

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-41 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 41 |
| title | Projectiles persistants et règles communes aux entités |
| decision | adaptee |
| priority | P1 |
| baseline_evidence | Tirs simples du moteur existant |
| documentation_after | docs/combat_extensions.md §9 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Registres d’impacts, objets armés et transferts à implémenter |
| acceptance_criterion | Projectile ne frappe pas deux fois après transfert ou retrait |

### CG-42 — Stages bonus et épreuves intégrées aux histoires

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-42 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 42 |
| title | Stages bonus et épreuves intégrées aux histoires |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Défis évoqués dans la bible |
| documentation_after | docs/combat_extensions.md §10 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Huit familles conçues à convertir en épreuves jouables |
| acceptance_criterion | Réussite, échec, score, reprise et récompense vérifiés |

### CG-43 — Espace d'exploration et de déblocage inspiré de la Krypt

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-43 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 43 |
| title | Espace d'exploration et de déblocage inspiré de la Krypt |
| decision | adaptee |
| priority | P1 |
| baseline_evidence | Galerie existante hors espace exploratoire |
| documentation_after | docs/combat_extensions.md §11 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Carte Archives puis parcours connecté à produire |
| acceptance_criterion | Graphe d'Archives sans porte illogique ni prérequis circulaire |

### CG-44 — Cohérence narrative, relations et compatibilités

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-44 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 44 |
| title | Cohérence narrative, relations et compatibilités |
| decision | retenue |
| priority | P0 |
| baseline_evidence | Périodes et sources présentes dans le catalogue |
| documentation_after | docs/combat_extensions.md §2 et 7 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Compléter les paires par scènes, versions et périodes précises |
| acceptance_criterion | Faction commune ne suffit pas à justifier un duo narratif |

### CG-45 — Assets, animations, sons et mise en scène

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-45 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 45 |
| title | Assets, animations, sons et mise en scène |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Budgets d'animation du guide de base |
| documentation_after | docs/combat_extensions.md §16 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | modeles_sources_copies |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Renseigner assets et clips sans les déclarer produits |
| acceptance_criterion | Chaque asset a sujet, version, statut et référence |

### CG-46 — Interface, apprentissage, accessibilité et réseau

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-46 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 46 |
| title | Interface, apprentissage, accessibilité et réseau |
| decision | retenue |
| priority | P0 |
| baseline_evidence | UI et commandes du prototype |
| documentation_after | docs/combat_extensions.md §4-6 et 8 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Tutoriel, confort et réseau des actions d’équipe à implémenter |
| acceptance_criterion | Refus explicite, remappage et résultat de simulation partagé |

### CG-47 — Validation, statistiques et ordre d'intégration

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-47 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 47 |
| title | Validation, statistiques et ordre d'intégration |
| decision | retenue |
| priority | P0 |
| baseline_evidence | Tests du duel et inventaire existants |
| documentation_after | docs/combat_extensions.md §17 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | plan_de_test_non_execute |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | 18 scénarios à exécuter au fil des intégrations |
| acceptance_criterion | 18 scénarios de l'extension exécutés et prouvés avant validation |

### CG-48 — Dix fiches de production complémentaires

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-48 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 48 |
| title | Dix fiches de production complémentaires |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Aucune série équivalente complète au dépôt initial |
| documentation_after | docs/combat_extensions.md §16 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | modeles_sources_copies |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Dix modèles copiés à remplir par sujet, paire ou bonus |
| acceptance_criterion | Dix modèles remplis pour chaque sujet ou paire prioritaire |

### CG-49 — Instruction d'intégration et références

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-49 |
| source_document | Combat_Games_Extension_01_Tag_Taunts_Bonus_v1.0.txt |
| source_sha256 | 330fb7485a7a52b2a20f855646c940aaac0fcd9510032bc84b2e17c518edd25f |
| source_section | 49 |
| title | Instruction d'intégration et références |
| decision | retenue |
| priority | P0 |
| baseline_evidence | Original absent au commit de référence |
| documentation_after | docs/combat_extensions.md §1 et 18 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Conserver bilan et sources à chaque lot |
| acceptance_criterion | Sources officielles séparées des nouvelles chorégraphies |

### CG-50 — PORTÉE, PRINCIPES ET RACCORDEMENT AUX GUIDES

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-50 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 50 |
| title | PORTÉE, PRINCIPES ET RACCORDEMENT AUX GUIDES |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Aucun module complet de droits au dépôt initial |
| documentation_after | docs/combat_extensions.md §12 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Appliquer catégories retenues et documenter exclusions |
| acceptance_criterion | Verrou d'accès distinct d'un asset inachevé |

### CG-51 — États de découverte, de droit et de disponibilité

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-51 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 51 |
| title | États de découverte, de droit et de disponibilité |
| decision | retenue |
| priority | P0 |
| baseline_evidence | Pas de modèle d'accès à quatre dimensions |
| documentation_after | docs/combat_extensions.md §12 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Construire modèle multidimensionnel et messages de refus |
| acceptance_criterion | Découverte, droit, installation et compatibilité séparés |

### CG-52 — Langage visuel adapté au lore

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-52 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 52 |
| title | Langage visuel adapté au lore |
| decision | adaptee |
| priority | P1 |
| baseline_evidence | Palette UI militaire, sans système complet |
| documentation_after | docs/combat_extensions.md §12 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Produire cadres, silhouettes, badges et variantes accessibles |
| acceptance_criterion | Dossier et silhouette accessibles ; secret réel masqué |

### CG-53 — Emplacements de personnages et partenaires

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-53 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 53 |
| title | Emplacements de personnages et partenaires |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Catalogue roster, pas de grille jouable complète |
| documentation_after | docs/combat_extensions.md §4 et 12 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Construire grille et conditions de composition |
| acceptance_criterion | Case verrouillée consultable sans confirmation possible |

### CG-54 — Costumes, palettes et accessoires

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-54 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 54 |
| title | Costumes, palettes et accessoires |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Catalogue costumes existant |
| documentation_after | docs/combat_extensions.md §12-14 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Séparer dépendances et préférences du droit |
| acceptance_criterion | Costume acquis avant personnage et préférences conservés |

### CG-55 — Stages, variantes et destinations

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-55 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 55 |
| title | Stages, variantes et destinations |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Catalogue stages et masters existants |
| documentation_after | docs/combat_extensions.md §12 et 15 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Distribution des stages et contrôle de disponibilité à construire |
| acceptance_criterion | Sélection, participation, installation et transition compatibles |

### CG-56 — Modes de jeu et parcours verrouillés

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-56 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 56 |
| title | Modes de jeu et parcours verrouillés |
| decision | adaptee |
| priority | P1 |
| baseline_evidence | Trois rencontres ouvertes dans le prototype |
| documentation_after | docs/combat_extensions.md §12 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Verrouiller uniquement les modes retenus avec alternatives |
| acceptance_criterion | Tutoriel, réglages et entraînement de base restent accessibles |

### CG-57 — Conditions de déblocage et progression

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-57 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 57 |
| title | Conditions de déblocage et progression |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Récompenses proposées dans les routes |
| documentation_after | docs/combat_extensions.md §13 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Évaluer conditions et événements autoritaires |
| acceptance_criterion | ET/OU explicites et sources d'accès indépendantes |

### CG-58 — Exploration, récompenses et scène de révélation

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-58 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 58 |
| title | Exploration, récompenses et scène de révélation |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Galerie sans attribution exploratoire |
| documentation_after | docs/combat_extensions.md §11 et 13 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Transaction avant révélation et reprise après interruption |
| acceptance_criterion | Interruption de révélation ne double ni ne perd le contenu |

### CG-59 — Contenus dédiés aux abonnés et modèles d'acquisition

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-59 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 59 |
| title | Contenus dédiés aux abonnés et modèles d'acquisition |
| decision | a_decider_avant_activation |
| priority | P2 |
| baseline_evidence | Aucune offre opérationnelle constatée |
| documentation_after | docs/combat_extensions.md §14 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | conception_optionnelle_non_active |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Choisir contenus et modèle d’acquisition avant toute activation |
| acceptance_criterion | Permanence, dépendances et durée annoncées avant engagement |

### CG-60 — Liaison avec Patreon ou un service équivalent

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-60 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 60 |
| title | Liaison avec Patreon ou un service équivalent |
| decision | differee |
| priority | P2 |
| baseline_evidence | Aucun adaptateur Patreon dans le prototype |
| documentation_after | docs/combat_extensions.md §14 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Vérifier fournisseur puis implémenter service de confiance |
| acceptance_criterion | Client local ne peut se déclarer abonné |

### CG-61 — Expiration, changements d'accès et fonctionnement hors ligne

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-61 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 61 |
| title | Expiration, changements d'accès et fonctionnement hors ligne |
| decision | retenue |
| priority | P0 |
| baseline_evidence | Aucune gestion de droits externes dans le prototype |
| documentation_after | docs/combat_extensions.md §14 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Définir politique hors ligne et retrait par source |
| acceptance_criterion | Expiration conserve source permanente et partie en cours |

### CG-62 — Sélection locale, multijoueur, entraînement et replays

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-62 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 62 |
| title | Sélection locale, multijoueur, entraînement et replays |
| decision | retenue |
| priority | P0 |
| baseline_evidence | Réseau et roster complet non livrés par prototype |
| documentation_after | docs/combat_extensions.md §12-15 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Éprouver sélection, participation, entraînement et replays |
| acceptance_criterion | Droit de choisir un stage distinct du droit d'y participer |

### CG-63 — Interface, textes, accessibilité et protection des surprises

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-63 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 63 |
| title | Interface, textes, accessibilité et protection des surprises |
| decision | retenue |
| priority | P0 |
| baseline_evidence | Options de confort partiellement définies |
| documentation_after | docs/combat_extensions.md §4 et 12 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | specifie_non_implemente |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Produire textes accessibles et contrôle des spoilers |
| acceptance_criterion | Nom, voix, texte accessible et image ne révèlent pas un secret |

### CG-64 — Production, sauvegarde et critères de validation

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-64 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 64 |
| title | Production, sauvegarde et critères de validation |
| decision | retenue |
| priority | P0 |
| baseline_evidence | Suivi d'assets sans journal de droits |
| documentation_after | docs/combat_extensions.md §13 et 17 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | plan_de_test_non_execute |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Exécuter les 22 cas avec sauvegardes et restauration |
| acceptance_criterion | 22 scénarios d'accès, migrations et sources multiples vérifiés |

### CG-65 — Six fiches de production à remplir

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-65 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 65 |
| title | Six fiches de production à remplir |
| decision | retenue |
| priority | P1 |
| baseline_evidence | Pas de fiches équivalentes complètes initialement |
| documentation_after | docs/combat_extensions.md §16 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | modeles_sources_copies |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Remplir six fiches par contenu, règle et offre retenue |
| acceptance_criterion | Six modèles remplis avec statut slot séparé de celui du contenu |

### CG-66 — Instruction prête à transmettre à un projet

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-66 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 66 |
| title | Instruction prête à transmettre à un projet |
| decision | retenue |
| priority | P0 |
| baseline_evidence | Original absent au commit de référence |
| documentation_after | docs/combat_extensions.md §1 et 17 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Maintenir distinction documenté/produit/intégré/testé |
| acceptance_criterion | Aucun service seulement conçu annoncé opérationnel |

### CG-67 — Références vérifiées et vocabulaire

| Champ source | Valeur |
| --- | --- |
| requirement_id | CG-67 |
| source_document | Combat_Games_Extension_02_Slots_Verrouilles_Deblocages_Abonnes_v1.0.txt |
| source_sha256 | 08b57ea542e83c487fef3276997a612d4657f2ee9ed4f8e46b0bf65a2778038b |
| source_section | 67 |
| title | Références vérifiées et vocabulaire |
| decision | retenue |
| priority | P0 |
| baseline_evidence | Références lore, pas celles du module d'accès |
| documentation_after | docs/combat_extensions.md §14 et 18 |
| documentation_status | source_integrated_and_project_mapping_present |
| runtime_status | rattachement_documentaire |
| runtime_test_status | not_run_by_guide_integration_v12 |
| remaining_work | Revérifier documentation fournisseur avant implémentation |
| acceptance_criterion | Modèles du jeu séparés des garanties du fournisseur |

## Audit et cas dacceptation des extensions

Source complète : [GUIDE_INTEGRATION_V12.md](../docs/production/GUIDE_INTEGRATION_V12.md).

### Audit d'intégration du guide de combat — V12

Date : **27 novembre 2026**. Projet : **Gears of War Combats**. Périmètre : guide général et deux extensions demandées, leur rattachement à la bible et leurs écarts de production.

#### Résultat

Les **trois originaux v1.0 sont intégrés sans modification**, avec leur provenance et leurs empreintes. Un [chapitre d'adaptation à Gears](../docs/combat_extensions.md) les relie aux personnages, aux périodes et aux règles déjà définies. La [bible principale](../docs/core_bible.md) renvoie à ce chapitre et rappelle la priorité actuelle aux assets fixes.

Cette passe intègre de la documentation et un suivi d'exigences. Elle n'ajoute au prototype ni animation dessinée, ni tag, ni système d'abonnement. Les limites sont explicites dans chaque document et dans la matrice.

#### Point de départ vérifié

Référence contrôlée : commit `370e49593ee6690076b4051afc7357d1e1707aad`, branche `codex/gears-static-assets-v9-20261125` de `darknigthmare/gear-of-wars-combats`.

L'arbre Git de cette révision ne contient aucun des trois fichiers originaux. Le contrôle compare également le SHA-1 Git du contenu de chaque original à tous les blobs suivis : aucune copie identique sous un autre nom n'est retrouvée. Cela prouve l'absence des copies exactes à cette révision ; cela ne signifie pas que tous leurs concepts étaient absents.

La bible existante décrivait déjà la provocation, la sélection, des récompenses, les récits, les boss, les armes et des budgets d'animation. `prototype/README.md`, `prototype/engine.js` et `prototype/app.js` exposent trois rencontres : duel Marcus/RAAM, Berserker et King Raven de simulation. Le moteur inspecté ne contient pas de profil d'équipe actif/réserve ni de gestion de droits Patreon. Les tests historiques du prototype ne sont pas présentés comme des tests des nouvelles extensions.

#### Sources récupérées et contrôle des copies

| Source | Version déclarée | Octets | Copie exacte |
| --- | --- | ---: | --- |
| Guide général | 1.0 — 25/11/2026 | 55 172 | Oui |
| Extension 01 | 1.0 — 26/11/2026 | 60 589 | Oui |
| Extension 02 | 1.0 — 27/11/2026 | 47 334 | Oui |

Les fichiers sont retrouvés sur Drive le 27 novembre 2026. Le [manifeste des sources](../docs/guides/combat/source_manifest.json) conserve noms, URL, identifiants de source, dates de dépôt, SHA-256, SHA-1 Git et résultat de comparaison à la révision initiale. La version imprimée dans le document est préservée, même lorsque son horodatage de dépôt UTC correspond à la veille.

Les copies sont accessibles depuis le [dossier des guides](../docs/guides/combat/README.md). Aucune adaptation, traduction ou correction n'est insérée dans ces originaux ; les décisions spécifiques au projet restent dans le chapitre V12.

#### Couverture documentaire

| Ensemble | Rubriques tracées | Traitement |
| --- | ---: | --- |
| Guide général | 30 : 00–29 | Raccord à la bible et aux inventaires existants ; écarts conservés |
| Extension 01 | 20 : 30–49 | Contrats d'équipe, présentation, clashes, entités, bonus et exploration |
| Extension 02 | 18 : 50–67 | Modèle d'accès, présentation des verrous, acquisitions et validation |
| **Total** | **68** | Aucune rubrique de sommaire omise |

Ce total est un nombre de **rubriques sources suivies**. Il n'est ni le nombre de fonctionnalités jouables, ni une liste atomique exhaustive de tous les tests, ni un taux d'avancement global du jeu.

La matrice comprend 57 rubriques retenues, 8 adaptées, 2 différées et 1 soumise au choix d'offre avant activation. « Différée » conserve une exigence et son critère ; cela ne la supprime pas. Le réseau reste une décision d'architecture à préparer tôt, même si la livraison vient plus tard. L'adaptateur d'abonnement et la définition de l'offre restent hors fonctionnement actuel.

- [Matrice CSV](../docs/production/GUIDE_REQUIREMENTS_V12.csv) : identifiant, source, section, décision, priorité, preuve initiale, documentation après intégration, état runtime, manque et critère d'acceptation.
- [Même matrice en JSON](../docs/production/GUIDE_REQUIREMENTS_V12.json) : version du schéma, périmètre et 68 entrées identiques.

#### Adaptations propres à Gears

Les associations prioritaires s'appuient sur des sources officielles citées dans le chapitre : Marcus/Dom, Delta, Kilo, les héros de Tactics, le groupe de Gears 4 et Scorpio. Les noms de supers, règles de tag, valeurs de jauge, bonus et Archives sont des créations du projet. Les sources des personnages ne leur confèrent pas un statut canonique.

Les règles empêchent de confondre la variante Gears 3 de Baird/Cole avec leurs versions Judgment, les versions du groupe de Gears 4 avec celles de Gears 5, JACK Gears 5 avec JACK Tactics, ou une équipe libre avec un événement de campagne. Chaque duo narratif réclame un contrôle de scène et de disponibilité.

Le chapitre couvre aussi les points qui dépassaient le résumé initial de la demande : clashes et QTE accessibles, objets posés, propriétaires des projectiles persistants, parties de boss, transitions de zones, destination non installée, réserve KO, conservation des compteurs de combo et fins dramatiques incompatibles.

Les verrous distinguent découverte, droits, installation et compatibilité. Un asset manquant reste un manque de production. Une acquisition permanente et un droit temporaire restent deux sources séparées. L'Archives de campagne est un espace d'interface original compatible, sans ajout d'un lieu officiel au lore.

#### Travail restant visible

Les 10 modèles de production de l'Extension 01 et les 6 de l'Extension 02 sont intégralement préservés dans les sources. Le chapitre définit les contrats et premières familles ; les fiches détaillées de chaque personnage, paire, scène, bonus ou récompense restent à remplir à mesure de leur production. Un modèle copié n'est pas déclaré fiche terminée.

Les 18 scénarios d'acceptation de l'Extension 01 et les 22 de l'Extension 02 restent à exécuter dans leurs futurs systèmes. Les résumés du chapitre n'effacent aucun scénario des originaux. Ce sous-lot n'exécute pas de tests runtime des extensions, puisqu'il ne les implémente pas.

La phase actuelle privilégie toujours **les personnages/costumes fixes manquants, ennemis, machines, projectiles et stages**. Les animations de taunt, sélection, tag, supers et déblocage sont planifiées ; aucun PNG fixe n'est compté comme une animation. Les layers de parallaxe, poses alternatives, clips et contrôle canon détaillé restent suivis séparément.

#### Vérification documentaire réalisée

- Les tailles et SHA-256 des trois copies correspondent aux fichiers téléchargés.
- Les trois contenus complets sont absents de l'arbre de la révision initiale, y compris sous un autre nom.
- Les sections 00 à 67 apparaissent une seule fois dans la matrice ; CSV et JSON partagent les mêmes 68 identifiants.
- Les chemins documentaires relatifs ajoutés pointent vers les fichiers prévus.
- Les nouveaux documents gardent les statuts de conception et de fonctionnement séparés.

Le contrôle ci-dessus confirme l'intégration documentaire. La qualité visuelle 1:1, l'équilibrage, le réseau et l'accès externe demandent leurs validations propres ; aucune de ces validations n'est déduite de la présence de ce rapport.

#### Traçabilité des 40 cas d’acceptation sources

Cette table reprend les **40 cas sources complets** (18 de l’Extension 01, section 47 ; 22 de l’Extension 02, section 64). Les identifiants `E01-01` à `E01-18` et `E02-01` à `E02-22` appartiennent au suivi de validation ; ils ne remplacent pas les rubriques `CG-00` à `CG-67`.

**État de chaque ligne : `non_execute` dans l’intégration documentaire V12.** Le rattachement indique où les règles et attentes sont conçues, pas où un test a réussi. Les sections citées renvoient au [chapitre d’adaptation](../docs/combat_extensions.md).

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

## Annexe historique du premier lot

Source complète : [delivery_status.md](../docs/delivery_status.md).

**Archive du 19 novembre 2026.** Les chiffres, tests rapportés et étapes futures de cette annexe sont ceux du premier lot ; voir l'état courant en tête de cette édition pour la production actuelle.

> **Instantané historique du premier lot (19 novembre 2026).** Pour le corpus récupéré et les nouvelles images, consulter [l’état consolidé du 20 novembre](../docs/production/CONSOLIDATION_2026-11-20.md).

### État du premier lot

#### Contenu de conception livré

La version 1 contient 36 fiches de combattants, 75 entrées de costume ou d'époque, 179 actions, 36 routes arcade et 24 propositions de combos pour les douze combattants du noyau. Les 179 actions se répartissent en 11 actions communes, 96 actions du noyau et 72 signatures des combattants d'extension. Les exécutions du noyau sont incluses dans ce décompte ; toutes les entrées ne sont donc pas des attaques utilisables pendant une manche.

Le catalogue Boss Battle comprend 24 rencontres et 72 phases décrites. Les 24 stages possèdent chacun six couches spécifiées, soit 144 calques à produire. La campagne présente 12 chapitres avec introduction, confrontation et conclusion. Les sources accompagnent les fiches et les propositions de gameplay sont identifiées comme des adaptations.

Les fichiers de données passent un contrôle des identifiants, des références entre roster, routes, boss, stages et chapitres, des valeurs de base et du budget d'animation. Ce contrôle ne certifie ni l'équilibrage en partie ni la fidélité visuelle.

#### Prototype livré

Trois rencontres sont jouables : un duel de Marcus contre RAAM, une Berserker et une simulation contre un King Raven. Le joueur dispose du déplacement, de deux attaques de corps à corps, du tir, de la garde, de l'esquive, du rechargement actif et d'un spécial. Les boss ont trois phases, des attaques annoncées et des fenêtres de vulnérabilité. Le décor Ephyra est intégré comme master complet.

Le prototype utilise une manche par duel et une jauge spéciale unique. La campagne, les tournois, le roster complet, les exécutions, les animations dessinées image par image et le réseau restent des contenus spécifiés pour les étapes suivantes. Les personnages non illustrés gardent une représentation provisoire. Marcus utilise sa pose neutre détourée, animée par transformations de présentation ; elle ne constitue pas une animation dessinée image par image.

Le rechargement et la posture correspondent au profil décrit dans la bible. Le prototype n'implémente pas encore le verrouillage intermédiaire du chargeur, les projections, les annulations, les hauteurs d'attaque, la garde parfaite et l'endurance. Son compteur mesure des impacts rapprochés et ne garantit pas un combo sans échappatoire.

Quinze tests de logique ont été exécutés avec succès. Les contrôles portent notamment sur la garde, les bornes inclusives de recharge, le bonus limité, les vulnérabilités, les phases, les résultats, la pause et la séparation du hasard visuel. Le rendu du canvas des trois modes a été produit et inspecté. Les scripts et un appui tactile bref ont aussi été exercés dans un environnement JS. Le HUD HTML et CSS, le responsive dans un navigateur et la compatibilité avec une manette physique restent à vérifier, car l'ouverture du navigateur de test est bloquée dans cet environnement.

#### Images produites et état artistique

Quatre compositions initiales ont été générées : Marcus Fenix en pose neutre, Kait Diaz en tenue hivernale en pose neutre, un décor d'Ephyra et un décor du Hollow. Les deux exports détourés sont également livrés et recensés dans le manifeste, soit six fichiers d'image. Ces dérivés des références de personnage ne comptent pas comme de nouvelles poses.

Les demandes initiales de sprites de combat pour Marcus, RAAM et la Berserker ont été refusées par le système d'image. Aucun résultat correspondant n'est déclaré livré. Les références neutres produites ensuite et les décors ont leur statut propre. Les détails de costume, les visages, les armes et les proportions devront être confrontés à des captures précises avant une validation de fidélité 1 pour 1.

Les décors sont des compositions inspirées des univers des épisodes indiqués. Ils ne reproduisent pas encore un emplacement photographié sous un angle exact et ne sont pas séparés en calques. Le suivi de production conserve les 144 couches à produire, sans les déclarer terminées à partir de deux images complètes.

#### Prochain lot de production

Le lot suivant doit valider les références de Marcus et RAAM, puis dessiner leurs attentes, déplacements, gardes, impacts et premiers coups. La Berserker nécessite une silhouette de référence, une anticipation de charge, une charge, une collision et une récupération. Le King Raven nécessite le modèle exact de l'épisode choisi, ses moteurs et ses armes séparés. Les six couches du stage Ephyra doivent être préparées à la même origine et avec les zones masquées reconstruites.

Les animations individuelles, les parties de boss, les calques et les illustrations de fin représentent 240 entrées de suivi regroupées. Une entrée d'animation est un ensemble de clips, pas un seul dessin. Le budget indicatif complet représente 552 dessins par orientation pour un costume entièrement dessiné ; les reprises et réutilisations réellement possibles seront décidées après validation de chaque personnage.

Le classeur fournit des champs de contrôle artistique, technique et d'intégration. Une référence produite ne devient prête pour le jeu qu'après satisfaction de ces contrôles. Les choix de gameplay et les fichiers sources du prototype sont inclus pour que la suite puisse commencer à partir de cette version.

## Reconstruction de cette edition

Commande : `python src/build_bible_markdown.py`, après `python src/consolidate_inventory.py --report-suffix V14`. Le [manifeste de construction](../docs/production/BIBLE_BUILD_V14.json) enregistre les sources et leurs SHA-256. Aucun texte original de guide ni PDF/DOCX historique n'est réécrit par ce script.
