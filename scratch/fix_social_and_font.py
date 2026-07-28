import re
import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Define complete social-conduit string op
social_conduit_md = """# Social Conduits & Alchemical Channels

Direct channels to trace and establish connection with the vessel architect:

---

## ✦ Primary Vessels

*   **Julian Ingress (Github):** [github.com/faizyasar](https://github.com/faizyasar)
    *   *System depository containing code archives and developmental traces.*
*   **Architect Portal (Portfolio):** [faizyasar.life](https://faizyasar.life)
    *   *The general portfolio containing visual artifacts and system architecture.*
*   **Esoteric Art Portal:** [lnrtdka.drr.ac](https://lnrtdka.drr.ac/)
    *   *Visual system layouts, graphic design archives, and sacred illustrations.*
*   **Occupied Grid (LinkedIn):** [linkedin.com/in/faizyasar](https://linkedin.com/in/faizyasar)
    *   *Professional node alignment and graduate network index.*
*   **Inspiration Vault (Pinterest):** [pinterest.com/FaizYasar](https://au.pinterest.com/FaizYasar/)
    *   *Visual references, alchemical motifs, and graphic style-boards.*
*   **Arcade Tarot Conduit:** [tarot.drr.ac](https://tarot.drr.ac/)
    *   *Interactive web divination node.*
*   **Cinephile Transmission (Letterboxd):** [letterboxd.com/FaziLuvsYuo](https://letterboxd.com/FaziLuvsYuo/)
    *   *Film diary logs, ratings, and curated cinematic lists.*
*   **Cultural Curation (Perfectly Imperfect):** [pi.fyi/u/nofiazco](https://www.pi.fyi/u/nofiazco)
    *   *Personal taste profile and recommendations.*

---

## ✦ System Status
*   **Architect:** Faiz Yasar
*   **Host Network:** Sydney, Australia [100% Alignment]
*   **Integrity Verification:** verified signature stable
*   **Epoch Synchrony:** active"""

safe_op_js = social_conduit_md.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

# Check if op is in variables list before cp=`
if ',op=`' not in content:
    # Inject ,op=`...` right before ,cp=`
    content = content.replace('`,cp=`', f'`,op=`{safe_op_js}`,cp=`')
    print("[SUCCESS] Injected op= variable for social-conduit.md")

# 2. Fix font in dev log & research logs (remove font-mono from markdown container)
old_md_container = 'className:"flex-1 flex flex-col h-full w-full bg-black/35 backdrop-blur-[2px] border border-white/40 p-4 sm:p-6 overflow-y-auto font-mono text-justify"'
new_md_container = 'className:"flex-1 flex flex-col h-full w-full bg-black/35 backdrop-blur-[2px] border border-white/40 p-4 sm:p-6 overflow-y-auto leading-relaxed relative z-10 scrollbar-thin scrollbar-thumb-white/10 text-justify"'

if old_md_container in content:
    content = content.replace(old_md_container, new_md_container)
    print("[SUCCESS] Restored original font (removed forced font-mono) for dev log and research markdown containers")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] fix_social_and_font script finished.")
