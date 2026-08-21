import re

with open('lexicon.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Nuke script
nuke_script = """
<script>
window.addEventListener('load', () => {
    const observer = new MutationObserver((mutations, obs) => {
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
        let node;
        while (node = walker.nextNode()) {
            if (node.nodeValue.includes('Cosmology & Physiology')) {
                // Find the wrapper (two levels up usually works for this layout)
                let wrapper = node.parentElement;
                if (wrapper && wrapper.parentElement && wrapper.parentElement.parentElement) {
                    wrapper.parentElement.parentElement.style.display = 'none';
                    // also hide the title itself if we missed it
                    wrapper.style.display = 'none';
                }
            }
        }
    });
    observer.observe(document.body, { childList: true, subtree: true });
});
</script>
"""

c = c.replace('</body>', nuke_script + '\n</body>')

with open('lexicon.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Injected nuke script to hide the tree diagram completely.')
