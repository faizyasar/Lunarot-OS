import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for background elements in index.html
print("=== SEARCH FOR BACKGROUND VIDEO / CANVAS IN INDEX.HTML ===")
for term in ["crtVideo", "crt-bg", "video", "webm", "poster", "canvas"]:
    pos = 0
    while True:
        idx = content.find(term, pos)
        if idx == -1:
            break
        print(f"[{term} at {idx}]:", repr(content[max(0, idx-60):min(len(content), idx+140)]))
        pos = idx + len(term) + 20

