import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const outputDir = process.env.GEARS_OUTPUT_DIR || path.resolve(root, '../outputs/gears_combats_v1');
const outputFilename = process.env.GEARS_OUTPUT_FILENAME || 'Gears_of_War_Combats_Production.xlsx';
const qaDir = process.env.GEARS_QA_DIR || path.resolve(root, '../tmp/qa/workbook');
const qaSheets = process.env.GEARS_QA_SHEETS
  ? new Set(process.env.GEARS_QA_SHEETS.split(',').map(name => name.trim()).filter(Boolean))
  : null;
await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(qaDir, { recursive: true });
const read = async name => JSON.parse(await fs.readFile(path.join(root, 'data', `${name}.json`), 'utf8'));
const [roster, moves, routes, bosses, stages, campaign, animations, manifest, production] = await Promise.all(['roster', 'movesets', 'arcade_routes', 'bosses', 'stages', 'campaign', 'animation_plan', 'assets_manifest', 'production_queue'].map(read));
const names = Object.fromEntries(roster.map(r => [r.id, r.name]));
const combos = routes.flatMap(r => r.combos.map(c => ({...c, character_id:r.character_id})));
const costumes = roster.flatMap(r => r.skins.map(s => ({...s, character_id:r.id, character:r.name})));
const phases = bosses.flatMap(b => b.phases.map(p => ({...p, boss_id:b.id, boss:b.name})));
const layers = stages.flatMap(s => s.layers.map(l => ({...l, stage_id:s.id, stage:s.name})));
const rows = {};
const wb = Workbook.create();
const summary = wb.worksheets.add('Synthèse');
const sheetNames = ['Production','Roster','Costumes','Mouvements','Combos','Routes arcade','Boss','Phases boss','Stages','Calques','Campagne','Animations','Assets'];
for (const name of sheetNames) wb.worksheets.add(name);
const steel = '#283746';
const pale = '#EFF3F6';
const amber = '#FFF1CC';
const blue = '#1F4E78';
const col = index => { let x=index+1, s=''; while(x){x--;s=String.fromCharCode(65+x%26)+s;x=Math.floor(x/26);} return s; };
const clean = x => x===undefined ? null : Array.isArray(x) ? x.join('\n') : x;

function sheetTable(name,title,headers,data,widths,opts={}){
  const sh=wb.worksheets.getItem(name);
  const last=col(headers.length-1), end=5+data.length;
  sh.showGridLines=false;
  const used=sh.getRange(`A1:${last}${end}`);
  used.format.font={name:'Arial',size:11,color:'#171D24'};
  used.format.verticalAlignment='center';
  sh.getRange('A2').values=[[title]];
  sh.getRange('A2').format.font={name:'Arial',size:15,bold:true,color:'#000000'};
  sh.getRange(`A2:${last}2`).format.rowHeight=25;
  sh.getRange(`A3:${last}3`).format.rowHeight=20;
  if(opts.note){sh.getRange('A3').values=[[opts.note]];sh.getRange('A3').format.font={name:'Arial',size:10,italic:true,color:'#465768'};}
  sh.getRange(`A4:${last}4`).format.borders={preset:'doubleBottom',style:'thin',color:'#CCD4DC'};
  sh.getRange(`A5:${last}${end}`).values=[headers,...data.map(row=>row.map(clean))];
  const table=sh.tables.add(`A5:${last}${end}`,true,`T_${name.normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-zA-Z0-9]/g,'')}`);
  table.showFilterButton=true;
  sh.getRange(`A5:${last}5`).format={fill:steel,font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},wrapText:true,verticalAlignment:'center',horizontalAlignment:'center',rowHeight:36};
  sh.getRange(`A5:${last}5`).format.borders={preset:'inside',style:'thin',color:'#FFFFFF'};
  if(data.length){
    sh.getRange(`A6:${last}${end}`).format.wrapText=true;
    for(let i=0;i<data.length;i++){
      const rr=i+6;
      const maxLines=Math.max(1,...data[i].map((raw,j)=>{const v=clean(raw);return typeof v==='string' ? v.split('\n').reduce((n,line)=>n+Math.max(1,Math.ceil(line.length/Math.max(7,widths[j]-3))),0) : 1;}));
      sh.getRange(`A${rr}:${last}${rr}`).format.rowHeight=Math.max(32,Math.min(220,maxLines*14+10));
      sh.getRange(`A${rr}:${last}${rr}`).format.fill=i%2?pale:'#FFFFFF';
    }
  }
  widths.forEach((w,j)=>{sh.getRange(`${col(j)}1:${col(j)}${end}`).format.columnWidth=w;});
  for(const j of opts.numeric??[]){sh.getRange(`${col(j)}6:${col(j)}${end}`).setNumberFormat('0_ ');sh.getRange(`${col(j)}6:${col(j)}${end}`).format.horizontalAlignment='right';sh.getRange(`${col(j)}6:${col(j)}${end}`).format.borders={right:{style:'thin',color:'#CCD4DC'}};}
  for(const j of opts.decimal??[]){sh.getRange(`${col(j)}6:${col(j)}${end}`).setNumberFormat('0.00_ ');sh.getRange(`${col(j)}6:${col(j)}${end}`).format.horizontalAlignment='right';sh.getRange(`${col(j)}6:${col(j)}${end}`).format.borders={right:{style:'thin',color:'#CCD4DC'}};}
  for(const j of opts.editable??[]){sh.getRange(`${col(j)}6:${col(j)}${end}`).format.fill=amber;}
  sh.freezePanes.freezeRows(5);
  sh.freezePanes.freezeColumns(Math.min(2,headers.length));
  rows[name]={end,count:data.length,cols:headers.length};
  return sh;
}

