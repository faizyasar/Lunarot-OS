import json
import base64
import os

with open(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Partition by manifest
start_str = 'type="__bundler/manifest">'
p1 = text.find(start_str)
if p1 != -1:
    p2 = text.find('</script>', p1)
    manifest_str = text[p1 + len(start_str):p2].strip()
    manifest = json.loads(manifest_str)
    print("Manifest found! Keys count:", len(manifest))
    for k, v in manifest.items():
        data = v.get('data', '')
        raw = base64.b64decode(data)
        if raw.startswith(b'glTF'):
            with open('scratch/cartridge.glb', 'wb') as f_out:
                f_out.write(raw)
            print('Extracted scratch/cartridge.glb:', len(raw), 'bytes')
        elif raw.startswith(b'RIFF') and b'WEBP' in raw[:16]:
            with open('scratch/cover.webp', 'wb') as f_out:
                f_out.write(raw)
            print('Extracted scratch/cover.webp:', len(raw), 'bytes')
else:
    print("start_str not found in golem.html")
