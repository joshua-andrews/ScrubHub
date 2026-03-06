with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Shotgun Title Slide
shotgun_slide = '''
    <!-- SLIDE 8.5: SWOT TITLE (SHOTGUN TRANSITION) -->
    <div class="slide" id="slide-9" style="position:relative; cursor: crosshair;" onclick="fireShotgun(event)">
        <div class="content" id="content-9" style="text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100%; align-items: center; transition: opacity 0.3s; z-index: 50;">
            <div class="slide-subtitle" style="font-size: 1.5rem; margin-bottom: 20px;">CHAPTER 2</div>
            <h1 id="swot-target-title" class="slide-header" style="border: none; font-size: 5rem; margin-bottom: 0; pointer-events: none;">Strategic Analysis</h1>
        </div>
        <div id="shotgun-fx-container" style="position:absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index: 40;"></div>
    </div>
'''

# We need to replace slide-9 with the pair. slide-9 -> slide-9.5
swot_old = '''    <!-- SLIDE 9: SWOT ANALYSIS -->
    <div class="slide" id="slide-9">
        <div class="content" id="content-9">
            <div class="slide-subtitle">Chapter 2: Strategic Analysis</div>
            <h1 class="slide-header">SWOT Analysis</h1>
            
            <div class="hud-grid">
                <div class="hud-box">
                    <h3>Strengths</h3>
                    <p>Existing footprint (4 strong GA locations). Competitive entry price point ( retail /  membership)  Customers who get two car washes a month will benefit from the membership.</p>
                </div>
                <div class="hud-box">
                    <h3 class="red-text">Weaknesses</h3>
                    <p>Fragmented digital journey (split across WordPress and DRB portal), website is clunky, zero proactive churn prevention.</p>
                </div>
                <div class="hud-box">
                    <h3>Opportunities</h3>
                    <p>Untapped revenue recovery via weather-triggered marketing, capturing impulse buyers via digital "Lightning Deals", digital gifting, and more.</p>
                </div>
                <div class="hud-box">
                    <h3 class="red-text">Threats</h3>
                    <p>Aggressive expansion by national chains (Mister Car Wash) who already operate with 79% subscription volume, and they have systems in place to make sure their customers stay loyal.</p>
                </div>
            </div>
        </div>
    </div>'''

if swot_old in html:
    pass
elif '<!-- SLIDE 9: SWOT ANALYSIS -->' in html:
    # Get exact boundaries
    import re
    match = re.search(r'    <!-- SLIDE 9: SWOT ANALYSIS -->(.*?)    <!-- SLIDE 10: THE DIGITAL OVERHAUL STRATEGY -->', html, re.DOTALL)
    if match:
        swot_old = '    <!-- SLIDE 9: SWOT ANALYSIS -->' + match.group(1)
        
swot_new = shotgun_slide + '''

    <!-- SLIDE 9.5: INTERACTIVE SWOT MATRIX -->
    <div class="slide" id="slide-10">
        <div class="content" id="content-10">
            <div class="slide-subtitle">Chapter 2: Strategic Analysis</div>
            <h1 class="slide-header">SWOT Analysis</h1>
            
            <div class="hud-grid" style="grid-template-columns: 1fr 1fr; gap: 30px;">
                <div class="hud-box swot-quadrant" style="cursor: pointer; text-align: center; padding: 40px;" onclick="openJournal('strength')">
                    <h1 style="color: #fff; margin-bottom: 10px;">STRENGTHS</h1>
                    <p class="hud-font red-text" style="margin: 0;">[ CLICK TO DECRYPT ARCHIVE ]</p>
                </div>
                <div class="hud-box swot-quadrant" style="cursor: pointer; border-color: #ff2a2a; text-align: center; padding: 40px;" onclick="openJournal('weakness')">
                    <h1 class="red-text" style="margin-bottom: 10px;">WEAKNESSES</h1>
                    <p class="hud-font red-text" style="margin: 0;">[ CLICK TO DECRYPT ARCHIVE ]</p>
                </div>
                <div class="hud-box swot-quadrant" style="cursor: pointer; text-align: center; padding: 40px;" onclick="openJournal('opportunity')">
                    <h1 style="color: #fff; margin-bottom: 10px;">OPPORTUNITIES</h1>
                    <p class="hud-font red-text" style="margin: 0;">[ CLICK TO DECRYPT ARCHIVE ]</p>
                </div>
                <div class="hud-box swot-quadrant" style="cursor: pointer; border-color: #ff2a2a; text-align: center; padding: 40px;" onclick="openJournal('threat')">
                    <h1 class="red-text" style="margin-bottom: 10px;">THREATS</h1>
                    <p class="hud-font red-text" style="margin: 0;">[ CLICK TO DECRYPT ARCHIVE ]</p>
                </div>
            </div>
        </div>
    </div>
'''

