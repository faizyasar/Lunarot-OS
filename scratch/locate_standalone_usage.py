import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find('TarotStandaloneView')
print("TarotStandaloneView pos:", pos)
if pos != -1:
    snippet = text[max(0, pos-100):min(len(text), pos+300)]
    print("TarotStandaloneView usage snippet:\n", repr(snippet))
