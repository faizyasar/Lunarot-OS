import re

with open('golem.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Add logic to focusPreset to toggle the iframe
injection = """    const iframe = document.getElementById('full-lexicon-iframe');
    if (iframe) {
        if (presetKey === 'full') {
            iframe.style.display = 'block';
        } else {
            iframe.style.display = 'none';
        }
    }"""

old_start = """    window.activePresetKey = presetKey;
    updateKnowledgeUI(presetKey);
    const p = EXACT_PRESETS[presetKey];"""

new_start = f"""    window.activePresetKey = presetKey;
    updateKnowledgeUI(presetKey);
{injection}
    const p = EXACT_PRESETS[presetKey];"""

c = c.replace(old_start, new_start)

with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Injected iframe toggle logic into focusPreset.')
