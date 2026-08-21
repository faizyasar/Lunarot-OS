import re

old_content = open('index.html', encoding='utf-8').read()
new_content = open('C:\\Users\\faizy\\Downloads\\Lunarot-OS-v6.8-Standalone-mobile-login (1).html', encoding='utf-8').read()

# CSS replacement
def get_css(content):
    matches = list(re.finditer(r'@media\(max-width:768px\)\{.*?(?=\")', content))
    for m in matches:
        if '.panel-left' in m.group(0):
            return m.group(0)
    return None

old_css = get_css(old_content)
new_css = get_css(new_content)

if old_css and new_css:
    old_content = old_content.replace(old_css, new_css)
    print(f'CSS replaced: old={len(old_css)} new={len(new_css)}')
else:
    print('Failed to find CSS!')

# JS replacement
def get_js(content, marker):
    idx = content.find(marker)
    if idx == -1: return None
    start = content.rfind('<script>', 0, idx)
    end = content.find('</script>', idx) + 9
    return content[start:end]

old_js = get_js(old_content, 'function applyX(track, x, animate){')
new_js = get_js(new_content, 'function syncFormPopups')

if old_js and new_js:
    old_content = old_content.replace(old_js, new_js)
    print(f'JS replaced: old={len(old_js)} new={len(new_js)}')
else:
    print('Failed to find JS!')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(old_content)
print('Done!')
