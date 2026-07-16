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
import { ViewStack } from './components/ViewStack';
import { VariableFontProximity } from './components/VariableFontProximity';
import './index.css';

const CARDS = [
  <OracleGateCard key="oracle" />,
  <AestheticTokensCard key="tokens" />,
  <SacredInputFieldsCard key="inputs" />,
  <PoeticTypographyCard key="poetic" />,
  <AsciiControlCard key="ascii" />,
  <IntegrationGuideCard key="guide" />,
];

export default function App() {
  const [collapsed, setCollapsed] = useState(false);
  const [activeCardIdx, setActiveCardIdx] = useState(0);

  useEffect(() => {
    const handleTopCardChanged = (e: any) => {
      setActiveCardIdx(e.detail?.originalIndex ?? 0);
    };
    window.addEventListener('top-card-changed', handleTopCardChanged);
    return () => window.removeEventListener('top-card-changed', handleTopCardChanged);
  }, []);

  return (
    <>
      <StarsCanvas />
      
      <ASCIIWaves />
      
      <div id="asciiContainer">
        <AsciiEyes />
      </div>

      <div id="appWrapper">
        <header>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, width: '30%' }}>
            <span style={{ color: 'var(--gold)', fontWeight: 'bold' }}>◇</span>
            <VariableFontProximity 
              label="LUNAROT OS // STANDALONE"
              fromWeight={300}
              toWeight={900}
              strength={45}
              fontSize="9.5px"
              color="#554444"
              style={{ letterSpacing: '0.25em', zIndex: 100 }}
              onClick={() => {
                setCollapsed(prev => !prev);
              }}
            />
          </div>
          
          <div style={{ display: 'flex', gap: 16, alignItems: 'center', justifyContent: 'center' }}>
            <button
              onClick={() => {
                window.dispatchEvent(new CustomEvent('change-card', { detail: { cardId: 0 } }));
              }}
              className={`nav-btn ${activeCardIdx === 0 ? 'active-primary' : ''}`}
            >
              ◆ SACRED ORACLE
            </button>

            <button
              onClick={() => {
                window.dispatchEvent(new CustomEvent('change-card', { detail: { cardId: 1 } }));
              }}
              className={`nav-btn ${activeCardIdx >= 1 && activeCardIdx <= 4 ? 'active-secondary' : ''}`}
            >
              ◆ STYLE SHOWCASE
            </button>

            <button
              onClick={() => {
                window.dispatchEvent(new CustomEvent('change-card', { detail: { cardId: 5 } }));
              }}
              className={`nav-btn ${activeCardIdx === 5 ? 'active-secondary' : ''}`}
            >
              ◆ INTEGRATION
            </button>
          </div>
          
          <div style={{ width: '30%', display: 'flex', justifyContent: 'flex-end', fontFamily: '"JetBrains Mono", monospace', fontSize: '8px', letterSpacing: '0.2em', color: 'rgba(255, 255, 255, 0.35)' }}>
            ASTRAL_SHELL_OK // SYS_ACTIVE
          </div>
        </header>

        <div id="viewContainer" style={{ opacity: collapsed ? 0 : 1, pointerEvents: collapsed ? 'none' : 'auto', transition: 'opacity 0.6s ease' }}>
          <ViewStack views={CARDS} cardWidth={460} cardHeight={600} />
        </div>

        <footer>
          <span>SACRED COF DECAY COMPILER v5.18-C // standalone shell online</span>
          <span>CHANCELLERY OF THE VOID</span>
        </footer>
      </div>
    </>
  );
}
