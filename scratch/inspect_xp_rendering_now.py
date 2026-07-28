import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

pos = content.find('v==="/db/tarot-directory.index"')
if pos != -1:
    snippet = content[max(0, pos-100):min(len(content), pos+800)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Exact xp rendering JSX now:\n", safe_snippet)
else:
    print("v===/db/tarot-directory.index not found")
