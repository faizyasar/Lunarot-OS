import os

src_file = r"C:\Users\faizy\Downloads\Lunarot OS - Build 671337.html"
target_index = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

if os.path.exists(src_file):
    size = os.path.getsize(src_file)
    print(f"[FOUND] {src_file} ({size} bytes)")
    with open(src_file, "r", encoding="utf-8", errors="ignore") as f:
        head = f.read(500)
    print("Head snippet:\n", head[:300])
else:
    print(f"[ERROR] {src_file} not found")
