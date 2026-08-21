import re

filepath = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
old_kf_css = """  /* Floating Text (3D Tracked) */
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
  }"""
new_kf_css = """  /* Floating Text (3D Tracked) */
  .knowledge-floating {
    position: absolute;
    text-align: center;
    text-shadow: 0 0 20px rgba(0,0,0,0.9), 0 0 10px rgba(0,0,0,1);
    opacity: 0;
    transform: translate(-50%, -50%) translateY(20px);
    transition: opacity 0.4s ease, transform 0.4s ease;
    pointer-events: none;
    max-width: 400px;
  }
  .knowledge-overlay.visible .knowledge-floating {
    opacity: 1;
    transform: translate(-50%, -50%);
  }
  .kf-description {
    font-size: 13px;
    font-family: 'Inter', sans-serif;
    color: rgba(255, 255, 255, 0.8);
    line-height: 1.6;
    margin-top: 16px;
    text-align: center;
  }"""
content = content.replace(old_kf_css, new_kf_css)

# Hide SVG
old_svg_css = """  /* SVG HUD Lines */
  .hud-svg-layer {"""
new_svg_css = """  /* SVG HUD Lines */
  .hud-svg-layer { display: none; """
content = content.replace(old_svg_css, new_svg_css)

# Hide Grimoire
old_grim_css = """  /* Glassmorphic Grimoire */
  .knowledge-grimoire {"""
new_grim_css = """  /* Glassmorphic Grimoire */
  .knowledge-grimoire { display: none; """
content = content.replace(old_grim_css, new_grim_css)

# Fix floating text css transition rule that was left over
old_trans = """  .knowledge-overlay.visible .knowledge-floating {
    opacity: 1;
    transform: translateY(0);
  }"""
if old_trans in content:
    content = content.replace(old_trans, "  /* original transition removed */")

# 2. Add description to HTML
old_kf_html = """    <!-- Floating Text -->
    <div id="knowledge-floating" class="knowledge-floating">
      <div id="kf-hebrew" class="kf-hebrew">כֶּתֶר</div>
      <div id="kf-title" class="kf-title">Crown / The First</div>
      <div id="kf-meaning" class="kf-meaning">Primordial Will / The One</div>
    </div>"""
new_kf_html = """    <!-- Floating Text -->
    <div id="knowledge-floating" class="knowledge-floating">
      <div id="kf-hebrew" class="kf-hebrew">כֶּתֶר</div>
      <div id="kf-title" class="kf-title">Crown / The First</div>
      <div id="kf-meaning" class="kf-meaning">Primordial Will / The One</div>
      <div id="kf-description" class="kf-description"></div>
    </div>"""
content = content.replace(old_kf_html, new_kf_html)

# 3. Update JS Logic
old_js_update = """    // Update Floating Text
    document.getElementById('kf-hebrew').textContent = node.hebrew;
    document.getElementById('kf-title').textContent = node.name;
    document.getElementById('kf-meaning').textContent = node.meaning;
    
    // Update Grimoire"""
new_js_update = """    // Update Floating Text
    document.getElementById('kf-hebrew').textContent = node.hebrew;
    document.getElementById('kf-title').textContent = node.name;
    document.getElementById('kf-meaning').textContent = node.meaning;
    document.getElementById('kf-description').textContent = node.description;
    
    // Update Grimoire"""
content = content.replace(old_js_update, new_js_update)

# 4. Remove offsets from render loop
old_offset = """    // Offset for the floating text
    const offsetX = 80;
    const offsetY = -60;"""
new_offset = """    // Offset for the floating text
    const offsetX = 0;
    const offsetY = 0;"""
content = content.replace(old_offset, new_offset)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script executed successfully.")
