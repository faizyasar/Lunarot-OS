import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

m_tag = 'script type="__bundler/template"'
pos = text.find(m_tag)
s = text.find('>', pos) + 1

# Everything before s is the outer template JSON string
# Let's inspect the first script tag before template string
# In fact, let's escape double quotes inside TarotStandaloneView definition!

old_comp = 'function TarotStandaloneView({onUpdateActivePlanets:c,onContextChange:E}){const[g,f]=D.useState(null);return D.useEffect(()=>{g&&E?E(`${g.cardName.toUpperCase()} // ${g.trad.toUpperCase()}`):E&&E("SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER")},[g,E]),D.useEffect(()=>{const h=e=>{e.data&&e.data.type==="LUNAROT_TAROT_INSPECT"?(f(e.data),c&&e.data.cardName&&c(new Set(Ko[e.data.cardName]||[]))):e.data&&e.data.type==="LUNAROT_TAROT_DESELECT"&&(f(null),c&&c(new Set()))};return window.addEventListener("message",h),()=>window.removeEventListener("message",h)},[c]),s.jsx("div",{className:"flex-1 flex flex-col h-full w-full bg-black/40 relative z-25 overflow-hidden",children:s.jsx("iframe",{src:"/tarot-standalone.html",className:"w-full h-full border-0 relative z-10",title:"Lunarot 3D Tarot Deck Standalone"})})}'

# Escape quotes with backslashes so it stays valid inside double-quoted JSON string
escaped_comp = old_comp.replace('"', '\\"')

if old_comp in text:
    text = text.replace(old_comp, escaped_comp)
    print("[SUCCESS] Escaped quotes inside TarotStandaloneView definition!")
else:
    print("[WARN] Could not find unescaped old_comp")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(text)

# Update all standalone copies
shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Done.")
