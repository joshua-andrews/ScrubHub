with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad1 = "if ((e.code === 'KeyB' || e.key === 'b' || e.key === 'B') && s1.classList.contains('active-slide') && progress < 100) {"
good1 = "console.log('keydown', e.code, e.key, s1.classList.contains('active-slide'), progress);\n            if ((e.code === 'KeyB' || e.key === 'b' || e.key === 'B') && s1.classList.contains('active-slide') && progress < 100) {"

bad2 = "let targetDuration = 2.5;"
good2 = "let targetDuration = 2.5;\n                if(isChainsawing) console.log('interval progress', progress);"

html = html.replace(bad1, good1).replace(bad2, good2)

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
