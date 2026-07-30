import re
import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"
target_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"
public_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\public\style-guide.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    index_content = f.read()

# Extract WebM video base64 data url
video_match = re.search(r'data:video/webm;base64,[^"]+', index_content)
if not video_match:
    print("[ERROR] WebM video data url not found")
    exit(1)

video_url = video_match.group(0)
print(f"[FOUND] WebM video URL ({len(video_url)} chars)")

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# CRT Monitor & Scanlines CSS
crt_fx_css = r"""
    /* CRT MONITOR & SCANLINE FX */
    .crt-monitor-specimen {
      position: relative;
      width: 100%;
      height: 380px;
      background: #030303;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid rgba(255,255,255,0.25);
      box-shadow: 0 0 40px rgba(0,0,0,0.9);
      transform: perspective(2000px) rotateX(0.5deg) scale(0.99);
    }

    .crt-screen-glass-preview {
      position: relative;
      width: 100%;
      height: 100%;
      overflow: hidden;
      animation: 0.25s infinite alternate crt-flicker-preview;
    }

    @keyframes crt-flicker-preview {
      0% { opacity: 0.98; }
      100% { opacity: 1.0; }
    }

    .crt-scanlines-overlay {
      position: absolute;
      inset: 0;
      z-index: 20;
      pointer-events: none;
      background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.35) 50%) 0 0 / 100% 3px;
    }

    .crt-vignette-overlay {
      position: absolute;
      inset: 0;
      z-index: 25;
      pointer-events: none;
      background: radial-gradient(circle, rgba(0,0,0,0) 60%, rgba(0,0,0,0.85));
    }
"""

if "/* CRT MONITOR & SCANLINE FX */" not in content:
    content = content.replace("</style>", crt_fx_css + "\n  </style>")

# Section 07 HTML Block
section_07_html = f"""
    <!-- SECTION 07: CRT MONITOR OVERLAY & BACKGROUND VIDEO FX -->
    <section id="crt-fx" class="space-y-6">
      <div class="border-b border-white/15 pb-3 flex justify-between items-end">
        <div>
          <h2 class="font-cinzel text-xl font-bold text-white tracking-widest uppercase flex items-center gap-2">
            <span class="text-white">✦</span> 07. CRT MONITOR OVERLAY & BACKGROUND VIDEO FX
          </h2>
          <p class="font-mono text-xs text-zinc-500 mt-1">Live CRT scanlines (3px grid), curved glass vignette, screen flicker, and background loop video FX.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 font-mono">

        <!-- Live CRT Monitor Specimen Frame -->
        <div class="lg:col-span-2 gothic-panel panel-white !p-0 overflow-hidden shadow-2xl">
          <div class="crt-monitor-specimen">
            <div id="crtGlass" class="crt-screen-glass-preview">
              <div id="crtScanlines" class="crt-scanlines-overlay"></div>
              <div id="crtVignette" class="crt-vignette-overlay"></div>
              
              <!-- Background Loop Video -->
              <video autoPlay muted loop playsInline preload="auto" class="absolute inset-0 w-full h-full object-cover z-0 opacity-80 pointer-events-none">
                <source src="{video_url}" type="video/webm">
              </video>

              <!-- Embedded OS Window Preview Inside Monitor -->
              <div class="absolute inset-6 z-10 flex flex-col justify-center items-center pointer-events-none">
                <div class="gothic-panel panel-white w-full max-w-md bg-black/75 backdrop-blur-md p-6 text-center space-y-3 shadow-2xl">
                  <span class="panel-title-tag">CRT_MONITOR // DISPLAY</span>
                  <h3 class="font-cinzel text-base font-bold text-white tracking-widest uppercase drop-shadow">LUNAROT OS CRT MONITOR FX</h3>
                  <p class="font-garamond text-xs text-[#cfc9c0] leading-relaxed">
                    Active background video loop with scanline raster lines, perimeter radial vignette, and glass flicker.
                  </p>
                  <div class="flex justify-center gap-2 text-[8px] pt-1">
                    <span class="border border-white/40 bg-white/10 text-white px-2 py-0.5 uppercase">[ SCANLINES: ACTIVE ]</span>
                    <span class="border border-white/40 bg-white/10 text-white px-2 py-0.5 uppercase">[ VIDEO: LOOPING ]</span>
                  </div>
                  <span class="panel-footer-tag">VESSEL_TELEMETRY</span>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- CRT FX Control Switches -->
        <div class="gothic-panel panel-white space-y-5">
          <span class="panel-title-tag">CRT_FX_CONTROLS</span>

          <div class="space-y-4 text-xs">
            <div class="space-y-1">
              <span class="text-white font-bold block">// SCANLINES (3PX RASTER)</span>
              <button onclick="toggleScanlines()" id="btnScanlines" class="gothic-btn-white w-full py-2 text-[9px]">[ TOGGLE SCANLINES: ON ]</button>
            </div>

            <div class="space-y-1">
              <span class="text-white font-bold block">// PERIMETER VIGNETTE</span>
              <button onclick="toggleVignette()" id="btnVignette" class="gothic-btn-white w-full py-2 text-[9px]">[ TOGGLE VIGNETTE: ON ]</button>
            </div>

            <div class="space-y-1">
              <span class="text-white font-bold block">// SCREEN FLICKER ANIMATION</span>
              <button onclick="toggleFlicker()" id="btnFlicker" class="gothic-btn-white w-full py-2 text-[9px]">[ TOGGLE FLICKER: ON ]</button>
            </div>
          </div>

          <div class="pt-3 border-t border-white/10 text-[10px] text-zinc-400 space-y-1">
            <p><strong class="text-white">Video Asset:</strong> Embedded Base64 WebM cosmic stream.</p>
            <p><strong class="text-white">Scanline Blend:</strong> Linear gradient 50% opacity mask.</p>
          </div>

          <span class="panel-footer-tag">FX_CONTROLLER</span>
        </div>

      </div>
    </section>
"""

