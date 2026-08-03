import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find('v==="/db/tarot-directory.index"')
if pos != -1:
    snippet = text[pos:pos+100]
    print("Exact snippet:")
    print(repr(snippet))
else:
    print("Not found")
