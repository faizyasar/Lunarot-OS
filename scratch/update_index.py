import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Letterboxd and Perfectly Imperfect to social section
old_social = """*   **Inspiration Vault (Pinterest):** [pinterest.com/FaizYasar](https://au.pinterest.com/FaizYasar/)
    *   *Visual references, alchemical motifs, and graphic style-boards.*"""

new_social = """*   **Inspiration Vault (Pinterest):** [pinterest.com/FaizYasar](https://au.pinterest.com/FaizYasar/)
    *   *Visual references, alchemical motifs, and graphic style-boards.*
*   **Cinephile Vault (Letterboxd):** [letterboxd.com/FaziLuvsYuo](https://letterboxd.com/FaziLuvsYuo/)
    *   *Film diary, cinematic telemetry, and curated list archives.*
*   **Perfectly Imperfect Node:** [pi.fyi/u/nofiazco](https://www.pi.fyi/u/nofiazco)
    *   *Taste logs, cultural fragments, and raw recommendations.*"""

if old_social in content:
    content = content.replace(old_social, new_social)
    print("[SUCCESS] Added Letterboxd and Perfectly Imperfect to Socials")
else:
    print("[WARN] Could not find old_social target")

# 2. Update tabs list to include "music"
old_tabs = '["log","map","dev","deka","social"].map('
new_tabs = '["log","map","dev","deka","social","music"].map('
if old_tabs in content:
    content = content.replace(old_tabs, new_tabs)
    print("[SUCCESS] Updated tabs list to include music")
else:
    print("[WARN] Could not find old_tabs target")

# 3. Update tab titles in navigation bar
old_nav_labels = 'C==="dev"?"📜 DEV-HISTORY.MD":"📡 SOCIAL-CONDUIT.MD"'
new_nav_labels = 'C==="dev"?"📜 DEV-HISTORY.MD":C==="music"?"🎵 MUSIC-CONDUIT.MD":"📡 SOCIAL-CONDUIT.MD"'
if old_nav_labels in content:
    content = content.replace(old_nav_labels, new_nav_labels)
    print("[SUCCESS] Updated nav labels for music tab")
else:
    print("[WARN] Could not find old_nav_labels target")

# 4. Make bottom-right OCCULT_W3_DIG clickable or replace with faizyasar.life link
old_footer_span = 's.jsx("span",{className:"absolute bottom-2 right-3 font-mono text-[6px] text-[#ef4444]/40 tracking-[0.2em] uppercase pointer-events-none",children:"OCCULT_W3_DIG"})'
new_footer_span = 's.jsx("a",{href:"https://faizyasar.life",target:"_blank",rel:"noreferrer",className:"absolute bottom-2 right-3 font-mono text-[9px] md:text-[10px] text-[#ef4444]/80 hover:text-white tracking-[0.2em] uppercase cursor-pointer z-30 transition-all underline decoration-dotted",children:"faizyasar.life"})'

if old_footer_span in content:
    content = content.replace(old_footer_span, new_footer_span)
    print("[SUCCESS] Made bottom-right corner faizyasar.life clickable link")
else:
    print("[WARN] Could not find old_footer_span target")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] Script finished.")
