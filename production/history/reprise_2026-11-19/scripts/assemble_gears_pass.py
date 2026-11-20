from pathlib import Path
from PIL import Image
import json, hashlib, shutil
from collections import Counter
root=Path('/workspace/scratch/8b5a16f9fa4a/gear-of-wars-combats')
session_path=root/'production/generation_session.json'
session=json.loads(session_path.read_text())
revision=json.loads(Path('/workspace/scratch/8b5a16f9fa4a/ukkon_revision.json').read_text())
session['records']=[revision if r['character_id']=='ukkon' else r for r in session['records']]
session['attempts'].append({'key':revision['key'],'status':'generated','prompt':revision['prompt'],'reference_paths':revision['reference_paths'],'output_path':revision['source_path'],'failure':None})
records=session['records']
assert len(records)==20
assert Counter(r['status'] for r in records)=={'generated':14,'blocked':6}
old=root/'assets/characters/queen_myrrah'
new=root/'assets/characters/myrrah'
if old.exists() and not new.exists(): old.rename(new)
labels={'gears2':'Gears of War 2','gears3':'Gears of War 3','gears4':'Gears of War 4','gears5':'Gears 5','gears5_hivebuster':'Gears 5 — Hivebuster / Escape','tactics':'Gears Tactics','classic':'Armure classique'}
notes={
'anya_stroud':['Source individuelle tronquée ; jambes et bottes à confronter à une référence complète.'],
'myrrah':['Source individuelle tronquée ; protections inférieures à vérifier.'],
'theron_guard':['Variante Gears 3 sans casque ; ne pas la présenter comme une validation Gears 1.'],
'fahz_chutani':['Prothèse de la jambe droite conservée ; visage et détails du plastron limités par la définition de la capture.'],
'clayton_carmine':['Version v02 : inscription GRUB KILLER corrigée ; bottes et genouillères à vérifier avec une source complète.'],
'victor_hoffman':['Apparence classique ; édition native du rendu non établie, ne pas certifier Gears 2.'],
'tai_kaliso':['Visage et crête fondés sur une capture Gears 2 ; complément de silhouette issu du concept art, détails inférieurs à vérifier.'],
'samantha_byrne':['Source tronquée ; jambières et bottes à vérifier.'],
'gabriel_diaz':['Référence officielle en pied disponible ; petits détails à revalider avant les animations.'],
'mikayla_dorn':['Référence officielle en pied disponible ; conserver les asymétries et les motifs du shemagh.'],
'lahni_kaliso':['Tenue Hivebuster / Escape ; pieds non couverts par la fiche officielle, tatouages à contrôler en détail.'],
'mac_macallister':['Tenue Hivebuster / Escape ; partie inférieure des jambes reconstituée, non certifiée.'],
'warden':['Casque vérifié sur capture de jeu ; détail des deux Breaker Maces à revalider avec une capture rapprochée.'],
'ukkon':['Version v02 : deux rails suspendus allongés vers les chevilles ; détails de la robe et des pieds à contrôler.']}
assets=[]; selected={}
for r in records:
    if r['status']!='generated': continue
    src=Path(r['source_path'])
    assert src.is_file()
    rel=f"assets/characters/{r['character_id']}/{r['variant']}/reference_fullbody_v{r['revision']:02}.png"
    dst=root/rel; dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists():
        assert hashlib.sha256(dst.read_bytes()).digest()==hashlib.sha256(src.read_bytes()).digest()
    else: shutil.copy2(src,dst)
    with Image.open(dst) as im:
        im.load()
        assert im.format=='PNG' and im.mode=='RGBA'
        a=im.getchannel('A');hist=a.histogram();total=im.width*im.height
        assert hist[0]>0 and sum(hist[240:])>0
        bbox=a.point(lambda n:255 if n>=128 else 0).getbbox()
        margins=[bbox[0],bbox[1],im.width-bbox[2],im.height-bbox[3]]
        item={'character_id':r['character_id'],'name':r['name'],'variant':r['variant'],'variant_label':labels[r['variant']],'purpose':'reference_fullbody','path':rel,'revision':r['revision'],'generation_key':r['key'],'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'size_bytes':dst.stat().st_size,'width':im.width,'height':im.height,'mode':im.mode,'alpha':{'min':a.getextrema()[0],'max':a.getextrema()[1],'fully_transparent_fraction':round(hist[0]/total,6),'near_opaque_fraction_alpha_ge_240':round(sum(hist[240:])/total,6),'subject_bbox_alpha_ge_128':list(bbox),'subject_margins_ltrb_px':margins},'technical_status':'png_rgba_cutout_verified','canonical_fidelity_status':'candidate_requires_detailed_review','animation_status':'not_produced_in_this_pass','production_ready':False,'qa_notes':notes[r['character_id']]}
        if min(margins)<24:item['qa_notes'].append('Marge visible étroite : prévoir un canevas de production plus généreux.')
        assets.append(item); selected[r['key']]=rel
assert len(list((root/'assets/characters').rglob('*.png')))==len(assets)==14
manifest={'schema_version':'1.0','project':'Gears of War Combats','pass_date':'2026-11-19','counts':{'selected_character_references':14,'selected_png_files':14,'blocked_characters':6,'historical_characters_not_recovered':16,'roster_entries':36},'scope':'Références en pied candidates, un personnage par PNG. Aucune animation ou intégration moteur certifiée dans cette passe.','assets':assets}
(root/'production/asset_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
roster=json.loads((root/'production/roster.json').read_text())
byid={r['character_id']:r for r in records}; byasset={a['character_id']:a for a in assets}
for c in roster['characters']:
    if c['id'] not in byid:continue
    r=byid[c['id']];c['variant']=r['variant'];c['animation_status']='not_produced_in_this_pass'
    if c['id'] in byasset:
        a=byasset[c['id']];c.update(visual_status='generated_reference_candidate',asset_paths=[a['path']],notes=' '.join(a['qa_notes']))
    else:c.update(visual_status='generation_blocked',asset_paths=[],notes='Demande refusée par le système de sécurité du générateur (moderation_blocked, sortie). Aucun PNG produit dans cette passe.')
roster['scope_notes']=["Le roster couvre 36 personnages ; la disponibilité est vérifiée séparément pour chacun.","14 références en pied sont présentes et vérifiées dans cette passe ; aucune n'est une animation finalisée.","6 personnages restent sans nouveau PNG après refus du générateur.","Les 16 anciens visuels restent une information historique ; leurs fichiers n'ont pas été récupérés ni publiés par cette passe.","Une identité reconnaissable et un PNG transparent ne suffisent pas à certifier une fidélité canonique intégrale 1:1."]
roster['current_pass_counts']=dict(Counter(c['visual_status'] for c in roster['characters']))
(root/'production/roster.json').write_text(json.dumps(roster,ensure_ascii=False,indent=2)+'\n')
def failure(f):
    return {'code':'moderation_blocked','stage':'output','message':'Generation refused by image safety system; no output image returned.'} if f else None
for r in session['records']:
    r.pop('source_path',None);r['selected_asset_path']=selected.get(r['key']);r['failure']=failure(r.get('failure'))
for a in session['attempts']:
    a['selected_asset_path']=selected.get(a['key']);a['is_selected']=a['key'] in selected;a.pop('output_path',None);a['failure']=failure(a.get('failure'))
session['counts']={'initial_character_requests':20,'correction_requests':3,'all_requests':23,'successful_outputs_including_revisions':17,'blocked_requests':6,'selected_character_images':14}
session['reference_path_note']="Les chemins de références temporaires servent à identifier les entrées utilisées. Pour les retrouver durablement, utiliser les URL dans production/references/."
session_path.write_text(json.dumps(session,ensure_ascii=False,indent=2)+'\n')
(root/'.gitattributes').write_text('*.png binary\n*.json text eol=lf\n*.md text eol=lf\n')
(root/'.gitignore').write_text('__pycache__/\n*.pyc\n.DS_Store\n')
assert len({c['id'] for c in roster['characters']})==36
assert len({a['sha256'] for a in assets})==14
assert all((root/p).is_file() for c in roster['characters'] for p in c['asset_paths'])
print(json.dumps({'selected_png':len(assets),'total_bytes':sum(a['size_bytes'] for a in assets),'roster_states':roster['current_pass_counts'],'all_sha256_verified':True,'all_asset_paths_exist':True},ensure_ascii=False))
