import subprocess
import os
import re

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")

# 1. Restore index.html from commit 4006ef0~1 (clean working state prior to today)
print("[1] Restoring index.html from clean working commit 4006ef0~1...")
res = subprocess.run(["git", "checkout", "4006ef0~1", "--", "index.html"], capture_output=True, text=True, cwd=root_dir)
if res.returncode == 0:
    print("[SUCCESS] Restored clean index.html")
else:
    print(f"[WARN] git checkout error: {res.stderr}")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# ==============================================================================
# 2. UPDATE VP (SIDEBAR TREE)
# ==============================================================================
# In original vp array: add music.index and deka-archive.index under database folder!
old_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📄"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📄"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📄"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"📁"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

new_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📜"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📜"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📡"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"🎴"},{name:"music.index",path:"/db/music.index",icon:"🎵"},{name:"deka-archive.index",path:"/db/deka-archive.index",icon:"🖼️"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

if old_vp in content:
    content = content.replace(old_vp, new_vp)
    print("[SUCCESS] Updated vp array with music.index and deka-archive.index under database")

# ==============================================================================
# 3. UPDATE DEV HISTORY LOG STRING `up` WITH WRITTEN-DOWN FORMAT
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

safe_up_js = written_log_md.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
up_match = re.search(r'up=`#.*?(?=`,op=)', content, re.DOTALL)
if up_match:
    content = content.replace(up_match.group(0), f'up=`{safe_up_js}')
    print("[SUCCESS] Updated up string with written-down log format")

# ==============================================================================
# 4. DEFINE MUSIC AND DEKA ARCHIVE COMPONENTS FROM GROUND UP
# ==============================================================================

music_comp_def = '''function MusicIndex(){return s.jsxs("div",{className:"flex-1 flex flex-col h-full w-full bg-black/35 backdrop-blur-[2px] border border-white/40 relative z-25 group overflow-hidden p-4 sm:p-6 md:p-8 font-mono space-y-6 overflow-y-auto scrollbar-thin scrollbar-thumb-white/10",children:[
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
])}'''

# Insert MusicIndex function right before xp()
if 'function xp()' in content:
    content = content.replace('function xp()', music_comp_def + '\nfunction xp()')
    print("[SUCCESS] Defined MusicIndex component from ground up")

# ==============================================================================
# 5. UPDATE XP() FILE VIEW ROUTING TO MAP EVERY SIDEBAR ITEM DIRECTLY
# ==============================================================================
old_xp_body = 'v==="/apps/sacred-draw.bin"&&g&&s.jsx(lp,{user:g,onUpdatePlanets:J,onUpdateActivePlanets:Y,onReset:q,isPurging:ce,setIsPurging:V}),v==="/apps/astral-pachinko.bin"&&g&&s.jsx(ip,{user:g,onUpdatePlanets:J,onUpdateActivePlanets:Y,onReset:q,isPurging:ce,setIsPurging:V}),v==="/research/sites-log.md"&&s.jsx(ai,{defaultTab:"log"}),v==="/research/link-web-map.md"&&s.jsx(ai,{defaultTab:"map"}),v==="/research/dev-history.md"&&s.jsx(ai,{defaultTab:"dev"}),v==="/research/deka-archives.md"&&s.jsx(ai,{defaultTab:"deka"}),v==="/research/social-conduit.md"&&s.jsx(ai,{defaultTab:"social"}),v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K}),v==="/sys/show-aesthetic-tokens.exe"&&s.jsx(gp,{}),v==="/sys/edit-vessel-handshake.conf"&&g&&s.jsx(yp,{user:g,onReSeed:I})'

new_xp_body = 'v==="/apps/sacred-draw.bin"&&g&&s.jsx(lp,{user:g,onUpdatePlanets:J,onUpdateActivePlanets:Y,onReset:q,isPurging:ce,setIsPurging:V}),v==="/apps/astral-pachinko.bin"&&g&&s.jsx(ip,{user:g,onUpdatePlanets:J,onUpdateActivePlanets:Y,onReset:q,isPurging:ce,setIsPurging:V}),v==="/research/sites-log.md"&&s.jsx(ai,{defaultTab:"log"}),v==="/research/link-web-map.md"&&s.jsx(ai,{defaultTab:"map"}),v==="/research/dev-history.md"&&s.jsx(ai,{defaultTab:"dev"}),v==="/research/deka-archives.md"&&s.jsx(ai,{defaultTab:"deka"}),v==="/research/social-conduit.md"&&s.jsx(ai,{defaultTab:"social"}),v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K}),v==="/db/music.index"&&s.jsx(MusicIndex,{}),v==="/db/deka-archive.index"&&s.jsx(ai,{defaultTab:"deka"}),v==="/sys/show-aesthetic-tokens.exe"&&s.jsx(gp,{}),v==="/sys/edit-vessel-handshake.conf"&&g&&s.jsx(yp,{user:g,onReSeed:I})'

if old_xp_body in content:
    content = content.replace(old_xp_body, new_xp_body)
    print("[SUCCESS] Updated xp() routing for music.index and deka-archive.index")

# Update window header titles switch case in xp()
old_header_switch = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;'
new_header_switch = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;case"/db/music.index":K("AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES");break;case"/db/deka-archive.index":K("DEKA DRIVE GALLERY // LIVE ASSET PREVIEWER");break;'

if old_header_switch in content:
    content = content.replace(old_header_switch, new_header_switch)
    print("[SUCCESS] Updated window header context titles for database files")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] restore_clean_and_apply_ground_up script finished.")
