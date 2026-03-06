from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    def on_console(msg):
        print(f"CONSOLE {msg.type}: {msg.text}")
    page.on("console", on_console)
    page.goto('file://c:/Users/joshu/Documents/Antigravity Projects/Clients/ScrubHub/scrubhub_tactical_pitch.html')
    
    page.evaluate('''() => {
        console.log("s1 classes: ", document.getElementById("slide-1").className);
        console.log("isChainsawing before: ", isChainsawing);
    }''')
    
    page.keyboard.down("b")
    page.wait_for_timeout(500)
    
    page.evaluate('''() => {
        console.log("isChainsawing after: ", isChainsawing);
        console.log("chainsawAudio paused state: ", document.getElementById("chainsaw-sound").paused);
        console.log("progress: ", progress);
    }''')
    
    browser.close()
