import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

pos = content.find("mark-wrap")
if pos != -1:
    snippet = content[max(0, pos-100):min(len(content), pos+300)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Mark snippet:\n", safe_snippet)

pos_mark = content.find(".mark{")
if pos_mark != -1:
    snippet_mark = content[pos_mark:pos_mark+500]
    safe_snippet_mark = snippet_mark.encode('ascii', errors='replace').decode('ascii')
    print("\n.mark CSS snippet:\n", safe_snippet_mark)
