import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

pos = content.find('v==="/apps/sacred-draw.bin"')
if pos != -1:
    snippet = content[max(0, pos-100):min(len(content), pos+800)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print("xp body rendering snippet:\n", safe_snippet)
else:
    print("v===/apps/sacred-draw.bin not found")
