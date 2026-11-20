# Prototype jouable de Gears of War Combats

Ouvrir **Gears_Combats_Prototype.html** dans un navigateur moderne. Ce fichier est autonome : code, styles et illustrations disponibles sont embarqués. Il ne requiert aucun compte, serveur, installation ni connexion réseau. Le dossier source peut également être servi localement pour travailler sur `index.html`.

## Contenu réellement jouable

- Duel de profil : Marcus Fenix contre le général RAAM contrôlé par l’ordinateur.
- Boss Berserker : charge vers un mur, écrasement, ouverture vulnérable et trois phases.
- King Raven : simulation non canonique contre un véhicule allié, bombardements annoncés, moteur vulnérable et trois phases.
- Déplacement, coup léger, coup lourd, garde avec jauge, esquive temporairement invulnérable, tir, chargeur de huit tirs, recharge active et tir spécial.
- Recharge parfaite : deux tirs renforcés de 10 %, arrondis à l’entier. Erreur de timing : enrayage temporaire.
- Chronomètre, vie, jauge spéciale, série de coups, score, pause, victoire, défaite et reprise.
- Six plans visuels avec des facteurs de parallaxe distincts. Le décor peint, lorsqu’il est chargé, constitue un fond supplémentaire ; il n’est pas livré comme un jeu de six couches peintes séparées.
- Commandes clavier AZERTY et QWERTY, tactiles et manettes compatibles avec l’API standard du navigateur.

Les chiffres et les phases de combat sont des propositions d’adaptation 2D. Les silhouettes dessinées dans le code sont des volumes temporaires. Les illustrations embarquées, lorsqu’elles sont disponibles, sont des poses fixes animées par déplacement et oscillation ; elles ne constituent pas encore des séries d’animation finalisées. Le King Raven reste une simulation explicitement séparée du récit officiel.

La reprise du 20 novembre embarque les poses neutres de Marcus et de RAAM. Les tirs et contacts restent pilotés par le moteur sans dessins correspondants des gestes. L’option « Afficher les illustrations des combattants » permet de revenir aux silhouettes mécaniques. Le duel illustré a été rendu et inspecté dans le canvas ; les pieds restent au sol et les deux personnages sont cadrés. Le contrôle canonique détaillé reste à finaliser. Berserker et King Raven gardent leurs volumes temporaires. Les autres PNG, y compris Dom et Theron, restent des références de production sans personnage jouable supplémentaire.

## Commandes

| Action | Clavier | Manette standard |
|---|---|---|
| Déplacement | Q ou A, D, flèches | Stick gauche ou croix |
| Coup léger | J | X |
| Coup lourd | K | Y |
| Tir | L maintenu | RT |
| Spécial à 100 points | I | RB |
| Garde de face | F ou flèche bas | LT |
| Esquive | Espace avec direction | A avec direction |
| Recharge active | R puis R dans la zone claire | B puis B |
| Pause | Échap | Start |

Les étiquettes manette suivent la disposition Xbox. Le navigateur peut demander un premier appui pour détecter une manette. La prise en charge matérielle n’a pas été vérifiée sur chaque modèle. Sur téléphone, les boutons tactiles restent visibles sous l’arène ; l’affichage paysage rend les distances plus faciles à lire.

## Gagner les rencontres

**Duel.** Les tirs contrôlent la distance mais le chargeur est limité. Garder réduit les dégâts ; rester continuellement en garde épuise sa jauge. Les coups lourds de RAAM sont annoncés par son armement et un signal au-dessus de sa tête.

**Berserker.** Les attaques géantes ignorent la garde. Le cercle annonce la portée de l’écrasement ; la ligne annonce la charge. Esquiver la traversée ou sortir de la zone. Quand le boss est étourdi, le signal doré ouvre une fenêtre de dégâts complets. Tirer sur le blindage fermé inflige seulement 18 % des dégâts normaux, ou 30 % pour le spécial.

**King Raven.** Quitter les cercles avant l’impact. Après la salve, viser le moteur pendant son ouverture. Les tirs s’orientent automatiquement en hauteur ; conserver de la distance horizontale avec l’appareil. Chaque phase ajoute une zone de bombardement.

## Structure et intégration

`engine.js` expose un moteur déterministe à 60 mises à jour par seconde, indépendant du rendu. `app.js` gère le canvas, les commandes et l’interface. `index.html` contient les styles et le balisage. `build.mjs` produit l’HTML autonome. `tests.cjs` vérifie les interactions critiques.

