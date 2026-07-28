import re

os54_path = r"C:\Users\faizy\Downloads\Lunarot-OS54.html"

with open(os54_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

pos_rp = content.find("function rp(")
if pos_rp != -1:
    pos_end = content.find("function ai(", pos_rp)
    if pos_end == -1:
        pos_end = pos_rp + 3000
    snippet_rp = content[pos_rp:pos_end]
    safe_snippet = snippet_rp.encode('ascii', errors='replace').decode('ascii')
    print("Exact rp() function in OS54:\n", safe_snippet)
