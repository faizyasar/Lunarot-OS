import re

with open('lexicon.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the previous script
c = re.sub(r'<script>\s*window\.addEventListener.*?</script>', '', c, flags=re.DOTALL)

new_script = """<script>
window.addEventListener('load', () => {
    // Wait for React to render
    setTimeout(() => {
        const elements = Array.from(document.querySelectorAll('*')).filter(e => 
            e.children.length === 0 && e.textContent && e.textContent.trim().toUpperCase() === 'ENCYCLOPEDIA'
        );
        
        if (elements.length > 0) {
            let el = elements[0];
            console.log("Found ENCYCLOPEDIA element:", el);
            
            // Dispatch a native click
            el.click();
            
            // Also dispatch mouse events just in case
            const mouseClickEvents = ['mousedown', 'mouseup', 'click'];
            mouseClickEvents.forEach(mouseEventType =>
                el.dispatchEvent(new MouseEvent(mouseEventType, {view: window, bubbles: true, cancelable: true, buttons: 1}))
            );
            
            // Also click parent just in case
            if (el.parentElement) {
                el.parentElement.click();
            }
        }
    }, 1500);
});
</script>"""

# inject right before </body>
c = c.replace('</body>', new_script + '\n</body>')

with open('lexicon.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Injected super-ultra robust auto-click script into lexicon.html')
