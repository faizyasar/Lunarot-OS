target_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

pos = content.find("function updateCRT()")
if pos != -1:
    snippet = content[pos:pos+1500]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("updateCRT snippet:\n", safe_snippet)
