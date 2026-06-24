import { useState, useEffect, useRef } from 'react';

interface FlameEtchedTextProps {
  text: string;
  speedMultiplier?: number;
  className?: string;
  onComplete?: () => void;
  chargedWords?: string[]; // Extra list of words to trigger the alchemical burn flicker
}

const ARABIC = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي';
function randArabic(): string {
  return ARABIC[Math.floor(Math.random() * ARABIC.length)];
}

function msDelay(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}

export default function FlameEtchedText({
  text,
  speedMultiplier = 1.0,
  className = '',
  onComplete,
  chargedWords = [],
}: FlameEtchedTextProps) {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const sessionRef = useRef<number>(0);

  useEffect(() => {
    sessionRef.current += 1;
    const sessionNum = sessionRef.current;
    const el = containerRef.current;
    if (!el) return;

    el.innerHTML = '';
    
    // Split text into words
    const words = text.split(' ');
    let rendered = '';

    const runTypewriter = async () => {
      for (let w = 0; w < words.length; w++) {
        if (sessionRef.current !== sessionNum) return;
        const word = words[w];
        if (!word) continue;

        // Check if word is charged:
        // 1. Wrapped in single or double asterisks (e.g. *word* or **word**)
        // 2. Included in the custom chargedWords prop list
        // 3. Contains a hyphen and is longer than 5 chars (like the original)
        const isAsteriskCharged = word.startsWith('*') && word.endsWith('*');
        const cleanWord = word.replace(/\*/g, '');
        const cleanLower = cleanWord.toLowerCase().replace(/[^a-z-]/g, '');
        
        const isCustomCharged = chargedWords.some(
          (cw) => cw.toLowerCase().replace(/[^a-z-]/g, '') === cleanLower
        );
        
        const isHyphenCharged = cleanWord.includes('-') && cleanWord.length > 5;
        
        const charged = isAsteriskCharged || isCustomCharged || isHyphenCharged;
        const displayWord = cleanWord;

        if (charged) {
          // Flame etch start indicator
          el.innerHTML = rendered + '<span class="etch-cursor">▌</span>';
          await msDelay((130 + Math.floor(Math.random() * 90)) * speedMultiplier);

          // Flicker glyphs
          const flickCount = 5 + Math.floor(Math.random() * 5);
          for (let f = 0; f < flickCount; f++) {
            if (sessionRef.current !== sessionNum) return;
            const ghost = displayWord
              .split('')
              .map((c) => (c.match(/[a-zA-Z]/) ? randArabic() : c))
              .join('');
            el.innerHTML =
              rendered +
              '<span class="etch-ghost">' +
              ghost +
              '</span><span class="etch-cursor">▌</span>';
            await msDelay((25 + Math.floor(Math.random() * 20)) * speedMultiplier);
          }

          if (sessionRef.current !== sessionNum) return;
          el.innerHTML =
            rendered +
            '<span class="etch-ghost">' +
            displayWord +
            '</span><span class="etch-cursor">▌</span>';
          await msDelay((60 + Math.floor(Math.random() * 40)) * speedMultiplier);

          if (sessionRef.current !== sessionNum) return;
          rendered += '<span class="etch-word">' + displayWord + '</span> ';
          el.innerHTML = rendered + '<span class="etch-cursor">▌</span>';
          await msDelay((40 + Math.floor(Math.random() * 30)) * speedMultiplier);
        } else {
          // Standard typewrite
          if (sessionRef.current !== sessionNum) return;
          rendered += displayWord + ' ';
          el.innerHTML = rendered + '<span class="etch-cursor">▌</span>';

          if (displayWord.match(/[,;:—]/)) {
            await msDelay((80 + Math.floor(Math.random() * 60)) * speedMultiplier);
          } else if (displayWord.match(/[.!?]$/)) {
            el.innerHTML = rendered;
            await msDelay((350 + Math.floor(Math.random() * 150)) * speedMultiplier);
            if (sessionRef.current !== sessionNum) return;
            el.innerHTML = rendered + '<span class="etch-cursor">▌</span>';
            await msDelay(40 * speedMultiplier);
          } else {
            await msDelay((12 + Math.floor(Math.random() * 8)) * speedMultiplier);
          }
        }
      }

      if (sessionRef.current === sessionNum) {
        el.innerHTML = rendered.trim();
        if (onComplete) onComplete();
      }
    };

    runTypewriter();

    return () => {
      sessionRef.current += 1;
    };
  }, [text, speedMultiplier, chargedWords]);

  return (
    <div
      ref={containerRef}
      className={`font-garamond leading-relaxed text-[#cfc9c0] ${className}`}
    />
  );
}
