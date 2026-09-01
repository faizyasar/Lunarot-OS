import re
import sys

with open(r'C:\Users\faizy\Downloads\Lunarot_Tarot_Deck_-_Standalone.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# remove massive base64 textures for cleaner analysis
clean_preview = re.sub(r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+', 'data:image/...[BASE64]...', text)

with open('scratch/tarot_deck_preview.html', 'w', encoding='utf-8') as f:
    f.write(clean_preview)

print('Wrote clean preview to scratch/tarot_deck_preview.html, length:', len(clean_preview))

# Check DOM elements
body_match = re.search(r'<body[^>]*>(.*?)</body>', clean_preview, re.DOTALL)
if body_match:
    print('Body preview:')
    print(body_match.group(1)[:1500])
