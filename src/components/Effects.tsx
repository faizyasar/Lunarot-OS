import React, { useEffect, useRef } from 'react';

function randArabic() {
  const ARABIC = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي';
  return ARABIC[Math.floor(Math.random() * ARABIC.length)];
}

export function Typewriter({ 
  text, 
  chargedList = [], 
  className, 
  style 
}: { 
  text: string; 
  chargedList?: string[]; 
  className?: string; 
  style?: React.CSSProperties;
  key?: React.Key;
}) {
  const containerRef = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    const element = containerRef.current;
    if (!element) return;

    element.innerHTML = '';
    const words = text.split(' ');
    let rendered = '';
    const session = Math.random().toString();
    element.setAttribute('data-session', session);

    const delay = (ms: number) => new Promise(r => setTimeout(r, ms));

    async function type() {
      for (let w = 0; w < words.length; w++) {
        if (element?.getAttribute('data-session') !== session) return;
        const word = words[w];
        if (!word) continue;

        const isAsterisk = word.startsWith('*') && word.endsWith('*');
        const cleanWord = word.replace(/\*/g, '');
        const cleanLower = cleanWord.toLowerCase().replace(/[^a-z-]/g, '');
        
        const isCustom = chargedList.some(cw => cw.toLowerCase().replace(/[^a-z-]/g, '') === cleanLower);
        const isHyphen = cleanWord.includes('-') && cleanWord.length > 5;
        const charged = isAsterisk || isCustom || isHyphen;

        if (charged) {
          element.innerHTML = rendered + '<span class="etch-cursor">▌</span>';
          await delay(130 + Math.random() * 90);
          
          const flickCount = 5 + Math.random() * 5;
          for (let f = 0; f < flickCount; f++) {
            if (element.getAttribute('data-session') !== session) return;
            const ghost = cleanWord.split('').map(c => c.match(/[a-zA-Z]/) ? randArabic() : c).join('');
            element.innerHTML = rendered + `<span class="etch-ghost">${ghost}</span><span class="etch-cursor">▌</span>`;
            await delay(25 + Math.random() * 20);
          }
          
          if (element.getAttribute('data-session') !== session) return;
          element.innerHTML = rendered + `<span class="etch-ghost">${cleanWord}</span><span class="etch-cursor">▌</span>`;
          await delay(60 + Math.random() * 40);

          if (element.getAttribute('data-session') !== session) return;
          rendered += `<span class="etch-word">${cleanWord}</span> `;
          element.innerHTML = rendered + '<span class="etch-cursor">▌</span>';
          await delay(40 + Math.random() * 30);
        } else {
          if (element.getAttribute('data-session') !== session) return;
          rendered += cleanWord + ' ';
          element.innerHTML = rendered + '<span class="etch-cursor">▌</span>';
          
          if (cleanWord.match(/[,;:—]/)) {
            await delay(80 + Math.random() * 60);
          } else if (cleanWord.match(/[.!?]$/)) {
            element.innerHTML = rendered;
            await delay(350 + Math.random() * 150);
            if (element.getAttribute('data-session') !== session) return;
            element.innerHTML = rendered + '<span class="etch-cursor">▌</span>';
            await delay(40);
          } else {
            await delay(12 + Math.random() * 8);
          }
        }
      }
      if (element?.getAttribute('data-session') === session) {
        element.innerHTML = rendered.trim();
      }
    }
    
    type();
  }, [text, chargedList]);

  return <div ref={containerRef} className={className} style={style} />;
}


export function HoverText({ text, className, style }: { text: string, className?: string, style?: React.CSSProperties }) {
  return (
    <div className={className} style={style}>
      {text.split('').map((char, i) => (
        <span key={i} className="char-span">
          {char === ' ' ? '\u00A0' : char}
        </span>
      ))}
    </div>
  );
}
