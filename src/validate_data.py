"""Validate cross-references and numeric contracts in the production bible."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'
errors=[];checks=[]
def read(n):return json.loads((DATA/(n+'.json')).read_text())
def require(condition,message):
 if not condition:errors.append(message)
def unique(rows,key,label):
 ids=[r[key] for r in rows];require(len(ids)==len(set(ids)),label+' duplicate identifiers');return set(ids)
roster=read('roster');moves=read('movesets');bosses=read('bosses');stages=read('stages');routes=read('arcade_routes');campaign=read('campaign')
chars=unique(roster,'id','Roster');bossids=unique(bosses,'id','Bosses');stageids=unique(stages,'id','Stages');unique(moves,'id','Moves')
unique(routes,'character_id','Routes');unique(campaign,'id','Campaign')
for c in roster:
 require(c['rival_id'] in chars,c['id']+' unknown rival')
 require(c['health']>0,c['id']+' invalid health')
for m in moves:
 require(m['character_id']=='universal' or m['character_id'] in chars,m['id']+' unknown character')
 for k in ['startup','active','recovery','damage','meter']:
  if m.get('kind')=='Exécution' and k!='meter':
   require(m[k] is None,m['id']+' execution should not claim combat '+k)
  else:
   require(isinstance(m[k],(int,float)) and m[k]>=0,m['id']+' invalid '+k)
for b in bosses:
 require(b['stage_id'] in stageids,b['id']+' unknown stage')
 require(len(b['phases'])==3,b['id']+' expected three documented phases')
 for p in b['phases']:
  require(p['telegraph_frames']>0 and p['punish_frames']>0,b['id']+' nonpositive timing')
for s in stages:
 require(len(s['layers'])==6,s['id']+' expected six layers')
 require(sum(l['collision'] for l in s['layers'])==1,s['id']+' expected one collision floor')
 require(not s['tournament_variant']['hazards'],s['id']+' tournament has hazards')
for route in routes:
 require(route['character_id'] in chars,route['character_id']+' unknown route character')
 for fight in route['route']:
  require(fight['opponent_id'] in chars|bossids,route['character_id']+' unknown opponent '+fight['opponent_id'])
for c in campaign:
 for b in c['boss_ids']:require(b in bossids,c['id']+' unknown boss '+b)
 for s in c['stage_ids']:require(s in stageids,c['id']+' unknown stage '+s)
plan=read('animation_plan')
require(sum(p['frames_per_orientation'] for p in plan)==552,'Animation frame estimate mismatch')
counts={'fighters':len(roster),'costume_records':sum(len(c['skins']) for c in roster),'moves':len(moves),'arcade_routes':len(routes),'combos':sum(len(r['combos']) for r in routes),'bosses':len(bosses),'boss_phases':sum(len(b['phases']) for b in bosses),'stages':len(stages),'parallax_layers':sum(len(s['layers']) for s in stages),'campaign_chapters':len(campaign),'animation_drawings_per_side':sum(p['frames_per_orientation'] for p in plan)}
report={'counts':counts,'checks':['Unique identifiers','Combatant and rival references','Movement ownership and nonnegative costs','Boss stage references and phase timings','Stage layers and tournament rules','Arcade opponents','Campaign stage and boss references','Animation estimate total'],'errors':errors,'status':'passed' if not errors else 'failed','limits':'Does not validate canonical visual fidelity, balance, or browser controls.'}
(ROOT/'docs/data_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