Les actifs peuvent être indiqués avant le chargement par `window.GEARS_ASSETS`, avec les clés `marcus`, `raam`, `berserker` et `stage`. Les sources attendent sinon `../assets/marcus_neutral_cutout.png`, `../assets/characters_v5/raam_gow1_fullbody.png`, `../assets/berserker.png` et `../assets/stage_ephyra.png`. Les fichiers absents déclenchent les volumes temporaires. Pour le fichier autonome, créer au besoin `asset-map.json` avec ces mêmes clés et les noms relatifs au dossier `assets`, puis lancer `node build.mjs`. Le script embarque les actifs trouvés et retire les dépendances relatives absentes.

Exemple de carte d’assets :

```json
{"marcus":"marcus_gow1_stance.png","raam":"raam_gow1_stance.png","berserker":"berserker_gow1_stance.png","stage":"ephyra_stage.png"}
```

## Validation

Lancer `node tests.cjs` pour vérifier la garde, l’esquive, les bornes inclusives de recharge, son bonus limité, l’enrayage, les dégâts de faiblesse, la progression de phase, la portée du corps à corps, les zones du véhicule, la pause et les résultats, ainsi que les bornes de simulation. Les 15 tests ont été exécutés avec succès. Le hasard des effets est séparé du hasard de l’IA.

Le rendu du canvas des trois rencontres a été produit, et le duel avec la nouvelle image de RAAM a été inspecté lors de la reprise du 20 novembre. Le chargement des scripts, le buffer des appuis tactiles courts et la pause ont aussi été vérifiés dans un environnement de test JS. Ce contrôle ne valide pas le rendu HTML et CSS dans un navigateur. Le lancement Chromium local est bloqué par une restriction système de sockets ; le navigateur Cloud ne permet pas les URL locales de type fichier. Aucune validation responsive réelle ni vérification de manette physique n’est donc déclarée.

Les fonctions `window.GearsPrototype.choose(mode)`, `start()`, `pause()` et `getState()` servent à l’inspection du prototype. Elles ne communiquent avec aucun service externe.

## Étapes encore prévues dans la bible

Campagne complète, tournoi, sélection de tout le roster, coups propres à chaque personnage, cinématiques, exécutions, sprites d’animation individuels, audio final, matchs locaux à deux joueurs, jeu en ligne et rollback ne sont pas implémentés dans ce prototype. Les contenus de la bible et le contenu réellement jouable sont suivis séparément.

## Profil de règles livré

| Élément | Règle du prototype | Différence avec la cible complète |
|---|---|---|
| Duel | Une manche de 99 secondes | La cible prévoit deux manches gagnantes |
| Vie | Marcus 1 000, RAAM 1 250, Berserker 2 800, King Raven 2 400 | Valeurs de test propres à ces rencontres |
| Attaques | Léger 6/3/15 frames et 62 dégâts ; lourd 17/4/25 et 112 dégâts | Moyen, hauteurs, projections, annulations et vrais combos à intégrer |
| Spécial | Jauge unique de 100, tir de 270 dégâts | La cible prévoit trois barres, plusieurs supers et un briseur |
| Tir | 8 munitions, 58 dégâts ; 64 après recharge parfaite | Le bonus de 10 % est arrondi à l’entier le plus proche |
| Recharge normale | 72 frames | Conforme au profil de base |
| Recharge parfaite | Confirmation de 34 à 43 inclus, fin à 44, deux tirs renforcés | Conforme au profil de base |
| Recharge sûre | Confirmation de 27 à 33 ou de 44 à 50 inclus, fin à 60 | Conforme au profil de base |
| Enrayage | Fin à 102 frames, soit 72 + 30 | Conforme au profil de base |
| Interruption de recharge | Tout impact non gardé annule le chargement en cours | Verrouillage intermédiaire du chargeur à implémenter |
| Garde | Bouton, sans hauteurs ; 0 chip au corps à corps ; 10 % sur tirs, non létal en duel | Garde directionnelle, haute/basse et parfaite à intégrer |
| Posture | 100 points ; perte égale à 50 % des dégâts gardés | Valeur de consommation de test à ajuster par coup |
| Régénération de posture | Après 45 frames sans garde ni coup reçu, 15 points par seconde | Conforme au profil de base |
| Rupture | 45 frames, puis 60 points restaurés | Conforme au profil de base |
| Esquive | 30 frames ; fenêtre d’évitement de 16 frames ; retour disponible après 66 frames | Endurance et coût de 25 points non implémentés |
| Série | Impacts rapprochés dans une fenêtre de 80 frames | Le compteur ne certifie pas un combo sans échappatoire |
| Boss | Phases à 66 % puis 33 %, ouverture de faiblesse, temps limite de 180 s | Parties destructibles, caméra avancée et coopération à intégrer |
| Décor | Un fond peint intégré et plans de rendu additionnels | Couches peintes séparées à produire |

La roulade réussie accorde également huit frames de protection contre les impacts multiples d’une même attaque géante. Les rencontres du prototype n’incluent pas d’attaques instantanément létales.
