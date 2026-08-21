import re

with open('golem.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all script tags
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)

with open('scratch/test_js.js', 'w', encoding='utf-8') as f:
    for s in scripts:
        f.write(s)
        f.write('\n\n')
