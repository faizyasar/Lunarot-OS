import re
import json

with open(r'C:\Users\faizy\Desktop\Anatomy fixed Casette new.html', 'r', encoding='utf-8') as f:
    html = f.read()

m_template = re.search(r'<script type="__bundler/template">(.*?)</script>', html, re.DOTALL)
m_manifest = re.search(r'<script type="__bundler/manifest">(.*?)</script>', html, re.DOTALL)

if m_template:
    template_str = json.loads(m_template.group(1))
    print('Template length:', len(template_str))
    print('--- TEMPLATE SNIPPET ---')
    print(template_str[:2000])
    with open(r'scratch\unpacked_template.html', 'w', encoding='utf-8') as out:
        out.write(template_str)

if m_manifest:
    manifest_data = json.loads(m_manifest.group(1))
    print('\nManifest keys:')
    for k, v in manifest_data.items():
        print(k, v['mime'], len(v['data']), 'compressed:', v.get('compressed'))
