from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    page.goto('file://c:/Users/joshu/Documents/Antigravity Projects/Clients/ScrubHub/scrubhub_tactical_pitch.html')
    
    # Read the text of the status or width of chainsaw-fill before press
    w1 = page.evaluate("document.getElementById('chainsaw-fill').style.width")
    print("Width before:", w1)
    
    page.keyboard.down("b")
    page.wait_for_timeout(1000)  # Hold for 1 sec
    
    w2 = page.evaluate("document.getElementById('chainsaw-fill').style.width")
    print("Width after 1s:", w2)
    
    page.keyboard.up("b")
    
    browser.close()
