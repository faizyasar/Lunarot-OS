import json
import re

with open(r'C:\Users\faizy\Downloads\Cassette Player Anatomy.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for m in re.finditer(r'<script(?:\s+type="([^"]*)")?>(.*?)</script>', text, re.DOTALL):
    stype, body = m.group(1), m.group(2)
    if stype == '__bundler/ext_resources':
        print('ext_resources:', body.strip())
    elif stype == '__bundler/manifest':
        man = json.loads(body.strip())
        for k, v in man.items():
            print(k, ':', v.get('name'), v.get('type'))
