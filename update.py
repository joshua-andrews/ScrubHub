import sys

with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix chapter 1
html = html.replace('<span class="hud-font red-text" style="float: right;">\[ CHAPTER 01 \]</span></p>', '<span class="hud-font red-text" style="float: right;">[ CHAPTER 01 ]</span></p>')

# Add Active Reload slide 2.5
slide_3_new = '''
    <!-- SLIDE 2.5: CHAPTER 1 TITLE (ACTIVE RELOAD) -->
    <div class="slide" id="slide-3" style="position:relative;">
        <div class="game-overlay" id="overlay-3">
            <div class="instructions">[ DECRYPTING INTEL - PRESS SPACE TO ACTIVE RELOAD ]</div>
            <div id="reload-status-3" style="font-family: 'Share Tech Mono'; color: #ff2a2a; font-size: 2rem; margin: 20px 0; text-shadow: 0 0 10px #ff0000;">WAITING...</div>
            <div id="reload-bar-container-3" style="width: 400px; height: 30px; border: 2px solid #500; background: #1a0000; position: relative;">
                <div id="reload-sweet-spot-3" style="position: absolute; height: 100%; top: 0; background: rgba(255,42,42,0.5); width: 60px; left: 250px;"></div>
                <div id="reload-slider-3" style="position: absolute; height: 100%; width: 10px; background: #fff; top: 0; left: 0;"></div>
            </div>
        </div>
        <div class="content" id="content-3" style="text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100%; align-items: center;">
            <div class="slide-subtitle" style="font-size: 1.5rem; margin-bottom: 20px;">CHAPTER 1</div>
            <h1 class="slide-header" style="border: none; font-size: 5rem; margin-bottom: 0;">The Landscape & Problem</h1>
        </div>
    </div>
'''
if '<!-- SLIDE 2.5' not in html:
    html = html.replace('    <!-- SLIDE 3: WHAT WE DID -->', slide_3_new + '\n    <!-- SLIDE 3.5: WHAT WE DID -->')

# Update "What we did" list
whatwedid_old = '''            <div class="hud-box">
                <p><strong>Audited ScrubHub's Current Digital Footprint:</strong> We evaluated the entire customer experience across all endpoints.</p>
                <p><strong>Competitive Teardown:</strong> Benchmarked the current workflow against top-tier national operators.</p>
                <p><strong>App Roadmap Specification:</strong> We laid out the specific features required for a branded app to bridge the gap between ScrubHub's current operations and top-tier national competitors.</p>
            </div>'''
            
whatwedid_new = '''            <div class="hud-grid-3">
                <div class="hud-box" style="text-align: center;">
                    <h1 style="font-size: 4rem; margin: 0; color: #ff2a2a; opacity: 0.5;">01</h1>
                    <p style="text-align:left;"><strong>Audited ScrubHub's Current Digital Footprint:</strong> We evaluated the entire customer experience across all endpoints.</p>
                </div>
                <div class="hud-box" style="text-align: center;">
                    <h1 style="font-size: 4rem; margin: 0; color: #ff2a2a; opacity: 0.5;">02</h1>
                    <p style="text-align:left;"><strong>Competitive Teardown:</strong> Benchmarked the current workflow against top-tier national operators.</p>
                </div>
                <div class="hud-box" style="text-align: center;">
                    <h1 style="font-size: 4rem; margin: 0; color: #ff2a2a; opacity: 0.5;">03</h1>
                    <p style="text-align:left;"><strong>App Roadmap Specification:</strong> We laid out the specific features required for a branded app to bridge the gap between ScrubHub's current operations and top-tier national competitors.</p>
                </div>
            </div>'''
html = html.replace(whatwedid_old, whatwedid_new)


# Update Audit Gallery
gallery = '''
            <div class="hud-grid" style="margin-top: 20px;">
                <div class="hud-box gallery-item" style="padding: 10px; cursor: pointer; border-color: #500; transition: transform 0.2s;" onclick="openLightbox('Photos/Hero section.jpeg')">
                    <img src="Photos/Hero section.jpeg" alt="Hero Section" style="width: 100%; height: auto; border-bottom: 1px solid #ff2a2a; padding-bottom: 5px;">
                    <p class="hud-font red-text" style="font-size: 0.8rem; text-align: center; margin-top: 10px; margin-bottom: 0;">[ VIEW HERO SECTION AUDIT ]</p>
                </div>
                <div class="hud-box gallery-item" style="padding: 10px; cursor: pointer; border-color: #500; transition: transform 0.2s;" onclick="openLightbox('Photos/Veteran section.jpeg')">
                    <img src="Photos/Veteran section.jpeg" alt="Veteran Section" style="width: 100%; height: auto; border-bottom: 1px solid #ff2a2a; padding-bottom: 5px;">
                    <p class="hud-font red-text" style="font-size: 0.8rem; text-align: center; margin-top: 10px; margin-bottom: 0;">[ VIEW VETERAN SECTION AUDIT ]</p>
                </div>
                <div class="hud-box gallery-item" style="padding: 10px; cursor: pointer; border-color: #500; transition: transform 0.2s;" onclick="openLightbox('Photos/Family Section.jpeg')">
                    <img src="Photos/Family Section.jpeg" alt="Family Section" style="width: 100%; height: auto; border-bottom: 1px solid #ff2a2a; padding-bottom: 5px;">
                    <p class="hud-font red-text" style="font-size: 0.8rem; text-align: center; margin-top: 10px; margin-bottom: 0;">[ VIEW FAMILY SECTION AUDIT ]</p>
                </div>
            </div>
'''
if 'Photos/Hero section.jpeg' not in html:
    html = html.replace('<!-- SLIDE 5: LAYING OUT THE FACTS -->', gallery + '\n    <!-- SLIDE 5: LAYING OUT THE FACTS -->')

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
