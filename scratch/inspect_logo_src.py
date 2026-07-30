import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Search for Y0 or logo image src definition
pos = content.find('alt:"LUNAROT Logo"')
if pos != -1:
    snippet = content[max(0, pos-400):min(len(content), pos+200)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print("Logo render snippet:\n", safe_snippet)

# Search for data:image or logo base64 / URL variables
matches = re.findall(r'const\s+[a-zA-Z0-9_$]+\s*=\s*"data:image/[^"]+"', content)
print("\nBase64 Image variables count:", len(matches))
for m in matches[:5]:
    safe_m = m[:100].encode('ascii', errors='replace').decode('ascii')
    print(safe_m)
