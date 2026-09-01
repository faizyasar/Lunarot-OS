import os
import shutil
from PIL import Image

src_webp = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_half_speed.webp'
out_desktop_webp = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'
out_desktop_gif = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.gif'
out_workspace_gif = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\lunarot_tarot_deck_spinning.gif'

im = Image.open(src_webp)
frames = []
for i in range(im.n_frames):
    im.seek(i)
    frames.append(im.convert('RGBA'))

print(f"Loaded {len(frames)} clean frames from scratch.")

# Save 115.2s quarter-speed WebP (160ms per frame x 720 frames)
temp_out_webp = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_quarter_speed.webp'
frames[0].save(
    temp_out_webp,
    save_all=True,
    append_images=frames[1:],
    duration=160,
    loop=0,
    quality=85,
    method=4
)
shutil.copy2(temp_out_webp, out_desktop_webp)
print(f"Saved Quarter-Speed WebP: {out_desktop_webp} ({os.path.getsize(out_desktop_webp):,} bytes)")

# 360-Frame Smooth GIF @ 320ms = 115.2s loop
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
    duration=320,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
shutil.copy2(out_desktop_gif, out_workspace_gif)
print(f"Saved Quarter-Speed GIF: {out_desktop_gif} ({os.path.getsize(out_desktop_gif):,} bytes)")

# Update Desktop HTML live spin speed to quarter-speed (0.013 deg/frame)
desktop_html_path = r'C:\Users\faizy\Desktop\HTMLS\Lunarot Tarot Deck (Spinning Transparent).html'
if os.path.exists(desktop_html_path):
    with open(desktop_html_path, 'r', encoding='utf-8') as f:
        dhtml = f.read()
    dhtml = dhtml.replace('currentY = (currentY + 0.0525) % 360;', 'currentY = (currentY + 0.013) % 360;')
    dhtml = dhtml.replace('currentY = (currentY + 0.105) % 360;', 'currentY = (currentY + 0.013) % 360;')
    with open(desktop_html_path, 'w', encoding='utf-8') as f:
        f.write(dhtml)
    print("Updated Desktop HTML live spin speed to 0.013 deg/frame")

print("ALL QUARTER-SPEED DELIVERABLES COMPLETED!")
