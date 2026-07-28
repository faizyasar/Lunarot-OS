import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

pos = content.find('className:"mark-wrap"')
if pos != -1:
    snippet = content[max(0, pos-100):min(len(content), pos+400)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Mark wrap snippet:\n", safe_snippet)
