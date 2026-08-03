import subprocess
import os
import time
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

encodes = [
    ('VP9 CRF 44 (8-bit)', 'crt-bg-vp9-crf44.webm', [
        ffmpeg, '-y', '-i', 'crt-bg.webm', '-c:v', 'libvpx-vp9', '-crf', '44', '-b:v', '0',
        '-row-mt', '1', '-tile-columns', '2', '-g', '195', '-auto-alt-ref', '1',
        '-lag-in-frames', '25', '-r', '20', '-an', 'crt-bg-vp9-crf44.webm'
    ]),
    ('VP9 CRF 46 (8-bit)', 'crt-bg-vp9-crf46.webm', [
        ffmpeg, '-y', '-i', 'crt-bg.webm', '-c:v', 'libvpx-vp9', '-crf', '46', '-b:v', '0',
        '-row-mt', '1', '-tile-columns', '2', '-g', '195', '-auto-alt-ref', '1',
        '-lag-in-frames', '25', '-r', '20', '-an', 'crt-bg-vp9-crf46.webm'
    ]),
    ('VP9 CRF 48 (8-bit)', 'crt-bg-vp9-crf48.webm', [
        ffmpeg, '-y', '-i', 'crt-bg.webm', '-c:v', 'libvpx-vp9', '-crf', '48', '-b:v', '0',
        '-row-mt', '1', '-tile-columns', '2', '-g', '195', '-auto-alt-ref', '1',
        '-lag-in-frames', '25', '-r', '20', '-an', 'crt-bg-vp9-crf48.webm'
    ]),
    ('VP9 CRF 44 (10-bit yuv420p10le)', 'crt-bg-vp9-crf44-10bit.webm', [
        ffmpeg, '-y', '-i', 'crt-bg.webm', '-c:v', 'libvpx-vp9', '-crf', '44', '-b:v', '0',
        '-pix_fmt', 'yuv420p10le', '-row-mt', '1', '-tile-columns', '2', '-g', '195', '-auto-alt-ref', '1',
        '-lag-in-frames', '25', '-r', '20', '-an', 'crt-bg-vp9-crf44-10bit.webm'
    ]),
    ('VP9 CRF 46 (10-bit yuv420p10le)', 'crt-bg-vp9-crf46-10bit.webm', [
        ffmpeg, '-y', '-i', 'crt-bg.webm', '-c:v', 'libvpx-vp9', '-crf', '46', '-b:v', '0',
        '-pix_fmt', 'yuv420p10le', '-row-mt', '1', '-tile-columns', '2', '-g', '195', '-auto-alt-ref', '1',
        '-lag-in-frames', '25', '-r', '20', '-an', 'crt-bg-vp9-crf46-10bit.webm'
    ]),
    ('AV1 CRF 46 (8-bit)', 'crt-bg-av1.webm', [
        ffmpeg, '-y', '-i', 'crt-bg.webm', '-c:v', 'libaom-av1', '-crf', '46', '-b:v', '0',
        '-cpu-used', '4', '-row-mt', '1', '-g', '195', '-r', '20', '-an', 'crt-bg-av1.webm'
    ])
]

results = []

for name, filename, cmd in encodes:
    print(f"Starting {name}...")
    t0 = time.time()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    t1 = time.time()
    if proc.returncode == 0 and os.path.exists(filename):
        size_bytes = os.path.getsize(filename)
        size_kb = size_bytes / 1024
        print(f"  DONE in {t1-t0:.2f}s -> {filename}: {size_bytes} bytes ({size_kb:.2f} KB)")
        results.append({
            'name': name,
            'filename': filename,
            'size_bytes': size_bytes,
            'size_kb': size_kb,
            'time_sec': t1-t0,
            'success': True
        })
    else:
        print(f"  FAILED ({name}): {proc.stderr[:200]}")
        results.append({
            'name': name,
            'filename': filename,
            'error': proc.stderr,
            'success': False
        })

print("\n=== ENCODING SUMMARY ===")
for r in results:
    if r['success']:
        print(f"{r['name']:35} | {r['filename']:28} | {r['size_bytes']:8} bytes | {r['size_kb']:7.2f} KB | {r['time_sec']:.1f}s")
    else:
        print(f"{r['name']:35} | FAILED: {r['error'][:60]}")
