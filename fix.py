with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix space bar error in startActiveReload
bad_space_check = "if(e.code === 'Space' && slides[currentSlideIndex].id === config.slideId) {"
good_space_check = "if(e.code === 'Space' && document.getElementById('slide-' + currentSlideIndex) && document.getElementById('slide-' + currentSlideIndex).id === config.slideId) {"
html = html.replace(bad_space_check, good_space_check)

# Clean up leftover slide 16 manual active reload variables that cause errors
html = html.replace('''        // --- Slide 16: Active Reload (Pricing) ---
        const slider = document.getElementById('reload-slider');
        const status = document.getElementById('reload-status');
        const overlay16 = document.getElementById('overlay-16');
        let reloadPos = 0;
        let reloadDir = 1;
        let reloadActive = false;
        let rInterval;''', '''        // --- Active Reload Engine ---''')

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
