import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Define single-line TarotStandaloneView (with escaped double quotes for JSON string compatibility)
tarot_iframe_component = 'function TarotStandaloneView({onUpdateActivePlanets:c,onContextChange:E}){const[g,f]=D.useState(null);return D.useEffect(()=>{g&&E?E(`${g.cardName.toUpperCase()} // ${g.trad.toUpperCase()}`):E&&E(\\"SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER\\")},[g,E]),D.useEffect(()=>{const h=e=>{e.data&&e.data.type===\\"LUNAROT_TAROT_INSPECT\\"?(f(e.data),c&&e.data.cardName&&c(new Set(Ko[e.data.cardName]||[]))):e.data&&e.data.type===\\"LUNAROT_TAROT_DESELECT\\"&&(f(null),c&&c(new Set()))};return window.addEventListener(\\"message\\",h),()=>window.removeEventListener(\\"message\\",h)},[c]),s.jsx(\\"div\\",{className:\\"flex-1 flex flex-col h-full w-full bg-black/40 relative z-25 overflow-hidden\\",children:s.jsx(\\"iframe\\",{src:\\"/tarot-standalone.html\\",className:\\"w-full h-full border-0 relative z-10\\",title:\\"Lunarot 3D Tarot Deck Standalone\\"})})}'

if 'function xp()' in content:
    content = content.replace('function xp()', tarot_iframe_component + 'function xp()')
    print("[SUCCESS] Inserted TarotStandaloneView component into Build 671339")
else:
    print("[ERROR] function xp() not found")

# 2. Swap tarot-directory.index render hook in xp()
old_tarot_render = 'v===\\"/db/tarot-directory.index\\"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K})'
new_tarot_render = 'v===\\"/db/tarot-directory.index\\"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K})'

if old_tarot_render in content:
    content = content.replace(old_tarot_render, new_tarot_render)
    print("[SUCCESS] Swapped tarot-directory.index render hook to TarotStandaloneView")
else:
    print("[WARN] Could not find exact old_tarot_render string")

# 3. Add header title switch case in xp()
old_header_case = 'case\\"/db/music.index\\":K(\\"AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES\\");break;'
new_header_case = 'case\\"/db/tarot-directory.index\\":K(\\"SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER\\");break;case\\"/db/music.index\\":K(\\"AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES\\");break;'

if old_header_case in content:
    content = content.replace(old_header_case, new_header_case)
    print("[SUCCESS] Added header switch case for tarot-directory.index")

# Save updated index.html
with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

# Sync all copies
shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Build 671339 successfully patched with 3D Standalone Tarot Deck.")
