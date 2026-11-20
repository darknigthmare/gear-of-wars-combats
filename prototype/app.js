(function () {
  'use strict';
  const E=window.GearsEngine, $=id=>document.getElementById(id), canvas=$('game'),ctx=canvas.getContext('2d');
  const paths={marcus:'../assets/marcus_neutral_cutout.png',raam:'../assets/characters_v5/raam_gow1_fullbody.png',berserker:'../assets/berserker.png',stage:'../assets/stage_ephyra.png',...(window.GEARS_ASSETS||{})};
  const images={};let selected='duel',game=E.create('duel'),screen='menu',last=0,accumulator=0,decorFrame=0,renderHeight=675,lastAnnouncement='',useIllustrations=true;
  const keyboard={},touch={},gamepad={},pressed={};
  for(const [name,src] of Object.entries(paths)){const img=new Image();img.onload=()=>{images[name]=img;if(name==='marcus')$('illustration-control').hidden=false;};img.onerror=()=>{};img.src=src;}
  const keymap={a:'left',q:'left',ArrowLeft:'left',d:'right',ArrowRight:'right',j:'light',k:'heavy',l:'shoot',i:'special',f:'guard',ArrowDown:'guard',' ':'dodge',r:'reload'};
  function clearInput(){for(const o of [keyboard,touch,gamepad,pressed])for(const k of Object.keys(o))delete o[k];}
  function title(){const info={duel:['Duel de profil','Marcus Fenix contre RAAM · mécaniques d’adaptation'],berserker:['Boss Battle · Berserker','Charge, écrasement et fenêtres de faiblesse · 3 phases'],raven:['Boss Battle · King Raven','Simulation non canonique · appareil allié opposé au joueur pour l’entraînement']}[selected];$('mode-title').textContent=info[0];$('mode-subtitle').textContent=info[1];}
  function choose(mode){selected=mode;document.querySelectorAll('.mode').forEach(el=>el.classList.toggle('active',el.dataset.mode===mode));if(screen==='menu')game=E.create(mode);title();updateHUD();}
  function start(){game=E.create(selected);screen='playing';$('menu').hidden=true;$('pause').hidden=true;$('result').hidden=true;$('pause-btn').disabled=false;$('pause-btn').textContent='Pause';clearInput();accumulator=0;$('arena').focus();title();updateHUD();announce('Début du combat contre '+game.enemy.name);}
  function showMenu(){screen='menu';game=E.create(selected);clearInput();$('menu').hidden=false;$('pause').hidden=true;$('result').hidden=true;$('pause-btn').disabled=true;$('start-btn').focus();updateHUD();}
  function togglePause(){if(screen!=='playing')return;game.paused=!game.paused;clearInput();$('pause').hidden=!game.paused;$('pause-btn').textContent=game.paused?'Reprendre':'Pause';if(game.paused)$('resume-btn').focus();else $('arena').focus();}
  function announce(text){if(text===lastAnnouncement)return;lastAnnouncement=text;$('announcer').textContent=text;}
  function result(){screen='result';$('result').hidden=false;$('pause-btn').disabled=true;const win=game.state==='victory';$('result-title').textContent=win?'VICTOIRE.':'DÉFAITE.';$('result-title').style.color=win?'#e8d4aa':'#e18375';$('result-description').textContent=win?(selected==='duel'?'RAAM est vaincu. Votre gestion de la distance et du chargeur a fait la différence.':'La rencontre est terminée. Vous avez exploité les ouvertures du boss.'):(selected==='duel'?'Observez l’armement de sa lame et gardez de face. Rechargez après avoir créé de la distance.':selected==='berserker'?'Les attaques géantes ignorent la garde. Esquivez la charge et frappez pendant l’ouverture dorée.':'Quittez les zones marquées avant l’impact. Gardez votre spécial pour le moteur exposé.');$('score').textContent=Math.round(game.score).toLocaleString('fr-FR');$('best-combo').textContent=game.bestCombo;$('perfect-count').textContent=game.perfectReloads;clearInput();$('retry-btn').focus();announce(win?'Victoire':'Défaite');}
  document.querySelectorAll('[data-mode]').forEach(b=>b.addEventListener('click',()=>choose(b.dataset.mode)));
  $('start-btn').onclick=start;$('retry-btn').onclick=start;$('menu-btn').onclick=showMenu;$('result-menu-btn').onclick=showMenu;$('pause-btn').onclick=togglePause;$('resume-btn').onclick=togglePause;
  $('show-illustration').onchange=()=>{useIllustrations=$('show-illustration').checked;};
  let helpPaused=false;
  $('help-btn').onclick=()=>{helpPaused=screen==='playing'&&!game.paused;if(helpPaused)togglePause();$('help').hidden=false;$('close-help').focus();};
  $('close-help').onclick=()=>{$('help').hidden=true;if(helpPaused&&game.paused)togglePause();else $('help-btn').focus();helpPaused=false;};
  document.addEventListener('keydown',ev=>{if(!$('help').hidden){if(ev.key==='Escape')$('close-help').click();return;}if(ev.key==='Escape'&&!ev.repeat){togglePause();return;}if((ev.key==='Enter')&&screen==='menu'){start();return;}const key=keymap[ev.key]||keymap[ev.key.toLowerCase()];if(key&&screen==='playing'){ev.preventDefault();keyboard[key]=true;if(!ev.repeat)pressed[key]=true;}});
  document.addEventListener('keyup',ev=>{const key=keymap[ev.key]||keymap[ev.key.toLowerCase()];if(key){keyboard[key]=false;if(screen==='playing')ev.preventDefault();}});
  window.addEventListener('blur',()=>{clearInput();if(screen==='playing'&&!game.paused)togglePause();});
  document.addEventListener('visibilitychange',()=>{if(document.hidden&&screen==='playing'&&!game.paused)togglePause();});
  for(const b of document.querySelectorAll('[data-action]')){
    b.addEventListener('pointerdown',ev=>{ev.preventDefault();if(screen!=='playing')return;b.setPointerCapture(ev.pointerId);touch[b.dataset.action]=true;pressed[b.dataset.action]=true;b.classList.add('down');});
    const release=ev=>{ev.preventDefault();touch[b.dataset.action]=false;b.classList.remove('down');};b.addEventListener('pointerup',release);b.addEventListener('pointercancel',release);b.addEventListener('lostpointercapture',release);
  }
  let padStart=false;
  function pollPad(){const pads=navigator.getGamepads?navigator.getGamepads():[],p=Array.from(pads).find(Boolean);for(const k of Object.keys(gamepad))delete gamepad[k];if(!p)return;const b=i=>!!p.buttons[i]?.pressed;gamepad.left=(p.axes[0]||0)<-.25||b(14);gamepad.right=(p.axes[0]||0)>.25||b(15);gamepad.dodge=b(0);gamepad.reload=b(1);gamepad.light=b(2);gamepad.heavy=b(3);gamepad.special=b(5);gamepad.guard=b(6);gamepad.shoot=b(7);if(b(9)&&!padStart){if(screen==='menu')start();else togglePause();}padStart=b(9);}
  function input(){const v={};for(const k of ['left','right','light','heavy','shoot','special','guard','dodge','reload'])v[k]=!!(keyboard[k]||touch[k]||gamepad[k]||pressed[k]);for(const k of Object.keys(pressed))delete pressed[k];return v;}
  function updateHUD(){const p=game.player,e=game.enemy;$('player-health').style.width=Math.max(0,p.hp/p.maxHp*100)+'%';$('enemy-health').style.width=Math.max(0,e.hp/e.maxHp*100)+'%';$('player-hp').textContent=Math.ceil(p.hp)+' / '+p.maxHp;$('enemy-hp').textContent=Math.ceil(e.hp)+' / '+e.maxHp;$('guard-fill').style.width=p.guard+'%';$('meter-fill').style.width=p.meter+'%';$('ammo').textContent=String(p.ammo).padStart(2,'0')+' / 08'+(p.perfectShots?' +':'');$('enemy-name').textContent=e.name.toUpperCase();$('clock').textContent=Math.ceil(game.time/60);$('phase').textContent=selected==='duel'?'DUEL · 1 MANCHE':('PHASE '+e.phase+' / 3'+(e.vulnerable?' · FAIBLESSE':' · BLINDAGE'));}
  function polygon(points,fill,stroke){ctx.beginPath();points.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));ctx.closePath();ctx.fillStyle=fill;ctx.fill();if(stroke){ctx.strokeStyle=stroke;ctx.stroke();}}
  function rect(x,y,w,h,fill){ctx.fillStyle=fill;ctx.fillRect(x,y,w,h);}
  function ellipse(x,y,rx,ry,fill){ctx.beginPath();ctx.ellipse(x,y,rx,ry,0,0,Math.PI*2);ctx.fillStyle=fill;ctx.fill();}
  function line(x1,y1,x2,y2,color,width=1){ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.strokeStyle=color;ctx.lineWidth=width;ctx.stroke();}
  function text(t,x,y,size=14,color='#dfe5df',align='left'){ctx.font=`600 ${size}px system-ui, sans-serif`;ctx.fillStyle=color;ctx.textAlign=align;ctx.fillText(t,x,y);}
  function background(){
    const offset=(game.player.x-600)*.12;
    const sky=ctx.createLinearGradient(0,-800,0,675);sky.addColorStop(0,'#141b23');sky.addColorStop(.5,'#1c2b37');sky.addColorStop(.8,'#37454a');sky.addColorStop(1,'#172026');ctx.fillStyle=sky;ctx.fillRect(0,-900,1200,2400);
    if(images.stage){const img=images.stage,scale=Math.max(1240/img.width,675/img.height);ctx.globalAlpha=.92;ctx.drawImage(img,(1200-img.width*scale)/2-offset*.12,(675-img.height*scale)/2,img.width*scale,img.height*scale);ctx.globalAlpha=1;rect(0,0,1200,675,'#10202a35');}
    /* Moving planes: clouds .04, painted plate / skyline .12, dust .3, arches .55, floor 1, foreground 1.2. */
    ctx.save();ctx.translate(-offset*.04,0);for(let i=0;i<6;i++){ellipse(180+i*240+Math.sin(decorFrame/600+i)*50,170+i%2*50,230,44,images.stage?'#8f9b9708':'#8f9b9720');}ctx.restore();
    if(!images.stage){
    ctx.save();ctx.translate(-offset*.12,0);for(let i=-1;i<12;i++){const x=i*125;const h=110+(i*47+230)%150;rect(x,440-h,100,h,'#26333b');rect(x+8,430-h,85,10,'#303e45');for(let j=0;j<6;j++)rect(x+13+(j%3)*28,457-h+Math.floor(j/3)*34,9,18,'#69716835');}ctx.restore();
    ctx.save();ctx.translate(-offset*.3,0);
    for(let i=-1;i<6;i++){const x=i*285+15;rect(x,235,205,280,'#1b272f');rect(x-7,225,220,18,'#4b5451');rect(x+20,211,167,13,'#354249');for(let j=0;j<4;j++){const wx=x+20+j*45;rect(wx,265,24,96,'#101c24');rect(wx+5,265,4,96,'#84948b19');rect(wx,386,24,83,'#0c1922');}rect(x,350,205,14,'#34424a');for(let j=0;j<7;j++)line(x,380+j*18,x+205,380+j*18,'#53626216');}
    ctx.restore();
    }
    ctx.save();ctx.translate(-offset*.55,0);
    if(!images.stage){
    for(const x of [-75,1070]){polygon([[x,118],[x+55,110],[x+82,505],[x-20,505]],'#17232c');rect(x-35,150,135,32,'#35424a');rect(x-23,450,115,55,'#27343d');rect(x-36,500,138,28,'#18242c');for(let i=0;i<4;i++)rect(x+9+i*13,188,6,245,'#45505645');}
    }else{for(const x of [36,1100])polygon([[x-40,534],[x-14,519],[x+11,524],[x+29,507],[x+58,534]],'#27333b90');}
    ctx.restore();
    const fog=ctx.createLinearGradient(0,350,0,545);fog.addColorStop(0,'#6b787900');fog.addColorStop(1,'#778b8c45');ctx.fillStyle=fog;ctx.fillRect(0,350,1200,195);
    polygon([[0,530],[1200,530],[1200,900],[0,900]],images.stage?'#10182030':'#202a30');line(0,545,1200,545,'#a2aaa780',2);line(0,550,1200,550,'#090f14',4);
    for(let i=-2;i<20;i++){const x=i*90-offset;line(x,548,x+55,675,'#a2aca217');}for(let i=0;i<5;i++)line(0,555+i*i*7,1200,555+i*i*7,'#a6ad9820');
    for(let i=0;i<18;i++){const x=((i*173+decorFrame*.25)%1300)-50-offset*.3,y=310+(i*83)%260;rect(x,y,2,2,'#cfb18a55');}
    rect(0,650,1200,80,'#0a111894');polygon([[0,625],[85-offset*1.2,615],[160-offset*1.2,642],[300-offset*1.2,650],[0,685]],'#0d171e');polygon([[930-offset*1.2,660],[1090-offset*1.2,622],[1200,638],[1200,700]],'#101920');
  }
  function character(actor,name,isEnemy){
    const x=actor.x,y=actor.y,flip=actor.facing,s=actor.h/146;
    ellipse(x,y+4,actor.w*.7,12,isEnemy?'#0a080860':'#080f166e');
    ctx.save();ctx.translate(x,y);ctx.scale(flip,1);
    const img=useIllustrations?images[name]:null;
    if(actor.dodge){ctx.translate(0,-8);ctx.rotate(flip*(30-actor.dodge)/30*Math.PI*2);ctx.scale(.7,.7);ctx.translate(0,25);}
    if(actor.flash&&Math.floor(actor.flash/2)%2)ctx.globalAlpha=.62;
    const bob=actor.attack?-Math.sin(Math.min(1,actor.attack.clock/14)*Math.PI)*4:Math.sin(decorFrame/20)*1.3;
    if(img){const h=actor.h+12,w=h*(img.width/img.height);ctx.drawImage(img,-w*.5,-h+bob,w,h);}
    else{
      ctx.translate(0,bob);ctx.scale(s,s);
      const a=isEnemy?'#554d4c':'#516370',b=isEnemy?'#28292f':'#253d4b',light=isEnemy?'#a37e61':'#9fc4d5';
      polygon([[-31,-87],[-7,-84],[-12,-30],[-11,-3],[-35,-3],[-33,-38]],b,'#82939a44');polygon([[6,-87],[31,-82],[34,-37],[41,-3],[14,-3],[8,-32]],a,'#82939a44');
      polygon([[-41,-123],[-11,-132],[25,-129],[42,-111],[30,-67],[-24,-69]],a,'#80929c66');polygon([[-16,-126],[22,-124],[19,-92],[-17,-94]],b,'#96a5aa55');
      rect(-21,-121,6,12,light);rect(15,-120,6,12,light);rect(-13,-80,30,10,'#1c282e');
      ellipse(4,-142,17,19,isEnemy?'#9c8b78':'#bfb1a2');polygon([[-14,-151],[8,-159],[20,-151],[20,-146],[-14,-145]],isEnemy?'#2b292b':'#171e26');rect(8,-143,9,4,'#293138');
      polygon([[-37,-119],[-52,-109],[-51,-80],[-28,-74],[-20,-85]],b,'#6e818a');polygon([[28,-118],[44,-110],[50,-91],[26,-85],[16,-100]],a,'#899a9f');
      const armY=actor.attack?-98:-83;polygon([[30,-110],[46,-102],[58,armY],[27,armY+7],[14,-96]],a,'#718892');
      rect(12,armY-5,79,13,'#121c23');rect(28,armY-10,40,11,'#53626b');rect(45,armY+5,16,10,'#13242c');polygon([[33,armY+10],[80,armY+10],[78,armY+15],[29,armY+15]],'#a0aeb0');
      if(isEnemy){polygon([[-31,-125],[-39,-145],[-20,-132]],'#777a77');polygon([[27,-125],[42,-143],[40,-117]],'#8d8b7d');}
    }
    ctx.restore();
    if(actor.guarding){ctx.strokeStyle='#9bd8e5aa';ctx.lineWidth=5;ctx.beginPath();ctx.arc(x+flip*22,y-80,63,flip>0?-1.4:1.7,flip>0?1.4:4.55);ctx.stroke();}
    if(actor.attack){const a=actor.attack,active=a.clock>=a.startup&&a.clock<a.startup+a.active;if(active){ctx.save();ctx.translate(x+flip*35,y-90);ctx.scale(flip,1);ctx.strokeStyle=isEnemy?'#ed6956':'#eac68e';ctx.lineWidth=a.type==='heavy'?12:7;ctx.beginPath();ctx.arc(0,0,a.reach*.6,-1,1);ctx.stroke();ctx.restore();}else if(a.clock<a.startup&&isEnemy){text('!',x,y-actor.h-16,30,'#ed7961','center');}}
  }
  function berserker(e){
    ellipse(e.x,E.FLOOR+5,85,17,'#04070980');ctx.save();ctx.translate(e.x,e.y);ctx.scale(e.facing,1);
    if(e.flash)ctx.globalAlpha=.7;
    if(images.berserker){const h=264,w=h*images.berserker.width/images.berserker.height;ctx.drawImage(images.berserker,-w/2,-h,w,h);}
    else{
      const body=e.vulnerable?'#847658':'#687474',edge=e.vulnerable?'#e2b76f':'#a0a8a2';
      polygon([[-52,-112],[-13,-105],[-15,-44],[-26,-3],[-66,-3],[-53,-48]],'#37494f',edge);polygon([[8,-109],[52,-104],[54,-43],[72,-4],[26,-4],[16,-40]],'#45565a',edge);
      polygon([[-61,-189],[-24,-212],[35,-210],[71,-178],[46,-95],[-41,-94]],body,edge);polygon([[-54,-184],[-78,-173],[-87,-119],[-82,-63],[-59,-57],[-49,-122]],body,edge);polygon([[51,-183],[84,-172],[100,-120],[95,-68],[73,-61],[59,-125]],body,edge);
      ellipse(9,-221,24,24,'#9eaa9b');polygon([[-17,-239],[-21,-252],[18,-250],[35,-229],[16,-222],[-6,-224]],'#586a67');for(let i=0;i<5;i++)line(-37+i*17,-197,-29+i*15,-121,edge,4);
      if(e.vulnerable)ellipse(0,-155,19,25,'#e4b660');
    }
    ctx.restore();
    if(e.vulnerable){ellipse(e.x,e.y-e.h*.6,12,12,'#f9ce7b');text('FAIBLESSE',e.x,e.y-e.h-20,15,'#f5cf8c','center');}
    if(e.state==='telegraph'){
      const pulse=.4+Math.sin(decorFrame/5)*.15;
      if(e.move==='slam'){ellipse(e.x,E.FLOOR,230,26,`rgba(224,82,53,${pulse})`);ctx.strokeStyle='#ff9e68';ctx.lineWidth=3;ctx.beginPath();ctx.ellipse(e.x,E.FLOOR,230,26,0,0,Math.PI*2);ctx.stroke();}
      else{rect(Math.min(e.x,e.targetX)-50,E.FLOOR-13,Math.abs(e.x-e.targetX)+100,13,`rgba(224,82,53,${pulse})`);for(let i=0;i<8;i++){const x=e.x+e.dir*(i*58+30);polygon([[x-14*e.dir,527],[x,536],[x-14*e.dir,545]],'#eb9a6c');}}
      text(e.move==='slam'?'ÉCRASEMENT':'CHARGE',e.x,e.y-e.h-40,19,'#f79976','center');
    }
  }
  function raven(e){
    const x=e.x,y=e.y;ellipse(x,E.FLOOR,130,14,'#0c141642');ctx.save();ctx.translate(x,y);if(e.flash)ctx.globalAlpha=.7;
    /* Temporary vehicle blockout, not a canon-validated model. */
    polygon([[-153,-24],[-123,-69],[22,-81],[98,-52],[91,6],[-90,20]],'#3d515b','#889a9d');polygon([[-148,-24],[-120,-61],[-71,-69],[-88,-19]],'#142b39','#66818a');polygon([[-66,-70],[-15,-74],[-12,-25],[-77,-22]],'#19333d','#80959b');rect(-20,-24,85,43,'#263d48');rect(5,-14,43,25,'#14252e');
    polygon([[83,-45],[228,-67],[258,-121],[275,-118],[265,-55],[116,-9]],'#344a54','#7a8b8a');line(258,-53,280,-25,'#647f84',5);
    rect(-19,-94,21,24,'#566e74');rect(-185,-105,365,7,'#9bb1ad88');line(-190,-98,183,-109,'#4a646b99',5);if(Math.floor(decorFrame)%4<2)rect(-195,-102,390,2,'#d7e1d0aa');
    line(-103,18,-115,38,'#243a45',8);line(69,13,78,38,'#243a45',8);line(-130,41,106,41,'#73878b',7);rect(-120,1,52,12,'#1d303b');rect(-72,5,20,29,'#2e454f');
    ellipse(37,-49,26,17,e.vulnerable?'#f6be63':'#102e38');if(e.vulnerable){ellipse(37,-49,11,9,'#fff0b1');ctx.strokeStyle='#ffd887';ctx.lineWidth=3;ctx.beginPath();ctx.arc(37,-49,39,0,Math.PI*2);ctx.stroke();}
    ctx.restore();if(e.vulnerable)text('MOTEUR EXPOSÉ',x+37,y-125,15,'#eeca8e','center');
  }
  function effects(){for(const z of game.zones){const pulse=.25+Math.sin(decorFrame/4)*.15;ellipse(z.x,E.FLOOR,z.radius,17,z.clock>0?`rgba(236,104,59,${pulse})`:'#ffc38faa');ctx.strokeStyle='#f4a06c';ctx.lineWidth=3;ctx.beginPath();ctx.ellipse(z.x,E.FLOOR,z.radius,17,0,0,Math.PI*2);ctx.stroke();if(z.clock>0){line(z.x,325,z.x,E.FLOOR,'#ef95666a',2);text((z.clock/60).toFixed(1),z.x,510,18,'#ffd3a4','center');}else{const fire=ctx.createLinearGradient(0,400,0,545);fire.addColorStop(0,'#ff983600');fire.addColorStop(1,'#ffad58b0');rect(z.x-z.radius*.6,400,z.radius*1.2,145,fire);}}
    for(const b of game.projectiles){line(b.x-b.vx*.8,b.y-b.vy*.8,b.x,b.y,b.owner==='enemy'?'#f48c6e':b.kind==='special'?'#f7c274':b.enhanced?'#b3e6ff':'#e6d9af',b.kind==='special'?10:4);if(b.kind==='special')ellipse(b.x,b.y,13,8,'#ffdb9a');}
    for(const p of game.particles){ctx.globalAlpha=Math.min(1,p.life/10);rect(p.x,p.y,4,4,p.color);}ctx.globalAlpha=1;
  }
  function ui(){
    if(screen==='playing'&&!game.paused){
      const p=game.player;
      if(p.reload){const r=p.reload,x=420,y=440,w=360,scale=Math.max(72,r.total);rect(x-15,y-30,w+30,70,'#0c141ae8');text(r.result==='jam'?'ENRAYAGE':r.locked?'CONFIRMÉ · CHARGEMENT':'RECHARGE ACTIVE · R',600,y-11,14,r.result==='jam'?'#e88c70':'#d0dfdb','center');rect(x,y,w,10,'#35444b');rect(x+w*27/scale,y,w*24/scale,10,'#95a7a7');rect(x+w*34/scale,y,w*10/scale,10,'#e8f1db');const px=x+w*r.clock/scale;rect(px-3,y-7,6,24,r.result==='jam'?'#e47452':'#f5f0cc');}
      const first=game.events[0];if(first){text(first.text,600,132,19,first.kind==='good'?'#e8c78c':first.kind==='bad'?'#f09a85':first.kind==='warning'?'#f2b893':'#d4e1df','center');}
      if(game.combo>=2){text(String(game.combo).padStart(2,'0'),65,230,39,'#e3bc87');text('SÉRIE',68,251,11,'#a6b2b3');}
      text('GARDE',28,645,9,'#9cb5be');text('SPÉCIAL '+Math.floor(p.meter)+' / 100',116,645,9,p.meter===100?'#f1c378':'#a6b4bb');
      const hint=game.tutorial||(game.mode==='duel'?'Gardez, esquivez et créez une ouverture.':'Attendez le signal doré pour infliger les dégâts complets.');
      rect(255,601,690,28,'#0d1820b0');text(hint,600,620,12,'#b4c7cc','center');
    }
  }
  function draw(){
    const rect=canvas.getBoundingClientRect(),desired=Math.round(1200*rect.height/rect.width);
    if(desired!==renderHeight&&desired>0){renderHeight=desired;canvas.height=renderHeight;}
    ctx.setTransform(1,0,0,1,0,0);ctx.clearRect(0,0,1200,renderHeight);
    const offY=(renderHeight-675)*.5;ctx.translate(0,offY);
    if(game.shake&&!game.paused)ctx.translate(Math.sin(game.frame*2.1)*game.shake*.4,Math.cos(game.frame*1.8)*game.shake*.2);
    background();
    if(game.mode==='raven')raven(game.enemy);
    if(game.mode==='berserker')berserker(game.enemy);
    if(game.mode==='duel')character(game.enemy,'raam',true);
    character(game.player,'marcus',false);effects();ui();
    if(screen==='menu'){const gradient=ctx.createLinearGradient(0,0,1200,0);gradient.addColorStop(0,'#081219a0');gradient.addColorStop(1,'#0d1c2500');ctx.fillStyle=gradient;ctx.fillRect(0,-offY,1200,renderHeight);}
    ctx.setTransform(1,0,0,1,0,0);
  }
  function loop(now){const elapsed=Math.min(100,now-(last||now));last=now;decorFrame+=elapsed/(1000/60);pollPad();if(screen==='playing'&&!game.paused){accumulator+=elapsed;while(accumulator>=1000/60){E.step(game,input());accumulator-=1000/60;if(game.state!=='playing'){result();break;}}}else accumulator=0;updateHUD();draw();requestAnimationFrame(loop);}
  // Explicit, narrow inspection hooks for deterministic QA; no network or storage side effects.
  window.GearsPrototype={start,choose,pause:togglePause,getState:()=>game,assets:images,setIllustrations:enabled=>{useIllustrations=!!enabled;$('show-illustration').checked=useIllustrations;},setAsset:(key,src)=>{const i=new Image();i.onload=()=>{images[key]=i;if(key==='marcus')$('illustration-control').hidden=false;};i.src=src;}};
  choose('duel');requestAnimationFrame(loop);
})();
