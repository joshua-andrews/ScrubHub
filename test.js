
        let currentSlideIndex = 1;
        const totalSlides = 17;
        let slideUnlocked = false; // Prevents nav before chainsaw

        function updateNav() {
            document.getElementById('slide-indicator').innerText = `SLIDE ${currentSlideIndex} / ${totalSlides}`;
            document.getElementById('slide-indicator').style.display = slideUnlocked ? 'block' : 'none';
            
            const btnPrev = document.getElementById('btn-prev');
            const btnNext = document.getElementById('btn-next');
            
            if(!slideUnlocked) {
                btnNext.style.display = 'none';
                btnPrev.style.display = 'none';
                return;
            }

            btnNext.style.display = 'block';
            btnPrev.style.display = 'block';
            
            if (currentSlideIndex === 1 || currentSlideIndex === 2) {
                btnPrev.disabled = true; // Don't let them go back to slide 1 once unlocked
            } else {
                btnPrev.disabled = false;
            }

            if (currentSlideIndex === totalSlides) {
                btnNext.style.display = 'none';
            } else {
                btnNext.style.display = 'block';
            }
        }

        function prevSlide() {
            if (currentSlideIndex > 2) {
                nextSlide(currentSlideIndex - 1);
            }
        }

        function nextSlide(num) {
            document.querySelectorAll('.slide').forEach(s => s.classList.remove('active-slide'));
            document.getElementById('slide-' + num).classList.add('active-slide');
            currentSlideIndex = num;
            updateNav();
            
            const nextSlideElement = document.getElementById('slide-' + num);
            
            if(num === 2) {
                // Slide 2 is Agenda
                revealContent(num);
            } else if (nextSlideElement && nextSlideElement.id === 'slide-3') {
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
            } else if (nextSlideElement && nextSlideElement.id === 'slide-16') {
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

        }

        function revealContent(slideNum) {
            const overlay = document.getElementById('overlay-' + slideNum);
            if(overlay) {
                overlay.style.opacity = 0;
                overlay.style.pointerEvents = 'none';
            }
            setTimeout(() => {
                const content = document.getElementById('content-' + slideNum);
                if(content) content.classList.add('revealed');
            }, 100);
        }

        revealContent(1); // Reveal slide 1 instantly

        // --- Slide 1 -> 2: Chainsaw Transition ---
        const s1 = document.getElementById('slide-1');
        const s2 = document.getElementById('slide-2');
        const fill = document.getElementById('chainsaw-fill');
        const s1Overlay = document.getElementById('chainsaw-overlay');
        const content1 = document.getElementById('content-1');
        const content2 = document.getElementById('content-2');
        const chainsawAudio = document.getElementById('chainsaw-sound');
        
        let progress = 0;
        let isChainsawing = false;
        let drainInterval = null;

        // Pre-render slide 2 safely underneath
        s2.style.display = 'flex';
        s2.style.position = 'absolute';
        s2.style.top = '0';
        s2.style.left = '0';
        s2.style.width = '100%';
        s2.style.height = '100%';
        s2.style.zIndex = '10';

        document.addEventListener('keydown', (e) => {
            if ((e.code === 'KeyB' || e.key === 'b' || e.key === 'B') && s1.classList.contains('active-slide') && progress < 100) {
                if (!isChainsawing) {
                    isChainsawing = true;
                    s1.classList.add('shaking');
                    chainsawAudio.volume = 1;
                    chainsawAudio.play().catch(e => console.log("Audio play failed depending on browser policy", e));
                }
            }
        });

        document.addEventListener('keyup', (e) => {
            if ((e.code === 'KeyB' || e.key === 'b' || e.key === 'B') && s1.classList.contains('active-slide')) {
                isChainsawing = false;
                s1.classList.remove('shaking');
            }
        });

        setInterval(() => {
            if (s1.classList.contains('active-slide')) {
                if (isChainsawing) {
                    if (chainsawAudio.volume < 1) chainsawAudio.volume = 1;
                } else {
                    // Fade out audio over a short duration
                    if (chainsawAudio.volume > 0.1) {
                        chainsawAudio.volume -= 0.1;
                    } else if (!chainsawAudio.paused) {
                        chainsawAudio.pause();
                        chainsawAudio.volume = 0;
                    }
                    
                    // Gradually drain the timeline audio position to correctly tie Audio -> Progress
                    if (chainsawAudio.paused && chainsawAudio.currentTime > 0) {
                        chainsawAudio.currentTime = Math.max(0, chainsawAudio.currentTime - 0.05); // Rolls back timeline
                    }
                }

                // Strictly tie the progress visual to 2.5 seconds of the audio's currentTime
                let targetDuration = 2.5;
                if (chainsawAudio) {
                    progress = (chainsawAudio.currentTime / targetDuration) * 100;
                }
                
                // Cap progress
                if (progress > 100) progress = 100;

                fill.style.width = progress + '%';
                
                // Visual transition effect
                let opacity = 1 - (progress / 100);
                content1.style.opacity = Math.max(0, opacity);
                content1.style.transform = `scale(${1 + (progress/200)})`; // Zooms in slightly
                s1Overlay.style.background = `rgba(255,0,0, ${progress / 150})`; // Adds a red tint 
                
                // Gradually map slide 2's opacity to the slide 1 hold progress directly for a smooth fade-in
                content2.style.opacity = Math.max(0, progress / 100);

                if (progress >= 100 && !slideUnlocked) {
                    isChainsawing = false; 
                    s1.classList.remove('shaking');
                    s1.classList.remove('active-slide');
                    slideUnlocked = true;
                    
                    // Fade audio out smoothly into slide 2, then pause
                    let fadeInterval = setInterval(() => {
                        if (chainsawAudio.volume > 0.1) chainsawAudio.volume -= 0.1;
                        else {
                            chainsawAudio.pause();
                            clearInterval(fadeInterval);
                        }
                    }, 50);
                    
                    // Cleanup inline styles completely to allow display: none swapping for Next slides
                    s2.style.display = '';
                    s2.style.position = '';
                    s2.style.top = '';
                    s2.style.left = '';
                    s2.style.width = '';
                    s2.style.height = '';
                    s2.style.zIndex = '';
                    content2.style.opacity = '';
                    content2.classList.add('revealed');
                    s1.style.display = 'none';
                    
                    // Safely transition exactly to Slide 2
                    nextSlide(2);
                }
            }
        }, 30);


        // --- Active Reload Engine ---


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
                if(e.code === 'Space' && document.getElementById('slide-' + currentSlideIndex) && document.getElementById('slide-' + currentSlideIndex).id === config.slideId) {
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


