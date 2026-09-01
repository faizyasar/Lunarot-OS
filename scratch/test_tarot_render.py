import os
import io
from PIL import Image
from playwright.sync_api import sync_playwright

html_path = os.path.abspath(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_spinning_render.html').replace('\\', '/')

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=1)
    page = context.new_page()
    page.goto(f"file:///{html_path}")
    page.wait_for_timeout(1500)

    # test angle 1 (front)
    page.evaluate("window.__setStageRotation(0, 12)")
    page.wait_for_timeout(50)
    png1 = page.screenshot(omit_background=True, type='png')
    img1 = Image.open(io.BytesIO(png1))
    img1.save('scratch/test_tarot_front.png')
    print('Front bbox:', img1.getbbox())

    # test angle 2 (quarter)
    page.evaluate("window.__setStageRotation(45, 12)")
    page.wait_for_timeout(50)
    png2 = page.screenshot(omit_background=True, type='png')
    img2 = Image.open(io.BytesIO(png2))
    img2.save('scratch/test_tarot_quarter.png')
    print('Quarter bbox:', img2.getbbox())

    # test angle 3 (side)
    page.evaluate("window.__setStageRotation(90, 12)")
    page.wait_for_timeout(50)
    png3 = page.screenshot(omit_background=True, type='png')
    img3 = Image.open(io.BytesIO(png3))
    img3.save('scratch/test_tarot_side.png')
    print('Side bbox:', img3.getbbox())

    # test angle 4 (back)
    page.evaluate("window.__setStageRotation(180, 12)")
    page.wait_for_timeout(50)
    png4 = page.screenshot(omit_background=True, type='png')
    img4 = Image.open(io.BytesIO(png4))
    img4.save('scratch/test_tarot_back.png')
    print('Back bbox:', img4.getbbox())

    browser.close()

print("Tarot screenshots saved successfully!")
