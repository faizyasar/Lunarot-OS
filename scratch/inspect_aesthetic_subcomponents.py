import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

for comp_name in ["F0(", "P0(", "_0(", "W0(", "$0("]:
    pos = content.find(f"function {comp_name}")
    if pos != -1:
        snippet = content[pos:pos+1500]
        safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
        print(f"=== {comp_name} ===\n{safe_snippet[:600]}\n")
