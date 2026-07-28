import re

os54_path = r"C:\Users\faizy\Downloads\Lunarot-OS54.html"

with open(os54_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

pos_ai = content.find("function ai(")
if pos_ai != -1:
    pos_end = content.find("function hp()", pos_ai)
    if pos_end == -1:
        pos_end = pos_ai + 20000
    snippet_ai = content[pos_ai:pos_end]
    safe_snippet = snippet_ai.encode('ascii', errors='replace').decode('ascii')
    print("Exact ai() function in OS54 length:", len(snippet_ai))
    with open(r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\os54_ai_function.js", "w", encoding="utf-8") as out:
        out.write(snippet_ai)
    print("Saved exact os54 ai function to scratch/os54_ai_function.js")
