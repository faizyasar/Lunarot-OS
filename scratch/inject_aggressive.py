import re

# start clean
with open('C:/Users/faizy/Downloads/standalone (1).html', 'r', encoding='utf-8') as f:
    c = f.read()

css_injection = """
<style>
/* Hide everything related to Unified Diagram by targeting the exact text */
body {
    /* If there's an issue with React hydration, we can use a CSS animation to constantly hide elements containing specific text? No. */
}
</style>
<script>
window.addEventListener('load', () => {
    // Keep checking every 100ms and delete the element if it exists
    setInterval(() => {
        const headers = document.querySelectorAll('h2');
        for (let h of headers) {
            if (h.textContent.includes('Cosmology & Physiology')) {
                // h2 -> div -> main wrapper
                let wrapper = h.parentElement.parentElement;
                if (wrapper) {
                    wrapper.style.display = 'none';
                    wrapper.style.visibility = 'hidden';
                    wrapper.style.opacity = '0';
                    wrapper.innerHTML = ''; // completely nuke it
                }
            }
        }
        
        // Let's also try to click the Encyclopedia tab as a fallback
        const tabs = document.querySelectorAll('span, button, a, div, h1, h2, h3, h4, h5, p, li');
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

print('Injected aggressive interval nuke and click script.')
