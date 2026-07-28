import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for letterboxd or instagram or twitter variable
for m in re.finditer(r'letterboxd\.com', content, re.IGNORECASE):
    idx = m.start()
    snippet = content[max(0, idx-100):min(len(content), idx+200)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Match at {idx}: {safe_snippet}")
