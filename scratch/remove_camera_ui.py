import re

with open('golem.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's completely remove the camera UI div
idx = c.find('id="camera-ui"')
if idx != -1:
    # search backwards for <div
    start_idx = c.rfind('<div', 0, idx)
    
    # now search forwards for COPY DATA
    copy_idx = c.find('COPY DATA', idx)
    end_div = c.find('</div>', copy_idx) + 6
    
    # Check if we found the whole block
    if start_idx != -1 and copy_idx != -1 and end_div != -1:
        # replace with display none
        c = c[:start_idx] + '<div id="camera-ui" style="display:none !important;"></div>' + c[end_div:]
        print('Successfully replaced camera UI')
        
with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(c)
