import { useState } from 'react';
import GothicPanel from './GothicPanel';
import GothicButton from './GothicButton';
import FlameEtchedText from './FlameEtchedText';
import InteractiveText from './InteractiveText';

export default function AboutScreen() {
  const [resetKey, setResetKey] = useState(0);

  const triggerCrazyEyes = () => {
    window.dispatchEvent(
      new CustomEvent('ascii-eyes-control', {
        detail: { action: 'crazy', duration: 5000 },
      })
    );
  };

  const handleReplayIntroText = () => {
    setResetKey((prev) => prev + 1);
  };

  return (
    <div className="w-full max-w-6xl mx-auto px-4 md:px-8 py-6 h-full overflow-y-auto font-mono text-[10px] md:text-[11px] leading-relaxed select-text pb-16">
      
      {/* Dossier Header */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-[var(--gold)]/30 pb-4 mb-8 gap-4">
        <div>
          <h1 className="font-cinzel text-xl md:text-2xl text-[var(--gold)] tracking-[0.2em] font-bold uppercase">
            ✦ LUNAROT SYSTEM ARCHIVE ✦
          </h1>
          <p className="text-white/40 text-[8px] md:text-[9px] tracking-wider mt-1 uppercase">
            CLASSIFIED DOSSIER // DEFUNCT WITCHCRAFT RECONSTRUCTION PROJECT
          </p>
        </div>
        <div className="flex gap-2">
          <GothicButton variant="secondary" onClick={triggerCrazyEyes} className="text-[7.5px] py-1 px-3">
            ☣ TRIGGER EYE SPASM
          </GothicButton>
          <GothicButton variant="primary" onClick={handleReplayIntroText} className="text-[7.5px] py-1 px-3">
            ↻ RE-ETCH INTRO
          </GothicButton>
        </div>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        
        {/* Left Column: Lore & Aesthetic (7 cols) */}
        <div className="lg:col-span-7 space-y-6">
          <GothicPanel variant="gold" titleTag="LORE.DOSSIER_01" footerTag="SACRED_MECHANICS_INC">
            <h2 className="font-cinzel text-sm text-[var(--gold)] tracking-widest font-semibold mb-4 border-b border-white/5 pb-2">
              Ⅰ. THE FORBIDDEN ENGINE
            </h2>
            <div className="space-y-4 text-white/80 font-garamond text-[13px] md:text-[14px] leading-relaxed">
              <div className="min-h-[60px] font-mono text-[9.5px] leading-relaxed text-[var(--gold)] bg-black/35 p-2.5 border border-white/5 mb-3">
                <FlameEtchedText
                  key={resetKey}
                  text="Warning: This framework contains *illegally* harvested artifacts from *Sacred-Mechanics* (Est. 1999). Unauthorized reproduction triggers *soul-replication* telemetry."
                  chargedWords={['illegally', 'Sacred-Mechanics', 'soul-replication']}
                />
              </div>
              <p>
                The Lunarot Engine is structured as a retro-gothic-alchemical terminal designed as a premium baseline for modern web applications. Originally conceptualized as an administrative console for a defunct 2000s witchcraft corporation, the interface fuses WebGL celestial coordinate tracking with terminal inputs to bridge the digital and the occult.
              </p>
              <p>
                Its core structure is locked dimensions to eliminate double scrollbars and dynamically scale elements. Every component, from the dashed inner borders to the custom input vectors, is designed to elicit a sense of mysterious interactive life.
              </p>
            </div>
          </GothicPanel>

          <GothicPanel variant="white" titleTag="INSPIRATION.ANALOG" footerTag="JAPANESE_DARK_WEB">
            <h2 className="font-cinzel text-sm text-white tracking-widest font-semibold mb-4 border-b border-white/5 pb-2">
              Ⅱ. AESTHETIC DNA & 個人サイト
            </h2>
            <div className="space-y-4 text-white/80 font-garamond text-[13px] md:text-[14px]">
              <p>
                Visual layouts take inspiration from the late-90s and mid-2000s Japanese personal websites (個人サイト) dedicated to dark-horror art, occult symbols, and text-based divination. Chief among these influences is the raw, haunting beauty of classic webs like <span className="text-[var(--gold)] font-mono text-[10px]">ankokukoubou.com</span>.
              </p>
              <InteractiveText
                text='"In the silence of the early net, the shadows of raw HTML contained rituals that modern flat design has forgotten."'
                className="block text-white/90 italic border-l-2 border-[var(--gold)]/40 pl-4 py-1 my-3"
              />
              <p>
                Rather than using generic modern styling, Lunarot OS enforces high-contrast, harmonized alchemical color tokens: <b className="text-[var(--gold)] font-mono text-[10.5px]">Void (#000000)</b>, <b className="text-white/40 font-mono text-[10.5px]">Ash (#080808)</b>, <b className="text-[var(--gold)] font-mono text-[10.5px]">Elden Gold (#c8a45a)</b>, and <b className="text-white font-mono text-[10.5px]">Parchment (#efede8)</b>.
              </p>
            </div>
          </GothicPanel>
        </div>

        {/* Right Column: Technical Specs (5 cols) */}
        <div className="lg:col-span-5 space-y-6">
          <GothicPanel variant="gold" titleTag="SPECS.TELEMETRY" footerTag="SYSTEM_DIAGNOSTIC">
            <h2 className="font-cinzel text-sm text-[var(--gold)] tracking-widest font-semibold mb-4 border-b border-white/5 pb-2">
              Ⅲ. TECHNICAL CONDUITS
            </h2>
            <div className="space-y-6 text-white/70">
              
              {/* Star Background description */}
              <div className="space-y-1.5">
                <div className="flex justify-between text-[8px] font-mono text-white/90">
                  <span>[CONDUIT_A] STAR_FIELD_ORBITS</span>
                  <span className="text-[var(--gold)]">ACTIVE</span>
                </div>
                <div className="w-full bg-white/5 h-[1px] mb-2" />
                <p className="font-garamond text-[12.5px] leading-relaxed">
                  A high-performance WebGL/Canvas backdrop drawing radial concentric orbits, Sephirotic coordinate nodes, weight wires, and planetary coordinates shifting continuously over time.
                </p>
              </div>

              {/* ASCII Background Eyes description */}
              <div className="space-y-1.5">
                <div className="flex justify-between text-[8px] font-mono text-white/90">
                  <span>[CONDUIT_B] ASCII_EYE_MATRIX</span>
                  <span className="text-[var(--gold)]">STANDBY</span>
                </div>
                <div className="w-full bg-white/5 h-[1px] mb-2" />
                <p className="font-garamond text-[12.5px] leading-relaxed">
                  A mathematical rendering of a mouse-tracking pupil. When idle, the eyes scan coordinates. When triggered (via the diagnostic button above), they slide into a spasmodic alchemical glyph morphing phase.
                </p>
              </div>

              {/* Flame Etched Typewriter description */}
              <div className="space-y-1.5">
                <div className="flex justify-between text-[8px] font-mono text-white/90">
                  <span>[CONDUIT_C] FLAME_ETCHED_TEXT</span>
                  <span className="text-[var(--gold)]">STABLE</span>
                </div>
                <div className="w-full bg-white/5 h-[1px] mb-2" />
                <p className="font-garamond text-[12.5px] leading-relaxed">
                  A dynamic text renderer that scans output strings. Standard words print with default delay intervals, while charged words trigger rapid flickering of Arabic characters before locking into a soft gold typography glow.
                </p>
              </div>

            </div>
          </GothicPanel>

          <GothicPanel variant="white" titleTag="DIMENSIONAL.LOCK" footerTag="SCALING_ENGINE">
            <h2 className="font-cinzel text-sm text-white tracking-widest font-semibold mb-3 border-b border-white/5 pb-2">
              Ⅳ. DIMENSIONAL CONTROL
            </h2>
            <p className="font-garamond text-[13px] text-white/70">
              To fit seamlessly inside custom viewport borders and third-party wrappers, the CSS enforces an absolute scaling factor (<code className="text-white bg-white/5 px-1 py-0.5 rounded font-mono text-[9px]">--c-scale</code>) combined with media queries. This eliminates double scrollbars entirely, keeping the gothic interface locked and responsive across all device sizes.
            </p>
          </GothicPanel>
        </div>

      </div>
    </div>
  );
}
