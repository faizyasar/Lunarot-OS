import re
import os

target_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"
public_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\public\style-guide.html"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# Update SVG Filter in HTML for a much stronger fisheye lens map
old_svg_filter = r"""  <!-- SVG Fisheye Barrel Distortion Filter -->
  <svg style="display:none;" width="0" height="0">
    <filter id="fisheyeFilter">
      <feTurbulence type="fractalNoise" baseFrequency="0.005 0.005" numOctaves="1" result="noise" />
      <feDisplacementMap id="fisheyeDisplace" in="SourceGraphic" in2="noise" scale="0" xChannelSelector="R" yChannelSelector="G" />
    </filter>
  </svg>"""

new_svg_filter = r"""  <!-- SVG Fisheye Barrel Distortion Filter -->
  <svg style="display:none;" width="0" height="0">
    <filter id="fisheyeFilter" x="-20%" y="-20%" width="140%" height="140%">
      <feTurbulence type="fractalNoise" baseFrequency="0.015 0.015" numOctaves="2" result="noise" />
      <feDisplacementMap id="fisheyeDisplace" in="SourceGraphic" in2="noise" scale="0" xChannelSelector="R" yChannelSelector="G" />
    </filter>
  </svg>"""

if old_svg_filter in content:
    content = content.replace(old_svg_filter, new_svg_filter)

# Update Javascript fisheye logic in updateCRT()
old_js_fisheye = r"""      // 3. Fisheye Lens Distortion (Inner Content Only - Outer Glass Corners Remain Fixed)
      const displaceEl = document.getElementById('fisheyeDisplace');
      const glassElInner = document.getElementById('crtGlass');
      if (glassElInner) {
        if (distortionVal > 0) {
          const scaleAmount = (distortionVal * 0.35).toFixed(1);
          if (displaceEl) displaceEl.setAttribute('scale', scaleAmount);
          glassElInner.style.filter = `url(#fisheyeFilter) perspective(900px) rotateX(${(distortionVal / 40).toFixed(1)}deg)`;
          glassElInner.style.transform = `scale(${(1 + (distortionVal / 600)).toFixed(3)})`;
        } else {
          glassElInner.style.filter = 'none';
          glassElInner.style.transform = 'none';
        }
      }"""

new_js_fisheye = r"""      // 3. Dramatic Spherical Fisheye Lens Barrel Distortion (0 to 100%)
      const displaceEl = document.getElementById('fisheyeDisplace');
      const glassElInner = document.getElementById('crtGlass');
      if (glassElInner) {
        if (distortionVal > 0) {
          // Multiply displacement scale up to 75 for extreme visible bulge
          const scaleAmount = (distortionVal * 0.75).toFixed(1);
          if (displaceEl) displaceEl.setAttribute('scale', scaleAmount);
          
          // Spherical 3D Lens Bulge perspective
          const perspective = (1000 - (distortionVal * 7)).toFixed(0);
          const rotateX = (distortionVal / 12).toFixed(1);
          const scale = (1 + (distortionVal / 250)).toFixed(3);
          
          glassElInner.style.filter = `url(#fisheyeFilter)`;
          glassElInner.style.transform = `perspective(${perspective}px) rotateX(${rotateX}deg) scale(${scale})`;
          glassElInner.style.transformOrigin = 'center center';
        } else {
          if (displaceEl) displaceEl.setAttribute('scale', '0');
          glassElInner.style.filter = 'none';
          glassElInner.style.transform = 'none';
        }
      }"""

if old_js_fisheye in content:
    content = content.replace(old_js_fisheye, new_js_fisheye)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

with open(public_file, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Dramatically intensified Fisheye Lens Bulge Effect in Style Guide HTML!")
