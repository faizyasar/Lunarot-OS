import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate container block around space-y-1
idx = content.find('className:"space-y-1"')
if idx != -1:
    snippet = content[max(0, idx-50):min(len(content), idx+600)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Found container snippet:\n", safe_snippet)
else:
    print("className space-y-1 not found")
