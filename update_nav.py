with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix updateNav slide-indicator crash
bad_nav = '''
        function updateNav() {
            document.getElementById('slide-indicator').innerText = SLIDE  / ;
            document.getElementById('slide-indicator').style.display = slideUnlocked ? 'block' : 'none';
            
            const btnPrev = document.getElementById('btn-prev');
            const btnNext = document.getElementById('btn-next');
'''
good_nav = '''
        function updateNav() {
            let indicator = document.getElementById('slide-indicator');
            if(indicator) {
                indicator.innerText = SLIDE  / ;
                indicator.style.display = slideUnlocked ? 'block' : 'none';
            }
            
            const btnPrev = document.getElementById('btn-prev');
            const btnNext = document.getElementById('btn-next');
'''
html = html.replace(bad_nav, good_nav)

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
