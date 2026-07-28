import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate the dev history block starting with ### ✦ 16/07/2026
pattern = r'(### ✦ 16/07/2026.*?\*   `\[Lunarot-Tarot-old:41ca5c2\]` Update index\.html)'
match = re.search(pattern, content, re.DOTALL)

if match:
    raw_block = match.group(1)
    
    # Wrap all 2026 entries under one 2026 umbrella
    umbrella_header = "# ✦ 2026\n\n"
    # Replace ### ✦ DD/MM/2026 with ## DD/MM/2026 under the 2026 umbrella
    updated_block = raw_block.replace("### ✦ ", "## ")
    
    final_log_section = umbrella_header + updated_block
    content = content.replace(raw_block, final_log_section)
    print("[SUCCESS] Wrapped 2026 log under single # ✦ 2026 umbrella in index.html")
else:
    print("[WARN] Could not find dev history block match in index.html")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] 2026 umbrella script finished.")
