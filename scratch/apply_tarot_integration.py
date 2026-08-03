import os
import re

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. New TarotStandaloneComponent to replace old pp component rendering or to be called inside pp
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

# Insert TarotStandaloneView before function xp()
if 'function xp()' in content:
    content = content.replace('function xp()', tarot_iframe_component + '\nfunction xp()')
    print("[SUCCESS] Inserted TarotStandaloneView component")
else:
    print("[ERROR] Could not find function xp()")

# Update xp rendering to call TarotStandaloneView for tarot-directory.index
old_tarot_render = 'v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K})'
new_tarot_render = 'v==="/db/tarot-directory.index"&&s.jsx(TarotStandaloneView,{onUpdateActivePlanets:Y,onContextChange:K})'

if old_tarot_render in content:
    content = content.replace(old_tarot_render, new_tarot_render)
    print("[SUCCESS] Swapped tarot-directory.index rendering to TarotStandaloneView")
else:
    print("[WARN] Could not find old_tarot_render pattern")

# Update header title switch in xp() for tarot-directory.index
old_header_case = 'case"/db/tarot-directory.index":'
if old_header_case not in content:
    # Append tarot-directory.index title handling into header switch
    old_sw_case = 'case"/db/music.index":K("AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES");break;'
    new_sw_case = 'case"/db/tarot-directory.index":K("SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER");break;case"/db/music.index":K("AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES");break;'
    if old_sw_case in content:
        content = content.replace(old_sw_case, new_sw_case)
        print("[SUCCESS] Added header title switch for tarot-directory.index")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

# Update public/osLATEST.html and public/Lunarot-OS.html and Lunarot-OS-LATEST.html
shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Updated index.html and all standalone copies with 3D Standalone Tarot Deck integration.")
