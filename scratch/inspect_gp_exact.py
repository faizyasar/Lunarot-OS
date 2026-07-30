import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

pos = content.find("function gp(")
if pos != -1:
    snippet = content[pos:pos+3500]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Exact gp() function snippet:\n", safe_snippet[:1500])
