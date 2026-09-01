import os
import io
import time
from PIL import Image
from playwright.sync_api import sync_playwright

html_path = os.path.abspath(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_clean_render.html').replace('\\', '/')

print("Step 1: Capturing 240 High-DPI frames for ultra-smooth, half-speed showcase spin...", flush=True)
start_time = time.time()

num_frames = 240
frames = []

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    # device_scale_factor=2 for super-sampling antialiasing
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=2)
    page = context.new_page()
    page.goto(f"file:///{html_path}")
    page.wait_for_timeout(1500)

    for i in range(num_frames):
        deg = (i / num_frames) * 360.0
        page.evaluate(f"window.__setStageRotation({deg}, 10)")
        page.wait_for_timeout(4)

        png_bytes = page.screenshot(omit_background=True, type='png')
        img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")

        # High-DPI center crop with supersampling downscale
        w, h = img.size
        # 800 * 2 = 1600 width, crop center (800, 844) with 1080x1080 box -> downsample to 420x420
        cx, cy = w // 2, int(h * 0.5275)
        crop_size = int(w * 0.675)
        crop_box = (cx - crop_size//2, cy - crop_size//2, cx + crop_size//2, cy + crop_size//2)
        cropped_img = img.crop(crop_box).resize((420, 420), Image.Resampling.LANCZOS)
        frames.append(cropped_img)

        if (i + 1) % 60 == 0 or i == num_frames - 1:
            print(f"Captured {i + 1}/{num_frames} frames ({time.time() - start_time:.1f}s)", flush=True)

    browser.close()

print(f"Step 2: Encoding Ultra-Smooth Half-Speed WebP and GIF ({time.time() - start_time:.1f}s)...", flush=True)

# 1. Ultra Smooth Animated WebP (240 frames @ 42ms = 10.0s per revolution, velvety smooth)
out_desktop_webp = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'
frames[0].save(
    out_desktop_webp,
    save_all=True,
    append_images=frames[1:],
    duration=42,
    loop=0,
    quality=88,
    method=4
)
print(f"Saved Ultra-Smooth WebP to: {out_desktop_webp} ({os.path.getsize(out_desktop_webp):,} bytes)", flush=True)

# 2. Matching Smooth GIF (120 frames @ 84ms = 10.0s)
gif_frames = []
sampled_frames = frames[::2]
for frame in sampled_frames:
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
    duration=84,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print(f"Saved Ultra-Smooth GIF to Desktop: {out_desktop_gif} ({os.path.getsize(out_desktop_gif):,} bytes)", flush=True)

gif_frames[0].save(
    out_workspace_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=84,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print(f"Saved Ultra-Smooth GIF to Workspace: {out_workspace_gif} ({os.path.getsize(out_workspace_gif):,} bytes)", flush=True)

# Step 3: Update Desktop HTML live spin speed to silky 0.15 deg/frame
desktop_html_path = r'C:\Users\faizy\Desktop\HTMLS\Lunarot Tarot Deck (Spinning Transparent).html'
if os.path.exists(desktop_html_path):
    with open(desktop_html_path, 'r', encoding='utf-8') as f:
        dhtml = f.read()
    dhtml = dhtml.replace('currentY = (currentY + 1.2) % 360;', 'currentY = (currentY + 0.15) % 360;')
    dhtml = dhtml.replace('currentY = (currentY + 0.6) % 360;', 'currentY = (currentY + 0.15) % 360;')
    dhtml = dhtml.replace('currentY = (currentY + 0.3) % 360;', 'currentY = (currentY + 0.15) % 360;')
    with open(desktop_html_path, 'w', encoding='utf-8') as f:
        f.write(dhtml)
    print("Updated Desktop HTML live spin speed to silky 0.15 deg/frame (~40s per full loop)")

print("ALL DONE IN", f"{time.time() - start_time:.1f}s", flush=True)
