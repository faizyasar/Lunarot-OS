import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# Make /apps/sacred-draw.bin render TarotStandaloneView (the 3D Deck of Cards style)
# Make /db/tarot-directory.index render pp (the 2D Tarot Directory)

old_rendering = 'v===\\"/apps/sacred-draw.bin\\"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K}),v===\\"/db/tarot-directory.index\\"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K})'

# Let's inspect where sacred-draw is rendered
pos = text.find('sacred-draw')
print("sacred-draw pos:", pos)
while pos != -1:
    snippet = text[max(0, pos-40):min(len(text), pos+120)]
    ascii_s = snippet.encode('ascii', errors='ignore').decode('ascii')
    print(f"Match at {pos}:", ascii_s)
    pos = text.find('sacred-draw', pos + 1)
