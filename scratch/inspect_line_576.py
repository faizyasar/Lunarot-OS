import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for keywords in the JSX structure of the OS layout
keywords = ['BUILD', 'CONDUITS', 'INGRESS', 'SOCIALS', 'FAIZYASAR', 'faizyasar', 'vessel', 'chancellery', 'OCCULT']

for kw in keywords:
    matches = [m.start() for m in re.finditer(re.escape(kw), content, re.IGNORECASE)]
    print(f"Keyword '{kw}': {len(matches)} matches")
    for m in matches[:5]:
        snippet = content[max(0, m-80):min(len(content), m+120)]
        safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
        print(f"  Pos {m}: ...{safe_snippet}...")
