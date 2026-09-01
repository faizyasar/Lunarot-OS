import json
import re
import os
import base64

with open(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem.html', 'r', encoding='utf-8') as f:
    text = f.read()

tags = re.findall(r'<script[^>]*type="([^"]*)"[^>]*>(.*?)</script>', text, re.DOTALL)
if not tags:
    tags = re.findall(r'<script([^>]*)>(.*?)</script>', text, re.DOTALL)

for t in tags:
    attr, body = t[0], t[1]
    if '__bundler/manifest' in attr or 'd659b33e' in body:
        data = json.loads(body.strip())
        for k, v in data.items():
            raw = base64.b64decode(v['data'])
            if raw.startswith(b'glTF'):
                with open('scratch/cartridge.glb', 'wb') as f_out:
                    f_out.write(raw)
                print('Extracted scratch/cartridge.glb:', len(raw), 'bytes')
            elif raw.startswith(b'RIFF') and b'WEBP' in raw[:16]:
                with open('scratch/cover.webp', 'wb') as f_out:
                    f_out.write(raw)
                print('Extracted scratch/cover.webp:', len(raw), 'bytes')
