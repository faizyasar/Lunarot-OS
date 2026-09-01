import json
import re
import os
import base64

transcript_path = r'C:\Users\faizy\.gemini\antigravity-ide\brain\fcc4dae8-da7e-4ef0-8d6d-a4daa9fe4f66\.system_generated\logs\transcript.jsonl'

manifest = {}
if os.path.exists(transcript_path):
    with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find manifest
    matches = re.findall(r'<script type=\\"__bundler/manifest\\">(.*?)</script>', content)
    if not matches:
        matches = re.findall(r'<script type="__bundler/manifest">(.*?)</script>', content)
    
    for m in matches:
        try:
            # unescape if json string
            unescaped = m.replace(r'\"', '"').replace(r'\\/', '/')
            data = json.loads(unescaped)
            for k, v in data.items():
                if "data" in v:
                    manifest[k] = v
        except Exception as e:
            pass

print("Total extracted manifest keys from transcript:", len(manifest))

glb_path = r'C:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\cartridge.glb'
cover_path = r'C:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\cover.webp'

for k, v in manifest.items():
    raw = base64.b64decode(v['data'])
    if raw.startswith(b'glTF'):
        with open(glb_path, 'wb') as f:
            f.write(raw)
        print("Saved GLB:", glb_path, f"({len(raw)} bytes)")
    elif raw.startswith(b'RIFF') and b'WEBP' in raw[:16]:
        with open(cover_path, 'wb') as f:
            f.write(raw)
        print("Saved Cover:", cover_path, f"({len(raw)} bytes)")
