import re
import json

filepath = r'C:\Users\faizy\Downloads\standalone (1).html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find("Malkhut/Regnum/Mulk")
with open(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\malkhut.txt', 'w', encoding='utf-8') as out:
    if idx != -1:
        start = max(0, idx - 1000)
        end = min(len(content), idx + 1000)
        out.write(content[start:end])
