import React, { useEffect, useRef, useState } from 'react';

const ARABIC = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي';
const randArabic = () => ARABIC[Math.floor(Math.random() * ARABIC.length)];

interface EtchedTypewriterProps {
  text: string;
  chargedWords?: string[];
  className?: string;
  onComplete?: () => void;
}

export default function EtchedTypewriter({ text, chargedWords = [], className = '', onComplete }: EtchedTypewriterProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const sessionRef = useRef<number>(0);

  const chargedWordsRef = useRef(chargedWords);
  const onCompleteRef = useRef(onComplete);

  useEffect(() => {
    chargedWordsRef.current = chargedWords;
    onCompleteRef.current = onComplete;
  }, [chargedWords, onComplete]);

  useEffect(() => {
    if (!containerRef.current || !text) return;

    const el = containerRef.current;
    const session = Math.random();
    sessionRef.current = session;
    
    el.innerHTML = '';
    const words = text.split(' ');
    let rendered = '';
    let isMounted = true;

    const delay = (ms: number) => new Promise(r => setTimeout(r, ms * 1.5)); // Slowed down typing

    const type = async () => {
      for (let w = 0; w < words.length; w++) {
        if (!isMounted || sessionRef.current !== session) return;
        
        const word = words[w];
        if (!word) {
          rendered += ' ';
          continue;
        }

        const isAsterisk = word.startsWith('*') && word.endsWith('*');
        const cleanWord = word.replace(/\*/g, '');
        const cleanLower = cleanWord.toLowerCase().replace(/[^a-z-]/g, '');
        
        const isCustom = chargedWordsRef.current.some(cw => cw.toLowerCase().replace(/[^a-z-]/g, '') === cleanLower);
        const isHyphen = cleanWord.includes('-') && cleanWord.length > 5;
        const charged = isAsterisk || isCustom || isHyphen;

        if (charged) {
          el.innerHTML = rendered + '<span class="text-[#ffffff] animate-[ecur_0.6s_ease-in-out_infinite_alternate] inline-block font-mono tracking-widest -mt-1 scale-y-110 ml-0.5">▌</span>';
          await delay(130 + Math.random() * 90);
          
          const flickCount = 5 + Math.random() * 5;
          for (let f = 0; f < flickCount; f++) {
            if (!isMounted || sessionRef.current !== session) return;
            const ghost = cleanWord.split('').map(c => c.match(/[a-zA-Z]/) ? randArabic() : c).join('');
            el.innerHTML = rendered + `<span class="text-[#ffffff] drop-shadow-[0_0_12px_rgba(255,255,255,0.7)] opacity-85 italic inline">${ghost}</span><span class="text-[#ffffff] animate-[ecur_0.6s_ease-in-out_infinite_alternate] inline-block font-mono tracking-widest -mt-1 scale-y-110 ml-0.5">▌</span>`;
            await delay(40 + Math.random() * 20); // Slower glitching
          }
          
          if (!isMounted || sessionRef.current !== session) return;
          el.innerHTML = rendered + `<span class="text-[#ffffff] drop-shadow-[0_0_12px_rgba(255,255,255,0.7)] opacity-85 italic inline">${cleanWord}</span><span class="text-[#ffffff] animate-[ecur_0.6s_ease-in-out_infinite_alternate] inline-block font-mono tracking-widest -mt-1 scale-y-110 ml-0.5">▌</span>`;
          await delay(100 + Math.random() * 40); // Slower

          if (!isMounted || sessionRef.current !== session) return;
          rendered += `<span class="text-[#ffffff] drop-shadow-[0_0_10px_rgba(255,255,255,0.5)] animate-[esettle_1.8s_ease_forwards] inline">${cleanWord}</span> `;
          el.innerHTML = rendered + '<span class="text-[#ffffff] animate-[ecur_0.6s_ease-in-out_infinite_alternate] inline-block font-mono tracking-widest -mt-1 scale-y-110 ml-0.5">▌</span>';
          await delay(60 + Math.random() * 30); // Slower
        } else {
          if (!isMounted || sessionRef.current !== session) return;
          rendered += cleanWord + ' ';
          el.innerHTML = rendered + '<span class="text-[#ffffff] animate-[ecur_0.6s_ease-in-out_infinite_alternate] inline-block font-mono tracking-widest -mt-1 scale-y-110 ml-0.5">▌</span>';
          
          if (cleanWord.match(/[,;:—]/)) {
            await delay(120 + Math.random() * 60); // Slower
          } else if (cleanWord.match(/[.!?]$/)) {
            el.innerHTML = rendered;
            await delay(400 + Math.random() * 150); // Slower
            if (!isMounted || sessionRef.current !== session) return;
            el.innerHTML = rendered + '<span class="text-[#ffffff] animate-[ecur_0.6s_ease-in-out_infinite_alternate] inline-block font-mono tracking-widest -mt-1 scale-y-110 ml-0.5">▌</span>';
            await delay(60); // Slower
          } else {
            await delay(20 + Math.random() * 10); // Slower
          }
        }
      }
      if (isMounted && sessionRef.current === session) {
        el.innerHTML = rendered.trim();
        if (onCompleteRef.current) {
          onCompleteRef.current();
        }
      }
    };

    type();

    return () => {
      isMounted = false;
      sessionRef.current = 0;
    };
  }, [text]);

  return (
    <span ref={containerRef} className={`${className} min-h-[1.5em]`} />
  );
}
