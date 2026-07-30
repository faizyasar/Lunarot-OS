import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Search for webm, video, bg, or monitor elements in index.html
videos = re.findall(r'<video[^>]+>', content, re.IGNORECASE)
print("Video tags in index.html:")
for v in videos:
    print(v)

# Search for video src URLs
video_srcs = re.findall(r'src="[^"]*\.webm[^"]*"', content, re.IGNORECASE)
if not video_srcs:
    video_srcs = re.findall(r'https://[^"]+\.webm', content, re.IGNORECASE)

print("\nWebM URLs in index.html:")
for s in video_srcs:
    print(s)

# Search for monitor, CRT, or scanline CSS/JSX elements
matches = [m.start() for m in re.finditer(r'monitor|scanline|crt|vessel-bg|starfield', content, re.IGNORECASE)]
print(f"\nMonitor/FX keywords found: {len(matches)}")
for m in matches[:10]:
    snippet = content[max(0, m-50):min(len(content), m+150)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Match at {m}: {safe_snippet}")
