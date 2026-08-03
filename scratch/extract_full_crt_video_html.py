import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("src:\\\"data:video/webm;base64,")
if idx != -1:
    end = content.find("})", idx)
    print("=== EXTRACTED VIDEO HTML ATTRIBUTES ===")
    print("Start:", idx)
    print("End:", end)
    print(content[idx-150:idx+80])

