import re

with open('C:/Users/faizy/Downloads/standalone (1).html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Hide the SVG tree completely
# 2. Hide the text Cosmology & Physiology
# 3. Stretch layout
# 4. Auto-click Encyclopedia
css_and_script = """
<style>
svg { display: none !important; }
h2, h3 { opacity: 0 !important; }

/* Fix sandwiched layout */
#root > div > div:first-child,
#root main,
#root section {
    max-width: 100% !important;
    width: 100% !important;
    flex-grow: 1 !important;
}
#root > div {
    display: flex !important;
    justify-content: flex-end !important;
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

print('Cleanly rebuilt lexicon.html')
