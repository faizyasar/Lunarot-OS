import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Find all img tags in JSX / HTML
imgs = [m.group(0) for m in re.finditer(r's\.jsx\("img",\{[^}]+\}\)', content)]
print(f"Total img tags found in JSX: {len(imgs)}")
for img in imgs[:10]:
    safe_img = img[:150].encode('ascii', errors='replace').decode('ascii')
    print(safe_img)
