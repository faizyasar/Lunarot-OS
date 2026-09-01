import os
import io
import json
import base64
import time
from PIL import Image
from playwright.sync_api import sync_playwright

html_path = os.path.abspath(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\cassette_clean_render.html')

# 60 frames for ultra-fast, smooth, tight loop (or 90 frames)
num_frames = 90
frames = []

print(f"Capturing {num_frames} frames via Playwright...")
start_time = time.time()

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    # device_scale_factor=1 for fast crisp capture
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=1)
    page = context.new_page()
    page.goto(f"file:///{html_path.replace(os.sep, '/')}")
    page.wait_for_timeout(1500)

    for i in range(num_frames):
        rad = (i / num_frames) * 2 * 3.141592653589793
        page.evaluate(f"window.__setRotation({rad}, 0.14, 0)")
        page.wait_for_timeout(10)

        png_bytes = page.screenshot(omit_background=True, type='png')
        img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")

        # Crop center 700x700 -> resize to 420x420
        w, h = img.size
        crop_box = (w//2 - 350, h//2 - 350, w//2 + 350, h//2 + 350)
        cropped_img = img.crop(crop_box).resize((420, 420), Image.Resampling.LANCZOS)
        frames.append(cropped_img)

        if (i + 1) % 30 == 0:
            print(f"Captured {i + 1}/{num_frames} frames ({time.time() - start_time:.1f}s)")

    browser.close()

print(f"Capture completed in {time.time() - start_time:.1f}s. Encoding WebP and GIF...")

# 1. High Quality Transparent Animated WebP (60 FPS -> 16ms)
output_desktop_webp = r'C:\Users\faizy\Desktop\cassette_spinning.webp'
frames[0].save(
    output_desktop_webp,
    save_all=True,
    append_images=frames[1:],
    duration=17,
    loop=0,
    quality=85,
    method=6
)
print("Saved WebP to:", output_desktop_webp, f"({os.path.getsize(output_desktop_webp)} bytes)")

# 2. Transparent Spinning GIF (60 FPS -> 17ms)
gif_frames = []
for frame in frames:
    alpha = frame.split()[3]
    mask = Image.eval(alpha, lambda a: 255 if a <= 12 else 0)
    rgb_frame = frame.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=128)
    rgb_frame.paste(255, mask)
    rgb_frame.info['transparency'] = 255
    gif_frames.append(rgb_frame)

output_desktop_gif = r'C:\Users\faizy\Desktop\cassette_spinning.gif'
output_workspace_gif = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\cassette_spinning.gif'

gif_frames[0].save(
    output_desktop_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=17,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print("Saved GIF to Desktop:", output_desktop_gif, f"({os.path.getsize(output_desktop_gif)} bytes)")

gif_frames[0].save(
    output_workspace_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=17,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print("Saved GIF to Workspace:", output_workspace_gif, f"({os.path.getsize(output_workspace_gif)} bytes)")
print("ALL DONE!")
