import os
from PIL import Image

webp_path = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'
gif_path = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.gif'
workspace_gif_path = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\lunarot_tarot_deck_spinning.gif'

im = Image.open(webp_path)
print(f"Loaded WebP with {im.n_frames} frames.")

frames = []
for i in range(im.n_frames):
    im.seek(i)
    frames.append(im.convert('RGBA'))

print(f"Extracted {len(frames)} frames.")

# Halve the speed: duration = 40ms (25fps playback of 720 sub-degree frames = 28.80 seconds per revolution)
frames[0].save(
    webp_path,
    save_all=True,
    append_images=frames[1:],
    duration=40,
    loop=0,
    quality=85,
    method=4
)
print(f"Saved Half-Speed WebP (28.8s loop): {webp_path} ({os.path.getsize(webp_path):,} bytes)")

# Update GIF to matching half speed (80ms per frame x 360 frames = 28.80s loop)
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
    duration=80,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print(f"Saved Half-Speed GIF to Desktop: {gif_path} ({os.path.getsize(gif_path):,} bytes)")

gif_frames[0].save(
    workspace_gif_path,
    save_all=True,
    append_images=gif_frames[1:],
    duration=80,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print(f"Saved Half-Speed GIF to Workspace: {workspace_gif_path} ({os.path.getsize(workspace_gif_path):,} bytes)")

# Update Desktop HTML live spin speed to half-speed (0.0525 deg/frame)
desktop_html_path = r'C:\Users\faizy\Desktop\HTMLS\Lunarot Tarot Deck (Spinning Transparent).html'
if os.path.exists(desktop_html_path):
    with open(desktop_html_path, 'r', encoding='utf-8') as f:
        dhtml = f.read()
    dhtml = dhtml.replace('currentY = (currentY + 0.105) % 360;', 'currentY = (currentY + 0.0525) % 360;')
    with open(desktop_html_path, 'w', encoding='utf-8') as f:
        f.write(dhtml)
    print("Updated Desktop HTML live spin speed to 0.0525 deg/frame")

print("ALL HALF-SPEED UPDATES APPLIED!")
