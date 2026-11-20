# Personnages armes et routes de combat

## Périmètre des fiches

Le catalogue définit 36 combattants, répartis en un noyau de 12 et une extension de 24, ainsi que 75 variantes de costume à documenter. Il contient 179 fiches d’action et 36 parcours arcade. Ce nombre mesure la conception écrite. Il ne mesure ni les sprites terminés ni les combattants intégrés.

Les identités et les épisodes renvoient à Gears of War. Les archétypes, jauges, frames, dégâts, combos, dialogues et fins décrits ici sont créés pour cette adaptation. Les armes attribuées à un kit peuvent provenir de l’arsenal du jeu sans constituer l’arme personnelle canonique de ce personnage. Une rencontre d’arcade entre personnages d’époques différentes ne devient pas un événement de la campagne.

Les pages officielles confirment notamment Kilo Squad dans Judgment, les rôles de Gabe, Sid et Mikayla dans Tactics, ainsi que Scorpio et ses capacités dans Hivebusters. Les détails précis de couture, de cicatrice, d’épaulière et de côté d’une prothèse exigent encore des captures définies. Le champ source_scope de chaque combattant conserve cette différence de niveau de preuve.

## Références de fidélité

Une variante reçoit son propre identifiant, son épisode, son costume et sa feuille de contrôle. Le bandana de Marcus, la pilosité de Dom, les lunettes de Baird, le casque de Clayton et les tatouages de Tai ne doivent pas devenir des accessoires interchangeables. Le personnage conserve les formes et les matériaux du costume choisi. Les armes sont contrôlées avec la même exigence que le visage.

E-Day dispose de références officielles décrivant Marcus, Dom et Tai. Ses variantes restent liées à ces références et à des captures du costume visé. Aucune arme moderne, cicatrice tardive ou pièce d’armure d’une autre époque ne leur est ajoutée par défaut. Ultimate Edition et Reloaded sont des références de présentation du premier jeu, pas automatiquement de nouveaux costumes.

Myrrah, Reine Reyna et Ukkon demandent une validation particulière : leur présence comme combattants directs et l’organisation de leurs coups sont une adaptation. RAAM et le Warden gardent une catégorie de taille élevée. Une créature géante ne devient pas un skin de soldat. JACK garde un corps flottant avec une zone vulnérable accessible ; son vol ne supprime pas les interactions du duel.

Les personnages invités, acteurs jouant un skin promotionnel et collaborations ne sont pas comptés parmi les 36. Anthony Carmine, Benjamin Carmine, Minh Young Kim, Jace, Barrick, Valera, Alicia, Sraak, Jermad, Karn et d’autres candidats pourront recevoir des fiches d’extension. Ils ne sont ni implicitement produits ni assimilés à des recolorations du roster existant.

## Commandes et lecture des données

L, M et H désignent les attaques légère, moyenne et lourde. E désigne la mobilité ; R le rechargement. Les directions utilisent la notation numérique relative à l’adversaire, avec 5 au neutre, 6 vers l’avant et 2 vers le bas. Une entrée 236M signifie bas, diagonale avant, avant, puis moyen. Les raccourcis modernes doivent appeler exactement la même action que cette entrée technique.

Le symbole > désigne une liaison après récupération. Le symbole xx désigne une annulation. La chaîne d’annulations commune est L xx M xx H. Toutes les séquences suivent les autorisations de leur fiche ; la notation n’autorise pas à ignorer une récupération. Les valeurs de frame sont calculées à 60 Hz et mesurées au premier contact possible, hors hitstop. Pour une attaque au sol, avantage = hitstun moins les frames actives restantes moins la récupération. Un projectile éloigné, un impact tardif et une attaque aérienne demandent une mesure distincte.

Les nombres de dégâts partent d’une vie de référence de 1000. Le premier, deuxième et troisième coups d’une séquence utilisent 100 %, 90 % et 80 % de leur valeur. Les estimations des deux combos noyau arrondissent chaque paquet de dégâts à l’entier le plus proche. Elles ne comptent ni bonus de rechargement ni compteur de dégâts additionnel. Le compteur de combo ne peut pas être réinitialisé artificiellement par une animation.

## Normals et actions communes

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

## Les douze combattants du noyau

