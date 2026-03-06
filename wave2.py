
with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1. FIX AGENDA: Update chapter names
# ============================================================
html = html.replace(
    '<p style="font-size: 1.5rem; border-bottom: 1px solid #330000; padding-bottom: 15px;"><strong>4. Operations &amp; Risk Mitigation</strong><span class="hud-font red-text" style="float: right;">[ CHAPTER 04 ]</span></p>',
    '<p style="font-size: 1.5rem; border-bottom: 1px solid #330000; padding-bottom: 15px;"><strong>4. Marketing Overview</strong><span class="hud-font red-text" style="float: right;">[ CHAPTER 04 ]</span></p>'
)
html = html.replace(
    '<p style="font-size: 1.5rem; margin-bottom: 0;"><strong>5. Execution Timeline &amp; Economics</strong><span class="hud-font red-text" style="float: right;">[ CHAPTER 05 ]</span></p>',
    '<p style="font-size: 1.5rem; margin-bottom: 0;"><strong>5. Execution Details</strong><span class="hud-font red-text" style="float: right;">[ CHAPTER 05 ]</span></p>'
)
# Also rename Chapter 3 in agenda
html = html.replace(
    '<p style="font-size: 1.5rem; border-bottom: 1px solid #330000; padding-bottom: 15px;"><strong>3. The Digital Overhaul Solution</strong><span class="hud-font red-text" style="float: right;">[ CHAPTER 03 ]</span></p>',
    '<p style="font-size: 1.5rem; border-bottom: 1px solid #330000; padding-bottom: 15px;"><strong>3. The Hammer of ScrubHub</strong><span class="hud-font red-text" style="float: right;">[ CHAPTER 03 ]</span></p>'
)

# ============================================================
# 2. FIX ACTIVE RELOAD: Correct status text and fix bar HTML
# ============================================================
# Status should say PRESS SPACE TO RELOAD not RELOADING on overlay init
html = html.replace(
    '<div id="reload-status-3" style="font-family: \'Share Tech Mono\'; color: #ff2a2a; font-size: 2rem; margin: 20px 0; text-shadow: 0 0 10px #ff0000;">RELOADING...</div>',
    '<div id="reload-status-3" style="font-family: \'Share Tech Mono\'; color: #ff2a2a; font-size: 2rem; margin: 20px 0; text-shadow: 0 0 10px #ff0000;">PRESS SPACE TO RELOAD</div>'
)

# Fix mangled reload-bar-container-3 HTML (has "position: 400px" bug)
html = html.replace(
    '<div id="reload-bar-container-3" style="width: 400px; height: 30px; border: 2px solid #500; background: #1a0000; position: relative;">',
    '<div id="reload-bar-container-3" style="width: 400px; height: 30px; border: 2px solid #500; background: #1a0000; position: relative;">'
)
# Fix the wider position issue from previous mangling
for sfx_id in ['ch3', 'ch4', 'ch5']:
    html = html.replace(
        f'<div id="reload-status-{sfx_id}" style="font-family: \'Share Tech Mono\'; color: #ff2a2a; font-size: 2rem; margin: 20px 0; text-shadow: 0 0 10px #ff0000;">RELOADING...</div>',
        f'<div id="reload-status-{sfx_id}" style="font-family: \'Share Tech Mono\'; color: #ff2a2a; font-size: 2rem; margin: 20px 0; text-shadow: 0 0 10px #ff0000;">PRESS SPACE TO RELOAD</div>'
    )

# Fix reload bar to be positioned more towards end (sweet spot near right side)
# Update JavaScript: randomize sweet spot more towards right side (200-320px range)
html = html.replace(
    '            let minLeft = 80;\n            let maxLeft = 300;',
    '            let minLeft = 200;\n            let maxLeft = 330;'
)

# ============================================================
# 3. UPDATE SHOTGUN AUDIO to v2 (28-30s — actual blast)
# ============================================================
html = html.replace(
    '<audio id="shotgun-sound" src="shotgun_raw.mp3" preload="auto"></audio>',
    '<audio id="shotgun-sound" src="shotgun_v2.mp3" preload="auto"></audio>'
)

# ============================================================
# 4. PARTICLE SYSTEM: Particles from TEXT as well as cursor
# ============================================================
old_fireShotgun_inner = '''            // Spread: 12-18 particles per shot
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
            }'''

