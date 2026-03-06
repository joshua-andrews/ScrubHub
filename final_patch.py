html = open('scrubhub_tactical_pitch.html', encoding='utf-8').read()

# ============================================================
# 1. AUDIO: Switch to final trimmed shotgun clip
# ============================================================
html = html.replace(
    'src="shotgun_v2.mp3"',
    'src="shotgun_final.mp3"'
)

# ============================================================
# 2. WEBSITE AUDIT SLIDE: Add 3 photo buttons at the bottom
# ============================================================
old_audit_close = '''
        </div>
    </div>

    <!-- SLIDE 4B: WEBSITE AUDIT EVIDENCE -->'''

new_audit_close = '''
            <!-- Click-to-view photo buttons -->
            <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; margin-top:12px;">
                <div class="hud-box gallery-item" style="padding:12px 8px; cursor:pointer; border-color:#500; text-align:center; transition:all 0.2s;"
                    onclick="openLightbox('Photos/Hero section.jpeg')"
                    onmouseover="this.style.borderColor='#ff2a2a'" onmouseout="this.style.borderColor='#500'">
                    <p class="hud-font red-text" style="font-size:0.8rem; margin:0;">🎯 VIEW HERO SECTION →</p>
                </div>
                <div class="hud-box gallery-item" style="padding:12px 8px; cursor:pointer; border-color:#500; text-align:center; transition:all 0.2s;"
                    onclick="openLightbox('Photos/Veteran section.jpeg')"
                    onmouseover="this.style.borderColor='#ff2a2a'" onmouseout="this.style.borderColor='#500'">
                    <p class="hud-font red-text" style="font-size:0.8rem; margin:0;">🎖️ VIEW VETERAN SECTION →</p>
                </div>
                <div class="hud-box gallery-item" style="padding:12px 8px; cursor:pointer; border-color:#500; text-align:center; transition:all 0.2s;"
                    onclick="openLightbox('Photos/Family Section.jpeg')"
                    onmouseover="this.style.borderColor='#ff2a2a'" onmouseout="this.style.borderColor='#500'">
                    <p class="hud-font red-text" style="font-size:0.8rem; margin:0;">👨‍👩‍👧 VIEW FAMILY SECTION →</p>
                </div>
            </div>

        </div>
    </div>

    <!-- SLIDE 4B: WEBSITE AUDIT EVIDENCE -->'''

html = html.replace(old_audit_close, new_audit_close, 1)

# ============================================================
# 3. TEXT-SHATTER PARTICLE SYSTEM: Make text visually break
# ============================================================
old_shard_detect = '''        // TEXT-side particles: chips fly off the title text
            let titleRect = title.getBoundingClientRect();
            let slideRect = slide.getBoundingClientRect();
            let textChips = 12 + Math.floor(Math.random() * 8);
            for(let i = 0; i < textChips; i++) {
                let chip = document.createElement('div');
                chip.className = 'chip-particle';
                // Random position along the title text bbox
                let tx = (titleRect.left - slideRect.left) + Math.random() * titleRect.width;
                let ty = (titleRect.top  - slideRect.top)  + Math.random() * titleRect.height;
                let size = 5 + Math.random() * 12;
                chip.style.width  = size + 'px';
                chip.style.height = (size * (0.4 + Math.random()*0.6)) + 'px';
                chip.style.borderRadius = '1px';
                chip.style.left = tx + 'px';
                chip.style.top  = ty + 'px';
                // Colours sampled from title (white, dim white, gray)
                let colors = ['#fff','#ddd','#aaa','#ff2a2a','#ff6600'];
                chip.style.background = colors[Math.floor(Math.random()*colors.length)];
                let angle = -90 + (Math.random()-0.5)*180; // mostly upward/outward
                let dist  = 40 + Math.random() * 120;
                chip.style.setProperty('--dx', (Math.cos(angle*Math.PI/180)*dist)+'px');
                chip.style.setProperty('--dy', (-Math.abs(Math.sin(angle*Math.PI/180)*dist)-20)+'px');
                chip.style.setProperty('--rot', (Math.random()*900-450)+'deg');
                chip.style.animationDuration = (0.5+Math.random()*0.6)+'s';
                fxBox.appendChild(chip);
                setTimeout(() => chip.remove(), 1200);
            }'''

