import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Swap components back:
# /db/tarot-directory.index -> TarotStandaloneView (3D Deck of Cards with original dark style)
# /apps/sacred-draw.bin -> lp (2D 3-card Sacred Draw Spread)

old_rendering = 'v===\\"/apps/sacred-draw.bin\\"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K}),v===\\"/db/tarot-directory.index\\"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K})'
new_rendering = 'v===\\"/apps/sacred-draw.bin\\"&&g&&s.jsx(lp,{user:g,onUpdatePlanets:J,onUpdateActivePlanets:Y,onReset:q,isPurging:ce,setIsPurging:V}),v===\\"/db/tarot-directory.index\\"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K})'

if old_rendering in text:
    text = text.replace(old_rendering, new_rendering)
    print("[SUCCESS] Swapped 3D Tarot Deck back to /db/tarot-directory.index and 2D spread back to /apps/sacred-draw.bin!")
else:
    print("[WARN] Could not find exact old_rendering string in index.html")

# 2. Restore dark wrapper background on TarotStandaloneView (bg-black/40)
old_transparent_wrapper = 'className:\\"flex-1 flex flex-col h-full w-full bg-transparent relative z-25 overflow-hidden\\"'
new_dark_wrapper = 'className:\\"flex-1 flex flex-col h-full w-full bg-black/40 relative z-25 overflow-hidden\\"'

if old_transparent_wrapper in text:
    text = text.replace(old_transparent_wrapper, new_dark_wrapper)
    print("[SUCCESS] Restored bg-black/40 wrapper background on TarotStandaloneView!")

# 3. Restore header title switch cases
old_header_sacred = 'case\\"/apps/sacred-draw.bin\\":K(\\"SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER\\");break;'
new_header_sacred = 'case\\"/apps/sacred-draw.bin\\":K(\\"SACRED GEOMETRY CANVAS // DRAW TO CONJURE\\");break;'
old_header_tarot = 'case\\"/db/tarot-directory.index\\":K(\\"SACRED TAROT DIRECTORY // 78 CONDUITS\\");break;'
new_header_tarot = 'case\\"/db/tarot-directory.index\\":K(\\"SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER\\");break;'

if old_header_sacred in text:
    text = text.replace(old_header_sacred, new_header_sacred)
if old_header_tarot in text:
    text = text.replace(old_header_tarot, new_header_tarot)

print("[SUCCESS] Restored header titles!")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(text)

shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))
print("[COMPLETE] Synced all files.")
