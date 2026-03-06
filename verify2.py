html = open('scrubhub_tactical_pitch.html', encoding='utf-8').read()
checks = {
    'Shotgun final audio': 'shotgun_final.mp3' in html,
    'Audit photo buttons on slide-4': 'VIEW HERO SECTION' in html,
    'Text-shatter letter blocks': 'TEXT-SHATTER: Bold letter' in html,
    'Chapter 4 title slide': 'id="slide-ch4"' in html,
    'Marketing Engine slide-12': 'Our Marketing Engine' in html,
    'Tech arch removed': 'Technical Architecture (Risk Mitigation)' not in html,
    'Chapter 5 title slide': 'id="slide-ch5"' in html,
    'Boss fight combined slide-16': 'hod-title-screen' in html,
    'Boss auto-start after 2s': '2000' in html and 'hod-title-screen' in html,
    'Great Work final slide': 'Great Work, Soldier' in html,
    'Approvals in What We Need': 'Scope of Work Approval' in html,
}
for k,v in checks.items():
    print('[OK]' if v else '[FAIL]', k)

import re
comments = re.findall(r'<!-- [A-Z].*?-->', html)
print('\nSlide order:')
for c in comments: print(' ', c)
