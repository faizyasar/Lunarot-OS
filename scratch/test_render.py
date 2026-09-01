import os
import io
from playwright.sync_api import sync_playwright
from PIL import Image

html_path = os.path.abspath('scratch/cassette_standalone.html')

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=1)
    page = context.new_page()
    page.goto(f"file:///{html_path.replace(os.sep, '/')}")
    page.wait_for_timeout(2000)

    # test angle 1 (front)
    page.evaluate("window.__setRotation(0, 0.12, 0)")
    page.wait_for_timeout(100)
    png1 = page.screenshot(omit_background=True, type='png')
    Image.open(io.BytesIO(png1)).save('scratch/test_angle_front.png')

    # test angle 2 (quarter)
    page.evaluate("window.__setRotation(0.785, 0.18, 0)")
    page.wait_for_timeout(100)
    png2 = page.screenshot(omit_background=True, type='png')
    Image.open(io.BytesIO(png2)).save('scratch/test_angle_quarter.png')

    # test angle 3 (back)
    page.evaluate("window.__setRotation(3.14159, 0.12, 0)")
    page.wait_for_timeout(100)
    png3 = page.screenshot(omit_background=True, type='png')
    Image.open(io.BytesIO(png3)).save('scratch/test_angle_back.png')

    browser.close()

print("Saved test screenshots to scratch/test_angle_*.png")
