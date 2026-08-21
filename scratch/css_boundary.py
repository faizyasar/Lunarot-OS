import sys

content = open('index.html', encoding='utf-8').read()
idx = content.find('.panel-left')
print('Found .panel-left at', idx)

for char in ['"', "'", '`', '<']:
    end_idx = content.find(char, idx)
    if end_idx != -1:
        print(f"Found {repr(char)} at {end_idx}, content around it: {repr(content[end_idx-20:end_idx+20])}")
