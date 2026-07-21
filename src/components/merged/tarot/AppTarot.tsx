import React, { useState, useEffect, useRef } from 'react';
import {
  DECK,
  CARD_CONJ,
  NatalUser,
  Planet,
  DrawnCard,
  ELEMENT_COLOR,
  SIGN_NAMES,
  SIGN_ADJ,
  CARD_ADJ,
} from '../types';
import { makeSynthesisParagraphs, pick } from '../utils';

async function etchParagraph(
  el: HTMLElement,
  text: string,
  sessionNum: number,
  currentSessionRef: { current: number }
): Promise<void> {
  el.classList.add('visible'); 
  el.innerHTML = '';
  
  const ARABIC = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي";
  const randArabic = () => ARABIC[Math.floor(Math.random() * ARABIC.length)];
  const msDelay = (ms: number) => new Promise(r => setTimeout(r, ms));
  
  const words = text.split(' ');
  let rendered = '';
  
  // Custom charged word checker
  const allAdjs = new Set<string>();
  Object.values(SIGN_ADJ).forEach((arr) => arr.forEach((w) => allAdjs.add(w.toLowerCase().replace(/[^a-z-]/g, ''))));
  Object.values(CARD_ADJ).forEach((arr) => arr.forEach((w) => allAdjs.add(w.toLowerCase().replace(/[^a-z-]/g, ''))));
  
  const isCharged = (w: string) => {
    const clean = w.toLowerCase().replace(/[^a-z-]/g, '');
    return allAdjs.has(clean) || (clean.includes('-') && clean.length > 5);
  };
  
  for (let w = 0; w < words.length; w++) {
    if (currentSessionRef.current !== sessionNum) return;
    const word = words[w];
    const clean = word.toLowerCase().replace(/[^a-z-]/g, '');
    const charged = isCharged(clean);
        
    if (charged) {
      el.innerHTML = rendered + '<span class="etch-cursor">▌</span>'; 
      await msDelay(130 + Math.random() * 90);
      
      const flickCount = 5 + Math.floor(Math.random() * 5);
      for (let f = 0; f < flickCount; f++) {
        if (currentSessionRef.current !== sessionNum) return;
        const ghost = word.split('').map(c => c.match(/[a-zA-Z]/) ? randArabic() : c).join('');
        el.innerHTML = rendered + '<span class="etch-ghost">' + ghost + '</span><span class="etch-cursor">▌</span>';
        await msDelay(25 + Math.floor(Math.random() * 20));
      }
      
      if (currentSessionRef.current !== sessionNum) return;
      el.innerHTML = rendered + '<span class="etch-ghost">' + word + '</span><span class="etch-cursor">▌</span>'; 
      await msDelay(60 + Math.floor(Math.random() * 40));
      
      if (currentSessionRef.current !== sessionNum) return;
      rendered += '<span class="etch-word">' + word + '</span> '; 
      el.innerHTML = rendered + '<span class="etch-cursor">▌</span>'; 
      await msDelay(40 + Math.floor(Math.random() * 30));
      
    } else {
      if (currentSessionRef.current !== sessionNum) return;
      rendered += word + ' '; 
      el.innerHTML = rendered + '<span class="etch-cursor">▌</span>';
      
      if (word.match(/[,;:—]/)) {
        await msDelay(80 + Math.floor(Math.random() * 60));
      } else if (word.match(/[.!?]$/)) { 
        el.innerHTML = rendered; 
        await msDelay(350 + Math.floor(Math.random() * 150)); 
        if (currentSessionRef.current !== sessionNum) return;
        el.innerHTML = rendered + '<span class="etch-cursor">▌</span>'; 
        await msDelay(40); 
      } else {
        await msDelay(12 + Math.floor(Math.random() * 8));
      }
    }
  }
  if (currentSessionRef.current === sessionNum) {
    el.innerHTML = rendered.trim();
  }
}

