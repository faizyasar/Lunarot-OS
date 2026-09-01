import json
import re

with open(r'C:\Users\faizy\Desktop\HTMLS\Astral Pachinko - Cartridge, Case & Magazine.html', 'r', encoding='utf-8') as f:
    text = f.read()

manifest_m = re.search(r'<script type="__bundler/manifest">(.*?)</script>', text, re.DOTALL)
template_m = re.search(r'<script type="__bundler/template">(.*?)</script>', text, re.DOTALL)

if manifest_m:
    manifest = json.loads(manifest_m.group(1))
    print('Manifest keys count:', len(manifest))
    for k, v in manifest.items():
        print(' -', k, v.get('mime'), 'len:', len(v.get('data','')))

if template_m:
    template = json.loads(template_m.group(1))
    print('Template length:', len(template))
    with open('scratch/astral_template.html', 'w', encoding='utf-8') as tf:
        tf.write(template)
    print('Saved template preview')
