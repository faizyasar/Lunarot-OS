import shutil
import os

src_file = r"C:\Users\faizy\Downloads\Lunarot OS - Build 671337.html"
root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
target_index = os.path.join(root_dir, "index.html")
target_latest = os.path.join(root_dir, "Lunarot-OS-LATEST.html")
public_dir = os.path.join(root_dir, "public")

if not os.path.exists(src_file):
    print(f"[ERROR] Source file not found: {src_file}")
else:
    size = os.path.getsize(src_file)
    print(f"[FOUND] {src_file} ({size} bytes)")

    # 1. Update index.html
    shutil.copyfile(src_file, target_index)
    print(f"[SUCCESS] Updated index.html from Build 671337")

    # 2. Update Lunarot-OS-LATEST.html
    shutil.copyfile(src_file, target_latest)
    print(f"[SUCCESS] Updated Lunarot-OS-LATEST.html")

    # 3. Update public/osLATEST.html and public/Lunarot-OS.html
    shutil.copyfile(src_file, os.path.join(public_dir, "osLATEST.html"))
    shutil.copyfile(src_file, os.path.join(public_dir, "Lunarot-OS.html"))
    print(f"[SUCCESS] Updated public standalone copies")

    print("[COMPLETE] Successfully applied Build 671337 across workspace.")
