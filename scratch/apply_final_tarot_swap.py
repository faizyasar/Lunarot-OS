import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

target = 'v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K})'
replacement = 'v==="/db/tarot-directory.index"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K})'

if target in content:
    content = content.replace(target, replacement)
    print("[SUCCESS] Successfully replaced tarot-directory.index render hook with TarotStandaloneView")
else:
    print("[ERROR] Target string not found")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

# Update standalone copies
shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Updated all standalone HTML copies.")
