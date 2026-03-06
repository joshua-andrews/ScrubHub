
with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1. ACTIVE RELOAD: Restore space-to-start (revert auto-start)
# ============================================================
html = html.replace(
    '''            status.innerHTML = "RELOADING...";
            status.style.color = "#ffaa00";
            status.style.textShadow = "0 0 10px #ff8800";

            let pos = 0;
            let speed = config.speed;
            let done = false;''',
    '''            status.innerHTML = "PRESS SPACE TO RELOAD";
            status.style.color = "#ff2a2a";
            status.style.textShadow = "0 0 10px #ff0000";

            let pos = 0;
            let speed = config.speed;
            let done = false;
            let started = false;'''
)
html = html.replace(
    "            // Auto-start immediately\n            let reloadInterval = setInterval(updateGame, 20);",
    "            let reloadInterval = null;"
)
html = html.replace(
    '''            function updateGame() {
                pos += speed;
                slider.style.left = pos + 'px';
                if(pos > 400) {
                    clearInterval(reloadInterval);
                    if(!done) failReload();
                }
            }

            function failReload() {
                done = false;
                status.innerHTML = config.failText;
                status.style.color = "#800";
                status.style.textShadow = "none";
                setTimeout(() => {
                    pos = 0;
                    slider.style.left = '0px';
                    status.innerHTML = "RELOADING...";
                    status.style.color = "#ffaa00";
                    status.style.textShadow = "0 0 10px #ff8800";
                    reloadInterval = setInterval(updateGame, 20);
                }, 900);
            }''',
    '''            function updateGame() {
                pos += speed;
                slider.style.left = pos + 'px';
                if(pos > 400) {
                    clearInterval(reloadInterval);
                    reloadInterval = null;
                    started = false;
                    if(!done) failReload();
                }
            }

            function failReload() {
                done = false;
                started = false;
                status.innerHTML = config.failText;
                status.style.color = "#800";
                status.style.textShadow = "none";
                setTimeout(() => {
                    pos = 0;
                    slider.style.left = '0px';
                    status.innerHTML = "PRESS SPACE TO RELOAD";
                    status.style.color = "#ff2a2a";
                    status.style.textShadow = "0 0 10px #ff0000";
                }, 900);
            }'''
)
html = html.replace(
    '''            // Space key to "fire" at the sweet spot
            document.onkeydown = function(e) {
                if(e.code === 'Space') {
                    e.preventDefault();
                    if(!done) {
                        let sliderCenter = pos + 5;
                        clearInterval(reloadInterval);
                        if(sliderCenter >= spotLeft && sliderCenter <= (spotLeft + spotWidth)) {
                            successReload();
                        } else {
                            failReload();
                        }
                    }
                }
            };''',
    '''            document.onkeydown = function(e) {
                if(e.code === 'Space') {
                    e.preventDefault();
                    if(!started && !done) {
                        started = true;
                        status.innerHTML = "RELOADING...";
                        status.style.color = "#ffaa00";
                        status.style.textShadow = "0 0 10px #ff8800";
                        reloadInterval = setInterval(updateGame, 20);
                    } else if(started && !done) {
                        let sliderCenter = pos + 5;
                        clearInterval(reloadInterval);
                        reloadInterval = null;
                        started = false;
                        if(sliderCenter >= spotLeft && sliderCenter <= (spotLeft + spotWidth)) {
                            successReload();
                        } else {
                            failReload();
                        }
                    }
                }
            };'''
)

