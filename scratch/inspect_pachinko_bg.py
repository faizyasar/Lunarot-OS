import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== PUBLIC/SACRED-PACHINKO.HTML ===")
with open("public/sacred-pachinko.html", "r", encoding="utf-8") as f:
    p1 = f.read()

print("Length:", len(p1))
print("First 1000 chars:")
print(p1[:1000])

print("\nSearch background in public/sacred-pachinko.html:")
for line in p1.split('\n')[:50]:
    if 'background' in line or 'body' in line or 'video' in line or 'canvas' in line:
        print("  ", line.strip())

