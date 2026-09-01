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

# Let's test optimizing:
# 1. 720 frames @ 340x340 with quality=65, method=6, duration=160ms (115.2s)
frames_720 = all_frames[::2]
frames_720_resized = [f.resize((340, 340), Image.Resampling.LANCZOS) for f in frames_720]

test1_path = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\test_opt_720.webp'
frames_720_resized[0].save(
    test1_path,
    save_all=True,
    append_images=frames_720_resized[1:],
    duration=160,
    loop=0,
    quality=65,
    method=6
)
print("Test 1 (720 frames, 340x340, Q65):", os.path.getsize(test1_path), "bytes")

# 2. 720 frames @ 360x360 with quality=58, method=6, duration=160ms (115.2s)
frames_720_360 = [f.resize((360, 360), Image.Resampling.LANCZOS) for f in frames_720]
test2_path = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\test_opt_720_360.webp'
frames_720_360[0].save(
    test2_path,
    save_all=True,
    append_images=frames_720_360[1:],
    duration=160,
    loop=0,
    quality=55,
    method=6
)
print("Test 2 (720 frames, 360x360, Q55):", os.path.getsize(test2_path), "bytes")

# 3. 1440 frames @ 300x300 with quality=50, method=6, duration=80ms (115.2s)
frames_1440_300 = [f.resize((300, 300), Image.Resampling.LANCZOS) for f in all_frames]
test3_path = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\test_opt_1440_300.webp'
frames_1440_300[0].save(
    test3_path,
    save_all=True,
    append_images=frames_1440_300[1:],
    duration=80,
    loop=0,
    quality=50,
    method=6
)
print("Test 3 (1440 frames, 300x300, Q50):", os.path.getsize(test3_path), "bytes")
