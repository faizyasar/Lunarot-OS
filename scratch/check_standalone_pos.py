import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect where TarotStandaloneView is rendered vs lp vs pp
pos = text.find('TarotStandaloneView')
while pos != -1:
    snippet = text[max(0, pos-40):min(len(text), pos+120)]
    ascii_s = snippet.encode('ascii', errors='ignore').decode('ascii')
    print(f"TarotStandaloneView at {pos}:", ascii_s)
    pos = text.find('TarotStandaloneView', pos + 1)
