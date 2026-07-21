import { useState, useEffect, useRef } from 'react';
import { getSunSign, getMoonSign, getRisingSign, toJD, SIGN_NAMES, NatalUser } from './merged/types';
import lunarotLogo from './lunarot_logo.webp';

const BOOT_LOGS_TIMELINE = [
  { prg: 5, log: '◆ [0xCC0110] BIND SECURE PORTS TO HOST 0.0.0.0... [OK]' },
  { prg: 20, log: '✦ [0x8FA12B] SYNCHRONIZING METEORIC DRIFT TO SOLAR CORRIDORS... [OK]' },
  { prg: 24, log: '⚠️ [0x77BE1D] DETECTED PLANETARY INTERFERENCE DRIFT...', delay: 450 },
  { prg: 25, log: '✦ RETRYING CONDUIT CONNECTION (Attempt 1/2)... [OK]' },
  { prg: 40, log: '✦ [0x098A2F] INTERPOLATING LUNAR CONVICTION MATRIX... [OK]' },
  { prg: 58, log: '⚠️ [0xEE120A] NATAL ENGINE DE-SYNCHRONIZATION ERROR...', delay: 500 },
  { prg: 59, log: '✦ FORCE ALIGNING GEOCENTRIC LONGITUDES... [OK]' },
  { prg: 70, log: '◆ [0xEE334A] INJECTING FAUSTIAN REGISTRY COOKIES UNSEALED... [OK]' },
  { prg: 80, log: '✦ RE-ROUTING STREAM THROUGH KABBALISTIC GATEWAY... [OK]', delay: 350 },
  { prg: 85, log: '◆ [0x12FF88] INITIATING DIRECT CHANNELS WITH CHANCELLERY OF THE VOID... [OK]' },
  { prg: 100, log: '✦ [0xAA99E1] SECURE NATAL DESCENT HANDSHAKE COMPLETE // WARNING: REGISTRY READY' }
];

