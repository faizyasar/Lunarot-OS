import re

with open('golem.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a slider for Radius (Zoom) in the HUD
new_hud_html = """
  <!-- Camera Telemetry HUD -->
  <div id="camera-telemetry" style="position:fixed; bottom:20px; right:20px; z-index:100; font-family:'JetBrains Mono', monospace; font-size:12px; background:rgba(0,0,0,0.8); padding:10px; border:1px solid #444; color: #fff; pointer-events: auto; display: flex; flex-direction: column; gap: 4px;">
     <div id="telemetry-text">target: ..., radius: ...</div>
     
     <div style="display:flex; align-items:center; gap: 8px; font-size:10px;">
        <span>ZOOM:</span>
        <input type="range" id="zoom-slider" min="5" max="400" step="1" oninput="cam.radius = parseFloat(this.value);" style="flex-grow:1;">
     </div>

     <div style="display:flex; gap: 4px; font-size:10px;">
        <button onclick="cam.target.x -= 1">-</button> TX <button onclick="cam.target.x += 1">+</button>
        <button onclick="cam.target.y -= 1">-</button> TY <button onclick="cam.target.y += 1">+</button>
        <button onclick="cam.target.z -= 1">-</button> TZ <button onclick="cam.target.z += 1">+</button>
     </div>
     <div style="display:flex; gap: 4px; font-size:10px;">
        <button onclick="cam.radius -= 1">-</button> RAD <button onclick="cam.radius += 1">+</button>
        <button onclick="cam.alpha -= 0.1">-</button> ALP <button onclick="cam.alpha += 0.1">+</button>
        <button onclick="cam.beta -= 0.1">-</button> BET <button onclick="cam.beta += 0.1">+</button>
     </div>
     <button class="copy-coords-btn" onclick="copyCameraCoords()" style="margin-top:8px; padding:5px 10px; background:#fff; color:#000; font-family:'Cinzel', serif; font-weight:bold; font-size:10px; cursor:pointer; border:none; letter-spacing:1px; width:100%;">COPY DATA</button>
  </div>
"""

content = re.sub(r'<!-- Camera Telemetry HUD -->.*?COPY DATA</button>\s*</div>', new_hud_html, content, flags=re.DOTALL)

# Also update the zoom slider's value in the render loop so it stays in sync if user uses mouse wheel
update_logic = """
       // Camera telemetry update
       const t = document.getElementById('telemetry-text');
       if(t) {
         t.innerText = `target: new BABYLON.Vector3(${cam.target.x.toFixed(1)}, ${cam.target.y.toFixed(1)}, ${cam.target.z.toFixed(1)}), radius: ${cam.radius.toFixed(1)}, alpha: ${cam.alpha.toFixed(2)}, beta: ${cam.beta.toFixed(2)}`;
         
         const zs = document.getElementById('zoom-slider');
         if(zs && document.activeElement !== zs) {
            zs.value = cam.radius;
         }
       }
"""
content = re.sub(r'// Camera telemetry update\s*const t = document.getElementById\(\'telemetry-text\'\);.*?\}', update_logic.strip(), content, flags=re.DOTALL)


with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Zoom slider added to telemetry interface.")
