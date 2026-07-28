index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

pos = 6724679
snippet = content[max(0, pos-400):min(len(content), pos+400)]
safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
print("--- BOTTOM BAR SNIPPET ---")
print(safe_snippet)
