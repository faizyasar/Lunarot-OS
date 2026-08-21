import sys
content = open('index.html', encoding='utf-8').read()
out = open('scratch/search_lunarot.txt', 'w', encoding='utf-8')

idx = 0
while True:
    idx = content.find('LUNAROT_', idx)
    if idx == -1:
        break
    # Extract 30 chars before and 30 chars after
    out.write('Found: ' + content[max(0, idx-30):min(len(content), idx+50)] + '\n')
    idx += 1
out.close()
