import os
import re

with open(r'C:\Users\faizy\Downloads\Lunarot_Tarot_Deck_-_Standalone.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Make background transparent, hide UI overlays, hide wrap so crisp box is seen
custom_css = """
<style>
  html, body {
    background: transparent !important;
    overflow: hidden !important;
    width: 100%; height: 100%;
    margin: 0; padding: 0;
  }
  .status-hint, .index-panel, .btn-rebox, .nav-btn, .dust-field, .cam-readout, .card-caption, .wrap {
    display: none !important;
  }
  #stage {
    transform: scale(1.6) !important;
    transition: none !important;
  }
  #scene {
    transition: none !important;
  }
  * {
    animation: none !important;
  }
</style>
"""

html = html.replace('</head>', custom_css + '\n</head>')

# Deterministic rotation function
control_script = """
<script>
window.__setStageRotation = function(yDeg, xDeg) {
  const scene = document.getElementById('scene');
  if (scene) {
    scene.style.transition = 'none';
    scene.style.transform = `rotateX(${xDeg !== undefined ? xDeg : 10}deg) rotateY(${yDeg}deg)`;
  }
};

let autoSpin = true;
let currentY = 0;
function spinLoop() {
  if (autoSpin) {
    currentY = (currentY + 1.2) % 360;
    const scene = document.getElementById('scene');
    if (scene) {
      scene.style.transform = `rotateX(10deg) rotateY(${currentY}deg)`;
    }
  }
  requestAnimationFrame(spinLoop);
}
requestAnimationFrame(spinLoop);
window.addEventListener('pointerdown', () => { autoSpin = false; });
</script>
"""

html = html.replace('</body>', control_script + '\n</body>')

clean_html_path = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_clean_render.html'
with open(clean_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved scratch/tarot_clean_render.html")
