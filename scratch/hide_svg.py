import re

# start clean
with open('C:/Users/faizy/Downloads/standalone (1).html', 'r', encoding='utf-8') as f:
    c = f.read()

css_injection = """
<style>
/* Hide the SVG tree completely */
svg {
    display: none !important;
}
/* Hide the text Cosmology & Physiology */
h2, h3 {
    opacity: 0 !important;
}
</style>
<script>
window.addEventListener('load', () => {
    // Keep trying to click ENCYCLOPEDIA to load the white UI
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
"""

c = c.replace('</body>', css_injection + '\n</body>')

with open('lexicon.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Injected SVG hider and clicker.')
