import os

target_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"
public_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\public\style-guide.html"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# CSS definitions for Vista Aero + Classic Apple Aqua Hybrid
vista_apple_css = r"""
    /* VISTA AERO + CLASSIC APPLE AQUA HYBRID AESTHETICS */
    .vista-window-header {
      background: linear-gradient(180deg, rgba(255,255,255,0.22) 0%, rgba(255,255,255,0.06) 49%, rgba(0,0,0,0.45) 50%, rgba(0,0,0,0.75) 100%);
      border-bottom: 1px solid rgba(255,255,255,0.18);
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.4);
    }

    .mac-window-dots {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .mac-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      position: relative;
      box-shadow: inset 0 1px 1px rgba(255,255,255,0.6), 0 1px 2px rgba(0,0,0,0.6);
      cursor: pointer;
      transition: transform 0.15s ease;
    }
    .mac-dot:hover { transform: scale(1.15); }
    .mac-dot-close { background: radial-gradient(circle at 35% 35%, #ff7b73, #ff3b30); border: 1px solid #c0261f; }
    .mac-dot-minimize { background: radial-gradient(circle at 35% 35%, #ffdf6d, #ffcc00); border: 1px solid #c79f00; }
    .mac-dot-maximize { background: radial-gradient(circle at 35% 35%, #58e072, #28cd41); border: 1px solid #1ba631; }

    .vista-aqua-btn {
      background: linear-gradient(180deg, rgba(255,255,255,0.25) 0%, rgba(255,255,255,0.08) 48%, rgba(0,0,0,0.3) 50%, rgba(0,0,0,0.6) 100%);
      border: 1px solid rgba(255,255,255,0.35);
      border-radius: 4px;
      color: #fff;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      padding: 8px 16px;
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.5), 0 2px 6px rgba(0,0,0,0.6);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .vista-aqua-btn:hover {
      background: linear-gradient(180deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.15) 48%, rgba(0,0,0,0.2) 50%, rgba(0,0,0,0.5) 100%);
      border-color: rgba(255,255,255,0.7);
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.7), 0 0 15px rgba(255,255,255,0.4);
      transform: translateY(-1px);
    }

    .sunken-well {
      background: rgba(0, 0, 0, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: inset 0 3px 8px rgba(0,0,0,0.8), 0 1px 0 rgba(255,255,255,0.15);
      padding: 1rem;
    }
"""

# Insert CSS before </style>
if "/* VISTA AERO + CLASSIC APPLE AQUA HYBRID AESTHETICS */" not in content:
    content = content.replace("</style>", vista_apple_css + "\n  </style>")

# Insert Section 06 into HTML body before </main>
section_06_html = r"""
    <!-- SECTION 06: VISTA AERO & CLASSIC APPLE AQUA HYBRID -->
    <section id="vista-apple" class="space-y-6">
      <div class="border-b border-white/15 pb-3 flex justify-between items-end">
        <div>
          <h2 class="font-cinzel text-xl font-bold text-white tracking-widest uppercase flex items-center gap-2">
            <span class="text-white">✦</span> 06. 2000s VISTA AERO x CLASSIC APPLE AQUA HYBRID
          </h2>
          <p class="font-mono text-xs text-zinc-500 mt-1">Glossy multi-stop Aero headers, classic Apple traffic light dots, glossy gel buttons, and sunken dark glass wells.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">

        <!-- Vista Aero / Apple Glass Window Frame Specimen -->
        <div class="gothic-panel panel-white overflow-hidden !p-0 shadow-2xl">
          <div class="vista-window-header px-4 py-2.5 flex justify-between items-center select-none">
            <div class="flex items-center gap-3">
              <div class="mac-window-dots">
                <span class="mac-dot mac-dot-close" title="Close"></span>
                <span class="mac-dot mac-dot-minimize" title="Minimize"></span>
                <span class="mac-dot mac-dot-maximize" title="Maximize"></span>
              </div>
              <span class="font-mono text-xs font-bold text-white tracking-widest uppercase drop-shadow">AERO_AQUA // WINDOW_TITLEBAR</span>
            </div>
            <span class="font-mono text-[9px] text-zinc-300 uppercase tracking-widest">v6.1</span>
          </div>

          <div class="p-5 space-y-4">
            <p class="font-garamond text-sm text-[#cfc9c0] leading-relaxed">
              Combines the glossy multi-stop specular reflection of 2000s Windows Vista Aero glass with early Mac OS X Aqua traffic light control spheres.
            </p>

            <div class="sunken-well space-y-2 font-mono text-xs">
              <div class="flex justify-between text-zinc-400">
                <span>SUNKEN GLASS WELL:</span>
                <span class="text-white font-bold">[ ACTIVE INSET SHADOW ]</span>
              </div>
              <p class="text-[11px] text-zinc-300">Recessed content container with inner drop shadow and bottom rim highlight.</p>
            </div>
          </div>
        </div>

        <!-- Vista / Aqua Controls Workshop -->
        <div class="gothic-panel panel-white space-y-5">
          <span class="panel-title-tag">GLOSSY_CONTROLS // VISTA_AQUA</span>

          <div class="space-y-3">
            <span class="font-mono text-[9px] text-white tracking-widest uppercase block">// GLOSSY AERO GEL BUTTONS</span>
            <div class="flex flex-wrap items-center gap-3">
              <button class="vista-aqua-btn">[ LAUNCH VESSEL ]</button>
              <button class="vista-aqua-btn">[ RE-LINK ASTRALS ]</button>
            </div>
          </div>

          <div class="space-y-3 pt-3 border-t border-white/10">
            <span class="font-mono text-[9px] text-white tracking-widest uppercase block">// MAC OS X TRAFFIC LIGHT CONTROLS</span>
            <div class="flex items-center gap-4 bg-black/60 p-3 border border-white/15">
              <div class="mac-window-dots">
                <span class="mac-dot mac-dot-close"></span>
                <span class="mac-dot mac-dot-minimize"></span>
                <span class="mac-dot mac-dot-maximize"></span>
              </div>
              <span class="font-mono text-xs text-zinc-300">[ RED: CLOSE | YELLOW: MINIMIZE | GREEN: MAXIMIZE ]</span>
            </div>
          </div>

          <span class="panel-footer-tag">AERO_AQUA_SPECIMEN</span>
        </div>

      </div>
    </section>
"""

if 'id="vista-apple"' not in content:
    content = content.replace("</main>", section_06_html + "\n  </main>")

# Add 06. Vista x Apple link to header nav
nav_marker = '<a href="#interactive"'
if nav_marker in content and '06. Vista x Apple' not in content:
    content = content.replace(nav_marker, '<a href="#vista-apple" class="px-3 py-1.5 border border-white/15 text-zinc-400 hover:text-white hover:border-white transition-all">06. Vista x Apple</a>\n      ' + nav_marker)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

with open(public_file, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Updated Style Guide HTML with Vista x Apple hybrid section.")
