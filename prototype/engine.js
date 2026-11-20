/* Gears of War Combats — prototype mechanics, original adaptation values. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.GearsEngine = factory();
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const W = 1200, FLOOR = 545, FPS = 60;
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const attacks = {
    light: { startup: 6, active: 3, recovery: 15, damage: 62, reach: 99, stagger: 15, meter: 9 },
    heavy: { startup: 17, active: 4, recovery: 25, damage: 112, reach: 134, stagger: 23, meter: 15 },
  };
  const modes = {
    duel: { name: 'Duel', foe: 'Général RAAM', health: 1250, width: 62, height: 156 },
    berserker: { name: 'Boss Battle', foe: 'Berserker', health: 2800, width: 104, height: 226 },
    raven: { name: 'Simulation véhicule', foe: 'King Raven', health: 2400, width: 190, height: 110 },
  };
  function create(mode = 'duel', seed = 2147) {
    if (!modes[mode]) mode = 'duel';
    const m = modes[mode];
    return { mode, frame: 0, seed, visualSeed:(seed^0x9e3779b9)>>>0, state: 'playing', paused: false, time: mode === 'duel' ? 99 * FPS : 180 * FPS,
      player: { x: 260, y: FLOOR, w: 52, h: 146, hp: 1000, maxHp: 1000, facing: 1, ammo: 8, maxAmmo: 8, meter: 0,
        guard: 100, guarding: false, guardRegenDelay:0, guardBreak:0, stun: 0, cooldown: 0, dodge: 0, dodgeCooldown: 0, dodgeDir: 1, reload: null, perfectShots: 0, attack: null, invuln: 0, flash: 0 },
      enemy: { x: 880, y: mode === 'raven' ? 285 : FLOOR, w: m.width, h: m.height, hp: m.health, maxHp: m.health,
        name: m.foe, facing: -1, phase: 1, state: 'idle', clock: 70, stun: 0, cooldown: 0, attack: null, flash: 0,
        vulnerable: mode === 'duel', targetX: 260, move: '', dir: -1, lastPhase: 1 },
      projectiles: [], zones: [], particles: [], events: [], combo: 0, comboTimer: 0, bestCombo: 0, damageDealt: 0, damageTaken: 0,
      score: 0, perfectReloads: 0, dodges: 0, reloadAttempts: 0, victoryTime: 0, lastInput: {}, tutorial: '', shake: 0,
    };
  }
  function random(g) { g.seed = (Math.imul(g.seed, 1664525) + 1013904223) >>> 0; return g.seed / 4294967296; }
  function visualRandom(g) { g.visualSeed=(Math.imul(g.visualSeed,1664525)+1013904223)>>>0;return g.visualSeed/4294967296; }
  function event(g, text, kind = 'info') { g.events.unshift({ text, kind, life: 160 }); g.events = g.events.slice(0, 4); }
  function particle(g, x, y, color, n = 8) { for (let i = 0; i < n; i++) g.particles.push({ x, y, vx: (visualRandom(g)-.5)*10, vy: -visualRandom(g)*7, life: 20 + visualRandom(g)*15, color }); }
  function activeDodge(p) { return p.dodge > 0 && p.dodge <= 24 && p.dodge >= 9; }
  function hitPlayer(g, damage, sourceX, unblockable = false, kind = 'melee') {
    const p = g.player;
    if (g.state !== 'playing' || p.invuln > 0) return { hit: false, reason: 'invulnerable' };
    if (activeDodge(p)) { g.dodges++; p.invuln=8;p.meter = clamp(p.meter + 6, 0, 100); event(g, 'ESQUIVE', 'good'); return { hit: false, reason: 'dodge' }; }
    const fromFront = Math.sign(sourceX - p.x) === p.facing;
    if (p.guarding && fromFront && !unblockable && p.guard > 0) {
      const loss = Math.ceil(damage * .5);p.guard-=loss;
      const chip=kind==='projectile'?Math.min(Math.ceil(damage*.1),Math.max(0,p.hp-(g.mode==='duel'?1:0))):0;
      p.hp-=chip;p.invuln=10;p.guardRegenDelay=45;g.damageTaken+=chip;
      particle(g, p.x + p.facing*40, p.y-90, '#80d0e4', 5);
      if (p.guard <= 0) { p.guard = 0; p.stun = 45;p.guardBreak=45; event(g, 'GARDE BRISÉE', 'bad'); }
      return { hit: true, reason: 'guard', damage: chip };
    }
    p.hp = Math.max(0, p.hp - damage); p.stun = Math.max(p.stun, 18); p.invuln = 22; p.flash = 8; p.attack = null;p.guardRegenDelay=45;
    if (p.reload) p.reload = null;
    p.x = clamp(p.x + Math.sign(p.x - sourceX) * 28, 55, W - 55);
    g.damageTaken += damage; g.combo = 0; g.shake = 10;
    particle(g, p.x, p.y-90, '#e6e0d4', 12);
    return { hit: true, reason: 'damage', damage };
  }
  function hitEnemy(g, damage, kind = 'melee') {
    const e = g.enemy, p = g.player;
    if (g.state !== 'playing' || e.hp <= 0) return 0;
    let mult = 1;
    if (g.mode !== 'duel' && !e.vulnerable) mult = kind === 'special' ? .3 : .18;
    const dealt = Math.round(damage*mult);
    e.hp = Math.max(0, e.hp - dealt); e.flash = 7; g.damageDealt += dealt; g.score += dealt;
    p.meter = clamp(p.meter + (kind === 'special' ? 0 : Math.max(3, Math.round(dealt/10))), 0, 100);
    g.combo = g.comboTimer > 0 ? g.combo + 1 : 1; g.comboTimer = 80; g.bestCombo = Math.max(g.bestCombo, g.combo);
    if (g.mode === 'duel') { e.stun = kind === 'heavy' ? 22 : 11; e.attack = null; e.x = clamp(e.x + p.facing*(kind === 'heavy' ? 35 : 12), 55, W-55); }
    particle(g, e.x, e.y - e.h*.6, e.vulnerable ? '#ffcc73' : '#98a8ac', kind === 'special' ? 24 : 9);
    g.shake = kind === 'special' ? 13 : kind === 'heavy' ? 7 : 3;
    if (g.mode !== 'duel' && !e.vulnerable) g.tutorial = 'Blindage actif. Attendez la fenêtre de faiblesse.';
    return dealt;
  }
  function startReload(g) {
    const p = g.player;
    if (p.stun || p.dodge || p.attack || p.cooldown > 6) return false;
    if (!p.reload) {
      if (p.ammo === p.maxAmmo) return false;
      p.reload = { clock: 0, total: 72, locked: false, result: 'loading' }; g.reloadAttempts++; return true;
    }
    const r = p.reload;
    if (r.locked) return false;
    if (r.clock >= 34 && r.clock <= 43) { r.locked=true;r.result='perfect';r.total=44;
    } else if (r.clock >= 27 && r.clock <= 50) { r.locked=true;r.result='safe';r.total=60;
    } else { r.locked = true; r.total = 102; r.result = 'jam'; event(g, 'ENRAYAGE · attendez', 'bad'); }
    return true;
  }
  function startPlayerAttack(g, type) {
    const p = g.player;
    if (p.stun || p.cooldown || p.attack || p.reload || p.dodge || p.guarding) return false;
    if (type === 'shoot' || type === 'special') {
      if (type === 'shoot' && p.ammo <= 0) { event(g, 'CHARGEUR VIDE · R pour recharger', 'bad'); p.cooldown=12; return false; }
      if (type === 'special' && p.meter < 100) { event(g, 'Spécial disponible à 100', 'info'); p.cooldown=10; return false; }
      const enhanced = type === 'shoot' && p.perfectShots > 0;
      if (type === 'shoot') { p.ammo--; if (enhanced) p.perfectShots--; } else p.meter=0;
      const damage = type === 'special' ? 270 : enhanced ? Math.round(58*1.1) : 58;
      const y = p.y - 92;
      const targetY = g.mode === 'raven' ? g.enemy.y - 45 : y;
      const dx = g.enemy.x - p.x, distance = Math.max(1, Math.abs(dx));
      g.projectiles.push({ x:p.x+p.facing*46,y,vx:p.facing*(type==='special'?23:21),vy:Math.sign(dx)===p.facing?(targetY-y)/distance*21:0,
        owner:'player',damage,kind:type,life:90,enhanced });
      p.cooldown = type === 'special' ? 45 : 18; p.flash = type === 'special' ? 10 : 4;
      return true;
    }
    const a=attacks[type]; if(!a)return false;
    p.attack = { type, clock:0, hit:false, ...a }; p.cooldown = a.startup+a.active+a.recovery; return true;
  }
  function updateAttack(g, a, actor, target, playerOwned) {
    if (!a) return;
    a.clock++;
    if (!a.hit && a.clock >= a.startup && a.clock < a.startup+a.active) {
      const distance = Math.abs(actor.x-target.x);
      const front = Math.sign(target.x-actor.x)===actor.facing;
      const vertical = Math.abs(actor.y-target.y)<100;
      if (front && vertical && distance < a.reach+target.w/2) {
        a.hit=true;
        if(playerOwned)hitEnemy(g,a.damage,a.type); else hitPlayer(g,a.damage,actor.x);
      }
    }
    if(a.clock>=a.startup+a.active+a.recovery)actor.attack=null;
  }
  function duelAI(g) {
    const e=g.enemy,p=g.player;
    e.facing=p.x<e.x?-1:1; e.vulnerable=true;
    if(e.stun>0||e.attack)return;
    const distance=Math.abs(e.x-p.x);
    if(distance>170)e.x+=e.facing*2.7;
    if(e.cooldown>0)return;
    if(distance<175) {
      e.attack={type:'heavy',clock:0,hit:false,startup:26,active:5,recovery:33,damage:115,reach:145}; e.cooldown=78;
      g.tutorial='RAAM arme sa lame. Gardez de face ou esquivez.';
    } else if(random(g)<.035) {
      e.state='aim'; e.clock=28; e.cooldown=100;
    }
  }
  function berserkerAI(g) {
    const e=g.enemy,p=g.player;
    e.facing=p.x<e.x?-1:1;
    if(e.state==='idle') {
      e.vulnerable=false; e.x=clamp(e.x+e.facing*1.2,90,W-90);
      if(--e.clock<=0) {
        e.move=Math.abs(e.x-p.x)<220?'slam':'charge'; e.state='telegraph';e.clock=e.move==='slam'?70-e.phase*6:86-e.phase*5;
        e.targetX=p.x;e.dir=e.facing;
        event(g,e.move==='slam'?'ÉCRASEMENT · sortez du cercle':'CHARGE · esquivez la traversée','warning');
        g.tutorial=e.move==='charge'?'La charge se termine contre le mur : attaquez pendant son étourdissement.':'Reculez hors du cercle ou esquivez au moment de l’impact.';
      }
    } else if(e.state==='telegraph') {
      if(--e.clock<=0){e.state='attack';e.clock=e.move==='slam'?14:90;if(e.move==='slam'){g.shake=17;if(Math.abs(p.x-e.x)<230)hitPlayer(g,145+e.phase*20,e.x,true);}}
    } else if(e.state==='attack') {
      e.clock--;
      if(e.move==='charge') {
        e.x+=e.dir*(12+e.phase*2);
        if(Math.abs(e.x-p.x)<100)hitPlayer(g,155+e.phase*16,e.x,true);
        if(e.x<=98||e.x>=W-98||e.clock<=0){e.x=clamp(e.x,98,W-98);e.state='exposed';e.clock=140-e.phase*12;e.vulnerable=true;g.shake=15;event(g,'FAIBLESSE · blindage ouvert','good');}
      } else if(e.clock<=0){e.state='exposed';e.clock=100-e.phase*8;e.vulnerable=true;event(g,'FAIBLESSE · punissez l’écrasement','good');}
    } else if(e.state==='exposed') {
      e.vulnerable=true;if(--e.clock<=0){e.state='idle';e.clock=75-e.phase*9;e.vulnerable=false;}
    }
  }
  function ravenAI(g) {
    const e=g.enemy,p=g.player;
    e.y=284+Math.sin(g.frame/42)*19;e.facing=-1;
    if(e.state==='idle'){
      e.vulnerable=false;e.x+=Math.sin(g.frame/90)*1.2;e.x=clamp(e.x,620,1010);
      if(--e.clock<=0){e.state='telegraph';e.clock=80-e.phase*7; e.targetX=p.x;
        const offsets=e.phase===1?[0]:e.phase===2?[-120,120]:[-210,0,210];
        for(const o of offsets)g.zones.push({x:clamp(p.x+o,70,W-70),radius:88,life:e.clock+12,clock:e.clock,hit:false});
        event(g,'SALVE MARQUÉE · quittez les zones','warning');g.tutorial='Après la salve, le moteur est exposé. Les tirs suivent automatiquement sa hauteur.';
      }
    } else if(e.state==='telegraph'){
      if(--e.clock<=0){e.state='attack';e.clock=27;g.shake=8;}
    } else if(e.state==='attack'){
      if(--e.clock<=0){e.state='exposed';e.clock=130-e.phase*10;e.vulnerable=true;event(g,'MOTEUR EXPOSÉ · feu !','good');}
    } else if(e.state==='exposed'){
      e.vulnerable=true;if(--e.clock<=0){e.state='idle';e.clock=67-e.phase*7;e.vulnerable=false;}
    }
  }
  function step(g, input={}) {
    if(g.paused||g.state!=='playing')return g;
    g.frame++;g.time--;
    const p=g.player,e=g.enemy;
    for(const actor of [p,e])for(const key of ['stun','cooldown','flash','invuln','dodgeCooldown','guardRegenDelay'])if(actor[key]>0)actor[key]--;
    const guardRestored=p.guardBreak>0&&--p.guardBreak===0;
    if(guardRestored)p.guard=Math.max(60,p.guard);
    if(g.shake>0)g.shake--;
    if(g.comboTimer>0)g.comboTimer--;else g.combo=0;
    g.events.forEach(x=>x.life--);g.events=g.events.filter(x=>x.life>0);
    const edge=k=>!!input[k]&&!g.lastInput[k];
    p.facing=e.x<p.x?-1:1;
    p.guarding=!!input.guard&&!p.stun&&!p.dodge&&!p.attack&&!p.reload&&!p.guardBreak;
    if(p.guarding)p.guardRegenDelay=45;else if(!p.guardBreak&&!p.guardRegenDelay&&!guardRestored)p.guard=clamp(p.guard+.25,0,100);
    if(p.reload){p.reload.clock++;if(p.reload.clock>=p.reload.total){
      const outcome=p.reload.result;p.ammo=p.maxAmmo;p.reload=null;
      if(outcome==='perfect'){p.perfectShots=2;p.meter=clamp(p.meter+12,0,100);g.perfectReloads++;g.score+=150;event(g,'RECHARGE PARFAITE · 2 tirs renforcés','good');}
      else event(g,outcome==='safe'?'Recharge rapide':'Chargeur plein',outcome==='safe'?'good':'info');
    }}
    if(edge('reload'))startReload(g);
    if(edge('dodge')&&!p.stun&&!p.dodge&&!p.dodgeCooldown&&!p.attack){
      p.dodge=30;p.dodgeCooldown=66;p.dodgeDir=input.left?-1:input.right?1:p.facing;p.reload=null;p.guarding=false;
    }
    if(p.dodge>0){p.dodge--;p.x=clamp(p.x+p.dodgeDir*12,55,W-55);}
    else if(!p.stun&&!p.attack&&!p.reload&&!p.guarding){p.x=clamp(p.x+((input.right?1:0)-(input.left?1:0))*5.8,55,W-55);}
    if(edge('light'))startPlayerAttack(g,'light');
    if(edge('heavy'))startPlayerAttack(g,'heavy');
    if(input.shoot)startPlayerAttack(g,'shoot');
    if(edge('special'))startPlayerAttack(g,'special');
    updateAttack(g,p.attack,p,e,true);updateAttack(g,e.attack,e,p,false);
    if(g.mode==='duel'){
      if(e.state==='aim'){
        if(--e.clock<=0){e.state='idle';g.projectiles.push({x:e.x+e.facing*45,y:FLOOR-95,vx:e.facing*13,vy:0,damage:70,owner:'enemy',kind:'shoot',life:100});}
      }else duelAI(g);
    }else{
      e.phase=e.hp<=e.maxHp*.33?3:e.hp<=e.maxHp*.66?2:1;
      if(e.phase!==e.lastPhase){event(g,'PHASE '+e.phase+' · intensification','warning');e.lastPhase=e.phase;g.score+=250;}
      if(g.mode==='berserker')berserkerAI(g);else ravenAI(g);
    }
    for(const b of g.projectiles){
      b.x+=b.vx;b.y+=b.vy;b.life--;
      const target=b.owner==='player'?e:p;
      if(b.life>0&&Math.abs(b.x-target.x)<target.w/2+17&&b.y>target.y-target.h-10&&b.y<target.y+10){
        if(b.owner==='player')hitEnemy(g,b.damage,b.kind);else hitPlayer(g,b.damage,b.x-b.vx,false,'projectile');b.life=0;
      }
    }
    g.projectiles=g.projectiles.filter(b=>b.life>0&&b.x>-50&&b.x<W+50);
    for(const z of g.zones){z.life--;z.clock--;if(z.clock<=0&&!z.hit){z.hit=true;g.shake=12;particle(g,z.x,FLOOR-20,'#ff9c42',24);if(Math.abs(p.x-z.x)<z.radius)hitPlayer(g,140+e.phase*20,e.x,true);}}
    g.zones=g.zones.filter(z=>z.life>0);
    for(const q of g.particles){q.x+=q.vx;q.y+=q.vy;q.vy+=.25;q.life--;}
    g.particles=g.particles.filter(q=>q.life>0);
    if(p.hp<=0){p.hp=0;g.state='defeat';event(g,'DÉFAITE','bad');}
    else if(e.hp<=0){e.hp=0;g.state='victory';g.victoryTime=g.frame;g.score+=Math.max(0,Math.floor(g.time/6))+Math.round(p.hp)+g.perfectReloads*100;event(g,'VICTOIRE','good');}
    else if(g.time<=0){g.time=0;g.state=(g.mode==='duel'&&p.hp/p.maxHp>e.hp/e.maxHp)?'victory':'defeat';event(g,'TEMPS ÉCOULÉ','warning');}
    g.lastInput={...input};return g;
  }
  return {W,FLOOR,FPS,attacks,modes,create,step,hitPlayer,hitEnemy,startReload,startPlayerAttack,activeDodge};
});
