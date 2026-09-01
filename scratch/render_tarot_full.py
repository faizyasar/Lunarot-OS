import os
import io
import sys
import time
from PIL import Image
from playwright.sync_api import sync_playwright

html_path = os.path.abspath(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_clean_render.html').replace('\\', '/')

print("Step 1: Launching Chrome via Playwright for Lunarot Tarot Deck...", flush=True)
start_time = time.time()

num_frames = 90
frames = []

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    # 800x800 high quality viewport
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=1)
    page = context.new_page()
    page.goto(f"file:///{html_path}")
    page.wait_for_timeout(1500)

    print(f"Step 2: Capturing {num_frames} frames (60 FPS smooth spin)...", flush=True)

    for i in range(num_frames):
        deg = (i / num_frames) * 360.0
        page.evaluate(f"window.__setStageRotation({deg}, 10)")
        page.wait_for_timeout(8)

        png_bytes = page.screenshot(omit_background=True, type='png')
        img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")

        # Center crop: center is approx (400, 422) with 540x540 bounding box
        crop_box = (400 - 270, 422 - 270, 400 + 270, 422 + 270)
        cropped_img = img.crop(crop_box).resize((400, 400), Image.Resampling.LANCZOS)
        frames.append(cropped_img)

        if (i + 1) % 30 == 0 or i == num_frames - 1:
            print(f"Captured {i + 1}/{num_frames} frames ({time.time() - start_time:.1f}s)", flush=True)

    browser.close()

print(f"Step 3: Encoding 60 FPS Transparent GIF and WebP...", flush=True)

# 1. High Quality Animated WebP (60 FPS / 17ms per frame)
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
print("Saved WebP to:", out_desktop_webp, f"({os.path.getsize(out_desktop_webp)} bytes)", flush=True)

# 2. Transparent Spinning GIF (60 FPS / 17ms per frame)
gif_frames = []
for frame in frames:
    alpha = frame.split()[3]
    mask = Image.eval(alpha, lambda a: 255 if a <= 12 else 0)
    rgb_frame = frame.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=128)
    rgb_frame.paste(255, mask)
    rgb_frame.info['transparency'] = 255
    gif_frames.append(rgb_frame)

out_desktop_gif = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.gif'
out_workspace_gif = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\lunarot_tarot_deck_spinning.gif'

gif_frames[0].save(
    out_desktop_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=17,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print("Saved GIF to Desktop:", out_desktop_gif, f"({os.path.getsize(out_desktop_gif)} bytes)", flush=True)

gif_frames[0].save(
    out_workspace_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=17,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print("Saved GIF to Workspace:", out_workspace_gif, f"({os.path.getsize(out_workspace_gif)} bytes)", flush=True)

# Step 4: Save Desktop and Downloads HTML files
desktop_html_path = r'C:\Users\faizy\Desktop\HTMLS\Lunarot Tarot Deck (Spinning Transparent).html'
downloads_path = r'C:\Users\faizy\Downloads\Lunarot_Tarot_Deck_-_Standalone.html'
backup_path = r'C:\Users\faizy\Downloads\Lunarot_Tarot_Deck_-_Standalone.original.html'

if os.path.exists(downloads_path) and not os.path.exists(backup_path):
    with open(downloads_path, 'r', encoding='utf-8', errors='ignore') as f_src:
        with open(backup_path, 'w', encoding='utf-8') as f_bak:
            f_bak.write(f_src.read())
    print("Backed up original downloads file to:", backup_path)

with open(html_path, 'r', encoding='utf-8') as f:
    clean_html_text = f.read()

os.makedirs(r'C:\Users\faizy\Desktop\HTMLS', exist_ok=True)
with open(desktop_html_path, 'w', encoding='utf-8') as f:
    f.write(clean_html_text)

with open(downloads_path, 'w', encoding='utf-8') as f:
    f.write(clean_html_text)

print(f"Updated HTML files:\n - {desktop_html_path}\n - {downloads_path}")
print("ALL TASKS COMPLETED SUCCESSFULLY IN", f"{time.time() - start_time:.1f}s", flush=True)
