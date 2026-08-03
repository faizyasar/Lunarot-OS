import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# Inspect pp function definition (Sacred Draw view)
pos = text.find('function pp(')
if pos != -1:
    print("Found function pp( at:", pos)
    snippet = text[pos:pos+1500]
    safe_snippet = snippet.encode('ascii', errors='ignore').decode('ascii')
    print("pp() code snippet:\n", safe_snippet)
else:
    print("pp() function not found directly")
