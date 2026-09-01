import re
import json
import base64
import gzip
import os

os.makedirs(r'scratch\assets', exist_ok=True)

with open(r'C:\Users\faizy\Desktop\Anatomy fixed Casette new.html', 'r', encoding='utf-8') as f:
    html = f.read()

m_manifest = re.search(r'<script type="__bundler/manifest">(.*?)</script>', html, re.DOTALL)

if m_manifest:
    manifest_data = json.loads(m_manifest.group(1))
    print(f"Extracting {len(manifest_data)} assets...")
    for uuid, entry in manifest_data.items():
        data = base64.b64decode(entry['data'])
        if entry.get('compressed'):
            data = gzip.decompress(data)
        ext = 'bin'
        mime = entry.get('mime', '')
        if 'webp' in mime: ext = 'webp'
        elif 'png' in mime: ext = 'png'
        elif 'jpeg' in mime or 'jpg' in mime: ext = 'jpg'
        elif 'font' in mime or 'woff2' in mime: ext = 'woff2'
        
        filepath = os.path.join(r'scratch\assets', f"{uuid}.{ext}")
        with open(filepath, 'wb') as out:
            out.write(data)
        print(f"Saved {filepath} ({len(data)} bytes, mime={mime})")
