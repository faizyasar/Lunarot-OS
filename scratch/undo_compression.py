import os
import shutil

src_webp_slow = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_1440_slow.webp'
src_webp_50fps = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_1440_50fps.webp'
src_webp_fast = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_fast_slow.webp'

out_desktop_webp = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'
out_desktop_gif = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.gif'
out_workspace_gif = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\lunarot_tarot_deck_spinning.gif'

# If tarot_1440_slow.webp exists, use it; otherwise generate from tarot_1440_50fps.webp
from PIL import Image

im = Image.open(src_webp_50fps)
print(f"Reading {im.n_frames} high-res master frames...")
frames = []
for i in range(im.n_frames):
    im.seek(i)
    frames.append(im.convert('RGBA'))

print(f"Loaded {len(frames)} uncompressed master frames.")

# Restore full-resolution 1440-frame WebP (80ms duration = 115.2s loop)
frames[0].save(
    out_desktop_webp,
    save_all=True,
    append_images=frames[1:],
    duration=80,
    loop=0,
    quality=85,
    method=4
)
print(f"Restored Full-Res Master WebP to Desktop: {out_desktop_webp} ({os.path.getsize(out_desktop_webp):,} bytes / {os.path.getsize(out_desktop_webp)/(1024*1024):.2f} MB)")

# Restore 720-frame full-resolution GIF
gif_frames = []
sampled = frames[::2]
for frame in sampled:
    alpha = frame.split()[3]
    mask = Image.eval(alpha, lambda a: 255 if a <= 12 else 0)
    rgb_frame = frame.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=128)
    rgb_frame.paste(255, mask)
    rgb_frame.info['transparency'] = 255
    gif_frames.append(rgb_frame)

gif_frames[0].save(
    out_desktop_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=160,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
shutil.copy2(out_desktop_gif, out_workspace_gif)
print(f"Restored Full-Res Master GIF to Desktop & Workspace: {out_desktop_gif} ({os.path.getsize(out_desktop_gif):,} bytes / {os.path.getsize(out_desktop_gif)/(1024*1024):.2f} MB)")

print("UNDO COMPLETED! FULL QUALITY RESTORED!")