Chaque fiche propose quatre spéciaux, deux supers et deux exécutions. Une super de niveau 1 coûte 100 points, une super de niveau 2 coûte 200. Les exécutions ont lieu après la dernière manche gagnée ; leurs colonnes de dégâts et de frames de combat restent sans objet. Elles ne se combinent pas à un combo pour tuer automatiquement une cible encore active.

### Marcus Fenix

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

### Dominic Santiago

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

### Damon Baird

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

### Augustus Cole

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

### Anya Stroud

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

### Kait Diaz

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

### Général RAAM

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

### Skorge

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

### Reine Myrrah

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

### Drone locuste

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

### Kantus

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

### Garde Theron

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

## Les vingt quatre combattants de l’extension

Ces combattants disposent chacun de trois signatures. Leur kit complet devra encore ajouter les spéciaux, supers secondaires, exécutions et routes de combo nécessaires au même niveau de finition que le noyau. Les mécaniques sont distinctes : soutien, charge, champ de contrôle, surchauffe, vol bas, barrière, longue portée et double arme ne partagent pas une unique fiche recolorée.

### JD Fenix

Référence : Gears 5, tenue de campagne gears 5 après le prologue. Artilleur à fenêtre de tir. Marque une zone puis déclenche une salve annoncée; éviter les tirs gratuits hors écran.

- **Grenade GL balisée** (236M) : Projectile à courbe et zone annoncée; une seule marque. Démarrage 24 frames, dégâts 120, coût 0.
- **Recul de commandement** (214E) : Recul court consommant une marque pour réduire la récupération. Démarrage 9 frames, dégâts 0, coût 0.
- **Barrage orbital** (236236H) : Super 200, salves fixes successives, première zone toujours visible. Démarrage 28 frames, dégâts 335, coût 200.

Rival de parcours : Warden. Introduction originale : Je prends la responsabilité du tir.

Fin originale : JD démonte les marqueurs du champ de bataille et consigne chaque décision avant le retour de l’escouade.

### Del Walker

Référence : Gears 5, tenue de campagne gears 5. Défense technique et surveillance. Balise qui informe puis protège une seule zone; pas de tourelle autonome permanente.

- **Balise de surveillance** (214M) : Pose destructible qui révèle le prochain déplacement proche. Démarrage 24 frames, dégâts 0, coût 0.
- **Rafale de réparation** (236L) : Tir confirmé recharge une fraction de la balise, jamais des PV gratuits. Démarrage 13 frames, dégâts 85, coût 0.
- **Couloir défendu** (236236H) : Super 200, salve bornée à une moitié d’écran annoncée. Démarrage 25 frames, dégâts 325, coût 200.

Rival de parcours : Drone locuste. Introduction originale : On garde une issue. Toujours.

Fin originale : Del utilise les pièces sauvées pour rétablir un poste de communication pour les réfugiés.

### Fahz Chutani

Référence : Gears 5, tenue de campagne gears 5. Tireur à lecture. Précision acquise à l’arrêt; révélation de position par la visée; tir évitable par changement de hauteur.

- **Visée patiente** (214M) : Préparation immobile 30 frames; perd sa charge sur déplacement. Démarrage 30 frames, dégâts 0, coût 0.
- **Longshot direct** (236H) : Tir unique à signal visuel; hauteur haute esquivable accroupi. Démarrage 24 frames, dégâts 135, coût 0.
- **Tir calculé** (236236H) : Super 200, premier tir vers une position fixée avant le déclenchement. Démarrage 18 frames, dégâts 335, coût 200.

Rival de parcours : Garde Theron. Introduction originale : Bouge encore. J’apprends vite.

Fin originale : Fahz laisse le premier transport aux blessés et rejoint la garde arrière sans commentaire.

### Clayton Carmine

Référence : Gears of War 3, tenue de campagne gears of war 3. Tank et riposte balistique. Absorption ponctuelle convertie en pression; aucun blindage permanent contre les projections.

- **Encaissement balistique** (214E) : Absorbe un projectile, jamais une projection; riposte exige nouvelle entrée. Démarrage 14 frames, dégâts 0, coût 0.
- **Mulcher en appui** (236H) : Rafale immobile; ventiler ensuite; ne se conserve pas en déplacement. Démarrage 26 frames, dégâts 145, coût 0.
- **Mur Carmine** (236236H) : Super 200, tir dévié puis charge; fenêtre de contre visible. Démarrage 16 frames, dégâts 350, coût 200.

