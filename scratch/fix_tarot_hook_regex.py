import os
import re
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Match v==="/db/tarot-directory.index" and replace the function name after s.jsx(
m = re.search(r'(v==="/db/tarot-directory\.index"&&s\.jsx\()([a-zA-Z0-9_$]+)(,)', content)
if m:
    old_full = m.group(0)
    new_full = m.group(1) + 'TarotStandaloneView' + m.group(3)
    content = content.replace(old_full, new_full)
    print(f"[SUCCESS] Replaced '{old_full}' with '{new_full}'")
else:
    print("[ERROR] Regex did not match tarot-directory render hook!")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

# Update all standalone copies
shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Successfully replaced tarot render hook.")
