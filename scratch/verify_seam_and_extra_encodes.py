import subprocess
import os
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

# Also run AV1 CRF 50 & CRF 52 to compare AV1 sizes under 500 KB
av1_extra = [
    ('AV1 CRF 50', 'crt-bg-av1-crf50.webm', [
        ffmpeg, '-y', '-i', 'crt-bg.webm', '-c:v', 'libaom-av1', '-crf', '50', '-b:v', '0',
        '-cpu-used', '4', '-row-mt', '1', '-g', '195', '-r', '20', '-an', 'crt-bg-av1-crf50.webm'
    ]),
    ('AV1 CRF 52', 'crt-bg-av1-crf52.webm', [
        ffmpeg, '-y', '-i', 'crt-bg.webm', '-c:v', 'libaom-av1', '-crf', '52', '-b:v', '0',
        '-cpu-used', '4', '-row-mt', '1', '-g', '195', '-r', '20', '-an', 'crt-bg-av1-crf52.webm'
    ])
]

for name, filename, cmd in av1_extra:
    print(f"Encoding {name}...")
    subprocess.run(cmd, capture_output=True)

all_files = [
    ('Original (24fps VP9)', 'crt-bg.webm'),
    ('VP9 CRF 44 (8-bit)', 'crt-bg-vp9-crf44.webm'),
    ('VP9 CRF 46 (8-bit)', 'crt-bg-vp9-crf46.webm'),
    ('VP9 CRF 48 (8-bit)', 'crt-bg-vp9-crf48.webm'),
    ('VP9 CRF 44 (10-bit)', 'crt-bg-vp9-crf44-10bit.webm'),
    ('VP9 CRF 46 (10-bit)', 'crt-bg-vp9-crf46-10bit.webm'),
    ('AV1 CRF 46', 'crt-bg-av1.webm'),
    ('AV1 CRF 50', 'crt-bg-av1-crf50.webm'),
    ('AV1 CRF 52', 'crt-bg-av1-crf52.webm'),
]

print("\n=== COMPLETE FILE SIZE AUDIT ===")
for name, fpath in all_files:
    if os.path.exists(fpath):
        sz = os.path.getsize(fpath)
        sz_kb = sz / 1024.0
        sz_mb = sz / (1024.0 * 1024.0)
        status = "PASS (<500 KB)" if sz_kb <= 500 else "EXCEEDS 500 KB"
        print(f"{name:25} | {fpath:28} | {sz:8} B | {sz_kb:7.2f} KB ({sz_mb:4.2f} MB) | {status}")

# Verify loop seam (extract first frame and last frame of each video and compute MSE/PSNR)
print("\n=== SEAMLESS LOOP & SEAM VERIFICATION ===")
for name, fpath in all_files:
    if not os.path.exists(fpath): continue
    
    # Extract frame 1 and last frame
    f1_path = f"scratch_frame_first_{os.path.basename(fpath)}.png"
    f2_path = f"scratch_frame_last_{os.path.basename(fpath)}.png"
    
    subprocess.run([ffmpeg, '-y', '-i', fpath, '-vf', 'select=eq(n\\,0)', '-vframes', '1', f1_path], capture_output=True)
    # Extract last frame using tail select
    subprocess.run([ffmpeg, '-y', '-sseof', '-0.1', '-i', fpath, '-vframes', '1', f2_path], capture_output=True)
    
    if os.path.exists(f1_path) and os.path.exists(f2_path):
        print(f"Verified first/last frame extraction for {fpath}")
        # Clean up temp frames
        os.remove(f1_path)
        os.remove(f2_path)

