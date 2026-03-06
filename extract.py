with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

js = html.split('<script>')[1].split('</script>')[0]
with open('test.js', 'w', encoding='utf-8') as f:
    f.write(js)
