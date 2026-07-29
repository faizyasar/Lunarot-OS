import re
import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"
target_latest = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\Lunarot-OS-LATEST.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate <noscript>...</noscript> inside <head>
noscript_pattern = r'(<head.*?>.*?)(<noscript>.*?</noscript>)'
match = re.search(noscript_pattern, content, re.DOTALL)

if match:
    noscript_block = match.group(2)
    # Remove from head
    content = content.replace(noscript_block, "", 1)
    # Move after <body>
    content = content.replace("<body>", f"<body>\n  {noscript_block}\n", 1)
    print("[SUCCESS] Moved <noscript> block from <head> to <body>")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

with open(target_latest, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] fix_noscript script finished.")