Rival de parcours : Grenadier locuste. Introduction originale : Essayez de me faire bouger.

Fin originale : Clayton aligne plusieurs casques sur un établi, puis en prend un seul pour repartir.

### Lizzie Carmine

Référence : Gears 5, tenue de campagne gears 5. Pilote mobile et pièges lourds. Gèle temporairement une trajectoire puis prépare un appel Silverback de courte durée.

- **Freinage tactique** (214M) : Glissade courte qui pose une zone de ralentissement annoncée. Démarrage 20 frames, dégâts 80, coût 0.
- **Salve de pilote** (236M) : Tir avec petit recul; consomme la charge de mobilité. Démarrage 14 frames, dégâts 90, coût 0.
- **Sortie Silverback** (236236H) : Super 200, insertion temporaire du véhicule; silhouette et sortie distinctes. Démarrage 30 frames, dégâts 345, coût 200.

Rival de parcours : Warden. Introduction originale : La route est fermée. Je vais la rouvrir.

Fin originale : Dans cette fin alternative hors continuité, Lizzie remet le moteur en route et ramène son convoi à l’abri.

### Victor Hoffman

Référence : Gears 5 multijoueur, hoffman en armure du lot opération 6. Commandant à ordres limités. Choisit un ordre parmi discipline, couverture et repli; changement d’ordre punissable.

- **Ordre de discipline** (214L) : Choisit une prochaine rafale à faible recul, changement punissable. Démarrage 25 frames, dégâts 0, coût 0.
- **Boltok d’autorité** (236M) : Tir lent mais forte pression à portée moyenne. Démarrage 17 frames, dégâts 105, coût 0.
- **Ligne infranchissable** (236236H) : Super 200, ordre de barrage sur zone annoncée et temporisée. Démarrage 24 frames, dégâts 330, coût 200.

Rival de parcours : Général RAAM. Introduction originale : Un ordre clair. Une sortie pour chacun.

Fin originale : Hoffman marque une nouvelle route sur la carte et laisse une équipe contrôler les issues.

### Tai Kaliso

Référence : Gears of War 2, tenue de campagne gears of war 2. Défenseur à lecture et punition. Garde de préparation qui résiste à un impact; perd contre projection et attaques répétées.

- **Garde du guerrier** (214E) : Encaisse un coup de mêlée hors projection durant une fenêtre brève. Démarrage 12 frames, dégâts 0, coût 0.
- **Retour de Gnasher** (236M) : Punition de proximité après une lecture; pas d’invulnérabilité. Démarrage 15 frames, dégâts 110, coût 0.
- **Résistance de Kaliso** (236236H) : Super 200, frappe lourde initiale et enchaînement d’armes de campagne. Démarrage 13 frames, dégâts 345, coût 200.

Rival de parcours : Skorge. Introduction originale : Je connais le poids de cette ligne.

Fin originale : Dans cette fin alternative, Tai dépose un signe de passage près de l’abri, puis rejoint ceux qu’il a protégés.

### Dizzy Wallin

Référence : Gears of War 2, tenue de pilote de betty. Pièges de terrain et anti-rush. Piège fixé au sol et tir retardé; récompense la préparation sans immortalité de couvert.

- **Piège de conducteur** (214M) : Grenade fixée après délai; un seul dispositif destructible. Démarrage 28 frames, dégâts 115, coût 0.
- **Gnasher de dégagement** (236M) : Tir proche avec recul du tireur. Démarrage 16 frames, dégâts 105, coût 0.
- **Betty tient la route** (236236H) : Super 200, séquence thématique de défense d’un véhicule; véhicule seulement cinématique. Démarrage 27 frames, dégâts 330, coût 200.

Rival de parcours : Général RAAM. Introduction originale : Vous discuterez après le démarrage.

Fin originale : Dizzy remet une plaque sur le moteur et transforme le véhicule en transport pour les survivants.

### Samantha Byrne

Référence : Gears of War 3, tenue de campagne gears of war 3. Tireuse mobile et changements d’angle. Pas court pendant l’armement d’un tir; deux trajectoires lisibles plutôt qu’un tir omnidirectionnel.

