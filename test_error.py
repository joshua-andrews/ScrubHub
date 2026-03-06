from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    page.on("pageerror", lambda exc: print(f"PAGE ERROR: {exc}"))
    page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
    
    page.goto('file://c:/Users/joshu/Documents/Antigravity Projects/Clients/ScrubHub/scrubhub_tactical_pitch.html')
    
    page.wait_for_timeout(2000)
    browser.close()
