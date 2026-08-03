import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's search for canvas elements or main layout containers in index.html
pos = 0
while True:
    pos = text.find('canvas', pos)
    if pos == -1:
        break
    print(f"Canvas reference at {pos}:", repr(text[max(0, pos-40):min(len(text), pos+60)]))
    pos += 6

# Search for main window/viewport background in index.html
pos = 0
while True:
    pos = text.find('sacred-draw', pos)
    if pos == -1:
        break
    print(f"sacred-draw reference at {pos}:", repr(text[max(0, pos-40):min(len(text), pos+60)]))
    pos += 11
