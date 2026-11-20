# Audit des rattachements de costumes — V7

Date : **20 novembre 2026**. État examiné : commit `a76973be5ad2b7f594de171e788a07394dcded41`.

## Résultat proposé

**34 rattachements explicites** peuvent être ajoutés entre des costumes existants et des PNG déjà présents. Les journaux désignent le même personnage et la même apparence / édition que la fiche du costume. Cette conclusion porte sur l’attribution d’une référence candidate ; elle ne certifie pas sa fidélité 1:1.

Le mapping proposé est [costume_asset_links_v7.json](../../data/costume_asset_links_v7.json). Chaque entrée fixe le chemin, le SHA-256, les identifiants de personnage et de costume, un journal existant, les URLs de provenance et les réserves. Aucun PNG, journal historique, catalogue ou inventaire n’a été modifié pour cet audit.

| Mesure | Avant rattachement | Après application des seuls 34 liens |
| --- | ---: | ---: |
| Costumes avec référence attribuée | 1 / 85 | 35 / 85 |
| Costumes sans référence attribuée | 84 | 50 |
| PNG personnages | 47 | 47 |
| PNG dédiés classés costume | 1 | 1 |
| PNG actifs / empreintes uniques | 56 / 56 | 56 / 56 |
| Fidélités 1:1 certifiées | 0 | 0 |

Les quatre références Del, Lizzie, Reyna et Skorge gardent leur statut **correction_required**. Les chiffres après application sont une projection de cet audit, avant toute nouvelle génération V7.

## Méthode et niveau de preuve

Les 85 fiches de costumes, les 47 entrées PNG de personnages et leurs journaux ont été rapprochés par identifiant explicite et édition. Les fichiers proposés ont été relus et leurs SHA-256 recalculés. Les sources ci-dessous sont les références déjà consignées dans les journaux, sans nouvelle vérification externe de chaque URL pendant cet audit. Les métadonnées et la QA prouvent la destination de la référence ; les réserves de ressemblance, de détails reconstruits et de cadrage restent applicables.

Les seules similitudes visuelles, les éditions non établies et les images de présentation ne suffisent pas à un rattachement. Une source générale de franchise dans une ancienne fiche de costume n’est pas traitée comme une preuve du costume : le journal de production précis et ses références sont prioritaires.

## Rattachements retenus

### 01. Dominic Santiago — Campagne Gears of War 2006

- Costume : `dom_skin_02` ; personnage : `dom`.
- PNG existant : [assets/characters_v5/dom_gow1_fullbody.png](../../assets/characters_v5/dom_gow1_fullbody.png).
- SHA-256 : `1c478f811a1a5001d757bd947ae95faf8439cbbdb20a9683eb0ce3b946cb3235`.
- Journal : [data/generation_v5/dom_record.json](../../data/generation_v5/dom_record.json).
- Justification : Le journal nomme explicitement l’armure CGU de Gears of War (2006).
- Statut à conserver : `candidate` ; variante déclarée : Gears of War (2006) — COG armor.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-of-war/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2026/04/gears-1-co-op-69d6e9d002b82.jpg).
- Réserves : Silhouette entière, deux mains et deux bottes visibles ; cheveux courts, barbe courte, armure COG sombre, lampes bleues et holster pectoral asymétrique conservés. Le RGB brut contient un voile sombre visible dans certains aperçus qui ignorent l'alpha ; le compositing blanc avec alpha produit un détourage visuellement propre.

### 02. Damon Baird — Campagne Gears of War 3

- Costume : `baird_skin_03` ; personnage : `baird`.
- PNG existant : [assets/characters_v2/baird_reference_v3.png](../../assets/characters_v2/baird_reference_v3.png).
- SHA-256 : `77db750641b2cae9423f7a2f216aaf2e23a0a89d112fc7176424a09c138d2c28`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/edit_baird_v3.json](../../data/generation_v2/edit_baird_v3.json).
- Justification : La correction V3 prend le key art Gears of War 3 et sa tenue de campagne sans manches comme référence.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 3.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-of-war-3/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2026/04/gears-of-war-3-69d7d9132411b-1024x576.jpg).
- Source consignée 3 : [référence](https://www.xbox.com/en-US/games/store/gears-3-baird-multiplayer-character/C54DHPZWRBV5).
- Réserves : Manches inventées retirées ; haut des bras conforme au visuel Gears 3. Petits panneaux, visage et marges avant animation à vérifier. Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.

### 03. Augustus Cole — Campagne Gears of War 3

- Costume : `cole_skin_02` ; personnage : `cole`.
- PNG existant : [assets/characters_v4/cole_reference_v4.png](../../assets/characters_v4/cole_reference_v4.png).
- SHA-256 : `132824804981ebcf0784e376c1fb378bb28547c6be064c99db0f593008284aa9`.
- Journal : [data/generation_v4/result_cole.json](../../data/generation_v4/result_cole.json).
- Justification : Le journal V4 identifie la tenue de campagne Gears of War 3, distincte de Thrashball et de Gears 5.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 3.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-of-war-3/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2026/04/gears-of-war-3-69d7d9132411b-1024x576.jpg).
- Source consignée 3 : [référence](https://news.xbox.com/en-us/2020/03/31/gears-5-operation-3-gridiron-available-today-for-all-players/).
- Réserves : Personnage unique entier, mains vides, pose neutre et orientation trois-quarts droite inspectées. Marge supérieure et marge sous les bottes très faibles : à reprendre avant animation.

### 04. Anya Stroud — Combat de campagne Gears of War 3

- Costume : `anya_skin_02` ; personnage : `anya`.
- PNG existant : [assets/characters/anya_stroud/gears3/reference_fullbody_v01.png](../../assets/characters/anya_stroud/gears3/reference_fullbody_v01.png).
- SHA-256 : `3971c9e39e6e4954361ac74944db42472ba78a6cfdda5d7b2a5fc747391205d3`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : Le journal sélectionne anya_stroud_gow3_stance : tenue de combat Gears of War 3.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 3.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-of-war-3/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2026/04/gears-3-co-op-69d7d90d192e5.jpg).
- Source consignée 3 : [référence](https://www.trueachievements.com/n4196/e3-2011-gears-of-war-3-campaign-screenshots).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Source individuelle tronquée ; jambes et bottes à confronter à une référence complète. Marge visible étroite : prévoir un canevas de production plus généreux.

### 05. Kait Diaz — Hiver Gears 5

- Costume : `kait_skin_02` ; personnage : `kait`.
- PNG existant : [assets/kait_neutral_cutout.png](../../assets/kait_neutral_cutout.png).
- SHA-256 : `1435d8506385ec4b97add0b61b1d75fc23e211f6f3c2a93cfe31e7594c5629ce`.
- Journal : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Justification : Le manifeste historique attribue explicitement ce détourage à Gears 5 hiver ; la présentation sur fond gris n’est pas réutilisée.
- Statut à conserver : `candidate` ; variante déclarée : Gears 5 hiver.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-5/).
- Réserves : Une pose, aucune animation, fidélité visuelle à contrôler Attribution de référence candidate uniquement : canonical_fidelity_validated=false, production_ready=false, animation_status=not_produced restent inchangés.

