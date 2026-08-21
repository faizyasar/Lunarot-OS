import re

def patch():
    with open(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\lexicon_debug\golem.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix 1: Shader luminance
    if 'pow(luminance' not in html:
        html = html.replace('float luminance = dot(tex.rgb, vec3(0.299, 0.587, 0.114));', 'float luminance = dot(tex.rgb, vec3(0.299, 0.587, 0.114));\n      luminance = pow(luminance, 1.25);')

    # Fix 2: Hoist lexiconData
    match_data = re.search(r'const lexiconData = \[.*?\];', html, re.DOTALL)
    if match_data:
        data_str = match_data.group(0)
        html = html.replace(data_str, '')
        html = re.sub(r'(<script>\s*)', r'\1' + data_str + '\n\n', html, count=1)

    # Remove FULL TREE view entirely
    html = re.sub(r'<div class="qf-btn" onclick="focusPreset\(\'full\'\)" id="btn-preset-full">.*?</div>\s*', '', html)

    # Start with KETER on load
    html = re.sub(r'window\.addEventListener\("DOMContentLoaded", \(\) => \{\s*', r'window.addEventListener("DOMContentLoaded", () => {\n  focusPreset("keter");\n', html)

    # The user zip `initLexiconMarkers` creates a div for each marker and calls `showLexiconPanel` on pointerenter.
    # But wait, in the zip `golem.html`, the user DID NOT USE `showLexiconPanel` for anything else. 
    # The actual beautiful UI is handled by `updateKnowledgeUI(item.id)`.
    # Let's replace `showLexiconPanel(item);` with `updateKnowledgeUI(item.id);` inside `initLexiconMarkers`.
    html = html.replace('showLexiconPanel(item);', 'updateKnowledgeUI(item.id);')
    
    with open(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print('Successfully patched zip golem.html and wrote to main workspace.')

patch()
