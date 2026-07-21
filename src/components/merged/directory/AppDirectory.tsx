import React, { useState, useMemo, useEffect, useRef } from 'react';
import { Card, DECK, CARD_ADJ, CARD_SINS, SIN_MANIFESTATIONS, CARD_CONJ, CARD_EXPLANATIONS } from '../types';
import InteractiveText from '../InteractiveText';
import EtchedTypewriter from './EtchedTypewriter';
import AtmosphericFluff from './AtmosphericFluff';
import OptionWheel from './OptionWheel';

interface AppDirectoryProps {
  onUpdateActivePlanets: (planets: Set<string>) => void;
  onContextChange?: (text: string) => void;
}

export default function AppDirectory({ onUpdateActivePlanets, onContextChange }: AppDirectoryProps) {
  const [selectedCard, setSelectedCard] = useState<Card>(DECK[0]);
  const [searchTerm, setSearchTerm] = useState('');
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (onContextChange) {
      onContextChange(`${selectedCard.name.toUpperCase()} // ${selectedCard.tradition.toUpperCase()}`);
    }
  }, [selectedCard, onContextChange]);

  const handleMouseMove = (e: React.MouseEvent) => {
    if (containerRef.current) {
      const rect = containerRef.current.getBoundingClientRect();
      setMousePos({ x: e.clientX - rect.left, y: e.clientY - rect.top });
    }
  };

  const filteredDeck = useMemo(() => {
    return DECK.filter((c) =>
      c.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      c.tradition.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }, [searchTerm]);

  useEffect(() => {
    if (searchTerm && filteredDeck.length > 0 && !filteredDeck.includes(selectedCard)) {
      setSelectedCard(filteredDeck[0]);
    }
  }, [searchTerm, filteredDeck, selectedCard]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (document.activeElement?.tagName === 'INPUT') return;
      if (filteredDeck.length === 0) return;
      
      const currentIndex = filteredDeck.findIndex(c => c.name === selectedCard.name);
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        const nextIndex = (currentIndex + 1) % filteredDeck.length;
        setSelectedCard(filteredDeck[nextIndex]);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        const prevIndex = (currentIndex - 1 + filteredDeck.length) % filteredDeck.length;
        setSelectedCard(filteredDeck[prevIndex]);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [filteredDeck, selectedCard]);

  const cardAdjectives = CARD_ADJ[selectedCard.name] || [];
  const cardSin = CARD_SINS[selectedCard.name];
  const sinData = cardSin ? SIN_MANIFESTATIONS[cardSin] : null;
  const conjuncts = CARD_CONJ[selectedCard.name] || [];

  useEffect(() => {
    onUpdateActivePlanets(new Set(CARD_CONJ[selectedCard.name] || []));
  }, [selectedCard.name, onUpdateActivePlanets]);

  return (
    <>
      <AtmosphericFluff />
      <div className="flex-1 flex flex-col overflow-hidden relative w-full items-center justify-center py-4 px-4 sm:px-8 bg-transparent">
        
        {/* GOTHIC PANEL CONTAINER WITH FULL TRANSPARENCY */}
        <div 
          ref={containerRef}
          className="w-full max-w-6xl h-full flex flex-row bg-transparent border border-[#ffffff]/20 relative z-25 group overflow-hidden"
          onMouseMove={handleMouseMove}
        >
          <div className="absolute inset-1.5 border border-dashed border-[#ffffff]/10 pointer-events-none z-0" />

          {/* Subtle Mouse spotlight effect */}
          <div 
            className="pointer-events-none absolute inset-0 transition-opacity duration-300 opacity-0 group-hover:opacity-100 z-0"
            style={{
              background: `radial-gradient(800px circle at ${mousePos.x}px ${mousePos.y}px, rgba(255, 255, 255, 0.05), transparent 40%)`
            }}
          />

          {/* Mobile Sidebar Overlay */}
          {isSidebarOpen && (
            <div 
              className="absolute inset-0 z-30 bg-black/40 backdrop-blur-sm md:hidden"
              onClick={() => setIsSidebarOpen(false)}
            />
          )}
          
          {/* SIDEBAR */}
          <div className={`absolute inset-y-6 left-1.5 z-40 w-[80%] max-w-xs md:relative md:inset-auto md:w-80 md:flex border-r border-[#ffffff]/15 flex-col bg-transparent transition-transform duration-500 mt-0 mb-0 md:mt-6 md:mb-6 md:ml-1.5 h-[calc(100%-3rem)] md:h-auto ${isSidebarOpen ? 'translate-x-0' : '-translate-x-[110%] md:translate-x-0'}`}>
            <div className="p-4 border-b border-[#ffffff]/15 flex items-center gap-2">
              <span className="text-[#ffffff] font-mono text-xs">&gt;</span>
              <input 
                type="text" 
                placeholder="SEARCH DECK..." 
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full bg-transparent text-[#efede8] text-xs outline-none font-mono placeholder:text-[#665555] uppercase tracking-widest transition-colors"
              />
            </div>
            
            {/* Infinite 3D OptionWheel Card Scroll */}
            <div className="flex-1 min-h-0 relative">
              {filteredDeck.length > 0 ? (
                <OptionWheel
                  items={filteredDeck}
                  selectedItem={selectedCard}
                  onSelect={setSelectedCard}
                  itemHeight={76}
                  radius={260}
                  renderItem={(card, isSelected) => (
                    <div className={`text-left font-mono text-xs sm:text-sm flex items-center justify-between w-full transition-all duration-300 border-l-2 py-3 px-4 ${
                      isSelected 
                      ? 'bg-[#ffffff]/5 text-[#ffffff] border-[#ffffff]' 
                      : 'text-[#666] border-transparent hover:text-[#cfc9c0] hover:border-[#ffffff]/20'
                    }`}>
                      <div className="flex flex-col min-w-0">
                        <span className={`font-cinzel text-sm sm:text-base tracking-widest uppercase truncate ${isSelected ? 'text-[#ffffff] drop-shadow-[0_0_8px_rgba(255,255,255,0.3)]' : 'text-[#888]'}`}>
                          {card.name}
                        </span>
                        <span className="text-[9px] sm:text-[10px] tracking-[0.2em] text-[#555] uppercase mt-1 truncate">
                          {card.tradition}
                        </span>
                      </div>
                      <span className={`text-lg sm:text-xl font-cinzel shrink-0 ${isSelected ? 'text-[#ffffff] scale-110' : 'opacity-20'}`}>{card.glyph}</span>
                    </div>
                  )}
                />
              ) : (
                <div className="p-4 text-xs text-[#555] tracking-widest uppercase text-center mt-4">
                  NO CARDS FOUND
                </div>
              )}
            </div>
          </div>

          {/* CONTENT VIEWPORT */}
          <div className="flex-1 overflow-y-auto p-6 pt-16 md:p-12 lg:p-16 flex flex-col scrollbar-hide relative z-10 bg-transparent mt-6 mb-6 mr-1.5 ml-1.5 md:ml-0">
            
            {/* Mobile menu toggle */}
            <button 
              className="md:hidden absolute top-4 left-4 z-20 text-[#ffffff] hover:text-white p-2 border border-[#ffffff]/20 bg-transparent flex items-center justify-center transition-colors"
              onClick={() => setIsSidebarOpen(true)}
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1" d="M4 6h16M4 12h16M4 18h8"></path></svg>
            </button>

            <span className="absolute top-0 right-4 font-mono text-[7px] text-[#554444] tracking-[0.3em] uppercase pointer-events-none">{selectedCard.num}</span>

            <div className="flex flex-col gap-2 border-b border-[#ffffff]/15 pb-4 mb-6 group/header relative mt-2 md:mt-0">
              <div className="flex items-center justify-between mt-2">
                <div className="flex flex-col">
                  <div className="flex flex-col md:flex-row md:items-baseline md:gap-4">
                    <h1 className="text-3xl sm:text-4xl md:text-4xl font-cinzel text-[#efede8] uppercase tracking-wide transition-all duration-500 origin-left">
                      <InteractiveText text={selectedCard.name} />
                    </h1>
                    <div className="text-[10px] md:text-xs font-mono text-[#838aa0] uppercase tracking-widest mt-2 md:mt-0 transition-all duration-500 border-l-2 border-[#838aa0]/20 pl-2">
                      <span className="text-[#ffffff]">TRADITION:</span> <span className="font-garamond italic lowercase tracking-wide text-sm text-[#cfc9c0]">"{selectedCard.tradition}"</span>
                    </div>
                  </div>
                </div>
                <div className="text-4xl sm:text-5xl md:text-5xl opacity-25 font-cinzel text-[#ffffff]" style={{ textShadow: "0 0 15px rgba(255,255,255,0.3)" }}>
                  {selectedCard.glyph}
                </div>
              </div>
            </div>

            <div className="flex flex-col gap-6 pb-6 bg-transparent">
              <div className="flex flex-col md:flex-row md:flex-wrap gap-6 md:gap-8 bg-transparent">
                {/* Esoteric Adjectives */}
                {cardAdjectives.length > 0 && (
                  <section className="group/section flex-1 min-w-[200px]">
                    <h3 className="text-[8px] tracking-[0.3em] text-[#ffffff] font-mono uppercase mb-3 border-l-2 border-[#ffffff] pl-2 transition-all">
                      Resonant Keywords
                    </h3>
                    <div className="flex flex-wrap gap-1.5">
                      {cardAdjectives.map((adj) => (
                        <span key={adj} className="px-2.5 py-1 text-[9px] font-mono uppercase tracking-widest border border-[#ffffff]/15 text-[#cfc9c0] hover:text-[#fff] hover:border-[#ffffff]/40 bg-transparent transition-all duration-300 cursor-default hover:scale-105">
                          {adj}
                        </span>
                      ))}
                    </div>
                  </section>
                )}

                {/* Astrological Conjuncts */}
                {conjuncts.length > 0 && (
                  <section className="group/section flex-1 min-w-[200px]">
                    <h3 className="text-[8px] tracking-[0.3em] text-[#ffffff] font-mono uppercase mb-3 border-l-2 border-[#ffffff] pl-2 transition-all">
                      Astrological Conjuncts
                    </h3>
                    <div className="flex flex-wrap gap-2">
                      {conjuncts.map((planet) => (
                        <div key={planet} className="flex items-center gap-1.5 px-2.5 py-1 border border-[#ffffff]/15 bg-transparent rounded-none transition-all duration-300 cursor-default">
                            <div className="w-1 h-1 rounded-full" style={{ backgroundColor: '#ffffff' }} />
                            <span className="text-[9px] font-mono tracking-widest uppercase text-[#cfc9c0]">{planet}</span>
                        </div>
                      ))}
                    </div>
                  </section>
                )}
              </div>

              {/* Shadow / Sin Manifestations (Immediate, clean render without techy fake scanning delay) */}
              {cardSin && sinData && (
                <section className="border border-[#ffffff]/15 p-6 relative overflow-hidden transition-all duration-500 mt-4 min-h-[160px] flex flex-col justify-center bg-transparent">
                  <div className="absolute inset-1.5 border border-dashed border-[#ffffff]/5 pointer-events-none" />
                  
                  <div className="w-full">
                    <span className="absolute top-2 left-4 font-mono text-[7px] text-red-700/60 tracking-[0.3em] uppercase pointer-events-none">
                      ASSOCIATED WITH // {cardSin.toUpperCase()}
                    </span>
                    
                    <div className="mt-6 flex flex-col gap-6">
                      <div className="font-garamond text-base sm:text-lg leading-relaxed text-[#cfc9c0] text-justify relative z-10">
                        <EtchedTypewriter 
                          text={CARD_EXPLANATIONS[selectedCard.name] || `${selectedCard.tradition} is the esoteric subtext.`}
                          chargedWords={["flesh", "shadow", "soul", "void", "abyss", "flame", "blood", "potential"]}
                        />
                      </div>
                      <div className="font-garamond text-base sm:text-lg leading-relaxed text-[#cfc9c0] text-justify italic relative z-10 pt-4 border-t border-[#ffffff]/10">
                        <span className="text-[#ffffff] font-cinzel text-xl mr-1 opacity-50">"</span>
                        <EtchedTypewriter 
                          text={`${sinData.boon} ${sinData.buff} ${sinData.curse}`} 
                          chargedWords={[cardSin, "blood", "flesh", "shadow", "soul", "void", "abyss", "flame"]}
                        />
                        <span className="text-[#ffffff] font-cinzel text-xl ml-1 opacity-50">"</span>
                      </div>
                    </div>
                  </div>
                </section>
              )}
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
