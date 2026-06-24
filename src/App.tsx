import { useState, useEffect } from 'react';
import { NatalUser, Planet } from './types';
import StarBackground from './components/StarBackground';
import AsciiBackgroundEyes from './components/AsciiBackgroundEyes';
import IntroScreen from './components/IntroScreen';
import IntakeScreen from './components/IntakeScreen';
import MainScreen from './components/MainScreen';
import HeaderNav from './components/HeaderNav';
import ShowcaseScreen from './components/ShowcaseScreen';

const SHOWCASE_DEFAULT_PLANETS: Planet[] = [
  { name: 'Sun', symbol: '☉', deg: 120, sign: 'Leo', color: '#c8a45a' },
  { name: 'Moon', symbol: '☽', deg: 245, sign: 'Taurus', color: '#998358' },
  { name: 'Rising', symbol: 'AC', deg: 45, sign: 'Aries', color: '#efede8' },
  { name: 'Mars', symbol: '♂', deg: 180, sign: 'Scorpio', color: '#c8a45a' },
  { name: 'Venus', symbol: '♀', deg: 90, sign: 'Taurus', color: '#ffffff' },
];

const SHOWCASE_DEFAULT_ACTIVE = new Set(['Sun', 'Moon', 'Rising']);

export default function App() {
  const [view, setView] = useState<'oracle' | 'showcase'>('oracle');
  const [screen, setScreen] = useState<'intro' | 'intake' | 'main'>('intro');
  const [user, setUser] = useState<NatalUser | null>(null);

  // States representing background planetary canvas targets
  const [planets, setPlanets] = useState<Planet[]>([]);
  const [activePlanets, setActivePlanets] = useState<Set<string>>(new Set());

  // Dynamic coordinates when switching views
  useEffect(() => {
    if (view === 'showcase') {
      setPlanets(SHOWCASE_DEFAULT_PLANETS);
      setActivePlanets(SHOWCASE_DEFAULT_ACTIVE);
    } else {
      // Return to user data coordinates if they exist
      if (user) {
        // MainScreen will calculate and broadcast coordinates via onUpdatePlanets/ActivePlanets
      } else {
        setPlanets([]);
        setActivePlanets(new Set());
      }
    }
  }, [view, user]);

  const handleDismissIntro = () => {
    setScreen('intake');
  };

  const handleIntakeSubmit = (natalUser: NatalUser) => {
    setUser(natalUser);
    setScreen('main');
  };

  const handleReset = () => {
    setUser(null);
    setPlanets([]);
    setActivePlanets(new Set());
    setScreen('intake');
  };

  return (
    <main className="relative w-screen h-screen max-h-screen text-[var(--parchment)] max-w-full overflow-hidden flex flex-col justify-between select-none bg-black">
      
      {/* Dynamic star twinkling and constellation background lines */}
      <StarBackground planets={planets} activePlanets={activePlanets} />

      {/* Barely visible blurred pair of ASCII eyes tracking mouse & blinking */}
      <AsciiBackgroundEyes />

      {/* Sleek top navigation control bar */}
      <HeaderNav currentView={view} onViewChange={setView} />

      {/* Frame boundary wrapper */}
      <div className="relative z-10 w-full flex-1 flex flex-col items-center justify-center overflow-hidden">
        
        {view === 'oracle' ? (
          <>
            {/* State 1: Gothic intro gate */}
            {screen === 'intro' && (
              <IntroScreen onDismiss={handleDismissIntro} />
            )}

            {/* State 2: Personal birth intake details */}
            {screen === 'intake' && (
              <IntakeScreen onSubmit={handleIntakeSubmit} />
            )}

            {/* State 3: Tarot draw layout & confluence summaries */}
            {screen === 'main' && user && (
              <MainScreen
                user={user}
                onUpdatePlanets={setPlanets}
                onUpdateActivePlanets={setActivePlanets}
                onReset={handleReset}
              />
            )}
          </>
        ) : (
          /* Style Guide Sandbox / Documentation Showcase Screen */
          <ShowcaseScreen />
        )}
        
      </div>
      
    </main>
  );
}
