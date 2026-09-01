import os
import io
import time
from PIL import Image
from playwright.sync_api import sync_playwright

html_path = os.path.abspath(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_clean_render.html').replace('\\', '/')

print("Generating Half-Speed 60 FPS WebP (3.0s smooth revolution, 180 frames)...", flush=True)
start_time = time.time()

num_frames = 180
frames = []

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=1)
    page = context.new_page()
    page.goto(f"file:///{html_path}")
    page.wait_for_timeout(1500)

    for i in range(num_frames):
        deg = (i / num_frames) * 360.0
        page.evaluate(f"window.__setStageRotation({deg}, 10)")
        page.wait_for_timeout(6)

        png_bytes = page.screenshot(omit_background=True, type='png')
        img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")

        # Center crop: center (400, 422), 540x540 box -> resize to 400x400
        crop_box = (400 - 270, 422 - 270, 400 + 270, 422 + 270)
        cropped_img = img.crop(crop_box).resize((400, 400), Image.Resampling.LANCZOS)
        frames.append(cropped_img)

        if (i + 1) % 45 == 0 or i == num_frames - 1:
            print(f"Captured {i + 1}/{num_frames} frames ({time.time() - start_time:.1f}s)", flush=True)

    browser.close()

# 1. High Quality 60 FPS WebP spinning half as fast (3.0s loop @ 16.67ms / frame)
out_desktop_webp = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'
frames[0].save(
    out_desktop_webp,
    save_all=True,
    append_images=frames[1:],
    duration=17,
    loop=0,
    quality=85,
    method=4
)
print(f"Saved half-speed WebP to: {out_desktop_webp} ({os.path.getsize(out_desktop_webp):,} bytes)", flush=True)

# Also update the Desktop HTML auto-spin speed so it also spins half as fast in browser
desktop_html_path = r'C:\Users\faizy\Desktop\HTMLS\Lunarot Tarot Deck (Spinning Transparent).html'
if os.path.exists(desktop_html_path):
    with open(desktop_html_path, 'r', encoding='utf-8') as f:
        dhtml = f.read()
    # change speed from 1.2 to 0.6 deg per frame
    dhtml = dhtml.replace('currentY = (currentY + 1.2) % 360;', 'currentY = (currentY + 0.6) % 360;')
    with open(desktop_html_path, 'w', encoding='utf-8') as f:
        f.write(dhtml)
    print("Updated Desktop HTML live spin speed to half-speed (0.6 deg/frame)")

print("COMPLETE IN", f"{time.time() - start_time:.1f}s", flush=True)
