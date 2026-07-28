import re
import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace bullet item styling in rp() so list items use font-garamond
target_bullet = 'className:`flex items-start ${x?"ml-6 text-xs text-[#838aa0]":"ml-2 text-sm text-[#cfc9c0]"} my-1`'
garamond_bullet = 'className:`flex items-start ${x?"ml-6 text-xs text-[#838aa0]":"ml-2 text-sm font-garamond text-[#cfc9c0]"} my-1`'

if target_bullet in content:
    content = content.replace(target_bullet, garamond_bullet)
    print("[SUCCESS] Added font-garamond to rp() list items")
else:
    print("[WARN] target_bullet not found")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] apply_garamond_to_rp script finished.")
