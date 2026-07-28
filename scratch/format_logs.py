import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"
history_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\public\history.html"
changelog_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\CHANGELOG.md"

# 1. Process index.html dev-history log
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# We look for the dev-history log block in index.html starting with *   **2026-07-16**
pattern = r'(\*\s+\*\*2026-\d\d-\d\d\*\*.*?\n(?=\n###|\n#|`,op=))'
log_match = re.search(r'(\*\s+\*\*2026-07-16\*\*.*?\*   \*\*2026-06-16\*\*  -  \\`\[Lunarot-Tarot-old:41ca5c2\]\\` Update index\.html)', content, re.DOTALL)

if log_match:
    raw_log = log_match.group(1)
    
    # Parse lines
    lines = raw_log.strip().split('\n')
    grouped = {}
    
    for line in lines:
        m = re.match(r'\*\s+\*\*(\d{4})-(\d{2})-(\d{2})\*\*\s+-\s+(.*)', line.strip())
        if m:
            yyyy, mm, dd, item = m.groups()
            dmy = f"{dd}/{mm}/{yyyy}"
            if dmy not in grouped:
                grouped[dmy] = []
            grouped[dmy].append(item)
    
    # Rebuild stylish combined markdown
    new_log_blocks = []
    for dmy, items in grouped.items():
        block = f"### ✦ {dmy}\n"
        for item in items:
            block += f"*   {item}\n"
        new_log_blocks.append(block.strip())
    
    formatted_log = "\n\n".join(new_log_blocks)
    
    content = content.replace(raw_log, formatted_log)
    print("[SUCCESS] Combined and formatted log in index.html to D/M/Y format")
else:
    print("[WARN] Raw log pattern not matched in index.html")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

# 2. Update CHANGELOG.md dates YYYY-MM-DD -> DD/MM/YYYY
with open(changelog_path, "r", encoding="utf-8") as f:
    cl_content = f.read()

def convert_date(match):
    yyyy, mm, dd = match.group(1), match.group(2), match.group(3)
    return f"{dd}/{mm}/{yyyy}"

cl_content = re.sub(r'(\d{4})-(\d{2})-(\d{2})', convert_date, cl_content)

with open(changelog_path, "w", encoding="utf-8") as f:
    f.write(cl_content)
print("[SUCCESS] Converted dates in CHANGELOG.md to D/M/Y")

# 3. Update public/history.html dates YYYY-MM-DD -> DD/MM/YYYY
with open(history_path, "r", encoding="utf-8") as f:
    h_content = f.read()

h_content = re.sub(r'(\d{4})-(\d{2})-(\d{2})', convert_date, h_content)

with open(history_path, "w", encoding="utf-8") as f:
    f.write(h_content)
print("[SUCCESS] Converted dates in public/history.html to D/M/Y")

print("[COMPLETE] Log formatting complete.")