if '<!-- SLIDE 8.5: SWOT TITLE (SHOTGUN TRANSITION) -->' not in html:
    html = html.replace(swot_old, swot_new)

# Add JSON content for journal directly to JS
journal_data = '''
        const swotData = {
            'strength': 
                <h3>STRENGTHS</h3>
                <p><strong>1. Ability to Introduce a Membership-Driven Revenue Model</strong></p>
                <p>ScrubHub can transition from primarily transactional washes to recurring membership revenue through a mobile and web platform.</p>
                <p>Industry data shows that subscription memberships are becoming the dominant revenue source for large chains. For example, Mister Car Wash reports that approximately 7476% of wash revenue now comes from its Unlimited Wash Club memberships, as detailed previously.</p>
                <p><br><strong>2. Opportunity to Remove Payment Friction</strong></p>
                <p>A ScrubHub app allows customers to pay automatically, manage subscriptions, and skip payment kiosks. Convenience is a vital driver: 73% of consumers say customer experience influences purchasing decisions.</p>
                <p><em>Implication: Faster digital payments and frictionless entry can improve the customer experience and increase repeat visits.</em></p>
                <p><br><strong>3. Ability to Capture Customer Data</strong></p>
                <p>A mobile platform allows ScrubHub to collect data on visit frequency, purchase behavior, and customer lifetime value. Many traditional car washes operate blind without this intel.</p>
                <p><em>Implication: ScrubHub can run targeted promotions, improve retention strategies, and make more data-driven business decisions.</em></p>
                <p><br><strong>4. Strong Market Demand for Professional Services</strong></p>
                <p>Professional car wash usage has grown significantly. The percentage of drivers using professional car washes increased from 50% in 1996 to about 79% in 2021.</p>
                <p><em>Implication: Demand continues to expand, creating a favorable structural environment for growth.</em></p>
            ,
            'weakness': 
                <h3>WEAKNESSES</h3>
                <p><strong>1. Limited Digital Infrastructure Today</strong></p>
                <p>If ScrubHub currently relies primarily on on-site payment kiosks and in-person transactions, the business likely lacks critical digital infrastructure such as mobile membership management, automated marketing, and loyalty tracking systems.</p>
                <p><em>Implication: Without digital tools, it is harder to compete with larger chains that have already implemented these automated systems.</em></p>
                <p><br><strong>2. Membership Churn Risk</strong></p>
                <p>Membership businesses must manage churn carefully.</p>
                <p>As previously mentioned, industry reports indicate that car wash memberships experience approximately 78% monthly churn, including both voluntary cancellations and failed payment churn.</p>
                <p><em>Implication: If the business ramps up memberships, it must implement tools (apps, push notifications, automated billing management) to manage retention effectively and plug the leaks.</em></p>
            ,
            'opportunity': 
                <h3>OPPORTUNITIES</h3>
                <p><strong>1. Growing Global Car Wash Market</strong></p>
                <p>The overall industry is expanding steadily. The global car wash services market was valued at .07 billion in 2024 and is expected to reach .51 billion by 2032.</p>
                <p><em>Implication: Entering the digital space now allows the company to capture growth as the market expands globally.</em></p>
                <p><br><strong>2. Loyalty Programs Increase Customer Spending</strong></p>
                <p>Loyalty systems encourage repeat visits and higher spending. Research shows that 81% of consumers say loyalty programs make them more likely to continue doing business with a brand.</p>
                <p><em>Implication: A digital loyalty system can increase visit frequency and customer lifetime value.</em></p>
                <p><br><strong>3. Advanced Behavioral Retargeting</strong></p>
                <p>With an automated marketing engine, if a customer opens an email and clicks but doesn't check out, we can immediately retarget them with push notifications or SMS.</p>
                <p><em>Implication: Advanced multi-channel automation stops revenue from falling through the cracks of the marketing funnel.</em></p>
            ,
            'threat': 
                <h3>THREATS</h3>
                <p><strong>1. Increasing Competition</strong></p>
                <p>The U.S. car wash industry has approximately 60,000 locations, creating strong local competition in nearly every geographic market.</p>
                <p><em>Implication: Customers often have multiple car wash options nearby, making brand differentiation critically important. Convenience wins fights.</em></p>
                <p><br><strong>2. Low Switching Costs for Customers</strong></p>
                <p>Because there are roughly 60,000 locations, customers can easily choose another car wash if it offers faster service, better pricing, or a more functional loyalty app.</p>
                <p><em>Implication: ScrubHub must create a relentlessly compelling customer experience to maintain loyalty, or risk losing members to chains that do.</em></p>
            
        };

        function openJournal(key) {
            document.getElementById('journal-content').innerHTML = swotData[key];
            document.getElementById('journal-modal').style.display = 'flex';
        }
        function closeJournal() {
            document.getElementById('journal-modal').style.display = 'none';
            document.getElementById('journal-content').innerHTML = '';
        }

        let shotgunShots = 0;
        function fireShotgun(event) {
            if(shotgunShots >= 3) return;
            shotgunShots++;
            
            // Play Sound
            // Since we don't have a shotgun sound file easily available, we'll try to find any existing sound 
            // but just the visual fx are powerful too.
            let fxBox = document.getElementById('shotgun-fx-container');
            let slide = document.getElementById('slide-9');
            let title = document.getElementById('swot-target-title');
            
            let rect = slide.getBoundingClientRect();
            let x = event.clientX - rect.left;
            let y = event.clientY - rect.top;

            // Flash
            let flash = document.createElement('div');
            flash.className = 'flash';
            flash.style.left = x + 'px';
            flash.style.top = y + 'px';
            fxBox.appendChild(flash);

            // Blood
            let blood = document.createElement('div');
            blood.className = 'blood-splatter';
            blood.style.left = x + 'px';
            blood.style.top = y + 'px';
            fxBox.appendChild(blood);

            // Hole
            let hole = document.createElement('div');
            hole.className = 'bullet-hole';
            hole.style.left = x + 'px';
            hole.style.top = y + 'px';
            fxBox.appendChild(hole);

            // Shake screen
            slide.classList.add('shaking');
            setTimeout(() => slide.classList.remove('shaking'), 200);

            // Diminish Title
            title.style.opacity = Math.max(0, 1 - (shotgunShots * 0.34));

            if(shotgunShots === 3) {
                setTimeout(() => {
                    nextSlide(parseInt(currentSlideIndex) + 1);
                }, 800);
            }
        }
'''

if 'const swotData =' not in html:
    html = html.replace('        function openLightbox(src)', journal_data + '\n        function openLightbox(src)')


# We need to fix the navigation logic.
# Because we added 2 slides ("slide-3" chapter title, "slide-9" shotgun), 
# The slide IDs are now:
# slide-1, slide-2, slide-3, slide-4, slide-5, slide-6, slide-7, slide-8, slide-9, slide-10 ...
# Oh wait, we need to make sure the slides array picks them all up dynamically.
# Existing JS: const slides = document.querySelectorAll('.slide'); handles it mostly fine.

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
