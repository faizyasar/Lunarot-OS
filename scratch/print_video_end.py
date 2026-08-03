import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("src:\\\"data:video/webm;base64,")
if idx != -1:
    print("=== END OF VIDEO TAG ===")
    print(content[idx+200000:idx+200800])

