with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_logic = '''        setInterval(() => {
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

                fill.style.width = progress + '%';'''

good_logic = '''        setInterval(() => {
            if (s1.classList.contains('active-slide')) {
                let targetDuration = 2.5;

                if (isChainsawing) {
                    progress += (30 / (targetDuration * 1000)) * 100; 
                    if (chainsawAudio && chainsawAudio.volume < 1) chainsawAudio.volume = 1;
                } else {
                    progress -= (30 / 1000) * 100; 
                    if (chainsawAudio) {
                        if (chainsawAudio.volume > 0.1) {
                            chainsawAudio.volume -= 0.1;
                        } else if (!chainsawAudio.paused) {
                            chainsawAudio.pause();
                            chainsawAudio.volume = 0;
                            chainsawAudio.currentTime = 0;
                        }
                    }
                }

                if (progress < 0) progress = 0;
                if (progress > 100) progress = 100;

                fill.style.width = progress + '%';'''

html = html.replace(bad_logic, good_logic)

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
