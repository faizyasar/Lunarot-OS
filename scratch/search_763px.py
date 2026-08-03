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
        print(f"\n=== CHECKING 763px IN {fname} ===")
        pos = 0
        while True:
            idx = content.find("763px", pos)
            if idx == -1:
                break
            print("  Match at", idx, ":", repr(content[max(0, idx-60):min(len(content), idx+100)]))
            pos = idx + 10

