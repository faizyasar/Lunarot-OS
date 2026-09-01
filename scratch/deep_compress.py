import os
from PIL import Image

gif_src = r'C:\Users\faizy\Desktop\cd_jewel_case_spinning.gif'
webp_src = r'C:\Users\faizy\Desktop\cd_jewel_case_spinning.webp'

print("Loading frames for deep compression...")
im = Image.open(webp_src)
frames = []
try:
    while True:
        # Convert each frame to RGBA
        frame = im.convert('RGBA')
        frames.append(frame)
        im.seek(len(frames))
except EOFError:
    pass

print(f"Loaded {len(frames)} frames.")

# 1. Resize to a crisp 380x380 (ideal size for avatars, web embeds, and lightweight asset loading)
target_size = (380, 380)
resized_frames = [f.resize(target_size, Image.Resampling.LANCZOS) for f in frames]

# --- 2. High-Compression Transparent WebP ---
# WebP with quality=80 and method=6 creates tiny files with pristine alpha
output_webp = r'C:\Users\faizy\Desktop\cd_jewel_case_spinning.webp'
resized_frames[0].save(
    output_webp,
    save_all=True,
    append_images=resized_frames[1:],
    duration=20,
    loop=0,
    quality=80,
    method=6
)
webp_size_kb = os.path.getsize(output_webp) / 1024
print(f"Compressed WebP: {webp_size_kb:.1f} KB -> {output_webp}")

# --- 3. High-Compression Transparent GIF ---
# Quantize to 128 colors for maximum LZW compression ratio
gif_frames = []
for f in resized_frames:
    alpha = f.split()[3]
    mask = Image.eval(alpha, lambda a: 255 if a <= 15 else 0)
    
    # 128 colors for high compression
    p_frame = f.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=128)
    p_frame.paste(255, mask)
    p_frame.info['transparency'] = 255
    gif_frames.append(p_frame)

output_gif = r'C:\Users\faizy\Desktop\cd_jewel_case_spinning.gif'
gif_frames[0].save(
    output_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=20,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
gif_size_mb = os.path.getsize(output_gif) / (1024 * 1024)
print(f"Compressed GIF: {gif_size_mb:.2f} MB -> {output_gif}")

# Also update workspace copy
workspace_gif = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\cd_jewel_case_spinning.gif'
gif_frames[0].save(
    workspace_gif,
    save_all=True,
    append_images=gif_frames[1:],
    duration=20,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=True
)
