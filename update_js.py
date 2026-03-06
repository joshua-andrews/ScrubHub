with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

# JS for lightbox
js_lightbox = '''
        function openLightbox(src) {
            document.getElementById('lightbox-img').src = src;
            document.getElementById('lightbox').style.display = 'flex';
        }
        function closeLightbox() {
            document.getElementById('lightbox').style.display = 'none';
        }
'''
if 'function openLightbox' not in html:
    html = html.replace('        function nextSlide(index) {', js_lightbox + '\n        function nextSlide(index) {')


# Refactor Active Reload for sliding
# Existing JS has reload-status, reload-sweet-spot, reload-slider for slide 16
js_active_reload_factory = '''
        function startActiveReload(config) {
            let overlay = document.getElementById(config.overlayId);
            let status = document.getElementById(config.statusId);
            let sweetSpot = document.getElementById(config.sweetSpotId);
            let slider = document.getElementById(config.sliderId);
            let s1Wrapper = document.getElementById(config.wrapperId);
            
            overlay.style.opacity = 1;
            overlay.style.pointerEvents = 'auto';
            status.innerHTML = "PRESS SPACE TO START";
            status.style.color = "#ff2a2a";

            let phase = 0; 
            let pos = 0;
            let speed = config.speed; 
            let reloadInterval;
            
            // Randomize sweet spot
            let spotWidth = 60;
            let minLeft = 100;
            let maxLeft = 320;
            let spotLeft = Math.floor(Math.random() * (maxLeft - minLeft + 1)) + minLeft;
            sweetSpot.style.left = spotLeft + 'px';
            sweetSpot.style.width = spotWidth + 'px';

            function updateGame() {
                pos += speed;
                slider.style.left = pos + 'px';
                if(pos > 400) {
                    clearInterval(reloadInterval);
                    failReload();
                }
            }

            function failReload() {
                phase = 0;
                status.innerHTML = config.failText;
                status.style.color = "#800";
                setTimeout(() => {
                    pos = 0;
                    slider.style.left = '0px';
                    status.innerHTML = "PRESS SPACE TO START";
                    status.style.color = "#ff2a2a";
                }, 1000);
            }

            function successReload() {
                clearInterval(reloadInterval);
                status.innerHTML = config.successText;
                status.style.color = "#fff";
                status.style.textShadow = "0 0 20px #fff";
                
                // Visual flare
                sweetSpot.style.background = "#fff";
                sweetSpot.style.boxShadow = "0 0 30px #fff";
                playShootSound();

                setTimeout(() => {
                    overlay.style.opacity = 0;
                    overlay.style.pointerEvents = 'none';
                    if(s1Wrapper) s1Wrapper.classList.add('revealed');
                    if(config.onSuccess) config.onSuccess();
                }, 1000);
            }

            // Remove old handler if any and bind new
            document.onkeydown = function(e) {
                if(e.code === 'Space' && slides[currentSlideIndex].id === config.slideId) {
                    e.preventDefault();
                    if(phase === 0) {
                        phase = 1;
                        status.innerHTML = "RELOADING...";
                        status.style.color = "#ffaa00";
                        reloadInterval = setInterval(updateGame, 20);
                    } else if(phase === 1) {
                        let sliderCenter = pos + 5;
                        if(sliderCenter >= spotLeft && sliderCenter <= (spotLeft + spotWidth)) {
                            successReload();
                        } else {
                            clearInterval(reloadInterval);
                            failReload();
                        }
                    }
                }
            }
        }
'''

# We need to find the old manual active reload code and completely replace it
import re
# Since python regex for multi-line is tricky, we'll slice
start_marker = "        function startActiveReload() {"
end_marker = "        function nextSlide(index) {"
if start_marker in html:
    idx_start = html.find(start_marker)
    idx_end = html.find(end_marker)
    html = html[:idx_start] + js_active_reload_factory + "\n" + html[idx_end:]

# Now connect the slide transitions to the factory
transition_code = '''
            if(num === 2) {
                // Slide 2 is Agenda, Slide 3 is Chapter 1 Title
                // We show slide 2 normally
                revealContent(num);
            } else if (slides[num-1].id === 'slide-3') {
                // Chapter 1 active reload
                startActiveReload({
                    slideId: 'slide-3',
                    overlayId: 'overlay-3',
                    statusId: 'reload-status-3',
                    sweetSpotId: 'reload-sweet-spot-3',
                    sliderId: 'reload-slider-3',
                    wrapperId: 'content-3',
                    speed: 10,
                    successText: "INTEL DECRYPTED. ACCESS GRANTED.",
                    failText: "DECRYPTION FAILED. JAMMED."
                });
            } else if (slides[num-1].id === 'slide-16') {
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
                });
            } else {
                revealContent(num);
            }
'''
if 'if(num === 16) startActiveReload();' in html:
    html = html.replace('if(num === 16) startActiveReload();\n            else revealContent(num);', transition_code)

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
