import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("src:\\\"data:video/webm;base64,")
if idx == -1:
    idx = content.find("data:video/webm;base64,")

if idx != -1:
    print("=== BACKGROUND VIDEO ELEMENT IN INDEX.HTML ===")
    print(content[idx-300:idx+400])

