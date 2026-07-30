import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace F0 color swatches with updated complete color palette swatches
old_f0_start = content.find("function F0(){")
old_f0_end = content.find("function W0(){", old_f0_start)

if old_f0_start != -1 and old_f0_end != -1:
    new_f0_code = '''function F0(){return s.jsxs("div",{className:"gothic-panel panel-gold w-full flex flex-col space-y-4 relative p-5",children:[
      s.jsx("span",{className:"panel-title-tag",children:"AESTHETIC_TOKENS // COLOR_PALETTE"}),
      s.jsx("span",{className:"panel-footer-tag",children:"THEME_ROOT v6.1"}),
      s.jsx("p",{className:"text-[8px] font-bold uppercase tracking-[0.2em] text-white/40 border-b border-white/10 pb-1 font-mono",children:"✦ COLOR SWATCHES & HEX TOKENS"}),
      s.jsxs("div",{className:"grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono text-[9px]",children:[
        s.jsxs("div",{className:"border border-white/15 p-2 bg-black/40 space-y-1.5",children:[
          s.jsx("div",{className:"h-10 w-full bg-[#c8a45a] border border-white/20 shadow-[0_0_10px_rgba(200,164,90,0.3)]"}),
          s.jsxs("div",{className:"flex justify-between items-center",children:[s.jsx("span",{className:"text-white font-bold",children:"GOLD PRIMARY"}),s.jsx("span",{className:"text-[#c8a45a]",children:"#c8a45a"})]})
        ]}),
        s.jsxs("div",{className:"border border-white/15 p-2 bg-black/40 space-y-1.5",children:[
          s.jsx("div",{className:"h-10 w-full bg-[#e3b341] border border-white/20 shadow-[0_0_10px_rgba(227,179,65,0.4)]"}),
          s.jsxs("div",{className:"flex justify-between items-center",children:[s.jsx("span",{className:"text-white font-bold",children:"GOLD BRIGHT"}),s.jsx("span",{className:"text-[#e3b341]",children:"#e3b341"})]})
        ]}),
        s.jsxs("div",{className:"border border-white/15 p-2 bg-black/40 space-y-1.5",children:[
          s.jsx("div",{className:"h-10 w-full bg-[#fb2c36] border border-white/20 shadow-[0_0_10px_rgba(251,44,54,0.4)]"}),
          s.jsxs("div",{className:"flex justify-between items-center",children:[s.jsx("span",{className:"text-white font-bold",children:"CRIMSON"}),s.jsx("span",{className:"text-[#fb2c36]",children:"#fb2c36"})]})
        ]}),
        s.jsxs("div",{className:"border border-white/15 p-2 bg-black/40 space-y-1.5",children:[
          s.jsx("div",{className:"h-10 w-full bg-[#00d2ef] border border-white/20 shadow-[0_0_10px_rgba(0,210,239,0.4)]"}),
          s.jsxs("div",{className:"flex justify-between items-center",children:[s.jsx("span",{className:"text-white font-bold",children:"CONFLUX CYAN"}),s.jsx("span",{className:"text-[#00d2ef]",children:"#00d2ef"})]})
        ]}),
        s.jsxs("div",{className:"border border-white/15 p-2 bg-black/40 space-y-1.5",children:[
          s.jsx("div",{className:"h-10 w-full bg-[#cfc9c0] border border-white/20"}),
          s.jsxs("div",{className:"flex justify-between items-center",children:[s.jsx("span",{className:"text-black font-bold",children:"PARCHMENT"}),s.jsx("span",{className:"text-[#cfc9c0]",children:"#cfc9c0"})]})
        ]}),
        s.jsxs("div",{className:"border border-white/15 p-2 bg-black/40 space-y-1.5",children:[
          s.jsx("div",{className:"h-10 w-full bg-[#838aa0] border border-white/20"}),
          s.jsxs("div",{className:"flex justify-between items-center",children:[s.jsx("span",{className:"text-white font-bold",children:"TELEMETRY"}),s.jsx("span",{className:"text-[#838aa0]",children:"#838aa0"})]})
        ]}),
        s.jsxs("div",{className:"border border-white/15 p-2 bg-black/40 space-y-1.5",children:[
          s.jsx("div",{className:"h-10 w-full bg-[#050505] border border-white/20"}),
          s.jsxs("div",{className:"flex justify-between items-center",children:[s.jsx("span",{className:"text-white font-bold",children:"VOID PITCH"}),s.jsx("span",{className:"text-zinc-500",children:"#050505"})]})
        ]}),
        s.jsxs("div",{className:"border border-white/15 p-2 bg-black/40 space-y-1.5",children:[
          s.jsx("div",{className:"h-10 w-full bg-white border border-white/20"}),
          s.jsxs("div",{className:"flex justify-between items-center",children:[s.jsx("span",{className:"text-black font-bold",children:"PURE WHITE"}),s.jsx("span",{className:"text-zinc-300",children:"#ffffff"})]})
        ]})
      ]})
    ])}'''
    content = content[:old_f0_start] + new_f0_code + "\n" + content[old_f0_end:]
    print("[SUCCESS] Replaced F0 color swatches in index.html")

