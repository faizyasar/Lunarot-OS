index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

snippet = content[462000:473000]
safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')

with open(r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\aesthetic_tokens_window_code.js", "w", encoding="utf-8") as out:
    out.write(safe_snippet)

print(f"Saved aesthetic tokens code snippet (length {len(snippet)}) to scratch/aesthetic_tokens_window_code.js")
