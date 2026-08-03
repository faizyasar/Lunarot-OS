import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("public/sacred-pachinko.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for images / webp assets or canvas drawing in sacred-pachinko.html
print("=== ASSETS AND CANVAS DRAWING IN SACRED PACHINKO ===")

# Find images / data URIs or asset references
assets = re.findall(r'["\'](assets/[^"\']+)["\']', content)
print(f"Asset paths found: {set(assets)}")

# Find canvas context drawing or image draw calls
draw_calls = re.findall(r'\.drawImage\([^)]+\)', content)
print(f"Found {len(draw_calls)} drawImage calls:")
for d in draw_calls[:20]:
    print("  ", d)

