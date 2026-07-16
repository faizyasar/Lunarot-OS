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
              style={{
                fontFamily: '"JetBrains Mono", monospace',
                fontSize: '8px',
                letterSpacing: '0.2em',
                padding: '4px 12px',
                background: activeCardIdx === 0 ? '#ffffff' : 'transparent',
                color: activeCardIdx === 0 ? '#000000' : 'rgba(255, 255, 255, 0.4)',
                border: activeCardIdx === 0 ? '1px solid #ffffff' : '1px solid rgba(255, 255, 255, 0.15)',
                boxShadow: activeCardIdx === 0 ? '0 0 10px rgba(255,255,255,0.3)' : 'none',
                cursor: 'pointer',
                fontWeight: 'bold',
                textTransform: 'uppercase',
                transition: 'all 0.3s'
              }}
            >
              ◆ SACRED ORACLE
            </button>

            <button
              onClick={() => {
                window.dispatchEvent(new CustomEvent('change-card', { detail: { cardId: 1 } }));
              }}
              style={{
                fontFamily: '"JetBrains Mono", monospace',
                fontSize: '8px',
                letterSpacing: '0.2em',
                padding: '4px 12px',
                background: (activeCardIdx >= 1 && activeCardIdx <= 4) ? 'rgba(0, 0, 0, 0.6)' : 'transparent',
                color: (activeCardIdx >= 1 && activeCardIdx <= 4) ? 'var(--gold)' : 'rgba(255, 255, 255, 0.4)',
                border: (activeCardIdx >= 1 && activeCardIdx <= 4) ? '1px solid var(--gold)' : '1px solid rgba(255, 255, 255, 0.15)',
                boxShadow: (activeCardIdx >= 1 && activeCardIdx <= 4) ? '0 0 10px rgba(200,164,90,0.2)' : 'none',
                cursor: 'pointer',
                fontWeight: 'bold',
                textTransform: 'uppercase',
                transition: 'all 0.3s'
              }}
            >
              ◆ STYLE SHOWCASE
            </button>

            <button
              onClick={() => {
                window.dispatchEvent(new CustomEvent('change-card', { detail: { cardId: 5 } }));
              }}
              style={{
                fontFamily: '"JetBrains Mono", monospace',
                fontSize: '8px',
                letterSpacing: '0.2em',
                padding: '4px 12px',
                background: activeCardIdx === 5 ? 'rgba(0, 0, 0, 0.6)' : 'transparent',
                color: activeCardIdx === 5 ? '#efede8' : 'rgba(255, 255, 255, 0.4)',
                border: activeCardIdx === 5 ? '1px solid #efede8' : '1px solid rgba(255, 255, 255, 0.15)',
                boxShadow: activeCardIdx === 5 ? '0 0 10px rgba(239,237,232,0.25)' : 'none',
                cursor: 'pointer',
                fontWeight: 'bold',
                textTransform: 'uppercase',
                transition: 'all 0.3s'
              }}
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
