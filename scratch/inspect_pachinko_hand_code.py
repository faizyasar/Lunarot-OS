import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("public/sacred-pachinko.html", "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
if len(scripts) >= 5:
    s5 = scripts[4]
    print("=== SCRIPT 5 HAND CODE SEARCH ===")
    
    # Search for hand rendering or positioning statements
    matches = re.finditer(r'.{0,100}(?:hand|Hand|arm|Arm).{0,100}', s5)
    print("Sample hand statements:")
    for idx, m in enumerate(matches):
        if idx < 40:
            print(f"[{idx+1}]:", repr(m.group(0).strip()))

