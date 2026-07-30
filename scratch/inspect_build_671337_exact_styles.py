import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# 1. Search for hex colors in index.html
hex_colors = set(re.findall(r'#[0-9a-fA-F]{3,8}', content))
print("Hex Colors found in index.html:")
for c in sorted(hex_colors):
    print(c)

# 2. Search for rgb/rgba colors in index.html
rgba_colors = set(re.findall(r'rgba\([^)]+\)', content))
print("\nRGBA Colors found in index.html (sample 15):")
for c in list(rgba_colors)[:15]:
    print(c)

# 3. Check font families in index.html
fonts = set(re.findall(r'font-[a-zA-Z0-9_-]+', content))
print("\nFont classes found in index.html:")
for fn in sorted(fonts):
    print(fn)
