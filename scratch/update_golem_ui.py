import os

filepath = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert script tag
if '<script src="golem_data.js"></script>' not in content:
    content = content.replace('</head>', '  <script src="golem_data.js"></script>\n</head>')

# 2. Add UI Markup for Knowledge HUD
ui_html = """
  <!-- Knowledge HUD (Floating & Bottom Bar) -->
  <div id="knowledge-overlay" class="knowledge-overlay">
    
    <!-- Floating Text -->
    <div id="knowledge-floating" class="knowledge-floating">
      <div id="kf-hebrew" class="kf-hebrew">כֶּתֶר</div>
      <div id="kf-title" class="kf-title">Crown / The First</div>
      <div id="kf-meaning" class="kf-meaning">Primordial Will / The One</div>
    </div>

    <!-- Glassmorphic Bottom Bar (Grimoire) -->
    <div id="knowledge-grimoire" class="knowledge-grimoire">
      
      <div class="grimoire-content">
        <div class="grimoire-header">
          <h2 id="kg-title">Keter / Al-Awwal</h2>
          <span id="kg-pillar" class="kg-pillar">Center Pillar</span>
        </div>
        
        <p id="kg-description" class="kg-description"></p>
        
        <div class="grimoire-grid">
          <div class="grimoire-section">
            <h3>Linguistics</h3>
            <p><strong>Roots:</strong> <span id="kg-roots"></span></p>
            <p><strong>Etymology:</strong> <span id="kg-etym"></span></p>
            <p><strong>Cognates:</strong> <span id="kg-cog"></span></p>
          </div>
          
          <div class="grimoire-section">
            <h3>Primary Sources</h3>
            <div id="kg-sources"></div>
          </div>
        </div>
      </div>
      
    </div>
    
  </div>
"""

if 'knowledge-overlay' not in content:
    content = content.replace('<body>', '<body>\n' + ui_html)

# 3. Add CSS for Knowledge HUD
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

  /* Floating Text */
  .knowledge-floating {
    margin-top: 15vh;
    margin-right: 15vw;
    align-self: flex-end;
    text-align: right;
    text-shadow: 0 0 20px rgba(255,255,255,0.3);
    transform: translateX(20px);
    transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
  }
  .knowledge-overlay.visible .knowledge-floating {
    transform: translateX(0);
  }
  .kf-hebrew {
    font-size: 80px;
    font-family: 'Times New Roman', serif;
    color: rgba(255, 255, 255, 0.15);
    line-height: 1;
    letter-spacing: 0.1em;
    margin-bottom: -15px;
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
"""

if 'knowledge-overlay' not in content:
    content = content.replace('</style>', css_html + '\n</style>')

# 4. JS Logic Integration
js_logic = """
  // Map presets to node IDs
  const presetNodeMap = {
    'skull': ['keter', 'chokhmah', 'binah'],
    'thorax': ['tiferet'],
    'spine': ['daat', 'yesod'],
    'hands': ['chesed', 'gevurah'],
    'pelvis': ['yesod'],
    'feet': ['netzach', 'hod', 'malkhut']
  };

  function updateKnowledgeUI(presetKey) {
    const overlay = document.getElementById('knowledge-overlay');
    if (presetKey === 'full' || !presetNodeMap[presetKey]) {
      overlay.classList.remove('visible');
      return;
    }
    
    // Pick the primary node for the preset to display
    const nodeIds = presetNodeMap[presetKey];
    let primaryNodeId = nodeIds[0];
    
    // If it's a multi-node preset, we just show the first one for simplicity for now
    // We could expand this to show multiple tabs in the future
    if (presetKey === 'skull') primaryNodeId = 'keter';
    if (presetKey === 'hands') primaryNodeId = 'chesed';
    if (presetKey === 'feet') primaryNodeId = 'malkhut';
    
    if (typeof mysticalData === 'undefined') return;
    
    const node = mysticalData.find(n => n.id === primaryNodeId);
    if (!node) return;
    
    // Update Floating Text
    document.getElementById('kf-hebrew').textContent = node.hebrew;
    document.getElementById('kf-title').textContent = node.name;
    document.getElementById('kf-meaning').textContent = node.meaning;
    
    // Update Grimoire
    document.getElementById('kg-title').textContent = node.transliteration;
    document.getElementById('kg-pillar').textContent = node.pillar + ' Pillar';
    document.getElementById('kg-description').textContent = node.description;
    
    if (node.linguistics) {
      document.getElementById('kg-roots').textContent = node.linguistics.rootConsonants || '';
      document.getElementById('kg-etym').textContent = node.linguistics.etymology || '';
      document.getElementById('kg-cog').textContent = node.linguistics.cognates || '';
    }
    
    const sourcesContainer = document.getElementById('kg-sources');
    sourcesContainer.innerHTML = '';
    if (node.primarySources && node.primarySources.length > 0) {
      node.primarySources.forEach(src => {
        const card = document.createElement('div');
        card.className = 'source-card';
        card.innerHTML = `
          <div class="source-meta">${src.manuscriptName} &bull; ${src.manuscriptEra}</div>
          <p class="source-quote">"${src.quotedTextTranslation}"</p>
          <p class="source-interp">${src.scholarlyInterpretation}</p>
        `;
        sourcesContainer.appendChild(card);
      });
    }
    
    // Show UI
    overlay.classList.add('visible');
  }
"""

if 'presetNodeMap' not in content:
    # Inject before focusPreset
    content = content.replace('function focusPreset(presetKey', js_logic + '\n  function focusPreset(presetKey')

# Modify focusPreset to call updateKnowledgeUI
# Ensure we don't duplicate it
if 'updateKnowledgeUI(presetKey);' not in content:
    content = content.replace('window.activePresetKey = presetKey;', 'window.activePresetKey = presetKey;\n    updateKnowledgeUI(presetKey);')


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Updated golem.html")
