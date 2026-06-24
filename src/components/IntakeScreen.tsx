import { useState, useEffect } from 'react';
import { SIGN_NAMES, getSunSign, getMoonSign, getRisingSign, toJD, NatalUser } from '../types';
import BootLoader from './BootLoader';
import GothicButton from './GothicButton';

interface IntakeScreenProps {
  onSubmit: (user: NatalUser) => void;
}

const ZODIAC_GLYPHS = ['♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓'];

const COMPACT_EYE_FRAMES = [
  `     .--------.     \n    /  (  ●  )  \\   \n    \\           /   \n     '--------'     `,
  `     .--------.     \n    /  (●   )   \\   \n    \\           /   \n     '--------'     `,
  `     .--------.     \n    /   (   ●)  \\   \n    \\           /   \n     '--------'     `,
  `     .--------.     \n    /  ( ◉ ◉ )  \\   \n    \\           /   \n     '--------'     `,
  `     .--------.     \n    /   - - -   \\   \n    \\           /   \n     '--------'     `,
  `     .--------.     \n    =============   \n     '--------'     `
];

const LOADING_SECTOR_LOGS = [
  "◆ [0xCC0110] BIND SECURE PORTS TO HOST 0.0.0.0... [OK]",
  "✦ [0x8FA12B] SYNCHRONIZING METEORIC DRIFT TO SOLAR CORRIDORS... [OK]",
  "✦ [0x098A2F] INTERPOLATING LUNAR CONVICTION MATRIX... [OK]",
  "◆ [0xEE334A] INJECTING FAUSTIAN REGISTRY COOKIES UNSEALED... [OK]",
  "◆ [0x12FF88] INITIATING DIRECT CHANNELS WITH CHANCELLERY OF THE VOID... [OK]",
  "✦ [0xAA99E1] SECURE NATAL DESCENT HANDSHAKE COMPLETE // WARNING: INTERNAL BURN THRESHOLDS EXCEEDED // LOAD SUCCESSFUL"
];

