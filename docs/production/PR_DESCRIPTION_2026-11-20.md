# Gears Combats — corpus récupéré et production V6/V7

## Pourquoi

La PR rassemble le corpus qui manquait au dépôt et poursuit la production des personnages, costumes, boss et décors. La passe V7 corrige aussi l'absence de rattachement entre des images déjà présentes et leurs fiches de costumes, tout en gardant les éditions et réserves artistiques visibles.

## Corpus et passe précédente conservés

- Restauration initiale de 277 fichiers : bible PDF/DOCX, tableurs, prototype, données, images, galerie et provenance.
- Récupération de Dizzy Gears 2 ; 36 personnages du roster initial disposent d'une référence.
- Lot V6 conservé : Boomer Tactics, Alicia Gears 3, Mechanic Mac, Matriarch et Gridlock Gears 4.
- Livrables du 19 novembre préservés comme instantanés historiques ; les JSON et la galerie décrivent la couverture courante.

## Six nouvelles images V7

| Sujet | Édition | Portée du fichier |
|---|---|---|
| Michael Barrick | Gears of War 3 — RAAM's Shadow | Personnage entier ; variante historique, cible Gears 5 encore ouverte |
| Colonel Ezra Loomis | Gears of War: Judgment | Personnage entier, pose bras croisés |
| Thrashball Cole | Gears of War 3 | Costume `cole_skin_03`, casque tenu à la main |
| Shibboleth | Gears of War: Judgment | Monture seule ; Karn absent et duo incomplet |
| Village | Gears 5 — Operation 8 | Master de l'intérieur cérémoniel adapté au combat 2D |
| Dawn | Gears 5 — Operation 8 | Master de la colonie minière adapté au combat 2D |

Chaque fichier possède son journal de génération, ses références, son prompt intégral, ses mesures techniques et ses réserves visuelles. Les sources reproduites sur des sites tiers restent identifiées comme telles.

## Catalogue et rattachements

- Ajoute trois identités documentées : Adam Fenix, version multijoueur Gears 3 ; Alex Brand, version multijoueur Judgment ; Karn, modèle Judgment distinct de la rencontre `boss_shibboleth`.
- Relie **34 PNG de personnages existants** à leur costume, sans copie d'image ni changement de statut artistique.
- Le mapping vérifie l'identité du personnage, le costume, l'empreinte SHA-256 et le journal de provenance. Un changement d'image invalide un lien devenu obsolète.
- Le rapport au costume ciblé est distinct du rapport à la tenue de base du personnage. Les variantes d'une autre édition ne remplissent pas silencieusement cette tenue de base.
- Charge les catalogues versionnés dans l'ordre numérique et fusionne leurs identités sans modifier le roster du moteur.
- Affiche les justifications des rattachements et leurs preuves dans la galerie.

## Couverture actuelle

| Catégorie | Fiches | Avec référence |
|---|---:|---:|
| Personnages, roster initial et extensions | 56 | 40 |
| Costumes | 85 | 36 |
| Boss, véhicules et rencontres | 31 | 6 |
| Stages | 34 | 4 |

**62 PNG actifs uniques**, plus **12 révisions archivées**. Les 62 actifs comprennent 49 images de personnages et variantes, 2 fichiers dédiés aux costumes, 6 boss ou véhicules et 5 décors. Ephyra reste un master supplémentaire sans rattachement arbitraire à une arène.

Le suivi garde **16 identités de personnages**, **49 costumes sans rattachement**, **25 boss ou rencontres** et **30 stages** sans référence associée. Les éditions cibles de Marcus 2006, Alicia Gears 5 et Barrick Gears 5 restent ouvertes malgré l'existence d'une autre version illustrée. Karn reste à produire pour compléter le duo avec Shibboleth.

## Vérification

- Validation des données core sans erreur.
- **8 tests d'inventaire réussis** : 4 V6 et 4 V7, dont les contrôles de réutilisation sans doublon, d'édition, de provenance, de SHA et de fusion des catalogues.
- Syntaxe JavaScript de la galerie et du template contrôlée.
- **74 PNG vérifiés**, actifs et archives, avec contrôle des chemins, empreintes, dimensions et alpha.
- Six journaux V7 et 34 rattachements audités contrôlés.
- Les 15 tests du moteur réussis lors de la reprise précédente restent une preuve antérieure ; le moteur n'est pas modifié par V7.
- La validation visuelle dans Chromium reste indisponible à cause du blocage de lancement déjà constaté. Aucun contrôle responsive réel n'est revendiqué.

## Fidélité et suite de production

**Aucune fidélité 1:1 n'est certifiée et aucune série d'animations complète n'est livrée.** Les comptes portent sur des références statiques. Les journaux conservent les écarts précis : visages, marquages, tatouages, gravures, orientation, parties masquées et marges. Les décors sont aplatis, avec une composition adaptée au combat latéral ; leurs couches de parallaxe restent à produire.

Del, Lizzie, Reyna et Skorge conservent leur statut de correction. Les réserves sur les références historiques et la provenance partielle de certaines reproductions restent visibles. Le prototype conserve ses trois rencontres existantes.

## Documents de suivi

- `docs/production/LISTING_V7.md` : listing courant et manques par catégorie.
- `docs/production/REPRISE_V7.md` : bilan, éditions et priorités de production.
- `docs/production/AUDIT_COSTUMES_V7.md` : les 34 rattachements et leurs preuves.
- `docs/production/VALIDATION_V7.json` : résultats et limites des contrôles.
- `docs/references/production-v7-catalog.md` : sources des trois nouvelles identités.
- `data/generation_v7/` : six journaux et prompts complets.
