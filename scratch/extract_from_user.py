import json
import base64
import os
import re

path = r'C:\Users\faizy\.gemini\antigravity-ide\brain\fcc4dae8-da7e-4ef0-8d6d-a4daa9fe4f66\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if line.startswith('{"content":') or '"type":"USER_INPUT"' in line:
            if 'd659b33e' in line:
                obj = json.loads(line)
                text = obj.get('content', '')
                if isinstance(text, str):
                    m = re.search(r'<script type="__bundler/manifest">\s*(\{.*?\})\s*</script>', text, re.DOTALL)
                    if m:
                        manifest = json.loads(m.group(1))
                        b64 = manifest['d659b33e-6421-45a9-b407-c0115e669e90']['data']
                        with open('scratch/cartridge.glb', 'wb') as f_out:
                            f_out.write(base64.b64decode(b64))
                        print('Successfully extracted cartridge.glb:', len(b64))

                        b64_c = manifest['83e7c9f1-ccb0-4760-9f89-6d3400734e60']['data']
                        with open('scratch/cover.webp', 'wb') as f_out:
                            f_out.write(base64.b64decode(b64_c))
                        print('Successfully extracted cover.webp:', len(b64_c))
                        break
