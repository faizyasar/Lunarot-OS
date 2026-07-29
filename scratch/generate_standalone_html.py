import shutil
import os

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
dist_index = os.path.join(root_dir, "dist", "index.html")
public_dir = os.path.join(root_dir, "public")

if not os.path.exists(dist_index):
    print("[ERROR] dist/index.html does not exist. Run npm run build first.")
else:
    size = os.path.getsize(dist_index)
    print(f"[FOUND] dist/index.html ({size} bytes)")

    # 1. Save in root directory as Lunarot-OS-LATEST.html
    root_target = os.path.join(root_dir, "Lunarot-OS-LATEST.html")
    shutil.copyfile(dist_index, root_target)
    print(f"[SUCCESS] Saved standalone HTML to {root_target}")

    # 2. Save in public directory as osLATEST.html
    public_target1 = os.path.join(public_dir, "osLATEST.html")
    shutil.copyfile(dist_index, public_target1)
    print(f"[SUCCESS] Saved standalone HTML to {public_target1}")

    # 3. Save in public directory as Lunarot-OS.html
    public_target2 = os.path.join(public_dir, "Lunarot-OS.html")
    shutil.copyfile(dist_index, public_target2)
    print(f"[SUCCESS] Saved standalone HTML to {public_target2}")

    print("[COMPLETE] Standalone HTML generation finished.")
