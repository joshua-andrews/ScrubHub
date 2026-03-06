
with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# PART A: Add CSS for particle chip system + Hammer of Dawn
# ============================================================
new_css = '''
        /* PARTICLE CHIP SYSTEM */
        .chip-particle {
            position: absolute;
            pointer-events: none;
            z-index: 60;
            border-radius: 2px;
            animation: chipFly 0.8s ease-out forwards;
        }
        @keyframes chipFly {
            0% { opacity: 1; transform: translate(0,0) rotate(0deg); }
            100% { opacity: 0; transform: translate(var(--dx),var(--dy)) rotate(var(--rot)) scale(0.1); }
        }
        .shotgun-hint {
            position: absolute;
            bottom: 80px;
            width: 100%;
            text-align: center;
            font-family: 'Share Tech Mono';
            font-size: 1rem;
            color: rgba(255,42,42,0.7);
            pointer-events: none;
            z-index: 55;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse { 0%,100%{opacity:0.4;} 50%{opacity:1;} }

        /* CROSSHAIR CURSOR */
        #slide-9 { cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 40 40'%3E%3Ccircle cx='20' cy='20' r='18' stroke='%23ff2a2a' stroke-width='1.5' fill='none'/%3E%3Cline x1='20' y1='2' x2='20' y2='12' stroke='%23ff2a2a' stroke-width='1.5'/%3E%3Cline x1='20' y1='28' x2='20' y2='38' stroke='%23ff2a2a' stroke-width='1.5'/%3E%3Cline x1='2' y1='20' x2='12' y2='20' stroke='%23ff2a2a' stroke-width='1.5'/%3E%3Cline x1='28' y1='20' x2='38' y2='20' stroke='%23ff2a2a' stroke-width='1.5'/%3E%3Ccircle cx='20' cy='20' r='2' fill='%23ff2a2a'/%3E%3C/svg%3E") 20 20, crosshair; }

        /* HAMMER OF DAWN */
        .hod-enemy {
            position: absolute;
            font-family: 'Share Tech Mono';
            font-size: 0.85rem;
            color: #ff2a2a;
            text-align: center;
            cursor: crosshair;
            user-select: none;
            padding: 8px 12px;
            border: 1px solid #500;
            background: rgba(20,0,0,0.8);
            transition: none;
            z-index: 20;
            text-shadow: 0 0 8px rgba(255,0,0,0.5);
            white-space: nowrap;
        }
        .hod-enemy.hit {
            animation: enemyHit 0.3s ease-out forwards;
        }
        .hod-enemy.dead {
            display: none;
        }
        @keyframes enemyHit {
            0% { transform: scale(1); filter: brightness(3); }
            50% { transform: scale(1.3); }
            100% { transform: scale(1); filter: brightness(1); }
        }
        .hod-beam {
            position: fixed;
            width: 4px;
            background: linear-gradient(to bottom, transparent, #ff6600, #ff2a2a, #fff);
            transform-origin: top center;
            pointer-events: none;
            z-index: 999;
            box-shadow: 0 0 20px #ff4400, 0 0 40px #ff2a2a;
            animation: beamFire 0.4s ease-out forwards;
        }
        @keyframes beamFire {
            0% { opacity: 1; width: 6px; }
            100% { opacity: 0; width: 2px; }
        }
        .hod-explosion {
            position: fixed;
            border-radius: 50%;
            pointer-events: none;
            z-index: 998;
            background: radial-gradient(circle, #fff 0%, #ff6600 30%, #ff2a2a 60%, transparent 100%);
            animation: explode 0.5s ease-out forwards;
        }
        @keyframes explode {
            0% { transform: translate(-50%,-50%) scale(0); opacity: 1; }
            100% { transform: translate(-50%,-50%) scale(3); opacity: 0; }
        }
        #hod-health-bar {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            width: 400px;
            height: 20px;
            border: 2px solid #ff2a2a;
            background: #1a0000;
            z-index: 30;
        }
        #hod-health-fill {
            height: 100%;
            background: linear-gradient(to right, #ff2a2a, #ff6600);
            width: 100%;
            transition: width 0.4s ease;
            box-shadow: 0 0 15px #ff2a2a;
        }
        #hod-status {
            position: absolute;
            bottom: 58px;
            width: 100%;
            text-align: center;
            font-family: 'Anton';
            font-size: 1.3rem;
            color: #ff2a2a;
            letter-spacing: 2px;
            z-index: 30;
            text-shadow: 0 0 10px rgba(255,0,0,0.8);
        }
        #hod-ammo {
            position: absolute;
            top: 30px;
            right: 40px;
            font-family: 'Share Tech Mono';
            font-size: 1rem;
            color: #ff6600;
            z-index: 30;
        }
        #hod-targeting-reticle {
            position: fixed;
            pointer-events: none;
            z-index: 997;
            border: 2px solid #ff6600;
            border-radius: 50%;
            width: 60px; height: 60px;
            box-shadow: 0 0 20px #ff4400;
            display: none;
            animation: reticleAnim 0.1s ease-in-out;
        }
        @keyframes reticleAnim {
            0%  { transform: translate(-50%,-50%) scale(2); opacity:0; }
            100%{ transform: translate(-50%,-50%) scale(1); opacity:1; }
        }
'''

