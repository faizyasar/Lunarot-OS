import re

with open('lexicon.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Add CSS to stretch the layout
css_stretch = """
<style>
/* Stretch all layout containers to fill the iframe */
#root > div, 
#root > div > div, 
#root main, 
#root section {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 100% !important;
    flex-basis: 100% !important;
}
/* Keep internal flex layouts (like header menu) working but wrap if needed */
#root header, #root nav {
    flex-wrap: wrap !important;
}
/* Ensure the text is readable and not artificially narrowed */
p, h1, h2, h3, h4, h5, h6 {
    max-width: 100% !important;
}
</style>
"""

c = c.replace('</style>', '</style>\n' + css_stretch)

with open('lexicon.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Injected CSS to stretch the layout in lexicon.html')
