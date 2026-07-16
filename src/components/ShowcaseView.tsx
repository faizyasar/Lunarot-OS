import { useState } from 'react';
import { Typewriter, HoverText } from './Effects';
import { SmokyText } from './SmokyText';

export function AestheticTokensCard() {
  return (
    <div className="gothic-panel panel-gold" style={{ width: '100%', display: 'flex', flexDirection: 'column' }}>
      <span className="panel-title-tag">AESTHETIC_TOKENS</span>
      <span className="panel-footer-tag">THEME_ROOT</span>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
        <p style={{ color: 'rgba(255,255,255,0.4)', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '0.2em', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: 4, fontSize: 8 }}>
          ◆ Core Color Swatches
        </p>
        <div className="swatch-grid">
          <div className="swatch-item">
            <div className="swatch-box" style={{ backgroundColor: '#000000' }}></div>
            <span style={{ color: 'rgba(255,255,255,0.4)' }}>void</span>
            <span style={{ color: 'rgba(255,255,255,0.3)' }}>#000000</span>
          </div>
          <div className="swatch-item">
            <div className="swatch-box" style={{ backgroundColor: '#080808' }}></div>
            <span style={{ color: 'rgba(255,255,255,0.4)' }}>ash</span>
            <span style={{ color: 'rgba(255,255,255,0.3)' }}>#080808</span>
          </div>
          <div className="swatch-item">
            <div className="swatch-box" style={{ backgroundColor: '#c8a45a' }}></div>
            <span style={{ color: 'var(--gold)' }}>gold</span>
            <span style={{ color: 'rgba(255,255,255,0.3)' }}>#c8a45a</span>
          </div>
          <div className="swatch-item">
            <div className="swatch-box" style={{ backgroundColor: '#efede8' }}></div>
            <span style={{ color: 'rgba(255,255,255,0.4)' }}>parchment</span>
            <span style={{ color: 'rgba(255,255,255,0.3)' }}>#efede8</span>
          </div>
          <div className="swatch-item">
            <div className="swatch-box" style={{ backgroundColor: '#ffffff' }}></div>
            <span style={{ color: 'rgba(255,255,255,0.4)' }}>cream</span>
            <span style={{ color: 'rgba(255,255,255,0.3)' }}>#ffffff</span>
          </div>
        </div>

        <div className="typo-sample" style={{ marginTop: 8 }}>
          <p style={{ color: 'rgba(255,255,255,0.4)', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '0.2em', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: 4, fontSize: 8 }}>
            ◆ Typography Scales
          </p>
          <div>
            <span className="typo-tag">// CINZEL SERIF (HEADERS)</span>
            <div style={{ height: 24, display: 'flex', justifyContent: 'flex-start' }}>
              <SmokyText 
                text="Sacred Conflux" 
                font={{ fontFamily: '"Cinzel", serif', fontSize: '16px', fontWeight: 800, letterSpacing: '0.1em', textTransform: 'uppercase', textAlign: 'left' }}
                color="var(--gold)"
                intensity={12}
              />
            </div>
          </div>
          <div>
            <span className="typo-tag">// GARAMOND SERIF (PROSE/POETRY)</span>
            <p className="font-garamond text-sm italic" style={{ color: '#cfc9c0', fontSize: 12, lineHeight: 1.5 }}>
              The ritual has begun. Your birth coordinates are unsealed inside our cloud matrices.
            </p>
          </div>
          <div>
            <span className="typo-tag">// JETBRAINS MONO (OS DETAILS)</span>
            <p className="font-mono" style={{ fontSize: 8.5, color: 'rgba(255,255,255,0.7)', letterSpacing: '0.15em' }}>
              SYS.REGISTRY_0x9FA2 // TELEMETRY CONNECT ONLINE
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}

export function AsciiControlCard() {
  const dispatchEyeCommand = (action: string, targetId?: string, duration?: number) => {
    window.dispatchEvent(
      new CustomEvent('ascii-eyes-control-custom', {
        detail: { action, targetId, duration },
      })
    );
  };
  
  return (
    <div className="gothic-panel panel-gold" style={{ width: '100%', display: 'flex', flexDirection: 'column' }}>
      <span className="panel-title-tag">ATMOSPHERE_TELEMETRY</span>
      <span className="panel-footer-tag">OS_EYES_CONTROL</span>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        <p style={{ color: 'rgba(255,255,255,0.4)', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '0.2em', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: 4, fontSize: 8 }}>
          ◆ Background ASCII Eyes Telemetry
        </p>
        <p className="font-garamond" style={{ fontSize: 11.5, color: '#cfc9c0', lineHeight: 1.5 }}>
          The background tracking eyes are rendered inside a preformatted grid. Use these overrides to command their focus or trigger wild alchemical spasms:
        </p>
        <div className="control-actions" style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
          <button onClick={() => dispatchEyeCommand('crazy', undefined, 4000)} className="gothic-btn btn-secondary" style={{ padding: '6px 12px', fontSize: 7.5 }}>
            ◆ TRIGGER CRAZY MODE
          </button>
          <button id="showcaseEyeTrack" onClick={() => dispatchEyeCommand('track-element', 'showcaseEyeTrack', 4000)} className="gothic-btn btn-secondary" style={{ padding: '6px 12px', fontSize: 7.5 }}>
            ◆ LOCK TRACK BUTTON
          </button>
          <button onClick={() => dispatchEyeCommand('reset')} className="gothic-btn btn-primary" style={{ padding: '6px 12px', fontSize: 7.5 }}>
            ◆ RESET TRACKING
          </button>
        </div>
      </div>
    </div>
  )
}

export function SacredInputFieldsCard() {
  return (
    <div className="gothic-panel panel-white" style={{ width: '100%', display: 'flex', flexDirection: 'column' }}>
      <span className="panel-title-tag">SACRED_INPUT_FIELDS</span>
      <span className="panel-footer-tag">FORM_ELEMENTS</span>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
          <div className="gothic-input-group">
            <div className="input-header-line"><span>◆ Text Identifier</span></div>
            <div className="input-row">
              <span className="input-label">TOKEN_ID :</span>
              <input type="text" className="input-field input-field-text" defaultValue="VESSEL_PLAYGROUND" />
            </div>
          </div>
          <div className="gothic-input-group">
            <div className="input-header-line"><span>◆ Solar Alignment</span></div>
            <div className="input-row">
              <span className="input-label">SOLAR_EPOCH :</span>
              <input type="date" className="input-field input-field-date" defaultValue="2026-06-24" />
            </div>
          </div>
          <div className="gothic-input-group">
            <div className="input-header-line"><span>◆ Temporal Axis</span></div>
            <div className="input-row">
              <span className="input-label">TEMP_AXIS :</span>
              <input type="time" className="input-field input-field-time" defaultValue="19:24" />
            </div>
          </div>
          <div className="gothic-input-group">
            <div className="input-header-line"><span>◆ Registry Dropdown</span></div>
            <div className="input-row">
              <span className="input-label">SELECT_VAL :</span>
              <select className="input-select" defaultValue="sec_4">
                <option value="sec_1">SECTOR I: ANTECEDENT</option>
                <option value="sec_2">SECTOR II: CONCURRENT</option>
                <option value="sec_3">SECTOR III: CONSEQUENT</option>
                <option value="sec_4">SECTOR IV: WATCHGATE</option>
              </select>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export function PoeticTypographyCard() {
  const [replayKey, setReplayKey] = useState(0);
  return (
    <div className="gothic-panel panel-gold" style={{ width: '100%', display: 'flex', flexDirection: 'column' }}>
      <span className="panel-title-tag">POETIC_TYPOGRAPHY</span>
      <span className="panel-footer-tag">ETCH_SEQUENCE</span>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
        <div>
          <span className="typo-tag">// INTERACTIVE CHAR HOVER</span>
          <HoverText 
            text="Hover your mouse over this text block to watch characters rotate and scale dynamically."
            className="font-garamond" 
            style={{ fontSize: 13, letterSpacing: '0.05em' }}
          />
        </div>
        
        <div style={{ borderTop: '1px solid rgba(255, 255, 255, 0.05)', paddingTop: 12 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
            <span className="typo-tag">// FLAME ETCHED TYPEWRITER PRINTING</span>
            <button onClick={() => setReplayKey(k => k + 1)} className="gothic-btn btn-secondary" style={{ padding: '4px 10px', fontSize: 7 }}>
              RE-PLAY ETCH
            </button>
          </div>
          <Typewriter 
            key={replayKey}
            className="typewriter-playground font-garamond"
            style={{ fontSize: 11.5, lineHeight: 1.6 }}
            text="Charged *terms* ignite into Arabic glyphs, then fade to *glowing* words. Normal sentences typewrite regularly."
            chargedList={['terms', 'glowing']}
          />
        </div>
      </div>
    </div>
  )
}

export function IntegrationGuideCard() {
  return (
    <div className="gothic-panel panel-gold" style={{ width: '100%', display: 'flex', flexDirection: 'column' }}>
      <span className="panel-title-tag">INTEGRATION_GUIDE</span>
      <span className="panel-footer-tag">CODE_COPY</span>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
        <p style={{ color: 'rgba(255,255,255,0.4)', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '0.2em', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: 4, fontSize: 8 }}>
          ◆ Static HTML Layout Structure
        </p>
        <div className="font-sans" style={{ fontSize: 10.5, lineHeight: 1.5, color: '#cfc9c0' }}>
          Copy this clean HTML template directly into your static code blocks to construct a baseline:
        </div>
        <div className="code-block">
{`<div class="gothic-panel panel-gold">
  <span class="panel-title-tag">SECURE_GATE</span>
  <p>Content here...</p>
  <span class="panel-footer-tag">V.1.0</span>
</div>

<button class="gothic-btn btn-primary">Execute Link</button>
<button class="gothic-btn btn-secondary">Ritual Shield</button>`}
        </div>
      </div>
    </div>
  )
}
