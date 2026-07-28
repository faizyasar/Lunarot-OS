import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for where v is handled and where tabs are rendered
for m in re.finditer(r'rp\(Ve\(\)\)', content):
    idx = m.start()
    snippet = content[max(0, idx-200):min(len(content), idx+500)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Match at {idx}:\n{safe_snippet}\n")
