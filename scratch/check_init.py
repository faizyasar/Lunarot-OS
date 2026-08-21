import re
with open('golem.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's find where 'full' is set as default.
matches = re.finditer(r'focusPreset\([\'"](.*?)[\'"]\)', c)
for m in matches:
    print('focusPreset call:', m.group(0))

print("\n--- Looking for initialization ---")
matches2 = re.finditer(r'window\..*?=', c)
for m in matches2:
    if 'full' in c[m.start():m.end()+30]:
        print('Init:', c[m.start():m.end()+30])

matches3 = re.finditer(r'function init.*?\n(.*?\{.*?\})', c, re.DOTALL)
for m in matches3:
    print('init function found')
