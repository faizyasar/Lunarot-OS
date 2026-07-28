import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search around 485000 - 495000 for markdown variables nh, sp, up, op, cp
pos = content.find("cp=`")
if pos != -1:
    snippet = content[max(0, pos-2000):pos+100]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Variables snippet before cp:\n", safe_snippet)
