import base64
import re
import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"
root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Extract Data URL
match = re.search(r'data:image/webp;base64,([A-Za-z0-9+/=]+)', content)
if not match:
    print("[ERROR] Base64 webp string not found")
    exit(1)

b64_data = match.group(1)
img_bytes = base64.b64decode(b64_data)

root_logo_path = os.path.join(root_dir, "lunarot-logo.webp")
public_logo_path = os.path.join(public_dir, "lunarot-logo.webp")

with open(root_logo_path, "wb") as f:
    f.write(img_bytes)

with open(public_logo_path, "wb") as f:
    f.write(img_bytes)

print(f"[SUCCESS] Extracted image ({len(img_bytes)} bytes) to {root_logo_path} and {public_logo_path}")
