import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/build_steam_pachinko_component.py", "r", encoding="utf-8") as f:
    s = f.read()

idx1 = s.find('steam_pachinko_code = """') + 25
idx2 = s.rfind('"""\n\nwith open(')
if idx2 == -1: idx2 = s.rfind('"""\n\nprint("Steam')
steam_pachinko_code = s[idx1:idx2]

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx_start = content.find("function ip({")
idx_end = content.find("function Pa(c){", idx_start)

if idx_start != -1 and idx_end != -1:
    # Subtract 1 from idx_end to capture the newline if it exists
    if content[idx_end-1] == '\n':
        idx_end -= 1
        
    print(f"Found idx_start: {idx_start}")
    print(f"Found idx_end: {idx_end}")
    
    # We replace from idx_start to idx_end
    new_content = content[:idx_start] + steam_pachinko_code + "\n" + content[idx_end+1:]
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("[SUCCESS] Replaced ip component cleanly!")
else:
    print(f"Failed to find boundaries! start={idx_start}, end={idx_end}")
