import { useState, useEffect } from 'react';

interface BootLoaderProps {
  logs?: string[];
  title?: string;
  onComplete: () => void;
  speedMultiplier?: number;
}

const DEFAULT_LOGS = [
  '◆ [0xCC0110] BIND SECURE PORTS TO HOST 0.0.0.0... [OK]',
  '✦ [0x8FA12B] SYNCHRONIZING METEORIC DRIFT TO SOLAR CORRIDORS... [OK]',
  '✦ [0x098A2F] INTERPOLATING LUNAR CONVICTION MATRIX... [OK]',
  '◆ [0xEE334A] INJECTING FAUSTIAN REGISTRY COOKIES UNSEALED... [OK]',
  '◆ [0x12FF88] INITIATING DIRECT CHANNELS WITH CHANCELLERY OF THE VOID... [OK]',
  '✦ [0xAA99E1] SECURE NATAL DESCENT HANDSHAKE COMPLETE // WARNING: REGISTRY READY',
];

export default function BootLoader({
  logs = DEFAULT_LOGS,
  title = 'LUNAROT ENGINE OS v5.18',
  onComplete,
  speedMultiplier = 1.0,
}: BootLoaderProps) {
  const [progress, setProgress] = useState(0);
  const [activeLogIndex, setActiveLogIndex] = useState(0);

  useEffect(() => {
    setProgress(0);
    setActiveLogIndex(0);

    const interval = setInterval(() => {
      setProgress((prev) => {
        const increment = Math.floor(Math.random() * 8) + 6;
        const next = prev + increment;
        if (next >= 100) {
          clearInterval(interval);
          setTimeout(() => {
            onComplete();
          }, 400);
          return 100;
        }

        const logPct = next / 100;
        const targetLogIdx = Math.min(
          Math.floor(logPct * logs.length),
          logs.length - 1
        );
        setActiveLogIndex(targetLogIdx);

        return next;
      });
    }, 110 * speedMultiplier);

    return () => clearInterval(interval);
  }, [logs, onComplete, speedMultiplier]);

  // Construct progress bar string
  const filledBlocks = Math.floor(progress / 4);
  const emptyBlocks = 25 - filledBlocks;
  const barString = `[${'█'.repeat(filledBlocks)}${'░'.repeat(emptyBlocks)}]`;

  return (
    <div className="relative z-10 w-full max-w-md px-8 py-10 border border-white/10 bg-black text-left font-mono text-[9px] tracking-wider uppercase space-y-6">
      <div className="flex justify-between items-center pb-2 border-b border-white/10">
        <span>[ {title} ]</span>
        <span className="animate-pulse text-white">RE-LINKING CONDUIT</span>
      </div>

      <div className="space-y-2 text-white/70 min-h-[90px] text-[7.5px] tracking-widest leading-relaxed">
        {logs.slice(0, activeLogIndex + 1).map((log, idx) => (
          <div key={idx} className="animate-[fade-in_0.3s_ease_forwards]">
            {log}
          </div>
        ))}
      </div>

      <div className="space-y-2">
        <div className="flex justify-between text-[7px] text-white/40">
          <span>INITIALIZING CHANNELS</span>
          <span>{progress}%</span>
        </div>
        <div className="text-[9px] tracking-normal font-sans text-white/80 select-none">
          {barString}
        </div>
      </div>
    </div>
  );
}
