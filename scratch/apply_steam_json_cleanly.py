import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read steam pachinko code
with open("scratch/build_steam_pachinko_component.py", "r", encoding="utf-8") as f:
    s = f.read()

idx1 = s.find('steam_pachinko_code = """') + 25
idx2 = s.rfind('"""\n\nwith open(')
if idx2 == -1: idx2 = s.rfind('"""\n\nprint("Steam')
steam_pachinko_code = s[idx1:idx2]

# Load old index (clean)
with open("scratch/old_index.html", "r", encoding="utf-16le") as f:
    content = f.read()

# Extract template
t_start = content.find('<script type="__bundler/template">\n') + len('<script type="__bundler/template">\n')
t_end = content.find('\n</script>', t_start)
template_json = content[t_start:t_end]

# Parse json
try:
    template_str = json.loads(template_json)
except Exception as e:
    print("Error parsing original template json:", e)
    sys.exit(1)

# Now do the replacement inside template_str
idx_start = template_str.find("function ip({")
idx_end = template_str.find("function Pa(c){", idx_start)

if idx_start != -1 and idx_end != -1:
    if template_str[idx_end-1] == '\n':
        idx_end -= 1
        
    print(f"Found idx_start: {idx_start}, idx_end: {idx_end}")
    
    # Replace in unescaped string
    new_template_str = template_str[:idx_start] + steam_pachinko_code + "\n" + template_str[idx_end+1:]
    
    # Convert back to JSON
    new_template_json = json.dumps(new_template_str)
    
    # Replace in main HTML
    new_content = content[:t_start] + new_template_json + content[t_end:]
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("[SUCCESS] Replaced ip component cleanly inside JSON string!")
else:
    print(f"Failed to find boundaries! start={idx_start}, end={idx_end}")
