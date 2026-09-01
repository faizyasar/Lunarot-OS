import json
import re
import os
import io
from PIL import Image
from playwright.sync_api import sync_playwright

src_path = r'C:\Users\faizy\Desktop\HTMLS\Astral Pachinko - Cartridge, Case & Magazine.html'
with open(src_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make background transparent and disable transitions
html = html.replace('background: #000000;', 'background: transparent !important;')
html = html.replace('html, body { width: 100%; height: 100%; overflow: hidden; background: transparent;',
                    'html, body { width: 100%; height: 100%; overflow: hidden; background: transparent !important;')
html = html.replace('html.solo, body.solo { background: radial-gradient(circle at 50% 46%, #0b0b0b, #000 78%); }',
                    'html.solo, body.solo { background: transparent !important; }')

# Disable all transitions to avoid animation jitter
html = html.replace('</style>', '* { transition: none !important; animation: none !important; }\n.hint-bar { display: none !important; }\n</style>')

# Add rotation controller
control_script = """
<script>
window.__setStageRotation = function(yDeg, xDeg) {
    const stage = document.getElementById('stage');
    if (stage) {
        stage.style.opacity = '1';
        stage.style.transform = `rotateX(${xDeg !== undefined ? xDeg : 8}deg) rotateY(${yDeg}deg)`;
    }
};
</script>
"""
html = html.replace('</body>', control_script + '\n</body>')

clean_html_path = r'C:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\astral_pachinko_render.html'
with open(clean_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved clean render HTML to:", clean_html_path)

# Also create continuous spinning HTML on desktop
desktop_spinning_html = html.replace('</style>', """
@keyframes autoSpinPachinko {
  0% { transform: rotateX(8deg) rotateY(0deg); opacity: 1; }
  100% { transform: rotateX(8deg) rotateY(360deg); opacity: 1; }
}
.stage {
  opacity: 1 !important;
  animation: autoSpinPachinko 6s linear infinite !important;
}
</style>
""")

desktop_html_path = r'C:\Users\faizy\Desktop\HTMLS\Astral Pachinko (Spinning Transparent).html'
with open(desktop_html_path, 'w', encoding='utf-8') as f:
    f.write(desktop_spinning_html)
print("Saved spinning HTML to:", desktop_html_path)

# Capture 90 frames (50 FPS, 20ms duration = perfectly smooth 1.8s loop)
num_frames = 90
frames = []

print(f"Capturing {num_frames} frames via Playwright...")
with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    context = browser.new_context(viewport={'width': 800, 'height': 800}, device_scale_factor=1)
    page = context.new_page()
    page.goto(f"file:///{clean_html_path.replace(os.sep, '/')}")
    page.wait_for_timeout(2000)

    for i in range(num_frames):
        deg = (i / num_frames) * 360.0
        page.evaluate(f"window.__setStageRotation({deg}, 8)")
        page.evaluate("() => document.body.offsetHeight")
        page.wait_for_timeout(20)

        png_bytes = page.screenshot(omit_background=True, type='png')
        img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")

        # Crop to center 600x600 -> resize to 380x380 for crisp compressed output
        w, h = img.size
        crop_box = (w//2 - 300, h//2 - 300, w//2 + 300, h//2 + 300)
        cropped_img = img.crop(crop_box).resize((380, 380), Image.Resampling.LANCZOS)
        frames.append(cropped_img)

        if (i + 1) % 30 == 0:
            print(f"Captured {i + 1}/{num_frames} frames ({deg:.1f}°)")

    browser.close()

print("Capture complete! Compiling 50fps transparent GIF and WebP...")

# 1. Transparent Animated WebP
output_webp = r'C:\Users\faizy\Desktop\astral_pachinko_spinning.webp'
frames[0].save(
    output_webp,
    save_all=True,
    append_images=frames[1:],
    duration=20,
    loop=0,
    quality=80,
    method=6
)
print("Saved WebP to:", output_webp)

# 2. Transparent Spinning GIF (50fps, 128 adaptive colors for small file size)
gif_frames = []
for frame in frames:
    alpha = frame.split()[3]
    mask = Image.eval(alpha, lambda a: 255 if a <= 12 else 0)
    rgb_frame = frame.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=128)
    rgb_frame.paste(255, mask)
    rgb_frame.info['transparency'] = 255
    gif_frames.append(rgb_frame)

output_desktop_gif = r'C:\Users\faizy\Desktop\astral_pachinko_spinning.gif'
output_workspace_gif = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\astral_pachinko_spinning.gif'

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
print("Saved GIF to Desktop:", output_desktop_gif)

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
print("Saved GIF to Workspace:", output_workspace_gif)