new_fireShotgun_inner = '''            // Gun-side particles (spread from click point)
            let numGunChips = 10 + Math.floor(Math.random() * 6);
            for(let i = 0; i < numGunChips; i++) {
                let chip = document.createElement('div');
                chip.className = 'chip-particle';
                let size = 4 + Math.random() * 8;
                chip.style.width = size + 'px';
                chip.style.height = size + 'px';
                chip.style.left = (x - size/2 + (Math.random()-0.5)*25) + 'px';
                chip.style.top  = (y - size/2 + (Math.random()-0.5)*15) + 'px';
                chip.style.background = Math.random() > 0.5 ? '#fff' : '#ff2a2a';
                let angle = Math.random() * 360;
                let dist = 50 + Math.random() * 130;
                chip.style.setProperty('--dx', (Math.cos(angle*Math.PI/180)*dist)+'px');
                chip.style.setProperty('--dy', (Math.sin(angle*Math.PI/180)*dist+30)+'px');
                chip.style.setProperty('--rot', (Math.random()*720-360)+'deg');
                chip.style.animationDuration = (0.4+Math.random()*0.5)+'s';
                fxBox.appendChild(chip);
                setTimeout(() => chip.remove(), 1000);
            }

            // TEXT-side particles: chips fly off the title text
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

html = html.replace(old_fireShotgun_inner, new_fireShotgun_inner)

# ============================================================
# 5. SHOTGUN: Ensure nextSlide ONLY called after particle cloud finishes
# ============================================================
html = html.replace(
    '''            if(shotgunChips <= 0 && !shotgunDone) {
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
            }''',
    '''            if(shotgunChips <= 0 && !shotgunDone) {
                shotgunDone = true;
                if(shotgunHint) shotgunHint.style.display = 'none';
                title.style.opacity = '0';
                // Wait for last particle wave to finish, then flash + advance
                setTimeout(() => {
                    slide.style.background = '';
                    let bigFlash = document.createElement('div');
                    bigFlash.style.cssText = 'position:absolute;top:0;left:0;width:100%;height:100%;background:#fff;z-index:100;pointer-events:none;animation:flashOut 0.8s forwards;';
                    slide.appendChild(bigFlash);
                    setTimeout(() => {
                        bigFlash.remove();
                        nextSlide(parseInt(currentSlideIndex) + 1);
                    }, 900);
                }, 1200);
            }'''
)

# ============================================================
# 6. WEBSITE AUDIT SLIDE: Add back the 3 photo buttons inline
# ============================================================
old_audit_end = '''            <!-- Audit photo buttons: click to open lightbox, no inline images -->
            <div class="hud-grid" style="margin-top: 15px;">
                <div class="hud-box gallery-item" style="padding: 15px 20px; cursor: pointer; border-color: #500; transition: all 0.2s; text-align:center;" onclick="openLightbox('Photos/Hero section.jpeg')">
                    <p class="hud-font red-text" style="font-size: 0.9rem; margin: 0;">[ VIEW HERO SECTION AUDIT → ]</p>
                </div>
                <div class="hud-box gallery-item" style="padding: 15px 20px; cursor: pointer; border-color: #500; transition: all 0.2s; text-align:center;" onclick="openLightbox('Photos/Veteran section.jpeg')">
                    <p class="hud-font red-text" style="font-size: 0.9rem; margin: 0;">[ VIEW VETERAN SECTION AUDIT → ]</p>
                </div>
                <div class="hud-box gallery-item" style="padding: 15px 20px; cursor: pointer; border-color: #500; transition: all 0.2s; text-align:center;" onclick="openLightbox('Photos/Family Section.jpeg')">
                    <p class="hud-font red-text" style="font-size: 0.9rem; margin: 0;">[ VIEW FAMILY SECTION AUDIT → ]</p>
                </div>
            </div>'''

new_audit_end = '''            <!-- Audit photo buttons -->
            <div class="hud-grid-3" style="margin-top:12px;">
                <div class="hud-box gallery-item" style="padding:14px 10px; cursor:pointer; border-color:#500; text-align:center; transition:all 0.2s;" onclick="openLightbox('Photos/Hero section.jpeg')">
                    <p class="hud-font red-text" style="font-size:0.85rem; margin:0;">🎯 [ HERO SECTION → ]</p>
                </div>
                <div class="hud-box gallery-item" style="padding:14px 10px; cursor:pointer; border-color:#500; text-align:center; transition:all 0.2s;" onclick="openLightbox('Photos/Veteran section.jpeg')">
                    <p class="hud-font red-text" style="font-size:0.85rem; margin:0;">🎖️ [ VETERAN SECTION → ]</p>
                </div>
                <div class="hud-box gallery-item" style="padding:14px 10px; cursor:pointer; border-color:#500; text-align:center; transition:all 0.2s;" onclick="openLightbox('Photos/Family Section.jpeg')">
                    <p class="hud-font red-text" style="font-size:0.85rem; margin:0;">👨‍👩‍👧 [ FAMILY SECTION → ]</p>
                </div>
            </div>'''

html = html.replace(old_audit_end, new_audit_end)

# ============================================================
# 7. REMOVE SLIDE 16 (Investment & ROI) entirely
# ============================================================
# Find and remove slide-16
start_s16 = html.find('\n    <!-- SLIDE 16: INVESTMENT & ROI MODEL -->')
end_s16 = html.find('\n    <!-- SLIDE 17:', start_s16)
if start_s16 > -1 and end_s16 > -1:
    html = html[:start_s16] + html[end_s16:]

# Also remove its active reload from nextSlide if still present
html = html.replace(
    "            } else if (nextSlideElement && nextSlideElement.id === 'slide-16') {\n                revealContent(num);",
    ""
)

# ============================================================
# 8. WHAT WE NEED FROM YOU: Add 3 new items
# ============================================================
html = html.replace(
    '<h1 class="slide-header">What We Need From You</h1>',
    '<h1 class="slide-header">What We Need From You</h1>'
)
# Find the hud-grid in the WHAT WE NEED slide and add new box
old_wnfybox = '''<div class="hud-box">
                    <h3 class="red-text">Access Required</h3>'''
# We need a new box added. Let's find the existing slide-15 content
idx_s15 = html.find('<!-- SLIDE 15:')
if idx_s15 > -1:
    # Find the closing </div></div> of that slide
    chunk = html[idx_s15:idx_s15+2000]
    # Add a 3rd hud-box item
    old_last_box = '''<h3 class="red-text">Point of Contact</h3>
                    <p>One dedicated ScrubHub team member who can speak on behalf of the brand and approve decisions.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE 16'''
    new_last_box = '''<h3 class="red-text">Point of Contact</h3>
                    <p>One dedicated ScrubHub team member who can speak on behalf of the brand and approve decisions.</p>
                </div>
                <div class="hud-box">
                    <h3 class="red-text">Approvals & Commitments</h3>
                    <ul style="font-size:0.95rem; color:#ccc; padding-left:20px;">
                        <li>Scope of Work Approval</li>
                        <li>Budget Approvals for Services, Hosting, and Related Fees</li>
                        <li>Weekly Check-ins</li>
                        <li>Async communication via <strong>Google Chat</strong></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE 16'''
    html = html.replace(old_last_box, new_last_box)

# ============================================================
# 9. BOSS FIGHT: Add "Final Chapter / Boss Fight" title slide
#    before the HoD arena (slide-16)
# ============================================================
final_chapter_slide = '''
    <!-- FINAL CHAPTER: BOSS FIGHT -->
    <div class="slide" id="slide-final-ch" style="position:relative;">
        <div class="content" id="content-final-ch" style="text-align:center; display:flex; flex-direction:column; justify-content:center; height:100%; align-items:center;">
            <div class="slide-subtitle" style="font-size:1.5rem; margin-bottom:20px; color:#ff2a2a;">FINAL CHAPTER</div>
            <h1 class="slide-header" style="border:none; font-size:6rem; margin-bottom:20px;">Boss Fight</h1>
            <p class="hud-font" style="color:#666; font-size:1rem; animation:pulse 1.5s infinite;">[ PRESS NEXT TO ENGAGE ]</p>
        </div>
    </div>

