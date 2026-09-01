import os
import io
from playwright.sync_api import sync_playwright
from PIL import Image

# Let's update scratch/cassette_standalone.html with optimal camera & lighting
with open('scratch/build_standalone.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Adjust camera position and lighting for maximum visual wow factor
code = code.replace(
    "camera.position.set(0, 20, 160);",
    "camera.position.set(0, 6, 185);"
)

with open('scratch/build_standalone.py', 'w', encoding='utf-8') as f:
    f.write(code)

os.system('python scratch/build_standalone.py')

html_path = os.path.abspath('scratch/cassette_standalone.html')

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=1)
    page = context.new_page()
    page.goto(f"file:///{html_path.replace(os.sep, '/')}")
    page.wait_for_timeout(2000)

    # Test full 360 rotation bounds
    min_x, min_y, max_x, max_y = 1000, 1000, 0, 0
    for deg in range(0, 360, 30):
        rad = deg * 3.14159265 / 180.0
        page.evaluate(f"window.__setRotation({rad}, 0.16, 0)")
        page.wait_for_timeout(30)
        png = page.screenshot(omit_background=True, type='png')
        img = Image.open(io.BytesIO(png))
        bbox = img.getbbox()
        if bbox:
            min_x = min(min_x, bbox[0])
            min_y = min(min_y, bbox[1])
            max_x = max(max_x, bbox[2])
            max_y = max(max_y, bbox[3])
            print(f"Angle {deg:3d}°: bbox={bbox}")

    print(f"Overall bounding box across full 360°: ({min_x}, {min_y}, {max_x}, {max_y}), span: ({max_x - min_x} x {max_y - min_y})")
    browser.close()