if 'id="crt-fx"' not in content:
    content = content.replace("</main>", section_07_html + "\n  </main>")

# JavaScript handlers for toggles
crt_js_handlers = r"""
    // CRT FX Toggle Handlers
    function toggleScanlines() {
      const el = document.getElementById('crtScanlines');
      const btn = document.getElementById('btnScanlines');
      if (el.style.display === 'none') {
        el.style.display = 'block';
        btn.innerText = '[ TOGGLE SCANLINES: ON ]';
      } else {
        el.style.display = 'none';
        btn.innerText = '[ TOGGLE SCANLINES: OFF ]';
      }
    }

    function toggleVignette() {
      const el = document.getElementById('crtVignette');
      const btn = document.getElementById('btnVignette');
      if (el.style.display === 'none') {
        el.style.display = 'block';
        btn.innerText = '[ TOGGLE VIGNETTE: ON ]';
      } else {
        el.style.display = 'none';
        btn.innerText = '[ TOGGLE VIGNETTE: OFF ]';
      }
    }

    function toggleFlicker() {
      const el = document.getElementById('crtGlass');
      const btn = document.getElementById('btnFlicker');
      if (el.style.animation === 'none') {
        el.style.animation = '0.25s infinite alternate crt-flicker-preview';
        btn.innerText = '[ TOGGLE FLICKER: ON ]';
      } else {
        el.style.animation = 'none';
        btn.innerText = '[ TOGGLE FLICKER: OFF ]';
      }
    }
"""

if "function toggleScanlines()" not in content:
    content = content.replace("</script>", crt_js_handlers + "\n  </script>")

# Add 07. CRT & Video FX link to header nav
nav_marker = '<a href="#vista-apple"'
if nav_marker in content and '07. CRT & Video FX' not in content:
    content = content.replace(nav_marker, '<a href="#crt-fx" class="px-3 py-1.5 border border-white/15 text-zinc-400 hover:text-white hover:border-white transition-all">07. CRT & Video FX</a>\n      ' + nav_marker)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

with open(public_file, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Updated Style Guide HTML with CRT & Video FX section.")