'''

# Insert before the SLIDE 16 comment (which is now the HoD slide after we removed investment)
if '<!-- SLIDE 16:' in html:
    html = html.replace('    <!-- SLIDE 16:', final_chapter_slide + '    <!-- SLIDE 16:')

# ============================================================
# 10. FINAL SLIDE: Update text to "Great work soldier / Any questions"
# ============================================================
html = html.replace(
    '<h1 class="slide-header" style="border: none; font-size: 4rem; margin-bottom: 20px; color: #ff2a2a; text-shadow: 0 0 20px rgba(255,0,0,0.8);">CONGRATULATIONS, SOLDIER.</h1><h1 class="slide-header" style="border: none; font-size: 3rem; margin-bottom: 0; color: #fff;">Any Questions?</h1>',
    '<h1 class="slide-header" style="border: none; font-size: 4rem; margin-bottom: 20px; color: #ff2a2a; text-shadow: 0 0 20px rgba(255,0,0,0.8);">Great Work, Soldier.</h1><h1 class="slide-header" style="border: none; font-size: 3rem; margin-bottom: 0; color: #fff;">Any Questions?</h1>'
)

# ============================================================
# 11. HOD: After boss fight, advance to LAST slide (not slide-16)
# ============================================================
html = html.replace(
    "                    // All dead — victory!\n                    hodActive = false;\n                    cancelAnimationFrame(hodAnimFrame);\n                    statusEl.innerHTML = '✓ COMPETITION ELIMINATED';\n                    document.getElementById('hod-health-fill').style.width = '0%';\n                    document.getElementById('hod-health-fill').style.background = '#00ff00';\n                    setTimeout(() => {\n                        document.getElementById('hod-arena').style.display = 'none';\n                        let c = document.getElementById('content-16');\n                        c.style.display = '';\n                        c.classList.add('revealed');\n                    }, 1200);",
    "                    // All dead — victory! Advance to final slide\n                    hodActive = false;\n                    cancelAnimationFrame(hodAnimFrame);\n                    statusEl.innerHTML = '✓ COMPETITION ELIMINATED';\n                    document.getElementById('hod-health-fill').style.width = '0%';\n                    document.getElementById('hod-health-fill').style.background = '#00ff00';\n                    setTimeout(() => {\n                        nextSlide(currentSlideIndex + 1);\n                    }, 1200);"
)

# ============================================================
# 12. Wire HoD to slide-16 (which is now the actual battle arena)
# ============================================================
html = html.replace(
    "            // Hammer of Dawn boss battle\n            if(num === 16) { setTimeout(initHammerOfDawn, 200); }",
    "            // Hammer of Dawn boss battle (slide-16 is the arena)\n            if(nextSlideElement && nextSlideElement.id === 'slide-16') { setTimeout(initHammerOfDawn, 200); }"
)

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Wave 2 corrections complete!")
