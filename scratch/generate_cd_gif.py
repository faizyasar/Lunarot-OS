import json
import re
import os
import io
import base64
from PIL import Image
from playwright.sync_api import sync_playwright

clean_html_path = r'C:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\cd_standalone_render.html'

# Capture 180 frames for an ultra-smooth 60fps 3-second loop (2 degrees per frame)
num_frames = 180
frames = []

print(f"Starting buttery 60fps capture ({num_frames} frames)...")

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    # Higher quality rendering with 500x500 tight crop
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=1)
    page = context.new_page()
    page.goto(f"file:///{clean_html_path.replace(os.sep, '/')}")
    page.wait_for_timeout(1000)

    for i in range(num_frames):
        deg = (i / num_frames) * 360.0
        page.evaluate(f"window.__setRotation({deg}, 6)")
        # Small wait for DOM repaint
        page.wait_for_timeout(16)
        
        # Transparent screenshot
        png_bytes = page.screenshot(omit_background=True, type='png')
        img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
        
        # Tight crop around CD model (center 800x800 -> 600x600)
        w, h = img.size
        crop_box = (w//2 - 300, h//2 - 300, w//2 + 300, h//2 + 300)
        cropped_img = img.crop(crop_box)
        frames.append(cropped_img)
        
        if (i + 1) % 30 == 0:
            print(f"Captured {i + 1}/{num_frames} frames ({deg:.1f}°)")

    browser.close()

print("Capture complete! Compiling 60fps transparent WebP and GIF...")

# 1. 60fps WebP (16.6ms -> 17ms per frame for native 60fps buttery playback)
output_webp = r'C:\Users\faizy\Desktop\cd_jewel_case_spinning.webp'
frames[0].save(
    output_webp,
    save_all=True,
    append_images=frames[1:],
    duration=17,
    loop=0,
    quality=90,
    method=6
)
print("Saved 60fps WebP to:", output_webp)

# 2. 60fps GIF (optimized palette for each frame with transparency preserved)
gif_frames = []
for frame in frames:
    alpha = frame.split()[3]
    mask = Image.eval(alpha, lambda a: 255 if a <= 12 else 0)
    
    rgb_frame = frame.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
    rgb_frame.paste(255, mask)
    rgb_frame.info['transparency'] = 255
    gif_frames.append(rgb_frame)

output_desktop_gif = r'C:\Users\faizy\Desktop\cd_jewel_case_spinning.gif'
output_workspace_gif = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\cd_jewel_case_spinning.gif'

gif_frames[0].save(
    output_desktop_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=17,
    loop=0,
    transparency=255,
    disposal=2
)
print("Saved 60fps GIF to:", output_desktop_gif)

gif_frames[0].save(
    output_workspace_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=17,
    loop=0,
    transparency=255,
    disposal=2
)
print("Saved 60fps GIF to workspace:", output_workspace_gif)
