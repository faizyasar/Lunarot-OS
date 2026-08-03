import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("function ip(")
if idx == -1:
    idx = content.find("ip=({")
if idx == -1:
    idx = content.find("ip=")

if idx != -1:
    print("=== PACHINKO COMPONENT ip IN INDEX.HTML ===")
    print(content[idx:idx+1500])
else:
    print("Component ip not found!")
