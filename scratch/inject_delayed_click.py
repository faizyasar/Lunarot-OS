import re

with open('lexicon.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the previous script
c = re.sub(r'<script>\s*function triggerReactClick.*?<\/script>', '', c, flags=re.DOTALL)

new_script = """<script>
window.addEventListener('load', () => {
    // Wait 1.5 seconds for React to completely render and hydrate
    setTimeout(() => {
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
        let node;
        while (node = walker.nextNode()) {
            if (node.nodeValue.trim().toUpperCase() === 'ENCYCLOPEDIA') {
                let element = node.parentElement;
                const mouseClickEvents = ['mousedown', 'click', 'mouseup'];
                mouseClickEvents.forEach(mouseEventType =>
                    element.dispatchEvent(
                        new MouseEvent(mouseEventType, {
                            view: window,
                            bubbles: true,
                            cancelable: true,
                            buttons: 1
                        })
                    )
                );
                console.log("Successfully auto-clicked ENCYCLOPEDIA");
                break;
            }
        }
    }, 1500);
});
</script>"""

# inject right before </body>
c = c.replace('</body>', new_script + '\n</body>')

with open('lexicon.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Injected delayed auto-click script into lexicon.html')