- **Pas de tir** (214M) : Déplacement bref préparant deux angles fixes à sélectionner. Démarrage 12 frames, dégâts 0, coût 0.
- **Longshot mobile** (236H) : Tir après le pas; interdit pendant la translation elle-même. Démarrage 22 frames, dégâts 125, coût 0.
- **Couverture croisée** (236236H) : Super 200, deux tirs de positions successives, aucune téléportation. Démarrage 18 frames, dégâts 330, coût 200.

Rival de parcours : Garde Theron. Introduction originale : Un angle libre. Ça me suffit.

Fin originale : Sam transmet un itinéraire dégagé et repart vérifier elle-même le dernier croisement.

### Garron Paduk

Référence : Gears of War Judgment, tenue de kilo squad dans judgment. Duel à distance et intimidation. Les tirs de Markza récompensent l’espacement; intimidation réduit temporairement la garde sans dégâts gratuits.

- **Markza mesuré** (236M) : Tir semi-auto qui récompense une portée optimale. Démarrage 17 frames, dégâts 100, coût 0.
- **Intimidation UIR** (214M) : Cri court de proximité; retire un peu de jauge de garde, jamais de PV. Démarrage 24 frames, dégâts 0, coût 0.
- **Verdict de Kilo** (236236H) : Super 200, rafale précise puis percussion de crosse. Démarrage 14 frames, dégâts 335, coût 200.

Rival de parcours : Reine Myrrah. Introduction originale : Je ne combats pas pour vos décorations.

Fin originale : Paduk arrache un panneau militaire inutile et le remplace par une indication vers le refuge.

### Sofia Hendrik

Référence : Gears of War Judgment, tenue de kilo squad dans judgment. Mobilité disciplinée et secours. Repositionnement en deux temps avec choix de couverture ou de contre; aucun soin infini.

- **Pas de cadette** (214E) : Deux sorties, garde ou contre, avec signe de posture distinct. Démarrage 10 frames, dégâts 0, coût 0.
- **Riposte disciplinée** (236M) : Crosse puis rafale; faible portée, bon retour au neutre. Démarrage 13 frames, dégâts 90, coût 0.
- **Protocole de Kilo** (236236H) : Super 200, ouverture de mêlée et tirs couvrant une évacuation imagée. Démarrage 12 frames, dégâts 325, coût 200.

Rival de parcours : Drone locuste. Introduction originale : Le protocole commence par ramener les vivants.

Fin originale : Sofia consigne le rapport de mission puis inscrit les noms des personnes évacuées avant les objectifs détruits.

### Gabe Diaz

Référence : Gears Tactics, tenue de campagne de base avant personnalisation. Soutien offensif. Exécution confirmée procure un ordre utilisable une seule fois; pas de tour supplémentaire littéral dans un jeu temps réel.

- **Ordre offensif** (214M) : Prépare une ressource de support après 28 frames exposées. Démarrage 28 frames, dégâts 0, coût 0.
- **Lancer de soutien** (236M) : Rafale consomme l’ordre pour réduire le recul, pas de double dégât. Démarrage 14 frames, dégâts 95, coût 0.
- **Escouade ralliée** (236236H) : Super 200, percée personnelle suivie d’une courte assistance cadrée. Démarrage 15 frames, dégâts 335, coût 200.

Rival de parcours : Ukkon. Introduction originale : Une ouverture suffit. Préparez-vous.

Fin originale : Gabe distribue le matériel récupéré aux survivants et repart avant que le poste soit devenu confortable.

### Sid Redburn

Référence : Gears Tactics, tenue de campagne de base. Vanguard et disruption. Intimidation à courte portée ouvre la garde; résistance active de durée limitée.

- **Intimidation Vanguard** (214M) : Courte zone de perturbation; requiert proximité et démarre lentement. Démarrage 23 frames, dégâts 70, coût 0.
- **Charge Retro** (236H) : Charge baïonnette, ligne fixe, récupération importante. Démarrage 24 frames, dégâts 135, coût 0.
- **Briser le front** (236236H) : Super 200, coup de crosse initial puis charge au Retro Lancer. Démarrage 13 frames, dégâts 345, coût 200.

Rival de parcours : Ukkon. Introduction originale : Cette fois, on termine la mission.

