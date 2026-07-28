import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

pos = content.find("CHANCELLERY OF THE VOID")
if pos != -1:
    snippet = content[max(0, pos-400):min(len(content), pos+800)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print("Lockscreen portal snippet:\n", safe_snippet)

pos_logo = content.find("LUNAROT")
while pos_logo != -1:
    snippet = content[max(0, pos_logo-100):min(len(content), pos_logo+300)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Match at {pos_logo}:\n{safe_snippet}\n")
    pos_logo = content.find("LUNAROT", pos_logo+1)
