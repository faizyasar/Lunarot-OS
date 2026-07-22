import { useState, useEffect } from 'react';
import { StarsCanvas, AsciiEyes } from './components/Backgrounds';
import { ASCIIWaves } from './components/ASCIIWaves';
import { OracleGateCard } from './components/OracleView';
import { 
  AestheticTokensCard, 
  AsciiControlCard, 
  SacredInputFieldsCard, 
  PoeticTypographyCard, 
  IntegrationGuideCard 
} from './components/ShowcaseView';
import AppTarot from './components/merged/tarot/AppTarot';
import AppPachinko from './components/merged/pachinko/AppPachinko';
import AppAnkoku from './components/merged/ankoku/AppAnkoku';
import AppDirectory from './components/merged/directory/AppDirectory';
import AppArtShowcase from './components/merged/art/AppArtShowcase';
import { NatalUser, Planet } from './components/merged/types';
import './index.css';

// System showcase folder aggregator
function SystemShowcase() {
  return (
    <div className="w-full h-full overflow-y-auto p-4 sm:p-6 space-y-8 scrollbar-thin scrollbar-thumb-white/10">
      <AestheticTokensCard />
      <SacredInputFieldsCard />
      <PoeticTypographyCard />
      <AsciiControlCard />
      <IntegrationGuideCard />
    </div>
  );
}

// System configuration editor
function EditVesselConfig({ user, onReSeed }: { user: NatalUser; onReSeed: () => void }) {
  return (
    <div className="w-full h-full flex flex-col items-center justify-center p-4 sm:p-8 text-center font-mono relative">
      <div className="max-w-md w-full bg-black/60 border border-[#ffffff]/30 p-6 rounded-none relative shadow-2xl">
        <div className="absolute inset-1 border border-dashed border-[#ffffff]/15 pointer-events-none" />
        <h3 className="font-cinzel text-sm text-[#ffffff] tracking-widest uppercase mb-4">edit-vessel-handshake.conf</h3>
        
        <div className="space-y-2 text-left text-[10px] sm:text-xs text-[#cfc9c0] border-b border-[#ffffff]/15 pb-4 mb-6">
          <div className="flex justify-between"><span className="text-[#888]">VESSEL_NAME :</span> <span>{user.name}</span></div>
          <div className="flex justify-between"><span className="text-[#888]">JULIAN_DATE :</span> <span>{user.jd.toFixed(4)}</span></div>
          <div className="flex justify-between"><span className="text-[#888]">NATAL_SUN   :</span> <span>{user.sun} ({user.sunIdx * 30 + 15}°)</span></div>
          <div className="flex justify-between"><span className="text-[#888]">NATAL_MOON  :</span> <span>{user.moon} ({user.moonIdx * 30 + 15}°)</span></div>
          {user.rising && (
            <div className="flex justify-between"><span className="text-[#888]">NATAL_RISING:</span> <span>{user.rising} ({user.risingIdx * 30}°)</span></div>
          )}
        </div>

        <p className="font-garamond text-xs italic text-[#cfc9c0]/70 mb-6 leading-relaxed">
          Recoil vessel consciousness parameters. This will terminate active alchemical sectors and return to the lockscreen portal.
        </p>

        <button 
          onClick={onReSeed}
          className="w-full px-4 py-2.5 border border-white/40 bg-white/10 text-white hover:bg-white/20 hover:text-white transition-all duration-300 font-bold uppercase tracking-widest text-[9px] cursor-pointer"
        >
          ✦ RE-LINK VESSEL COGNITION
        </button>
      </div>
    </div>
  );
}

const FOLDERS = [
  {
    name: '📁 applications',
    key: 'apps',
    files: [
      { name: 'sacred-draw.bin', path: '/apps/sacred-draw.bin', icon: '✦' },
      { name: 'astral-pachinko.bin', path: '/apps/astral-pachinko.bin', icon: '✶' },
    ]
  },
  {
    name: '📁 research',
    key: 'research',
    files: [
      { name: 'sites-log.md', path: '/research/sites-log.md', icon: '📄' },
      { name: 'link-web-map.md', path: '/research/link-web-map.md', icon: '📄' },
      { name: 'dev-history.md', path: '/research/dev-history.md', icon: '📄' },
      { name: 'deka-archives.md', path: '/research/deka-archives.md', icon: '📄' },
      { name: 'social-conduit.md', path: '/research/social-conduit.md', icon: '📄' },
    ]
  },
  {
    name: '📁 database',
    key: 'db',
    files: [
      { name: 'tarot-directory.index', path: '/db/tarot-directory.index', icon: '📁' },
    ]
  },
  {
    name: '🪐 lnrtdka.drr.ac',
    key: 'art',
    files: [
      { name: 'art-showcase.bin', path: '/art/art-showcase.bin', icon: '🪐' }
    ]
  },
  {
    name: '📁 system',
    key: 'sys',
    files: [
      { name: 'show-aesthetic-tokens.exe', path: '/sys/show-aesthetic-tokens.exe', icon: '⚙' },
      { name: 'edit-vessel-handshake.conf', path: '/sys/edit-vessel-handshake.conf', icon: '⟳' },
    ]
  }
];