### 06. Général RAAM — Combat final Gears of War 2006

- Costume : `raam_skin_01` ; personnage : `raam`.
- PNG existant : [assets/characters_v5/raam_gow1_fullbody.png](../../assets/characters_v5/raam_gow1_fullbody.png).
- SHA-256 : `d5090cda44057420ff40438a3e3f8d18c94167b95e1bed83a04fc6b2bcd97f95`.
- Journal : [data/generation_v5/raam_record.json](../../data/generation_v5/raam_record.json).
- Justification : Le journal V5 cible le costume original GoW 2006 / portage PC original, en excluant Ultimate Edition des références d’entrée.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War (2006 / portage PC original).
- Source consignée 1 : [référence](https://models.spriters-resource.com/pc_computer/gearsofwar/asset/290796/).
- Source consignée 2 : [référence](https://models.spriters-resource.com/media/preview_icons/288/290796.png?updated=1755498012).
- Source consignée 3 : [référence](https://videogamesandthebible.com/2013/07/31/gears-of-war-and-the-bible-part-1-the-locust-horde/).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Une seule silhouette complète : tête, mains, pans de manteau, bottes visibles. Larges col et épaulières nervurés, cuirasse noire à boucles, bras pâles et long manteau fendu cohérents avec les références classiques.

### 07. Skorge — Palais Gears of War 2

- Costume : `skorge_skin_01` ; personnage : `skorge`.
- PNG existant : [assets/characters_v2/skorge_reference_v3.png](../../assets/characters_v2/skorge_reference_v3.png).
- SHA-256 : `a4a3d68b3a7b1598aaaea3c0cde50fbeb7d949304e2bbceed8f349c19d222012`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/edit_skorge_v3.json](../../data/generation_v2/edit_skorge_v3.json).
- Justification : La correction V3 utilise le modèle de campagne Gears of War 2 ; le résultat reste à corriger.
- Statut à conserver : `correction_required` ; variante déclarée : Gears of War 2.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-of-war-2/).
- Source consignée 2 : [référence](https://news.xbox.com/en-us/2020/11/17/gears-5-operation-5/).
- Source consignée 3 : [référence](https://gearsofwar.fandom.com/wiki/Skorge).
- Réserves : Conserver quality_state=correction_required ; le rattachement ne résout aucune correction visuelle connue. Plastron et abdomen améliorés. Casque encore nervuré horizontalement au lieu de la plaque frontale en V ; liens de tête encore plats.

### 08. Reine Myrrah — Armure royale Gears of War 3

- Costume : `myrrah_skin_01` ; personnage : `myrrah`.
- PNG existant : [assets/characters/myrrah/gears3/reference_fullbody_v01.png](../../assets/characters/myrrah/gears3/reference_fullbody_v01.png).
- SHA-256 : `8f24b38a127405822231481bb55fb33ec0cf111ebce552dad99680af89834a09`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : Le journal queen_myrrah_gow3_stance et le rendu promotionnel E3 2011 identifient l’armure royale GoW3.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 3.
- Source consignée 1 : [référence](https://www.trueachievements.com/n4196/e3-2011-gears-of-war-3-campaign-screenshots).
- Source consignée 2 : [référence](https://www.trueachievements.com/customimages/003248.jpg).
- Réserves : Source individuelle tronquée ; protections inférieures à vérifier. Marge visible étroite : prévoir un canevas de production plus généreux.

### 09. Drone locuste — Drone Gears of War 2006

- Costume : `locust_drone_skin_01` ; personnage : `locust_drone`.
- PNG existant : [assets/characters_v2/locust_drone_reference_v2.png](../../assets/characters_v2/locust_drone_reference_v2.png).
- SHA-256 : `e1ee3dca92be0150b70c7c5c2b600f881b8f131e01d3eaa8696ea9bd6adf7a3c`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/result_locust_drone.json](../../data/generation_v2/result_locust_drone.json).
- Justification : Le journal cible explicitement le Drone d’infanterie standard du Gears of War original (2006).
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 2006.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-of-war/).
- Source consignée 2 : [référence](https://news.xbox.com/en-us/2019/12/11/gears-5-operation-2-free-for-all-available-today-for-all-players/).
- Source consignée 3 : [référence](https://www.gearsofwar.com/en-us/news/dev-blog-enemies/).
- Réserves : Identité reconnaissable ; panneau par panneau, variante du Drone et correspondance au modèle de 2006 non certifiées. Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.

### 10. Kantus — Kantus Gears of War 2

- Costume : `kantus_skin_01` ; personnage : `kantus`.
- PNG existant : [assets/characters_v2/kantus_reference_v3.png](../../assets/characters_v2/kantus_reference_v3.png).
- SHA-256 : `85900a7d134c2c1731dd4a4eda09b7e85d4771e6c9bf3a8848a87d0319a7fa84`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/edit_kantus_v3.json](../../data/generation_v2/edit_kantus_v3.json).
- Justification : Le modèle original Gears of War 2 est prioritaire dans la correction V3 ; ce lien ne couvre pas le Kantus Tactics.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 2.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-of-war-2/).
- Source consignée 2 : [référence](https://www.gearsofwar.com/en-us/news/dev-blog-enemies/).
- Réserves : Casque, col, anneaux et pans corrigés. Jambes et pieds comparés à un concept, sans certification du modèle final. Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.

### 11. JD Fenix — CGU Gears 5 après ellipse

- Costume : `jd_skin_03` ; personnage : `jd`.
- PNG existant : [assets/characters_v2/jd_reference_v2.png](../../assets/characters_v2/jd_reference_v2.png).
- SHA-256 : `acfe1fb81543e98962767f46299f3362225429db810dee13fcab60c8b3a28fae`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/result_jd.json](../../data/generation_v2/result_jd.json).
- Justification : Le prompt et la QA précisent après ellipse / Scarred JD, partie Vasgar de Gears 5, et excluent le prologue.
- Statut à conserver : `candidate` ; variante déclarée : Gears 5.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-5/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2026/04/Accessibility_desktopBG-69d931f5a4c02-1024x570.jpg).
- Source consignée 3 : [référence](https://www.gearsofwar.com/fr-fr/news/gears-5-on-pc/).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Variante après ellipse et bras droit marqué reconnaissables ; détails du visage, des marques et attaches non certifiés. Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.

### 12. Del Walker — Campagne Gears 5

- Costume : `del_skin_02` ; personnage : `del`.
- PNG existant : [assets/characters_v2/del_reference_v3.png](../../assets/characters_v2/del_reference_v3.png).
- SHA-256 : `4b6ea5c768808e210a8ad85af8f1985406c3d78222b5a00170532d36e7e2f1bd`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/edit_del_v3.json](../../data/generation_v2/edit_del_v3.json).
- Justification : La correction V3 concerne Del dans sa tenue CGU de campagne Gears 5 ; le journal initial exclut la version hivernale.
- Statut à conserver : `correction_required` ; variante déclarée : Gears 5.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-5/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2026/04/desktop-campaign-3840x2160-69d932032874a-1024x576.jpg).
- Source consignée 3 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2026/04/Accessibility_desktopBG-69d931f5a4c02-1024x570.jpg).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Conserver quality_state=correction_required ; le rattachement ne résout aucune correction visuelle connue. Bretelles lumineuses améliorées. Les grilles doivent redevenir de petites ouvertures rectangulaires au milieu des plaques pectorales circulaires.