Fin originale : Sid range un dossier fermé et assure personnellement la garde de nuit.

### Mikayla Dorn

Référence : Gears Tactics, tenue de campagne de base. Sniper et préparation. Position d’observation unique; quitter la pose annule la précision bonus.

- **Poste d’observation** (214E) : Pose stationnaire; une seule position active et aucune invisibilité. Démarrage 28 frames, dégâts 0, coût 0.
- **Longshot préparé** (236H) : Tir haut, forte récupération, bénéficie seulement de la pose active. Démarrage 25 frames, dégâts 140, coût 0.
- **Angle mort** (236236H) : Super 200, visée annoncée puis tir qui garde sa trajectoire de départ. Démarrage 20 frames, dégâts 340, coût 200.

Rival de parcours : Garde Theron. Introduction originale : Tu ne passeras pas vers les miens.

Fin originale : Mikayla rend aux civils une rue praticable et forme une nouvelle sentinelle à surveiller l’horizon.

### Reine Reyna

Référence : Gears 5 multijoueur, reine reyna du lot opération 6. Contrôle organique et saisies. Extensions organiques séparées du hurtbox central; attaques de portée longue avec récupération élevée.

- **Fouet de l’Essaim** (236M) : Allonge organique avec hurtbox exposée sur l’appendice. Démarrage 19 frames, dégâts 115, coût 0.
- **Entrave organique** (214H) : Saisie de sol annoncée; échoue contre saut et contre cible en hitstun. Démarrage 30 frames, dégâts 140, coût 0.
- **Couronne de l’Essaim** (236236H) : Super 200, projections organiques sur zones signalées. Démarrage 26 frames, dégâts 350, coût 200.

Rival de parcours : Kait Diaz. Introduction originale : La ruche n’oublie aucune voix.

Fin originale : Dans cette fin alternative, une pulsation traverse la ruche. Aucun destin canonique de Kait n’est imposé par cet ending.

### Lahni Kaliso

Référence : Gears 5 Hivebusters, tenue de campagne hivebusters. Mêlée et charge électrique. Electroblade dure un temps court avec consommation à chaque coup; pression puissante mais à faible portée.

- **Lame d’ouverture** (236L) : Percée de très courte portée au couteau. Démarrage 10 frames, dégâts 85, coût 0.
- **Electroblade** (214H) : Charge temporaire plafonnée; chaque attaque électrique consomme une unité. Démarrage 25 frames, dégâts 0, coût 0.
- **Arc de Scorpio** (236236H) : Super 200, premier coup de lame puis impulsions électriques de portée courte. Démarrage 9 frames, dégâts 340, coût 200.

Rival de parcours : Warden. Introduction originale : Je passe en premier. Restez près de moi.

Fin originale : Lahni retrouve Scorpio au point d’extraction et coupe sa charge électrique avant d’aider les blessés.

### Keegan

Référence : Gears 5 Hivebusters, tenue de campagne hivebusters. Soutien de munitions et explosifs. Resupply crée une zone limitée; le combattant doit y rester exposé pour récupérer des ressources.

- **Resupply** (214M) : Zone de munitions à occupation requise, durée et rendement plafonnés. Démarrage 30 frames, dégâts 0, coût 0.
- **Boomshot de couverture** (236H) : Projectile lent en cloche, explosion annoncée à l’impact. Démarrage 27 frames, dégâts 135, coût 0.
- **Réserve de Scorpio** (236236H) : Super 200, tirs explosifs successifs sans recharge pendant la cinématique. Démarrage 23 frames, dégâts 345, coût 200.

Rival de parcours : Kantus. Introduction originale : Il reste de quoi ouvrir la sortie.

Fin originale : Keegan partage les réserves restantes avant de prendre sa propre part.

### Mac

Référence : Gears 5 Hivebusters, tenue de campagne hivebusters. Bouclier mobile et arme de poing. Barrier s’oriente au déclenchement et s’épuise; les attaques arrière et projections restent une réponse.

- **Barrier** (214E) : Bouclier frontal orienté au départ; pas de rotation automatique. Démarrage 20 frames, dégâts 0, coût 0.
- **Boltok derrière la ligne** (236M) : Tir lent permis avec Barrier mais réduit sa durée. Démarrage 17 frames, dégâts 100, coût 0.
- **Avancée de Scorpio** (236236H) : Super 200, charge de bouclier comme première frappe puis tirs de Boltok. Démarrage 12 frames, dégâts 335, coût 200.

