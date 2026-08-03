import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update /apps/sacred-draw.bin to render TarotStandaloneView (the 3D Standalone Tarot Deck)
# 2. Update /db/tarot-directory.index to render pp (the 2D sacred draw directory)

old_rendering = 'v===\\"/db/tarot-directory.index\\"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K}),v===\\"/db/music.index\\"'
new_rendering = 'v===\\"/db/tarot-directory.index\\"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K}),v===\\"/apps/sacred-draw.bin\\"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K}),v===\\"/db/music.index\\"'

if old_rendering in text:
    text = text.replace(old_rendering, new_rendering)
    print("[SUCCESS] Mapped 3D Tarot Deck to /apps/sacred-draw.bin and 2D directory to /db/tarot-directory.index!")
else:
    print("[WARN] Could not find exact old_rendering string in index.html")

# Update header title switch cases as well
old_header_case = 'case\\"/db/tarot-directory.index\\":K(\\"SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER\\");break;'
new_header_case = 'case\\"/apps/sacred-draw.bin\\":K(\\"SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER\\");break;case\\"/db/tarot-directory.index\\":K(\\"SACRED TAROT DIRECTORY // 78 CONDUITS\\");break;'

if old_header_case in text:
    text = text.replace(old_header_case, new_header_case)
    print("[SUCCESS] Updated header title switch cases for sacred-draw.bin and tarot-directory.index!")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(text)

shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))
print("[COMPLETE] Synced all files.")
