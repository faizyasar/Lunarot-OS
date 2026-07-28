import sys

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split('\n')
for i, l in enumerate(lines):
    if 'faizyasar' in l.lower() or 'lunarot' in l.lower() or 'occult' in l.lower() or 'conduits' in l.lower() or 'build' in l.lower():
        # Print safely in ascii or utf-8
        safe_l = l[:150].encode('ascii', errors='replace').decode('ascii')
        print(f"Line {i+1}: {safe_l}")
