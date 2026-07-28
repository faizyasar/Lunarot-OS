import os
import shutil
import json
import re

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
public_dir = os.path.join(root_dir, "public")
src_file = r"C:\Users\faizy\Downloads\Sacred Pachinko 0.9.html"

# ==============================================================================
# 1. SACRED PACHINKO STATIC FILES & VERCEL ROUTING
# ==============================================================================
pachinko_html = os.path.join(public_dir, "pachinko.html")
sacred_pachinko_html = os.path.join(public_dir, "sacred-pachinko.html")

if os.path.exists(src_file):
    shutil.copyfile(src_file, pachinko_html)
    shutil.copyfile(src_file, sacred_pachinko_html)
    print("[SUCCESS] Copied Sacred Pachinko 0.9 to public/pachinko.html and public/sacred-pachinko.html")

vercel_json_path = os.path.join(root_dir, "vercel.json")
vercel_config = {
  "cleanUrls": True,
  "rewrites": [
    { "source": "/sacred-pachinko", "destination": "/sacred-pachinko.html" },
    { "source": "/pachinko", "destination": "/pachinko.html" },
    { "source": "/history", "destination": "/history.html" }
  ]
}

with open(vercel_json_path, "w", encoding="utf-8") as f:
    json.dump(vercel_config, f, indent=2)
print("[SUCCESS] Configured vercel.json")


# ==============================================================================
# 2. LOG FORMAT IN WRITTEN-DOWN MARKDOWN STYLE
# ==============================================================================
written_log_md = """# ✦ DEV HISTORY CHRONICLES

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

changelog_path = os.path.join(root_dir, "CHANGELOG.md")
with open(changelog_path, "w", encoding="utf-8") as f:
    f.write("# Changelog - Lunarot OS Ecosystem History\n\n" + written_log_md)
print("[SUCCESS] Updated CHANGELOG.md with written-down log style")

history_html_path = os.path.join(public_dir, "history.html")
history_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lunarot OS - Ecosystem History Log</title>
  <style>
    body {{
      background: #000;
      color: #cfc9c0;
      font-family: ui-monospace, 'SF Mono', Menlo, Consolas, monospace;
      padding: 32px 24px;
      line-height: 1.6;
      max-width: 850px;
      margin: 0 auto;
    }}
    h1 {{ color: #ffffff; font-size: 22px; letter-spacing: 0.1em; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 12px; }}
    h2 {{ color: #ffffff; font-size: 18px; margin-top: 28px; border-bottom: 1px dashed rgba(255,255,255,0.15); padding-bottom: 4px; }}
    h3 {{ color: #838aa0; font-size: 13px; margin-top: 18px; letter-spacing: 0.15em; }}
    ul {{ list-style-type: square; padding-left: 20px; }}
    li {{ margin-bottom: 6px; font-size: 13px; }}
    code {{ color: #ffffff; background: rgba(255,255,255,0.1); padding: 2px 6px; font-size: 11px; }}
  </style>
</head>
<body>
  <h1>✦ Lunarot OS - Ecosystem History Log</h1>
  <div id="content">
"""

for line in written_log_md.split('\n'):
    if line.startswith('# ✦ '):
        history_html_content += f"<h2>{line[4:]}</h2>\n"
    elif line.startswith('## '):
        history_html_content += f"<h3>Day: {line[3:]}</h3>\n<ul>\n"
    elif line.startswith('*   '):
        item_text = line[4:].replace('`', '<code>', 1).replace('`', '</code>', 1)
        history_html_content += f"  <li>{item_text}</li>\n"

history_html_content += """
  </div>
</body>
</html>"""

with open(history_html_path, "w", encoding="utf-8") as f:
    f.write(history_html_content)
print("[SUCCESS] Updated public/history.html with written-down log style")


# ==============================================================================
# 3. UPDATE INDEX.HTML WITH DIRECT COMPONENT ROUTING FOR MUSIC & DEKA
# ==============================================================================
index_path = os.path.join(root_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update vp array
old_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📄"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📄"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📄"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"📁"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

new_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📜"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📜"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📡"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"🎴"},{name:"music.index",path:"/db/music.index",icon:"🎵"},{name:"deka-archive.index",path:"/db/deka-archive.index",icon:"🖼️"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

if old_vp in content:
    content = content.replace(old_vp, new_vp)
    print("[SUCCESS] Updated vp array in index.html")

# Update research top tabs bar to ONLY ["log","map","dev","social"]
old_tabs_bar = 'children:["log","map","dev","deka","social"].map('
new_tabs_bar = 'children:["log","map","dev","social"].map('
if old_tabs_bar in content:
    content = content.replace(old_tabs_bar, new_tabs_bar)
    print("[SUCCESS] Updated research top tabs bar in index.html")

# Update Ve() function to switch on v directly
old_ve_fn = 'Ve=()=>{switch(E){case"log":return nh;case"map":return sp;case"dev":return up;case"social":return op;case"deka":return cp;default:return nh}}'
new_ve_fn = 'Ve=()=>{switch(v){case"/research/sites-log.md":return nh;case"/research/link-web-map.md":return sp;case"/research/dev-history.md":return up;case"/research/social-conduit.md":return op;case"/research/deka-archives.md":return cp;default:return nh}}'

if old_ve_fn in content:
    content = content.replace(old_ve_fn, new_ve_fn)
    print("[SUCCESS] Updated Ve() function in index.html")

# Replace up variable with written_log_md
safe_up_js = written_log_md.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
up_match = re.search(r'up=`#.*?(?=`,cp=)', content, re.DOTALL)

if up_match:
    content = content.replace(up_match.group(0), f'up=`{safe_up_js}')
    print("[SUCCESS] Replaced up string in index.html with written-down log")

# Now update main xp() body rendering logic for /db/music.index and /db/deka-archive.index
old_xp_rendering = 'v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K}),v==="/sys/show-aesthetic-tokens.exe"&&s.jsx(gp,{}),v==="/sys/edit-vessel-handshake.conf"&&g&&s.jsx(yp,{user:g,onReSeed:I})'

# Create MusicComponent JSX for music.index
music_comp_jsx = '''s.jsxs("div",{className:"flex-1 flex flex-col h-full w-full bg-black/35 backdrop-blur-[2px] border border-white/40 relative z-25 group overflow-hidden p-4 sm:p-6 md:p-8 font-mono space-y-6 overflow-y-auto",children:[
  s.jsx("span",{className:"absolute top-2 left-3 font-mono text-[7px] text-zinc-500/50 tracking-[0.3em] uppercase pointer-events-none",children:"AUDIAL_TELEMETRY // MUSIC"}),
  s.jsxs("div",{className:"border border-white/25 bg-black/60 p-5 rounded-none relative shadow-xl space-y-4 mt-4",children:[
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
]})'''

# Deka archive component JSX
deka_comp_jsx = 's.jsx(ai,{defaultTab:"deka"})'

new_xp_rendering = 'v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K}),v==="/db/music.index"&&' + music_comp_jsx + ',v==="/db/deka-archive.index"&&' + deka_comp_jsx + ',v==="/sys/show-aesthetic-tokens.exe"&&s.jsx(gp,{}),v==="/sys/edit-vessel-handshake.conf"&&g&&s.jsx(yp,{user:g,onReSeed:I})'

if old_xp_rendering in content:
    content = content.replace(old_xp_rendering, new_xp_rendering)
    print("[SUCCESS] Injected music.index and deka-archive.index rendering cases in xp()")
else:
    print("[WARN] Could not find old_xp_rendering in index.html")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] Master script finished.")
