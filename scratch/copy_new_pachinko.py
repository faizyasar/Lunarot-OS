import shutil
import os

src_file = r"C:\Users\faizy\Downloads\Sacred Pachinko 0.9.html"
root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
public_dir = os.path.join(root_dir, "public")

if not os.path.exists(src_file):
    print(f"[ERROR] Source file does not exist: {src_file}")
else:
    size = os.path.getsize(src_file)
    print(f"[FOUND] {src_file} ({size} bytes)")

    # Targets to replace
    t1 = os.path.join(root_dir, "pachinkoLATEST.html")
    t2 = os.path.join(public_dir, "pachinkoLATEST.html")
    t3 = os.path.join(public_dir, "sacred-pachinko.html")
    t4 = os.path.join(public_dir, "pachinko.html")

    shutil.copyfile(src_file, t1)
    print("[SUCCESS] Updated root pachinkoLATEST.html")

    shutil.copyfile(src_file, t2)
    print("[SUCCESS] Updated public/pachinkoLATEST.html")

    shutil.copyfile(src_file, t3)
    print("[SUCCESS] Updated public/sacred-pachinko.html")

    shutil.copyfile(src_file, t4)
    print("[SUCCESS] Updated public/pachinko.html")

    print("[COMPLETE] Copy operation finished.")