const productionSheet=sheetTable('Production','File de production',
 ['ID tâche','Sujet','Catégorie','Priorité','Quantité','Unité','Dépendance','Exigence','Statut'],
 production.map(p=>[p.id,p.subject,p.category,p.priority,p.units,p.unit,p.dependency,p.requirement,p.status]),
 [32,33,34,12,12,27,62,92,27],
 {note:'Le statut suit la production réelle. Les ensembles de clips ne sont pas comptés comme des dessins individuels.',numeric:[4],editable:[8]});
productionSheet.getRange(`I6:I${rows.Production.end}`).dataValidation={rule:{type:'list',values:['À produire','En cours','Généré à contrôler','À corriger','Validé','Intégré']}};

sheetTable('Roster','Roster de production',
 ['ID','Personnage','Lot','Épisode de référence','Costume de base','Archétype','Mécanique propre','Armes prévues','État de réalisation','État artistique','Fichier de référence','Source du corpus','Portée de la source'],
 roster.map(r=>[r.id,r.name,r.tier,r.source_game,r.base_costume,r.archetype,r.gimmick,r.weapons,r.implementation_status,r.art_status,r.base_reference_path??null,r.source_url,r.source_scope]),
 [23,25,18,26,42,33,66,37,48,48,62,60,68],
 {note:'Personnages de la franchise. Kits, statistiques et scènes créés pour cette adaptation 2D.'});

sheetTable('Costumes','Costumes et variantes',
 ['ID variante','Personnage','Variante précise','État de référence','Règle de gameplay','Règle d’image','Source du corpus'],
 costumes.map(s=>[s.id,s.character,s.name,s.status,s.gameplay,s.asset_rule,s.source_url]),
 [25,24,44,52,46,48,68],
 {note:'75 fiches de variantes. Une fiche de costume ne prouve pas qu’un sprite a été produit.'});

sheetTable('Mouvements','Mouvements et frame data',
 ['ID action','Personnage','Type','Action','Commande','Départ','Actives','Récup.','Dégâts','Garde','Contact','Jauge','Ressource','Description','Annulations'],
 moves.map(m=>[m.id,names[m.character_id]??'Universel',m.kind,m.name,m.input,m.startup,m.active,m.recovery,m.damage,m.block_adv,m.hit_adv,m.meter,m.resource,m.description,m.cancel]),
 [25,23,16,34,24,10,10,10,10,10,10,10,24,84,52],
 {note:'Frames à 60 Hz. Toutes les valeurs sont des propositions de balance. Cellule vide = sans objet ou variable.',numeric:[5,6,7,8,9,10,11]});

