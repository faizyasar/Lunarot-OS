import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for op= in index.html
pos = content.find("op=`")
if pos != -1:
    snippet = content[pos:pos+1000]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("op string snippet:\n", safe_snippet)
else:
    print("op=` not found")
