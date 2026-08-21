import re
with open('golem.html', 'r', encoding='utf-8') as f:
    c = f.read()

match2 = re.search(r'COPY DATA', c, re.IGNORECASE)
if match2:
    idx = match2.start()
    with open('scratch/camera_ui_context.txt', 'w', encoding='utf-8') as out:
        out.write(c[max(0, idx-1500):min(len(c), idx+1500)])