sheetTable('Combos','Combos du noyau',
 ['ID combo','Personnage','Notation','Coût jauge','Dégâts estimés','Autre ressource','Preuve temporelle','Portée requise','État de validation'],
 combos.map(c=>[c.id,names[c.character_id],c.notation,c.meter_cost,c.damage_estimate,c.action_resource,c.proof,c.range,c.status]),
 [27,24,28,13,16,50,92,66,64],
 {note:'> liaison après récupération. xx annulation. Estimations sans bonus de rechargement.',numeric:[3,4]});

sheetTable('Routes arcade','Routes arcade individuelles',
 ['ID personnage','Personnage','Rival','Introduction originale','Réplique originale','Scène de rivalité','Fin originale','Ordre des huit combats','Récompense'],
 routes.map(r=>[r.character_id,r.name,names[r.rival_id],r.intro_scene,r.intro_line_original,r.rival_scene,r.ending,r.route.map(s=>`${s.step}. ${s.kind}: ${names[s.opponent_id]??s.opponent_id}`).join('\n'),r.reward]),
 [24,24,24,62,56,67,82,48,60],
 {note:'Arcade hors continuité. Cinq duels, rival, Boss Battle, duel final, puis ending séparé.'});

sheetTable('Boss','Catalogue des boss',
 ['ID boss','Boss','Type','Épisode','Stage','Ratio de cadrage','Parties ciblables','Victoire','Règles solo','État de réalisation','Sources','Portée canonique'],
 bosses.map(b=>[b.id,b.name,b.nature,b.source_game,b.stage_id,b.gameplay_scale_human_height,b.targetable_parts,b.victory,b.solo_rules,b.content_status,b.source_urls,b.canon_scope]),
 [25,25,25,26,30,17,66,80,88,48,75,75],
 {note:'Ratios, phases, seuils et timings créés pour la 2D. Véhicules alliés opposés en simulation.',decimal:[5]});

sheetTable('Phases boss','Phases et réponses aux attaques',
 ['ID boss','Boss','Phase','Vie du boss','Nom de phase','Signal visuel ou sonore','Anticipation frames','Attaque','Réponse du joueur','Ouverture frames'],
 phases.map(p=>[p.boss_id,p.boss,p.index,p.hp_band,p.name,p.telegraph,p.telegraph_frames,p.attack,p.counterplay,p.punish_frames]),
 [26,26,9,16,30,84,17,84,92,17],
 {note:'72 phases spécifiées. Les fenêtres sont des réglages de conception à 60 Hz.',numeric:[2,6,9]});

sheetTable('Stages','Arènes et ambiances',
 ['ID stage','Arène','Épisode','Moment de la journée','Repère principal','Palette','Formats','Priorité','État des calques','Variante spectacle','Sources'],
 stages.map(s=>[s.id,s.name,s.source_game,s.time_of_day,s.signature_landmark,s.palette,s.formats,s.priority,s.content_status,s.spectacle_variant,s.source_urls]),
 [27,32,27,27,61,40,18,10,50,86,80],
 {note:'24 compositions à produire. La version tournoi garde un sol constant et désactive les dangers.'});

sheetTable('Calques','Calques de parallaxe',
 ['ID calque','Arène','Plan Z','Parallaxe X','Parallaxe Y','Alpha requis','Collision','Contenu','Fichier cible','Statut'],
 layers.map(l=>[l.id,l.stage,l.z,l.parallax_x,l.parallax_y,l.alpha?'Oui':'Non',l.collision?'Oui':'Non',l.content,l.file,l.status]),
 [35,33,10,14,14,14,13,76,72,23],
 {note:'Six plans par stage. Les VFX de premier plan sont gérés séparément par le moteur.',numeric:[2],decimal:[3,4],editable:[9]});
const layerSheet=wb.worksheets.getItem('Calques');
layerSheet.getRange(`J6:J${rows.Calques.end}`).dataValidation={rule:{type:'list',values:['À générer','Généré à contrôler','À corriger','Validé','Intégré']}};

