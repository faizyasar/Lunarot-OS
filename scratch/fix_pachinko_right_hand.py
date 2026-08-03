import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

files_to_fix = [
    "public/sacred-pachinko.html",
    "public/pachinko.html"
]

target_str = 'style=\\"position:absolute;left:763px;'
replacement_str = 'style=\\"position:absolute;right:-45px;'

for fname in files_to_fix:
    if os.path.exists(fname):
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
        
        if target_str in content:
            content = content.replace(target_str, replacement_str)
            with open(fname, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[SUCCESS] Updated right hand positioning in {fname}!")
        else:
            print(f"[WARN] Target string not found in {fname}!")

