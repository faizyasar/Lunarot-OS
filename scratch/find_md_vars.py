import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search around 480k - 500k for variable definitions nh=, sp=, up=, cp=
pos = content.find("nh=`")
if pos != -1:
    snippet = content[pos:pos+500]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print("nh definition snippet:\n", safe_snippet)

pos_cp = content.find("cp=`")
if pos_cp != -1:
    snippet_cp = content[pos_cp:pos_cp+500]
    safe_snippet_cp = snippet_cp.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print("cp definition snippet:\n", safe_snippet_cp)
