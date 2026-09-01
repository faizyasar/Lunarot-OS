import os
import io
import time
from PIL import Image
from playwright.sync_api import sync_playwright

clean_html_path = r'C:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\cd_standalone_render.html'

# Read HTML and ensure ALL transitions are completely removed
with open(clean_html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Force disable all transitions
html = html.replace('transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);', 'transition: none !important;')
html = html.replace('transition: transform 0.55s cubic-bezier(0.2, 0.8, 0.25, 1);', 'transition: none !important;')
html = html.replace('</style>', '* { transition: none !important; animation: none !important; }\n</style>')

with open(clean_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated HTML with transitions disabled.")

# We want butter smooth 60fps (or 50fps max GIF speed).
# For 50fps GIF (20ms delay): 60 frames = 1.2s rotation, or 100 frames = 2s rotation.
# 100 frames with 20ms delay = 50 FPS (butter smooth, zero browser clamp lag!)
num_frames = 90  # 90 frames at 25ms delay (40fps) or 20ms delay (50fps)
frames = []

print(f"Capturing {num_frames} clean frames...")

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=1)
    page = context.new_page()
    page.goto(f"file:///{clean_html_path.replace(os.sep, '/')}")
    page.wait_for_timeout(1000)

    for i in range(num_frames):
        deg = (i / num_frames) * 360.0
        page.evaluate(f"""() => {{
            const scene = document.getElementById('cdScene');
            scene.style.transform = 'rotateX(6deg) rotateY({deg}deg)';
        }}""")
        # Force a reflow / repaint
        page.evaluate("() => document.body.offsetHeight")
        page.wait_for_timeout(20)
        
        png_bytes = page.screenshot(omit_background=True, type='png')
        img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
        
        # Crop to bounding box 550x550 centered
        w, h = img.size
        crop_box = (w//2 - 275, h//2 - 275, w//2 + 275, h//2 + 275)
        cropped_img = img.crop(crop_box)
        frames.append(cropped_img)

    browser.close()

print("Capture complete! Building smooth GIF with 20ms delay (50fps) and WebP...")

# Build GIF with proper 20ms delay (which browsers render at full speed without throttling)
gif_frames = []
for frame in frames:
    alpha = frame.split()[3]
    mask = Image.eval(alpha, lambda a: 255 if a <= 15 else 0)
    
    rgb = frame.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
    rgb.paste(255, mask)
    rgb.info['transparency'] = 255
    gif_frames.append(rgb)

# 20ms duration = 50 FPS (the maximum supported speed in GIF spec without 100ms penalty)
output_desktop_gif = r'C:\Users\faizy\Desktop\cd_jewel_case_spinning.gif'
output_workspace_gif = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\cd_jewel_case_spinning.gif'

gif_frames[0].save(
    output_desktop_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=20,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print("Saved butter-smooth GIF to Desktop:", output_desktop_gif)

gif_frames[0].save(
    output_workspace_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=20,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print("Saved butter-smooth GIF to Workspace:", output_workspace_gif)

# Also save 60fps WebP (16ms duration)
output_webp = r'C:\Users\faizy\Desktop\cd_jewel_case_spinning.webp'
frames[0].save(
    output_webp,
    save_all=True,
    append_images=frames[1:],
    duration=20,
    loop=0,
    quality=90
)
print("Saved 60fps WebP to Desktop:", output_webp)
