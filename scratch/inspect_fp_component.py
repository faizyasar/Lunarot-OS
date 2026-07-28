import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for where vp/research window component is defined
pos = content.find("RESEARCH_LOG // ANKOKU")
if pos != -1:
    snippet = content[max(0, pos-200):min(len(content), pos+800)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Research window snippet:\n", safe_snippet)
else:
    print("RESEARCH_LOG // ANKOKU not found")
