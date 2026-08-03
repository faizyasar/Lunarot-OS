import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("=== SEARCH FOR PACHINKO IN INDEX.HTML ===")
idx = content.find("pachinko")
while idx != -1:
    print(content[max(0, idx-100):min(len(content), idx+200)])
    idx = content.find("pachinko", idx+1)

print("\n=== PUBLIC/SACRED-PACHINKO.HTML HEAD / BACKGROUND SEARCH ===")
with open("public/sacred-pachinko.html", "r", encoding="utf-8") as f:
    p_content = f.read()
print(p_content[:1500])