html = html.replace('    </style>', new_css + '\n    </style>')

# ============================================================
# PART B: Add <div> for Hammer of Dawn inside slide-16 content
# ============================================================
old_s16_content = '''        <div class="content" id="content-16">
            <div class="slide-subtitle">Chapter 5: Execution Details</div>
            <h1 class="slide-header">Investment &amp; ROI Model</h1>'''

new_s16_content = '''        <!-- HAMMER OF DAWN BOSS BATTLE -->
        <div id="hod-arena" style="position:absolute;top:0;left:0;width:100%;height:100%;display:none;z-index:25;overflow:hidden;">
            <div id="hod-status">ELIMINATE THE COMPETITION TO UNLOCK INVESTMENT DETAILS</div>
            <div id="hod-ammo">🎯 HAMMER OF DAWN — CLICK ENEMIES TO STRIKE</div>
            <div id="hod-health-bar"><div id="hod-health-fill"></div></div>
            <div id="hod-targeting-reticle"></div>
        </div>

        <div class="content" id="content-16" style="display:none;">
            <div class="slide-subtitle">Chapter 5: Execution Details</div>
            <h1 class="slide-header">Investment &amp; ROI Model</h1>'''

html = html.replace(old_s16_content, new_s16_content)

# close the hidden content-16 after last closing div of slide-16
# Need to find the closing/end of slide-16 and mark content-16 properly
# Actually just ensure the closing bracket pattern is matched
# (content already ends with </div></div> from the HTML)

# ============================================================
# PART C: Replace the old fireShotgun and add new JS
# ============================================================
old_shotgun_js = '''        let shotgunShots = 0;
        function fireShotgun(event) {
            if(shotgunShots >= 3) return;
            shotgunShots++;
            
            let fxBox = document.getElementById('shotgun-fx-container');
            let slide = document.getElementById('slide-9');
            let title = document.getElementById('swot-target-title');
            
            let rect = slide.getBoundingClientRect();
            let x = event.clientX - rect.left;
            let y = event.clientY - rect.top;

            let flash = document.createElement('div');
            flash.className = 'flash';
            flash.style.left = x + 'px';
            flash.style.top = y + 'px';
            fxBox.appendChild(flash);

            let blood = document.createElement('div');
            blood.className = 'blood-splatter';
            blood.style.left = x + 'px';
            blood.style.top = y + 'px';
            fxBox.appendChild(blood);

            let hole = document.createElement('div');
            hole.className = 'bullet-hole';
            hole.style.left = x + 'px';
            hole.style.top = y + 'px';
            fxBox.appendChild(hole);

            slide.classList.add('shaking');
            setTimeout(() => slide.classList.remove('shaking'), 200);

            title.style.opacity = Math.max(0, 1 - (shotgunShots * 0.34));

            if(shotgunShots === 3) {
                setTimeout(() => {
                    nextSlide(parseInt(currentSlideIndex) + 1);
                }, 800);
            }
        }'''

