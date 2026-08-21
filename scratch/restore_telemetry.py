import re

with open('golem.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add the telemetry div if not present
html_addition = """
  <!-- Camera Telemetry HUD -->
  <div id="camera-telemetry" style="position:fixed; bottom:20px; right:20px; z-index:100; font-family:'JetBrains Mono', monospace; font-size:12px; background:rgba(0,0,0,0.8); padding:10px; border:1px solid #444; color: #fff; pointer-events: auto;">
     <div id="telemetry-text">target: ..., radius: ...</div>
     <button class="copy-coords-btn" onclick="copyCameraCoords()" style="margin-top:8px; padding:5px 10px; background:#fff; color:#000; font-family:'Cinzel', serif; font-weight:bold; font-size:10px; cursor:pointer; border:none; letter-spacing:1px; width:100%;">COPY DATA</button>
  </div>
"""
if 'id="camera-telemetry"' not in content:
    content = content.replace('<video id="crt-video"', html_addition + '\n  <video id="crt-video"')

# 2. Add the update logic inside scene.onBeforeRenderObservable
# We know the tracking logic was added, let's inject it into that block
update_logic = """
       // Camera telemetry update
       const t = document.getElementById('telemetry-text');
       if(t) {
         t.innerText = `target: new BABYLON.Vector3(${cam.target.x.toFixed(1)}, ${cam.target.y.toFixed(1)}, ${cam.target.z.toFixed(1)}), radius: ${cam.radius.toFixed(1)}, alpha: ${cam.alpha.toFixed(2)}, beta: ${cam.beta.toFixed(2)}`;
       }
"""
if 'Camera telemetry update' not in content:
    content = content.replace("const showMarkers = (window.activePresetKey === 'full');", "const showMarkers = (window.activePresetKey === 'full');\n" + update_logic)

with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Telemetry restored.")
