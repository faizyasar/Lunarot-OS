import re

os54_path = r"C:\Users\faizy\Downloads\Lunarot-OS54.html"

with open(os54_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Locate script tags
scripts = re.findall(r'<script[^>]*>', content, re.IGNORECASE)
print("Script tags in OS54:")
for s_tag in scripts:
    print(s_tag)
