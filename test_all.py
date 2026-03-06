import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        page.on('console', lambda msg: print('CONSOLE:', msg.text))
        page.on('pageerror', lambda err: print('PAGE ERROR:', err))
        
        await page.goto('file://c:/Users/joshu/Documents/Antigravity Projects/Clients/ScrubHub/scrubhub_tactical_pitch.html')
        await page.wait_for_timeout(1000)
        
        # Dispatch a native event to be 100% sure
        await page.evaluate('''() => {
            const ev = new KeyboardEvent('keydown', { key: 'b', code: 'KeyB' });
            document.dispatchEvent(ev);
        }''')
        
        await page.wait_for_timeout(500)
        
        await browser.close()

asyncio.run(main())
