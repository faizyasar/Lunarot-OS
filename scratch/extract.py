import sys
content = open('index.html', encoding='utf-8').read()
idx = content.find('<script type="__bundler/manifest">')
if idx != -1:
    end_idx = content.find('</script>', idx)
    manifest_str = content[idx+34:end_idx]
    with open('scratch/manifest.json', 'w', encoding='utf-8') as f:
        f.write(manifest_str)