interface AppTarotProps {
  user: NatalUser;
  onUpdatePlanets: (planets: Planet[]) => void;
  onUpdateActivePlanets: (active: Set<string>) => void;
  onReset: () => void;
  isPurging: boolean;
  setIsPurging: (val: boolean) => void;
}

const POSITIONS = ["I: ANTECEDENT", "II: CONCURRENT", "III: CONSEQUENT"];

const SVG_BACK = (
  <svg className="w-full h-full p-2 opacity-50" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <circle cx="100" cy="100" r="85" fill="none" stroke="#ffffff" strokeWidth="0.6" strokeDasharray="3 3" />
    <circle cx="100" cy="100" r="75" fill="none" stroke="#ffffff" strokeWidth="0.4" />
    <circle cx="100" cy="100" r="50" fill="none" stroke="#ffffff" strokeWidth="0.8" />
    <circle cx="100" cy="100" r="30" fill="none" stroke="#ffffff" strokeWidth="0.5" />
    <circle cx="100" cy="100" r="15" fill="none" stroke="#ffffff" strokeWidth="1" />
    <line x1="100" y1="10" x2="100" y2="190" stroke="#ffffff" strokeWidth="0.4" strokeDasharray="2 4" />
    <line x1="10" y1="100" x2="190" y2="100" stroke="#ffffff" strokeWidth="0.4" strokeDasharray="2 4" />
    <polygon points="100,15 173,142 27,142" fill="none" stroke="#ffffff" strokeWidth="0.3" opacity="0.6" />
    <polygon points="100,185 173,58 27,58" fill="none" stroke="#ffffff" strokeWidth="0.3" opacity="0.3" />
  </svg>
);