# ============================================================
# 2. WEBSITE AUDIT: Compact content to fit on screen
# ============================================================
html = html.replace(
    '<p>Every digital touchpoint affects your marketing channels. A cohesive experience is mandatory. Currently, the website is not optimized for conversion rate or UX/UI.</p>',
    '<p style="font-size:0.9rem; margin-bottom:10px;">Every digital touchpoint affects your marketing channels. Currently, the website has 4 critical conversion issues.</p>'
)
html = html.replace(
    '<p style="font-size: 1rem;">The banner "Join Unlimited Scrub Club" functions as a header, not a button, adding friction. Upfront veteran/family discounts clutter the hero unless data proves they actively convert new users.</p>',
    '<p style="font-size:0.85rem; margin-bottom:0;">The banner functions as a header, not a button, adding friction. Discounts clutter the hero section unnecessarily.</p>'
)
html = html.replace(
    '<p style="font-size: 1rem;">The "About Us" section disrupts the funnel. Customers only care about what ScrubHub does for <em>them</em>. The wash menu and membership pricing must be pushing to the top.</p>',
    '<p style="font-size:0.85rem; margin-bottom:0;">The "About Us" section disrupts the funnel. Wash menu and membership pricing must lead.</p>'
)
html = html.replace(
    '<p style="font-size: 1rem;">Testimonials are buried instead of sprinkled throughout for social proof. The footer reads "Copyright 2024" (two years behind). These details ruin reputation and signal an outdated company.</p>',
    '<p style="font-size:0.85rem; margin-bottom:0;">Testimonials are buried. Footer reads "Copyright 2024" — two years behind. Signals an outdated brand.</p>'
)
html = html.replace(
    '<p style="font-size: 1rem;">Using scroll-depth popups, we can exchange custom offers for emails and build an automated remarketing list. This is not including them opting into a referral program or considering any website UI updates.</p>',
    '<p style="font-size:0.85rem; margin-bottom:5px;">Scroll-depth popups can build an automated remarketing list on autopilot.</p>'
)
# Shrink the table
html = html.replace(
    '<table style="margin-top: 10px; font-size: 0.9rem;">',
    '<table style="margin-top: 5px; font-size: 0.78rem;">'
)

# ============================================================
# 3. WEBSITE AUDIT PHOTOS: Move to new slide after audit slide
# ============================================================
# Find and remove existing buttons from audit slide, insert new slide after it
audit_buttons = '''            <!-- Audit photo buttons: click to open lightbox, no inline images -->
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
            </div>
        </div>
    </div>

    <!-- SLIDE 5: LAYING OUT THE FACTS -->'''

audit_buttons_new = '''        </div>
    </div>

    <!-- SLIDE 4B: WEBSITE AUDIT EVIDENCE -->
    <div class="slide" id="slide-4b">
        <div class="content" id="content-4b">
            <div class="slide-subtitle">Chapter 1: The Landscape &amp; Problem</div>
            <h1 class="slide-header">Audit Evidence</h1>
            <p style="font-size:0.9rem; margin-bottom:15px;">Click any section below to expand and view the full findings.</p>
            <div class="hud-grid-3" style="margin-top:10px;">
                <div class="hud-box gallery-item" style="padding: 30px 20px; cursor: pointer; border-color: #500; transition: all 0.2s; text-align:center;" onclick="openLightbox('Photos/Hero section.jpeg')">
                    <p style="font-size:2rem; margin:0 0 10px 0;">🎯</p>
                    <h3 class="red-text" style="margin-bottom:8px;">Hero Section</h3>
                    <p class="hud-font" style="font-size: 0.8rem; margin: 0; color:#666;">[ CLICK TO EXPAND → ]</p>
                </div>
                <div class="hud-box gallery-item" style="padding: 30px 20px; cursor: pointer; border-color: #500; transition: all 0.2s; text-align:center;" onclick="openLightbox('Photos/Veteran section.jpeg')">
                    <p style="font-size:2rem; margin:0 0 10px 0;">🎖️</p>
                    <h3 class="red-text" style="margin-bottom:8px;">Veteran Section</h3>
                    <p class="hud-font" style="font-size: 0.8rem; margin: 0; color:#666;">[ CLICK TO EXPAND → ]</p>
                </div>
                <div class="hud-box gallery-item" style="padding: 30px 20px; cursor: pointer; border-color: #500; transition: all 0.2s; text-align:center;" onclick="openLightbox('Photos/Family Section.jpeg')">
                    <p style="font-size:2rem; margin:0 0 10px 0;">👨‍👩‍👧</p>
                    <h3 class="red-text" style="margin-bottom:8px;">Family Section</h3>
                    <p class="hud-font" style="font-size: 0.8rem; margin: 0; color:#666;">[ CLICK TO EXPAND → ]</p>
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE 5: LAYING OUT THE FACTS -->'''

