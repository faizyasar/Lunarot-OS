import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the heading and group under ## ✦ 2026 umbrella
old_header = "## ✦ Git Repository Commits Trace"
new_header = "## ✦ 2026"

if old_header in content:
    content = content.replace(old_header, new_header)
    print("[SUCCESS] Replaced header with 2026 umbrella")

# Replace ### ✦ DD/MM/2026 with ### DD/MM/2026
content = re.sub(r'### ✦ (\d\d/\d\d/2026)', r'### \1', content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] Umbrella script finished.")
