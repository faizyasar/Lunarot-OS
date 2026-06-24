import {
  SIGN_ADJ,
  CARD_ADJ,
  TEMPLATES_LINE,
  TEMPLATES_SYNTHESIS,
  CARD_SINS,
  SIN_MANIFESTATIONS,
  NatalUser,
  DrawnCard,
} from './types';

export function pick<T>(arr: T[]): T {
  return arr[Math.floor(Math.random() * arr.length)];
}

export function makeLine(chartSign: string, cardName: string, isReversed: boolean): string {
  const chartAdj = pick(SIGN_ADJ[chartSign] || SIGN_ADJ['Pisces']);
  let cardAdj = pick(CARD_ADJ[cardName] || ['present', 'still', 'unnamed']);
  
  if (isReversed) {
    const neg = ['not quite', 'once', 'almost', 'barely', 'refusing to be'];
    cardAdj = pick(neg) + ' ' + cardAdj;
  }
  
  return pick(TEMPLATES_LINE)
    .replace('{chart}', chartAdj)
    .replace('{card}', cardAdj)
    .replace('{sign}', chartSign);
}

export function calculateSinOutcome(drawn: DrawnCard[]): string {
  const sinCounts: Record<string, number> = {};
  
  drawn.forEach(c => {
    const s = CARD_SINS[c.name] || 'Pride';
    sinCounts[s] = (sinCounts[s] || 0) + 1;
  });
  
  let dominantSin = Object.keys(sinCounts).reduce((a, b) => 
    sinCounts[a] > sinCounts[b] ? a : b
  );
  
  if (sinCounts[dominantSin] === 1 && drawn.length >= 2) {
    dominantSin = CARD_SINS[drawn[1].name] || 'Pride';
  }

  const negativeCount = drawn.filter(c => c.reversed || c.broken).length;
  let type: 'boon' | 'buff' | 'curse' = 'boon';
  if (negativeCount === 1) type = 'buff';
  if (negativeCount >= 2) type = 'curse';
  
  const manifestation = SIN_MANIFESTATIONS[dominantSin]?.[type];
  return manifestation || "The void is silent on your destiny.";
}

export function makeSynthesis(natal: NatalUser, drawn: DrawnCard[]): string {
  const tmpl = pick(TEMPLATES_SYNTHESIS);
  const sunAdj = pick(SIGN_ADJ[natal.sun] || ['stone-built']);
  const moonAdj = pick(SIGN_ADJ[natal.moon] || ['oceanic']);
  
  const allAdjs = drawn.reduce<string[]>((acc, c) => 
    acc.concat(CARD_ADJ[c.name] || ['present']), []
  );
  
  const ca1 = pick(allAdjs);
  const rest = allAdjs.filter(a => a !== ca1);
  const ca2 = rest.length ? pick(rest) : pick(allAdjs);
  
  return tmpl
    .replace('{sun}', natal.sun)
    .replace('{sunAdj}', sunAdj)
    .replace('{moon}', natal.moon)
    .replace('{moonAdj}', moonAdj)
    .replace('{cardAdj1}', ca1)
    .replace('{cardAdj2}', ca2);
}

export function makeSynthesisParagraphs(natal: NatalUser, drawn: DrawnCard[]): string[] {
  const single = makeSynthesis(natal, drawn);
  
  if (drawn.length < 3) {
    return [single, "The tapestry of fate is still unfurling."];
  }
  
  const a1 = pick(CARD_ADJ[drawn[0].name] || ['present']);
  const a2 = pick(CARD_ADJ[drawn[1].name] || ['still']);
  const a3 = pick(CARD_ADJ[drawn[2].name] || ['unnamed']);
  const sunAdj = pick(SIGN_ADJ[natal.sun] || ['stone-built']);
  const moonAdj = pick(SIGN_ADJ[natal.moon] || ['oceanic']);
  
  let p2 = `The arc from ${drawn[0].name} to ${drawn[2].name} passes through ${drawn[1].name}. ${a1} becoming ${a2}, then ${a3}. A ${sunAdj} instinct meeting a ${moonAdj} horizon. The chart already knew. The cards only confirmed it. `;
  
  p2 += calculateSinOutcome(drawn);

  return [single, p2];
}
