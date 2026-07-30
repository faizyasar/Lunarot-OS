import re

target_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"
public_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\public\style-guide.html"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace step 3 in updateCRT()
old_step3 = r"""      // 3. Screen Distortion (Perspective & Scale)
      const monitorEl = document.querySelector('.crt-monitor-specimen');
      if (monitorEl) {
        const perspective = 2000 - (distortionVal * 15);
        const rotateX = (distortionVal / 50).toFixed(1);
        const scale = (1 - (distortionVal / 500)).toFixed(3);
        monitorEl.style.transform = `perspective(${perspective}px) rotateX(${rotateX}deg) scale(${scale})`;
        monitorEl.style.borderRadius = `${12 + Math.floor(distortionVal / 5)}px`;
      }"""

new_step3 = r"""      // 3. Fisheye Lens Distortion (Inner Content Only - Outer Glass Corners Remain Fixed)
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

pos_step3 = content.find("// 3. Screen Distortion (Perspective & Scale)")
if pos_step3 != -1:
    pos_step3_end = content.find("// 4. Chromatic Aberration", pos_step3)
    if pos_step3_end != -1:
        content = content[:pos_step3] + new_step3.strip() + "\n\n" + content[pos_step3_end:]
        print("[SUCCESS] Replaced step 3 in style-guide.html with pure Fisheye Lens Distortion")

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

with open(public_file, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] replace_fisheye_exact script finished.")
