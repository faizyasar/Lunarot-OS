import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate where v === "/db/music.index" is in index.html
pos = content.find('v==="/db/music.index"')
if pos != -1:
    snippet = content[max(0, pos-200):min(len(content), pos+600)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Match at {pos}:\n{safe_snippet}\n")
else:
    print("v===/db/music.index not found")

# Locate where v === "/db/deka-archive.index" is in index.html
pos_deka = content.find('v==="/db/deka-archive.index"')
if pos_deka != -1:
    snippet_deka = content[max(0, pos_deka-200):min(len(content), pos_deka+600)]
    safe_snippet_deka = snippet_deka.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Match at {pos_deka}:\n{safe_snippet_deka}\n")
else:
    print("v===/db/deka-archive.index not found")
