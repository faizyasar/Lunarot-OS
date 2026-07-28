import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for logon or lockscreen rendering block
pos = content.find("LUNAROT OS")
while pos != -1:
    snippet = content[max(0, pos-200):min(len(content), pos+400)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Match at {pos}:\n{safe_snippet}\n")
    pos = content.find("LUNAROT OS", pos+1)
