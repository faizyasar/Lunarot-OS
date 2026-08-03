import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("public/sacred-pachinko.html", "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
print(f"Found {len(scripts)} scripts in sacred-pachinko.html")

for idx, s in enumerate(scripts):
    print(f"\n--- SCRIPT {idx+1} (length {len(s)}) ---")
    # Search for left/right positioning or skeleton/hand variables
    for term in ['hand', 'arm', 'left', 'right', 'skeleton', 'fire', 'board', 'canvas']:
        count = len(re.findall(term, s, re.IGNORECASE))
        if count > 0:
            print(f"  Term '{term}': {count} occurrences")

