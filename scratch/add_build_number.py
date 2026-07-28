import re
import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate mark-wrap logo rendering
old_logo_block = 's.jsx("div",{className:"mark-wrap",children:s.jsx("img",{className:"mark anim-fade-up",src:Y0,alt:"LUNAROT Logo"})})'

new_logo_block = 's.jsxs("div",{className:"mark-wrap flex flex-col items-center",children:[s.jsx("img",{className:"mark anim-fade-up",src:Y0,alt:"LUNAROT Logo"}),s.jsx("span",{className:"font-mono text-[9px] text-[#838aa0] tracking-[0.25em] uppercase mt-3 block text-center opacity-85 hover:opacity-100 transition-opacity select-none",children:"BUILD v6.1 // cac02eb"})]})'

if old_logo_block in content:
    content = content.replace(old_logo_block, new_logo_block)
    print("[SUCCESS] Added build number badge directly under front page logo in index.html")
else:
    print("[WARN] Could not find old_logo_block target")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] add_build_number script finished.")
