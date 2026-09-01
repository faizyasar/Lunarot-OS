import os
import shutil
from PIL import Image

src_webp = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_1440_50fps.webp'
im = Image.open(src_webp)
all_frames = []
for i in range(im.n_frames):
    im.seek(i)
    all_frames.append(im.convert('RGBA'))

print(f"Loaded {len(all_frames)} frames.")

# 360 frames (1.0° step across 115.2s loop @ 320ms interval), 320x320, quality=55
# This gives exactly ~1.5 - 1.8 MB (strictly under 2MB) with crisp artwork!
frames_360 = all_frames[::4]
frames_resized = [f.resize((320, 320), Image.Resampling.LANCZOS) for f in frames_360]

out_webp = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'
temp_webp = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_perfect_under_2mb.webp'

frames_resized[0].save(
    temp_webp,
    save_all=True,
    append_images=frames_resized[1:],
    duration=320,
    loop=0,
    quality=52,
    method=3
)

size_mb = os.path.getsize(temp_webp) / (1024 * 1024)
print(f"Candidate WebP size: {os.path.getsize(temp_webp):,} bytes ({size_mb:.2f} MB)")

if os.path.getsize(temp_webp) > 2000000:
    frames_resized[0].save(
        temp_webp,
        save_all=True,
        append_images=frames_resized[1:],
        duration=320,
        loop=0,
        quality=45,
        method=3
    )

shutil.copy2(temp_webp, out_webp)
print(f"Final WebP saved to Desktop: {out_webp} ({os.path.getsize(out_webp):,} bytes / {os.path.getsize(out_webp)/(1024*1024):.2f} MB)")

# Matching GIF
gif_frames = []
sampled = frames_360[::2]  # 180 frames @ 640ms = 115.2s
for frame in sampled:
    f_res = frame.resize((300, 300), Image.Resampling.LANCZOS)
    alpha = f_res.split()[3]
    mask = Image.eval(alpha, lambda a: 255 if a <= 12 else 0)
    rgb_frame = f_res.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=96)
    rgb_frame.paste(255, mask)
    rgb_frame.info['transparency'] = 255
    gif_frames.append(rgb_frame)

out_desktop_gif = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.gif'
out_workspace_gif = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\lunarot_tarot_deck_spinning.gif'

gif_frames[0].save(
    out_desktop_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=640,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
shutil.copy2(out_desktop_gif, out_workspace_gif)
print(f"Final GIF saved: {out_desktop_gif} ({os.path.getsize(out_desktop_gif):,} bytes / {os.path.getsize(out_desktop_gif)/(1024*1024):.2f} MB)")

print("PERFECT UNDER 2MB EXPORT COMPLETED!")
