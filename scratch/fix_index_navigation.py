import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. New dev history string `up` formatted under [year] / [day-month] / content
new_up_string = """# ✦ DEV HISTORY CHRONICLES

# ✦ 2026

## 29/07
*   `[lunarot-os:4006ef0]` feat: add music conduit tab, boy harsher lastfm stats, letterboxd and pi.fyi links
*   `[lunarot-os:9b6d2de]` fix: place music.index and deka-archive.index under database, fix bottom bar faizyasar.life link

## 28/07
*   `[lunarot-os:0930e5c]` feat: group logs in D/M/Y format, restore sacred pachinko routes and database folders

## 26/07
*   `[lunarot-os:0.9.0]` Static serve routing for osLATEST.html and pachinkoLATEST.html

## 24/07
*   `[lunarot-os:0.5.0]` Integrated Sacred Pachinko 3 standalone build and single-file HTML bundler configuration

## 16/07
*   `[lunarot-os:5419300]` Update compiled lunarot-os.html bundle
*   `[lunarot-os:6f15070]` Standardize header nav tabs to use index.css .nav-btn classes
*   `[lunarot-os:ef68893]` Restore header nav selectors (tabs) and sync active card stack highlights
*   `[lunarot-os:c329e32]` Add standalone lunarot-os-2.html copy-paste template
*   `[lunarot-os:0bfa55a]` Optimise backgrounds rendering inside lunarot-os.html
*   `[lunarot-os:b75566a]` Update main README and submodules refs
*   `[lunarot-os:fc43333]` Update submodule references to optimised versions
*   `[lunarot-os:6b4d650]` Sync Lunarot OS with standalone shell updates
*   `[Lunarot-Directory:b916d0a]` Update README with humanised details
*   `[Lunarot-Directory:f34f636]` Optimise background rendering and add OS components
*   `[Lunarot-Pachinko:4952232]` Update README with humanised details
*   `[Lunarot-Pachinko:48ab910]` Optimise background rendering and add OS components
*   `[Lunarot-Tarot:cd0cb99]` Update README with humanised details
*   `[Lunarot-Tarot:ef84c65]` Optimise background rendering and add OS components

## 26/06
*   `[Lunarot-Directory:bf9b7d0]` docs: update metadata and README for alchemical style

## 25/06
*   `[Lunarot-Directory:4df590f]` feat: scaffold Lunarot Tarot application
*   `[Lunarot-Directory:6f5e4fb]` Initial commit

## 24/06
*   `[Lunarot-Ankoku:062bb3f]` Update README.md structure formatting
*   `[Lunarot-Ankoku:3386a82]` Edit README for improved readability and expression
*   `[Lunarot-Ankoku:1baf135]` initial research log
*   `[Lunarot-Pachinko:1d84b6c]` Using the same aesthetic as Lunarot Tarot Engine
*   `[Lunarot-Pachinko:6f4ea31]` Initial commit
*   `[Lunarot-Tarot-old:d4c82f7]` Add deprecation notice and point users to Lunarot-Tarot-Engine-1.0

## 23/06
*   `[Lunarot-Tarot-old:7c1080c]` Merge pull request #1 from faizyasar/copilot/make-repo-crawlable
*   `[Lunarot-Tarot-old:44eda96]` Enhance sitemap metadata
*   `[Lunarot-Tarot-old:f55c7ba]` Add crawlability metadata, robots, and sitemap

## 20/06
*   `[Lunarot-Tarot:afc11be]` chore: generate package-lock.json for project dependencies

## 19/06
*   `[Lunarot-Tarot:89e7f18]` Update README.md

## 17/06
*   `[Lunarot-Tarot:3797bef]` feat: add unsettling ASCII eye tracking system
*   `[Lunarot-Tarot:e09060f]` style: refine layout and visual aesthetic
*   `[Lunarot-Tarot:17b59fc]` feat: initialize Sacred Draw application
*   `[Lunarot-Tarot:728ca75]` Initial commit

## 16/06
*   `[Lunarot-Tarot-old:15dac69]` Update index.html
*   `[Lunarot-Tarot-old:a8c5117]` Update index.html
*   `[Lunarot-Tarot-old:455cac9]` Update index.html
*   `[Lunarot-Tarot-old:41ca5c2]` Update index.html"""

