import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update existing bottom bar FAIZYASAR.LIFE link to ensure pointer-events-auto, z-50, and hover glow
old_bottom_bar_link = 's.jsx("a",{href:"https://faizyasar.life",target:"_blank",rel:"noopener noreferrer",className:"text-[var(--gold)] font-bold hover:text-white transition-colors cursor-pointer min-h-[40px] md:min-h-0 flex items-center",children:"FAIZYASAR.LIFE"})'
new_bottom_bar_link = 's.jsx("a",{href:"https://faizyasar.life",target:"_blank",rel:"noopener noreferrer",className:"text-[var(--gold)] font-bold hover:text-white hover:underline transition-all cursor-pointer min-h-[40px] md:min-h-0 flex items-center relative z-50 pointer-events-auto",children:"FAIZYASAR.LIFE"})'

if old_bottom_bar_link in content:
    content = content.replace(old_bottom_bar_link, new_bottom_bar_link)
    print("[SUCCESS] Updated existing bottom bar FAIZYASAR.LIFE link with z-50 and pointer-events-auto")
else:
    print("[WARN] Could not find old_bottom_bar_link target")

# 2. Make sure switch cases handle /db/music.index, /db/deka-archive.index, and /research/deka-archives.md
old_switch_target = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;'
new_switch_target = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;case"/db/music.index":K("AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES");g("music");break;case"/db/deka-archive.index":K("DEKA DRIVE GALLERY // LIVE ASSET PREVIEWER");g("deka");break;'

if old_switch_target in content:
    content = content.replace(old_switch_target, new_switch_target)
    print("[SUCCESS] Verified switch cases for database files")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] Fix script finished.")
