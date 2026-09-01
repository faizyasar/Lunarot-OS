import os
from PIL import Image

webp_path = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'
gif_path = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.gif'
workspace_gif_path = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\lunarot_tarot_deck_spinning.gif'

im = Image.open(webp_path)
print(f"Loaded {im.n_frames} frames from WebP.")

frames = []
for i in range(im.n_frames):
    im.seek(i)
    frames.append(im.convert('RGBA'))

print(f"Extracted {len(frames)} frames.")

# A quarter of the previous speed (4x slower: 160ms per frame x 720 frames = 115.2s ultra-slow museum showcase rotation)
frames[0].save(
    webp_path,
    save_all=True,
    append_images=frames[1:],
    duration=160,
    loop=0,
    quality=85,
    method=4
)
print(f"Saved Quarter-Speed WebP (115.2s loop): {webp_path} ({os.path.getsize(webp_path):,} bytes)")

# Update GIF to matching quarter speed (320ms per frame x 360 frames = 115.2s loop)
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
    gif_path,
    save_all=True,
    append_images=gif_frames[1:],
    duration=320,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print(f"Saved Quarter-Speed GIF to Desktop: {gif_path} ({os.path.getsize(gif_path):,} bytes)")

gif_frames[0].save(
    workspace_gif_path,
    save_all=True,
    append_images=gif_frames[1:],
    duration=320,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print(f"Saved Quarter-Speed GIF to Workspace: {workspace_gif_path} ({os.path.getsize(workspace_gif_path):,} bytes)")

# Update Desktop HTML live spin speed to quarter-speed (0.013 deg/frame)
desktop_html_path = r'C:\Users\faizy\Desktop\HTMLS\Lunarot Tarot Deck (Spinning Transparent).html'
if os.path.exists(desktop_html_path):
    with open(desktop_html_path, 'r', encoding='utf-8') as f:
        dhtml = f.read()
    dhtml = dhtml.replace('currentY = (currentY + 0.0525) % 360;', 'currentY = (currentY + 0.013) % 360;')
    dhtml = dhtml.replace('currentY = (currentY + 0.105) % 360;', 'currentY = (currentY + 0.013) % 360;')
    with open(desktop_html_path, 'w', encoding='utf-8') as f:
        f.write(dhtml)
    print("Updated Desktop HTML live spin speed to ultra-slow 0.013 deg/frame")

print("QUARTER SPEED APPLIED SUCCESSFULLY!")
