import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace bg-black/40 with bg-transparent on TarotStandaloneView
old_str = 'className:\\"flex-1 flex flex-col h-full w-full bg-black/40 relative z-25 overflow-hidden\\"'
new_str = 'className:\\"flex-1 flex flex-col h-full w-full bg-transparent relative z-25 overflow-hidden\\"'

if old_str in text:
    text = text.replace(old_str, new_str)
    print("[SUCCESS] Made TarotStandaloneView wrapper background transparent in index.html!")
else:
    print("[WARN] Could not find exact old_str in index.html")

# Replace bg-black/35 on music component
old_music = "bg-black/35 backdrop-blur-[2px]"
new_music = "bg-transparent"

if old_music in text:
    text = text.replace(old_music, new_music)
    print("[SUCCESS] Made music component background transparent in index.html!")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(text)

shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))
print("[COMPLETE] Synced all OS files.")