### 13. Fahz Chutani — Campagne Gears 5

- Costume : `fahz_skin_01` ; personnage : `fahz`.
- PNG existant : [assets/characters/fahz_chutani/gears5/reference_fullbody_v01.png](../../assets/characters/fahz_chutani/gears5/reference_fullbody_v01.png).
- SHA-256 : `b3f4e9742172264e361c6096cef970388f563e685a80196453ac2caca5ff872c`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : Le journal fahz_chutani_gears5 retient l’armure CGU bleue standard de campagne Gears 5.
- Statut à conserver : `candidate` ; variante déclarée : Gears 5.
- Source consignée 1 : [référence](https://www.uhdpaper.com/2019/08/gears-5-fahz-chutani-4k-567.html).
- Source consignée 2 : [référence](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgi_q09-XsGwF6cjdQhlkaZ1CuI97S9BYlJkPJFmKDS_ANEhQKpnZ5TZ3p2f8OoeuH0PiufIy5n9W8NlEau2uHwF7462bjfx_VezC9o_ClnDFFRSanTp_yyJ_Ix1dBKH8mP1zksjsYyDIg/w919/gears-5-fahz-chutani-uhdpaper.com-4K-5.67-wp.thumbnail.jpg).
- Réserves : Prothèse de la jambe droite conservée ; visage et détails du plastron limités par la définition de la capture. Attribution de référence candidate uniquement : canonical_fidelity_validated=false, production_ready=false, animation_status=not_produced restent inchangés.

### 14. Clayton Carmine — Campagne Gears of War 3

- Costume : `clayton_skin_01` ; personnage : `clayton`.
- PNG existant : [assets/characters/clayton_carmine/gears3/reference_fullbody_v02.png](../../assets/characters/clayton_carmine/gears3/reference_fullbody_v02.png).
- SHA-256 : `6c4ecae874cbbeba258863919d4be8338cc3f1c6f2f1ba4a01772db028887920`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : La sélection clayton_carmine_gears3_lettering_v02 corrige le marquage GRUB KILLER sur la tenue standard GoW3.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 3.
- Source consignée 1 : [référence](https://www.trueachievements.com/n4196/e3-2011-gears-of-war-3-campaign-screenshots).
- Source consignée 2 : [référence](https://www.trueachievements.com/customimages/003232.jpg).
- Réserves : Version v02 : inscription GRUB KILLER corrigée ; bottes et genouillères à vérifier avec une source complète. Marge visible étroite : prévoir un canevas de production plus généreux.

### 15. Lizzie Carmine — Campagne Gears 5

- Costume : `lizzie_skin_01` ; personnage : `lizzie`.
- PNG existant : [assets/characters_v2/lizzie_reference_v2.png](../../assets/characters_v2/lizzie_reference_v2.png).
- SHA-256 : `e8a46625126247982ea03ecb9fa4c2cc45cac4f21384c444e98c9ac19b3dddf3`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/result_lizzie.json](../../data/generation_v2/result_lizzie.json).
- Justification : Le journal V2 vise l’armure bleue régulière Gears 5 ; le candidat existant garde ses corrections requises.
- Statut à conserver : `correction_required` ; variante déclarée : Gears 5.
- Source consignée 1 : [référence](https://news.xbox.com/en-us/2019/12/11/gears-5-operation-2-free-for-all-available-today-for-all-players/).
- Source consignée 2 : [référence](https://bananachu.artstation.com/projects/QzZvxr?album_id=397336).
- Source consignée 3 : [référence](https://bananachu.artstation.com/resume).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Conserver quality_state=correction_required ; le rattachement ne résout aucune correction visuelle connue. Casque, optiques et col réinterprétés ; la correction demandée a été refusée par le système d’image. Version initiale conservée comme candidat.

### 16. Victor Hoffman — Hoffman en armure Gears 5

- Costume : `hoffman_skin_01` ; personnage : `hoffman`.
- PNG existant : [assets/characters_v4/hoffman_reference_v4.png](../../assets/characters_v4/hoffman_reference_v4.png).
- SHA-256 : `5349cae7484740521a710901c0429de1d0b3b8d170691c32f12af51d092a0e3f`.
- Journal : [data/generation_v4/result_hoffman.json](../../data/generation_v4/result_hoffman.json).
- Justification : Le journal V4 nomme Armored Hoffman, Gears 5 Operation 6, et fournit le lien boutique officiel ; le PNG classique non daté est exclu.
- Statut à conserver : `candidate` ; variante déclarée : Gears 5 multijoueur.
- Source consignée 1 : [référence](https://www.xbox.com/fr-fr/games/store/gears-5-operation-6-bundle/9nblc6fv6spg).
- Source consignée 2 : [référence](https://store-images.s-microsoft.com/image/apps.337.13510871565080275.ff765211-eed2-4e91-9d47-e587f251fce5.43d742b7-4c77-4394-997d-4364ddd0157a?h=265&q=90&w=177).
- Réserves : Personnage unique entier, homme âgé moustachu avec casquette, mains vides, orientation droite inspectés. Marge supérieure et marge sous les bottes trop faibles pour une base d’animation.

### 17. Tai Kaliso — Campagne Gears of War 2

- Costume : `tai_skin_01` ; personnage : `tai`.
- PNG existant : [assets/characters/tai_kaliso/gears2/reference_fullbody_v01.png](../../assets/characters/tai_kaliso/gears2/reference_fullbody_v01.png).
- SHA-256 : `212473ac370562619bdbc5cc062865185cbc28eb4d951f0a06858597ff83ba6a`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : Le journal tai_kaliso_gears2 utilise une capture GoW2 Xbox 360 et le concept contemporain pour la tenue du deuxième jeu.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 2.
- Source consignée 1 : [référence](https://www.mobygames.com/game/38697/gears-of-war-2/screenshots/xbox360/370298/).
- Source consignée 2 : [référence](https://cdn.mobygames.com/screenshots/16679907-gears-of-war-2-xbox-360-tai-kaliso-a-new-character-featured-in-t.png).
- Source consignée 3 : [référence](https://www.gamereactor.se/mer-fran-gears-of-war-2-14372/).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Visage et crête fondés sur une capture Gears 2 ; complément de silhouette issu du concept art, détails inférieurs à vérifier. Marge visible étroite : prévoir un canevas de production plus généreux.

### 18. Dizzy Wallin — Pilote Gears of War 2

- Costume : `dizzy_skin_01` ; personnage : `dizzy`.
- PNG existant : [assets/characters_v6/dizzy_gow2_fullbody.png](../../assets/characters_v6/dizzy_gow2_fullbody.png).
- SHA-256 : `8d9a5ead61a44d0ffa11518e3b656a364bc7624dd68b4ea02bf939af1dc0108a`.
- Journal : [data/generation_v6/dizzy_record.json](../../data/generation_v6/dizzy_record.json).
- Justification : Le journal V6 et le rendu presse de 2008 désignent le pilote GoW2, tenue de Betty.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 2 — tenue de pilote de Betty.
- Source consignée 1 : [référence](https://www.gamereactor.se/mer-fran-gears-of-war-2-14372/).
- Source consignée 2 : [référence](https://www.gamereactor.se/media/66/mergearswar_156693_650x.jpg).
- Réserves : Un personnage entier, chapeau, deux mains et deux bottes visibles. Chapeau brun usé, barbe grise, boucle dorée, bras tatoués, sangles, cartouches et plastron au crâne reconnaissables.

### 19. Samantha Byrne — Campagne Gears of War 3

- Costume : `sam_skin_01` ; personnage : `sam`.
- PNG existant : [assets/characters/samantha_byrne/gears3/reference_fullbody_v01.png](../../assets/characters/samantha_byrne/gears3/reference_fullbody_v01.png).
- SHA-256 : `54e2cde4d30e44455048c72b669bd8c3a764b61b6ff9488e4dcac9796a3498dd`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : La sélection samantha_byrne_gears3 utilise le rendu promotionnel E3 2011 de sa tenue de campagne GoW3.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 3.
- Source consignée 1 : [référence](https://www.trueachievements.com/n4196/e3-2011-gears-of-war-3-campaign-screenshots).
- Source consignée 2 : [référence](https://www.trueachievements.com/customimages/003236.jpg).
- Réserves : Source tronquée ; jambières et bottes à vérifier. Marge visible étroite : prévoir un canevas de production plus généreux.

### 20. Garron Paduk — Kilo Squad Judgment

- Costume : `paduk_skin_01` ; personnage : `paduk`.
- PNG existant : [assets/characters_v2/paduk_reference_v3.png](../../assets/characters_v2/paduk_reference_v3.png).
- SHA-256 : `96afca09c9ed49c47eaddd0cb3de63055e7d186506b98d7170b084bd7fac251c`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/edit_paduk_v3.json](../../data/generation_v2/edit_paduk_v3.json).
- Justification : Le journal initial précise Kilo Squad Judgment ; la correction V3 conserve cette tenue UIR.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War Judgment.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-gb/games/gears-of-war-judgment/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2026/04/gears-judgement-co-op-69d808161b80b.jpg).
- Source consignée 3 : [référence](https://www.maxon.net/es/article/creating-assets-for-epic-games-gears-of-war-judgment).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Armure Judgment corrigée à partir du visuel promotionnel. Teintes exactes et partie inférieure des bottes non établies par cette référence. Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.

### 21. Sofia Hendrik — Kilo Squad Judgment

- Costume : `sofia_skin_01` ; personnage : `sofia`.
- PNG existant : [assets/characters_v2/sofia_reference_v3.png](../../assets/characters_v2/sofia_reference_v3.png).
- SHA-256 : `89e683efac2ddbac0e0132d661065ecc2dc8f967a3101d9d2e2df3000b5b935b`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/edit_sofia_v3.json](../../data/generation_v2/edit_sofia_v3.json).
- Justification : La correction V3 prend sa tenue de cadette Onyx de Gears of War Judgment ; aucun transfert vers un autre opus.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War Judgment.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-gb/games/gears-of-war-judgment/).
- Source consignée 2 : [référence](https://chriswells.artstation.com/projects/qQbnL).
- Source consignée 3 : [référence](https://www.maxon.net/es/article/creating-assets-for-epic-games-gears-of-war-judgment).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Tenue Onyx et plastron corrigés. Visage, coiffure arrière et détourage à valider ; marge supérieure étroite avant préparation des sprites. Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.

### 22. Gabe Diaz — Tenue de base Gears Tactics

- Costume : `gabe_skin_01` ; personnage : `gabe`.
- PNG existant : [assets/characters/gabriel_diaz/tactics/reference_fullbody_v01.png](../../assets/characters/gabriel_diaz/tactics/reference_fullbody_v01.png).
- SHA-256 : `4a8b42d31cee4372c6003ac1b90393d711a64c03e554e282701b9990ff5f8b31`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : La sélection gabe_diaz_tactics prend le rendu officiel du blog des personnages Tactics pour sa tenue initiale.
- Statut à conserver : `candidate` ; variante déclarée : Gears Tactics.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/news/dev-blog-characters/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2020/04/f58127fb483b171065a9fad6b79ecbcfcf9032d5-69cb0c3a70b1e.jpg).
- Réserves : Référence officielle en pied disponible ; petits détails à revalider avant les animations. Attribution de référence candidate uniquement : canonical_fidelity_validated=false, production_ready=false, animation_status=not_produced restent inchangés.

### 23. Sid Redburn — Tenue de base Gears Tactics

- Costume : `sid_skin_01` ; personnage : `sid`.
- PNG existant : [assets/characters_v2/sid_reference_v3.png](../../assets/characters_v2/sid_reference_v3.png).
- SHA-256 : `41d3d01b0b9e621fae04e3ae97c88418884cd54bb2f45f143691c4ec38d993f0`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/edit_sid_v3.json](../../data/generation_v2/edit_sid_v3.json).
- Justification : Le journal V3 conserve la tenue par défaut Gears Tactics lors du retrait du fond.
- Statut à conserver : `candidate` ; variante déclarée : Gears Tactics.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-nz/news/dev-blog-characters/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2020/04/b070c2d094613f6ac28e09b19f87bc24cf487790-69cb0c5d1797f.jpg).
- Réserves : Version corrigée d’après le rendu officiel ; cache-œil anatomiquement gauche et pièces principales cohérents. Liserés de détourage à vérifier sur décor. Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.

### 24. Mikayla Dorn — Tenue de base Gears Tactics

- Costume : `mikayla_skin_01` ; personnage : `mikayla`.
- PNG existant : [assets/characters/mikayla_dorn/tactics/reference_fullbody_v01.png](../../assets/characters/mikayla_dorn/tactics/reference_fullbody_v01.png).
- SHA-256 : `7ff15814543f710d68f3f5c1f9c6a323eb77ab7ed3592be7af70ab5d4e7e5a47`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : La sélection mikayla_dorn_tactics utilise le rendu officiel de sa tenue initiale civile / milicienne.
- Statut à conserver : `candidate` ; variante déclarée : Gears Tactics.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/news/dev-blog-characters/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2020/04/fa96bb216cfb2950a825f30086ee5d6f05084c0c-69cb0c872baa9.jpg).
- Réserves : Référence officielle en pied disponible ; conserver les asymétries et les motifs du shemagh. Marge visible étroite : prévoir un canevas de production plus généreux.

### 25. Reine Reyna — Reine Reyna Gears 5

- Costume : `reyna_skin_01` ; personnage : `reyna`.
- PNG existant : [assets/characters_v2/reyna_reference_v3.png](../../assets/characters_v2/reyna_reference_v3.png).
- SHA-256 : `ca087379a9c9f1cb82eb8196eaf82a24c43b7c40be298a06c62f4fad1bdb9949`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/edit_reyna_v3.json](../../data/generation_v2/edit_reyna_v3.json).
- Justification : La correction V3 retient la Reine Reyna normale Gears 5 Operation 6 et exclut la variante Blood Red comme modèle de couleur.
- Statut à conserver : `correction_required` ; variante déclarée : Gears 5 multijoueur.
- Source consignée 1 : [référence](https://www.xbox.com/fr-fr/games/store/gears-5-operation-6-bundle/9nblc6fv6spg).
- Source consignée 2 : [référence](https://store.steampowered.com/news/posts/?appids=1097840&enddate=1616457409&feed=steam_community_announcements).
- Réserves : Conserver quality_state=correction_required ; le rattachement ne résout aucune correction visuelle connue. Cheveux, carapace et vrilles rétablis. Cristaux du front encore en arc de diadème au lieu de l’amas asymétrique ; bas du corps non documenté.

### 26. Lahni Kaliso — Tenue Escape Gears 5

- Costume : `lahni_skin_02` ; personnage : `lahni`.
- PNG existant : [assets/characters/lahni_kaliso/gears5_hivebuster/reference_fullbody_v01.png](../../assets/characters/lahni_kaliso/gears5_hivebuster/reference_fullbody_v01.png).
- SHA-256 : `6b3df7eeeb90d63278ccf21a675aede4977dda510af768fd49348464af142500`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : Le journal lahni_kaliso_hivebuster et la bio officielle identifient la tenue Scorpio standard / Escape ; aucun lien avec la tenue d’introduction Brash Brigade.
- Statut à conserver : `candidate` ; variante déclarée : Gears 5 — Hivebuster / Escape.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/news/hivebusters-graphic-novel-available-now/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2020/08/Hivebuster_Bios_Lahni_1080x1080-5f443f1966f5b-69cb11337f94d.png).
- Réserves : Tenue Hivebuster / Escape ; pieds non couverts par la fiche officielle, tatouages à contrôler en détail. Marge visible étroite : prévoir un canevas de production plus généreux.

### 27. Keegan — Campagne Hivebusters

- Costume : `keegan_skin_01` ; personnage : `keegan`.
- PNG existant : [assets/characters_v4/keegan_reference_v4.png](../../assets/characters_v4/keegan_reference_v4.png).
- SHA-256 : `120700af3f9126d700e0139eeaa1c0b8444d77837250949e8180309df804754d`.
- Journal : [data/generation_v4/result_keegan.json](../../data/generation_v4/result_keegan.json).
- Justification : Le journal V4 désigne explicitement la tenue Scorpio de campagne Hivebusters et exclut Onyx Guard.
- Statut à conserver : `candidate` ; variante déclarée : Gears 5 Hivebusters.
- Source consignée 1 : [référence](https://news.xbox.com/en-us/2020/12/08/gears-5-hivebusters-arrives-december-15/).
- Source consignée 2 : [référence](https://www.gearsofwar.com/en-us/news/hivebusters/).
- Source consignée 3 : [référence](https://www.gearsofwar.com/en-us/news/hivebusters-graphic-novel-available-now/).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Personnage entier en pose neutre, tête et bottes complètes, mains vides. Crâne chauve, rouflaquettes et moustache reliées, menton découvert, tenue beige/olive Scorpio et jambes matelassées présents.

### 28. Mac — Campagne Hivebusters

- Costume : `mac_skin_01` ; personnage : `mac`.
- PNG existant : [assets/characters_v4/mac_reference_v4.png](../../assets/characters_v4/mac_reference_v4.png).
- SHA-256 : `a08888becee515c6971948b9fd17fdbfc30589cb725854f6cd169ddf9b720f29`.
- Journal : [data/generation_v4/result_mac.json](../../data/generation_v4/result_mac.json).
- Justification : Le journal V4 identifie la tenue Scorpio standard de campagne Hivebusters et exclut expressément Mechanic Mac.
- Statut à conserver : `candidate` ; variante déclarée : Gears 5 Hivebusters.
- Source consignée 1 : [référence](https://news.xbox.com/en-us/2020/12/08/gears-5-hivebusters-arrives-december-15/).
- Source consignée 2 : [référence](https://www.gearsofwar.com/en-us/news/hivebusters/).
- Source consignée 3 : [référence](https://www.gearsofwar.com/en-us/news/hivebusters-graphic-novel-available-now/).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Personnage entier en pose neutre trois-quarts vers la droite, mains nues et vides, bottes entières. Cheveux roux relevés, visage rasé, chemise claire aux manches remontées, pendentif et gilet Scorpio présents.

### 29. JACK — JACK Gears 5

- Costume : `jack_skin_01` ; personnage : `jack`.
- PNG existant : [assets/characters_v2/jack_reference_v3.png](../../assets/characters_v2/jack_reference_v3.png).
- SHA-256 : `4ea029dd975eb71ea2cc54c2dbc944f6d2804ddd03063fe4fea117c79727a38f`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/edit_jack_v3.json](../../data/generation_v2/edit_jack_v3.json).
- Justification : La correction V3 reprend JACK sur une capture effective de Gears 5 ; le modèle Tactics est distinct.
- Statut à conserver : `candidate` ; variante déclarée : Gears 5.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-5/).
- Source consignée 2 : [référence](https://rizo.artstation.com/projects/BmWbJA).
- Source consignée 3 : [référence](https://mindwalkstudios.artstation.com/projects/oAle0O).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Capot et modules triangulaires corrigés. Orientation fine des modules, panneaux et configuration des outils encore à vérifier. Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.

### 30. DeeBee — Shepherd Gears of War 4

- Costume : `deebee_skin_01` ; personnage : `deebee`.
- PNG existant : [assets/characters_v4/deebee_reference_v4.png](../../assets/characters_v4/deebee_reference_v4.png).
- SHA-256 : `d269f5937c4ffc9d6415f8162b6c1002b615fe5cd87897e5fab58fe0b4cf834c`.
- Journal : [data/generation_v4/result_deebee.json](../../data/generation_v4/result_deebee.json).
- Justification : Le journal V4 identifie le Shepherd standard de Gears of War 4 ; ce lien ne remplit pas le DeeBee multijoueur Gears 5.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 4.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-of-war-4/).
- Source consignée 2 : [référence](https://primagames.com/eguides/gears-of-war-4-eguide/enemy-forces/deebees).
- Source consignée 3 : [référence](https://www.artstation.com/artwork/LJO50).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Un seul DeeBee, vue trois-quarts vers la droite, mains vides, tête et pieds entiers. Capteurs ambre et carénages bleu sombre, proportions générales reconnaissables.

### 31. Warden — Warden Gears 5

- Costume : `warden_skin_01` ; personnage : `warden`.
- PNG existant : [assets/characters/warden/gears5/reference_fullbody_v01.png](../../assets/characters/warden/gears5/reference_fullbody_v01.png).
- SHA-256 : `759348e4392a075c9511f2dfb11999b96f6fc0a9959315a9480f985de6213f5d`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : La sélection warden_gears5 utilise la capture en jeu Gears 5 pour le casque et une figurine licenciée comme complément anatomique.
- Statut à conserver : `candidate` ; variante déclarée : Gears 5.
- Source consignée 1 : [référence](https://steamcommunity.com/sharedfiles/filedetails/?id=2059243289&l=schinese).
- Source consignée 2 : [référence](https://images.steamusercontent.com/ugc/1011563720478551744/45834B6CC0151AF7851DC5DE8A4D74B94CD6CFE4/?ima=fit&imcolor=%23000000&imh=576&impolicy=Letterbox&imw=1024&letterbox=true).
- Source consignée 3 : [référence](https://www.gearsofwar.com/en-us/news/2020-gearsmas-holiday-gift-guide/).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Casque vérifié sur capture de jeu ; détail des deux Breaker Maces à revalider avec une capture rapprochée. Marge visible étroite : prévoir un canevas de production plus généreux.

### 32. Drone de l’Essaim — Drone Gears of War 4

- Costume : `swarm_drone_skin_01` ; personnage : `swarm_drone`.
- PNG existant : [assets/characters_v2/swarm_drone_reference_v2.png](../../assets/characters_v2/swarm_drone_reference_v2.png).
- SHA-256 : `e5988ddd8831be2962b7596f02cdb957d51230026cb41e35312dbc10f97340e0`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/result_swarm_drone.json](../../data/generation_v2/result_swarm_drone.json).
- Justification : Le journal V2 nomme le Drone Rifle standard de campagne Gears of War 4 ; Gears 5 et la variante UIR ne sont pas couverts.
- Statut à conserver : `candidate` ; variante déclarée : Gears of War 4.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/games/gears-of-war-4/).
- Source consignée 2 : [référence](https://haiweihou.artstation.com/projects/WrZXJ).
- Réserves : Swarm Drone reconnaissable ; équipement précis de la variante Rifle de Gears 4 à comparer au modèle du jeu. Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.

### 33. Ukkon — Campagne Gears Tactics

- Costume : `ukkon_skin_01` ; personnage : `ukkon`.
- PNG existant : [assets/characters/ukkon/tactics/reference_fullbody_v02.png](../../assets/characters/ukkon/tactics/reference_fullbody_v02.png).
- SHA-256 : `6f10e33e5195e8a950908a3b8aff5fc5a04b4a7bd82d8d2875e9120630fdf9d6`.
- Métadonnée de provenance enregistrée : [production/history/reprise_2026-11-19/production/asset_manifest.json](../../production/history/reprise_2026-11-19/production/asset_manifest.json).
- Journal complémentaire : [production/history/reprise_2026-11-19/production/generation_session.json](../../production/history/reprise_2026-11-19/production/generation_session.json).
- Justification : La sélection ukkon_tactics_rails_v02 corrige les longues structures d’épaule de la tenue finale Tactics documentée dans les blogs officiels.
- Statut à conserver : `candidate` ; variante déclarée : Gears Tactics.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/news/dev-blog-enemies/).
- Source consignée 2 : [référence](https://live.cdn.gearsofwar.com/gearsofwar/sites/3/2020/04/e3d6aae501363570c-69cb060527a2d.jpg).
- Source consignée 3 : [référence](https://www.gearsofwar.com/en-us/news/dev-blog-you-should-know/).
- Les autres URLs de provenance sont conservées dans le mapping JSON.
- Réserves : Version v02 : deux rails suspendus allongés vers les chevilles ; détails de la robe et des pieds à contrôler. Marge visible étroite : prévoir un canevas de production plus généreux.

### 34. Grenadier locuste — Grenadier Gears Tactics

- Costume : `grenadier_skin_01` ; personnage : `grenadier`.
- PNG existant : [assets/characters_v2/grenadier_reference_v2.png](../../assets/characters_v2/grenadier_reference_v2.png).
- SHA-256 : `5f52a802e772bd4eb5936df0eca5ee818b3686047d7df71992a84f10f909b438`.
- Métadonnée de provenance enregistrée : [production/history/initial_2026-11-19/assets_manifest.json](../../production/history/initial_2026-11-19/assets_manifest.json).
- Journal complémentaire : [data/generation_v2/result_grenadier.json](../../data/generation_v2/result_grenadier.json).
- Justification : Le journal V2 vise le Grenadier standard Gears Tactics au repos, et non la variante Gears of War 2006.
- Statut à conserver : `candidate` ; variante déclarée : Gears Tactics.
- Source consignée 1 : [référence](https://www.gearsofwar.com/en-us/news/dev-blog-enemies/).
- Source consignée 2 : [référence](https://store.steampowered.com/news/posts/?appgroupname=Gears+Tactics&appids=1184050&enddate=1588625128&feed=steam_community_announcements).
- Réserves : Grenadier reconnaissable ; grenades attachées au harnais acceptées, modèle et quantité exacts de la version Tactics à vérifier. Une pose neutre individuelle ; aucune animation finalisée ni arme tenue. La correspondance 1:1 reste à contrôler.

## Contrôle de provenance stricte — correction du mapping

Les **34 liens** ont été revérifiés après activation du contrôle du consolidateur : `source_record_path` appartient désormais dans chaque cas aux `metadata_records` déjà enregistrés pour le PNG. Pour **25 liens**, le journal détaillé de génération ne figurait pas dans cette liste historique : il est conservé dans `additional_evidence_paths`, tandis que la source principale pointe vers le manifeste historique enregistré. Ce manifeste contient le chemin exact du PNG, son identité, son édition et son SHA-256 concordant ; il ne s’agit pas d’ajouter une provenance nouvelle ou d’affaiblir le contrôle.

Les 34 chemins de PNG, les 34 empreintes, les parents de costumes et tous les fichiers de preuves principales et complémentaires ont été vérifiés. **Aucun lien retiré, aucun statut changé, aucune image modifiée.** Les journaux complémentaires explicitent notamment les distinctions de campagne / après ellipse ; ils ne remplacent jamais la preuve principale enregistrée.

## Associations refusées ou différées

| Sujet / demande | Décision et justification |
| --- | --- |
| Marcus : costumes 2006, GoW3, Gears 5, E-Day | Les deux PNG historiques sont identifiés Ultimate Edition. Aucun des quatre slots n’est couvert ; ne pas renommer UE en 2006. |
| Theron : `theron_skin_01` / 2006 | Le candidat V5 indique lui-même une édition exacte non validée : référence de jeu GoW2 et figurine licenciée. Le PNG historique est GoW3 sans casque. Aucun ne prouve l’édition 2006. |
| Theron : `theron_skin_02` / Tactics | Aucun PNG Tactics attesté. |
| Hoffman classique vers GoW3 ou Gears 5 | Le PNG classique est d’édition non établie. Seul le PNG V4 documenté Armored Hoffman Operation 6 est retenu pour le costume Gears 5. |
| JD prologue : `jd_skin_02` | Le PNG disponible est après ellipse ; seul `jd_skin_03` est rattaché. |
| Lahni campagne générique : `lahni_skin_01` | L’asset est identifié précisément Scorpio / Escape. Par prudence, seul `lahni_skin_02` est lié ; une clarification du slot campagne précède tout second lien. |
| `lahni_hivebusters_intro`, `keegan_hivebusters_intro`, Onyx Guard Keegan | Les images Scorpio standard ne couvrent pas Brash Brigade / Onyx Guard d’introduction ; aucun rattachement. |
| Mechanic Mac | Déjà lié à `mac_skin_02` par le PNG dédié V6. Le lien ajouté `mac_skin_01` utilise la référence standard V4, dont le prompt exclut Mechanic Mac. |
| Alicia Valera | PNG GoW3 RAAM’s Shadow, tandis que la fiche d’extension cible Gears 5 Operation 8 Drop 2 ; pas de slot costume GoW3 explicite à rattacher. Aucun faux transfert Gears 5. |
| Boomer Tactics | Référence de personnage disponible, mais aucun costume correspondant explicitement recensé dans les 85 slots. Aucun slot créé par cet audit. |
| V-Day Sam, Black Steel, Blood Red, UIR, Collector’s, Hivebuster Fahz | Aucune équivalence automatique avec les tenues de campagne des mêmes personnages. Ces variantes restent sans rattachement. |
| Versions E-Day et autres opus | Une tenue proche dans un autre jeu ne remplit pas le slot. Les sorties restées bloquées sans fichier ne sont jamais comptées. |

## Application technique proposée

Le consolidateur possède déjà le test `category == "costume" and asset.get("costume_id") == row["id"]` dans `make_coverage`. L’asset peut donc rester `category=character` et conserver son `subject_id` original tout en étant référencé par une fiche costume.

Charger le mapping **après `collect_assets` et avant `make_coverage`** ; sinon les anciens enregistrements V5/V6 peuvent écraser une annotation ajoutée trop tôt dans les seeds. Vérifier pour chaque lien : chemin unique et présent, SHA inchangé, costume connu, parent du costume égal au personnage de l’asset, absence d’un costume_id contradictoire. Ajouter uniquement `costume_id` et une trace de l’audit. Préserver exactement catégorie, identifiant de personnage, priorité de sélection, état de qualité et réserves. Ne jamais créer une seconde entrée asset ou recopier le PNG.

Les tests actuels couvrent le costume dédié et les parents invalides. Un test utile supplémentaire est un PNG personnage rattaché à un costume : le total PNG doit rester identique, les deux fiches doivent pointer vers le même chemin et le statut correction_required doit survivre. Tester aussi SHA erroné, parent différent et association concurrente contradictoire.

## Recherche des anciens fichiers encore hors corpus

37 chemins de sorties générées ont été extraits des journaux Gears existants et vérifiés sur disque : **37 correspondent par SHA-256 à un asset actif ou à une archive déjà intégrée ; 0 sortie supplémentaire et 0 chemin indisponible**. Les corpus antérieurs ciblés et les ZIP V1/V2 avaient déjà été rapprochés au cours de la récupération V6 : aucune image distincte supplémentaire. Les anciens scripts de reprise ne différaient que par une ligne vide finale. Aucun autre univers n’a été parcouru.

Cet audit et son mapping sont des fichiers de proposition. Leur intégration aux inventaires et à la PR doit être effectuée par la passe V7 ; aucune mutation GitHub n’a été faite ici.
