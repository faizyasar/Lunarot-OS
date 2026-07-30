import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Search for data:image/webp in index.html
matches = re.finditer(r'data:image/[^"]+', content)
for i, m in enumerate(matches):
    url = m.group(0)
    print(f"Data URL #{i+1} (length {len(url)}): {url[:80]}...")
