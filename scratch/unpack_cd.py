import json
import re
import gzip
import base64

with open(r'C:\Users\faizy\Desktop\HTMLS\CD Jewel Case.html', 'r', encoding='utf-8') as f:
    content = f.read()

manifest_m = re.search(r'<script type="__bundler/manifest">(.*?)</script>', content, re.DOTALL)
template_m = re.search(r'<script type="__bundler/template">(.*?)</script>', content, re.DOTALL)

if manifest_m:
    manifest = json.loads(manifest_m.group(1))
    print('Manifest entries:', len(manifest))
    for k, v in manifest.items():
        print(f"UUID: {k}, MIME: {v.get('mime')}, compressed: {v.get('compressed')}, data len: {len(v.get('data', ''))}")
        # Decode and save assets if any
        raw_bytes = base64.b64decode(v['data'])
        if v.get('compressed'):
            raw_bytes = gzip.decompress(raw_bytes)
        print(f"  -> unpacked bytes: {len(raw_bytes)}")
        if 'image' in v.get('mime', ''):
            with open(f"scratch/asset_{k[:8]}.png", "wb") as img_f:
                img_f.write(raw_bytes)
            print(f"  -> saved image asset to scratch/asset_{k[:8]}.png")

if template_m:
    template = json.loads(template_m.group(1))
    print("\nTemplate length:", len(template))
    with open("scratch/unpacked_template.html", "w", encoding="utf-8") as tf:
        tf.write(template)
    print("Saved unpacked template to scratch/unpacked_template.html")