sheetTable('Campagne','Chapitres de campagne',
 ['ID chapitre','Ordre','Chapitre','Épisode','Personnages autorisés','Stages','Boss','Rival','Introduction originale','Scène du rival','Fin originale','Garde de continuité','Sources'],
 campaign.map(c=>[c.id,c.order,c.title,c.source_game,c.playable_characters,c.stage_ids,c.boss_ids,c.rival,c.intro_original,c.rival_scene_original,c.ending_original,c.canon_guard,c.source_urls]),
 [24,10,35,29,45,38,30,24,100,100,100,96,80],
 {note:'Anthologie en douze chapitres. Dialogues et mise en scène originaux pour cette adaptation.',numeric:[1]});

const animationSheet=sheetTable('Animations','Budget de dessins par combattant',
 ['État','Famille','Dessins par sens','Sens','Costumes','Dessins prévus','Dessins validés','Dessins restants','Avancement','Statut calculé','Détail du budget'],
 animations.map(a=>[a.id,a.family,a.frames_per_orientation,a.orientations,a.costumes,null,a.produced_frames,null,null,null,a.note]),
 [25,24,18,10,12,18,18,18,16,26,80],
 {note:'Budget pour un combattant et un costume. Un dessin distinct ne correspond pas à une frame de simulation.',numeric:[2,3,4,5,6,7],editable:[2,3,4,6]});
for(let i=0;i<animations.length;i++){
  const rr=i+6;
  animationSheet.getRange(`F${rr}`).formulas=[[`=C${rr}*D${rr}*E${rr}`]];
  animationSheet.getRange(`H${rr}`).formulas=[[`=MAX(0,F${rr}-G${rr})`]];
  animationSheet.getRange(`I${rr}`).formulas=[[`=IF(F${rr}=0,"n.a.",G${rr}/F${rr})`]];
  animationSheet.getRange(`J${rr}`).formulas=[[`=IF(G${rr}>F${rr},"Quantité à vérifier",IF(G${rr}=F${rr},"Complet",IF(G${rr}=0,"À produire","En cours")))`]];
}
animationSheet.getRange(`I6:I${rows.Animations.end}`).setNumberFormat('0.0%');
animationSheet.getRange(`J6:J${rows.Animations.end}`).conditionalFormats.add('containsText',{text:'vérifier',format:{fill:'#FCE1DD',font:{bold:true,color:'#8B1E13'}}});
for(const c of ['C','D','E','G'])animationSheet.getRange(`${c}6:${c}${rows.Animations.end}`).dataValidation={rule:{type:'whole',operator:'between',formula1:0,formula2:100000}};

async function walkAssets(dir){
  let result=[];
  for(const entry of await fs.readdir(dir,{withFileTypes:true})){
    const file=path.join(dir,entry.name);
    if(entry.isDirectory())result.push(...await walkAssets(file));
    else if(/\.(png|jpg|jpeg|webp)$/i.test(entry.name))result.push(file);
  }
  return result;
}
const imagePaths=(await walkAssets(path.join(root,'assets'))).sort();
const assetRows=[];
for(const [i,file] of imagePaths.entries()){
  const data=await fs.readFile(file);
  const png=data.length>24 && data[0]===137 && data.subarray(1,4).toString()==='PNG';
  const relative=path.relative(root,file);
  const meta=manifest.find(m=>m.path===relative);
  const alphaRequired=meta?.alpha_required ?? /cutout|détour|detour|sprite/i.test(`${meta?.category??''} ${relative}`);
  const actualAlpha=meta?.has_transparency ?? false;
  const technicalCheck=String(meta?.technical_check??'');
  const tech=/à corriger/i.test(technicalCheck)?'À corriger'
    : /à contrôler|à valider|non contrôlé|non validé/i.test(technicalCheck)?'À contrôler'
    : /validé|contrôlé/i.test(technicalCheck)?'Validé':'À contrôler';
  const fidelity=['À valider','À contrôler','À corriger','Validé'].includes(meta?.fidelity_check)
    ? meta.fidelity_check : 'À valider';
  const integrated=meta?.integration_check?.startsWith('Intégré')?'Intégré':'À intégrer';
  assetRows.push([meta?.id??`image_${String(i+1).padStart(3,'0')}`,relative,png?data.readUInt32BE(16):null,png?data.readUInt32BE(20):null,Math.round(data.length/1024),'Généré',tech,fidelity,integrated,null,meta?.category??'Image',actualAlpha?'Oui':'Non',alphaRequired?'Oui':'Non',meta?.limitations??'Contrôle de référence à réaliser']);
}
const assetSheet=sheetTable('Assets','Images réellement livrées',
 ['ID image','Fichier livré','Largeur px','Hauteur px','Taille Kio','Existence','Contrôle technique','Fidélité à la référence','Intégration','Statut calculé','Catégorie','Alpha observé','Alpha requis','Limites du fichier'],
 assetRows,[25,58,15,15,15,19,28,30,26,40,30,16,16,80],
 {note:'Une image générée reste à contrôler. Les animations complètes et les six calques ne sont pas déduits d’une seule pose.',numeric:[2,3,4],editable:[6,7,8]});
