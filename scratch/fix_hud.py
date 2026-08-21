import re

filepath = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS before </style>
css_html = """
  /* Knowledge UI Styles */
  .knowledge-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
    z-index: 20;
    opacity: 0;
    transition: opacity 0.8s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .knowledge-overlay.visible {
    opacity: 1;
    pointer-events: auto;
  }

  /* Floating Text (3D Tracked) */
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
  }

  .kf-hebrew {
    font-size: 60px;
    font-family: 'Times New Roman', serif;
    color: rgba(255, 255, 255, 0.15);
    line-height: 1;
    letter-spacing: 0.05em;
    margin-bottom: -5px;
  }
  .kf-title {
    font-size: 32px;
    font-family: 'Cinzel', serif;
    color: #ffffff;
    letter-spacing: 0.15em;
    text-transform: uppercase;
  }
  .kf-meaning {
    font-size: 14px;
    font-family: 'JetBrains Mono', monospace;
    color: rgba(255, 255, 255, 0.6);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-top: 8px;
  }

  /* Glassmorphic Grimoire */
  .knowledge-grimoire {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    margin: 0 40px 40px 120px; /* Offset for left sidebar */
    padding: 32px;
    background: rgba(10, 10, 12, 0.6);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 4px;
    color: #e0e0e0;
    transform: translateY(40px);
    transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
    box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1);
  }
  .knowledge-overlay.visible .knowledge-grimoire {
    transform: translateY(0);
  }
  .grimoire-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 24px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 16px;
  }
  .grimoire-header h2 {
    margin: 0;
    font-family: 'Cinzel', serif;
    font-size: 24px;
    letter-spacing: 0.1em;
    color: #fff;
  }
  .kg-pillar {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: #888;
  }
  .kg-description {
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    line-height: 1.7;
    color: #ccc;
    margin-bottom: 32px;
  }
  .grimoire-grid {
    display: grid;
    grid-template-columns: 1fr 1.5fr;
    gap: 40px;
  }
  .grimoire-section h3 {
    margin: 0 0 16px 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: #999;
  }
  .grimoire-section p {
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    line-height: 1.6;
    color: #aaa;
    margin: 8px 0;
  }
  .grimoire-section p strong {
    color: #ddd;
    font-weight: 500;
  }
  
  .source-card {
    border-left: 2px solid rgba(255,255,255,0.2);
    padding-left: 16px;
    margin-bottom: 16px;
  }
  .source-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #777;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 8px;
  }
  .source-quote {
    font-family: 'Cinzel', serif;
    font-size: 16px;
    color: #fff;
    font-style: italic;
    line-height: 1.5;
    margin: 0 0 8px 0;
  }
  .source-interp {
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    line-height: 1.6;
    color: #999;
    margin: 0;
  }
</style>"""

if '.knowledge-overlay' not in content:
    content = content.replace('</style>', css_html)

# 2. Add SVG HUD to HTML
hud_svg_html = """  <!-- Knowledge HUD (Floating & Bottom Bar) -->
  <div id="knowledge-overlay" class="knowledge-overlay">
    
    <!-- SVG Tracking Lines -->
    <svg id="hud-svg" class="hud-svg-layer">
      <line id="hud-line" x1="0" y1="0" x2="0" y2="0" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" />
      <circle id="hud-dot" cx="0" cy="0" r="3" fill="rgba(255,255,255,1)" />
      <circle id="hud-dot-outer" cx="0" cy="0" r="10" fill="none" stroke="rgba(255,255,255,0.6)" stroke-width="1" stroke-dasharray="2 4" />
    </svg>
    
    <!-- Floating Text -->"""

if '<svg id="hud-svg"' not in content:
    content = content.replace('  <!-- Knowledge HUD (Floating & Bottom Bar) -->\n  <div id="knowledge-overlay" class="knowledge-overlay">\n    \n    <!-- Floating Text -->', hud_svg_html)


# 3. Modify updateKnowledgeUI to inject the Render Loop just after scene creation
# The render loop should be in the scene creation block, so let's find `return scene;` inside createScene

render_loop_js = """
  // 3D HUD Tracking Loop
  scene.onBeforeRenderObservable.add(() => {
    const overlay = document.getElementById('knowledge-overlay');
    if (!overlay || !overlay.classList.contains('visible') || !window.activePresetKey || window.activePresetKey === 'full') {
      return;
    }
    
    const p = EXACT_PRESETS[window.activePresetKey];
    if (!p) return;
    
    // Project 3D coordinate to 2D Screen
    const engineWidth = engine.getRenderWidth();
    const engineHeight = engine.getRenderHeight();
    const viewport = camera.viewport.toGlobal(engineWidth, engineHeight);
    
    const projected = BABYLON.Vector3.Project(
        p.target,
        BABYLON.Matrix.Identity(),
        scene.getTransformMatrix(),
        viewport
    );
    
    const targetX = projected.x;
    const targetY = projected.y;
    
    // Offset for the floating text
    const offsetX = 100;
    const offsetY = -80;
    const textX = targetX + offsetX;
    const textY = targetY + offsetY;
    
    // Update SVG Lines
    const line = document.getElementById('hud-line');
    const dot = document.getElementById('hud-dot');
    const dotOuter = document.getElementById('hud-dot-outer');
    
    if (line && dot && dotOuter) {
      line.setAttribute('x1', targetX);
      line.setAttribute('y1', targetY);
      line.setAttribute('x2', textX);
      line.setAttribute('y2', textY + 40); // attach to middle of text border
      
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
  });

  return scene;"""

if '3D HUD Tracking Loop' not in content:
    content = content.replace('return scene;', render_loop_js)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
