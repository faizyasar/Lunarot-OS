import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# Remove old lp component render for /apps/sacred-draw.bin
old_lp_render = 'v===\\"/apps/sacred-draw.bin\\"&&g&&s.jsx(lp,{user:g,onUpdatePlanets:J,onUpdateActivePlanets:Y,onReset:q,isPurging:ce,setIsPurging:V}),'
new_lp_render = 'v===\\"/db/tarot-directory.index\\"&&g&&s.jsx(lp,{user:g,onUpdatePlanets:J,onUpdateActivePlanets:Y,onReset:q,isPurging:ce,setIsPurging:V}),'

if old_lp_render in text:
    text = text.replace(old_lp_render, new_lp_render)
    print("[SUCCESS] Replaced 3-card spread (lp) on sacred-draw.bin with 3D Deck (TarotStandaloneView)!")
else:
    print("[WARN] Could not find old_lp_render")

# Ensure header text for /apps/sacred-draw.bin is updated
old_header_case = 'case\\"/apps/sacred-draw.bin\\":K(\\"SACRED GEOMETRY CANVAS // DRAW TO CONJURE\\");break;'
new_header_case = 'case\\"/apps/sacred-draw.bin\\":K(\\"SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER\\");break;'

if old_header_case in text:
    text = text.replace(old_header_case, new_header_case)
    print("[SUCCESS] Updated header title for /apps/sacred-draw.bin!")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(text)

shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))
print("[COMPLETE] Synced all files.")
