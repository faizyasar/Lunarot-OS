import shutil
import os

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
dist_index = os.path.join(root_dir, "dist", "index.html")
target_latest = os.path.join(root_dir, "Lunarot-OS-LATEST.html")
public_dir = os.path.join(root_dir, "public")

if os.path.exists(dist_index):
    shutil.copyfile(dist_index, target_latest)
    shutil.copyfile(dist_index, os.path.join(public_dir, "osLATEST.html"))
    shutil.copyfile(dist_index, os.path.join(public_dir, "Lunarot-OS.html"))
    print("[SUCCESS] Synchronized all standalone downloadable files with Build 671337 production output")
else:
    print("[ERROR] dist/index.html missing")