for(let i=0;i<assetRows.length;i++){
  const rr=i+6;
  assetSheet.getRange(`J${rr}`).formulas=[[`=IF(AND(F${rr}="Généré",G${rr}="Validé",H${rr}="Validé",I${rr}="Intégré",OR(M${rr}="Non",L${rr}="Oui")),"Validé et intégré","Contrôles ou intégration requis")`]];
}
assetSheet.getRange(`G6:G${rows.Assets.end}`).dataValidation={rule:{type:'list',values:['À contrôler','À corriger','Validé']}};
assetSheet.getRange(`H6:H${rows.Assets.end}`).dataValidation={rule:{type:'list',values:['À valider','À contrôler','À corriger','Validé']}};
assetSheet.getRange(`I6:I${rows.Assets.end}`).dataValidation={rule:{type:'list',values:['À intégrer','Intégré']}};

summary.showGridLines=false;
summary.tabColor=steel;
summary.getRange('A1:H36').format.font={name:'Arial',size:11,color:'#171D24'};
summary.getRange('A1:H36').format.verticalAlignment='center';
summary.getRange('A1:H36').format.rowHeight=24;
summary.getRange('A1:A36').format.columnWidth=43;
summary.getRange('B1:B36').format.columnWidth=15;
summary.getRange('C1:C36').format.columnWidth=15;
summary.getRange('D1:D36').format.columnWidth=5;
summary.getRange('E1:E36').format.columnWidth=44;
summary.getRange('F1:F36').format.columnWidth=18;
summary.getRange('G1:H36').format.columnWidth=15;
summary.getRange('A2').values=[['Gears of War Combats']];
summary.getRange('A2').format.font={name:'Arial',size:16,bold:true,color:'#000000'};
summary.getRange('A3').values=[['Production au 19 novembre 2026']];
summary.getRange('A3').format.font={name:'Arial',size:10,color:'#465768'};
summary.getRange('A4:F4').format.borders={preset:'doubleBottom',style:'thin',color:'#CCD4DC'};
summary.getRange('A5:C5').values=[['Contenu spécifié','Nombre','Unité']];
summary.getRange('E5:F5').values=[['Réalisation observée','Nombre']];
for(const range of ['A5:C5','E5:F5','A23:C23','E23:F23'])summary.getRange(range).format={fill:steel,font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:32,wrapText:true,verticalAlignment:'center'};
const summaryRows=[['Combattants','Roster','fiches'],['Costumes','Costumes','variantes'],['Actions de combat','Mouvements','actions'],['Combos du noyau','Combos','routes'],['Routes arcade','Routes arcade','parcours'],['Boss','Boss','rencontres'],['Phases de boss','Phases boss','phases'],['Stages','Stages','arènes'],['Calques de parallaxe','Calques','calques'],['Chapitres histoire','Campagne','chapitres']];
summaryRows.forEach(([label,sh,unit],i)=>{
  const rr=i+6;
  summary.getRange(`A${rr}:C${rr}`).values=[[label,null,unit]];
  summary.getRange(`B${rr}`).formulas=[[`=COUNTA('${sh}'!A6:A5000)`]];
  if(i%2)summary.getRange(`A${rr}:C${rr}`).format.fill=pale;
});
summary.getRange('E6:E12').values=[['Images générées présentes'],['Images avec contrôle technique validé'],['Images avec fidélité validée'],['Images intégrées'],['Images avec tous les contrôles'],['Calques générés à contrôler'],['Calques validés ou intégrés']];
summary.getRange('F6:F12').formulas=[['=COUNTA(Assets!A6:A5000)'],['=COUNTIFS(Assets!G6:G5000,"Validé")'],['=COUNTIFS(Assets!H6:H5000,"Validé")'],['=COUNTIFS(Assets!I6:I5000,"Intégré")'],['=COUNTIFS(Assets!J6:J5000,"Validé et intégré")'],['=COUNTIFS(Calques!J6:J5000,"Généré à contrôler")'],['=COUNTIFS(Calques!J6:J5000,"Validé")+COUNTIFS(Calques!J6:J5000,"Intégré")']];
summary.getRange('E14:E15').values=[['Entrées de production'],['Priorités P0 à intégrer']];
summary.getRange('F14:F15').formulas=[['=COUNTA(Production!A6:A5000)'],['=COUNTIFS(Production!D6:D5000,"P0",Production!I6:I5000,"<>Intégré")']];
summary.getRange('E6:E12').format.wrapText=true;
summary.getRange('E6:F12').format.rowHeight=35;
summary.getRange('A18').values=[['Les quantités de conception ne sont pas des quantités de contenu jouable.']];
summary.getRange('A19').values=[['Les cases ambre accueillent les mises à jour de production et les validations.']];
summary.getRange('A20').values=[['Le prototype livré couvre un sous-ensemble. Les autres actions restent à implémenter.']];
summary.getRange('A18:F20').format.font={name:'Arial',size:10,color:'#465768'};
summary.getRange('A23:C23').values=[['Budget de dessins','Nombre','Périmètre']];
summary.getRange('A24:A28').values=[['Dessins prévus'],['Dessins validés'],['Dessins restants'],['Avancement du gabarit'],['États et familles d’actions']];
summary.getRange('B24:B28').formulas=[['=SUM(Animations!F6:F5000)'],['=SUM(Animations!G6:G5000)'],['=SUM(Animations!H6:H5000)'],['=IF(B24=0,"n.a.",B25/B24)'],['=COUNTA(Animations!A6:A5000)']];
summary.getRange('C24:C28').values=[['1 combattant'],['1 combattant'],['1 combattant'],['1 costume'],['gabarit']];
summary.getRange('B27').setNumberFormat('0.0%_ ');
summary.getRange('E23:F23').values=[['Extension du budget','Dessins']];
summary.getRange('E24:E26').values=[['Quatre combattants complets'],['Douze combattants complets'],['Trente-six combattants complets']];
summary.getRange('F24:F26').formulas=[['=B24*4'],['=B24*12'],['=B24*B6']];
summary.getRange('E28').values=[['Estimations à un costume par combattant.']];
summary.getRange('E29').values=[['Les poses générées ne valident pas un cycle animé.']];
summary.getRange('E28:F29').format.font={name:'Arial',size:10,color:'#465768'};
summary.getRange('A32').values=[['Fidélité']];
summary.getRange('A32').format.font={name:'Arial',size:11,bold:true,color:'#000000'};
summary.getRange('A33').values=[['Référence canonique, adaptation de gameplay et réalisation sont suivies séparément.']];
summary.getRange('A34').values=[['Les sources et leurs limites de preuve figurent dans les onglets de contenu.']];
summary.getRange('B6:B28').format.horizontalAlignment='right';
summary.getRange('F6:F26').format.horizontalAlignment='right';
summary.getRange('B6:B28').format.borders={right:{style:'thin',color:'#CCD4DC'}};
summary.getRange('B23:C23').format.horizontalAlignment='center';
for(const r of ['B6:B26','B28','F6:F26'])summary.getRange(r).setNumberFormat('#,##0_ ');

