import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("src:\\\"data:video/webm;base64,")
if idx != -1:
    end_idx = content.find("}\\\")", idx)
    if end_idx == -1:
        end_idx = content.find("})", idx)
    print("=== VIDEO TAG PROPERTIES ===")
    # search for className around video
    print(content[idx+240000:idx+255000])