export default function IntakeScreen({ onSubmit }: IntakeScreenProps) {
  const [name, setName] = useState('');
  const [dob, setDob] = useState(() => {
    // Default to a vintage solar date or today
    return '1999-08-11';
  });
  const [time, setTime] = useState('12:12');
  const [errorMsg, setErrorMsg] = useState('');
  
  // Simulated OS loading state after submission
  const [isLoggingIn, setIsLoggingIn] = useState(false);

  // Moving eye graphic state
  const [eyeFrameIndex, setEyeFrameIndex] = useState(0);

  // Eye movement cycle
  useEffect(() => {
    const eyeInterval = setInterval(() => {
      const rand = Math.random();
      if (rand < 0.45) {
        setEyeFrameIndex(0); // center
      } else if (rand < 0.6) {
        setEyeFrameIndex(1); // left
      } else if (rand < 0.75) {
        setEyeFrameIndex(2); // right
      } else if (rand < 0.85) {
        setEyeFrameIndex(3); // side-glance wide
      } else if (rand < 0.93) {
        setEyeFrameIndex(4); // blink-half
      } else {
        setEyeFrameIndex(5); // blink-close
        setTimeout(() => setEyeFrameIndex(0), 120);
      }
    }, 800);

    return () => clearInterval(eyeInterval);
  }, []);

  // Handle submit keypress & trigger simulated OS lag loading
  const handleTriggerLogin = () => {
    if (!dob) {
      setErrorMsg('✦ ERR: SOLAR ALIGNMENT REQUIRED FOR COMPILATION.');
      return;
    }
    setErrorMsg('');
    setIsLoggingIn(true);
  };

  const handleBootComplete = () => {
    const [year, month, day] = dob.split('-').map(Number);
    let birthHour: number | null = null;
    if (time) {
      const [h, m] = time.split(':').map(Number);
      birthHour = h + m / 60;
    }
    const jd = toJD(year, month, day, birthHour || 12);
    const sunIdx = getSunSign(month, day);
    const moonIdx = getMoonSign(jd);
    const risingIdx = birthHour !== null ? getRisingSign(jd, birthHour) : null;

    const finalUser: NatalUser = {
      sun: SIGN_NAMES[sunIdx],
      moon: SIGN_NAMES[moonIdx],
      rising: risingIdx !== null ? SIGN_NAMES[risingIdx] : null,
      hasRising: risingIdx !== null,
      name: name.trim() || 'COGNITION_VESSEL_N',
      sunIdx,
      moonIdx,
      risingIdx,
      jd
    };

    onSubmit(finalUser);
  };

  // Astrological live calculation preview values
  const [year, month, day] = dob ? dob.split('-').map(Number) : [1990, 1, 1];
  let birthHour: number | null = null;
  if (time) {
    const [h, m] = time.split(':').map(Number);
    birthHour = h + m / 60;
  }
  const jd = dob ? toJD(year, month, day, birthHour || 12) : 0;
  const tempSunIdx = dob ? getSunSign(month, day) : -1;
  const tempMoonIdx = dob ? getMoonSign(jd) : -1;
  const tempRisingIdx = (dob && birthHour !== null) ? getRisingSign(jd, birthHour) : null;

  return (
    <div 
      id="intakeScreen" 
      className="fixed inset-0 w-screen h-screen flex flex-col items-center justify-center bg-black z-50 select-none overflow-hidden"
    >
      {/* Background terminal matrix noise */}
      <div className="absolute inset-0 z-0 opacity-10 pointer-events-none flex flex-col justify-between p-6 leading-3 text-[5.5px] font-mono text-white/50 tracking-wider uppercase">
        <div className="space-y-1">
          <p>[ SYSTEM REGISTRY INGRESS LOG ]</p>
          <p>SYSREG_0x00FE29 // STATUS: SECURE_AUTH</p>
          <p>ASCENSION DECAY LIMIT NOMINAL // PARADOX HOVER: NO</p>
          <p>CONDUIT RE-REGISTRATION ENFORCED PORTS RE-READ</p>
          <p>DO NOT POWER OFF DIRECT CONTAINERS WHILE THE FIRE IGNITES</p>
        </div>
        <div className="text-right space-y-1">
          <p>[ SYSTEM CORE SPECS ]</p>
          <p>LUNAROT ENGINE OS v5.18-C // PORT 3000</p>
          <p>WARNING: SOULED VESSEL IMMINENT</p>
          <p>ASTRAL PARADOX CALCULATOR ENFORCING INTERMODAL BIOPHYSICAL RECOIL</p>
        </div>
      </div>

      {isLoggingIn ? (
        /* ───── MICRO LOADING SEQUENCE (OS STYLE BOOT) ───── */
        <BootLoader
          logs={LOADING_SECTOR_LOGS}
          title="LUNAROT ENGINE OS v5.18"
          onComplete={handleBootComplete}
        />
      ) : (
        /* ───── UNIFIED TERMINAL REGISTRY LOGIN (ASSUMING ALREADY REGISTERED) ───── */
        <div className="relative z-10 w-full max-w-sm px-6 py-4 flex flex-col items-center justify-center text-center">
          
          {/* HEADER SYSTEM */}
          <div className="mb-4 text-center space-y-1 w-full">
            <div className="font-mono text-[7px] text-white/40 tracking-[0.45em] uppercase">
              // LUNAROT ENGINE OS //
            </div>
            <h1 className="font-mono text-sm tracking-[0.35em] text-white font-extrabold uppercase select-none">
              REGISTRY LOG-IN
            </h1>
            <p className="text-[6px] tracking-[0.3em] text-white/30 uppercase font-mono">
              PARADOX RECORD ID: 0x9FA2 // AUTOLOAD CONFIGS OK
            </p>
          </div>

          {/* EYE GRAPHIC IN CENTER */}
          <div className="mb-5 relative select-none">
            <pre className="font-mono text-white text-[8px] leading-[1.25] text-center bg-black/60 p-2 border border-white/10 rounded-none inline-block">
              {COMPACT_EYE_FRAMES[eyeFrameIndex]}
              <span className="text-[5.5px] block text-white/40 tracking-[0.2em] mt-1.5">// OS_GATE_ONLINE //</span>
            </pre>
          </div>

          {/* UNIFIED ASCII GRID CONFIG PORTAL */}
          <div className="w-full border border-white/15 bg-[#050505] p-4 text-left font-mono text-[8px] tracking-[0.15em] py-5">
            <div className="text-[7.5px] font-bold text-white/40 tracking-[0.2em] border-b border-white/10 pb-1.5 mb-3 uppercase flex justify-between">
              <span>◆ CONDUIT HARDWARE ADDR</span>
              <span>[ REGISTRY_RE_ENTRY ]</span>
            </div>
            
            <table className="w-full border-collapse">
              <tbody>
                {/* 1. Name Identifier */}
                <tr className="border-b border-white-[0.03]">
                  <td className="py-2 pr-2 text-white/40 font-bold select-none text-[7px]">TOKEN_ID :</td>
                  <td className="py-2 text-right">
                    <input
                      type="text"
                      maxLength={20}
                      placeholder="VESSEL_N"
                      value={name}
                      onChange={(e) => setName(e.target.value)}
                      onKeyDown={(e) => e.key === 'Enter' && handleTriggerLogin()}
                      className="bg-transparent border-none text-right font-mono text-[8.5px] text-white placeholder-white/20 focus:outline-none focus:text-white select-text cursor-text uppercase tracking-widest w-40"
                    />
                  </td>
                </tr>

                {/* 2. DOB Solar Alignment */}
                <tr className="border-b border-white-[0.03]">
                  <td className="py-2 pr-2 text-white/40 font-bold select-none text-[7px]">SOLAR_EPOCH:</td>
                  <td className="py-2 text-right flex items-center justify-end gap-1.5">
                    <input
                      type="date"
                      value={dob}
                      onChange={(e) => setDob(e.target.value)}
                      onKeyDown={(e) => e.key === 'Enter' && handleTriggerLogin()}
                      className="bg-transparent border-none text-right font-mono text-[8.5px] text-white focus:outline-none select-text cursor-text w-28 uppercase tracking-widest"
                      style={{ colorScheme: 'dark' }}
                    />
                    <span className="text-white/70 select-none text-[8px] w-6 text-center">
                      {tempSunIdx !== -1 ? ZODIAC_GLYPHS[tempSunIdx] : '✦'}
                    </span>
                  </td>
                </tr>

                {/* 3. Time Temporal Axis */}
                <tr>
                  <td className="py-2 pr-2 text-white/40 font-bold select-none text-[7px]">TEMP_AXIS :</td>
                  <td className="py-2 text-right flex items-center justify-end gap-1.5">
                    <input
                      type="time"
                      value={time}
                      onChange={(e) => setTime(e.target.value)}
                      onKeyDown={(e) => e.key === 'Enter' && handleTriggerLogin()}
                      className="bg-transparent border-none text-right font-mono text-[8.5px] text-white focus:outline-none select-text cursor-text w-20 tracking-widest"
                      style={{ colorScheme: 'dark' }}
                    />
                    <span className="text-white/70 select-none text-[8px] w-6 text-center">
                      {tempRisingIdx !== null ? ZODIAC_GLYPHS[tempRisingIdx] : '☀'}
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>

            {/* LIVE ASTRAL CALCULATION READOUT */}
            <div className="border-t border-white/10 mt-3 pt-2 text-[6.5px] leading-relaxed text-white/40 select-none flex justify-between items-center font-mono">
              <span>SOLAR: {tempSunIdx !== -1 ? SIGN_NAMES[tempSunIdx].toUpperCase() : "???"}</span>
              <span>LUNAR: {tempMoonIdx !== -1 ? SIGN_NAMES[tempMoonIdx].toUpperCase() : "???"}</span>
              <span>RISING: {tempRisingIdx !== null ? SIGN_NAMES[tempRisingIdx].toUpperCase() : "BYPASSED"}</span>
            </div>
          </div>

          {/* ACTION STRIP */}
          <div className="mt-5 w-full space-y-3">
            <GothicButton
              variant="primary"
              fullWidth
              onClick={handleTriggerLogin}
            >
              ◆ EXECUTE SYSTEM LINK // BOOT OS
            </GothicButton>
            <div className="font-mono text-[6px] tracking-[0.25em] text-white/30 uppercase select-none">
              AUTOPILOT CONNECT PORT 3000 // CHANCELLERY OF THE VOID
            </div>
          </div>

          {/* Validation/Feedback error messages */}
          {errorMsg && (
            <div className="text-center font-mono text-[7px] text-white font-bold uppercase tracking-[0.15em] mt-3 animate-pulse">
              {errorMsg}
            </div>
          )}

        </div>
      )}
    </div>
  );
}
