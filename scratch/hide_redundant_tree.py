import re

with open('lexicon.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the failed auto-click scripts
c = re.sub(r'<script>\s*window\.addEventListener.*?<\/script>', '', c, flags=re.DOTALL)

# Inject CSS to hide the 2D tree diagram wrapper
css_injection = """
<style>
/* Hide the redundant 2D tree diagram because the 3D skeleton covers this */
.justify-between.overflow-hidden.pt-4 {
    display: none !important;
}
</style>
"""

c = c.replace('</head>', css_injection + '\n</head>')

with open('lexicon.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Injected CSS to hide the redundant tree diagram.')
