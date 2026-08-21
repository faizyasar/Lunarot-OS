import re

with open('lexicon.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the previous script with an even more robust one
old_script = """<script>
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
        if (node.nodeValue.trim().toUpperCase() === 'ENCYCLOPEDIA') {
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

print('Injected super robust auto-click script into lexicon.html')
