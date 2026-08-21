import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.goto("file:///c:/Users/faizy/Documents/Lunarot%20Engine/Lunarot-Tarot-Engine-1.0/open3dviewer_skeletal_figure.html")
        await page.wait_for_timeout(3000)
        await page.screenshot(path="scratch/preview.png")
        await browser.close()

asyncio.run(main())
