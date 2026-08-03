import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update vp array in sidebar if needed (or verify tarot-directory.index is present)
old_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📄"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📄"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📄"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"📁"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

new_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📜"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📜"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📡"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"🎴"},{name:"music.index",path:"/db/music.index",icon:"🎵"},{name:"deka-archive.index",path:"/db/deka-archive.index",icon:"🖼️"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

if old_vp in content:
    content = content.replace(old_vp, new_vp)
    print("[SUCCESS] Updated vp array")

# 2. Add TarotStandaloneView definition before function xp()
tarot_iframe_component = '''function TarotStandaloneView({onUpdateActivePlanets:c,onContextChange:E}){
  const [activeCard, setActiveCard] = D.useState(null);

  D.useEffect(()=>{
    if(activeCard && E) {
      E(`${activeCard.cardName.toUpperCase()} // ${activeCard.trad.toUpperCase()}`);
    } else if(E) {
      E("SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER");
    }
  }, [activeCard, E]);

  D.useEffect(()=>{
    const handleMsg = (e) => {
      if(e.data && e.data.type === "LUNAROT_TAROT_INSPECT") {
        setActiveCard(e.data);
        if(c && e.data.cardName) {
          const astroMap = Ko[e.data.cardName] || [];
          c(new Set(astroMap));
        }
      } else if(e.data && e.data.type === "LUNAROT_TAROT_DESELECT") {
        setActiveCard(null);
        if(c) c(new Set());
      }
    };
    window.addEventListener("message", handleMsg);
    return () => window.removeEventListener("message", handleMsg);
  }, [c]);

  return s.jsx("div", {
    className: "flex-1 flex flex-col h-full w-full bg-black/40 relative z-25 overflow-hidden",
    children: s.jsx("iframe", {
      src: "/tarot-standalone.html",
      className: "w-full h-full border-0 relative z-10",
      title: "Lunarot 3D Tarot Deck Standalone"
    })
  });
}'''

if 'function xp()' in content:
    content = content.replace('function xp()', tarot_iframe_component + '\nfunction xp()')
    print("[SUCCESS] Inserted TarotStandaloneView component")

# 3. Swap tarot-directory.index render hook
old_tarot_hook = 'v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K})'
new_tarot_hook = 'v==="/db/tarot-directory.index"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K})'

if old_tarot_hook in content:
    content = content.replace(old_tarot_hook, new_tarot_hook)
    print("[SUCCESS] Swapped tarot render hook")
else:
    print("[WARN] Could not find exact old_tarot_hook, searching regex...")
    import re
    m = re.search(r'v==="/db/tarot-directory\.index"&&s\.jsx\([^,]+,', content)
    if m:
        content = content.replace(m.group(0), 'v==="/db/tarot-directory.index"&&s.jsx(TarotStandaloneView,')
        print("[SUCCESS] Swapped tarot render hook via regex")

# Write to file
with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

# Update all standalone copies
shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Clean patch applied.")
