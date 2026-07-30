import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Locate aesthetic tokens function gp() in index.html
pos_gp = content.find("function gp(")
if pos_gp != -1:
    snippet_gp = content[pos_gp:pos_gp+3000]
    safe_gp = snippet_gp.encode('ascii', errors='replace').decode('ascii')
    print("Aesthetic tokens snippet (gp):\n", safe_gp[:1500])

# Extract Google Fonts import
font_match = re.search(r'@import"https://fonts.googleapis.com/[^"]+"', content)
if font_match:
    print("\nGoogle Fonts Import:\n", font_match.group(0))
