import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

has_component = "function TarotStandaloneView" in text
has_iframe_src = "/tarot-standalone.html" in text
has_render_hook = 'v===\\"/db/tarot-directory.index\\"&&s.jsx(TarotStandaloneView' in text

print("========================================")
print("INDEX.HTML VERIFICATION REPORT:")
print(" - TarotStandaloneView Component defined:", has_component)
print(" - Embedded iframe src /tarot-standalone.html:", has_iframe_src)
print(" - /db/tarot-directory.index mapped to TarotStandaloneView:", has_render_hook)
print("========================================")

if has_component and has_iframe_src and has_render_hook:
    shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
    shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
    shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))
    print("[SUCCESS] All build artifacts verified and synchronized.")