export default function App() {
  const [booted, setBooted] = useState(false);
  const [natalUser, setNatalUser] = useState<NatalUser | null>(null);
  const [activeFile, setActiveFile] = useState('/apps/sacred-draw.bin');
  const [openFolders, setOpenFolders] = useState<Set<string>>(new Set(['apps', 'research', 'db', 'art', 'sys']));
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [isRevealed, setIsRevealed] = useState(false);
  const [contextualText, setContextualText] = useState('chancellery of the void');

  // Shared planetary calculations coordinates
  const [planets, setPlanets] = useState<Planet[]>([]);
  const [activePlanets, setActivePlanets] = useState<Set<string>>(new Set());
  const [isPurging, setIsPurging] = useState(false);

  const toggleFolder = (key: string) => {
    setOpenFolders(prev => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });
  };

  const handleRecoilConsciousness = () => {
    setActivePlanets(new Set());
    setIsPurging(false);
  };

  useEffect(() => {
    if (!booted) {
      setContextualText('chancellery of the void');
      return;
    }
    
    switch (activeFile) {
      case '/apps/sacred-draw.bin':
        setContextualText('SACRED GEOMETRY CANVAS // DRAW TO CONJURE');
        break;
      case '/apps/astral-pachinko.bin':
        setContextualText('ASTRAL PACHINKO SIMULATOR // PHYSICS METRIC');
        break;
      case '/research/sites-log.md':
        setContextualText('PORTAL ACCESS LOG // RESEARCH ARCHIVES');
        break;
      case '/research/link-web-map.md':
        setContextualText('LINK CONDUIT NETWORKS // INTERNET TOPOLOGY');
        break;
      case '/research/dev-history.md':
        setContextualText('DEVELOPMENT CHRONICLES // RECONSTRUCTED LOGS');
        break;
      case '/research/deka-archives.md':
        setContextualText('DEKA HISTORICAL DOSSIER // CHANNELS RECORDED');
        break;
      case '/research/social-conduit.md':
        setContextualText('COMMUNICATIONS CONDUITS // INGRESS SOCIALS');
        break;
      case '/sys/show-aesthetic-tokens.exe':
        setContextualText('AESTHETIC TELEMETRY TOKENS // SYSTEM METRICS');
        break;
      case '/sys/edit-vessel-handshake.conf':
        setContextualText('VESSEL HANDSHAKE REGISTRY // UPDATE CHART');
        break;
      default:
        break;
    }
  }, [activeFile, booted]);

  const handleReSeed = () => {
    setBooted(false);
    setNatalUser(null);
    setActivePlanets(new Set());
    setIsPurging(false);
  };

  // Auto-close sidebar on smaller viewports on file select
  const selectFile = (path: string) => {
    if (path.startsWith('http://') || path.startsWith('https://')) {
      window.open(path, '_blank');
      return;
    }
    setActiveFile(path);
    if (window.innerWidth < 768) {
      setSidebarOpen(false);
    }
  };

  return (
    <div className="crt-monitor">
      <div className="crt-screen-glass">
        <div className="crt-scanlines" />
        <div className="crt-vignette" />
        <div className="crt-bezel" />

        {/* Astrological starfield canvas in background */}
        <StarsCanvas planets={planets} activePlanets={activePlanets} />
        
        <ASCIIWaves />
        
        {/* Main ASCII reactive eye system */}
        <div 
          id="asciiContainer" 
          className={`transition-all duration-[2500ms] ease-out ${
            !booted 
              ? 'opacity-0 scale-75 pointer-events-none' 
              : isPurging 
                ? 'opacity-80 scale-100' 
                : 'opacity-100 scale-100'
          }`}
        >
          <AsciiEyes />
        </div>

        <div id="appWrapper" className="flex flex-col h-screen w-screen overflow-hidden relative">
        {/* Desktop virtual workspace after birth chart boot */}
        {booted && (
          <div className="flex-1 flex flex-col min-h-0 relative z-30">
            {/* Header Telemetry line */}
            <header className="w-full h-11 border-b border-white/10 px-4 flex items-center justify-between shrink-0 font-mono text-[9px] tracking-[0.2em] bg-transparent z-30 select-none">
              <div className="flex items-center gap-3">
                <button 
                  onClick={() => setSidebarOpen(prev => !prev)}
                  className="px-2 py-1 border border-white/10 hover:bg-[#ffffff]/10 hover:border-[#ffffff]/30 transition-colors uppercase font-bold tracking-[0.2em] cursor-pointer text-[#cfc9c0]"
                >
                  ☰ EXPLORER
                </button>
                <button 
                  onClick={() => setIsRevealed(prev => !prev)}
                  className="text-[#ffffff] font-bold hidden sm:inline hover:text-white transition-colors cursor-pointer select-none px-2 py-1 border border-transparent hover:border-[#ffffff]/30 hover:bg-[#ffffff]/5 uppercase tracking-[0.2em]"
                >
                  LUNAROT OS v6.1
                </button>
              </div>

              {natalUser && (
                <div className="text-[#665555] truncate px-4 font-mono hidden md:block lowercase tracking-wider text-[8px]">
                  vessel: {natalUser.name} | sun: {natalUser.sun} | moon: {natalUser.moon} {natalUser.rising && `| asc: ${natalUser.rising}`}
                </div>
              )}

              <button 
                onClick={handleReSeed}
                className="px-2 py-1.5 border border-white/40 bg-white/10 text-white hover:bg-white/20 hover:text-white transition-colors uppercase font-bold tracking-[0.2em] cursor-pointer"
              >
                ⟳ RE-SEED
              </button>
            </header>

            {/* Core Workspaces dual-pane layout wrapper */}
            <div className={`flex-1 flex flex-row min-h-0 relative z-20 transition-all duration-300 ${isRevealed ? 'opacity-0 pointer-events-none scale-95' : 'opacity-100'}`}>
              
              <aside 
                className="absolute md:relative inset-y-0 left-0 z-40 border-r border-white/10 flex flex-col bg-black/95 md:bg-transparent select-none transition-all duration-200 ease-in-out overflow-hidden h-full"
                style={{
                  width: sidebarOpen ? '256px' : '0px',
                  opacity: sidebarOpen ? 1 : 0,
                  pointerEvents: sidebarOpen ? 'auto' : 'none'
                }}
              >
                <div className="w-64 h-full flex flex-col shrink-0">
                  <div className="p-3 border-b border-white/10 bg-transparent flex items-center justify-between">
                    <span className="font-mono text-[8.5px] text-[#888888] tracking-widest uppercase">Occult Directories</span>
                    <span className="text-[7.5px] text-[#666666] tracking-[0.2em]">DESK_STABLE</span>
                  </div>

                  <div className="flex-1 overflow-y-auto p-4 space-y-4 font-mono text-[10px] tracking-[0.16em] uppercase scrollbar-thin scrollbar-thumb-white/5">
                    {FOLDERS.map((folder) => {
                      const isOpen = openFolders.has(folder.key);
                      return (
                        <div key={folder.key} className="space-y-1">
                          <button
                            onClick={() => toggleFolder(folder.key)}
                            className="flex items-center w-full text-left font-bold text-[#ffffff] hover:text-white transition-colors py-1 cursor-pointer"
                          >
                            <span className="mr-2 text-[8px]">{isOpen ? '▼' : '▶'}</span>
                            {folder.name}
                          </button>
                          
                          {isOpen && (
                            <div className="pl-4 border-l border-[#ffffff]/15 space-y-0.5 ml-1.5">
                              {folder.files.map((file) => {
                                const isSelected = activeFile === file.path;
                                return (
                                  <button
                                    key={file.path}
                                    onClick={() => selectFile(file.path)}
                                    className={`flex items-center w-full text-left py-1.5 px-2 transition-all duration-200 border-l-2 cursor-pointer ${
                                      isSelected 
                                        ? 'bg-white/5 text-white border-[#ffffff] font-bold shadow-[inset_3px_0_0_rgba(255,255,255,0.2)]' 
                                        : 'text-[#838aa0] border-transparent hover:text-white hover:bg-white/5 pl-3'
                                    }`}
                                  >
                                    <span className="mr-2 opacity-65">{file.icon}</span>
                                    <span className="truncate">{file.name}</span>
                                  </button>
                                );
                              })}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              </aside>

              {/* Right Pane - Content switchboard viewport */}
              <main className="flex-1 min-w-0 min-h-0 flex flex-col bg-transparent relative overflow-hidden">
                {/* Embedded window header */}
                <div className="h-6 border-b border-white/5 px-4 flex items-center justify-between shrink-0 font-mono text-[7px] text-[#443333] tracking-[0.2em] bg-transparent select-none">
                  <span>file: {activeFile.toLowerCase()}</span>
                  <span>integrity: stable</span>
                </div>

                <div className="flex-1 min-h-0 min-w-0 relative">
                  {/* File Route Switcher */}
                  {activeFile === '/apps/sacred-draw.bin' && natalUser && (
                    <AppTarot 
                      user={natalUser} 
                      onUpdatePlanets={setPlanets}
                      onUpdateActivePlanets={setActivePlanets}
                      onReset={handleRecoilConsciousness}
                      isPurging={isPurging}
                      setIsPurging={setIsPurging}
                    />
                  )}

                  {activeFile === '/apps/astral-pachinko.bin' && natalUser && (
                    <AppPachinko
                      user={natalUser}
                      onUpdatePlanets={setPlanets}
                      onUpdateActivePlanets={setActivePlanets}
                      onReset={handleRecoilConsciousness}
                      isPurging={isPurging}
                      setIsPurging={setIsPurging}
                    />
                  )}

                  {activeFile === '/research/sites-log.md' && (
                    <AppAnkoku defaultTab="log" />
                  )}

                  {activeFile === '/research/link-web-map.md' && (
                    <AppAnkoku defaultTab="map" />
                  )}

                  {activeFile === '/research/dev-history.md' && (
                    <AppAnkoku defaultTab="dev" />
                  )}

                  {activeFile === '/research/deka-archives.md' && (
                    <AppAnkoku defaultTab="deka" />
                  )}

                  {activeFile === '/research/social-conduit.md' && (
                    <AppAnkoku defaultTab="social" />
                  )}

                  {activeFile === '/db/tarot-directory.index' && (
                    <AppDirectory onUpdateActivePlanets={setActivePlanets} onContextChange={setContextualText} />
                  )}

                  {activeFile === '/art/art-showcase.bin' && (
                    <AppArtShowcase onContextChange={setContextualText} />
                  )}

                  {activeFile === '/sys/show-aesthetic-tokens.exe' && (
                    <SystemShowcase />
                  )}

                  {activeFile === '/sys/edit-vessel-handshake.conf' && natalUser && (
                    <EditVesselConfig user={natalUser} onReSeed={handleReSeed} />
                  )}
                </div>
              </main>

            </div>

            {isRevealed && (
              <div 
                onClick={() => setIsRevealed(false)}
                className="absolute inset-0 z-10 cursor-pointer select-none"
              />
            )}

            {/* Consolidated status footer line */}
            <footer className="h-8 border-t border-white/5 px-6 flex items-center justify-between text-[6px] tracking-[0.2em] text-[#443333] select-none shrink-0 font-mono bg-transparent">
              <span className="text-[var(--gold)] font-bold uppercase tracking-[0.2em]">lunarot OS build {typeof __BUILD_COMMIT_HASH__ !== "undefined" ? __BUILD_COMMIT_HASH__ : "39c2a5d"}</span>
              <span className="hidden sm:inline text-[#ffffff]/60 uppercase tracking-[0.25em] transition-all duration-300">
                {contextualText}
              </span>
              <span>1998-2026</span>
            </footer>
          </div>
        )}

        {/* Locked System Login Gate Screen Overlay */}
        <div 
          className={`absolute inset-0 z-50 transition-all duration-[1200ms] ease-in-out ${
            booted 
              ? 'opacity-0 pointer-events-none scale-105' 
              : 'opacity-100'
          }`}
        >
          <OracleGateCard onSystemBoot={(user) => {
            setNatalUser(user);
            setBooted(true);
          }} />
        </div>
      </div>
    </div>
  </div>
  );
}
