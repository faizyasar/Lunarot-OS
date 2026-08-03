import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# Swap components:
# /apps/sacred-draw.bin -> TarotStandaloneView (3D Deck of Cards)
# /db/tarot-directory.index -> pp (2D Sacred Draw Directory)

old_case = 'v===\\"/db/tarot-directory.index\\"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K})'
new_case = 'v===\\"/apps/sacred-draw.bin\\"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K}),v===\\"/db/tarot-directory.index\\"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K})'

if old_case in text:
    text = text.replace(old_case, new_case)
    print("[SUCCESS] Swapped 3D Deck to /apps/sacred-draw.bin and 2D directory to /db/tarot-directory.index!")
else:
    print("[ERROR] old_case not found")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(text)

shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))
print("[COMPLETE] Synced all files.")
