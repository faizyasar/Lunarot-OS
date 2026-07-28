import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inspect vp array definition
pos_vp = content.find("const vp=[")
if pos_vp != -1:
    snippet_vp = content[pos_vp:pos_vp+500]
    safe_snippet_vp = snippet_vp.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print("VP Array:\n", safe_snippet_vp)

# 2. Inspect where vp items are mapped / rendered in the sidebar
pos_map = content.find("files.map")
while pos_map != -1:
    snippet_map = content[max(0, pos_map-100):min(len(content), pos_map+300)]
    safe_snippet_map = snippet_map.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"\nfiles.map at {pos_map}:\n", safe_snippet_map)
    pos_map = content.find("files.map", pos_map+1)

# 3. Inspect main window rendering logic in xp()
pos_xp = content.find('v==="/apps/sacred-draw.bin"')
if pos_xp != -1:
    snippet_xp = content[max(0, pos_xp-100):min(len(content), pos_xp+800)]
    safe_snippet_xp = snippet_xp.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print("\nXP rendering logic:\n", safe_snippet_xp)
