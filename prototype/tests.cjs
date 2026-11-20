const assert = require('node:assert/strict');
const E = require('./engine.js');
let count = 0;
function test(name, fn) { fn(); count++; console.log('PASS '+name); }
test('La garde de face bloque les dégâts de corps à corps et consomme sa jauge', () => {
  const g=E.create();g.player.guarding=true;g.player.facing=1;
  const result=E.hitPlayer(g,100,g.player.x+100);
  assert.equal(result.reason,'guard');assert.equal(g.player.hp,1000);assert.equal(g.player.guard,50);
});
test('Le chip des tirs est de 10 % et ne peut pas tuer en duel',()=>{
  const g=E.create();g.player.guarding=true;g.player.facing=1;
  assert.equal(E.hitPlayer(g,70,g.player.x+100,false,'projectile').damage,7);assert.equal(g.player.hp,993);
  g.player.invuln=0;g.player.hp=4;g.player.guard=100;E.hitPlayer(g,70,g.player.x+100,false,'projectile');assert.equal(g.player.hp,1);
});
test('Une attaque géante traverse la garde, mais peut être esquivée', () => {
  const g=E.create('berserker');g.player.guarding=true;
  E.hitPlayer(g,200,g.player.x+100,true);assert.equal(g.player.hp,800);
  g.player.invuln=0;g.player.dodge=15;
  assert.equal(E.hitPlayer(g,200,g.player.x+100,true).reason,'dodge');assert.equal(g.player.hp,800);
});
test('La recharge parfaite finit à 44 f et renforce exactement deux tirs de 10 % arrondis', () => {
  const g=E.create();g.player.ammo=1;assert(E.startReload(g));g.player.reload.clock=34;assert(E.startReload(g));
  assert.equal(g.player.ammo,1);for(let i=0;i<9;i++)E.step(g,{});assert.equal(g.player.ammo,1);E.step(g,{});
  assert.equal(g.player.ammo,8);assert.equal(g.player.perfectShots,2);assert.equal(g.perfectReloads,1);
  for(let i=0;i<3;i++){g.player.cooldown=0;assert(E.startPlayerAttack(g,'shoot'));}
  assert.deepEqual(g.projectiles.map(b=>b.damage),[64,64,58]);assert.equal(g.player.perfectShots,0);
});
test('Toutes les bornes de recharge respectent les fenêtres inclusives',()=>{
  for(const [clock,outcome,total] of [[26,'jam',102],[27,'safe',60],[33,'safe',60],[34,'perfect',44],[43,'perfect',44],[44,'safe',60],[50,'safe',60],[51,'jam',102]]){
    const g=E.create();g.player.ammo=0;E.startReload(g);g.player.reload.clock=clock;E.startReload(g);
    assert.equal(g.player.reload.result,outcome,'clock '+clock);assert.equal(g.player.reload.total,total);assert.equal(g.player.ammo,0);assert.equal(E.startReload(g),false);
  }
});
test('La recharge sans confirmation se termine à 72 f',()=>{
  const g=E.create();g.enemy.cooldown=1000;g.player.ammo=0;E.startReload(g);for(let i=0;i<71;i++)E.step(g,{});assert.equal(g.player.ammo,0);E.step(g,{});assert.equal(g.player.ammo,8);
});
test('Un appui trop tôt provoque un enrayage terminé sans second appui', () => {
  const g=E.create();g.enemy.x=1150;g.enemy.cooldown=500;g.player.ammo=0;
  E.startReload(g);g.player.reload.clock=10;E.startReload(g);
  assert.equal(g.player.reload.result,'jam');assert.equal(g.player.reload.total,102);
  for(let i=0;i<92;i++)E.step(g,{});
  assert.equal(g.player.reload,null);assert.equal(g.player.ammo,8);
});
test('La garde attend 45 f, puis récupère 15 points par seconde',()=>{
  const g=E.create();g.player.guard=50;g.player.guardRegenDelay=45;g.enemy.cooldown=1000;
  for(let i=0;i<44;i++)E.step(g,{});assert.equal(g.player.guard,50);E.step(g,{});assert.equal(g.player.guard,50.25);
  for(let i=0;i<59;i++)E.step(g,{});assert.equal(g.player.guard,65);
});
test('Une rupture immobilise 45 f puis restaure 60 points de garde',()=>{
  const g=E.create();g.enemy.cooldown=1000;g.player.guarding=true;g.player.guard=5;E.hitPlayer(g,100,g.player.x+100);
  assert.equal(g.player.guardBreak,45);assert.equal(g.player.stun,45);for(let i=0;i<44;i++)E.step(g,{});assert.equal(g.player.guard,0);E.step(g,{});assert.equal(g.player.guard,60);
});
test('La faiblesse du boss modifie les dégâts, puis déclenche ses trois phases', () => {
  const g=E.create('berserker');g.enemy.vulnerable=false;
  assert.equal(E.hitEnemy(g,100,'shoot'),18);g.enemy.vulnerable=true;assert.equal(E.hitEnemy(g,100,'shoot'),100);
  g.enemy.hp=g.enemy.maxHp*.6;E.step(g,{});assert.equal(g.enemy.phase,2);
  g.enemy.hp=g.enemy.maxHp*.3;E.step(g,{});assert.equal(g.enemy.phase,3);
});
test('Le coup léger touche à portée et ne touche pas hors portée', () => {
  const near=E.create();near.enemy.x=near.player.x+100;near.enemy.cooldown=500;
  E.step(near,{light:true});for(let i=0;i<7;i++)E.step(near,{});
  assert.equal(near.enemy.hp,near.enemy.maxHp-62);
  const far=E.create();E.step(far,{light:true});for(let i=0;i<7;i++)E.step(far,{});
  assert.equal(far.enemy.hp,far.enemy.maxHp);
});
test('La salve du véhicule montre trois zones en phase trois', () => {
  const g=E.create('raven');g.enemy.hp=500;g.enemy.clock=1;E.step(g,{});
  assert.equal(g.enemy.phase,3);assert.equal(g.enemy.state,'telegraph');assert.equal(g.zones.length,3);assert(g.zones.every(z=>z.clock>0));
});
test('La pause et les écrans de résultat stoppent le temps', () => {
  const g=E.create();const time=g.time;g.paused=true;E.step(g,{shoot:true});assert.equal(g.time,time);assert.equal(g.player.ammo,8);
  g.paused=false;g.enemy.hp=0;E.step(g,{});assert.equal(g.state,'victory');const t=g.time;E.step(g,{shoot:true});assert.equal(g.time,t);
});
test('Les trois rencontres restent finies et bornées sous 20 000 pas simulés', () => {
  for(const mode of ['duel','berserker','raven']){
    const g=E.create(mode);
    for(let i=0;i<20000&&g.state==='playing';i++)E.step(g,{left:i%400<100,right:i%400>=200&&i%400<300,shoot:i%150<100,reload:i%150===105||i%150===150,guard:i%300>270,dodge:i%70===0,light:i%30===0,heavy:i%71===0,special:i%120===0});
    assert(['victory','defeat'].includes(g.state));assert(Number.isFinite(g.player.x));assert(g.player.hp>=0);assert(g.enemy.hp>=0);assert(g.player.ammo>=0);
  }
});
test('Le hasard des particules ne change pas la simulation de combat',()=>{
  const a=E.create('duel',42),b=E.create('duel',42);b.visualSeed=987654;
  for(let i=0;i<1500;i++){const input={shoot:i%160<100,reload:i%160===105||i%160===140,right:i%200<30,dodge:i%91===0};E.step(a,input);E.step(b,input);}
  for(const key of ['hp','x','ammo','meter'])assert.equal(a.player[key],b.player[key]);assert.equal(a.enemy.hp,b.enemy.hp);assert.equal(a.enemy.x,b.enemy.x);assert.equal(a.seed,b.seed);
});
console.log(`${count} tests passed.`);
