import re

with open('golem.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Disable snapping
content = content.replace("""rubberBandTimeout = setTimeout(() => {
            focusPreset(window.activePresetKey, false);
        }, 1500);""", """// rubberBandTimeout = setTimeout(() => {
        //    focusPreset(window.activePresetKey, false);
        // }, 1500);""")
# Just in case the indentation differs:
content = re.sub(r'rubberBandTimeout = setTimeout\(\(\) => \{\s+focusPreset\(window.activePresetKey, false\);\s+\}, 1500\);', r'// Snapping disabled', content)


# 2. Advanced Telemetry HUD
new_hud_html = """
  <!-- Camera Telemetry HUD -->
  <div id="camera-telemetry" style="position:fixed; bottom:20px; right:20px; z-index:100; font-family:'JetBrains Mono', monospace; font-size:12px; background:rgba(0,0,0,0.8); padding:10px; border:1px solid #444; color: #fff; pointer-events: auto; display: flex; flex-direction: column; gap: 4px;">
     <div id="telemetry-text">target: ..., radius: ...</div>
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

# Remove old HUD if present
if '<!-- Camera Telemetry HUD -->' in content:
    start_idx = content.find('<!-- Camera Telemetry HUD -->')
    end_idx = content.find('</div>\n', start_idx + 300)
    # Be careful here, let's just use regex replacement
    content = re.sub(r'<!-- Camera Telemetry HUD -->.*?</div>\s*</div>\s*', new_hud_html, content, flags=re.DOTALL)
    if 'TX <button' not in content:
        content = re.sub(r'<!-- Camera Telemetry HUD -->.*?COPY DATA</button>\s*</div>\s*', new_hud_html, content, flags=re.DOTALL)
else:
    # If not present, add it below render-canvas
    content = content.replace('<video id="crt-video"', new_hud_html + '\n  <video id="crt-video"')

# 3. Add styling for the new buttons
css_buttons = """
  #camera-telemetry button {
    background: #222;
    color: #fff;
    border: 1px solid #555;
    cursor: pointer;
    padding: 2px 6px;
    font-family: 'JetBrains Mono', monospace;
  }
  #camera-telemetry button:hover {
    background: #444;
  }
  #camera-telemetry .copy-coords-btn {
    background: #fff;
    color: #000;
  }
  #camera-telemetry .copy-coords-btn:hover {
    background: #ccc;
  }
"""
if '#camera-telemetry button' not in content:
    content = content.replace('</style>', css_buttons + '</style>')

with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Advanced telemetry injected and snapping disabled.")