new_shotgun_js = '''        // ---- PARTICLE CHIP SHOTGUN SYSTEM ----
        let shotgunChips = 100; // percentage of title remaining
        let shotgunDone = false;
        let shotgunHint = null;

        function initShotgunSlide() {
            shotgunChips = 100;
            shotgunDone = false;
            let title = document.getElementById('swot-target-title');
            title.style.opacity = '1';
            title.style.filter = '';
            // Add hint
            if (!shotgunHint) {
                shotgunHint = document.createElement('div');
                shotgunHint.className = 'shotgun-hint';
                shotgunHint.innerHTML = '[ CLICK TO DESTROY THE TARGET — UNLEASH EVERY ROUND ]';
                document.getElementById('slide-9').appendChild(shotgunHint);
            }
            shotgunHint.style.display = 'block';
        }

        function fireShotgun(event) {
            if(shotgunDone) return;

            let fxBox = document.getElementById('shotgun-fx-container');
            let slide = document.getElementById('slide-9');
            let title = document.getElementById('swot-target-title');

            let rect = slide.getBoundingClientRect();
            let x = event.clientX - rect.left;
            let y = event.clientY - rect.top;

            // Play shotgun sound
            let snd = document.getElementById('shotgun-sound');
            if(snd) { snd.currentTime = 0; snd.volume = 0.8; snd.play().catch(()=>{}); }

            // Screen shake
            slide.classList.add('shaking');
            setTimeout(() => slide.classList.remove('shaking'), 150);

            // Muzzle flash
            let flash = document.createElement('div');
            flash.className = 'flash';
            flash.style.left = x + 'px';
            flash.style.top = y + 'px';
            fxBox.appendChild(flash);
            setTimeout(() => flash.remove(), 200);

            // Spread: 12-18 particles per shot
            let numParticles = 14 + Math.floor(Math.random() * 6);
            for(let i = 0; i < numParticles; i++) {
                let chip = document.createElement('div');
                chip.className = 'chip-particle';
                let size = 4 + Math.random() * 10;
                chip.style.width = size + 'px';
                chip.style.height = size + 'px';
                chip.style.left = (x - size/2 + (Math.random()-0.5)*30) + 'px';
                chip.style.top  = (y - size/2 + (Math.random()-0.5)*20) + 'px';
                chip.style.background = Math.random() > 0.5 ? '#fff' : '#ff2a2a';
                let angle = Math.random() * 360;
                let dist = 60 + Math.random() * 160;
                chip.style.setProperty('--dx', (Math.cos(angle * Math.PI/180) * dist) + 'px');
                chip.style.setProperty('--dy', (Math.sin(angle * Math.PI/180) * dist + 40) + 'px');
                chip.style.setProperty('--rot', (Math.random() * 720 - 360) + 'deg');
                chip.style.animationDuration = (0.5 + Math.random() * 0.5) + 's';
                fxBox.appendChild(chip);
                setTimeout(() => chip.remove(), 1100);
            }

            // Chip away at the title (each shot removes 8-15%)
            let damage = 8 + Math.random() * 7;
            shotgunChips = Math.max(0, shotgunChips - damage);
            title.style.opacity = (shotgunChips / 100).toFixed(2);
            title.style.filter = shotgunChips < 40 ? `blur(${(40-shotgunChips)/15}px)` : '';

            // Red tint overlay grows
            let frac = (100 - shotgunChips) / 100;
            slide.style.background = `rgba(${Math.floor(frac*60)},0,0,1)`;

            if(shotgunChips <= 0 && !shotgunDone) {
                shotgunDone = true;
                if(shotgunHint) shotgunHint.style.display = 'none';
                // Big finale flash
                let bigFlash = document.createElement('div');
                bigFlash.style.cssText = 'position:absolute;top:0;left:0;width:100%;height:100%;background:#fff;z-index:100;pointer-events:none;animation:flashOut 0.6s forwards;';
                slide.appendChild(bigFlash);
                slide.style.background = '';
                setTimeout(() => {
                    bigFlash.remove();
                    nextSlide(parseInt(currentSlideIndex) + 1);
                }, 700);
            }
        }

        // ---- HAMMER OF DAWN BOSS BATTLE ----
        let hodActive = false;
        let hodEnemies = [];
        let hodAnimFrame = null;
        let hodKills = 0;
        const HOD_ENEMIES = ['Mister Car Wash', 'EverWash', 'Glaze Car Wash'];
        const HOD_MAX_HITS = 3;

        function initHammerOfDawn() {
            hodActive = true;
            hodKills = 0;
            let arena = document.getElementById('hod-arena');
            let content16 = document.getElementById('content-16');
            let healthBar = document.getElementById('hod-health-fill');
            let statusEl = document.getElementById('hod-status');

            arena.style.display = 'block';
            content16.style.display = 'none';
            healthBar.style.width = '100%';
            statusEl.innerHTML = 'HAMMER OF DAWN ACTIVATED — TAKE OUT THE COMPETITION';

            // Clear old enemies
            arena.querySelectorAll('.hod-enemy').forEach(e => e.remove());
            hodEnemies = [];

            HOD_ENEMIES.forEach((name, i) => {
                let el = document.createElement('div');
                el.className = 'hod-enemy';
                el.innerHTML = '⚠ ' + name.toUpperCase() + ' ⚠';
                el.dataset.name = name;
                el.dataset.hits = 0;
                el.style.left = (20 + i * 28) + '%';
                el.style.top  = (20 + i * 18) + '%';
                el.onclick = (ev) => { ev.stopPropagation(); strikeEnemy(el, ev); };
                arena.appendChild(el);
                
                hodEnemies.push({
                    el: el,
                    x: parseFloat(el.style.left),
                    y: parseFloat(el.style.top),
                    vx: (Math.random() - 0.5) * 0.4,
                    vy: (Math.random() - 0.5) * 0.3,
                    dead: false,
                    hits: 0
                });
            });

            animateEnemies();
        }

        function animateEnemies() {
            if(!hodActive) return;
            let arena = document.getElementById('hod-arena');
            let arenaW = arena.offsetWidth;
            let arenaH = arena.offsetHeight;
            let speedMult = 1 + hodKills * 0.7; // faster with each kill

            hodEnemies.forEach(e => {
                if(e.dead) return;
                e.x += e.vx * speedMult;
                e.y += e.vy * speedMult;
                // Bounce off edges
                if(e.x < 2 || e.x > 80) e.vx *= -1;
                if(e.y < 5 || e.y > 75) e.vy *= -1;
                e.x = Math.max(2, Math.min(80, e.x));
                e.y = Math.max(5, Math.min(75, e.y));
                e.el.style.left = e.x + '%';
                e.el.style.top  = e.y + '%';
            });
            hodAnimFrame = requestAnimationFrame(animateEnemies);
        }

        function strikeEnemy(el, event) {
            let enemyData = hodEnemies.find(e => e.el === el);
            if(!enemyData || enemyData.dead) return;

            enemyData.hits++;
            let pct = enemyData.hits / HOD_MAX_HITS;
            el.style.opacity = (1 - pct * 0.6).toFixed(2);
            el.style.borderColor = pct >= 1 ? '#fff' : '#ff6600';
            el.classList.add('hit');
            setTimeout(() => el.classList.remove('hit'), 300);

            // Fire the beam
            let rect = el.getBoundingClientRect();
            let cx = rect.left + rect.width/2;
            let cy = rect.top + rect.height/2;
            fireHodBeam(cx, cy);

            // Explosion on target
            let exp = document.createElement('div');
            exp.className = 'hod-explosion';
            exp.style.left = cx + 'px';
            exp.style.top  = cy + 'px';
            exp.style.width = '80px'; exp.style.height = '80px';
            document.body.appendChild(exp);
            setTimeout(() => exp.remove(), 600);

            if(enemyData.hits >= HOD_MAX_HITS) {
                // Kill it
                enemyData.dead = true;
                el.classList.add('dead');
                hodKills++;

                // Update health bar
                let pctLeft = (HOD_ENEMIES.length - hodKills) / HOD_ENEMIES.length;
                document.getElementById('hod-health-fill').style.width = (pctLeft * 100) + '%';

                let statusEl = document.getElementById('hod-status');
                if(hodKills < HOD_ENEMIES.length) {
                    statusEl.innerHTML = `TARGET NEUTRALIZED — ${HOD_ENEMIES.length - hodKills} REMAINING`;
                } else {
                    // All dead — victory!
                    hodActive = false;
                    cancelAnimationFrame(hodAnimFrame);
                    statusEl.innerHTML = '✓ COMPETITION ELIMINATED';
                    document.getElementById('hod-health-fill').style.width = '0%';
                    document.getElementById('hod-health-fill').style.background = '#00ff00';
                    setTimeout(() => {
                        document.getElementById('hod-arena').style.display = 'none';
                        let c = document.getElementById('content-16');
                        c.style.display = '';
                        c.classList.add('revealed');
                    }, 1200);
                }
            }
        }

        function fireHodBeam(tx, ty) {
            // Beam from top of screen down to target
            let beam = document.createElement('div');
            beam.className = 'hod-beam';
            let startX = tx;
            let startY = 0;
            let length = ty;
            beam.style.left = startX + 'px';
            beam.style.top  = startY + 'px';
            beam.style.height = length + 'px';
            document.body.appendChild(beam);
            setTimeout(() => beam.remove(), 450);

            // Targeting reticle
            let ret = document.getElementById('hod-targeting-reticle');
            ret.style.left = tx + 'px';
            ret.style.top  = ty + 'px';
            ret.style.display = 'block';
            setTimeout(() => { ret.style.display = 'none'; }, 400);
        }'''

