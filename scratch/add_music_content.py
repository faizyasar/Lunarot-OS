import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's inspect where E==="deka" or rp(Ve()) is located
# We want to add E==="music" section right before or after E==="deka"

target = 'E==="deka"&&s.jsx("div"'

# Let's define the JSX for E==="music"
music_jsx = '''E==="music"&&s.jsxs("div",{className:"mt-4 space-y-6 font-mono",children:[
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
]}),'''

if target in content:
    content = content.replace(target, music_jsx + target)
    print("[SUCCESS] Added E==='music' section to index.html")
else:
    print("[WARN] Could not find target E==='deka' in content")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] Script finished.")