# Replace `up` string variable in index.html
# Search for up=`# Vibecoding Development Log...`
up_match = re.search(r'up=`#.*?(?=`,cp=)', content, re.DOTALL)
if up_match:
    content = content.replace(up_match.group(0), f'up=`{new_up_string}')
    print("[SUCCESS] Replaced up string variable with structured 2026 dev history log")
else:
    print("[WARN] Could not find up string pattern match")

# 2. Update Ve() function to map exact file paths v
new_ve_fn = 'Ve=()=>{switch(v){case"/research/sites-log.md":return nh;case"/research/link-web-map.md":return sp;case"/research/dev-history.md":return up;case"/research/social-conduit.md":return op;case"/research/deka-archives.md":return cp;default:return nh}}'

old_ve_fn = re.search(r'Ve=\(\)=>\{switch\(E\).*?default:return nh\}\}', content)
if old_ve_fn:
    content = content.replace(old_ve_fn.group(0), new_ve_fn)
    print("[SUCCESS] Updated Ve() function to switch on file path v directly")

# 3. Update main view container rendering logic based on file path v
# Replace rendering block inside window content container
old_content_render = re.search(r's\.jsxs\("div",\{className:"space-y-1",children:\[.*?\)\}\)\}\)', content, re.DOTALL)

music_and_deka_jsx = '''s.jsxs("div",{className:"space-y-1",children:[
  v==="/db/music.index"?s.jsxs("div",{className:"mt-2 space-y-6 font-mono",children:[
    s.jsxs("div",{className:"border border-white/25 bg-black/60 p-5 rounded-none relative shadow-xl space-y-4",children:[
      s.jsx("div",{className:"absolute inset-1 border border-dashed border-white/10 pointer-events-none"}),
      s.jsxs("div",{className:"flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 border-b border-white/20 pb-3",children:[
        s.jsx("h3",{className:"text-xs font-bold text-white uppercase tracking-widest flex items-center gap-2",children:[s.jsx("span",{className:"text-red-600",children:"✦"})," GOTHIC SPOTIFY TRANSMISSION // CURATED PLAYLIST"]}),
        s.jsx("a",{href:"https://open.spotify.com/user/1277848177?si=8eef40800a9946b9",target:"_blank",rel:"noreferrer",className:"text-[9px] text-zinc-400 hover:text-white underline tracking-wider",children:"[ SPOTIFY PROFILE ]"})
      ]}),
      s.jsx("div",{className:"w-full overflow-hidden rounded-xl border border-white/20 bg-black/80 p-1",children:
        s.jsx("iframe",{src:"https://open.spotify.com/embed/playlist/0hSRNJC6W4mg4iugjZocUN?utm_source=generator&theme=0&si=cecb1d813fc3439f",width:"100%",height:"152",frameBorder:"0",allow:"autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture",loading:"lazy",style:{borderRadius:"12px"}})
      })
    ]}),
    s.jsxs("div",{className:"border border-white/25 bg-black/60 p-5 rounded-none relative shadow-xl space-y-4",children:[
      s.jsx("div",{className:"absolute inset-1 border border-dashed border-white/10 pointer-events-none"}),
      s.jsxs("div",{className:"flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 border-b border-white/20 pb-3",children:[
        s.jsx("h3",{className:"text-xs font-bold text-white uppercase tracking-widest flex items-center gap-2",children:[s.jsx("span",{className:"text-red-600",children:"✦"})," LAST.FM AUDIAL TELEMETRY // @VANZAIKAISER"]}),
        s.jsx("a",{href:"https://www.last.fm/user/VANZAIKAISER",target:"_blank",rel:"noreferrer",className:"text-[9px] text-red-500 hover:text-white underline tracking-wider",children:"[ LAST.FM PROFILE ]"})
      ]}),
      s.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-4 text-[10px] text-[#cfc9c0]",children:[
        s.jsxs("div",{className:"border border-white/15 p-4 bg-black/40 space-y-2",children:[
          s.jsx("div",{className:"text-xs text-white font-bold tracking-widest uppercase border-b border-white/10 pb-1 flex justify-between items-center",children:[s.jsx("span",{children:"TOP ARTIST RESONANCE"}),s.jsx("span",{className:"text-red-500 font-mono text-[9px]",children:"#1 SCROBBLED"})]}),
          s.jsx("div",{className:"text-sm text-red-400 font-bold tracking-wider pt-1",children:"BOY HARSHER"}),
          s.jsx("p",{className:"text-[9px] text-zinc-400 leading-relaxed font-sans",children:"Darkwave / EBM duo (Jae Matthews & Augustus Muller). Heavy synthetic basslines, industrial rhythms, cinematic longing."}),
          s.jsxs("div",{className:"space-y-1 pt-2 font-mono text-[9px]",children:[
            s.jsxs("div",{className:"flex justify-between text-zinc-400",children:[s.jsx("span",{children:"SCROBBLE FREQUENCY:"}),s.jsx("span",{className:"text-white font-bold",children:"HEAVY ROTATION"})]}),
            s.jsxs("div",{className:"flex justify-between text-zinc-400",children:[s.jsx("span",{children:"ALCHEMICAL ALIGNMENT:"}),s.jsx("span",{className:"text-white font-bold",children:"99.8% RESONANCE"})]})
          ]})
        ]}),
        s.jsxs("div",{className:"border border-white/15 p-4 bg-black/40 space-y-2",children:[
          s.jsx("div",{className:"text-xs text-white font-bold tracking-widest uppercase border-b border-white/10 pb-1",children:"BOY HARSHER // ESSENTIAL ANTHEMS"}),
          s.jsxs("ul",{className:"space-y-1 text-[9px] text-zinc-300 font-mono pt-1",children:[
            s.jsxs("li",{className:"flex items-center gap-2",children:[s.jsx("span",{className:"text-red-500",children:"►"}),s.jsx("span",{className:"text-white font-bold",children:"PAIN"}),s.jsx("span",{className:"text-zinc-500 text-[8px]",children:"[Lesser Man]"})]}),
            s.jsxs("li",{className:"flex items-center gap-2",children:[s.jsx("span",{className:"text-red-500",children:"►"}),s.jsx("span",{className:"text-white font-bold",children:"MOTION"}),s.jsx("span",{className:"text-zinc-500 text-[8px]",children:"[Yr Body Is Nothing]"})]}),
            s.jsxs("li",{className:"flex items-center gap-2",children:[s.jsx("span",{className:"text-red-500",children:"►"}),s.jsx("span",{className:"text-white font-bold",children:"COUNTRY GIRL"}),s.jsx("span",{className:"text-zinc-500 text-[8px]",children:"[Country Girl Uncut]"})]}),
            s.jsxs("li",{className:"flex items-center gap-2",children:[s.jsx("span",{className:"text-red-500",children:"►"}),s.jsx("span",{className:"text-white font-bold",children:"MODULATIONS"}),s.jsx("span",{className:"text-zinc-500 text-[8px]",children:"[Careful]"})]}),
            s.jsxs("li",{className:"flex items-center gap-2",children:[s.jsx("span",{className:"text-red-500",children:"►"}),s.jsx("span",{className:"text-white font-bold",children:"TEARS"}),s.jsx("span",{className:"text-zinc-500 text-[8px]",children:"[Careful]"})]}),
            s.jsxs("li",{className:"flex items-center gap-2",children:[s.jsx("span",{className:"text-red-500",children:"►"}),s.jsx("span",{className:"text-white font-bold",children:"MACHINA (FT. MARIANA SALDAÑA)"}),s.jsx("span",{className:"text-zinc-500 text-[8px]",children:"[The Runner]"})]})
          ]})
        ]})
      ]})
    ]})
  ]):v==="/db/deka-archive.index"?s.jsx("div",{className:"mt-2 border-t border-white/20 pt-6",children:F?s.jsxs("div",{className:"flex flex-col gap-4 font-mono",children:[s.jsxs("div",{className:"flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 border-b border-white/25 pb-3",children:[s.jsxs("div",{className:"flex items-center gap-2 text-[10px]",children:[s.jsx("span",{className:"text-[#838aa0]",children:"ACTIVE_VESSEL :"}),s.jsx("span",{className:"text-white font-bold",children:"10LAgjxx... (Deka Archive)"})]}),s.jsxs("div",{className:"flex flex-wrap items-center gap-3",children:[s.jsxs("div",{className:"flex items-center gap-1.5 text-[10px]",children:[s.jsx("span",{className:"text-[#838aa0]",children:"FILTER_FOLDER :"}),s.jsx("select",{value:q,onChange:C=>I(C.target.value),className:"bg-black border border-white/30 text-white px-2 py-0.5 focus:outline-none focus:border-red-800 text-[10px]",children:B.map(([C,Q])=>s.jsx("option",{value:C,children:Q},C))})]}),s.jsx("button",{onClick:()=>{localStorage.removeItem("deka_apps_script_url"),Z(""),ae("")},className:"text-[9px] text-[#838aa0] hover:text-white underline cursor-pointer",children:"[ Configure Web App ]"})]})]}),Y&&s.jsx("div",{className:"flex items-center justify-center py-12",children:s.jsx("span",{className:"text-xs text-white animate-pulse tracking-widest uppercase",children:"✦ LINKING DRIVE COGNITION TREE..."})}),V&&s.jsxs("div",{className:"border border-white/40 bg-white/10 text-white p-4 text-xs",children:[s.jsx("p",{className:"font-bold mb-2",children:"ERROR : connection handshake failed"}),s.jsx("p",{className:"opacity-80",children:V}),s.jsx("button",{onClick:()=>ge(F),className:"mt-3 px-3 py-1 border border-zinc-700 text-white hover:bg-red-900/10 uppercase tracking-widest text-[9px] cursor-pointer",children:"Retry Handshake"})]}),he&&s.jsxs("div",{className:"relative w-full h-[550px] bg-black/40 border border-white/30 overflow-hidden rounded",children:[s.jsxs("div",{className:"absolute top-2 right-3 z-30 flex gap-2",children:[s.jsx("a",{href:he.replace("/preview","/view"),target:"_blank",rel:"noreferrer",className:"font-mono text-[9px] text-white hover:text-white bg-black/60 px-3 py-1.5 border border-white/30 rounded",children:"[ OPEN IN DRIVE ]"}),s.jsx("button",{onClick:()=>ue(null),className:"font-mono text-[9px] text-white hover:text-white bg-black/60 px-3 py-1.5 border border-white/30 rounded cursor-pointer",children:"[ CLOSE PREVIEW ]"})]}),s.jsx("iframe",{src:he,width:"100%",height:"100%",frameBorder:"0",className:"w-full h-full filter invert-[88%] hue-rotate-180 brightness-[85%] saturate-[95%] opacity-95",allowFullScreen:!0,loading:"lazy",sandbox:"allow-scripts allow-same-origin allow-popups"})]}),!Y&&!V&&J.length>0&&s.jsx("div",{className:"grid grid-cols-2 sm:grid-cols-4 gap-4",children:le.map((C,Q)=>{const ee=C.mimeType.startsWith("image/"),ye=ti(C.thumbnailUrl,C.id);return s.jsxs("div",{onClick:()=>{ee?be(ye,C.id):ue(C.embedUrl)},className:"aspect-square relative bg-black/45 border border-white/25 hover:border-red-500/50 rounded overflow-hidden cursor-zoom-in group/item transition-all duration-300 hover:shadow-[0_0_12px_rgba(239,68,68,0.15)] flex flex-col justify-between",children:[ee?s.jsx("img",{src:ye,alt:C.name,loading:"lazy",className:"w-full h-full object-cover filter saturate-[65%] group-hover/item:saturate-100 transition-all duration-500"}):s.jsxs("div",{className:"flex-1 flex flex-col items-center justify-center p-3 text-center gap-2",children:[s.jsx("span",{className:"text-2xl text-red-950 group-hover/item:text-white transition-colors duration-300",children:"📄"}),s.jsx("span",{className:"text-[9px] text-[#cfc9c0]/80 tracking-wider truncate w-full",children:C.name})]}),s.jsxs("div",{className:"absolute inset-x-0 bottom-0 bg-gradient-to-t from-black via-black/80 to-transparent p-2 flex flex-col gap-0.5",children:[s.jsx("span",{className:"font-mono text-[9px] text-white tracking-wider truncate w-full",children:C.name}),s.jsxs("span",{className:"font-mono text-[7px] text-[#838aa0] uppercase tracking-widest truncate w-full",children:[C.parentFolder," // ",ee?"IMG":"DOC"]})]})]},Q)})}),!Y&&!V&&J.length===0&&s.jsx("div",{className:"text-center py-12 border border-dashed border-white/20",children:s.jsx("span",{className:"text-[10px] text-[#838aa0] uppercase tracking-widest",children:"No previewable assets found in this folder."})})]}):s.jsxs("div",{className:"bg-black/60 border border-white/30 p-5 rounded-none font-mono text-left mb-6",children:[s.jsx("h3",{className:"text-xs font-bold text-white uppercase mb-3 tracking-wider",children:"✦ Connect Deka Google Drive Live Previewer"}),s.jsx("p",{className:"text-[10px] text-[#cfc9c0]/80 mb-4 leading-relaxed font-sans",children:"Setup a serverless Google Apps Script Web App to load, query, and preview all folders, subfolders, and documents recursively from Google Drive."}),s.jsxs("div",{className:"space-y-3 text-[10px] text-[#cfc9c0] mb-5",children:[s.jsxs("div",{className:"flex items-start",children:[s.jsx("span",{className:"text-zinc-500 mr-2",children:"1."}),s.jsxs("span",{children:["Open ",s.jsx("a",{href:"https://script.google.com",target:"_blank",rel:"noreferrer",className:"text-white hover:underline",children:"script.google.com"})," and click ",s.jsx("b",{children:"New Project"}),"."]})]}),s.jsxs("div",{className:"flex items-start",children:[s.jsx("span",{className:"text-zinc-500 mr-2",children:"2."}),s.jsx("span",{children:"Paste the script code below into the editor."})]}),s.jsxs("div",{className:"flex items-start",children:[s.jsx("span",{className:"text-zinc-500 mr-2",children:"3."}),s.jsxs("span",{children:["Click ",s.jsx("b",{children:"Deploy > New Deployment"}),". Select ",s.jsx("b",{children:"Web App"}),"."]})]}),s.jsxs("div",{className:"flex items-start",children:[s.jsx("span",{className:"text-zinc-500 mr-2",children:"4."}),s.jsxs("span",{children:["Configure: ",s.jsx("i",{children:"Execute as:"})," ",s.jsx("b",{children:"Me"}),", ",s.jsx("i",{children:"Who has access:"})," ",s.jsx("b",{children:"Anyone"}),". Click Deploy."]})]}),s.jsxs("div",{className:"flex items-start",children:[s.jsx("span",{className:"text-zinc-500 mr-2",children:"5."}),s.jsxs("span",{children:["Copy the generated ",s.jsx("b",{children:"Web App URL"})," and paste it below."]})]})]}),s.jsxs("form",{onSubmit:fe,className:"flex gap-2 mb-6",children:[s.jsx("input",{type:"url",placeholder:"Paste Google Apps Script Web App URL here...",value:K,onChange:C=>ae(C.target.value),className:"flex-1 bg-black border border-white/30 px-3 py-1.5 text-xs text-white focus:outline-none focus:border-red-800",required:!0}),s.jsx("button",{type:"submit",className:"px-4 py-1.5 border border-zinc-700 bg-white/20 text-white hover:bg-white/40 text-xs font-bold uppercase tracking-wider cursor-pointer",children:"Connect"})]}),s.jsxs("div",{className:"flex justify-between items-center mb-2",children:[s.jsx("h4",{className:"text-[10px] text-white uppercase tracking-widest font-bold",children:"Google Apps Script Code:"}),s.jsx("button",{onClick:C=>{C.preventDefault(),navigator.clipboard.writeText(Oe),M(!0),setTimeout(()=>M(!1),2e3)},className:"px-3 py-1 border border-zinc-700 bg-white/20 text-white hover:bg-white/40 text-[9px] font-mono tracking-widest uppercase cursor-pointer select-none",children:z?"✦ COPIED ✦":"[ COPY SCRIPT ]"})]}),s.jsx("pre",{className:"bg-black/90 border border-white/20 p-3 rounded font-mono text-[9px] text-[#cfc9c0] overflow-x-auto max-h-40 scrollbar-thin select-text",style:{userSelect:"text"},children:s.jsx("code",{children:Oe})})]}):rp(Ve())
]})'''

if old_content_render:
    content = content.replace(old_content_render.group(0), music_and_deka_jsx)
    print("[SUCCESS] Replaced main content rendering logic with direct v check for music, deka gallery, and markdown")
else:
    print("[WARN] Could not match main content rendering block")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] fix_index_navigation script finished.")
