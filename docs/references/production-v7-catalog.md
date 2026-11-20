# Catalogue de production V7 — trois identités complémentaires

Audit du 20 novembre 2026. Fichier associé : [production_catalog_v7.json](../../data/production_catalog_v7.json).

Cette passe ajoute **3 fiches de personnages**, sans image, costume autonome, boss ou stage supplémentaire. Les sources établissent les identités et les éditions ciblées. Aucune nouvelle fiche ne certifie une fidélité visuelle 1:1, une génération réalisée ou une implémentation jouable.

## Vérification des omissions

La vérification porte sur les identifiants et noms de `data/roster.json`, `data/production_catalog_v6.json` et `data/bosses.json`. Le roster initial contient 36 personnages ; V6 ajoute 17 identités, soit 53 avant cette passe.

| Identifiant ajouté | Édition et apparence ciblées | Constat dans les données antérieures | Décision |
| --- | --- | --- | --- |
| `adam_fenix` | Gears of War 3, personnage multijoueur Adam Fenix | Aucun identifiant ni fiche de personnage Adam Fenix dans le roster ou V6 | Ajouter une cible de personnage ; détails de tenue en pied à documenter |
| `alex_brand` | Gears of War: Judgment, apparence multijoueur Alex Brand | Aucune fiche de personnage dans le roster ou V6 | Ajouter une cible de personnage documentée par Xbox et son modélisateur |
| `karn` | Gears of War: Judgment, modèle de Karn | Aucune fiche autonome ; le nom apparaît déjà dans `boss_shibboleth`, « Karn sur Shibboleth » | Ajouter le personnage ; conserver la rencontre existante sans nouveau boss |

La présence du nom Karn dans une rencontre montée est enregistrée explicitement : il ne s'agit pas d'un personnage absent de toute documentation, mais d'une identité sans fiche autonome dans le catalogue des personnages.

## Preuves primaires et limites

### Adam Fenix

- [Fiche Xbox — Adam Fenix Multiplayer Character](https://www.xbox.com/en-us/games/store/adam-fenix-multiplayer-character/btt6glfffmlv) : publication Microsoft Studios, développement Epic Games, contenu associé à Gears of War 3. La cible retenue est cette apparence multijoueur.
- [Xbox Wire — annonce du 6 juin 2011](https://news.xbox.com/en-us/2011/06/06/announcing-the-xbox-360-gears-of-war-3-limited-edition-console/) : l'offre Gears of War 3 inclut Adam Fenix comme personnage multijoueur.

Ces deux sources suffisent pour l'identité, le jeu et la variante de distribution. Elles ne constituent pas ici une inspection visuelle complète du modèle. La tenue de campagne, les matériaux et les détails masqués ne sont pas extrapolés. Statut : `identity_confirmed_game_costume_pending`.

### Alex Brand

- [Xbox Wire — annonce des précommandes du 7 novembre 2012](https://news.xbox.com/en-us/2012/11/07/gears-of-war-judgment-pre-orders-kickoff-today/) : Alex Brand est nommée parmi les apparences multijoueurs de Judgment proposées avec certaines précommandes.
- [Mike Kime — modèle Alex Brand pour Judgment](https://pseudopod.artstation.com/projects/OgJa6) : le portfolio crédite le concept à James Hawkins et le modèle à Mike Kime, avec certaines pièces issues du travail de Chris Wells.
- [Entretien des artistes Epic et People Can Fly, Maxon, 28 août 2013](https://www.maxon.net/en/article/creating-assets-for-epic-games-gears-of-war-judgment) : Mike Kime confirme avoir travaillé sur Alex Brand.

L'apparence cible reste celle de Judgment. Aucune fusion avec les comics ou une édition différente n'est établie. Les pages et leurs crédits ont été vérifiés ; la comparaison des vues du modèle aux captures finales du jeu reste à faire. Statut : `identity_and_model_credit_confirmed_visual_review_pending`.

### Karn et la rencontre Shibboleth

- [Mike Kime — modèle Karn pour Judgment](https://pseudopod.artstation.com/projects/gVB5E) : concept James Hawkins ; modèle partagé entre Mike Kime et Mark Morgan ; l'artiste précise son travail sur un état endommagé.
- [Entretien Epic / People Can Fly, Maxon, 28 août 2013](https://www.maxon.net/en/article/creating-assets-for-epic-games-gears-of-war-judgment) : les développeurs distinguent le travail de PCF sur Shibboleth de celui de Kime et Morgan sur Karn.

Le nouvel identifiant `karn` désigne le personnage. `boss_shibboleth` conserve la rencontre déjà cataloguée et son contexte monté. Cette séparation n'ajoute aucun boss. L'état intact ou endommagé devra être fixé avant une génération ; aucun statut multijoueur n'est déduit de ces sources. Statut : `identity_and_model_credit_confirmed_visual_review_pending`.

## Comptes et intégration

| Catégorie | Après V6 | Ajouts nets V7 | Après fusion V6 + V7 |
| --- | ---: | ---: | ---: |
| Personnages | 53 | 3 | 56 |
| Costumes autonomes | 85 | 0 | 85 |
| Boss / rencontres | 31 | 0 | 31 |
| Stages | 34 | 0 | 34 |

Le fichier conserve les quatre tableaux `characters`, `costumes`, `bosses` et `stages`. Seul `characters` reçoit des entrées ; les trois autres tableaux restent vides. La fusion se fait par identifiant après V6. Les comptes ci-dessus décrivent le catalogue, pas des assets ni des combattants implémentés.

Aucun PNG, journal de génération, statut d'asset, roster jouable ou rencontre existante n'est modifié par cet audit. Les trois fiches gardent `canonical_fidelity_validated: false`. Les seules sorties de cette tâche sont le catalogue V7 et le présent rapport.
