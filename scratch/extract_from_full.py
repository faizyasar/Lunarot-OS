import json
import re
import base64
import os

path = r'C:\Users\faizy\.gemini\antigravity-ide\brain\fcc4dae8-da7e-4ef0-8d6d-a4daa9fe4f66\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if 'd659b33e' in line:
            print('Found on line', idx)
            # find all data fields
            pattern_glb = r'd659b33e-6421-45a9-b407-c0115e669e90.*?\"data\":\"(.*?)\"'
            m1 = re.search(pattern_glb, line)
            if m1:
                b64 = m1.group(1).replace(r'\/', '/').replace(r'\\', '')
                with open('scratch/cartridge.glb', 'wb') as out_f:
                    out_f.write(base64.b64decode(b64))
                print('Saved cartridge.glb:', os.path.getsize('scratch/cartridge.glb'), 'bytes')
            
            pattern_cover = r'83e7c9f1-ccb0-4760-9f89-6d3400734e60.*?\"data\":\"(.*?)\"'
            m2 = re.search(pattern_cover, line)
            if m2:
                b64_c = m2.group(1).replace(r'\/', '/').replace(r'\\', '')
                with open('scratch/cover.webp', 'wb') as out_f:
                    out_f.write(base64.b64decode(b64_c))
                print('Saved cover.webp:', os.path.getsize('scratch/cover.webp'), 'bytes')
