import re
import os

target_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"
public_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\public\style-guide.html"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# Expanded CRT Distortion CSS
crt_distortion_css = r"""
    /* CRT DISTORTION & SCANLINE WORKBENCH */
    .crt-distortion-wrapper {
      transition: transform 0.2s ease, filter 0.2s ease;
    }

    .chromatic-aberration {
      text-shadow: -2px 0 rgba(255,0,0,0.7), 2px 0 rgba(0,255,255,0.7);
    }

    /* Custom Range Sliders */
    input[type=range] {
      -webkit-appearance: none;
      width: 100%;
      background: rgba(255,255,255,0.1);
      height: 4px;
      border-radius: 2px;
      outline: none;
    }
    input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: #ffffff;
      border: 1px solid rgba(0,0,0,0.8);
      box-shadow: 0 0 8px rgba(255,255,255,0.8);
      cursor: pointer;
      transition: transform 0.15s ease;
    }
    input[type=range]::-webkit-slider-thumb:hover {
      transform: scale(1.25);
    }
"""

if "/* CRT DISTORTION & SCANLINE WORKBENCH */" not in content:
    content = content.replace("</style>", crt_distortion_css + "\n  </style>")

# Replace Section 07 HTML Controls with Sliders
section_07_controls = r"""
        <!-- CRT FX Interactive Distortion Workbench Sliders -->
        <div class="gothic-panel panel-white space-y-5">
          <span class="panel-title-tag">CRT_DISTORTION_WORKBENCH</span>

          <div class="space-y-4 text-xs font-mono">

            <!-- 1. Scanline Heaviness -->
            <div class="space-y-1">
              <div class="flex justify-between items-center text-[10px]">
                <span class="text-white font-bold uppercase">// SCANLINE HEAVINESS</span>
                <span id="valScanlines" class="text-white font-bold">50%</span>
              </div>
              <input type="range" id="sliderScanlines" min="0" max="100" value="50" oninput="updateCRT()">
            </div>

            <!-- 2. Screen Flicker Intensity -->
            <div class="space-y-1">
              <div class="flex justify-between items-center text-[10px]">
                <span class="text-white font-bold uppercase">// FLICKER INTENSITY</span>
                <span id="valFlicker" class="text-white font-bold">50%</span>
              </div>
              <input type="range" id="sliderFlicker" min="0" max="100" value="50" oninput="updateCRT()">
            </div>

            <!-- 3. Screen Distortion (Curvature Bulge) -->
            <div class="space-y-1">
              <div class="flex justify-between items-center text-[10px]">
                <span class="text-white font-bold uppercase">// BARREL DISTORTION (CURVATURE)</span>
                <span id="valDistortion" class="text-white font-bold">25%</span>
              </div>
              <input type="range" id="sliderDistortion" min="0" max="100" value="25" oninput="updateCRT()">
            </div>

            <!-- 4. RGB Chromatic Aberration -->
            <div class="space-y-1">
              <div class="flex justify-between items-center text-[10px]">
                <span class="text-white font-bold uppercase">// RGB CHROMATIC ABERRATION</span>
                <span id="valAberration" class="text-white font-bold">0px</span>
              </div>
              <input type="range" id="sliderAberration" min="0" max="10" value="0" oninput="updateCRT()">
            </div>

            <!-- 5. Perimeter Vignette Darkness -->
            <div class="space-y-1">
              <div class="flex justify-between items-center text-[10px]">
                <span class="text-white font-bold uppercase">// PERIMETER VIGNETTE DARKNESS</span>
                <span id="valVignette" class="text-white font-bold">85%</span>
              </div>
              <input type="range" id="sliderVignette" min="0" max="100" value="85" oninput="updateCRT()">
            </div>

            <!-- Reset Button -->
            <button onclick="resetCRT()" class="gothic-btn-white w-full py-2 text-[9px] mt-2">[ RESET CRT DISTORTION DEFAULTS ]</button>
          </div>

          <span class="panel-footer-tag">FX_SLIDERS</span>
        </div>
"""

