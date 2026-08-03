import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find('/db/tarot-directory.index')
pos2 = text.find('/db/tarot-directory.index', pos + 1)

print("Exact repr around 2nd occurrence:")
snippet = text[pos2-10:pos2+100]
print(repr(snippet))
