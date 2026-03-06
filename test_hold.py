from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file://c:/Users/joshu/Documents/Antigravity Projects/Clients/ScrubHub/scrubhub_tactical_pitch.html')
    
    print("Initial width:", page.evaluate("document.getElementById('chainsaw-fill').style.width"))
    
    # Press and hold B
    page.keyboard.down("b")
    
    for i in range(5):
        time.sleep(0.5)
        w = page.evaluate("document.getElementById('chainsaw-fill').style.width")
        print(f"Width after {i*0.5 + 0.5}s:", w)
        
    page.keyboard.up("b")
    browser.close()
