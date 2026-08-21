import re
with open('golem.html', 'r', encoding='utf-8') as f:
    c = f.read()

# search for literally \n in a javascript string
matches = re.finditer(r'[\'\"].*?\\n.*?[\'\"]', c)
for m in matches:
    print('Found JS string with \\n:', m.group(0))
