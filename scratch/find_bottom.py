import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for matches containing bottom or footer
matches = [m.start() for m in re.finditer(r'bottom|footer', content, re.IGNORECASE)]

print(f"Total matches for bottom/footer: {len(matches)}")
for idx in matches:
    snippet = content[max(0, idx-100):min(len(content), idx+150)]
    print("--- SNIPPET ---")
    print(snippet.replace('\n', ' '))
