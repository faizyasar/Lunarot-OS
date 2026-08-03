import os
import shutil

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")
public_dir = os.path.join(root_dir, "public")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# single line minify of TarotStandaloneView definition
old_comp = '''function TarotStandaloneView({onUpdateActivePlanets:c,onContextChange:E}){
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

new_comp = 'function TarotStandaloneView({onUpdateActivePlanets:c,onContextChange:E}){const[g,f]=D.useState(null);return D.useEffect(()=>{g&&E?E(`${g.cardName.toUpperCase()} // ${g.trad.toUpperCase()}`):E&&E("SACRED TAROT DECK // 78 CONDUITS 3D EXPLORER")},[g,E]),D.useEffect(()=>{const h=e=>{e.data&&e.data.type==="LUNAROT_TAROT_INSPECT"?(f(e.data),c&&e.data.cardName&&c(new Set(Ko[e.data.cardName]||[]))):e.data&&e.data.type==="LUNAROT_TAROT_DESELECT"&&(f(null),c&&c(new Set()))};return window.addEventListener("message",h),()=>window.removeEventListener("message",h)},[c]),s.jsx("div",{className:"flex-1 flex flex-col h-full w-full bg-black/40 relative z-25 overflow-hidden",children:s.jsx("iframe",{src:"/tarot-standalone.html",className:"w-full h-full border-0 relative z-10",title:"Lunarot 3D Tarot Deck Standalone"})})}'

if old_comp in content:
    content = content.replace(old_comp, new_comp)
    print("[SUCCESS] Replaced multiline TarotStandaloneView with single-line minified version")
else:
    print("[WARN] Multiline component string not found directly, stripping literal newlines...")
    # fallback: replace literal newlines in the component definition
    pos = content.find('function TarotStandaloneView')
    if pos != -1:
        end_pos = content.find('}\nfunction xp()', pos)
        if end_pos == -1:
            end_pos = content.find('}function xp()', pos)
        if end_pos != -1:
            old_slice = content[pos:end_pos+1]
            content = content.replace(old_slice, new_comp)
            print("[SUCCESS] Replaced TarotStandaloneView definition")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

# Update all standalone copies
shutil.copyfile(index_path, os.path.join(root_dir, "Lunarot-OS-LATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "osLATEST.html"))
shutil.copyfile(index_path, os.path.join(public_dir, "Lunarot-OS.html"))

print("[COMPLETE] Updated all standalone files.")