Rival de parcours : Drone de l’Essaim. Introduction originale : Cette fois, la barrière tient.

Fin originale : Mac observe le départ du transport, puis abaisse enfin sa barrière au milieu du silence.

### JACK

Référence : Gears 5, robot de soutien de campagne. Vol bas et outils. Hauteur flottante limitée par une jauge; boîte de collision centrale persistante; pas de camping aérien.

- **Arc électrique** (236M) : Tir court avec distance maximale stricte. Démarrage 14 frames, dégâts 85, coût 0.
- **Décalage de vol** (214E) : Monte ou descend d’une seule hauteur; batterie drainée pendant la hauteur haute. Démarrage 12 frames, dégâts 0, coût 0.
- **Surcharge de soutien** (236236H) : Super 200, impulsion après signal; ne neutralise pas toutes les commandes adverses. Démarrage 21 frames, dégâts 320, coût 200.

Rival de parcours : DeeBee. Introduction originale : Signal sonore original sans imitation de voix.

Fin originale : JACK recharge sur un établi pendant que les voyants d’un poste de secours se rallument.

### DeeBee

Référence : Gears of War 4, unité shepherd standard. Robot à surchauffe. Enforcer alimente une jauge de chaleur; ventilation forcée punitive si le joueur prolonge les rafales.

- **Enforcer en rafale** (236M) : Rafale augmente chaleur; interdite au seuil de surchauffe. Démarrage 13 frames, dégâts 95, coût 0.
- **Ventilation forcée** (214E) : Réduit chaleur avec une fenêtre de 46 frames entièrement punissable. Démarrage 24 frames, dégâts 0, coût 0.
- **Protocole de suppression** (236236H) : Super 200, rafale lourde puis ventilation imposée; pas d’autodestruction gratuite. Démarrage 19 frames, dégâts 330, coût 200.

Rival de parcours : JACK. Introduction originale : Périmètre contesté. Intervention en cours.

Fin originale : Le DeeBee classe la zone comme accessible et rejoint une colonne de réparation.

### Warden

Référence : Gears 5, warden standard de campagne. Deux masses et rupture de garde. Deux armes lourdes alternent zones d’impact; casque segmenté visuel et armure temporaire limitée.

- **Masse gauche** (236M) : Frappe de sol à grand rayon; côté de frappe annoncé. Démarrage 22 frames, dégâts 135, coût 0.
- **Masse droite** (214H) : Overhead lent; peut casser une armure temporaire, pas une garde entière. Démarrage 28 frames, dégâts 145, coût 0.
- **Garde brisée** (236236H) : Super 200, coup initial lourd puis alternance des deux masses. Démarrage 17 frames, dégâts 360, coût 200.

Rival de parcours : Augustus Cole. Introduction originale : La ruche garde ce seuil.

Fin originale : Le Warden reprend sa place devant l’entrée de la ruche, comme un poste de garde redevenu silencieux.

### Drone de l’Essaim

Référence : Gears of War 4, drone standard de campagne. Pression au sol et prises. Prise au contact puis recul; arme de référence et configuration exactes à verrouiller avant génération.

- **Rafale de l’Essaim** (236M) : Rafale au recul variable borné, trajectoire déterministe. Démarrage 15 frames, dégâts 95, coût 0.
- **Prise de chasse** (63214H) : Projection courte avec recul après succès; impossible pendant hitstun. Démarrage de 12 frames, plus lent que la projection normale; réponse par saut ou recul. Démarrage 12 frames, dégâts 135, coût 0.
- **Pression de ruche** (236236H) : Super 200, frappe puis tirs, sans contrôle mental ou téléportation ajoutés. Démarrage 14 frames, dégâts 335, coût 200.

Rival de parcours : Kait Diaz. Introduction originale : La prise revient à la ruche.

Fin originale : Le Drone rejoint une procession dans les profondeurs; l’ending montre sa fonction de troupe.

### Ukkon

Référence : Gears Tactics, scientifique de campagne. Invocations limitées et zones. Un spécimen de petite taille actif à la fois; ses ordres ont une anticipation et une récupération visibles.

