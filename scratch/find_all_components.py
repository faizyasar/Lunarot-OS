import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for function definitions around 490k - 540k
matches = [m.start() for m in re.finditer(r'function\s+([a-zA-Z0-9_$]+)\s*\(', content)]
print(f"Total function definitions: {len(matches)}")
for m in matches:
    if m > 480000 and m < 540000:
        snippet = content[m:m+100]
        safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
        print(f"Pos {m}: {safe_snippet}")
