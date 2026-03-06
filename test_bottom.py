with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('</body>', '''
    <script>
        logDebug("Bottom of script reached.");
        setTimeout(() => {
            logDebug("Dispatching synthetic B event...");
            document.dispatchEvent(new KeyboardEvent('keydown', { key: 'b', code: 'KeyB', bubbles: true }));
        }, 3000);
    </script>
</body>''')

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
