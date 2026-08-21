import re

filepath = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for knowledge-floating
old_css = """  /* Floating Text */
  .knowledge-floating {
    margin-top: 15vh;
    margin-right: 15vw;
    align-self: flex-end;
    text-align: right;
    text-shadow: 0 0 20px rgba(255,255,255,0.3);
    transform: translateX(20px);
    transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
  }"""

new_css = """  /* Floating Text (3D Tracked) */
  .knowledge-floating {
    position: absolute;
    text-align: left;
    text-shadow: 0 0 20px rgba(0,0,0,0.8);
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.4s ease, transform 0.4s ease;
    pointer-events: none;
    border-left: 1px solid rgba(255,255,255,0.3);
    padding-left: 16px;
  }
  .knowledge-overlay.visible .knowledge-floating {
    opacity: 1;
    transform: translateY(0);
  }
  
  /* SVG HUD Lines */
  .hud-svg-layer {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    pointer-events: none;
    z-index: 15;
    opacity: 0;
    transition: opacity 0.4s ease;
  }
  .knowledge-overlay.visible .hud-svg-layer {
    opacity: 1;
  }"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("CSS block not found!")

# 2. Add SVG to HTML
old_html = """  <!-- Knowledge HUD (Floating & Bottom Bar) -->
  <div id="knowledge-overlay" class="knowledge-overlay">"""

new_html = """  <!-- Knowledge HUD (Floating & Bottom Bar) -->
  <div id="knowledge-overlay" class="knowledge-overlay">
    
    <!-- SVG Tracking Lines -->
    <svg id="hud-svg" class="hud-svg-layer">
      <line id="hud-line" x1="0" y1="0" x2="0" y2="0" stroke="rgba(255,255,255,0.3)" stroke-width="1" />
      <circle id="hud-dot" cx="0" cy="0" r="3" fill="rgba(255,255,255,0.8)" />
      <circle id="hud-dot-outer" cx="0" cy="0" r="8" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1" stroke-dasharray="2 2" />
    </svg>"""

if old_html in content:
    content = content.replace(old_html, new_html)
else:
    print("HTML block not found!")

# 3. Modify text styles to align left instead of right
old_kf_hebrew = """  .kf-hebrew {
    font-size: 80px;
    font-family: 'Times New Roman', serif;
    color: rgba(255, 255, 255, 0.15);
    line-height: 1;
    letter-spacing: 0.1em;
    margin-bottom: -15px;
  }"""
new_kf_hebrew = """  .kf-hebrew {
    font-size: 60px;
    font-family: 'Times New Roman', serif;
    color: rgba(255, 255, 255, 0.15);
    line-height: 1;
    letter-spacing: 0.05em;
    margin-bottom: -5px;
  }"""
if old_kf_hebrew in content:
    content = content.replace(old_kf_hebrew, new_kf_hebrew)


# 4. Inject 3D projection logic
# Look for updateKnowledgeUI and add the render loop code.
old_js = """    // Show UI
    overlay.classList.add('visible');
  }"""

new_js = """    // Show UI
    overlay.classList.add('visible');
  }
  
  // 3D HUD Tracking Loop
  scene.onBeforeRenderObservable.add(() => {
    const overlay = document.getElementById('knowledge-overlay');
    if (!overlay || !overlay.classList.contains('visible') || !window.activePresetKey || window.activePresetKey === 'full') {
      return;
    }
    
    const p = EXACT_PRESETS[window.activePresetKey];
    if (!p) return;
    
    // Use the preset target as the anchor point
    // We add a tiny bit to Y to attach slightly above the center of the bone group
    const anchorPoint = p.target.clone();
    
    const engineWidth = engine.getRenderWidth();
    const engineHeight = engine.getRenderHeight();
    const viewport = camera.viewport.toGlobal(engineWidth, engineHeight);
    
    // Project 3D coordinate to 2D Screen
    const projected = BABYLON.Vector3.Project(
        anchorPoint,
        BABYLON.Matrix.Identity(),
        scene.getTransformMatrix(),
        viewport
    );
    
    const targetX = projected.x;
    const targetY = projected.y;
    
    // Offset for the floating text
    const offsetX = 80;
    const offsetY = -60;
    const textX = targetX + offsetX;
    const textY = targetY + offsetY;
    
    // Update SVG Lines
    const line = document.getElementById('hud-line');
    const dot = document.getElementById('hud-dot');
    const dotOuter = document.getElementById('hud-dot-outer');
    
    if (line && dot) {
      line.setAttribute('x1', targetX);
      line.setAttribute('y1', targetY);
      line.setAttribute('x2', textX);
      line.setAttribute('y2', textY + 20); // attach to middle of text border
      
      dot.setAttribute('cx', targetX);
      dot.setAttribute('cy', targetY);
      dotOuter.setAttribute('cx', targetX);
      dotOuter.setAttribute('cy', targetY);
      
      // Rotate the outer dotted circle for sci-fi effect
      const time = performance.now() * 0.05;
      dotOuter.setAttribute('transform', `rotate(${time} ${targetX} ${targetY})`);
    }
    
    // Update Floating Text Div
    const textDiv = document.getElementById('knowledge-floating');
    if (textDiv) {
      textDiv.style.left = textX + 'px';
      textDiv.style.top = textY + 'px';
    }
  });"""

if old_js in content:
    content = content.replace(old_js, new_js)
else:
    print("JS logic block not found!")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated 3D HUD tracking!")