new_shard_detect = '''        // TEXT-SHATTER: Bold letter-sized chunks break off the title
            let titleRect = title.getBoundingClientRect();
            let slideRect = slide.getBoundingClientRect();
            // Spawn fragments that look like letter blocks
            let textChips = 18 + Math.floor(Math.random() * 10);
            for(let i = 0; i < textChips; i++) {
                let chip = document.createElement('div');
                chip.className = 'chip-particle';
                // Random position tightly overlapping the title rect
                let tx = (titleRect.left - slideRect.left) + Math.random() * titleRect.width;
                let ty = (titleRect.top  - slideRect.top)  + Math.random() * titleRect.height * 0.8;
                // Letter-block sized chunks (tall rectangles like letters breaking)
                let w = 12 + Math.random() * 30;
                let h = 30 + Math.random() * 40;
                chip.style.width  = w + 'px';
                chip.style.height = h + 'px';
                chip.style.borderRadius = '2px';
                chip.style.left = (tx - w/2) + 'px';
                chip.style.top  = (ty - h/2) + 'px';
                // Bright white chunks with red accent
                let colors = ['#ffffff','#ffffff','#eeeeee','#ff2a2a','#ffaa00'];
                chip.style.background = colors[Math.floor(Math.random()*colors.length)];
                chip.style.opacity = '0.9';
                // Explode outward in all directions but mostly away from center
                let angle = Math.random() * 360;
                let dist  = 80 + Math.random() * 200;
                chip.style.setProperty('--dx', (Math.cos(angle*Math.PI/180)*dist)+'px');
                chip.style.setProperty('--dy', (Math.sin(angle*Math.PI/180)*dist - 60)+'px');
                chip.style.setProperty('--rot', (Math.random()*1080-540)+'deg');
                chip.style.animationDuration = (0.6+Math.random()*0.7)+'s';
                fxBox.appendChild(chip);
                setTimeout(() => chip.remove(), 1400);
            }'''

html = html.replace(old_shard_detect, new_shard_detect)

# ============================================================
# 4. NEW FEATURES SLIDE: Reduce font to fit without overflow
# ============================================================
html = html.replace(
    '<div class="slide-subtitle">Chapter 3: The Hammer of ScrubHub</div>\n            <h1 class="slide-header">New Features</h1>',
    '<div class="slide-subtitle">Chapter 3: The Hammer of ScrubHub</div>\n            <h1 class="slide-header" style="margin-bottom:8px;">New Features</h1>'
)
# Shrink the feature grid font slightly
html = html.replace(
    'id="content-11">', 
    'id="content-11" style="overflow:hidden;">'
)

# ============================================================
# 5. REPLACE TECHNICAL ARCHITECTURE (slide-12) with MARKETING SLIDE
#    AND INSERT Chapter 4 Title Slide before it
# ============================================================

# Find old slide-12 block
idx_s12_start = html.find('\n    <!-- SLIDE 12: TECHNICAL ARCHITECTURE -->')
idx_s12_end   = html.find('\n    <!-- SLIDE 13:', idx_s12_start)

