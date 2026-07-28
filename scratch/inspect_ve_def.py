import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for Ve definition
matches = [m.start() for m in re.finditer(r'Ve\b', content)]
print(f"Total matches for Ve: {len(matches)}")
for m in matches[:10]:
    snippet = content[max(0, m-50):min(len(content), m+150)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Pos {m}: {safe_snippet}")
