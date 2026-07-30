import re
import os

target_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"
public_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\public\style-guide.html"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# SVG Fisheye Filter Definition
svg_fisheye_filter = r"""
  <!-- SVG Fisheye Barrel Distortion Filter -->
  <svg style="display:none;" width="0" height="0">
    <filter id="fisheyeFilter">
      <feTurbulence type="fractalNoise" baseFrequency="0.005 0.005" numOctaves="1" result="noise" />
      <feDisplacementMap id="fisheyeDisplace" in="SourceGraphic" in2="noise" scale="0" xChannelSelector="R" yChannelSelector="G" />
    </filter>
  </svg>
"""

if '<filter id="fisheyeFilter">' not in content:
    content = content.replace("<main", svg_fisheye_filter + "\n  <main")

# Update JavaScript to apply Fisheye Lens Distortion ONLY to inner screen content (without altering outer glass corner radius)
old_js_func = r"""      // 3. Screen Distortion (Perspective & Scale)
      const monitorEl = document.querySelector('.crt-monitor-specimen');
      if (monitorEl) {
        const perspective = 2000 - (distortionVal * 15);
        const rotateX = (distortionVal / 50).toFixed(1);
        const scale = (1 - (distortionVal / 500)).toFixed(3);
        monitorEl.style.transform = `perspective(${perspective}px) rotateX(${rotateX}deg) scale(${scale})`;
        monitorEl.style.borderRadius = `${12 + Math.floor(distortionVal / 5)}px`;
      }"""

new_js_func = r"""      // 3. Fisheye Lens Barrel Distortion (Inner Screen Content Only - Glass Corners Remain Fixed)
      const displaceEl = document.getElementById('fisheyeDisplace');
      const glassElInner = document.getElementById('crtGlass');
      if (glassElInner) {
        if (distortionVal > 0) {
          const bulgeScale = (distortionVal * 0.4).toFixed(1);
          if (displaceEl) displaceEl.setAttribute('scale', bulgeScale);
          glassElInner.style.filter = `url(#fisheyeFilter) perspective(800px) rotateX(${(distortionVal / 40).toFixed(1)}deg) scale(${(1 + (distortionVal / 600)).toFixed(3)})`;
        } else {
          glassElInner.style.filter = 'none';
        }
      }"""

if "fisheyeDisplace" not in content and old_js_func in content:
    content = content.replace(old_js_func, new_js_func)
    print("[SUCCESS] Replaced legacy monitor scale with pure Fisheye Lens Barrel Distortion")

# Update label in controls
content = content.replace("// BARREL DISTORTION (CURVATURE)", "// FISHEYE LENS BARREL DISTORTION")

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

with open(public_file, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] update_fisheye_barrel_distortion script finished.")
