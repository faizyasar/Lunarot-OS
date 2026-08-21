import re

with open('golem.html', 'r', encoding='utf-8') as f:
    content = f.read()

css_addition = """
  /* Sephirot Overlay */
  #sephirot-overlay {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 5;
  }
  .sephirah-marker {
    position: absolute;
    transform: translate(-50%, -50%);
    font-family: 'Cinzel', serif;
    font-size: 11px;
    color: #ffffff;
    text-shadow: 0 0 10px rgba(0,0,0,0.8), 0 0 5px rgba(255,255,255,0.4);
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.5s ease;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
  }
  .sephirah-marker.visible {
    opacity: 1;
  }
  .sephirah-marker .hebrew {
    font-family: 'Times New Roman', serif;
    font-size: 18px;
    color: rgba(255, 255, 255, 0.95);
  }
  .sephirah-marker .dot {
    width: 4px;
    height: 4px;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 50%;
    box-shadow: 0 0 8px white;
    margin-top: 4px;
  }
"""
if '/* Sephirot Overlay */' not in content:
    content = content.replace('</style>', css_addition + '</style>')

html_addition = '<div id="sephirot-overlay"></div>'
if html_addition not in content:
    content = content.replace('<video id="crt-video"', html_addition + '\n  <video id="crt-video"')

js_init = """
  const sephirotMeshMap = {
    'keter': 'Frontal bone',
    'chokhmah': 'Temporal bone.l',
    'binah': 'Temporal bone.r',
    'daat': 'Vertebra C3',
    'chesed': 'Humerus.l',
    'gevurah': 'Humerus.r',
    'tiferet': 'Body of sternum',
    'netzach': 'Femur.l',
    'hod': 'Femur.r',
    'yesod': 'Sacrum',
    'malkhut': 'Talus.l'
  };

  let sephirotMarkers = {};
  let trackedMeshes = {};

  function initSephirotMarkers() {
    const container = document.getElementById('sephirot-overlay');
    if (!container || typeof mysticalData === 'undefined') return;
    
    mysticalData.forEach(node => {
      const div = document.createElement('div');
      div.className = 'sephirah-marker';
      div.id = 'marker-' + node.id;
      
      const hebrew = document.createElement('div');
      hebrew.className = 'hebrew';
      hebrew.textContent = node.hebrew;
      
      const name = document.createElement('div');
      name.textContent = node.name;
      
      const dot = document.createElement('div');
      dot.className = 'dot';
      
      div.appendChild(hebrew);
      div.appendChild(name);
      div.appendChild(dot);
      container.appendChild(div);
      
      sephirotMarkers[node.id] = div;
    });
  }
  
  // Call once data is loaded
  document.addEventListener('DOMContentLoaded', initSephirotMarkers);
"""

if 'initSephirotMarkers' not in content:
    content = content.replace('// Map presets to node IDs', js_init + '\n\n  // Map presets to node IDs')

js_tracker = """
    // Map meshes for Sephirah tracking
    scene.meshes.forEach(mesh => {
      for (const [key, meshName] of Object.entries(sephirotMeshMap)) {
         if (mesh.name === meshName) {
            trackedMeshes[key] = mesh;
         }
      }
    });

    scene.onBeforeRenderObservable.add(() => {
       const showMarkers = (window.activePresetKey === 'full');
       
       for (const key of Object.keys(sephirotMarkers)) {
          const marker = sephirotMarkers[key];
          if (showMarkers && trackedMeshes[key]) {
             const mesh = trackedMeshes[key];
             // get the center of the bounding box for more accurate placement
             const pos = mesh.getBoundingInfo().boundingBox.centerWorld;
             
             let proj = BABYLON.Vector3.Project(
                pos,
                BABYLON.Matrix.Identity(),
                scene.getTransformMatrix(),
                cam.viewport.toGlobal(engine.getRenderWidth(), engine.getRenderHeight())
             );
             
             if (proj.z > 0 && proj.z < 1) {
                marker.style.left = proj.x + 'px';
                marker.style.top = proj.y + 'px';
                marker.classList.add('visible');
             } else {
                marker.classList.remove('visible');
             }
          } else {
             marker.classList.remove('visible');
          }
       }
    });
"""

if 'scene.onBeforeRenderObservable.add(' not in content:
    content = content.replace('// Auto-focus full body on load', js_tracker + '\n\n    // Auto-focus full body on load')


with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Successfully patched golem.html')
