import re

with open('golem.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the CSS for knowledge-floating and knowledge-grimoire
css_replacement = """  /* Right Knowledge Panel with Negative Effect */
  .right-knowledge-panel {
    position: fixed;
    top: 50%;
    right: 32px;
    transform: translateY(-50%);
    z-index: 10;
    width: 420px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.4s ease, transform 0.4s ease;
    
    /* Negative effect */
    mix-blend-mode: difference;
    color: #ffffff;
    text-shadow: 0 0 12px rgba(255, 255, 255, 0.4);
  }
  .knowledge-overlay.visible .right-knowledge-panel {
    opacity: 1;
  }
  
  .rk-header { margin-bottom: 4px; }
  .rk-meaning { font-family: 'Cinzel', serif; font-size: 16px; font-style: italic; margin-bottom: 12px; color: rgba(255,255,255,0.95); }
  .rk-hebrew { font-family: 'Times New Roman', serif; font-size: 26px; letter-spacing: 0.02em; line-height: 1.3; margin-bottom: 2px;}
  .rk-latin { font-family: 'Cinzel', serif; font-size: 15px; margin-bottom: 2px; }
  .rk-translit { font-family: 'JetBrains Mono', monospace; font-size: 12px; letter-spacing: 0.05em; color: rgba(255,255,255,0.8); }
  
  .rk-section { display: flex; flex-direction: column; gap: 6px; }
  .rk-section-title { font-family: 'JetBrains Mono', monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; color: rgba(255,255,255,0.7); border-bottom: 1px solid rgba(255,255,255,0.3); padding-bottom: 4px; margin-bottom: 2px;}
  .rk-section-body { font-family: 'Inter', sans-serif; font-size: 12px; line-height: 1.6; color: rgba(255,255,255,0.9); }
  .rk-subsection-title { font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 600; color: rgba(255,255,255,0.95); margin-top: 2px; }
  .rk-hebrew-small { font-family: 'Times New Roman', serif; font-size: 18px; margin-bottom: 2px; }
  .rk-inline-item { font-family: 'Inter', sans-serif; font-size: 12px; color: rgba(255,255,255,0.9); }
"""

start_css = content.find('/* Floating Text (3D Tracked) */')
end_css = content.find('</style>')
if start_css != -1 and end_css != -1:
    content = content[:start_css] + css_replacement + content[end_css:]

# 2. Replace the HTML for knowledge-overlay
html_replacement = """  <!-- Knowledge HUD (Floating & Bottom Bar) -->
  <div id="knowledge-overlay" class="knowledge-overlay">
    
    <div id="right-knowledge-panel" class="right-knowledge-panel">
      <div class="rk-header">
        <div id="rk-meaning" class="rk-meaning"></div>
        <div id="rk-hebrew" class="rk-hebrew"></div>
        <div id="rk-latin" class="rk-latin"></div>
        <div id="rk-translit" class="rk-translit"></div>
      </div>
      
      <div class="rk-section">
        <div class="rk-section-title">Divine Attribute Context</div>
        <div id="rk-context" class="rk-section-body"></div>
      </div>

      <div class="rk-section">
        <div class="rk-section-title">Anatomical & Psychological Seat</div>
        <div id="rk-anatomy" class="rk-section-body"></div>
      </div>

      <div class="rk-section">
        <div class="rk-section-title">Historical Semitic Philology</div>
        <div class="rk-subsection-title">Trilateral Consonantal Root</div>
        <div id="rk-roots" class="rk-hebrew-small"></div>
        <div class="rk-inline-item"><strong>Etymological origin:</strong> <span id="rk-etym"></span></div>
      </div>

      <div class="rk-section">
        <div class="rk-section-title">Phonetic Cognates</div>
        <div id="rk-cognates" class="rk-section-body"></div>
      </div>

      <div class="rk-section">
        <div class="rk-section-title">Linguistic shifts</div>
        <div id="rk-shifts" class="rk-section-body"></div>
      </div>
    </div>
    
  </div>"""

start_html = content.find('<!-- Knowledge HUD (Floating & Bottom Bar) -->')
end_html = content.find('<!-- Background CRT Video -->')
if start_html != -1 and end_html != -1:
    content = content[:start_html] + html_replacement + '\\n\\n  ' + content[end_html:]

# 3. Replace updateKnowledgeUI
js_update_replacement = """    document.getElementById('rk-meaning').textContent = '"' + (node.meaning || '') + '"';
    document.getElementById('rk-hebrew').textContent = (node.hebrew || '') + ' / ' + (node.arabic || '');
    document.getElementById('rk-latin').textContent = node.latin || '';
    document.getElementById('rk-translit').textContent = '/' + (node.transliteration || '') + '/';
    
    document.getElementById('rk-context').textContent = node.description || '';
    document.getElementById('rk-anatomy').textContent = node.bodyPart || '';
    
    if (node.linguistics) {
      document.getElementById('rk-roots').textContent = node.linguistics.rootConsonants || '';
      document.getElementById('rk-etym').textContent = node.linguistics.etymology || '';
      document.getElementById('rk-cognates').textContent = node.linguistics.cognates || '';
      document.getElementById('rk-shifts').textContent = node.linguistics.historicalEvolution || '';
    }"""

start_js_up = content.find('// Update Floating Text')
end_js_up = content.find('// Show UI')
if start_js_up != -1 and end_js_up != -1:
    content = content[:start_js_up] + js_update_replacement + '\\n    \\n    ' + content[end_js_up:]

# 4. Remove the 3D Tracking Loop (scene.onBeforeRenderObservable.add) entirely
start_loop = content.find('// 3D HUD Tracking Loop')
end_loop = content.find('function focusPreset')
if start_loop != -1 and end_loop != -1:
    content = content[:start_loop] + content[end_loop:]

with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Script completed successfully')
