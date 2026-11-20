"""Rebuild the complete consolidated manifest and refresh production queue entries.

Use this entry point for the current corpus. The former v1/v2-only manifest
builder would discard newer character and boss records.
"""
from pathlib import Path
import json
from consolidate_inventory import build_inventory

ROOT = Path(__file__).resolve().parents[1]
consolidation = build_inventory()
records = json.loads((ROOT / 'data/assets_manifest.json').read_text())
roster=json.loads((ROOT/'data/roster.json').read_text());stages=json.loads((ROOT/'data/stages.json').read_text());bosses=json.loads((ROOT/'data/bosses.json').read_text())
queue=[]
for c in roster:
 queue.append({'id':'anim_'+c['id'],'subject':c['name'],'category':'Animations du combattant','priority':c['priority'],'status':'À produire','dependency':'Référence de costume validée','units':1,'unit':'ensemble de clips','requirement':'Un personnage et une pose par fichier, pivots et hitboxes synchronisés, orientations distinctes si asymétrie'})
for b in bosses:
 queue.append({'id':'art_'+b['id'],'subject':b['name'],'category':'Boss et parties','priority':b['priority'],'status':'À produire','dependency':'Référence visuelle du jeu vérifiée','units':1,'unit':'ensemble de parties et animations','requirement':b['visual_risk']})
for s in stages:
 for l in s['layers']:
  queue.append({'id':'layer_'+l['id'],'subject':s['name']+' '+l['id'].split('_')[-1],'category':'Calque de parallaxe','priority':s['priority'],'status':'À produire','dependency':'Master et géométrie du stage validés','units':1,'unit':'image de calque','requirement':l['content']})
for c in roster:
 queue.append({'id':'ending_'+c['id'],'subject':c['name'],'category':'Illustration de fin','priority':'P1','status':'À produire','dependency':'Route arcade validée','units':1,'unit':'illustration','requirement':'Fin originale propre à la route, un épisode et une continuité clairement indiqués'})
(ROOT/'data/production_queue.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2))
print(json.dumps({'images':len(records),'queue_records':len(queue),'alpha_images':sum(r['has_transparency'] for r in records)},ensure_ascii=False))
