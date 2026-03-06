from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Setup console logging
    def on_console(msg):
        print(f"CONSOLE {msg.type}: {msg.text}")
    
    page.on("console", on_console)
    page.goto('file://c:/Users/joshu/Documents/Antigravity Projects/Clients/ScrubHub/scrubhub_tactical_pitch.html')
    
    # Wait a sec
    page.wait_for_timeout(1000)
    
    # Press B
    print("Pressing B...")
    page.keyboard.down("b")
    page.wait_for_timeout(3000)
    page.keyboard.up("b")
    
    print("Done waiting.")
    browser.close()
