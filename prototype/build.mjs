import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const dir=path.dirname(fileURLToPath(import.meta.url));
let html=await fs.readFile(path.join(dir,'index.html'),'utf8');
const assets={};
const defaults={marcus:'marcus_neutral_cutout.png',raam:'characters_v5/raam_gow1_fullbody.png',berserker:'berserker.png',stage:'stage_ephyra.png'};
const mappingFile=path.join(dir,'asset-map.json');
let mapping={};try{mapping=JSON.parse(await fs.readFile(mappingFile,'utf8'));}catch{}
for(const [key,filename] of Object.entries({...defaults,...mapping})){
  const file=path.isAbsolute(filename)?filename:path.join(dir,'../assets',filename);
  try{const data=await fs.readFile(file);const ext=path.extname(file).toLowerCase();assets[key]=`data:${ext==='.jpg'||ext==='.jpeg'?'image/jpeg':'image/png'};base64,${data.toString('base64')}`;}catch{}
}
let app=await fs.readFile(path.join(dir,'app.js'),'utf8');
app=app.replace("{marcus:'../assets/marcus_neutral_cutout.png',raam:'../assets/characters_v5/raam_gow1_fullbody.png',berserker:'../assets/berserker.png',stage:'../assets/stage_ephyra.png',...(window.GEARS_ASSETS||{})}",'{...(window.GEARS_ASSETS||{})}');
const engine=await fs.readFile(path.join(dir,'engine.js'),'utf8');
html=html.replace('<script src="engine.js"></script>',`<script>window.GEARS_ASSETS=${JSON.stringify(assets)};<\/script>\n<script>${engine}<\/script>`).replace('<script src="app.js"></script>',`<script>${app}<\/script>`);
await fs.writeFile(path.join(dir,'Gears_Combats_Prototype.html'),html);
console.log(JSON.stringify({file:path.join(dir,'Gears_Combats_Prototype.html'),embeddedAssets:Object.keys(assets),bytes:Buffer.byteLength(html)}));
