import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("public/sacred-pachinko.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for hand references
print("=== HAND REFERENCES IN SACRED PACHINKO ===")
matches = [line.strip() for line in content.split('\n') if any(k in line.lower() for k in ['hand', 'arm', 'fireleft', 'fireright', 'left_hand', 'righthand'])]

print(f"Found {len(matches)} matching lines:")
for m in matches[:40]:
    if len(m) < 160:
        print("  ", m)

