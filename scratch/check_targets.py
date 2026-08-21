with open('golem.html', 'r', encoding='utf-8') as f:
    c = f.read()

targets = [
    '</style>',
    '<div id="sephirot-markers"></div>',
    'function init() {',
    'const createScene = ',
    'if (sephirotMeshMap[key] === mesh.name)',
    '// --- Sephirot Markers ---'
]

for t in targets:
    print(f"{t!r} in file: {t in c}")
