import re

with open('golem.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change .sephirah-marker to be a relative flex item instead of absolute
# We will use regex to find the .sephirah-marker block and modify it

def modify_marker_css(match):
    block = match.group(0)
    block = block.replace('position: absolute;', 'position: relative;')
    block = block.replace('transform: translate(-50%, -50%);', 'transform: none;')
    block = block.replace('align-items: center;', 'align-items: flex-end;')
    block = block.replace('text-align: center;', 'text-align: right;')
    return block

content = re.sub(r'\.sephirah-marker \{.*?\}', modify_marker_css, content, flags=re.DOTALL)

with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("sephirah-marker CSS updated to relative")
