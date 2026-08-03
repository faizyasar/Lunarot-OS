import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("function ip({")
if idx == -1:
    idx = content.find("ip=({")

if idx != -1:
    print("=== FULL ip COMPONENT DEFINITION ===")
    print(content[idx:idx+3500])