# Replace old right-side controls in Section 07
old_controls_pattern = r'<!-- CRT FX Control Switches -->.*?</span>\s*</div>'
content = re.sub(old_controls_pattern, section_07_controls.strip(), content, flags=re.DOTALL)

# Add real-time JavaScript CRT update function
update_crt_js = r"""
    // Real-time CRT Distortion & Scanline Workbench Controller
    function updateCRT() {
      const scanlinesVal = document.getElementById('sliderScanlines').value;
      const flickerVal = document.getElementById('sliderFlicker').value;
      const distortionVal = document.getElementById('sliderDistortion').value;
      const aberrationVal = document.getElementById('sliderAberration').value;
      const vignetteVal = document.getElementById('sliderVignette').value;

      // Update Labels
      document.getElementById('valScanlines').innerText = scanlinesVal + '%';
      document.getElementById('valFlicker').innerText = flickerVal + '%';
      document.getElementById('valDistortion').innerText = distortionVal + '%';
      document.getElementById('valAberration').innerText = aberrationVal + 'px';
      document.getElementById('valVignette').innerText = vignetteVal + '%';

      // 1. Scanlines Opacity & Raster
      const scanlinesEl = document.getElementById('crtScanlines');
      if (scanlinesEl) {
        scanlinesEl.style.opacity = scanlinesVal / 100;
        const size = Math.max(2, Math.floor(scanlinesVal / 20));
        scanlinesEl.style.background = `linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, ${scanlinesVal / 100}) 50%) 0 0 / 100% ${size}px`;
      }

      // 2. Screen Flicker Speed
      const glassEl = document.getElementById('crtGlass');
      if (glassEl) {
        if (flickerVal > 0) {
          const speed = (0.5 - (flickerVal / 250)).toFixed(2);
          glassEl.style.animation = `${speed}s infinite alternate crt-flicker-preview`;
        } else {
          glassEl.style.animation = 'none';
        }
      }

      // 3. Screen Distortion (Perspective & Scale)
      const monitorEl = document.querySelector('.crt-monitor-specimen');
      if (monitorEl) {
        const perspective = 2000 - (distortionVal * 15);
        const rotateX = (distortionVal / 50).toFixed(1);
        const scale = (1 - (distortionVal / 500)).toFixed(3);
        monitorEl.style.transform = `perspective(${perspective}px) rotateX(${rotateX}deg) scale(${scale})`;
        monitorEl.style.borderRadius = `${12 + Math.floor(distortionVal / 5)}px`;
      }

      // 4. Chromatic Aberration (RGB Shift)
      const textEl = document.querySelector('#crtGlass h3');
      if (textEl) {
        if (aberrationVal > 0) {
          textEl.style.textShadow = `-${aberrationVal}px 0 rgba(255,0,0,0.8), ${aberrationVal}px 0 rgba(0,255,255,0.8)`;
        } else {
          textEl.style.textShadow = 'none';
        }
      }

      // 5. Vignette Darkness
      const vignetteEl = document.getElementById('crtVignette');
      if (vignetteEl) {
        vignetteEl.style.background = `radial-gradient(circle, rgba(0,0,0,0) ${100 - vignetteVal}%, rgba(0,0,0,${vignetteVal / 100}))`;
      }
    }

    function resetCRT() {
      document.getElementById('sliderScanlines').value = 50;
      document.getElementById('sliderFlicker').value = 50;
      document.getElementById('sliderDistortion').value = 25;
      document.getElementById('sliderAberration').value = 0;
      document.getElementById('sliderVignette').value = 85;
      updateCRT();
    }
"""

if "function updateCRT()" not in content:
    content = content.replace("</script>", update_crt_js + "\n  </script>")

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

with open(public_file, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Added interactive CRT Distortion Sliders Workbench to Style Guide!")
