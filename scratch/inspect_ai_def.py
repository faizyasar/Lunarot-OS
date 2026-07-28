import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate ai component definition
pos = content.find("function ai(")
if pos != -1:
    snippet = content[pos:pos+1500]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Function ai definition:\n", safe_snippet)
else:
    # Try finding const ai = or similar
    matches = [m.start() for m in re.finditer(r'\bai\b', content)]
    print(f"Total ai matches: {len(matches)}")
    for m in matches[20:30]:
        snippet = content[max(0, m-50):min(len(content), m+150)]
        safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
        print(f"Match at {m}: {safe_snippet}")
