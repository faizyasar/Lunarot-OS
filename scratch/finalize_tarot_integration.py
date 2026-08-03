import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace pp component invocation for /db/tarot-directory.index with TarotStandaloneView
old_tarot_render = 'v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K})'
new_tarot_render = 'v==="/db/tarot-directory.index"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K})'

if old_tarot_render in content:
    content = content.replace(old_tarot_render, new_tarot_render)
    print("[SUCCESS] Swapped tarot-directory.index rendering to TarotStandaloneView")
else:
    print("[WARN] Could not find old_tarot_render pattern")

# Update window header titles switch case in xp()
old_header_switch = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;'
new_header_switch = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;case"/db/tarot-directory.index":K("SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER");break;case"/db/music.index":K("AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES");break;case"/db/deka-archive.index":K("DEKA DRIVE GALLERY // LIVE ASSET PREVIEWER");break;'

if old_header_switch in content:
    content = content.replace(old_header_switch, new_header_switch)
    print("[SUCCESS] Updated window header context titles")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

# Update public standalone copies
shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Successfully finalized Tarot Standalone Deck integration.")