// Verify live recalculation and prerequisites in-place, then restore every input.
wb.recalculate();
const initialPlan=summary.getRange('B24').values[0][0];
animationSheet.getRange('C6').values=[[animations[0].frames_per_orientation+1]];
wb.recalculate();
const changedPlan=summary.getRange('B24').values[0][0];
if(changedPlan!==initialPlan+animations[0].orientations*animations[0].costumes)throw new Error('Animation budget did not recalculate.');
animationSheet.getRange('C6').values=[[animations[0].frames_per_orientation]];
if(assetRows.length){
  const originalAsset=assetSheet.getRange('G6:I6').values;
  const originalAlpha=assetSheet.getRange('L6:M6').values;
  assetSheet.getRange('I6').values=[['À intégrer']];
  assetSheet.getRange('L6:M6').values=[['Oui','Non']];
  assetSheet.getRange('G6:H6').values=[['Validé','Validé']];
  wb.recalculate();
  if(summary.getRange('F10').values[0][0]!==0)throw new Error('Asset incorrectly ready without integration.');
  assetSheet.getRange('I6').values=[['Intégré']];
  wb.recalculate();
  if(summary.getRange('F10').values[0][0]!==1)throw new Error('Asset readiness did not recalculate.');
  assetSheet.getRange('L6:M6').values=[['Non','Oui']];
  wb.recalculate();
  if(summary.getRange('F10').values[0][0]!==0)throw new Error('Asset incorrectly ready without required alpha.');
  assetSheet.getRange('G6:I6').values=originalAsset;
  assetSheet.getRange('L6:M6').values=originalAlpha;
}
wb.recalculate();
const summaryInspect=await wb.inspect({kind:'table',range:'Synthèse!A5:F15',include:'values,formulas',tableMaxRows:12,tableMaxCols:6,maxChars:6500});
console.log(summaryInspect.ndjson);
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:60},summary:'Formula error scan',maxChars:3000});
console.log(errors.ndjson);
const validation={roster:roster.length,costumes:costumes.length,moves:moves.length,combos:combos.length,routes:routes.length,bosses:bosses.length,phases:phases.length,stages:stages.length,layers:layers.length,chapters:campaign.length,productionTasks:production.length,animationRows:animations.length,drawingsPerOrientation:animations.reduce((sum,a)=>sum+a.frames_per_orientation*a.costumes,0),drawingsPerFighter:initialPlan,animationDrawingsValidated:summary.getRange('B25').values[0][0],imagesPresent:assetRows.length,imagesTechnicalValidated:summary.getRange('F7').values[0][0],imagesFidelityValidated:summary.getRange('F8').values[0][0],imagesIntegrated:summary.getRange('F9').values[0][0],imagesReady:summary.getRange('F10').values[0][0],imagesAlphaRequired:assetRows.filter(r=>r[12]==='Oui').length,imagesMissingRequiredAlpha:assetRows.filter(r=>r[12]==='Oui'&&r[11]!=='Oui').length,animationRecalculation:true,assetPrerequisiteRecalculation:true,requiredAlphaRecalculation:true,outputPath:path.join(outputDir,outputFilename),qaSheets:qaSheets?[...qaSheets]:['Synthèse',...sheetNames]};
await fs.writeFile(path.join(qaDir,'validation.json'),JSON.stringify(validation,null,2));
await fs.writeFile(path.join(qaDir,'formula_scan.ndjson'),errors.ndjson);
const xlsx=await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(path.join(outputDir,outputFilename));
console.log('EXPORTED',JSON.stringify(validation));
for(const [i,name] of ['Synthèse',...sheetNames].entries()){
  if(qaSheets && !qaSheets.has(name))continue;
  const end=name==='Synthèse'?34:Math.min(rows[name].end,10);
  const last=name==='Synthèse'?'F':col(Math.min(rows[name].cols-1,7));
  const blob=await wb.render({sheetName:name,range:`A1:${last}${end}`,scale:1,format:'png'});
  await fs.writeFile(path.join(qaDir,`${String(i).padStart(2,'0')}_${name.normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/ /g,'_')}.png`),new Uint8Array(await blob.arrayBuffer()));
  console.log('RENDERED',name);
  if(['Mouvements','Assets','Campagne','Boss','Roster'].includes(name)){
    const left=name==='Mouvements'?'I':name==='Assets'?'I':name==='Campagne'?'I':'I';
    const edge=col(rows[name].cols-1);
    const detail=await wb.render({sheetName:name,range:`${left}5:${edge}${Math.min(rows[name].end,8)}`,scale:1,format:'png'});
    await fs.writeFile(path.join(qaDir,`detail_${name.normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/ /g,'_')}.png`),new Uint8Array(await detail.arrayBuffer()));
  }
}
console.log('COMPLETE');