export default function AppTarot({
  user,
  onUpdatePlanets,
  onUpdateActivePlanets,
  onReset,
  isPurging,
  setIsPurging,
}: AppTarotProps) {
  const [drawPhase, setDrawPhase] = useState<'idle' | 'spawning' | 'shuffling' | 'dealing'>('spawning');
  const [shuffling, setShuffling] = useState(true);
  const [drawnCards, setDrawnCards] = useState<DrawnCard[]>([]);
  const [revealed, setRevealed] = useState<boolean[]>([false, false, false]);
  const [paragraphs, setParagraphs] = useState<string[]>([]);
  const [activeSet, setActiveSet] = useState<Set<string>>(new Set());
  const [dealtCount, setDealtCount] = useState(0);
  const [windowWidth, setWindowWidth] = useState(typeof window !== 'undefined' ? window.innerWidth : 1024);
  const [telemetryMessage, setTelemetryMessage] = useState("DESCENT IN PROGRESS // DO NOT BREAK CIRCLE");
  const [cardTransforms, setCardTransforms] = useState<Array<{ x: number; y: number; rot: number }>>([
    { x: 0, y: 0, rot: 0 },
    { x: 0, y: 0, rot: 0 },
    { x: 0, y: 0, rot: 0 },
  ]);
  const [draggingIndex, setDraggingIndex] = useState<number | null>(null);
  
  const dragStart = useRef<{ [key: number]: { x: number; y: number; ox: number; oy: number; rot: number; hasMoved: boolean } }>({});
  const p1Ref = useRef<HTMLDivElement | null>(null);
  const p2Ref = useRef<HTMLDivElement | null>(null);
  const printingSessionRef = useRef<number>(0);

  useEffect(() => {
    const handleResize = () => setWindowWidth(window.innerWidth);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const getShuffleTranslateX = (index: number) => {
    const isMobile = windowWidth < 768;
    const dist = isMobile ? 80 : 160;
    if (index === 0) return dist;
    if (index === 2) return -dist;
    return 0;
  };

  const handleCardPointerDown = (e: React.PointerEvent<HTMLDivElement>, index: number) => {
    if (drawPhase !== 'idle' || index >= dealtCount || isPurging) return;

    dragStart.current[index] = {
      x: e.clientX,
      y: e.clientY,
      ox: cardTransforms[index]?.x || 0,
      oy: cardTransforms[index]?.y || 0,
      rot: cardTransforms[index]?.rot || 0,
      hasMoved: false,
    };
    
    setDraggingIndex(index);
    window.dispatchEvent(new CustomEvent('ascii-eyes-control-custom', { detail: { action: 'track-element', targetId: `wrap-${index}` } }));

    const handleGlobalPointerMove = (moveEvent: PointerEvent) => {
      const data = dragStart.current[index];
      if (!data) return;

      const rawDx = moveEvent.clientX - data.x;
      const rawDy = moveEvent.clientY - data.y;
      const dist = Math.hypot(rawDx, rawDy);
      const maxDrag = 65; 
      let dx = rawDx;
      let dy = rawDy;

      if (dist > maxDrag) {
        dx = (rawDx / dist) * maxDrag;
        dy = (rawDy / dist) * maxDrag;
      } else if (dist > 4) {
        const factor = Math.cos((dist / maxDrag) * (Math.PI / 3));
        dx = rawDx * factor;
        dy = rawDy * factor;
      }

      if (Math.hypot(rawDx, rawDy) > 6) {
        data.hasMoved = true;
      }

      setCardTransforms((prev) => {
        const updated = [...prev];
        updated[index] = {
          x: data.ox + dx,
          y: data.oy + dy,
          rot: 0,
        };
        return updated;
      });
    };

    const handleGlobalPointerUp = () => {
      window.removeEventListener('pointermove', handleGlobalPointerMove);
      window.removeEventListener('pointerup', handleGlobalPointerUp);
      
      setDraggingIndex(null);
      window.dispatchEvent(new CustomEvent('ascii-eyes-control-custom', { detail: { action: 'reset' } }));

      const data = dragStart.current[index];
      if (data) {
        if (!data.hasMoved) {
          handleFlip(index);
        } else {
          setCardTransforms((prev) => {
            const updated = [...prev];
            updated[index] = {
              x: data.ox,
              y: data.oy,
              rot: data.rot,
            };
            return updated;
          });
        }
        delete dragStart.current[index];
      }
    };

    window.addEventListener('pointermove', handleGlobalPointerMove);
    window.addEventListener('pointerup', handleGlobalPointerUp);
  };

  // Compute and broadcast natal planets based on user details
  useEffect(() => {
    const sunDeg = user.sunIdx * 30 + 15;
    const moonDeg = user.moonIdx * 30 + 15;
    
    const initialPlanets: Planet[] = [
      {
        name: 'Sun',
        symbol: '☉',
        deg: sunDeg,
        sign: user.sun,
        color: ELEMENT_COLOR[user.sun] || '#f5c842',
      },
      {
        name: 'Moon',
        symbol: '☽',
        deg: moonDeg,
        sign: user.moon,
        color: ELEMENT_COLOR[user.moon] || '#c8c8ff',
      },
    ];

    if (user.risingIdx !== null && user.rising) {
      initialPlanets.push({
        name: 'Rising',
        symbol: 'AC',
        deg: user.risingIdx * 30,
        sign: user.rising,
        color: ELEMENT_COLOR[user.rising] || '#7ec8e3',
      });
    }

    const planetaryMultipliers = [
      { name: 'Mars', symbol: '♂', speed: 2.0 },
      { name: 'Venus', symbol: '♀', speed: 1.6 },
      { name: 'Mercury', symbol: '☿', speed: 1.1 },
      { name: 'Jupiter', symbol: '♃', speed: 0.08 },
      { name: 'Saturn', symbol: '♄', speed: 0.03 },
    ];

    planetaryMultipliers.forEach((f) => {
      const deg = ((user.jd * f.speed) % 360 + 360) % 360;
      const signIdx = Math.floor(deg / 30);
      const sign = SIGN_NAMES[signIdx];
      initialPlanets.push({
        name: f.name,
        symbol: f.symbol,
        deg,
        sign,
        color: ELEMENT_COLOR[sign] || '#ffffff',
      });
    });

    onUpdatePlanets(initialPlanets);
  }, [user]);

  // Handle deck drawing and shuffling phase
  const triggerDraw = () => {
    setDrawPhase('spawning');
    setShuffling(true);
    setDealtCount(0);
    setRevealed([false, false, false]);
    setParagraphs([]);
    setTelemetryMessage("OS DESK // COMPILING SOL-ASTRAL CONDUITS...");

    const newActive = new Set<string>();
    setActiveSet(newActive);
    onUpdateActivePlanets(newActive);

    const available = [...DECK];
    const drawn: DrawnCard[] = [];
    for (let i = 0; i < 3; i++) {
      const randIdx = Math.floor(Math.random() * available.length);
      const card = available.splice(randIdx, 1)[0];
      const isReversed = Math.random() < 0.45;
      const isBroken = Math.random() < 0.12;

      drawn.push({
        ...card,
        reversed: isReversed,
        broken: isBroken,
        burning: false,
      });
    }
    setDrawnCards(drawn);

    setCardTransforms([
      { x: 0, y: 0, rot: 0 },
      { x: 0, y: 0, rot: 0 },
      { x: 0, y: 0, rot: 0 },
    ]);

    const synthesis = makeSynthesisParagraphs(user, drawn);
    setParagraphs(synthesis);

    setTimeout(() => {
      setDrawPhase('shuffling');
      setTelemetryMessage("MATRIX COMPLEMENT ENFORCED // ROTATING SECTORS...");
      
      const targetOffsets = [
        { x: (Math.random() * 24 - 12), y: (Math.random() * 20 - 10), rot: 0 },
        { x: (Math.random() * 24 - 12), y: (Math.random() * 20 - 10), rot: 0 },
        { x: (Math.random() * 24 - 12), y: (Math.random() * 20 - 10), rot: 0 },
      ];

      setTimeout(() => {
        setDrawPhase('dealing');
        setShuffling(false);
        setTelemetryMessage("RANDOMIZATION COMPLETE // EMITTING CONDUITS...");
        setCardTransforms(targetOffsets);
        setDealtCount(0);
        window.dispatchEvent(new CustomEvent('ascii-eyes-control-custom', { detail: { action: 'track-element', targetId: 'wrap-0', duration: 300 } }));
        
        setTimeout(() => {
          setDealtCount(1);
          setTelemetryMessage("LEFT CONDUIT EMITTED // ANTECEDENT PHASE");
          window.dispatchEvent(new CustomEvent('ascii-eyes-control-custom', { detail: { action: 'track-element', targetId: 'wrap-1', duration: 700 } }));
        }, 300);

        setTimeout(() => {
          setDealtCount(2);
          setTelemetryMessage("CENTER CONDUIT EMITTED // CONCURRENT PHASE");
          window.dispatchEvent(new CustomEvent('ascii-eyes-control-custom', { detail: { action: 'track-element', targetId: 'wrap-2', duration: 700 } }));
        }, 1000);

        setTimeout(() => {
          setDealtCount(3);
          setTelemetryMessage("RIGHT CONDUIT EMITTED // CONSEQUENT PHASE");
          window.dispatchEvent(new CustomEvent('ascii-eyes-control-custom', { detail: { action: 'reset' } }));
        }, 1700);

        setTimeout(() => {
          setDrawPhase('idle');
          setTelemetryMessage("DESCENT COMPLETE // CIRCLE STABILIZED // UNRAVEL CONDUITS TO COMMENCE_");
        }, 2200);

      }, 1800);
    }, 1400);
  };

  useEffect(() => {
    triggerDraw();
  }, [user]);

  const activateConjValues = (cardName: string) => {
    const updated = new Set<string>(activeSet);
    for (const [key, planets] of Object.entries(CARD_CONJ)) {
      if (cardName.toLowerCase().includes(key.toLowerCase())) {
        planets.forEach((p) => updated.add(p));
      }
    }
    setActiveSet(updated);
    onUpdateActivePlanets(updated);
  };

  const handleAnomalyBurn = async (idx: number) => {
    setIsPurging(true);
    setTelemetryMessage(`✦✦ WARNING: CORRUPT ANOMALY DETECTED AT PORTAL ${idx + 1} // INITIATING EXORCISM SEQUENCE ✦✦`);
    
    window.dispatchEvent(new CustomEvent('ascii-eyes-control-custom', { detail: { action: 'track-element', targetId: `wrap-${idx}`, duration: 4200 } }));
    window.dispatchEvent(new CustomEvent('ascii-eyes-control-custom', { detail: { action: 'crazy', duration: 4200 } }));

    await new Promise(r => setTimeout(r, 1500));
    
    setDrawnCards((prev) => {
      const next = [...prev];
      if (next[idx]) {
        next[idx] = { ...next[idx], burning: true };
      }
      return next;
    });

    await new Promise(r => setTimeout(r, 2500));

    setDrawnCards((prev) => {
      const currentNames = prev.map(c => c.name);
      const remaining = DECK.filter(c => !currentNames.includes(c.name));
      
      const next = [...prev];
      if (remaining.length > 0 && next[idx]) {
        const newCard = pick(remaining);
        const isReversed = Math.random() < 0.45;
        next[idx] = {
          ...newCard,
          reversed: isReversed,
          broken: false,
          burning: false,
        };
      }
      
      setTimeout(() => {
        setParagraphs(makeSynthesisParagraphs(user, next));
      }, 50);

      return next;
    });

    setRevealed((prev) => {
      const next = [...prev];
      next[idx] = false;
      return next;
    });

    setTelemetryMessage(`✦ PORTAL ${idx + 1} RE-SEEDED // MUTATION PURGED // UNRAVEL TO CONTINUE ✦`);
    setIsPurging(false);

    setTimeout(() => {
      setTelemetryMessage("DESCENT IN PROGRESS // DO NOT BREAK CIRCLE");
    }, 4500);
  };

  const handleFlip = (idx: number) => {
    if (drawPhase !== 'idle' || idx >= dealtCount || revealed[idx] || isPurging) return;

    const updated = [...revealed];
    updated[idx] = true;
    setRevealed(updated);

    const card = drawnCards[idx];
    if (card) {
      activateConjValues(card.broken ? 'Disaster' : card.name);
      if (card.broken) {
        handleAnomalyBurn(idx);
      }
    }
  };

  const allRevealed = revealed.length > 0 && revealed.every(r => r === true);

  useEffect(() => {
    if (!allRevealed || paragraphs.length === 0) {
      if (p1Ref.current) p1Ref.current.innerHTML = '';
      if (p2Ref.current) p2Ref.current.innerHTML = '';
      return;
    }

    printingSessionRef.current += 1;
    const sessionNum = printingSessionRef.current;

    const runPrinting = async () => {
      if (p1Ref.current) {
        p1Ref.current.innerHTML = '';
        await etchParagraph(p1Ref.current, paragraphs[0], sessionNum, printingSessionRef);
      }
      if (printingSessionRef.current !== sessionNum) return;
      if (p2Ref.current && paragraphs[1]) {
        p2Ref.current.innerHTML = '';
        await etchParagraph(p2Ref.current, paragraphs[1], sessionNum, printingSessionRef);
      }
    };

    runPrinting();

    return () => {
      printingSessionRef.current += 1;
    };
  }, [allRevealed, paragraphs]);

  const solarAdj = SIGN_ADJ[user.sun]?.[0] || 'ignited';
  const lunarAdj = SIGN_ADJ[user.moon]?.[0] || 'tidal';
  
  const formattedAlignment = user.rising 
    ? `${user.name || 'Traveler'}, your sun in ${user.sun} and moon in ${user.moon} align with ${user.rising} rising.`
    : `${user.name || 'Traveler'}, your sun in ${user.sun} and moon in ${user.moon} align with natal coordinates.`;
    
  const formattedAspects = `Solar coordinates spark with ${solarAdj} fire, meeting the deep ${lunarAdj} tides of your inner waters.`;

  return (
    <div className={`flex flex-col w-full h-full text-[#cfc9c0] font-mono relative select-none overflow-hidden animate-[fade-in_1s_ease_forwards] ${isPurging ? 'screen-shake' : ''}`}>
      
      {/* SYSTEM TELEMETRY SUB-HEADER */}
      <header className="w-full relative z-30 pt-3 pb-1 px-4 flex justify-between items-center select-none shrink-0 border-b border-white/5 font-mono text-[7px] text-[#443333] tracking-[0.2em]">
        <span>{isPurging ? "anomaly detected" : "sector tarot active"}</span>
        <span className="lowercase font-bold tracking-wider">{telemetryMessage.toLowerCase()}</span>
        <span>{isPurging ? "purging..." : "stability nominal"}</span>
      </header>

      {/* CENTER WORKSPACE */}
      <main className="flex-1 min-h-0 h-0 flex flex-col items-center justify-center relative z-20 w-full px-4 py-4 overflow-visible">
        
        {/* Tarot Spread cards row */}
        <div className="flex flex-row justify-center items-center gap-4 md:gap-8 lg:gap-10 w-full max-w-4xl select-none">
          {[0, 1, 2].map((i) => {
            const card = drawnCards[i] || {
              name: 'THE ANOMALY',
              num: '???',
              glyph: '⍼',
              tradition: 'Void Paradox',
              reversed: false,
              broken: true,
              burning: false,
            };
            const isDealt = i < dealtCount;
            const isFlipped = revealed[i];

            let opacityVal = 1;
            let containerTransform = 'none';
            let cardTransform = 'none';
            let transitionStr = 'transform 0.6s cubic-bezier(0.19, 1, 0.22, 1), opacity 0.6s ease';
            let zIndexVal = 10;

            if (drawPhase === 'spawning') {
              opacityVal = 1;
              containerTransform = 'none';
              cardTransform = 'none';
              zIndexVal = 10;
              transitionStr = 'transform 0.6s cubic-bezier(0.19, 1, 0.22, 1), opacity 0.6s ease';
            } else if (drawPhase === 'shuffling') {
              opacityVal = 1;
              const xDist = getShuffleTranslateX(i);
              containerTransform = `translate3d(${xDist}px, 0, 0) scale(0.9)`;
              cardTransform = 'none';
              zIndexVal = i === 1 ? 5 : 20;
              transitionStr = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
            } else if (drawPhase === 'dealing') {
              if (isDealt) {
                const tx = cardTransforms[i]?.x || 0;
                const ty = cardTransforms[i]?.y || 0;
                const trot = cardTransforms[i]?.rot || 0;
                containerTransform = `translate3d(${tx}px, ${ty}px, 0) scale(1)`;
                cardTransform = `rotate(${trot}deg)`;
                zIndexVal = draggingIndex === i ? 60 : 15;
                opacityVal = 1;
                transitionStr = 'transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.285), opacity 0.4s ease';
              } else {
                const xDist = getShuffleTranslateX(i);
                const stackY = -i * 3;
                const stackRot = (i - 1) * 3;
                containerTransform = `translate3d(${xDist}px, ${stackY}px, 0) scale(0.85)`;
                cardTransform = `rotate(${stackRot}deg)`;
                zIndexVal = 30 - i;
                opacityVal = 0.85;
                transitionStr = 'transform 0.5s ease-out';
              }
            } else {
              const tx = cardTransforms[i]?.x || 0;
              const ty = cardTransforms[i]?.y || 0;
              const trot = cardTransforms[i]?.rot || 0;
              containerTransform = `translate3d(${tx}px, ${ty}px, 0) scale(1)`;
              cardTransform = `rotate(${trot}deg)`;
              zIndexVal = draggingIndex === i ? 60 : 15;
              opacityVal = 1;
              transitionStr = draggingIndex === i ? 'none' : 'transform 0.6s cubic-bezier(0.19, 1, 0.22, 1), opacity 0.6s ease';
            }

            const shuffleAnimClass = drawPhase === 'shuffling' ? (i === 1 ? 'shuffling-r' : 'shuffling-l') : '';

            return (
              <div 
                key={i} 
                className="flex flex-col items-center"
                style={{
                  opacity: opacityVal,
                  transform: containerTransform,
                  transition: draggingIndex === i ? 'none' : transitionStr,
                  zIndex: zIndexVal,
                }}
              >
                {/* Position label */}
                <div className="font-mono text-[7.5px] tracking-[0.3em] text-white/50 uppercase mb-3 text-center select-none">
                  {POSITIONS[i]}
                </div>

                {/* Tactile Card visually floating */}
                <div 
                  id={`wrap-${i}`} 
                  className="card-wrap select-none touch-none active:scale-[1.01] relative"
                  onPointerDown={(e) => handleCardPointerDown(e, i)}
                  style={{
                    cursor: (draggingIndex === i) ? 'grabbing' : (drawPhase === 'idle' ? 'grab' : 'default'),
                    transform: cardTransform,
                    transition: draggingIndex === i ? 'none' : transitionStr,
                  }}
                >
                  <div
                    onClick={() => handleFlip(i)}
                    className={`card relative ${shuffleAnimClass} ${isFlipped ? 'flipped' : ''} ${card.reversed && !card.broken ? 'rev' : ''} ${card.broken ? 'broken' : ''} ${card.burning ? 'burning' : ''}`}
                  >
                    {/* CARD BACK */}
                    <div className="card-back absolute inset-0 select-none pointer-events-none">
                      {SVG_BACK}
                      <div className="tap-hint font-sans tracking-widest text-white/30">
                        {drawPhase === 'shuffling' ? 'SHUFFLING' : 'UNRAVEL'}
                      </div>
                    </div>

                    {/* CARD FRONT */}
                    <div className="card-front absolute inset-0 select-none">
                      <div className="cnum text-left font-mono tracking-wider text-white/60 w-full text-[8.5px]">
                        {card.broken ? '???' : card.num}
                      </div>

                      <div className="cglyph font-garamond font-semibold select-none text-[48px] md:text-[52px] my-1 text-[#cfc9c0] filter drop-shadow-[0_0_12px_rgba(255,255,255,0.2)]">
                        {card.broken ? '⍼' : card.glyph}
                      </div>

                      <div className="cname font-mono text-[9px] text-center leading-normal text-white font-bold tracking-wider select-none">
                        {card.broken ? 'THE ANOMALY' : card.name.toUpperCase()}
                      </div>

                      <div className="crev font-mono text-[8px] text-white/70 italic tracking-[0.12em] uppercase select-none mt-0.5 h-[10px]">
                        {card.reversed && !card.broken ? '⟳ inverted' : ''}
                      </div>

                      {card.burning && (
                        <div className="absolute inset-x-0 bottom-0 top-0 bg-gradient-to-t from-white/90 via-white/30 to-transparent animate-pulse rounded-lg flex flex-col items-center justify-center overflow-hidden z-25 pointer-events-none">
                          <div className="absolute w-2 h-2 bg-white rounded-full blur-[0.5px] animate-[spark-up_1.2s_infinite_alternate]" style={{ left: '20%', bottom: '5%' }} />
                          <div className="absolute w-1.5 h-1.5 bg-white/70 rounded-full blur-[0.5px] animate-[spark-up_1.5s_infinite_alternate_0.3s]" style={{ left: '50%', bottom: '15%' }} />
                          <div className="absolute w-2.5 h-2.5 bg-white rounded-full blur-[1px] animate-[spark-up_2s_infinite_alternate_0.6s]" style={{ left: '75%', bottom: '8%' }} />
                          <div className="absolute w-1.2 h-3 bg-white/50 rounded-full blur-[0.5px] animate-[spark-up_1.7s_infinite_alternate_0.1s]" style={{ left: '42%', bottom: '22%' }} />
                        </div>
                      )}
                    </div>

                    {/* SPAWNING OVERLAY */}
                    {drawPhase === 'spawning' && (
                      <div className="absolute inset-0 rounded-lg border border-white/10 bg-black/90 flex flex-col items-center justify-center p-3 font-mono text-[8px] text-[#554444] select-none z-50">
                        <span>aligning...</span>
                      </div>
                    )}

                  </div>
                </div>

                {/* Miniature text reading directly below the card */}
                <div
                  className={`mt-3 text-center max-w-[125px] transition-all duration-700 select-none ${
                    (isFlipped && drawPhase === 'idle') ? 'opacity-100 transform translate-y-0' : 'opacity-0 transform translate-y-2 pointer-events-none'
                  }`}
                >
                  <h4 className="font-mono text-[9px] text-white font-bold uppercase tracking-widest mb-0.5 select-none">
                    {card.broken ? 'Broken' : card.name}
                  </h4>
                  <p className="font-mono text-[7px] text-[#888888] tracking-widest uppercase mb-1.5 select-none font-sans">
                    {card.broken ? 'Anomaly' : card.tradition}
                  </p>
                  <p className="font-garamond text-[11px] text-[#cfc9c0]/70 italic leading-relaxed select-none">
                    {card.broken
                      ? 'Shattered conflux.'
                      : card.reversed
                      ? 'Blockaded flow.'
                      : 'Fully manifest.'}
                  </p>
                </div>

              </div>
            );
          })}
        </div>

      </main>

      {/* SUBTEXT & CONVERTED ALIGNMENT DISPLAY PANEL */}
      <div className="w-full max-w-4xl mx-auto flex flex-col items-center justify-center text-center px-4 pb-4 select-none shrink-0 z-30">
        
        <div 
          className="space-y-1 bg-black/50 backdrop-blur-[2px] p-2.5 rounded-none border border-white/10 w-full max-w-xl pointer-events-none select-none transition-all duration-300"
          style={{ borderStyle: 'inset' }}
        >
          <p className="font-garamond text-[11px] md:text-xs tracking-wide leading-relaxed text-[#cfc9c0]/80">
            {formattedAlignment} {formattedAspects}
          </p>

          <div className="h-[1px] bg-gradient-to-r from-transparent via-white/15 to-transparent w-3/4 mx-auto my-1" />

          {/* Typing Synthesis Section */}
          <div className="min-h-[44px] flex items-center justify-center py-0.5 font-garamond">
            {!allRevealed ? (
              <div className="text-[9px] font-mono tracking-[0.25em] text-white/40 uppercase animate-pulse">
                ✦ UNVEIL THE THREE CONCURRENT MOMENTS TO ENFORCE INTERPRETATION ✦
              </div>
            ) : (
              <div className="font-garamond text-[11px] md:text-xs italic text-[#cfc9c0] leading-relaxed select-none max-w-lg text-center">
                <div ref={p1Ref} className="mb-1" />
                <div ref={p2Ref} className="opacity-75 text-[10px]" />
              </div>
            )}
          </div>
        </div>

        {/* Controls action strip */}
        <div className="flex justify-center items-center gap-6 mt-3 font-mono text-[7.5px] tracking-[0.2em] select-none">
          <button
            onClick={triggerDraw}
            disabled={shuffling || isPurging}
            className={`text-[#cfc9c0] hover:text-white transition-colors cursor-pointer ${(shuffling || isPurging) ? 'opacity-30 cursor-not-allowed pointer-events-none' : ''}`}
          >
            re-draw tarot spread
          </button>
          <span className="text-white/10">|</span>
          <button
            onClick={onReset}
            disabled={isPurging}
            className={`text-[#665555] hover:text-[#cfc9c0] transition-colors cursor-pointer ${isPurging ? 'opacity-30 cursor-not-allowed pointer-events-none' : ''}`}
          >
            clear alignment
          </button>
        </div>

      </div>

    </div>
  );
}
