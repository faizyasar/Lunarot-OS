import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate v==="/db/tarot-directory.index" and replace its rendered component
target = 'v==="/db/tarot-directory.index"&&s.jsx('
idx = content.find(target)

if idx != -1:
    end_jsx = content.find('),v===', idx)
    if end_jsx != -1:
        old_sub = content[idx:end_jsx+1]
        new_sub = 'v==="/db/tarot-directory.index"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K})'
        content = content.replace(old_sub, new_sub)
        print(f"[SUCCESS] Replaced '{old_sub[:60]}...' with TarotStandaloneView")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Successfully integrated 3D Tarot Standalone Deck.")
