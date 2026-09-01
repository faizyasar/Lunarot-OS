import os
import io
import json
import base64
from PIL import Image
from playwright.sync_api import sync_playwright

print("Step 1: Preparing Standalone and Clean Render HTML...")
os.system('python "c:\\Users\\faizy\\Documents\\Lunarot Engine\\Lunarot-Tarot-Engine-1.0\\scratch\\generate_cassette_files.py"')

html_path = os.path.abspath(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\cassette_clean_render.html')

# Save to Desktop HTMLS folder as well
desktop_html_dir = r'C:\Users\faizy\Desktop\HTMLS'
os.makedirs(desktop_html_dir, exist_ok=True)
desktop_html_path = os.path.join(desktop_html_dir, 'Cassette (Spinning Transparent - No Cover).html')

with open(html_path, 'r', encoding='utf-8') as f:
    clean_html_text = f.read()

with open(desktop_html_path, 'w', encoding='utf-8') as f:
    f.write(clean_html_text)

print(f"Saved Desktop HTML to: {desktop_html_path}")

# Step 2: Update the downloaded file C:\Users\faizy\Downloads\Cassette Player Anatomy.html
downloads_path = r'C:\Users\faizy\Downloads\Cassette Player Anatomy.html'
backup_path = r'C:\Users\faizy\Downloads\Cassette Player Anatomy.original.html'

if os.path.exists(downloads_path) and not os.path.exists(backup_path):
    with open(downloads_path, 'r', encoding='utf-8', errors='ignore') as f_src:
        with open(backup_path, 'w', encoding='utf-8') as f_bak:
            f_bak.write(f_src.read())
    print("Backed up original to:", backup_path)

# Also update the downloaded file with the clean standalone / no cover version
with open(downloads_path, 'w', encoding='utf-8') as f_out:
    f_out.write(clean_html_text)
print("Updated Downloads file:", downloads_path)

# Step 3: Capture 120 frames at 60 FPS
num_frames = 120
frames = []

print(f"Step 4: Capturing {num_frames} frames via Playwright (60 FPS smooth rotation)...")

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    # 800x800 high-DPI viewport for antialiasing
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=2)
    page = context.new_page()
    page.goto(f"file:///{html_path.replace(os.sep, '/')}")
    page.wait_for_timeout(2000)

    for i in range(num_frames):
        rad = (i / num_frames) * 2 * 3.141592653589793
        page.evaluate(f"window.__setRotation({rad}, 0.14, 0)")
        page.wait_for_timeout(10)

        png_bytes = page.screenshot(omit_background=True, type='png')
        img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")

        # Crop tight center with subtle padding and downsample for crisp Lanczos supersampling
        w, h = img.size
        crop_size = int(w * 0.95)
        crop_box = (w//2 - crop_size//2, h//2 - crop_size//2, w//2 + crop_size//2, h//2 + crop_size//2)
        cropped_img = img.crop(crop_box).resize((440, 440), Image.Resampling.LANCZOS)
        frames.append(cropped_img)

        if (i + 1) % 30 == 0 or i == num_frames - 1:
            deg = (i / num_frames) * 360.0
            print(f"Captured {i + 1}/{num_frames} frames ({deg:.1f}°)")

    browser.close()

print("Frame capture complete! Generating 60 FPS WebP and GIF...")

# 1. High Quality 60 FPS Transparent Animated WebP
output_desktop_webp = r'C:\Users\faizy\Desktop\cassette_spinning.webp'
frames[0].save(
    output_desktop_webp,
    save_all=True,
    append_images=frames[1:],
    duration=16.666,
    loop=0,
    quality=85,
    method=6
)
print("Saved 60fps WebP to:", output_desktop_webp)

# 2. Transparent Spinning GIF (60 FPS / 16.67ms per frame)
# Optimized adaptive palette with crisp transparency preservation
gif_frames = []
for frame in frames:
    alpha = frame.split()[3]
    # Mask transparent areas (alpha <= 12)
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
print("Saved 60fps GIF to Desktop:", output_desktop_gif)

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
print("Saved 60fps GIF to Workspace:", output_workspace_gif)

print("All tasks successfully completed!")
