import re
import json

with open('golem.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject CSS
css_to_add = """
  /* Floating Lexicon Markers */
  #lexicon-markers-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 20;
    overflow: hidden;
  }

  .lexicon-marker {
    position: absolute;
    transform: translate(-50%, -50%);
    pointer-events: auto;
    font-family: 'JetBrains Mono', monospace;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: opacity 0.3s ease;
  }
  
  .lexicon-marker.hidden {
    opacity: 0;
    pointer-events: none;
  }

  .lexicon-dot {
    width: 6px;
    height: 6px;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 50%;
    box-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
    flex-shrink: 0;
    cursor: crosshair;
  }
  
  .lexicon-label-compact {
    font-size: 10px;
    color: rgba(255, 255, 255, 0.7);
    text-shadow: 0 0 4px #000;
    white-space: nowrap;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    cursor: crosshair;
    transition: color 0.2s ease;
  }
  
  .lexicon-marker:hover .lexicon-label-compact {
    color: #fff;
    text-shadow: 0 0 8px rgba(255, 255, 255, 0.8);
  }

  .lexicon-card {
    position: absolute;
    left: 20px;
    top: -20px;
    width: 320px;
    background: rgba(5, 5, 10, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 16px;
    border-radius: 4px;
    opacity: 0;
    transform: translateX(10px);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    pointer-events: none;
    color: #e0e0e0;
    font-family: 'Inter', sans-serif;
  }

  .lexicon-marker:hover .lexicon-card {
    opacity: 1;
    transform: translateX(0);
    pointer-events: auto;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.05) inset;
  }

  .lexicon-card .lc-term {
    font-family: 'Cinzel', serif;
    font-size: 14px;
    color: #fff;
    margin-bottom: 4px;
    letter-spacing: 0.05em;
  }
  
  .lexicon-card .lc-hebrew {
    font-family: 'Times New Roman', serif;
    font-size: 18px;
    color: #aaa;
    margin-bottom: 8px;
    direction: rtl;
    text-align: right;
  }
  
  .lexicon-card .lc-root {
    font-size: 9px;
    color: #777;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 4px;
  }

  .lexicon-card .lc-def {
    font-size: 11px;
    line-height: 1.5;
    color: #ccc;
    margin-bottom: 8px;
  }

  .lexicon-card .lc-mystic {
    font-size: 11px;
    line-height: 1.5;
    color: #999;
    font-style: italic;
    border-left: 2px solid rgba(255,255,255,0.2);
    padding-left: 8px;
  }
"""

if "Floating Lexicon Markers" not in html:
    html = html.replace('</style>', css_to_add + '\n</style>')

# 2. Inject HTML container
html_to_add = '<div id="lexicon-markers-container"></div>'
if html_to_add not in html:
    # Add it right before the sephirot-markers container
    html = html.replace('<div id="sephirot-markers"></div>', html_to_add + '\n  <div id="sephirot-markers"></div>')


# 3. Inject JS logic
# Read the extracted lexicon data
with open('scratch/lexicon_dump.json', 'r', encoding='utf-8') as lf:
    lexicon_data = lf.read()

js_to_add = f"""
  // --- LEXICON DATA & MAPPING ---
  const lexiconData = {lexicon_data};

  const lexiconMeshMap = {{
    'ein-sof': 'Frontal bone',
    'shekhinah': 'Talus.l',
    'logos': 'Mandible',
    'anima-mundi': 'Body of sternum',
    'macrocosm-microcosm': 'Scapula.l',
    'ruach-spiritus': 'Vertebra T4',
    'unio-mystica': 'Parietal bone.l',
    'prima-materia': 'Sacrum',
    'gematria-abjad': 'Phalanx distal 1.l',
    'ascent-of-soul': 'Vertebra L1',
    'magnum-opus': 'Femur.l',
    'adam-kadmon': 'Vertebra C1'
  }};

  const lexiconDOMNodes = {{}};

  function initLexiconMarkers() {{
    const container = document.getElementById('lexicon-markers-container');
    if (!container) return;
    
    lexiconData.forEach(item => {{
      const boneName = lexiconMeshMap[item.id];
      if (!boneName) return;

      const marker = document.createElement('div');
      marker.className = 'lexicon-marker';
      marker.id = 'lex-marker-' + item.id;
      
      const dot = document.createElement('div');
      dot.className = 'lexicon-dot';
      
      const label = document.createElement('div');
      label.className = 'lexicon-label-compact';
      label.textContent = item.transliteration;
      
      const card = document.createElement('div');
      card.className = 'lexicon-card';
      
      let cardHTML = `<div class="lc-term">${{item.term}}</div>`;
      if (item.hebrew) cardHTML += `<div class="lc-hebrew">${{item.hebrew}}</div>`;
      if (item.linguisticRoot) cardHTML += `<div class="lc-root">${{item.linguisticRoot}}</div>`;
      if (item.definition) cardHTML += `<div class="lc-def">${{item.definition}}</div>`;
      if (item.mysticalSignificance) cardHTML += `<div class="lc-mystic">${{item.mysticalSignificance}}</div>`;
      
      card.innerHTML = cardHTML;
      
      marker.appendChild(dot);
      marker.appendChild(label);
      marker.appendChild(card);
      container.appendChild(marker);
      
      lexiconDOMNodes[item.id] = {{ el: marker, boneName: boneName, mesh: null }};
    }});
  }}
"""

if "// --- LEXICON DATA & MAPPING ---" not in html:
    # Inject right before init() function
    html = html.replace('function init() {', js_to_add + '\nfunction init() {')

# 4. Hook into init() to populate meshes and into render loop
hook_init = "initLexiconMarkers();"
if hook_init not in html:
    html = html.replace('createScene(canvas, engine);', 'createScene(canvas, engine);\n    ' + hook_init)

# Hook into mesh loading to populate lexiconDOMNodes meshes
hook_mesh = """
        // Populate lexicon meshes
        for (const [id, data] of Object.entries(lexiconDOMNodes)) {
          if (mesh.name === data.boneName) {
            data.mesh = mesh;
          }
        }
"""
if "Populate lexicon meshes" not in html:
    # find where sephirot meshes are populated
    target = "if (sephirotMeshMap[key] === mesh.name)"
    html = html.replace(target, hook_mesh + '\n          ' + target)


# Hook into render loop
hook_render = """
        // Lexicon Telemetry
        const showLexicon = (window.activePresetKey === 'keter' || window.activePresetKey === 'full'); // Show them on keter and full body maybe? Wait, user wants them sprinkled. Let's just always show them, but fade based on distance, or just always show them if camera is somewhat far.
        // Let's just show them if activePresetKey is 'keter' or we can just always show them and fade out if behind camera.
        
        for (const [id, data] of Object.entries(lexiconDOMNodes)) {
           if (!data.mesh) continue;
           
           // Simple distance check to hide markers if too zoomed in or too far
           const dist = BABYLON.Vector3.Distance(scene.activeCamera.position, data.mesh.getAbsolutePosition());
           
           // Calculate projection
           const pos = data.mesh.getAbsolutePosition();
           const proj = BABYLON.Vector3.Project(
               pos,
               BABYLON.Matrix.Identity(),
               scene.getTransformMatrix(),
               camera.viewport.toGlobal(engine.getRenderWidth(), engine.getRenderHeight())
           );
           
           if (proj.z > 0 && proj.z < 1) {
               data.el.style.left = proj.x + 'px';
               data.el.style.top = proj.y + 'px';
               // Hide if too close (e.g. zooming deep into a bone)
               if (dist < 5.0) {
                   data.el.classList.add('hidden');
               } else {
                   data.el.classList.remove('hidden');
               }
           } else {
               data.el.classList.add('hidden');
           }
        }
"""
if "Lexicon Telemetry" not in html:
    target2 = "// --- Sephirot Markers ---"
    html = html.replace(target2, hook_render + '\n\n        ' + target2)

with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("golem.html patched with Lexicon markers!")