export function OracleGateCard({ onSystemBoot }: { onSystemBoot?: (user: NatalUser) => void }) {
  const [stage, setStage] = useState<'intake' | 'boot' | 'gate'>('intake');
  const [progress, setProgress] = useState(0);
  const [tokenId, setTokenId] = useState("COGNITION_VESSEL");
  const [solarEpoch, setSolarEpoch] = useState("1999-08-11");
  const [tempAxis, setTempAxis] = useState("12:12");
  const [bootLogs, setBootLogs] = useState<string[]>([]);

  const hasInteractedRef = useRef(false);

  useEffect(() => {
    // Start-up text cycling re-type reveal
    let isCancelled = false;
    
    const cycle = async () => {
      await new Promise(r => setTimeout(r, 2000));
      if (isCancelled || hasInteractedRef.current) return;

      const words = ["PILOT_SOUL", "GUEST_VESSEL", "FAIZ_YASAR", "COGNITION_VESSEL"];

      for (const word of words) {
        if (isCancelled || hasInteractedRef.current) return;

        // Delete characters
        let current = tokenId;
        while (current.length > 0) {
          if (isCancelled || hasInteractedRef.current) return;
          current = current.substring(0, current.length - 1);
          setTokenId(current);
          await new Promise(r => setTimeout(r, 45));
        }

        await new Promise(r => setTimeout(r, 200));

        // Type characters
        for (let i = 0; i < word.length; i++) {
          if (isCancelled || hasInteractedRef.current) return;
          current += word[i];
          setTokenId(current);
          await new Promise(r => setTimeout(r, 65));
        }

        await new Promise(r => setTimeout(r, 1200));
      }
    };

    cycle();

    return () => {
      isCancelled = true;
    };
  }, []);

  const stopCycle = () => {
    hasInteractedRef.current = true;
  };

  const handleExecute = () => {
    stopCycle();
    setStage('boot');
    setProgress(0);
    setBootLogs([]);
    
    const nextStep = (p: number, idx: number) => {
      if (p >= 100) {
        setProgress(100);
        
        // Append any remaining logs
        const finalLogs: string[] = [];
        for (let i = idx; i < BOOT_LOGS_TIMELINE.length; i++) {
          finalLogs.push(BOOT_LOGS_TIMELINE[i].log);
        }
        if (finalLogs.length > 0) {
          setBootLogs(prev => [...prev, ...finalLogs]);
        }

        // Compute real natal details
        const [year, month, day] = solarEpoch.split('-').map(Number);
        let birthHour = 12;
        if (tempAxis) {
          const [h, m] = tempAxis.split(':').map(Number);
          birthHour = h + m / 60;
        }
        const jd = toJD(year, month, day, birthHour);
        const sunIdx = getSunSign(month, day);
        const moonIdx = getMoonSign(jd);
        const risingIdx = tempAxis ? getRisingSign(jd, birthHour) : null;

        const userObj: NatalUser = {
          sun: SIGN_NAMES[sunIdx],
          moon: SIGN_NAMES[moonIdx],
          rising: risingIdx !== null ? SIGN_NAMES[risingIdx] : null,
          hasRising: risingIdx !== null,
          name: tokenId.trim() || 'COGNITION_VESSEL',
          sunIdx,
          moonIdx,
          risingIdx,
          jd
        };

        setTimeout(() => {
          if (onSystemBoot) {
            onSystemBoot(userObj);
          } else {
            setStage('gate');
          }
        }, 800);
        return;
      }

      // Check logs to add
      let nextIdx = idx;
      let addedLog = false;
      let nextLogDelay = 0;
      const logsToAdd: string[] = [];

      while (nextIdx < BOOT_LOGS_TIMELINE.length && p >= BOOT_LOGS_TIMELINE[nextIdx].prg) {
        logsToAdd.push(BOOT_LOGS_TIMELINE[nextIdx].log);
        if (BOOT_LOGS_TIMELINE[nextIdx].delay) {
          nextLogDelay = Math.max(nextLogDelay, BOOT_LOGS_TIMELINE[nextIdx].delay);
        }
        nextIdx++;
        addedLog = true;
      }

      if (addedLog) {
        setBootLogs(prev => [...prev, ...logsToAdd]);
      }

      setProgress(p);

      const baseDelay = Math.floor(Math.random() * 40) + 30;
      const totalDelay = nextLogDelay > 0 ? nextLogDelay : baseDelay;

      setTimeout(() => {
        const increment = Math.floor(Math.random() * 5) + 3;
        nextStep(p + increment, nextIdx);
      }, totalDelay);
    };

    nextStep(0, 0);
  };

  const handleReSeed = () => {
    stopCycle();
    setTokenId("COGNITION_VESSEL");
    setSolarEpoch("1999-08-11");
    setTempAxis("12:12");
    setStage('intake');
  };

  const blocks = Math.floor(progress / 4);
  const asciiProgress = `[${'█'.repeat(blocks)}${'░'.repeat(25 - blocks)}]`;

  return (
    <div className="screen select-none">
      {/* top metallic bar */}
      <div className="bar-top"></div>
      
      {/* black band under top bar */}
      <div className="band-top"></div>

      {/* main panel region */}
      <div className="panels">
        {/* Left Panel */}
        <div className="panel panel-left">
          <div className="edge-top"></div>
          <div className="edge-bottom"></div>
          <div className="mark-wrap">
            <img 
              className="mark anim-fade-up" 
              src={lunarotLogo} 
              alt="LUNAROT Logo" 
            />
          </div>
        </div>

        {/* Gap Mid */}
        <div className="gap-mid"></div>

        {/* Right Panel */}
        <div className="panel panel-right">
          <div className="edge-top"></div>
          <div className="edge-bottom"></div>

          {stage === 'intake' && (
            <>
              {/* Form Input fields */}
              <div className="fields">
                <div className="anim-blur-in" style={{ animationDelay: '0.75s', marginBottom: '1.8vh', display: 'flex', flexDirection: 'column' }}>
                  <label style={{ fontSize: '8px', textTransform: 'uppercase', letterSpacing: '0.25em', color: 'rgba(255,255,255,0.4)', fontFamily: 'Tahoma, sans-serif', fontStyle: 'normal', fontWeight: 'bold', marginBottom: '2px' }}>
                    TOKEN ID
                  </label>
                  <input 
                    type="text" 
                    maxLength={20}
                    value={tokenId}
                    onChange={e => {
                      stopCycle();
                      setTokenId(e.target.value);
                    }}
                    className="logon-input-field" 
                    placeholder="VESSEL_N"
                    onFocus={stopCycle}
                    onMouseDown={stopCycle}
                    onTouchStart={stopCycle}
                  />
                </div>

                <div className="anim-blur-in" style={{ animationDelay: '0.95s', marginBottom: '1.8vh', display: 'flex', flexDirection: 'column' }}>
                  <label style={{ fontSize: '8px', textTransform: 'uppercase', letterSpacing: '0.25em', color: 'rgba(255,255,255,0.4)', fontFamily: 'Tahoma, sans-serif', fontStyle: 'normal', fontWeight: 'bold', marginBottom: '2px' }}>
                    SOLAR EPOCH
                  </label>
                  <input 
                    type="date" 
                    value={solarEpoch}
                    onChange={e => setSolarEpoch(e.target.value)}
                    className="logon-input-field" 
                  />
                </div>

                <div className="anim-blur-in" style={{ animationDelay: '1.15s', marginBottom: '1.8vh', display: 'flex', flexDirection: 'column' }}>
                  <label style={{ fontSize: '8px', textTransform: 'uppercase', letterSpacing: '0.25em', color: 'rgba(255,255,255,0.4)', fontFamily: 'Tahoma, sans-serif', fontStyle: 'normal', fontWeight: 'bold', marginBottom: '2px' }}>
                    TEMP AXIS
                  </label>
                  <input 
                    type="time" 
                    value={tempAxis}
                    onChange={e => setTempAxis(e.target.value)}
                    className="logon-input-field" 
                  />
                </div>
              </div>

              {/* Logon Actions */}
              <div className="anim-blur-in" style={{ animationDelay: '1.35s', width: '85%' }}>
                <button 
                  onClick={handleExecute}
                  className="gothic-btn btn-primary"
                  style={{
                    fontSize: '8px',
                    letterSpacing: '0.25em',
                    padding: '6px 16px',
                    cursor: 'pointer',
                    userSelect: 'none'
                  }}
                >
                  ◆ EXECUTE SYSTEM LINK
                </button>
              </div>
            </>
          )}

          {stage === 'boot' && (
            <div className="boot-loader-box" style={{ display: 'block', width: '90%', background: 'transparent', border: 'none', padding: '0 24px 0 0', margin: 0 }}>
              <div className="boot-header" style={{ marginBottom: '2vh', borderBottomColor: 'rgba(255,255,255,0.1)' }}>
                <span className="font-mono text-white text-[10px]">[ LUNAROT ENGINE OS v5.18 ]</span>
                <span className="font-mono text-white text-[9px]" style={{ animation: 'breathe 1.5s infinite' }}>RE-LINKING CONDUIT</span>
              </div>
              <div className="boot-logs scrollbar-thin scrollbar-thumb-white/10" style={{ minHeight: '140px', maxHeight: '220px', overflowY: 'auto', fontFamily: 'monospace', fontSize: '7.5px', color: 'rgba(255,255,255,0.75)', lineHeight: 1.8 }}>
                {bootLogs.map((log, i) => (
                  <div key={i}>{log}</div>
                ))}
              </div>
              <div className="boot-progress-bar-container" style={{ marginTop: '2.5vh' }}>
                <div className="boot-progress-info" style={{ fontSize: '7px', color: 'rgba(255,255,255,0.4)', display: 'flex', justifycontent: 'space-between', fontFamily: 'monospace' }}>
                  <span>INITIALIZING CHANNELS</span>
                  <span>{progress}%</span>
                </div>
                <div className="boot-progress-ascii" style={{ fontFamily: 'monospace', fontSize: '9px', color: 'rgba(255,255,255,0.85)', marginTop: '4px' }}>
                  {asciiProgress}
                </div>
              </div>
            </div>
          )}

          {/* Barcode block at bottom right */}
          <div className="barcode-block anim-blur-in" style={{ animationDelay: '1.55s' }}>
            <div className="barcode-lines" />
            <div style={{ fontFamily: 'monospace', fontSize: '8px', color: '#ffffff', marginTop: '5px', letterSpacing: '0.12em' }}>
              (c)2026 lunarotdeka
            </div>
          </div>
        </div>
      </div>

      {/* black band above bottom bar */}
      <div className="band-bottom"></div>

      {/* bottom metallic bar */}
      <div className="bar-bottom">
        <div className="power-cluster">
          <div 
            className="orb" 
            title="Log On / Boot OS"
            onClick={stage === 'intake' ? handleExecute : undefined}
          />
          <div 
            className="arrow-btn" 
            title="Reset to Defaults"
            onClick={handleReSeed}
          >
            <span></span>
          </div>
        </div>
        <div className="logon-note">
          After you log on, you can add or change accounts.<br />
          Just go to Control Panel and click User Accounts.
        </div>
      </div>
    </div>
  );
}
