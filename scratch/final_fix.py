import re

# 1. Fix golem.html (hide camera-telemetry)
with open('golem.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<div id="camera-telemetry" style="', '<div id="camera-telemetry" style="display:none !important; ')

# 2. Make iframe width 50% so there's plenty of space
c = re.sub(r'<iframe id="full-lexicon-iframe".*?>', '<iframe id="full-lexicon-iframe" src="lexicon.html" style="position: fixed; right: 0; top: 0; width: 50%; height: 100%; border: none; display: none; z-index: 4;"></iframe>', c)

with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(c)
    
# 3. Fix lexicon.html (remove the weird stretch CSS, and just make the column full width properly)
with open('lexicon.html', 'r', encoding='utf-8') as f:
    lx = f.read()

# I had injected <style>...</style> at the bottom.
lx = re.sub(r'<style>.*?Stretch all layout.*?<\/style>', '', lx, flags=re.DOTALL)

# Let's add a clean one
clean_css = """
<style>
/* Fix sandwiched layout */
#root > div > div:first-child,
#root main,
#root section {
    max-width: 100% !important;
    width: 100% !important;
    flex-grow: 1 !important;
}
/* If the whole thing is in a container, make it align to the right side of the iframe */
#root > div {
    display: flex !important;
    justify-content: flex-end !important;
}
</style>
"""
lx = lx.replace('</style>', '</style>\n' + clean_css)

with open('lexicon.html', 'w', encoding='utf-8') as f:
    f.write(lx)