html = html.replace(audit_buttons, audit_buttons_new)

# ============================================================
# 4. SWOT CLICK TEXT: "Click to Decrypt" → "Click to Read Journal"
# ============================================================
html = html.replace('[ CLICK TO DECRYPT ARCHIVE ]', '[ CLICK TO READ JOURNAL ]')

# ============================================================
# 5. SWOT JOURNAL: Replace CSS background with dark readable design
# ============================================================
html = html.replace(
    """<div style="position:relative; width: 800px; height: 600px; background: url('C:/Users/joshu/.gemini/antigravity/brain/474e2374-260b-4ead-bb38-6e0c1a12336c/war_torn_paper_1772777354577.png') center/cover; padding: 50px; box-sizing: border-box; box-shadow: 0 0 50px #000, inset 0 0 50px rgba(0,0,0,0.5); border-radius: 3px; color: #2a1f1a;">""",
    """<div style="position:relative; width: 860px; height: 620px; background: #0a0000; border: 2px solid #ff2a2a; box-shadow: 0 0 60px rgba(255,0,0,0.3), inset 0 0 40px rgba(20,0,0,0.8); padding: 40px 50px; box-sizing: border-box; color: #ddd;">"""
)
# Fix journal content styles for dark bg
html = html.replace(
    "#journal-content * { color: #1a1a1a !important; text-shadow: none !important; font-family: 'Share Tech Mono', monospace !important; }",
    "#journal-content * { color: #ccc !important; text-shadow: none !important; font-family: 'Share Tech Mono', monospace !important; }"
)
html = html.replace(
    "#journal-content h3 { font-family: 'Anton', sans-serif !important; font-size: 2rem; color: #500 !important; margin-bottom: 20px; }",
    "#journal-content h3 { font-family: 'Anton', sans-serif !important; font-size: 2rem; color: #ff2a2a !important; margin-bottom: 20px; text-shadow: 0 0 10px rgba(255,42,42,0.5) !important; }"
)
# Fix close button color
html = html.replace(
    'style="position:absolute; top:20px; right:20px; background:none; border:none; color:#800; font-family:\'Anton\'; font-size:2rem; cursor:pointer; text-shadow: 0 0 5px rgba(255,0,0,0.3);">X</button>',
    'style="position:absolute; top:20px; right:20px; background:none; border:none; color:#ff2a2a; font-family:\'Anton\'; font-size:2rem; cursor:pointer; text-shadow: 0 0 10px rgba(255,0,0,0.5);">✕</button>'
)

# ============================================================
# 6. ADD CHAPTER 3 TITLE SLIDE "The Hammer of ScrubHub"
# ============================================================
ch3_title = '''
    <!-- CHAPTER 3 TITLE: THE HAMMER OF SCRUBHUB -->
    <div class="slide" id="slide-ch3" style="position:relative;">
        <div class="game-overlay" id="overlay-ch3">
            <div class="instructions">[ ACTIVE RELOAD — PRESS SPACE AT THE RIGHT MOMENT ]</div>
            <div id="reload-status-ch3" style="font-family: 'Share Tech Mono'; color: #ff2a2a; font-size: 2rem; margin: 20px 0; text-shadow: 0 0 10px #ff0000;">PRESS SPACE TO RELOAD</div>
            <div id="reload-bar-container-ch3" style="width: 400px; height: 30px; border: 2px solid #500; background: #1a0000; position: relative;">
                <div id="reload-sweet-spot-ch3" style="position: absolute; height: 100%; top: 0; background: rgba(255,42,42,0.5); width: 60px; left: 250px;"></div>
                <div id="reload-slider-ch3" style="position: absolute; height: 100%; width: 10px; background: #fff; top: 0; left: 0;"></div>
            </div>
        </div>
        <div class="content" id="content-ch3" style="text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100%; align-items: center;">
            <div class="slide-subtitle" style="font-size: 1.5rem; margin-bottom: 20px;">CHAPTER 3</div>
            <h1 class="slide-header" style="border: none; font-size: 5rem; margin-bottom: 0;">The Hammer of ScrubHub</h1>
        </div>
    </div>

'''

