import re
with open('golem.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find camera-ui and append display:none
c = re.sub(r'(<div id="camera-ui" style="[^"]*)(")', r'\1; display: none !important;\2', c)

# update iframe in golem.html to give it more width so it's not sandwiched, or maybe right-align it better
# it's currently width:40%. Let's make it width:45% and right:0.
c = re.sub(r'width:40%;', 'width:45%; right:0;', c)

with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated golem.html: Hid camera UI and adjusted iframe.')
