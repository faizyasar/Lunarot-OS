import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for op=
matches = [m.start() for m in re.finditer(r'\bop\s*=\s*', content)]
print(f"Total op= matches: {len(matches)}")
for m in matches:
    snippet = content[max(0, m-20):min(len(content), m+100)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Match at {m}: {safe_snippet}")
