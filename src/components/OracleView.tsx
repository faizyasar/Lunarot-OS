import { useState } from 'react';
import { CompactEye } from './Backgrounds';
import { Typewriter } from './Effects';
import { SmokyText } from './SmokyText';

const BOOT_LOGS = [
  '◆ [0xCC0110] BIND SECURE PORTS TO HOST 0.0.0.0... [OK]',
  '✦ [0x8FA12B] SYNCHRONIZING METEORIC DRIFT TO SOLAR CORRIDORS... [OK]',
  '✦ [0x098A2F] INTERPOLATING LUNAR CONVICTION MATRIX... [OK]',
  '◆ [0xEE334A] INJECTING FAUSTIAN REGISTRY COOKIES UNSEALED... [OK]',
  '◆ [0x12FF88] INITIATING DIRECT CHANNELS WITH CHANCELLERY OF THE VOID... [OK]',
  '✦ [0xAA99E1] SECURE NATAL DESCENT HANDSHAKE COMPLETE // WARNING: REGISTRY READY',
];

export function OracleGateCard() {
  const [stage, setStage] = useState<'intake' | 'boot' | 'gate'>('intake');
  const [progress, setProgress] = useState(0);

  const handleExecute = () => {
    setStage('boot');
    setProgress(0);
    
    const interval = setInterval(() => {
      setProgress((prev) => {
        const next = prev + Math.floor(Math.random() * 8) + 6;
        if (next >= 100) {
          clearInterval(interval);
          setTimeout(() => setStage('gate'), 500);
          return 100;
        }
        return next;
      });
    }, 100);
  };

  const handleRecoil = () => {
    setStage('intake');
  };

  const currentLogIdx = Math.min(Math.floor((progress / 100) * BOOT_LOGS.length), BOOT_LOGS.length - 1);
  const blocks = Math.floor(progress / 4);
  const asciiProgress = `[${'█'.repeat(blocks)}${'░'.repeat(25 - blocks)}]`;

  return (
    <div className="gothic-panel panel-gold" style={{ width: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
      
      {/* ─── INTAKE SCREEN ─── */}
      {stage === 'intake' && (
        <div className="intake-container" style={{ width: '100%' }}>
          <div style={{ textAlign: 'center', marginBottom: 8, width: '100%' }}>
            <div style={{ fontFamily: '"JetBrains Mono", monospace', fontSize: 7, color: 'rgba(255,255,255,0.4)', letterSpacing: '0.45em', textTransform: 'uppercase', marginBottom: 4 }}>
              // LUNAROT ENGINE OS //
            </div>
            <div style={{ height: 24, marginBottom: 8, display: 'flex', justifyContent: 'center' }}>
              <SmokyText 
                text="REGISTRY LOG-IN" 
                font={{ fontFamily: '"Cinzel", serif', fontSize: '16px', fontWeight: 800, letterSpacing: '0.3em', textTransform: 'uppercase' }}
                color="var(--parchment)"
                intensity={12}
              />
            </div>
          </div>

          <div className="compact-eye-box" style={{ marginBottom: 24 }}>
            <CompactEye />
          </div>

          <div style={{ width: '100%', padding: '0 8px 24px 8px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
              <span className="panel-title-tag" style={{ position: 'relative', left: 0, top: 0 }}>CONDUIT ADDR</span>
              <span className="panel-footer-tag" style={{ position: 'relative', right: 0, bottom: 0 }}>RE_ENTRY</span>
            </div>
            
            <div className="gothic-input-group" style={{ marginTop: 10 }}>
              <div className="input-row">
                <span className="input-label">TOKEN_ID :</span>
                <input type="text" maxLength={20} placeholder="VESSEL_N" className="input-field input-field-text" defaultValue="COGNITION_VESSEL" />
              </div>
              <div className="input-row">
                <span className="input-label">SOLAR_EPOCH :</span>
                <input type="date" className="input-field input-field-date" defaultValue="1999-08-11" />
              </div>
              <div className="input-row" style={{ border: 'none' }}>
                <span className="input-label">TEMP_AXIS :</span>
                <input type="time" className="input-field input-field-time" defaultValue="12:12" />
              </div>
            </div>
          </div>

          <div style={{ width: '100%', textAlign: 'center' }}>
            <button onClick={handleExecute} className="gothic-btn btn-primary btn-full">
              ◆ EXECUTE SYSTEM LINK // BOOT OS
            </button>
            <div style={{ fontFamily: '"JetBrains Mono", monospace', fontSize: 6, letterSpacing: '0.25em', color: 'rgba(255,255,255,0.3)', textTransform: 'uppercase', marginTop: 8 }}>
              PORT 3000 // CHANCELLERY OF THE VOID
            </div>
          </div>
        </div>
      )}

      {/* ─── BOOT SCREEN ─── */}
      {stage === 'boot' && (
        <div className="boot-loader-box" style={{ display: 'block', width: '100%' }}>
          <div className="boot-header">
            <span>[ LUNAROT ENGINE OS v5.18 ]</span>
            <span style={{ color: '#ffffff', animation: 'breathe 1.5s infinite' }}>RE-LINKING CONDUIT</span>
          </div>
          <div className="boot-logs">
            {BOOT_LOGS.slice(0, currentLogIdx + 1).map((log, i) => (
              <div key={i}>{log}</div>
            ))}
          </div>
          <div className="boot-progress-bar-container">
            <div className="boot-progress-info">
              <span>INITIALIZING CHANNELS</span>
              <span>{progress}%</span>
            </div>
            <div className="boot-progress-ascii">{asciiProgress}</div>
          </div>
        </div>
      )}

      {/* ─── MAIN GATE SCREEN ─── */}
      {stage === 'gate' && (
        <div className="intake-container" style={{ width: '100%' }}>
          <div style={{ padding: 10, textAlign: 'center' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 24 }}>
              <span className="panel-title-tag" style={{ position: 'relative', left: 0, top: 0 }}>ORACLE_GATE_OPEN</span>
              <span className="panel-footer-tag" style={{ position: 'relative', right: 0, bottom: 0 }}>CONFLUX_STATUS</span>
            </div>
            
            <div style={{ height: 24, marginBottom: 12, display: 'flex', justifyContent: 'center' }}>
              <SmokyText 
                text="◆ CONSCIOUSNESS VESSEL REACHED ◆" 
                font={{ fontFamily: '"Cinzel", serif', fontSize: '14px', letterSpacing: '0.2em' }}
                color="var(--gold)"
                intensity={12}
              />
            </div>
            <div className="font-garamond" style={{ fontSize: 12, lineHeight: 1.6, color: '#cfc9c0', marginBottom: 20 }}>
              Your solar alignment epoch has been recorded inside the alchemical matrix registry. The planetary channels are drifting, ready to transmit coordinates.
            </div>
            
            <Typewriter 
              className="typewriter-playground font-garamond"
              style={{ fontSize: 11.5, textAlign: 'left', minHeight: 60 }}
              text="The *sacred* channels are locked. Solar fire meets the *poetic* coordinates of the void."
              chargedList={['sacred', 'poetic']}
            />
            
            <div style={{ marginTop: 24, display: 'flex', justifyContent: 'center', gap: 16 }}>
              <button onClick={handleRecoil} className="gothic-btn btn-secondary">
                ◆ RECOIL CONSCIOUSNESS
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}
