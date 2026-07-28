import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's restore index.html from git if needed, or fix the space-y-1 block cleanly
# Let's inspect from touchStart to the end of the div
start_pos = content.find('onTouchStart:$,onTouchEnd:ve,children:s.jsxs("div",{className:"space-y-1"')
end_pos = content.find('f&&s.jsxs("div",{className:`fixed inset-0 bg-black/95')

if start_pos != -1 and end_pos != -1:
    print(f"Start pos: {start_pos}, End pos: {end_pos}")
    snippet = content[start_pos:end_pos]
    # Let's print the last 200 chars of snippet
    safe_end = snippet[-200:].encode('ascii', errors='replace').decode('ascii')
    print("Snippet end:\n", safe_end)
