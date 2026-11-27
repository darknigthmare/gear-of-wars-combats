# Listing V14 — images fixes et fidélité à l’édition

**27 novembre 2026 · Darknigthmare · Gears of War Combats**

La passe apporte **5 nouveaux PNG actifs**, **2 révisions Reyna archivées, avec la correction de coiffure sélectionnée comme référence**, **1 refus unique pour Mina Jinn** et **1 alias Lahni documenté sans génération**. Les **18 refus antérieurs** sont conservés sans relance.

Un sujet et une pose par PNG, dimensions et octets natifs. **0 fidélité 1:1 certifiée ; 0 ensemble d’animations complet.** Les nombres mesurent des références attribuées, pas des personnages jouables ni des éditions visuellement homologuées.

## Cinq nouveaux candidats

| Sujet | Édition | Fichier | Dimensions | Provenance |
| --- | --- | --- | --- | --- |
| Reyna Diaz humaine Outsider — correction ciblée de la coiffure | Gears of War 4 | [PNG](../../assets/costumes_v14/reyna_human_g4_hairfix.png) | 1024 × 1536 · RGBA | [Sources, prompt et QA](../../data/generation_v14/reyna_skin_02_record.json) |
| Carrier Minion / Canker — Gears of War 4 | Gears of War 4 | [PNG](../../assets/projectiles_v14/canker_g4.png) | 1877 × 838 · RGBA | [Sources, prompt et QA](../../data/generation_v14/projectile_canker_g4_record.json) |
| Leech individuel — Gears 5 | Gears 5 | [PNG](../../assets/creatures_v14/leech_g5.png) | 2172 × 724 · RGBA | [Sources, prompt et QA](../../data/generation_v14/creature_leech_g5_record.json) |
| Wretch — modèle organique Gears of War: E-Day | Gears of War: E-Day | [PNG](../../assets/creatures_v14/wretch_eday.png) | 1024 × 1536 · RGBA | [Sources, prompt et QA](../../data/generation_v14/creature_wretch_eday_record.json) |
| Ticker organique — Gears of War: E-Day | Gears of War: E-Day | [PNG](../../assets/creatures_v14/ticker_eday.png) | 1774 × 887 · RGBA | [Sources, prompt et QA](../../data/generation_v14/creature_ticker_eday_record.json) |

### Reyna Diaz humaine Outsider — correction ciblée de la coiffure

`reyna_skin_02` · SHA-256 `2f286efc3e8da89109c2008f86c5a5fb3222cb2fcbff8c6726ade2e60b90cff1`.

Natte sur l’épaule anatomique droite, tatouage bras gauche et tenue humaine G4 conservés. La correction sélectionnée couvre la tempe droite de cheveux ; elle corrige le rasage inversé de l’original, d’après la référence officielle. Le visage, les motifs précis et les accessoires restent à comparer. Trois-quarts surtout frontal ; marges utiles de 26 px en haut et 10 px en bas (alpha > 8), inférieures à la cible. Alpha maximal natif 254. Le halo apparent de certains aperçus provient principalement de RGB sous alpha 0 ; de vrais pixels à faible alpha subsistent.

### Carrier Minion / Canker — Gears of War 4

`projectile_canker_g4` · SHA-256 `d4a9280ef8d64a723f85b7337d4632f217b0e04140ccb82a28a3f699099be29b`.

Un seul projectile organique complet, sac à droite et appendices à gauche. Lobes et membranes suivent la référence finale ; la lueur interne est plus vive, les fines nervures et appendices sont réinterprétés. Marges horizontales étroites et faible alpha périphérique conservés. Aucun effet d’explosion ni comportement moteur livré.

### Leech individuel — Gears 5

`creature_leech_g5` · SHA-256 `994a0a2dc12aaa65119ed85301ef1ef52920cf91dc6e52f583d100e873a8ad92`.

Un seul Leech complet, distinct de la formation Flock. La bouche est plus ouverte et le dos reste visible : la pose ne constitue pas un profil orthographique vérifié. Les petites dents et épines doivent être comparées. Marges horizontales d’environ 3–4 % et résidu alpha 1 au bord gauche.

### Wretch — modèle organique Gears of War: E-Day

`creature_wretch_eday` · SHA-256 `1515f872211b4722ca8eb2f990cf9c877682db92b6576c71f0149df5310d7c51`.

