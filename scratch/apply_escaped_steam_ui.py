import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/build_steam_pachinko_component.py", "r", encoding="utf-8") as f:
    s = f.read()

idx1 = s.find('steam_pachinko_code = """') + 25
idx2 = s.rfind('"""\n\nwith open(')
if idx2 == -1: idx2 = s.rfind('"""\n\nprint("Steam')
steam_pachinko_code = s[idx1:idx2]

escaped_code = json.dumps(steam_pachinko_code)[1:-1]

with open("scratch/old_index.html", "r", encoding="utf-16le") as f:
    content = f.read()

idx_start = content.find("function ip({")
idx_end = content.find("function Pa(c){", idx_start)

if idx_start != -1 and idx_end != -1:
    prefix = content[idx_end-4:idx_end]
    print(f"Prefix before Pa: {repr(prefix)}")
    if prefix.endswith('\\n'):
        idx_end -= 2

    print(f"Found idx_start: {idx_start}, idx_end: {idx_end}")
    
    new_content = content[:idx_start] + escaped_code + "\\n" + content[idx_end:]
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("[SUCCESS] Replaced ip component with escaped code!")
else:
    print("Failed to find boundaries.")
