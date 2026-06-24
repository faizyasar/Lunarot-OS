import { useState } from 'react';
import GothicButton from './GothicButton';
import {
  GothicTextInput,
  GothicDateInput,
  GothicTimeInput,
  GothicSelect,
} from './GothicInput';
import GothicPanel from './GothicPanel';
import FlameEtchedText from './FlameEtchedText';
import InteractiveText from './InteractiveText';
import BootLoader from './BootLoader';

export default function ShowcaseScreen() {
  // Demo States
  const [typedKey, setTypedKey] = useState(0);
  const [showBootDemo, setShowBootDemo] = useState(false);
  const [bootCompleted, setBootCompleted] = useState(false);

  // Form states
  const [name, setName] = useState('VESSEL_PLAYGROUND');
  const [dob, setDob] = useState('2026-06-24');
  const [time, setTime] = useState('19:24');
  const [option, setOption] = useState('sector_4');

  // Trigger eye actions
  const triggerCrazyEyes = () => {
    window.dispatchEvent(
      new CustomEvent('ascii-eyes-control', {
        detail: { action: 'crazy', duration: 4000 },
      })
    );
  };

  const trackElementEyes = (id: string) => {
    window.dispatchEvent(
      new CustomEvent('ascii-eyes-control', {
        detail: { action: 'track-element', targetId: id, duration: 4000 },
      })
    );
  };

  const resetEyes = () => {
    window.dispatchEvent(
      new CustomEvent('ascii-eyes-control', {
        detail: { action: 'reset' },
      })
    );
  };

  const handleRestartTypewriter = () => {
    setTypedKey((prev) => prev + 1);
  };

  const triggerBootSequence = () => {
    setBootCompleted(false);
    setShowBootDemo(true);
  };

  // Mock code snippets for easy copy paste
  const panelCode = `<GothicPanel variant="gold" titleTag="SECURE_GATE" footerTag="V.1.0">
  <p>Your custom content here...</p>
</GothicPanel>`;

  const btnCode = `<GothicButton variant="primary">Primary Link</GothicButton>
<GothicButton variant="secondary">Sacred Ritual</GothicButton>`;

  const inputCode = `<GothicTextInput label="User Token" value={name} onChange={e => setName(e.target.value)} />`;

  const typewriterCode = `<FlameEtchedText text="*Charged* terms burn in Arabic glyphs before they settle." />`;

  return (
    <div className="w-full h-full max-h-full flex flex-col md:grid md:grid-cols-12 gap-6 p-6 overflow-y-auto select-text font-mono text-[10px] text-white/80 animate-[fade-in_0.8s_ease_forwards] relative z-20">
      
      {/* ─── COLUMN 1: TOKENS & ATMO CONTROL ─── */}
      <div className="md:col-span-5 flex flex-col gap-6">
        
        {/* Design system tokens card */}
        <GothicPanel variant="gold" titleTag="AESTHETIC_TOKENS" footerTag="THEME_ROOT">
          <div className="space-y-4">
            <p className="text-white/40 font-bold uppercase tracking-[0.2em] border-b border-white/10 pb-1 text-[8.5px]">
              ◆ Core Color Swatches
            </p>
            <div className="grid grid-cols-5 gap-2 text-center text-[7.5px] font-bold">
              <div className="flex flex-col gap-1">
                <div className="h-10 bg-black border border-white/10" />
                <span className="text-white/40">void</span>
                <span className="text-white/30">#000000</span>
              </div>
              <div className="flex flex-col gap-1">
                <div className="h-10 bg-[#080808] border border-white/10" />
                <span className="text-white/40">ash</span>
                <span className="text-white/30">#080808</span>
              </div>
              <div className="flex flex-col gap-1">
                <div className="h-10 bg-[#c8a45a] border border-white/10" />
                <span className="text-[var(--gold)]">gold</span>
                <span className="text-white/30">#c8a45a</span>
              </div>
              <div className="flex flex-col gap-1">
                <div className="h-10 bg-[#efede8] text-black font-extrabold flex items-center justify-center border border-white/10" />
                <span className="text-white/40">parchment</span>
                <span className="text-white/30">#efede8</span>
              </div>
              <div className="flex flex-col gap-1">
                <div className="h-10 bg-white border border-white/10" />
                <span className="text-white/40">cream</span>
                <span className="text-white/30">#ffffff</span>
              </div>
            </div>

            <div className="space-y-2 pt-2">
              <p className="text-white/40 font-bold uppercase tracking-[0.2em] border-b border-white/10 pb-1 text-[8.5px]">
                ◆ Typography Scales
              </p>
              <div className="space-y-3 font-sans">
                <div>
                  <span className="text-white/30 block font-mono text-[7px]">// CINZEL SERIF (HEADERS)</span>
                  <h1 className="font-cinzel text-lg md:text-xl text-[var(--gold)] font-bold tracking-wider">
                    Sacred Conflux
                  </h1>
                </div>
                <div>
                  <span className="text-white/30 block font-mono text-[7px]">// GARAMOND SERIF (PROSE)</span>
                  <p className="font-garamond text-sm leading-relaxed text-[#cfc9c0] italic">
                    The ritual has begun. Your astral details are locked inside our cloud meridians.
                  </p>
                </div>
                <div>
                  <span className="text-white/30 block font-mono text-[7px]">// JETBRAINS MONO (OS TELEMETRY)</span>
                  <p className="font-mono text-[8.5px] leading-relaxed text-white/70 tracking-widest uppercase">
                    SYS.REGISTRY_0x9FA2 // COMP CONDUIT LINK SUCCESSFUL
                  </p>
                </div>
              </div>
            </div>
          </div>
        </GothicPanel>

        {/* Ambient controls panel */}
        <GothicPanel variant="gold" titleTag="ATMOSPHERE_TELEMETRY" footerTag="OS_EYES_CONTROL">
          <div className="space-y-4">
            <p className="text-white/40 font-bold uppercase tracking-[0.2em] border-b border-white/10 pb-1 text-[8.5px]">
              ◆ ASCII Background Eyes Control
            </p>
            <p className="text-[#cfc9c0]/70 text-[9px] font-sans leading-relaxed">
              The ASCII eyes in the background track your pointer. Use the telemetry triggers below to command their current target coordinates or trigger cursed spasms.
            </p>
            <div className="flex flex-wrap gap-3 pt-1">
              <GothicButton
                id="eyeBtnCrazy"
                variant="secondary"
                onClick={triggerCrazyEyes}
                className="py-1.5 text-[7.5px]"
              >
                ◆ TRIGGER CRAZY MODE
              </GothicButton>
              <GothicButton
                id="eyeBtnTrack"
                variant="secondary"
                onClick={() => trackElementEyes('eyeBtnTrack')}
                className="py-1.5 text-[7.5px]"
              >
                ◆ LOCK TRACK ME
              </GothicButton>
              <GothicButton
                id="eyeBtnReset"
                variant="primary"
                onClick={resetEyes}
                className="py-1.5 text-[7.5px]"
              >
                ◆ RESET MOUSE TRACK
              </GothicButton>
            </div>
            <div className="text-[6.5px] text-white/30 tracking-[0.2em] pt-1">
              // CRAZY MODE ALTERS IRIS CHARACTERS TO ALCHEMICAL GLYPHS FOR 4S //
            </div>
          </div>
        </GothicPanel>
      </div>

      {/* ─── COLUMN 2: WIDGETS & PLAYGROUND ─── */}
      <div className="md:col-span-7 flex flex-col gap-6">
        
        {/* Gothic form widgets */}
        <GothicPanel variant="white" titleTag="SACRED_INPUT_FIELDS" footerTag="FORM_ELEMENTS">
          <div className="space-y-4">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <GothicTextInput
                label="Ident Token"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
              <GothicDateInput
                label="Solar Alignment"
                value={dob}
                zodiacGlyph="♋"
                onChange={(e) => setDob(e.target.value)}
              />
              <GothicTimeInput
                label="Temporal Axis"
                value={time}
                timeGlyph="☽"
                onChange={(e) => setTime(e.target.value)}
              />
              <GothicSelect
                label="Registry Sector"
                value={option}
                onChange={(e) => setOption(e.target.value)}
                options={[
                  { value: 'sector_1', label: 'Sector I: Antecedent' },
                  { value: 'sector_2', label: 'Sector II: Concurrent' },
                  { value: 'sector_3', label: 'Sector III: Consequent' },
                  { value: 'sector_4', label: 'Sector IV: Watchgate' },
                ]}
              />
            </div>

            <div className="pt-2 border-t border-white/5 space-y-2">
              <span className="text-white/30 block font-mono text-[7px]">// PREVIEW OF REGISTERED METADATA</span>
              <div className="bg-black/60 border border-white/10 p-3 rounded-none flex justify-between items-center text-[7.5px] tracking-widest text-[var(--gold)]">
                <span>NAME: {name.toUpperCase()}</span>
                <span>ALIGN: {dob} @ {time}</span>
                <span>SECTOR: {option.toUpperCase()}</span>
              </div>
            </div>
          </div>
        </GothicPanel>

        {/* Dynamic animations & typewriting showcase */}
        <GothicPanel variant="gold" titleTag="POETIC_TYPOGRAPHY" footerTag="ETCH_SEQUENCE">
          <div className="space-y-4">
            {/* Interactive hover text */}
            <div className="space-y-1">
              <span className="text-white/30 block font-mono text-[7px]">// INTERACTIVE CHAR HOVER</span>
              <div className="text-base tracking-wider">
                <InteractiveText text="Hover your cursor over this sentence to feel the letters breathe and hover glow." />
              </div>
            </div>

            {/* Typewriter */}
            <div className="space-y-2 pt-2 border-t border-white/5">
              <div className="flex justify-between items-center">
                <span className="text-white/30 block font-mono text-[7px]">// FLAME ETCHED TYPING</span>
                <GothicButton variant="secondary" onClick={handleRestartTypewriter} className="py-1 text-[7.5px]">
                  RE-PLAY ETCH
                </GothicButton>
              </div>

              <div className="bg-black/45 border border-white/10 p-3 min-h-[44px]">
                <FlameEtchedText
                  key={typedKey}
                  text="Charged *adjectives* and *poetic* coordinates spark in alchemical *Arabic* ghost glyphs before they solidify in gold. Normal words typewrite regularly."
                  chargedWords={['Arabic', 'adjectives', 'poetic']}
                />
              </div>
            </div>
          </div>
        </GothicPanel>

        {/* Boot Loader sequence demonstration */}
        <GothicPanel variant="white" titleTag="BOOT_PROGRESS_LOADER" footerTag="OS_BOOT_SEQUENCE">
          <div className="space-y-4">
            <p className="text-[#cfc9c0]/70 text-[9px] font-sans leading-relaxed">
              Lunarot uses a simulated retro-terminal progress bootloader when the user unseals/links their zodiac alignment registry. Test the bootloader below.
            </p>
            
            {!showBootDemo ? (
              <GothicButton variant="primary" onClick={triggerBootSequence}>
                ◆ LOAD SIMULATED BOOT SEQUENCE
              </GothicButton>
            ) : (
              <div className="flex flex-col items-center justify-center p-4 bg-black/80 border border-white/10">
                {bootCompleted ? (
                  <div className="text-center py-4 space-y-3">
                    <p className="text-[var(--gold)] font-bold tracking-[0.2em]">◆ OS BOOT COMPLETED SUCCESSFUL ◆</p>
                    <GothicButton variant="secondary" onClick={() => setShowBootDemo(false)}>
                      RESET LOADER
                    </GothicButton>
                  </div>
                ) : (
                  <BootLoader
                    speedMultiplier={0.8}
                    onComplete={() => setBootCompleted(true)}
                  />
                )}
              </div>
            )}
          </div>
        </GothicPanel>

        {/* Developer Integration Code Blocks */}
        <GothicPanel variant="gold" titleTag="INTEGRATION_GUIDE" footerTag="CODE_COPY">
          <div className="space-y-3">
            <p className="text-white/40 font-bold uppercase tracking-[0.2em] border-b border-white/10 pb-1 text-[8.5px]">
              ◆ Template Usage Quickstart
            </p>
            <p className="text-[#cfc9c0]/70 text-[9px] font-sans leading-relaxed">
              Import the modular gothic styling components directly into your custom screen layout:
            </p>
            
            <div className="space-y-2">
              <div>
                <span className="text-white/30 text-[7px]">// Gothic Glassmorphic Panel</span>
                <pre className="bg-black/70 border border-white/10 p-2 text-[7.5px] leading-relaxed text-[#cfc9c0] overflow-x-auto whitespace-pre">
                  {panelCode}
                </pre>
              </div>
              <div>
                <span className="text-white/30 text-[7px]">// Themed Forms & Inputs</span>
                <pre className="bg-black/70 border border-white/10 p-2 text-[7.5px] leading-relaxed text-[#cfc9c0] overflow-x-auto whitespace-pre">
                  {inputCode}
                </pre>
              </div>
            </div>
          </div>
        </GothicPanel>

      </div>
    </div>
  );
}
