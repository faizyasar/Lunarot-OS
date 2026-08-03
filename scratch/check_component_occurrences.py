import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find('TarotStandaloneView')
count = 0
while pos != -1:
    count += 1
    snippet = text[max(0, pos-20):min(len(text), pos+60)]
    ascii_snippet = snippet.encode('ascii', errors='ignore').decode('ascii')
    print(f"[{count}] {repr(ascii_snippet)}")
    pos = text.find('TarotStandaloneView', pos + 1)
