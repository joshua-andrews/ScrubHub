from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file://c:/Users/joshu/Documents/Antigravity Projects/Clients/ScrubHub/scrubhub_tactical_pitch.html')
    
    page.keyboard.down('b')
    page.wait_for_timeout(1500)
    page.keyboard.up('b')
    
    val = page.evaluate('document.getElementById("debug-log").innerText')
    print("DOM LOG CONTENT:\n" + val)
    
    browser.close()
