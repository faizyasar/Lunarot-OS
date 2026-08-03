import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("s.jsx(\\\"video\\\",{")
if idx != -1:
    print(content[idx+400:idx+1200])
