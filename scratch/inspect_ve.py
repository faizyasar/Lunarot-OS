import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for Ve definition or usage
for m in re.finditer(r'Ve\s*=\s*\(\)\s*=>', content):
    idx = m.start()
    snippet = content[max(0, idx-50):min(len(content), idx+500)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Ve definition at {idx}:\n{safe_snippet}\n")
