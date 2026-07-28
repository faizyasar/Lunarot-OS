import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search around 535000 for useState definitions in the main OS component
pos = 535000
snippet = content[max(0, pos-1000):min(len(content), pos+1000)]
safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
print("Snippet around 535k:\n", safe_snippet[:1500])
