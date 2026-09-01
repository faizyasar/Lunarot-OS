import os
import io
import time
from PIL import Image
from playwright.sync_api import sync_playwright

html_path = os.path.abspath(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_clean_render.html').replace('\\', '/')

print("Step 1: Capturing 720 frames for 28.8s Half-Speed Loop...", flush=True)
start_time = time.time()

num_frames = 720
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
        page.wait_for_timeout(1)

        png_bytes = page.screenshot(omit_background=True, type='png')
        img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")

        # Center crop: center (400, 422), 540x540 box -> resize to 420x420
        crop_box = (400 - 270, 422 - 270, 400 + 270, 422 + 270)
        cropped_img = img.crop(crop_box).resize((420, 420), Image.Resampling.LANCZOS)
        frames.append(cropped_img)

        if (i + 1) % 180 == 0 or i == num_frames - 1:
            print(f"Captured {i + 1}/{num_frames} frames ({time.time() - start_time:.1f}s)", flush=True)

    browser.close()

print(f"Step 2: Compiling Half-Speed WebP and GIF (duration=40ms, 28.8s loop)...", flush=True)

out_temp_webp = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_half_speed.webp'
out_desktop_webp = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'

frames[0].save(
    out_temp_webp,
    save_all=True,
    append_images=frames[1:],
    duration=40,
    loop=0,
    quality=85,
    method=4
)

import shutil
shutil.copy2(out_temp_webp, out_desktop_webp)
print(f"Saved Half-Speed WebP to: {out_desktop_webp} ({os.path.getsize(out_desktop_webp):,} bytes)", flush=True)

# 360-Frame Smooth GIF (80ms per frame x 360 frames = 28.80s loop)
gif_frames = []
sampled = frames[::2]
for frame in sampled:
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
    duration=80,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print(f"Saved Half-Speed GIF to Desktop: {out_desktop_gif} ({os.path.getsize(out_desktop_gif):,} bytes)", flush=True)

gif_frames[0].save(
    out_workspace_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=80,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print(f"Saved Half-Speed GIF to Workspace: {out_workspace_gif} ({os.path.getsize(out_workspace_gif):,} bytes)", flush=True)

print(f"ALL DONE IN {time.time() - start_time:.1f}s", flush=True)