if idx_s12_start > -1 and idx_s12_end > -1:
    ch4_and_marketing = '''
    <!-- CHAPTER 4 TITLE: MARKETING OVERVIEW -->
    <div class="slide" id="slide-ch4" style="position:relative;">
        <div class="game-overlay" id="overlay-ch4">
            <div class="instructions">[ ACTIVE RELOAD — PRESS SPACE AT THE RIGHT MOMENT ]</div>
            <div id="reload-status-ch4" style="font-family: 'Share Tech Mono'; color: #ff2a2a; font-size: 2rem; margin: 20px 0; text-shadow: 0 0 10px #ff0000;">PRESS SPACE TO RELOAD</div>
            <div id="reload-bar-container-ch4" style="width: 400px; height: 30px; border: 2px solid #500; background: #1a0000; position: relative;">
                <div id="reload-sweet-spot-ch4" style="position: absolute; height: 100%; top: 0; background: rgba(255,42,42,0.5); width: 60px; left: 250px;"></div>
                <div id="reload-slider-ch4" style="position: absolute; height: 100%; width: 10px; background: #fff; top: 0; left: 0;"></div>
            </div>
        </div>
        <div class="content" id="content-ch4" style="text-align:center; display:flex; flex-direction:column; justify-content:center; height:100%; align-items:center;">
            <div class="slide-subtitle" style="font-size:1.5rem; margin-bottom:20px;">CHAPTER 4</div>
            <h1 class="slide-header" style="border:none; font-size:5rem; margin-bottom:0;">Marketing Overview</h1>
        </div>
    </div>

    <!-- SLIDE 12: MARKETING ENGINE -->
    <div class="slide" id="slide-12">
        <div class="content" id="content-12">
            <div class="slide-subtitle">Chapter 4: Marketing Overview</div>
            <h1 class="slide-header">Our Marketing Engine</h1>
            <p style="font-size:0.9rem; margin-bottom:10px;">A full-stack growth system that runs in the background — attracting, converting, and retaining customers automatically.</p>
            <div class="hud-grid">
                <div class="hud-box">
                    <h3 class="red-text">Acquisition Automations</h3>
                    <p style="font-size:0.9rem;">A website pop-up captures new visitor emails, triggering a <strong>Welcome Series</strong> — automated emails that introduce ScrubHub and push toward the first membership sign-up.</p>
                </div>
                <div class="hud-box">
                    <h3 class="red-text">Abandoned Checkout Recovery</h3>
                    <p style="font-size:0.9rem;">If someone starts the membership flow and doesn't complete it, an <strong>abandoned cart sequence</strong> fires automatically to recover that revenue before it's gone.</p>
                </div>
                <div class="hud-box">
                    <h3 class="red-text">App Push Notifications</h3>
                    <p style="font-size:0.9rem;">App users who open and click but don't purchase receive a <strong>targeted push notification</strong> within 24 hours with a personalized offer to close the loop.</p>
                </div>
                <div class="hud-box">
                    <h3 class="red-text">Unlimited Campaign Execution</h3>
                    <p style="font-size:0.9rem;">We handle unlimited email design and automations. You bring the campaign idea — we design, you approve, we send. Lightning deals, seasonal pushes, weather-triggered alerts — all handled.</p>
                </div>
            </div>
        </div>
    </div>'''

    html = html[:idx_s12_start] + ch4_and_marketing + html[idx_s12_end:]

# ============================================================
# 6. ADD CHAPTER 5 TITLE SLIDE before implementation timeline
#    (only if not already there as slide-ch5)
# ============================================================
if 'id="slide-ch5"' not in html:
    ch5_title = '''
    <!-- CHAPTER 5 TITLE: EXECUTION DETAILS -->
    <div class="slide" id="slide-ch5" style="position:relative;">
        <div class="game-overlay" id="overlay-ch5">
            <div class="instructions">[ ACTIVE RELOAD — PRESS SPACE AT THE RIGHT MOMENT ]</div>
            <div id="reload-status-ch5" style="font-family: 'Share Tech Mono'; color: #ff2a2a; font-size: 2rem; margin: 20px 0; text-shadow: 0 0 10px #ff0000;">PRESS SPACE TO RELOAD</div>
            <div id="reload-bar-container-ch5" style="width: 400px; height: 30px; border: 2px solid #500; background: #1a0000; position: relative;">
                <div id="reload-sweet-spot-ch5" style="position: absolute; height: 100%; top: 0; background: rgba(255,42,42,0.5); width: 60px; left: 250px;"></div>
                <div id="reload-slider-ch5" style="position: absolute; height: 100%; width: 10px; background: #fff; top: 0; left: 0;"></div>
            </div>
        </div>
        <div class="content" id="content-ch5" style="text-align:center; display:flex; flex-direction:column; justify-content:center; height:100%; align-items:center;">
            <div class="slide-subtitle" style="font-size:1.5rem; margin-bottom:20px;">CHAPTER 5</div>
            <h1 class="slide-header" style="border:none; font-size:5rem; margin-bottom:0;">Execution Details</h1>
        </div>
    </div>

'''
    html = html.replace(
        '    <!-- SLIDE 14: IMPLEMENTATION TIMELINE -->',
        ch5_title + '    <!-- SLIDE 14: IMPLEMENTATION TIMELINE -->'
    )