html = html.replace('    <!-- SLIDE 10: THE DIGITAL OVERHAUL STRATEGY -->', ch3_title + '    <!-- SLIDE 10: THE DIGITAL OVERHAUL STRATEGY -->')

# ============================================================
# 7. RENAME "The Proposed Solution" → "The Hammer of ScrubHub"
# ============================================================
html = html.replace('Chapter 3: The Proposed Solution', 'Chapter 3: The Hammer of ScrubHub')
html = html.replace('The Proposed Solution', 'The Hammer of ScrubHub')
html = html.replace('<h1 class="slide-header">The Digital Overhaul Strategy</h1>', '<h1 class="slide-header">The Digital Overhaul Strategy</h1>')

# ============================================================
# 8. AGENDA: "Operations & Risk Mitigation" → "Marketing Overview"
#    "Execution Timeline & Economics" → "Execution Details"
# ============================================================
html = html.replace('5. Execution Timeline &amp; Economics', '5. Execution Details')
html = html.replace('4. Operations &amp; Risk Mitigation', '4. Marketing Overview')
html = html.replace('Operations &amp; Risk Mitigation', 'Marketing Overview')

# ============================================================
# 9. RESTORE MISSING APP FOUNDATION SLIDE (5 Bottom Tabs)
#    Insert before the "New Features" slide (slide-11)
# ============================================================
app_foundation_slide = '''
    <!-- SLIDE 10B: APP FOUNDATION -->
    <div class="slide" id="slide-10b">
        <div class="content" id="content-10b">
            <div class="slide-subtitle">Chapter 3: The Hammer of ScrubHub</div>
            <h1 class="slide-header">The App Foundation</h1>
            <p style="font-size:0.9rem; margin-bottom:10px;">A single, unified platform with 5 core tabs — everything the customer needs, nothing they don't.</p>
            <table>
                <tr>
                    <th>The 5 Core Tabs</th>
                    <th>Tab Name</th>
                    <th>What the Customer Does Here</th>
                </tr>
                <tr>
                    <td><strong>Tab 1: The Dashboard</strong></td>
                    <td class="hud-font">Home</td>
                    <td>See how much money they've saved, view their active plan, and buy Lightning Deals.</td>
                </tr>
                <tr>
                    <td><strong>Tab 2: The Physical Asset</strong></td>
                    <td class="hud-font">My Garage</td>
                    <td>Add or remove cars and license plates (for the tunnel cameras).</td>
                </tr>
                <tr>
                    <td><strong>Tab 3: The Store</strong></td>
                    <td class="hud-font">Wash Plans</td>
                    <td>Buy a new membership, upgrade a tier, or cancel a plan.</td>
                </tr>
                <tr>
                    <td><strong>Tab 4: The Map</strong></td>
                    <td class="hud-font">Locations</td>
                    <td>Find the nearest wash, see if it's open, and get driving directions.</td>
                </tr>
                <tr>
                    <td><strong>Tab 5: The Admin Hub</strong></td>
                    <td class="hud-font">Account</td>
                    <td>Update credit cards, view past receipts, and contact Help &amp; Support.</td>
                </tr>
            </table>
        </div>
    </div>

'''
html = html.replace('    <!-- SLIDE 11: FEATURE-TO-ROI MAPPING -->', app_foundation_slide + '    <!-- SLIDE 11: FEATURE-TO-ROI MAPPING -->')

