import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("public/sacred-pachinko.html", "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
if len(scripts) >= 5:
    s5 = scripts[4]
    print("=== MAIN HAND JS REFERENCES IN SCRIPT 5 ===")
    
    matches = re.finditer(r'.{0,100}(?:mainLeftHand|mainRightHand).{0,100}', s5)
    for idx, m in enumerate(matches):
        print(f"[{idx+1}]:", repr(m.group(0).strip()))

