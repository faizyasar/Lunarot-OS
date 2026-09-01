import json
import base64
import os

path = r'C:\Users\faizy\.gemini\antigravity-ide\brain\fcc4dae8-da7e-4ef0-8d6d-a4daa9fe4f66\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if 'd659b33e' in line:
            obj = json.loads(line)
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
                print('Found raw_text, length:', len(raw_text))
                start = raw_text.find('<script type="__bundler/manifest">')
                print('Start pos:', start)
                if start != -1:
                    print('Snippet after start:', repr(raw_text[start:start+100]))
                    end = raw_text.find('</script>', start)
                    print('End pos:', end)
                    if end != -1:
                        manifest_str = raw_text[start + len('<script type="__bundler/manifest">'):end]
                        print('Manifest snippet:', repr(manifest_str[:150]))
            break