Version E-Day organique sans armure, corps entier, longues mains et pieds visibles. Vue trois-quarts droite ; détails postérieurs partiellement extrapolés faute de vue arrière. Alpha maximal natif 254, résidus alpha 1 périphériques ; RGB invisibles sous alpha 0 distingués d’un fond opaque.

### Ticker organique — Gears of War: E-Day

`creature_ticker_eday` · SHA-256 `ae7291da0c64bb5fc40de236f2f686d447da162ecab06334ccd68dac503ff03e`.

Uniquement le Ticker organique de la partie inférieure de la source, sans Reaver, bombe ni harnais. Corps entier, patte arrière éloignée partiellement masquée comme sur la référence. Marges utiles alpha > 8 : gauche 6,37 %, droite 6,31 %, haut 5,86 %, bas 3,95 % ; objectif 8 % non atteint. Résidus alpha 1 en haut et à gauche. Microdétails non certifiés.

## Reyna — sélection après deux éditions ciblées

La première édition visant les marges et l’alpha reste écartée : les marges ne sont pas corrigées et plusieurs détails sont repeints. La revue a ensuite identifié un rasage inversé sur le candidat initial. Une deuxième édition, limitée à cette correction de coiffure, rétablit la tempe droite couverte et est sélectionnée après comparaison au modèle officiel. Natte droite et tatouage gauche sont conservés ; visage, motifs, coutures et marges restent à valider. Les différences de pixels ne sont pas présentées comme une garantie 1:1.

Le [candidat initial](../../rejected_candidates/costumes_v14/reyna_human_g4_initial.png) et le [nettoyage écarté](../../rejected_candidates/costumes_v14/reyna_human_g4_clean.png) sont archivés hors actifs. Les trois journaux préservent [la génération initiale](revisions_v14/reyna_human_g4_initial_record.json), [l’édition alpha](revisions_v14/reyna_human_g4_clean_record.json) et [la correction de coiffure sélectionnée](revisions_v14/reyna_human_g4_hairfix_record.json). Trois sorties Reyna ne comptent que pour un PNG actif.

## Mina Jinn — refus enregistré

Le modèle final Gears of War 4 a été retrouvé et inspecté. L’unique tentative a été refusée par le générateur ; aucun PNG n’est attribué à Mina Jinn et aucun réessai n’est effectué. [Journal du refus](../../data/generation_v14/mina_jinn_g4_record.json).

## Lahni — deux appellations, un seul fichier

Le rapprochement **lahni_hivebusters_intro → lahni_skin_01** désigne la tenue Brash Brigade finale du début de Hivebusters. Il s’appuie sur le concept d’introduction et le modèle final, en privilégiant les manches courtes noires de la version finale. C’est une inférence documentée de catalogue ; le rapprochement ne certifie pas les détails du PNG. Les deux entrées partagent [le PNG V13](../../assets/costumes_v13/lahni_skin_01.png), avec les réserves historiques intactes. [Mapping](../../data/costume_reference_aliases_v14.json) · [Preuve](../../data/generation_v14/lahni_hivebusters_intro_record.json).

La tenue Escape reste distincte. L’alias potentiel Keegan intro n’est pas activé : sa cible Onyx Guard n’a pas de PNG après refus, et cette autre appellation ne sert pas à relancer la génération.

## Inventaire après consolidation

| Catégorie | Avec référence | Catalogue | Sans référence |
| --- | --- | --- | --- |
| Personnages | 51 | 57 | 6 |
| Costumes | 65 | 85 | 20 |
| Boss, créatures et machines | 30 | 34 | 4 |
| Stages | 34 | 34 | 0 |
| Projectiles | 5 | 9 | 4 |

**159 PNG actifs uniques + 17 archives**, sur **219 entrées de catalogue**. Les 35 manquants de départ ont été revus : Reyna est produite, Lahni intro reçoit son alias, 33 anciens manquants demeurent. Les cinq nouvelles entrées du catalogue comprennent quatre références et Mina Jinn sans image, soit **34 entrées sans référence au total**.

## Conception et contrôles

La [nouvelle annexe V14](CAST_AND_CREATURES_V14.md) précise les rôles proposés, la version humaine de Reyna et les créatures complémentaires. Elle ne modifie pas les 36 combattants du prototype. Les guides originaux, 68 rubriques et 40 cas d’acceptation restent conservés ; ces cas ne sont pas exécutés par la production d’images.

[Reprise et manquants](REPRISE_V14.md) · [Sources de recherche](../references/production-v14-research.md) · [Validation](VALIDATION_V14.json) · [Revue indépendante](REVIEW_V14.md).
