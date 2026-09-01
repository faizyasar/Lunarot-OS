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

# Strategy: 480 high-density frames (0.75° per step @ 240ms duration = 115.2s loop)
# Resized to 360x360 with quality=60, method=3
frames_480 = all_frames[::3]
frames_480_360 = [f.resize((360, 360), Image.Resampling.LANCZOS) for f in frames_480]

out_webp = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'
temp_webp = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_under_2mb.webp'

frames_480_360[0].save(
    temp_webp,
    save_all=True,
    append_images=frames_480_360[1:],
    duration=240,
    loop=0,
    quality=55,
    method=3
)

size = os.path.getsize(temp_webp)
print(f"Candidate WebP size: {size:,} bytes ({size / (1024*1024):.2f} MB)")

if size > 2000000:
    # Reduce slightly if needed
    frames_480_320 = [f.resize((320, 320), Image.Resampling.LANCZOS) for f in frames_480]
    frames_480_320[0].save(
        temp_webp,
        save_all=True,
        append_images=frames_480_320[1:],
        duration=240,
        loop=0,
        quality=50,
        method=3
    )
    size = os.path.getsize(temp_webp)
    print(f"Adjusted WebP size: {size:,} bytes ({size / (1024*1024):.2f} MB)")

shutil.copy2(temp_webp, out_webp)
print(f"Successfully saved WebP to Desktop: {out_webp} ({os.path.getsize(out_webp):,} bytes / {os.path.getsize(out_webp)/(1024*1024):.2f} MB)")

# Also create matching compact GIF under 5MB
gif_frames = []
sampled = frames_480[::3] # 160 frames
for frame in sampled:
    f_res = frame.resize((320, 320), Image.Resampling.LANCZOS)
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
    duration=720,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
shutil.copy2(out_desktop_gif, out_workspace_gif)
print(f"Successfully saved compact GIF: {out_desktop_gif} ({os.path.getsize(out_desktop_gif):,} bytes / {os.path.getsize(out_desktop_gif)/(1024*1024):.2f} MB)")