# Update P0 (Form & Buttons Specimen)
old_p0_start = content.find("function P0(){")
old_p0_end = content.find("function _0(){", old_p0_start)

if old_p0_start != -1 and old_p0_end != -1:
    new_p0_code = '''function P0(){return s.jsxs("div",{className:"gothic-panel panel-white w-full flex flex-col space-y-5 relative p-5 font-mono",children:[
      s.jsx("span",{className:"panel-title-tag",children:"SACRED_BUTTONS_&_FORMS"}),
      s.jsx("span",{className:"panel-footer-tag",children:"INTERACTIVE_SPECIMEN"}),
      s.jsxs("div",{className:"space-y-3",children:[
        s.jsx("p",{className:"text-[8px] font-bold uppercase tracking-[0.2em] text-white/40 border-b border-white/10 pb-1",children:"✦ BUTTON & BADGE SPECIMENS"}),
        s.jsxs("div",{className:"flex flex-wrap items-center gap-3",children:[
          s.jsx("button",{className:"gothic-btn-gold px-4 py-2 text-[9px] uppercase tracking-widest",children:"[ INITIATE CONDUIT ]"}),
          s.jsx("button",{className:"gothic-btn-dark px-4 py-2 text-[9px] uppercase tracking-widest",children:"[ RITUAL SHIELD ]"}),
          s.jsx("button",{className:"gothic-btn-crimson px-4 py-2 text-[9px] uppercase tracking-widest",children:"[ PURGE VESSEL ]"})
        ]}),
        s.jsxs("div",{className:"flex flex-wrap items-center gap-2 pt-2 text-[8px]",children:[
          s.jsx("span",{className:"border border-[#c8a45a]/50 bg-[#c8a45a]/10 text-[#c8a45a] px-2 py-0.5 font-bold uppercase",children:"[ OK ]"}),
          s.jsx("span",{className:"border border-white/20 bg-black/60 text-white px-2 py-0.5 uppercase",children:"[ ONLINE ]"}),
          s.jsx("span",{className:"border border-red-500/40 bg-red-500/10 text-red-400 px-2 py-0.5 uppercase",children:"[ SCROBBLED ]"}),
          s.jsx("span",{className:"border border-cyan-400/40 bg-cyan-400/10 text-cyan-300 px-2 py-0.5 uppercase",children:"[ RE-LINKING ]"})
        ]})
      ]}),
      s.jsxs("div",{className:"space-y-3 pt-3 border-t border-white/10",children:[
        s.jsx("p",{className:"text-[8px] font-bold uppercase tracking-[0.2em] text-white/40 border-b border-white/10 pb-1",children:"✦ FORM FIELD SPECIMEN"}),
        s.jsxs("div",{className:"gothic-input-group space-y-1",children:[
          s.jsx("div",{className:"input-header-line text-[9px] text-zinc-400 uppercase tracking-widest",children:"VESSEL REGISTRY INGRESS"}),
          s.jsx("input",{className:"gothic-input-field w-full bg-transparent border-b border-white/25 text-xs text-white p-2 outline-none focus:border-[#c8a45a]",defaultValue:"COGNITION_VESSEL",placeholder:"Enter vessel..."})
        ]})
      ]})
    ])}'''
    content = content[:old_p0_start] + new_p0_code + "\n" + content[old_p0_end:]
    print("[SUCCESS] Replaced P0 buttons and form specimen in index.html")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] update_gp_in_index script finished.")
