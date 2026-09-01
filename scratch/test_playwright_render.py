import asyncio
import os
from playwright.async_api import async_playwright

async def render_test():
    html_path = os.path.abspath(r'C:\Users\faizy\Desktop\Anatomy fixed Casette new.html')
    file_url = f'file:///{html_path.replace("\\", "/")}'
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='msedge', headless=True)
        page = await browser.new_page(viewport={'width': 800, 'height': 800})
        
        # Listen for console messages and errors
        page.on('console', lambda msg: print(f'[Browser Console] {msg.type}: {msg.text}'))
        page.on('pageerror', lambda err: print(f'[Browser PageError] {err}'))
        
        print(f'Navigating to {file_url}...')
        await page.goto(file_url, wait_until='networkidle')
        await asyncio.sleep(3) # Wait for unbundling and rendering
        
        screenshot_path = os.path.abspath(r'scratch\test_render.png')
        await page.screenshot(path=screenshot_path)
        print(f'Saved screenshot to {screenshot_path}')
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(render_test())
