from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    errors = []
    
    page.on("pageerror", lambda exc: errors.append(str(exc)))
    page.on("console", lambda msg: errors.append(f"CONSOLE {msg.type}: {msg.text}") if msg.type == 'error' else None)
    
    # Also inject a global error listener just in case
    page.add_init_script('''
        window.addEventListener('error', function(e) {
            console.error("GLOBAL ERROR: " + e.message + " at " + e.filename + ":" + e.lineno);
        });
    ''')
    
    page.goto('file://c:/Users/joshu/Documents/Antigravity Projects/Clients/ScrubHub/scrubhub_tactical_pitch.html')
    page.wait_for_timeout(2000)
    
    # Try pressing B
    page.keyboard.down("b")
    page.wait_for_timeout(100)
    page.keyboard.up("b")
    
    with open('js_errors.log', 'w') as f:
        for err in errors:
            f.write(err + "\n")
            
    print("Logged to js_errors.log")
    browser.close()
