import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for 16/07/2026 in content
idx = content.find("16/07/2026")
if idx != -1:
    snippet = content[max(0, idx-100):min(len(content), idx+300)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Snippet at 16/07/2026:\n{safe_snippet}")
else:
    print("16/07/2026 not found, searching 2026")
