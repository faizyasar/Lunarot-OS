import sys
import re

content = open('index.html', encoding='utf-8').read()
out = open('scratch/search_spread_cd.txt', 'w', encoding='utf-8')

# Look for postMessage calls
matches = re.finditer(r'postMessage\(\s*\{[^}]*type:\s*[\'"]([^\'"]+)[\'"]', content)
found_types = set([match.group(1) for match in matches])

for m in found_types:
    out.write('Found type: ' + m + '\n')
out.close()
