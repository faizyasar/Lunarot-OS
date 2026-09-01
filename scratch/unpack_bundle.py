import json
import base64
import os
import re

with open(r'C:\Users\faizy\Downloads\Cassette Player Anatomy.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

m = re.search(r'<script type="__bundler/manifest">(.*?)</script>', html, re.DOTALL)
if m:
    manifest = json.loads(m.group(1).strip())
    print('Manifest keys:', len(manifest))
    os.makedirs('scratch/cassette_assets', exist_ok=True)
    for k, v in manifest.items():
        name = v.get('name') or k
        mime = v.get('type') or ''
        data_len = len(v.get('data', ''))
        print(f'{k}: name={name}, type={mime}, size={data_len}')
        if 'data' in v:
            with open(os.path.join('scratch/cassette_assets', name), 'wb') as f_out:
                f_out.write(base64.b64decode(v['data']))

t = re.search(r'<script type="__bundler/template">(.*?)</script>', html, re.DOTALL)
if t:
    template_content = t.group(1)
    print('Template length:', len(template_content))
    with open('scratch/cassette_template.html', 'w', encoding='utf-8') as f_out:
        f_out.write(template_content)

scripts = re.findall(r'<script(?:\s+type="([^"]*)")?>(.*?)</script>', html, re.DOTALL)
print('All scripts count:', len(scripts))
for idx, (stype, sbody) in enumerate(scripts):
    print(f'Script {idx}: type={stype}, len={len(sbody)}')
