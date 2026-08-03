import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

print("Length of HEAD index.html:", len(text))
print("Build version tag in HEAD:", "A671339" in text or "671339" in text)
print("music.index in HEAD:", "/db/music.index" in text)
print("deka-archive.index in HEAD:", "/db/deka-archive.index" in text)
