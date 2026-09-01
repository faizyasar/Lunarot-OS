import json
import base64
import os

path = r'C:\Users\faizy\.gemini\antigravity-ide\brain\fcc4dae8-da7e-4ef0-8d6d-a4daa9fe4f66\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if 'd659b33e' in line:
            obj = json.loads(line)
            # Recursively find text
            def search_text(o):
                if isinstance(o, str):
                    if 'd659b33e-6421-45a9-b407-c0115e669e90' in o:
                        return o
                elif isinstance(o, dict):
                    for v in o.values():
                        res = search_text(v)
                        if res: return res
                elif isinstance(o, list):
                    for item in o:
                        res = search_text(item)
                        if res: return res
                return None
            
            raw_text = search_text(obj)
            if raw_text:
                start = raw_text.find('<script type="__bundler/manifest">')
                end = raw_text.find('</script>', start)
                if start != -1 and end != -1:
                    manifest_str = raw_text[start + len('<script type="__bundler/manifest">'):end].strip()
                    manifest = json.loads(manifest_str)
                    if 'd659b33e-6421-45a9-b407-c0115e669e90' in manifest:
                        b64 = manifest['d659b33e-6421-45a9-b407-c0115e669e90']['data']
                        with open('scratch/cartridge.glb', 'wb') as f_out:
                            f_out.write(base64.b64decode(b64))
                        print('Successfully extracted cartridge.glb:', os.path.getsize('scratch/cartridge.glb'), 'bytes')
                    
                    if '83e7c9f1-ccb0-4760-9f89-6d3400734e60' in manifest:
                        b64_c = manifest['83e7c9f1-ccb0-4760-9f89-6d3400734e60']['data']
                        with open('scratch/cover.webp', 'wb') as f_out:
                            f_out.write(base64.b64decode(b64_c))
                        print('Successfully extracted cover.webp:', os.path.getsize('scratch/cover.webp'), 'bytes')
                    break
