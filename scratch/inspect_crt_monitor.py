import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

pos = content.find("crt-monitor")
if pos != -1:
    snippet = content[max(0, pos-200):min(len(content), pos+1500)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print("CRT Monitor snippet:\n", safe_snippet)

# Search for CSS definitions of crt-monitor, crt-screen-glass, crt-scanlines, starfield, background video
for css_cls in [".crt-monitor", ".crt-screen-glass", ".crt-scanlines", "video", "webm", "background"]:
    p = content.find(css_cls)
    if p != -1:
        snip = content[p:p+300]
        safe_snip = snip.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
        print(f"\nCSS {css_cls}:\n{safe_snip}")
