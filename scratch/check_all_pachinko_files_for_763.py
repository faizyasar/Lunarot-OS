import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

files_to_check = [
    "public/sacred-pachinko.html",
    "public/pachinko.html",
    "index.html"
]

for fname in files_to_check:
    if os.path.exists(fname):
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"\n=== CHECKING {fname} ===")
        matches = re.finditer(r'.{0,60}mainRightHandRef.{0,100}', content)
        for m in matches:
            print("  ", repr(m.group(0).strip()))

