import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# Replace <title>My Google AI Studio App</title> or any generic <title>
old_title_pattern = r'<title>.*?</title>'
new_title = '<title>LUNAROT OS</title>'

if re.search(old_title_pattern, idx_content):
    idx_content = re.sub(old_title_pattern, new_title, idx_content, count=1)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("[SUCCESS] Updated title in index.html to 'LUNAROT OS'!")
else:
    print("[WARN] <title> tag not found in index.html")

# 2. Update public/sacred-pachinko.html and public/pachinko.html
for p_file in ["public/sacred-pachinko.html", "public/pachinko.html"]:
    if os.path.exists(p_file):
        with open(p_file, "r", encoding="utf-8") as f:
            p_content = f.read()
        
        p_content = re.sub(r'<title>.*?</title>', '<title>Sacred Pachinko // Lunarot OS</title>', p_content, count=1)
        with open(p_file, "w", encoding="utf-8") as f:
            f.write(p_content)
        print(f"[SUCCESS] Updated title in {p_file} to 'Sacred Pachinko // Lunarot OS'!")

