import subprocess

result = subprocess.run(["git", "show", "4006ef0~1:index.html"], capture_output=True, cwd=r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0")

content = result.stdout.decode('utf-8', errors='ignore')

pos_ai = content.find("function ai(")
if pos_ai != -1:
    pos_end = content.find("function hp()", pos_ai)
    if pos_end == -1:
        pos_end = pos_ai + 15000
    snippet_ai = content[pos_ai:pos_end]
    print(f"Full ai function length: {len(snippet_ai)}")
    with open(r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\original_ai_function.js", "w", encoding="utf-8") as out:
        out.write(snippet_ai)
    print("Saved original ai function to scratch/original_ai_function.js")
