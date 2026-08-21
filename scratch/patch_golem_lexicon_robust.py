import os

def insert_before(lines, target, content):
    for i, line in enumerate(lines):
        if target in line:
            lines.insert(i, content + '\n')
            return True
    return False

def insert_after(lines, target, content):
    for i, line in enumerate(lines):
        if target in line:
            lines.insert(i + 1, content + '\n')
            return True
    return False

with open('golem.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

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
if not any("Floating Lexicon Markers" in l for l in lines):
    insert_before(lines, "</style>", css_to_add)

# 2. HTML Container
html_to_add = '  <div id="lexicon-markers-container"></div>'
if not any('id="lexicon-markers-container"' in l for l in lines):
    insert_before(lines, '<div id="sephirot-overlay">', html_to_add)

# Read JSON Data
with open('scratch/lexicon_dump.json', 'r', encoding='utf-8') as lf:
    lexicon_data = lf.read()

# 3. Lexicon Data & Mapping
js_data = f"""
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
"""
if not any("const lexiconData" in l for l in lines):
    insert_before(lines, "const sephirotMeshMap = {", js_data)

# 4. initLexiconMarkers Function
js_init = """
  function initLexiconMarkers() {
    const container = document.getElementById('lexicon-markers-container');
    if (!container) return;
    
    lexiconData.forEach(item => {
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
      
      let cardHTML = `<div class="lc-term">${item.term}</div>`;
      if (item.hebrew) cardHTML += `<div class="lc-hebrew">${item.hebrew}</div>`;
      if (item.linguisticRoot) cardHTML += `<div class="lc-root">${item.linguisticRoot}</div>`;
      if (item.definition) cardHTML += `<div class="lc-def">${item.definition}</div>`;
      if (item.mysticalSignificance) cardHTML += `<div class="lc-mystic">${item.mysticalSignificance}</div>`;
      
      card.innerHTML = cardHTML;
      
      marker.appendChild(dot);
      marker.appendChild(label);
      marker.appendChild(card);
      container.appendChild(marker);
      
      lexiconDOMNodes[item.id] = { el: marker, boneName: boneName, mesh: null };
    });
  }
"""
if not any("function initLexiconMarkers" in l for l in lines):
    # Insert after the end of initSephirotMarkers
    # We find initSephirotMarkers, then look for its closing brace
    for i, line in enumerate(lines):
        if "function initSephirotMarkers()" in line:
            # simple assumption: it ends before DOMContentLoaded
            break
    insert_before(lines, "document.addEventListener('DOMContentLoaded', initSephirotMarkers);", js_init)

# 5. Add DOMContentLoaded for lexicon
if not any("initLexiconMarkers);" in l for l in lines):
    insert_after(lines, "document.addEventListener('DOMContentLoaded', initSephirotMarkers);", "  document.addEventListener('DOMContentLoaded', initLexiconMarkers);")

# 6. Lexicon Mesh Mapping Loop
mesh_map_logic = """
    // Populate lexicon meshes
    scene.transformNodes.forEach(node => {
      for (const [id, data] of Object.entries(lexiconDOMNodes)) {
         if (node.name && node.name.includes(data.boneName)) {
            data.mesh = node;
         }
      }
    });
    scene.meshes.forEach(mesh => {
      for (const [id, data] of Object.entries(lexiconDOMNodes)) {
         if (mesh.name && mesh.name.includes(data.boneName)) {
            data.mesh = mesh;
         }
      }
    });
"""
if not any("Populate lexicon meshes" in l for l in lines):
    # insert right before scene.onBeforeRenderObservable.add
    insert_before(lines, "scene.onBeforeRenderObservable.add(() => {", mesh_map_logic)

# 7. Lexicon UI Update Loop
render_loop_logic = """
        // Lexicon Telemetry
        const showLexicon = true; // Always show floating text
        
        for (const [id, data] of Object.entries(lexiconDOMNodes)) {
           if (!data.mesh) continue;
           
           const dist = BABYLON.Vector3.Distance(cam.position, data.mesh.getAbsolutePosition());
           
           const pos = data.mesh.getAbsolutePosition();
           const proj = BABYLON.Vector3.Project(
               pos,
               BABYLON.Matrix.Identity(),
               scene.getTransformMatrix(),
               cam.viewport.toGlobal(engine.getRenderWidth(), engine.getRenderHeight())
           );
           
           if (proj.z > 0 && proj.z < 1) {
               data.el.style.left = proj.x + 'px';
               data.el.style.top = proj.y + 'px';
               if (dist < 5.0 || dist > 200.0) {
                   data.el.classList.add('hidden');
               } else {
                   data.el.classList.remove('hidden');
               }
           } else {
               data.el.classList.add('hidden');
           }
        }
"""
if not any("Lexicon Telemetry" in l for l in lines):
    # Insert at the end of the render loop (before the first closing brace in that block)
    # Finding the end of the render loop is tricky, let's insert it right after the sephirotMarkers loop
    # We find 'for (const key of Object.keys(sephirotMarkers)) {' and insert after its block ends
    # A safer way: we see '             } else {\n                marker.classList.remove('visible');\n             }\n          } else {\n             marker.classList.remove('visible');\n          }\n       }' in the sephirot loop. Let's just insert before the '    });' that closes scene.onBeforeRenderObservable
    for i, line in enumerate(lines):
        if "scene.onBeforeRenderObservable.add(() => {" in line:
            start_i = i
            break
    for i in range(start_i, len(lines)):
        if "    });" in lines[i]: # end of observable
            lines.insert(i, render_loop_logic + '\n')
            break

with open('golem.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
    
print("golem.html patched with Lexicon markers! Successfully!")
