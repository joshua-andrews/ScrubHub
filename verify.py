html = open('scrubhub_tactical_pitch.html', encoding='utf-8').read()
checks = {
  'Agenda Marketing Overview': '4. Marketing Overview' in html,
  'Agenda Execution Details': '5. Execution Details' in html,
  'Agenda Hammer of ScrubHub': 'The Hammer of ScrubHub' in html,
  'Active reload PRESS SPACE text': 'PRESS SPACE TO RELOAD' in html,
  'New shotgun audio': 'shotgun_v2.mp3' in html,
  'Text particles from title': 'TEXT-side particles' in html,
  'Photo buttons on audit slide': 'HERO SECTION' in html,
  'What We Need new items': 'Scope of Work Approval' in html,
  'Final Chapter slide': 'slide-final-ch' in html,
  'Great work soldier text': 'Great Work, Soldier' in html,
  'Investment slide removed': '<!-- SLIDE 16: INVESTMENT' not in html,
  'Shotgun V2 audio tag': 'shotgun_v2' in html,
}
for k,v in checks.items():
    print(('[OK]' if v else '[FAIL]'), k)
total = html.count('class="slide"')
print(f'Total slide divs: {total}')