html = html.replace(old_shotgun_js, new_shotgun_js)

# ============================================================
# PART D: Wire up initShotgunSlide and initHammerOfDawn in nextSlide
# ============================================================
html = html.replace(
    "            if(num === 2) {\n                // Slide 2 is Agenda\n                revealContent(num);",
    """            if(num === 2) {
                // Slide 2 is Agenda
                revealContent(num);"""
)

# Add call to initShotgunSlide when navigating to slide-9
html = html.replace(
    "document.querySelectorAll('.slide').forEach(s => s.classList.remove('active-slide'));\n            document.getElementById('slide-' + num).classList.add('active-slide');\n            currentSlideIndex = num;\n            updateNav();",
    """document.querySelectorAll('.slide').forEach(s => s.classList.remove('active-slide'));
            let slideEl = document.getElementById('slide-' + num);
            if(!slideEl) return;
            slideEl.classList.add('active-slide');
            currentSlideIndex = num;
            updateNav();"""
)

# Add shotgun init + HoD init after setActiveSlide
old_nextslide_tail = "            const nextSlideElement = document.getElementById('slide-' + num);"
new_nextslide_tail = """            const nextSlideElement = document.getElementById('slide-' + num);
            // Shotgun slide init
            if(num === 9) { setTimeout(initShotgunSlide, 100); }
            // Hammer of Dawn boss battle
            if(num === 16) { setTimeout(initHammerOfDawn, 200); }"""

html = html.replace(old_nextslide_tail, new_nextslide_tail, 1)

# ============================================================
# PART E: Add @keyframes flashOut CSS
# ============================================================
html = html.replace(
    '@keyframes muzzleFlash { 0% { opacity: 1; transform: translate(-50%, -50%) scale(0.5); } 100% { opacity: 0; transform: translate(-50%, -50%) scale(1.5); } }',
    '@keyframes muzzleFlash { 0% { opacity: 1; transform: translate(-50%, -50%) scale(0.5); } 100% { opacity: 0; transform: translate(-50%, -50%) scale(1.5); } }\n        @keyframes flashOut { 0% { opacity: 1; } 100% { opacity: 0; } }'
)

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Game mechanics injection complete!")
