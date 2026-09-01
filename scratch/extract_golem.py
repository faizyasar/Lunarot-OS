import json
import re
import os
import base64

with open(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length of golem.html:', len(text))
m = re.search(r'<script type="__bundler/manifest">(.*?)</script>', text, re.DOTALL)
if m:
    manifest = json.loads(m.group(1))
    print('Manifest keys:', len(manifest))
    for k, v in manifest.items():
        print(' -', k, v.get('mime'))
        data = v.get('data', '')
        raw = base64.b64decode(data)
        if raw.startswith(b'glTF'):
            with open('scratch/cartridge.glb', 'wb') as f_out:
                f_out.write(raw)
            print('Saved scratch/cartridge.glb:', len(raw), 'bytes')
        elif raw.startswith(b'RIFF') and b'WEBP' in raw[:16]:
            with open('scratch/cover.webp', 'wb') as f_out:
                f_out.write(raw)
            print('Saved scratch/cover.webp:', len(raw), 'bytes')
