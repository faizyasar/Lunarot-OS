import os
import re

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
index_path = os.path.join(root_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update rp() so bullet points `* ` also use `font-garamond`!
old_bullet = 'className:`flex items-start ${x?"ml-6 text-xs text-[#838aa0]":"ml-2 text-sm text-[#cfc9c0]"} my-1`'
new_bullet = 'className:`flex items-start ${x?"ml-6 text-xs text-[#838aa0]":"ml-2 text-sm font-garamond text-[#cfc9c0]"} my-1`'

if old_bullet in content:
    content = content.replace(old_bullet, new_bullet)
    print("[SUCCESS] Added font-garamond to rp() bullet items so all list logs render in gorgeous Garamond font")

# 2. Update vp array (sidebar tree) so music.index and deka-archive.index are in database folder
old_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📄"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📄"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📄"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"📁"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

new_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📜"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📜"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📡"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"🎴"},{name:"music.index",path:"/db/music.index",icon:"🎵"},{name:"deka-archive.index",path:"/db/deka-archive.index",icon:"🖼️"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

if old_vp in content:
    content = content.replace(old_vp, new_vp)
    print("[SUCCESS] Updated vp array with music.index and deka-archive.index")

# 3. Add MusicIndex component right before xp()
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
          s.jsxs("div",{className:"flex justify-between text-[#838aa0]",children:[s.jsx("span",{children:"SCROBBLE FREQUENCY:"}),s.jsx("span",{className:"text-white font-bold",children:"HEAVY ROTATION"})]}),
          s.jsxs("div",{className:"flex justify-between text-[#838aa0]",children:[s.jsx("span",{children:"ALCHEMICAL ALIGNMENT:"}),s.jsx("span",{className:"text-white font-bold",children:"99.8% RESONANCE"})]})
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

if 'function MusicIndex()' not in content and 'function xp()' in content:
    content = content.replace('function xp()', music_comp_def + '\nfunction xp()')
    print("[SUCCESS] Inserted MusicIndex component")

# 4. Update xp() file view routing
old_xp_rendering = 'v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K}),v==="/sys/show-aesthetic-tokens.exe"&&s.jsx(gp,{}),v==="/sys/edit-vessel-handshake.conf"&&g&&s.jsx(yp,{user:g,onReSeed:I})'

new_xp_rendering = 'v==="/db/tarot-directory.index"&&s.jsx(pp,{onUpdateActivePlanets:Y,onContextChange:K}),v==="/db/music.index"&&s.jsx(MusicIndex,{}),v==="/db/deka-archive.index"&&s.jsx(ai,{defaultTab:"deka"}),v==="/sys/show-aesthetic-tokens.exe"&&s.jsx(gp,{}),v==="/sys/edit-vessel-handshake.conf"&&g&&s.jsx(yp,{user:g,onReSeed:I})'

if old_xp_rendering in content:
    content = content.replace(old_xp_rendering, new_xp_rendering)
    print("[SUCCESS] Updated xp() routing for music.index and deka-archive.index")

# Update window header titles switch case in xp()
old_header_switch = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;'
new_header_switch = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;case"/db/music.index":K("AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES");break;case"/db/deka-archive.index":K("DEKA DRIVE GALLERY // LIVE ASSET PREVIEWER");break;'

if old_header_switch in content:
    content = content.replace(old_header_switch, new_header_switch)
    print("[SUCCESS] Updated window header context titles")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] apply_perfect_garamond_fix complete.")