# ============================================================
# 10. RENAME "Feature-to-ROI Mapping" → "New Features"
# ============================================================
html = html.replace('Feature-to-ROI Mapping', 'New Features')
html = html.replace('<h1 class="slide-header">New Features</h1>', '<h1 class="slide-header">New Features</h1>')

# ============================================================
# 11. "saving thousands of dollars a month" fix
# ============================================================
html = html.replace('saving thousands of dollars a month', 'recovering thousands of dollars in monthly revenue')

# ============================================================
# 12. REPLACE TECHNICAL ARCHITECTURE SLIDE with MARKETING slide
#     AND ADD Chapter 4 title slide before it
# ============================================================
ch4_title = '''
    <!-- CHAPTER 4 TITLE: MARKETING OVERVIEW -->
    <div class="slide" id="slide-ch4">
        <div class="game-overlay" id="overlay-ch4">
            <div class="instructions">[ ACTIVE RELOAD — PRESS SPACE AT THE RIGHT MOMENT ]</div>
            <div id="reload-status-ch4" style="font-family: 'Share Tech Mono'; color: #ff2a2a; font-size: 2rem; margin: 20px 0; text-shadow: 0 0 10px #ff0000;">PRESS SPACE TO RELOAD</div>
            <div id="reload-bar-container-ch4" style="width: 400px; height: 30px; border: 2px solid #500; background: #1a0000; position: relative;">
                <div id="reload-sweet-spot-ch4" style="position: absolute; height: 100%; top: 0; background: rgba(255,42,42,0.5); width: 60px; left: 250px;"></div>
                <div id="reload-slider-ch4" style="position: absolute; height: 100%; width: 10px; background: #fff; top: 0; left: 0;"></div>
            </div>
        </div>
        <div class="content" id="content-ch4" style="text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100%; align-items: center;">
            <div class="slide-subtitle" style="font-size: 1.5rem; margin-bottom: 20px;">CHAPTER 4</div>
            <h1 class="slide-header" style="border: none; font-size: 5rem; margin-bottom: 0;">Marketing Overview</h1>
        </div>
    </div>

'''

old_tech_arch = '''    <!-- SLIDE 12: TECHNICAL ARCHITECTURE -->
    <div class="slide" id="slide-12">
        <div class="content" id="content-12">
            <div class="slide-subtitle">Chapter 4: Operations &amp; Risk Management</div>
            <h1 class="slide-header">Technical Architecture (Risk Mitigation)</h1>
            <div class="hud-box">
                <h3 style="color: #fff;">The "Hybrid Approach"</h3>
                <p>We aren't ripping out DRB Website Connect. We are securely layering on top of your existing POS system, ensuring <strong>zero operational downtime</strong>.</p>
                <div style="font-family: monospace; color: #ff2a2a; text-align: center; font-size: 1.5rem; margin-top: 30px;">
                    [ CUSTOM IOS/ANDROID APP ]<br>
                    |<br>
                    v<br>
                    [ DRB CERTIFIED API LAYER ]<br>
                    |<br>
                    v<br>
                    [ EXISTING DRB POS ]
                </div>
            </div>
        </div>
    </div>'''

