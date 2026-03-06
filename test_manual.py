from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file://c:/Users/joshu/Documents/Antigravity Projects/Clients/ScrubHub/scrubhub_tactical_pitch.html')
    
    # 1. Manually fire event via Javascript inside the browser context
    page.evaluate('''() => {
        let ev = new KeyboardEvent('keydown', { key: 'b', code: 'KeyB', bubbles: true });
        document.dispatchEvent(ev);
    }''')
    
    page.wait_for_timeout(500)
    
    # Check the debug log overlay
    val = page.evaluate('document.getElementById("debug-log").innerText')
    print("DOM LOG CONTENT:")
    print(val)
    
    browser.close()
