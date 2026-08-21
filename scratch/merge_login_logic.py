import sys
import re

old_content = open('index.html', encoding='utf-8').read()
new_content = open('C:\\Users\\faizy\\Downloads\\Lunarot-OS-v6.8-Standalone-mobile-login (1).html', encoding='utf-8').read()

# The CSS block inside the minified string
old_css_matches = list(re.finditer(r'@media\(max-width:768px\)\{.*?(?=\")', old_content))
if old_css_matches:
    old_css_str = old_css_matches[-1].group(0)  # We expect it to be near the end of the template string
    print('Found old CSS:', len(old_css_str), 'chars')
else:
    print('Old CSS not found')
    old_css_str = None

new_css_matches = list(re.finditer(r'@media\(max-width:768px\)\{.*?(?=\")', new_content))
if new_css_matches:
    new_css_str = new_css_matches[-1].group(0)
    print('Found new CSS:', len(new_css_str), 'chars')
else:
    print('New CSS not found')
    new_css_str = None

if old_css_str and new_css_str:
    old_content = old_content.replace(old_css_str, new_css_str)
    print('CSS replaced')

# The JS block
# Find the start of the JS which we know begins with document.addEventListener('DOMContentLoaded', async function() {
old_js_start = old_content.find("document.addEventListener('DOMContentLoaded', async function() {")
old_js_end = old_content.find("</script>", old_js_start)

if old_js_start != -1 and old_js_end != -1:
    old_js_str = old_content[old_js_start:old_js_end].strip()
    print('Found old JS:', len(old_js_str), 'chars')
else:
    print('Old JS not found')
    old_js_str = None

new_js_start = new_content.find("document.addEventListener('DOMContentLoaded', async function() {")
new_js_end = new_content.find("</script>", new_js_start)

if new_js_start != -1 and new_js_end != -1:
    new_js_str = new_content[new_js_start:new_js_end].strip()
    print('Found new JS:', len(new_js_str), 'chars')
else:
    print('New JS not found')
    new_js_str = None

if old_js_str and new_js_str:
    old_content = old_content.replace(old_js_str, new_js_str)
    print('JS replaced')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(old_content)
print('Replacement complete!')