# ============================================================
# 7. BOSS FIGHT: Replace Final Chapter title slide + arena
#    with auto-launch (enemies appear after 2s timeout)
# ============================================================

# Remove the old slide-final-ch (plain title) if present,
# keeping only the arena slide (slide-16) which has the HoD arena inside it.
# Make slide-16 be the combined title+arena slide that auto-starts.

# First check if slide-final-ch exists
if 'id="slide-final-ch"' in html:
    # Remove it — we'll merge it into slide-16
    start_fc = html.find('\n    <!-- FINAL CHAPTER: BOSS FIGHT -->')
    end_fc   = html.find('\n    <!-- SLIDE 17:', start_fc)
    if start_fc > -1 and end_fc > -1:
        html = html[:start_fc] + html[end_fc:]

# Now rebuild slide-16 to be the combined boss fight slide
# Find where slide-16 begins
idx_s16 = html.find('\n    <!-- SLIDE 16:')
idx_s17 = html.find('\n    <!-- SLIDE 17:', idx_s16+1)

if idx_s16 > -1 and idx_s17 > -1:
    boss_slide = '''
    <!-- FINAL CHAPTER: BOSS FIGHT (slide-16) -->
    <div class="slide" id="slide-16" style="position:relative; cursor:crosshair;">
        <!-- Pre-battle title (fades out after 2s) -->
        <div id="hod-title-screen" style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:30;display:flex;flex-direction:column;justify-content:center;align-items:center;background:#0a0000;transition:opacity 0.8s;">
            <div class="slide-subtitle" style="font-size:1.5rem; color:#ff2a2a; margin-bottom:15px;">FINAL CHAPTER</div>
            <h1 style="font-family:'Anton'; font-size:7rem; color:#fff; margin:0; text-shadow:0 0 30px rgba(255,255,255,0.3);">Boss Fight</h1>
        </div>

        <!-- Battle arena -->
        <div id="hod-arena" style="position:absolute;top:0;left:0;width:100%;height:100%;display:block;z-index:20;overflow:hidden;opacity:0;transition:opacity 0.5s;">
            <div id="hod-status" style="position:absolute;top:30px;width:100%;text-align:center;font-family:'Anton';font-size:1.3rem;color:#ff2a2a;letter-spacing:2px;z-index:30;text-shadow:0 0 10px rgba(255,0,0,0.8);">ELIMINATE THE COMPETITION</div>
            <div id="hod-ammo" style="position:absolute;top:30px;right:40px;font-family:'Share Tech Mono';font-size:0.9rem;color:#ff6600;z-index:30;">🎯 HAMMER OF DAWN — CLICK TO STRIKE</div>
            <div id="hod-health-bar" style="position:absolute;bottom:30px;left:50%;transform:translateX(-50%);width:400px;height:20px;border:2px solid #ff2a2a;background:#1a0000;z-index:30;">
                <div id="hod-health-fill" style="height:100%;background:linear-gradient(to right,#ff2a2a,#ff6600);width:100%;transition:width 0.4s ease;box-shadow:0 0 15px #ff2a2a;"></div>
            </div>
            <div id="hod-targeting-reticle" style="position:fixed;pointer-events:none;z-index:997;border:2px solid #ff6600;border-radius:50%;width:60px;height:60px;box-shadow:0 0 20px #ff4400;display:none;transform:translate(-50%,-50%);"></div>
        </div>
    </div>

'''
    html = html[:idx_s16] + boss_slide + html[idx_s17:]

# ============================================================
# 8. BOSS FIGHT JS: Update initHammerOfDawn to auto-fade title
#    and show arena after 2 seconds; also fix nextSlide to
#    trigger it when slide-16 is entered
# ============================================================

old_hod_init = '''        function initHammerOfDawn() {
            hodActive = true;
            hodKills = 0;
            let arena = document.getElementById('hod-arena');
            let content16 = document.getElementById('content-16');
            let healthBar = document.getElementById('hod-health-fill');
            let statusEl = document.getElementById('hod-status');

            arena.style.display = 'block';
            content16.style.display = 'none';
            healthBar.style.width = '100%';
            statusEl.innerHTML = 'HAMMER OF DAWN ACTIVATED — TAKE OUT THE COMPETITION';'''

