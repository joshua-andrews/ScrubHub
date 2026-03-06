with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

# First we need to make sure the end of startActiveReload is closed properly
# Currently, line 970 is the closing bracket for onkeydown, line 971 is for startActiveReload.
# Wait, let's look at test.js line 299:
# 298:             }
# 299:         }
# So there are 2 closing braces at the end. In scrubhub_tactical_pitch.html currently:
# 969:                 }
# 970:             }
# 971:         }
# So startActiveReload is fully closed!

js_to_append = r'''
        function openLightbox(src) {
            document.getElementById('lightbox-img').src = src;
            document.getElementById('lightbox').style.display = 'flex';
        }
        function closeLightbox() {
            document.getElementById('lightbox').style.display = 'none';
        }

        const swotData = {
            'strength': 
                <h3>STRENGTHS</h3>
                <p><strong>1. Ability to Introduce a Membership-Driven Revenue Model</strong></p>
                <p>ScrubHub can transition from primarily transactional washes to recurring membership revenue through a mobile and web platform.</p>
                <p>Industry data shows that subscription memberships are becoming the dominant revenue source for large chains. For example, Mister Car Wash reports that approximately 74% of wash revenue now comes from its Unlimited Wash Club memberships, as detailed previously.</p>
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
                <p>As previously mentioned, industry reports indicate that car wash memberships experience approximately 7.6% monthly churn, including both voluntary cancellations and failed payment churn.</p>
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
        }
    </script>
</body>
</html>
'''

# First clean up the debug script tag that test_bottom.py appended at the very end
if '<script>\n        logDebug("Bottom of script reached.");' in html:
    html = html.split('<script>\n        logDebug("Bottom of script reached.");')[0]
elif '</body>' in html:
    # If there's already a closing body or script from before, we need to be careful.
    # But we know it ended abruptly near startActiveReload.
    pass

# We will just append the missing javascript directly to the end of the file.
html = html.rstrip() + '\n' + js_to_append

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
