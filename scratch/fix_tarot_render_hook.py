import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate v==="/db/tarot-directory.index" and replace its component
old_pattern = 'v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K})'
new_pattern = 'v==="/db/tarot-directory.index"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K})'

if old_pattern in content:
    content = content.replace(old_pattern, new_pattern)
    print("[SUCCESS] Replaced old tarot render pattern with TarotStandaloneView")
else:
    print("[WARN] Could not find exact old_pattern string, doing regex search...")
    import re
    m = re.search(r'v==="/db/tarot-directory\.index"&&s\.jsx\([^,]+,', content)
    if m:
        matched_str = m.group(0)
        print("Matched pattern:", matched_str)
        content = content.replace(matched_str, 'v==="/db/tarot-directory.index"&&s.jsx(TarotStandaloneView,')
        print("[SUCCESS] Updated tarot render hook via regex")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

# Update standalone copies
shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Successfully replaced tarot-directory.index render hook in index.html.")
