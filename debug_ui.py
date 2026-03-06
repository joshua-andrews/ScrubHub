with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

debug_div = '''
    <div id="debug-log" style="position:fixed; top:10px; left:10px; width:400px; height:800px; background:rgba(0,0,0,0.8); color:lime; z-index:9999; font-family:monospace; pointer-events:none; overflow-y:auto; padding:10px;">DEBUG LOG:</div>
    <script>
        function logDebug(msg) {
            let el = document.getElementById("debug-log");
            if(el) el.innerHTML += "<br>" + msg;
            console.log(msg);
        }
        logDebug("Script Started");
    </script>
'''

html = html.replace('<body>', '<body>' + debug_div)

# Now attach logDebug to the keydown and interval
html = html.replace("console.log('keydown',", "logDebug('keydown ' + e.code + ' ' + progress); console.log('keydown',")
html = html.replace("if(isChainsawing) console.log('interval progress', progress);", "if(isChainsawing) logDebug('interval progress ' + progress);")

with open('scrubhub_tactical_pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)
