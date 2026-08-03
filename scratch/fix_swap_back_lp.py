import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Swap main view condition:
# lp component (Sacred Draw 3-card spread) goes back to /apps/sacred-draw.bin
# TarotStandaloneView (3D Deck of Cards) goes back to /db/tarot-directory.index

old_lp = 'v===\\"/db/tarot-directory.index\\"&&g&&s.jsx(lp,{user:g,onUpdatePlanets:J,onUpdateActivePlanets:Y,onReset:q,isPurging:ce,setIsPurging:V})'
new_lp = 'v===\\"/apps/sacred-draw.bin\\"&&g&&s.jsx(lp,{user:g,onUpdatePlanets:J,onUpdateActivePlanets:Y,onReset:q,isPurging:ce,setIsPurging:V})'

if old_lp in text:
    text = text.replace(old_lp, new_lp)
    print("[SUCCESS] Restored lp (Sacred Draw 3-card spread) to /apps/sacred-draw.bin!")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(text)

shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))
print("[COMPLETE] Synced all files.")
