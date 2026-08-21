import re

with open('lexicon.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Add a script before </body> to automatically click ENCYCLOPEDIA
script_to_inject = """<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        // Find all elements that might be the encyclopedia button
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
        let node;
        while (node = walker.nextNode()) {
            if (node.nodeValue.trim() === 'ENCYCLOPEDIA') {
                let elem = node.parentElement;
                while (elem && elem.tagName !== 'BUTTON' && elem.tagName !== 'A' && !elem.onclick) {
                    // if it's just a span or div, it might have click handler, so try clicking it anyway
                    if (elem.tagName === 'DIV' || elem.tagName === 'SPAN') {
                        elem.click();
                    }
                    elem = elem.parentElement;
                }
                if (elem) elem.click();
            }
        }
    }, 100);
});
</script>
</body>"""

c = c.replace('</body>', script_to_inject)

with open('lexicon.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Injected auto-click script into lexicon.html')
