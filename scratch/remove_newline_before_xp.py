import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

target = '})}\nfunction xp()'
replacement = '});}function xp()'

if target in text:
    text = text.replace(target, replacement)
    print("[SUCCESS] Removed literal newline between TarotStandaloneView and function xp()")
else:
    print("[WARN] Target not found")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(text)

# Update all standalone copies
shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Done.")