- **Spécimen libéré** (214M) : Une petite invocation destructible avec trajet annoncé; pas de boss miniature. Démarrage 30 frames, dégâts 95, coût 0.
- **Ordre d’expérience** (236M) : Donne une commande au spécimen; échec visible si aucune invocation. Démarrage 18 frames, dégâts 105, coût 0.
- **Expérience interdite** (236236H) : Super 200, laboratoire imagé en arrière-plan et attaque bornée au plan du duel. Démarrage 28 frames, dégâts 340, coût 200.

Rival de parcours : Gabe Diaz. Introduction originale : Chaque résistance apporte une donnée.

Fin originale : Dans cette fin alternative, Ukkon referme un carnet de résultats et disparaît dans son laboratoire.

### Grenadier locuste

Référence : Gears Tactics, grenadier standard. Gnasher et rage contrôlée. Une jauge monte quand il subit des dégâts puis s’épuise pendant sa charge; résistance et contre ne se cumulent pas.

- **Gnasher en rage** (236M) : Tir proche, recul accru en mode rage mais aucune armure simultanée. Démarrage 14 frames, dégâts 110, coût 0.
- **Charge enragée** (236H) : Consomme jauge de rage pour progresser; pas de boucle de gain pendant charge. Démarrage 24 frames, dégâts 130, coût 0.
- **Brèche de l’assaut** (236236H) : Super 200, percussion puis tirs rapprochés; aucune grenade hors écran. Démarrage 15 frames, dégâts 345, coût 200.

Rival de parcours : Clayton Carmine. Introduction originale : Plus près.

Fin originale : Le Grenadier rassemble son groupe autour d’une brèche fraîche et repart vers la ligne suivante.

## Armes et traduction en duel

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

## Routes individuelles et mise en scène

Chaque route comporte cinq duels, un rival, une rencontre Boss Battle et un duel final, suivis d’un ending indépendant. Les adversaires des duels sont tous distincts pour éviter une répétition involontaire. La route enregistre les identifiants, le besoin d’arène, l’introduction et les règles de chaque étape. La défaite au boss autorise une reprise au boss dans le réglage standard ; la variante d’endurance peut imposer d’autres ressources, annoncées avant le départ.

Les 36 introductions, scènes de rivalité et fins sont livrées comme synopsis originaux. Elles fournissent une direction de mise en scène et une phrase d’introduction. Elles ne constituent pas encore des scripts de doublage complets, des vidéos ou des dessins d’ending. Le texte prononcé par JACK demeure un signal sonore original ; on ne lui invente pas un acteur humain à imiter.

L’écran de fin conserve une image propre au personnage, un court épilogue et le retour au menu. Une version courte passe l’exécution et affiche directement le résultat. L’unlock récompense une illustration ou une entrée de galerie, sans modifier les dégâts du personnage en tournoi.

## Tests des kits et réponses adverses

Les liens temporels des 24 combos du noyau satisfont les fenêtres inscrites : 2L à +6 vers 5L à 6 frames, puis annulation vers S1 dans les 18 frames de hitstun ; 5H à +10 vers 5M à 10 frames, puis annulation vers U1 dans les 23 frames de hitstun. Ces preuves restent conditionnées au contact réel, au recul et aux hitboxes. Le moteur doit tester défense enregistrée, contre attaque la plus rapide, saut et roulade à chaque liaison.

Les projections spéciales ne prennent pas une cible en hitstun. Un super qui conclut un combo possède donc une frappe d’ouverture, puis seulement une saisie cinématique. Les invocations de Myrrah et Ukkon ont une limite explicite, une arrivée signalée et un moyen d’interruption. Le chant du Kantus ne produit pas une boucle de soin en duel. L’armure de RAAM et Clayton ne couvre pas les projections. La furtivité de Kait conserve un indice de position. Ces règles sont des conditions de lisibilité, pas des capacités officiellement attribuées à ces personnages dans tous leurs épisodes.

Chaque kit doit réussir quatre essais avant validation : neutralité sans ressource, punition d’un spécial raté, réponse disponible à la mécanique dominante, puis combat entier sans boucle. L’intégration finale ajoute les tests de collisions pour les paires S contre XL et pour les saisies entre humain, Locuste, Essaim et robot.

## Sources de référence des personnages

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
