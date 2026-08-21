import re

with open('golem.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Revert marker CSS
c = c.replace('position: relative;', 'position: absolute;')
c = c.replace('transform: none;', 'transform: translate(-50%, -50%);')
c = c.replace('align-items: flex-end;', 'align-items: center;')
c = c.replace('text-align: right;', 'text-align: center;')

# 2. Revert sephirot-overlay CSS
old_overlay = '''  #sephirot-overlay {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 5;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-end;
    padding-right: 80px;
    gap: 12px;
  }'''
new_overlay = '''  #sephirot-overlay {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 5;
  }'''
c = c.replace(old_overlay, new_overlay)

# 3. Add Iframe HTML
iframe_html = '''  <div id="sephirot-overlay"></div>
  <iframe id="full-lexicon-iframe" src="lexicon.html" style="position: fixed; right: 0; top: 0; width: 45%; height: 100%; border: none; display: none; z-index: 4;"></iframe>'''
c = c.replace('  <div id="sephirot-overlay"></div>', iframe_html)

# 4. Revert JS tracking loop
tracking_loop_regex = r"for\s*\(\s*const key of Object\.keys\(sephirotMarkers\)\s*\)\s*\{\s*const marker = sephirotMarkers\[key\];\s*if\s*\(showMarkers\)\s*\{\s*marker\.classList\.add\('visible'\);\s*// Hide the white dot since it's a lexicon now\s*const dot = marker\.querySelector\('\.dot'\);\s*if\s*\(dot\)\s*dot\.style\.display\s*=\s*'none';\s*\}\s*else\s*\{\s*marker\.classList\.remove\('visible'\);\s*\}\s*\}"

new_tracking_loop = """for (const key of Object.keys(sephirotMarkers)) {
          const marker = sephirotMarkers[key];
          if (showMarkers && trackedMeshes[key]) {
             let pos = trackedMeshes[key].getBoundingInfo().boundingBox.centerWorld;
             let proj = BABYLON.Vector3.Project(
                pos,
                BABYLON.Matrix.Identity(),
                scene.getTransformMatrix(),
                cam.viewport.toGlobal(engine.getRenderWidth(), engine.getRenderHeight())
             );
             if (proj.z > 0 && proj.z < 1) {
                let xPct = (proj.x / engine.getRenderWidth()) * 100;
                let yPct = (proj.y / engine.getRenderHeight()) * 100;
                marker.style.left = xPct + '%';
                marker.style.top = yPct + '%';
                marker.classList.add('visible');
             } else {
                marker.classList.remove('visible');
             }
          } else {
             marker.classList.remove('visible');
          }
       }"""

c = re.sub(tracking_loop_regex, new_tracking_loop, c, flags=re.DOTALL)


with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Reverted CSS, restored 3D tracking, and added iframe HTML.')
