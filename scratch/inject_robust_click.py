import re

with open('lexicon.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the previous script with a robust one
old_script = """<script>
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
</script>"""

new_script = """<script>
function triggerReactClick(element) {
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
}

let clicked = false;
setInterval(() => {
    if (clicked) return;
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    let node;
    while (node = walker.nextNode()) {
        if (node.nodeValue.trim() === 'ENCYCLOPEDIA') {
            triggerReactClick(node.parentElement);
            clicked = true;
            break;
        }
    }
}, 200);
</script>"""

c = c.replace(old_script, new_script)

with open('lexicon.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Injected robust auto-click script into lexicon.html')
