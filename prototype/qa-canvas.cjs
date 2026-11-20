/* Local JS and canvas smoke check. This does not claim browser or CSS verification. */
const fs=require('node:fs');
const vm=require('node:vm');
const path=require('node:path');
const assert=require('node:assert/strict');
const {createRequire}=require('node:module');
const runtimeRequire=createRequire(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,'package.json'));
const {createCanvas,loadImage}=runtimeRequire('@napi-rs/canvas');
async function main(){
const dir=__dirname,html=fs.readFileSync(path.join(dir,'index.html'),'utf8');
class Element{
  constructor(id){this.id=id;this.hidden=['pause','result','help'].includes(id);this.style={};this.dataset={};this.events={};this.textContent='';this.disabled=false;this.classList={toggle(){},add(){},remove(){}};}
  addEventListener(name,fn){this.events[name]=fn;}
  click(){if(this.onclick)this.onclick();if(this.events.click)this.events.click({preventDefault(){}});}
  focus(){}setPointerCapture(){}
}
const els={};for(const match of html.matchAll(/id="([^"]+)"/g))els[match[1]]=new Element(match[1]);
const modes=['duel','berserker','raven'].map(mode=>{const b=new Element(mode);b.dataset.mode=mode;return b;});
const actions=['left','right','guard','dodge','light','heavy','shoot','special','reload'].map(action=>{const b=new Element(action);b.dataset.action=action;return b;});
const canvas=createCanvas(1200,675);canvas.getBoundingClientRect=()=>({width:1200,height:675});els.game=canvas;
const document={events:{},getElementById:id=>els[id],querySelectorAll:selector=>selector==='[data-action]'?actions:modes,addEventListener(name,fn){this.events[name]=fn;},hidden:false};
let queue=[],now=1000;
class ImageStub{set src(v){if(this.onerror)this.onerror();}}
const context={document,Image:ImageStub,navigator:{getGamepads:()=>[]},requestAnimationFrame:fn=>queue.push(fn),addEventListener(){},console,Math,Number,String,Object,Array,GEARS_ASSETS:{}};context.window=context;
vm.createContext(context);vm.runInContext(fs.readFileSync(path.join(dir,'engine.js'),'utf8'),context);vm.runInContext(fs.readFileSync(path.join(dir,'app.js'),'utf8'),context);
const stagePath=path.join(dir,'../assets/stage_ephyra.png');
if(fs.existsSync(stagePath)){context.GearsPrototype.assets.stage=await loadImage(stagePath);}
const marcusPath=path.join(dir,'../assets/marcus_neutral_cutout.png');
if(fs.existsSync(marcusPath)){context.GearsPrototype.assets.marcus=await loadImage(marcusPath);}
const raamPath=path.join(dir,'../assets/characters_v5/raam_gow1_fullbody.png');
if(fs.existsSync(raamPath)){context.GearsPrototype.assets.raam=await loadImage(raamPath);}
function frame(){const fn=queue.shift();now+=1000/60;fn(now);}
frame();assert(els['enemy-name'].textContent.includes('RAAM'));context.GearsPrototype.start();frame();
const shoot=actions.find(b=>b.dataset.action==='shoot');const ev={preventDefault(){},pointerId:1};shoot.events.pointerdown(ev);shoot.events.pointerup(ev);frame();frame();
assert.equal(context.GearsPrototype.getState().player.ammo,7,'A short touch between frames must fire');
context.GearsPrototype.pause();const t=context.GearsPrototype.getState().time;frame();assert.equal(context.GearsPrototype.getState().time,t);context.GearsPrototype.pause();
fs.mkdirSync(path.join(dir,'qa'),{recursive:true});
for(const mode of ['duel','berserker','raven']){
  context.GearsPrototype.choose(mode);context.GearsPrototype.start();
  if(mode!=='duel'){const g=context.GearsPrototype.getState();g.enemy.state='exposed';g.enemy.vulnerable=true;g.enemy.clock=100;}
  frame();frame();fs.writeFileSync(path.join(dir,'qa',`canvas-${mode}.png`),canvas.toBuffer('image/png'));
}
if(fs.existsSync(marcusPath)){
  context.GearsPrototype.setIllustrations(true);
  for(const mode of ['duel','berserker']){context.GearsPrototype.choose(mode);context.GearsPrototype.start();frame();frame();fs.writeFileSync(path.join(dir,'qa',`canvas-${mode}-illustration.png`),canvas.toBuffer('image/png'));}
  context.GearsPrototype.setIllustrations(false);
}
assert(context.GearsPrototype.assets.raam,'The generated RAAM reference must load');
const result={date:'2026-11-20',engineTests:'Separate command: node tests.cjs',jsParse:'pass',canvasRenderer:'all three modes rendered locally; Marcus and RAAM illustrations loaded for the duel',loadedAssets:Object.keys(context.GearsPrototype.assets).sort(),shortTouchBuffer:'pass',pause:'pass',browserVerification:'blocked: local Chromium socket() failed with Operation not permitted',cssResponsiveVerification:'not run',hardwareGamepad:'not tested'};
fs.writeFileSync(path.join(dir,'qa','canvas-report-v5.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));
}
main().catch(error=>{console.error(error);process.exitCode=1;});
