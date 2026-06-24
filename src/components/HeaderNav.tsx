interface HeaderNavProps {
  currentView: 'oracle' | 'showcase' | 'about';
  onViewChange: (view: 'oracle' | 'showcase' | 'about') => void;
  title?: string;
  subtitle?: string;
}

export default function HeaderNav({
  currentView,
  onViewChange,
  title = 'LUNAROT ENGINE OS // TEMPLATE V.1',
  subtitle = 'STATUS: DESIGN_SYSTEM_ONLINE',
}: HeaderNavProps) {
  return (
    <header className="w-full relative z-40 pt-3 pb-3 px-6 sm:px-8 flex flex-col md:flex-row justify-between items-center select-none shrink-0 border-b border-white/10 bg-black/80 backdrop-blur-md font-mono text-[7px] md:text-[8px] tracking-[0.2em] text-white/40 gap-3">
      {/* Brand Title */}
      <div className="flex items-center gap-2">
        <span className="text-[var(--gold)] font-bold">◇</span>
        <span className="text-white/80 font-bold uppercase tracking-[0.3em]">
          {title}
        </span>
      </div>

      {/* View Selectors */}
      <div className="flex items-center gap-4 sm:gap-6">
        <button
          onClick={() => onViewChange('oracle')}
          className={`px-3 py-1 border transition-all duration-300 font-bold cursor-pointer tracking-[0.25em] ${
            currentView === 'oracle'
              ? 'border-white bg-white text-black shadow-[0_0_10px_rgba(255,255,255,0.3)]'
              : 'border-white/20 text-white/50 hover:text-white hover:border-white/55'
          }`}
        >
          ◆ SACRED ORACLE
        </button>

        <button
          onClick={() => onViewChange('showcase')}
          className={`px-3 py-1 border transition-all duration-300 font-bold cursor-pointer tracking-[0.25em] ${
            currentView === 'showcase'
              ? 'border-[var(--gold)] bg-black/60 text-[var(--gold)] shadow-[0_0_10px_rgba(200,164,90,0.2)]'
              : 'border-white/20 text-white/50 hover:text-white hover:border-white/55'
          }`}
        >
          ◆ STYLE SHOWCASE
        </button>

        <button
          onClick={() => onViewChange('about')}
          className={`px-3 py-1 border transition-all duration-300 font-bold cursor-pointer tracking-[0.25em] ${
            currentView === 'about'
              ? 'border-[#efede8] bg-black/60 text-[#efede8] shadow-[0_0_10px_rgba(239,237,232,0.25)]'
              : 'border-white/20 text-white/50 hover:text-white hover:border-white/55'
          }`}
        >
          ◆ ABOUT
        </button>
      </div>

      {/* Subtitle Telemetry */}
      <div className="hidden md:flex items-center gap-2">
        <span className="w-1.5 h-1.5 rounded-full bg-[var(--gold)] animate-pulse" />
        <span>{subtitle}</span>
      </div>
    </header>
  );
}
