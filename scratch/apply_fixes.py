import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Revert inner window bottom-right element back to OCCULT_W3_DIG
old_inner_link = 's.jsx("a",{href:"https://faizyasar.life",target:"_blank",rel:"noreferrer",className:"absolute bottom-2 right-3 font-mono text-[9px] md:text-[10px] text-[#ef4444]/80 hover:text-white tracking-[0.2em] uppercase cursor-pointer z-30 transition-all underline decoration-dotted",children:"faizyasar.life"})'
new_inner_span = 's.jsx("span",{className:"absolute bottom-2 right-3 font-mono text-[6px] text-[#ef4444]/40 tracking-[0.2em] uppercase pointer-events-none",children:"OCCULT_W3_DIG"})'

if old_inner_link in content:
    content = content.replace(old_inner_link, new_inner_span)
    print("[SUCCESS] Reverted inner window bottom-right back to OCCULT_W3_DIG")
else:
    print("[WARN] Inner link target not found, checking alternative")

# 2. Update vp array (sidebar folder structure)
old_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📄"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📄"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📄"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"📁"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

new_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📄"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📜"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📡"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"🎴"},{name:"music.index",path:"/db/music.index",icon:"🎵"},{name:"deka-archive.index",path:"/db/deka-archive.index",icon:"🖼️"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

if old_vp in content:
    content = content.replace(old_vp, new_vp)
    print("[SUCCESS] Updated vp array with music.index and deka-archive.index in database folder")
else:
    print("[WARN] Could not find old_vp target")

# 3. Update switch(v) to handle /db/music.index and /db/deka-archive.index
old_switch = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;'
new_switch = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;case"/db/music.index":K("AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES");g("music");break;case"/db/deka-archive.index":K("DEKA DRIVE GALLERY // LIVE ASSET PREVIEWER");g("deka");break;'

if old_switch in content:
    content = content.replace(old_switch, new_switch)
    print("[SUCCESS] Added switch cases for /db/music.index and /db/deka-archive.index")
else:
    print("[WARN] Could not find old_switch target")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] Script finished.")
