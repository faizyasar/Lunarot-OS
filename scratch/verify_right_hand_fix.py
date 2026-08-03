import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ["public/sacred-pachinko.html", "public/pachinko.html"]:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"\n=== VERIFYING {fname} ===")
    print("Contains left:763px:", "left:763px" in content)
    print("Contains right:-45px:", "right:-45px" in content)
