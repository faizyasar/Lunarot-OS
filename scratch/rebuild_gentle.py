import re

with open('C:/Users/faizy/Downloads/standalone (1).html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Hide the SVG tree completely
# 2. Hide the text Cosmology & Physiology
# 3. Clean flex expansion
# 4. Auto-click Encyclopedia
css_and_script = """
<style>
/* Hide the redundant 2D tree diagram */
svg { display: none !important; }
h2, h3 { opacity: 0 !important; } /* Specifically for Cosmology & Physiology */

/* The main layout is likely a flex row. We hid the right child (SVG). 
   Let's let the left child expand naturally without forcing hard widths on internals. */
#root > div > div:first-child {
    flex: 1 1 auto !important;
    max-width: none !important;
    padding-right: 40px !important;
}
/* Ensure text can breathe */
#root p {
    max-width: 600px !important;
}
</style>
<script>
window.addEventListener('load', () => {
    setInterval(() => {
        const tabs = document.querySelectorAll('span, button, a, div, p, li');
        for (let tab of tabs) {
            if (tab.textContent.trim().toUpperCase() === 'ENCYCLOPEDIA' && !tab.dataset.clicked) {
                tab.dataset.clicked = "true";
                tab.click();
                if(tab.parentElement) tab.parentElement.click();
            }
        }
    }, 250);
});
</script>
</head>
"""

c = c.replace('</head>', css_and_script)

with open('lexicon.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Rebuilt lexicon.html with gentle flex CSS.')
