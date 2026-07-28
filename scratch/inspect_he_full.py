import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate he definition in index.html
pos = content.find("he=_=>{")
if pos == -1:
    pos = content.find("he=_=>")

if pos != -1:
    snippet = content[max(0, pos-100):min(len(content), pos+400)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print("he definition snippet:\n", safe_snippet)
else:
    print("he=_=> not found, searching he=")
    matches = [m.start() for m in re.finditer(r'he\s*=\s*', content)]
    for m in matches:
        snippet = content[max(0, m-20):min(len(content), m+100)]
        safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
        print(f"Match at {m}: {safe_snippet}")