new_marketing_arch = ch4_title + '''    <!-- SLIDE 12: MARKETING OVERVIEW -->
    <div class="slide" id="slide-12">
        <div class="content" id="content-12">
            <div class="slide-subtitle">Chapter 4: Marketing Overview</div>
            <h1 class="slide-header">Our Marketing Engine</h1>
            <p style="font-size:0.9rem; margin-bottom:10px;">A full-stack growth system that runs in the background — attracting, converting, and retaining customers automatically.</p>
            <div class="hud-grid">
                <div class="hud-box">
                    <h3 class="red-text">Acquisition Automations</h3>
                    <p style="font-size:0.9rem;">A website pop-up captures new visitor emails, triggering a <strong>Welcome Series</strong> — automated emails that introduce ScrubHub, build trust, and push toward the first wash or membership sign-up.</p>
                </div>
                <div class="hud-box">
                    <h3 class="red-text">Abandoned Checkout Recovery</h3>
                    <p style="font-size:0.9rem;">If someone starts the membership flow and doesn't complete it, an <strong>abandoned cart sequence</strong> fires automatically to recover that revenue before it's gone.</p>
                </div>
                <div class="hud-box">
                    <h3 class="red-text">App Push Notifications</h3>
                    <p style="font-size:0.9rem;">For app users who open and click but don't purchase: they receive a <strong>targeted push notification</strong> within 24 hours with a personalized offer to close the loop.</p>
                </div>
                <div class="hud-box">
                    <h3 class="red-text">Unlimited Campaign Execution</h3>
                    <p style="font-size:0.9rem;">We set up all automations and handle unlimited email design. You bring the ideas — we design, you approve, we send. Lightning deals, seasonal pushes, weather-triggered alerts — all handled.</p>
                </div>
            </div>
        </div>
    </div>'''

html = html.replace(old_tech_arch, new_marketing_arch)

# ============================================================
# 13. OPERATIONS DASHBOARD: Edit text
# ============================================================
html = html.replace(
    '<p>What the District Manager gets out of it: Real-time visibility into the metrics that matter.</p>',
    '<p>Real-time visibility into the metrics that matter — your digital ROI, at a glance.</p>'
)
# Add monthly reports note
html = html.replace(
    '<div class="hud-box" style="grid-column: span 2;">\n                    <h3 class="red-text">Attributed Campaign Revenue</h3>',
    '''<div class="hud-box" style="grid-column: span 2;">
                    <h3 class="red-text">Automatic Monthly Reports</h3>
                    <p>Automated monthly summaries delivered directly to support your financial records and data tracking — no manual pulling required.</p>
                </div>
                <div class="hud-box" style="grid-column: span 2;">
                    <h3 class="red-text">Attributed Campaign Revenue</h3>'''
)

# ============================================================
# 14. CHAPTER 4 label fix everywhere
# ============================================================
html = html.replace('Chapter 4: Operations &amp; Risk Management', 'Chapter 4: Marketing Overview')
html = html.replace('Chapter 4: Operations & Risk Management', 'Chapter 4: Marketing Overview')

# ============================================================
# 15. ADD CHAPTER 5 TITLE SLIDE before Implementation Timeline
#     Update agenda, change timing to 16 weeks
# ============================================================
ch5_title = '''
    <!-- CHAPTER 5 TITLE: EXECUTION DETAILS -->
    <div class="slide" id="slide-ch5">
        <div class="game-overlay" id="overlay-ch5">
            <div class="instructions">[ ACTIVE RELOAD — PRESS SPACE AT THE RIGHT MOMENT ]</div>
            <div id="reload-status-ch5" style="font-family: 'Share Tech Mono'; color: #ff2a2a; font-size: 2rem; margin: 20px 0; text-shadow: 0 0 10px #ff0000;">PRESS SPACE TO RELOAD</div>
            <div id="reload-bar-container-ch5" style="width: 400px; height: 30px; border: 2px solid #500; background: #1a0000; position: relative;">
                <div id="reload-sweet-spot-ch5" style="position: absolute; height: 100%; top: 0; background: rgba(255,42,42,0.5); width: 60px; left: 250px;"></div>
                <div id="reload-slider-ch5" style="position: absolute; height: 100%; width: 10px; background: #fff; top: 0; left: 0;"></div>
            </div>
        </div>
        <div class="content" id="content-ch5" style="text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100%; align-items: center;">
            <div class="slide-subtitle" style="font-size: 1.5rem; margin-bottom: 20px;">CHAPTER 5</div>
            <h1 class="slide-header" style="border: none; font-size: 5rem; margin-bottom: 0;">Execution Details</h1>
        </div>
    </div>

'''
html = html.replace('    <!-- SLIDE 14: IMPLEMENTATION TIMELINE -->', ch5_title + '    <!-- SLIDE 14: IMPLEMENTATION TIMELINE -->')

