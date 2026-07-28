import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for function xp
pos = content.find("function xp()")
if pos != -1:
    snippet = content[pos:pos+1500]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Function xp snippet:\n", safe_snippet)
else:
    print("function xp not found")
