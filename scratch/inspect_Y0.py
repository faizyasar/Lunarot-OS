import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Search for Y0=
pos = content.find("Y0=")
if pos != -1:
    snippet = content[pos:pos+500]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Y0 definition snippet:\n", safe_snippet)

# Search for base64 or img imports
matches = re.findall(r'Y0\s*=\s*"[^"]+"', content)
for m in matches:
    print("Matched Y0:", m[:80])