# ============================================================
# 16. RENAME "Execution Timeline & Economics" → "Execution Details"
# ============================================================
html = html.replace('Chapter 5: Execution &amp; Economics', 'Chapter 5: Execution Details')
html = html.replace('Chapter 5: Execution & Economics', 'Chapter 5: Execution Details')
html = html.replace('<h1 class="slide-header">Implementation Timeline</h1>', '<h1 class="slide-header">Execution Timeline</h1>')
html = html.replace('<p>A realistic, 12-week roadmap for deployment.</p>', '<p>A realistic, 16-week roadmap for deployment.</p>')

# Update the timeline weeks
html = html.replace('<h3 class="hud-font">Weeks 1-2: Discovery</h3>', '<h3 class="hud-font">Weeks 1-3: Discovery</h3>')
html = html.replace('<h3 class="hud-font">Weeks 3-5: Design</h3>', '<h3 class="hud-font">Weeks 4-7: Design</h3>')
html = html.replace('<h3 class="hud-font">Weeks 6-10: Build</h3>', '<h3 class="hud-font">Weeks 8-13: Build</h3>')
html = html.replace('<h3 class="hud-font">Weeks 11-12: Testing &amp; Launch</h3>', '<h3 class="hud-font">Weeks 14-16: Testing &amp; Launch</h3>')

# ============================================================
# 17. "What I Need From You" → "What We Need From You"
# ============================================================
html = html.replace('What I Need From You', 'What We Need From You')

# ============================================================
# 18. AGENDA SLIDE: Fix chapter names
# ============================================================
html = html.replace(
    '<strong>5. Execution Timeline &amp; Economics</strong>',
    '<strong>5. Execution Details</strong>'
)

# ============================================================
# 19. CHAPTER 3/4/5 ACTIVE RELOAD IDs in nextSlide()
# ============================================================
# Update nextSlide to handle the new chapter title slides
old_nextslide_ch3 = "            } else if (nextSlideElement && nextSlideElement.id === 'slide-3') {\n                // Chapter 1 active reload\n                startActiveReload({"
old_nextslide_ch3_config = """                    slideId: 'slide-3',
                    overlayId: 'overlay-3',
                    statusId: 'reload-status-3',
                    sweetSpotId: 'reload-sweet-spot-3',
                    sliderId: 'reload-slider-3',
                    wrapperId: 'content-3',
                    speed: 10,
                    successText: "INTEL DECRYPTED. ACCESS GRANTED.",
                    failText: "DECRYPTION FAILED. JAMMED."
                });"""

new_ch_reload_logic = """            } else if (nextSlideElement && (nextSlideElement.id === 'slide-3' || nextSlideElement.id === 'slide-ch3' || nextSlideElement.id === 'slide-ch4' || nextSlideElement.id === 'slide-ch5')) {
                let sfxMap = {
                    'slide-3':   { overlayId: 'overlay-3', statusId: 'reload-status-3', sweetSpotId: 'reload-sweet-spot-3', sliderId: 'reload-slider-3', wrapperId: 'content-3', speed: 10 },
                    'slide-ch3': { overlayId: 'overlay-ch3', statusId: 'reload-status-ch3', sweetSpotId: 'reload-sweet-spot-ch3', sliderId: 'reload-slider-ch3', wrapperId: 'content-ch3', speed: 10 },
                    'slide-ch4': { overlayId: 'overlay-ch4', statusId: 'reload-status-ch4', sweetSpotId: 'reload-sweet-spot-ch4', sliderId: 'reload-slider-ch4', wrapperId: 'content-ch4', speed: 11 },
                    'slide-ch5': { overlayId: 'overlay-ch5', statusId: 'reload-status-ch5', sweetSpotId: 'reload-sweet-spot-ch5', sliderId: 'reload-slider-ch5', wrapperId: 'content-ch5', speed: 12 },
                };
                let cfg = sfxMap[nextSlideElement.id];
                startActiveReload({
                    slideId: nextSlideElement.id,
                    overlayId: cfg.overlayId, statusId: cfg.statusId,
                    sweetSpotId: cfg.sweetSpotId, sliderId: cfg.sliderId,
                    wrapperId: cfg.wrapperId, speed: cfg.speed,
                    successText: "ACCESS GRANTED.", failText: "JAMMED. TRY AGAIN."
                });"""

