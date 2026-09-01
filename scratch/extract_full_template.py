import json

with open(r'C:\Users\faizy\Desktop\Anatomy fixed Casette new.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<script type="__bundler/template">\n'
idx = html.find(start_marker) + len(start_marker)

decoder = json.JSONDecoder()
template_str, _ = decoder.raw_decode(html, idx)

print("Full template length:", len(template_str))

with open(r'scratch\full_unpacked_template.html', 'w', encoding='utf-8') as out:
    out.write(template_str)

print("Successfully written scratch\\full_unpacked_template.html!")
