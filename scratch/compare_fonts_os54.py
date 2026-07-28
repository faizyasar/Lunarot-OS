import os
import re

os54_path = r"C:\Users\faizy\Downloads\Lunarot-OS54.html"
index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(os54_path, "r", encoding="utf-8", errors="ignore") as f:
    os54_content = f.read()

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    index_content = f.read()

# Compare rp() functions
pos_rp54 = os54_content.find("function rp(")
pos_rp_idx = index_content.find("function rp(")

snippet54 = os54_content[pos_rp54:pos_rp54+1500]
snippet_idx = index_content[pos_rp_idx:pos_rp_idx+1500]

print("=== rp() in OS54 ===")
print(snippet54.encode('ascii', errors='replace').decode('ascii')[:600])

print("\n=== rp() in index.html ===")
print(snippet_idx.encode('ascii', errors='replace').decode('ascii')[:600])

# Compare Google Fonts link tags in head
head54 = os54_content[:os54_content.find("</head>")]
head_idx = index_content[:index_content.find("</head>")]

print("\n=== Head Font links in OS54 ===")
fonts54 = re.findall(r'href="[^"]*fonts[^"]*"', head54)
for f in fonts54:
    print(f)

print("\n=== Head Font links in index.html ===")
fonts_idx = re.findall(r'href="[^"]*fonts[^"]*"', head_idx)
for f in fonts_idx:
    print(f)
