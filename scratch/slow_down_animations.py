import os
from PIL import Image

webp_path = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'
gif_path = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.gif'
workspace_gif_path = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\lunarot_tarot_deck_spinning.gif'

im = Image.open(webp_path)
frames = []
for i in range(im.n_frames):
    im.seek(i)
    frames.append(im.convert('RGBA'))

print(f"Loaded {len(frames)} frames from WebP.")

# 33.3ms per frame on 180 frames = 6.0 seconds per revolution (slow, elegant showcase drift)
frames[0].save(
    webp_path,
    save_all=True,
    append_images=frames[1:],
    duration=33,
    loop=0,
    quality=85,
    method=4
)
print(f"Saved slow 6.0s WebP to: {webp_path} ({os.path.getsize(webp_path):,} bytes)")

# Also create the matching slow GIF
gif_frames = []
# sample every 2nd frame (90 frames @ 66ms delay = 6.0s) for compact size and butter smoothness
sampled_frames = frames[::2]
for frame in sampled_frames:
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
    duration=66,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print(f"Saved slow 6.0s GIF to Desktop: {gif_path} ({os.path.getsize(gif_path):,} bytes)")

gif_frames[0].save(
    workspace_gif_path,
    save_all=True,
    append_images=gif_frames[1:],
    duration=66,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
print(f"Saved slow 6.0s GIF to Workspace: {workspace_gif_path} ({os.path.getsize(workspace_gif_path):,} bytes)")