new_hod_init = '''        function initHammerOfDawn() {
            hodActive = true;
            hodKills = 0;
            let arena = document.getElementById('hod-arena');
            let titleScreen = document.getElementById('hod-title-screen');
            let healthBar = document.getElementById('hod-health-fill');
            let statusEl = document.getElementById('hod-status');

            // Show title for 2 seconds then fade to battle
            arena.style.opacity = '0';
            if(titleScreen) titleScreen.style.opacity = '1';
            healthBar.style.width = '100%';
            statusEl.innerHTML = 'ELIMINATE THE COMPETITION';

            setTimeout(() => {
                if(titleScreen) { titleScreen.style.opacity = '0'; }
                setTimeout(() => {
                    if(titleScreen) titleScreen.style.display = 'none';
                    arena.style.opacity = '1';
                }, 800);
            }, 2000);'''

html = html.replace(old_hod_init, new_hod_init)

# ============================================================
# 9. FIX nextSlide: wire chapter-4 and chapter-5 active reload
# ============================================================
# Update the sfxMap in nextSlide to include slide-ch4 and slide-ch5
old_sfxmap = """                let sfxMap = {
                    'slide-3':   { overlayId: 'overlay-3', statusId: 'reload-status-3', sweetSpotId: 'reload-sweet-spot-3', sliderId: 'reload-slider-3', wrapperId: 'content-3', speed: 10 },
                    'slide-ch3': { overlayId: 'overlay-ch3', statusId: 'reload-status-ch3', sweetSpotId: 'reload-sweet-spot-ch3', sliderId: 'reload-slider-ch3', wrapperId: 'content-ch3', speed: 10 },
                    'slide-ch4': { overlayId: 'overlay-ch4', statusId: 'reload-status-ch4', sweetSpotId: 'reload-sweet-spot-ch4', sliderId: 'reload-slider-ch4', wrapperId: 'content-ch4', speed: 11 },
                    'slide-ch5': { overlayId: 'overlay-ch5', statusId: 'reload-status-ch5', sweetSpotId: 'reload-sweet-spot-ch5', sliderId: 'reload-slider-ch5', wrapperId: 'content-ch5', speed: 12 },
                };"""

new_sfxmap = """                let sfxMap = {
                    'slide-3':   { overlayId: 'overlay-3',    statusId: 'reload-status-3',    sweetSpotId: 'reload-sweet-spot-3',    sliderId: 'reload-slider-3',    wrapperId: 'content-3',    speed: 10 },
                    'slide-ch3': { overlayId: 'overlay-ch3',  statusId: 'reload-status-ch3',  sweetSpotId: 'reload-sweet-spot-ch3',  sliderId: 'reload-slider-ch3',  wrapperId: 'content-ch3',  speed: 10 },
                    'slide-ch4': { overlayId: 'overlay-ch4',  statusId: 'reload-status-ch4',  sweetSpotId: 'reload-sweet-spot-ch4',  sliderId: 'reload-slider-ch4',  wrapperId: 'content-ch4',  speed: 11 },
                    'slide-ch5': { overlayId: 'overlay-ch5',  statusId: 'reload-status-ch5',  sweetSpotId: 'reload-sweet-spot-ch5',  sliderId: 'reload-slider-ch5',  wrapperId: 'content-ch5',  speed: 12 },
                };"""
html = html.replace(old_sfxmap, new_sfxmap)

# Ensure slide-ch4 and ch5 are included in the active reload trigger condition
html = html.replace(
    "nextSlideElement.id === 'slide-ch5')) {",
    "nextSlideElement.id === 'slide-ch5' || nextSlideElement.id === 'slide-ch4')) {"
)

# ============================================================
# 10. FIX nextSlide: trigger HoD when slide-16 is navigated to
# ============================================================
html = html.replace(
    "// Hammer of Dawn boss battle (slide-16 is the arena)\n            if(nextSlideElement && nextSlideElement.id === 'slide-16') { setTimeout(initHammerOfDawn, 200); }",
    "// Hammer of Dawn boss battle\n            if(nextSlideElement && (nextSlideElement.id === 'slide-16' || nextSlideElement.id === 'slide-final-ch')) { setTimeout(initHammerOfDawn, 200); }"
)

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Final patch complete!")