# Use a simple replace on the old block
html = html.replace(
    "            } else if (nextSlideElement && nextSlideElement.id === 'slide-3') {\n                // Chapter 1 active reload\n                startActiveReload({\n                    slideId: 'slide-3',\n                    overlayId: 'overlay-3',\n                    statusId: 'reload-status-3',\n                    sweetSpotId: 'reload-sweet-spot-3',\n                    sliderId: 'reload-slider-3',\n                    wrapperId: 'content-3',\n                    speed: 10,\n                    successText: \"INTEL DECRYPTED. ACCESS GRANTED.\",\n                    failText: \"DECRYPTION FAILED. JAMMED.\"\n                });",
    new_ch_reload_logic
)

# ============================================================
# 20. SLIDE 16: Remove active reload, replace with BOSS BATTLE
# ============================================================
old_slide16_overlay = '''    <!-- SLIDE 16: INVESTMENT & ROI MODEL (ACTIVE RELOAD) -->
    <div class="slide" id="slide-16">
        <div class="game-overlay" id="overlay-16">
            <div class="instructions">[ DECRYPTING INVESTMENT MODEL - PRESS SPACE TO ACTIVE RELOAD ]</div>
            <div id="reload-status">WAITING...</div>
            <div id="reload-bar-container">
                <div id="reload-sweet-spot"></div>
                <div id="reload-slider"></div>
            </div>
        </div>'''

new_slide16_header = '''    <!-- SLIDE 16: INVESTMENT & ROI MODEL -->
    <div class="slide" id="slide-16">'''

html = html.replace(old_slide16_overlay, new_slide16_header)

# Remove the slide-16 active reload from nextSlide()
html = html.replace(
    """            } else if (nextSlideElement && nextSlideElement.id === 'slide-16') {
                // Investment active reload
                startActiveReload({
                    slideId: 'slide-16',
                    overlayId: 'overlay-16',
                    statusId: 'reload-status',
                    sweetSpotId: 'reload-sweet-spot',
                    sliderId: 'reload-slider',
                    wrapperId: 'content-16',
                    speed: 8,
                    successText: "PERFECT RELOAD. DAMAGE BOOSTED.",
                    failText: "GUN JAMMED."
                });""",
    "            } else if (nextSlideElement && nextSlideElement.id === 'slide-16') {\n                revealContent(num);"
)

# ============================================================
# 21. LAST SLIDE: Change text
# ============================================================
html = html.replace(
    '<p class="hud-font" style="font-size: 1.5rem; margin-top: 20px;">Please approve the Discovery Phase to initiate timeline.</p>',
    ''
)
html = html.replace(
    '<h1 class="slide-header" style="border: none; font-size: 5rem; margin-bottom: 0;">Next Steps &amp; Q&amp;A</h1>',
    '<h1 class="slide-header" style="border: none; font-size: 4rem; margin-bottom: 20px; color: #ff2a2a; text-shadow: 0 0 20px rgba(255,0,0,0.8);">CONGRATULATIONS, SOLDIER.</h1><h1 class="slide-header" style="border: none; font-size: 3rem; margin-bottom: 0; color: #fff;">Any Questions?</h1>'
)

# ============================================================
# 22. Add shotgun.mp3 audio element and rename shotgun_raw
# ============================================================
html = html.replace(
    '<audio id="chainsaw-sound" src="chainsaw.mp3" preload="auto"></audio>',
    '<audio id="chainsaw-sound" src="chainsaw.mp3" preload="auto"></audio>\n    <audio id="shotgun-sound" src="shotgun_raw.mp3" preload="auto"></audio>'
)

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Overhaul complete!")
