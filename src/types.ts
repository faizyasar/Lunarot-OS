export interface Card {
  name: string;
  num: string;
  glyph: string;
  tradition: string;
}

export interface DrawnCard extends Card {
  reversed: boolean;
  broken: boolean;
  burning: boolean;
}

export interface NatalUser {
  sun: string;
  moon: string;
  rising: string | null;
  hasRising: boolean;
  name: string | null;
  sunIdx: number;
  moonIdx: number;
  risingIdx: number | null;
  jd: number;
}

export interface Planet {
  name: string;
  symbol: string;
  deg: number;
  sign: string;
  color: string;
}

export const SIGN_NAMES = [
  'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
  'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
];

export const ELEMENT_COLOR: Record<string, string> = {
  Aries: '#e05050',
  Taurus: '#80c860',
  Gemini: '#f0d060',
  Cancer: '#7ec8e3',
  Leo: '#f5c842',
  Virgo: '#b0e0b0',
  Libra: '#f0a0e0',
  Scorpio: '#c080a0',
  Sagittarius: '#ffd580',
  Capricorn: '#a08060',
  Aquarius: '#80e8ff',
  Pisces: '#8080ff'
};

export const DECK: Card[] = [
  { name: "The Fool", num: "0", glyph: "🜁", tradition: "The Leap of Faith" },
  { name: "The Magician", num: "I", glyph: "☿", tradition: "The Vessel" },
  { name: "The High Priestess", num: "II", glyph: "☽", tradition: "The Inner Sanctum" },
  { name: "The Empress", num: "III", glyph: "♀", tradition: "The Holy Mother" },
  { name: "The Emperor", num: "IV", glyph: "♂", tradition: "The Divine Law" },
  { name: "The Hierophant", num: "V", glyph: "♉", tradition: "The Initiated Teaching" },
  { name: "The Lovers", num: "VI", glyph: "♊", tradition: "The Holy Covenant" },
  { name: "The Chariot", num: "VII", glyph: "♋", tradition: "Merkabah Mysticism" },
  { name: "Strength", num: "VIII", glyph: "♌", tradition: "The Greater Jihad" },
  { name: "The Hermit", num: "IX", glyph: "⊕", tradition: "The Desert Fathers" },
  { name: "Wheel of Fortune", num: "X", glyph: "♃", tradition: "Divine Providence" },
  { name: "Justice", num: "XI", glyph: "♎", tradition: "The Final Reckoning" },
  { name: "The Hanged Man", num: "XII", glyph: "♆", tradition: "The Dark Night" },
  { name: "Death", num: "XIII", glyph: "♏", tradition: "Fanaa · Sufi Annihilation" },
  { name: "Temperance", num: "XIV", glyph: "♐", tradition: "Tikkun Olam" },
  { name: "The Devil", num: "XV", glyph: "♑", tradition: "Zoroastrian Shadow" },
  { name: "The Tower", num: "XVI", glyph: "🜂", tradition: "The Prophetic Strike" },
  { name: "The Star", num: "XVII", glyph: "★", tradition: "Ahura Mazda's Light" },
  { name: "The Moon", num: "XVIII", glyph: "☾", tradition: "The Veil of Maya" },
  { name: "The Sun", num: "XIX", glyph: "☉", tradition: "The Divine Illumination" },
  { name: "Judgement", num: "XX", glyph: "🜃", tradition: "The Final Trumpet" },
  { name: "The World", num: "XXI", glyph: "♄", tradition: "Return to Ein Sof" },
  { name: "Ace of Cups", num: "A·♥", glyph: "🜄", tradition: "Divine Love · Agape" },
  { name: "Three of Swords", num: "III·⚔", glyph: "△", tradition: "The Pierced Heart" },
  { name: "Five of Cups", num: "V·♥", glyph: "🜄", tradition: "The Spilled and Standing" },
  { name: "Ten of Pentacles", num: "X·◈", glyph: "◈", tradition: "The Living Legacy" },
  { name: "Page of Wands", num: "P·🔥", glyph: "🜂", tradition: "The Unlit Torch" },
  { name: "Knight of Swords", num: "Kn·⚔", glyph: "⚔", tradition: "Truth at Speed" },
  { name: "Queen of Cups", num: "Q·♥", glyph: "🜄", tradition: "The Throne of Empathy" },
  { name: "King of Pentacles", num: "K·◈", glyph: "◈", tradition: "The Patient Empire" },
  { name: "Seven of Wands", num: "VII·🔥", glyph: "🜂", tradition: "The Defended Summit" },
  { name: "Two of Cups", num: "II·♥", glyph: "🜄", tradition: "The Mirrored Soul" }
];

export const SIGN_ADJ: Record<string, string[]> = {
  Aries:       ['ignited', 'sovereign', 'first-born', 'ungoverned', 'headlong', 'scorched', 'nascent', 'raw-edged', 'unbroken', 'blazing', 'impulsive', 'initiating', 'fierce', 'untamed', 'rushing', 'crackling'],
  Taurus:      ['rooted', 'slow-turning', 'earthbound', 'unhurried', 'anchored', 'mineral', 'enduring', 'lush', 'immovable', 'patient', 'sensate', 'verdant', 'weighted', 'solid', 'persistent', 'laden'],
  Gemini:      ['doubled', 'mercurial', 'half-lit', 'mutable', 'edge-walking', 'flickering', 'bifurcated', 'restless', 'curious', 'windborne', 'plural', 'scattered', 'quicksilver', 'unresolved', 'circling', 'twice-told'],
  Cancer:      ['tidal', 'shell-wearing', 'lunar-pulled', 'interior', 'moonlit', 'retreating', 'ancestral', 'soft-shelled', 'protective', 'dreaming', 'submerged', 'tender', 'walled', 'remembering', 'saltwater', 'enclosed'],
  Leo:         ['gilded', 'sun-fixed', 'sovereign', 'heart-forward', 'performing', 'radiant', 'proud', 'generous', 'central', 'illuminated', 'magnanimous', 'warm-blooded', 'theatrical', 'glowing', 'named', 'seen'],
  Virgo:       ['precise', 'discerning', 'grain-sorted', 'quiet-handed', 'exact', 'ritual', 'attending', 'mending', 'cleansed', 'analytical', 'devoted', 'fault-finding', 'minimal', 'careful', 'ordered', 'gathered'],
  Libra:       ['suspended', 'weighing', 'wind-minded', 'both-sided', 'aesthetic', 'hovering', 'diplomatic', 'unresolved', 'harmonising', 'soft-spoken', 'mirrored', 'balanced', 'air-born', 'refining', 'considering', 'between'],
  Scorpio:     ['subterranean', 'molten', 'still-water', 'unblinking', 'venom-laced', 'regenerating', 'deep-cut', 'obsidian', 'penetrating', 'fixed', 'alchemical', 'silent', 'magnetic', 'unearthing', 'relentless', 'unseen'],
  Sagittarius: ['arrow-loosed', 'horizon-bound', 'fire-riding', 'expansive', 'half-wild', 'philosophical', 'wandering', 'truth-hungry', 'centauric', 'boundless', 'bright-aimed', 'roaming', 'questioning', 'free', 'overshot', 'becoming'],
  Capricorn:   ['stone-built', 'patient-climbing', 'winter-born', 'austere', 'load-bearing', 'long-shadowed', 'mineral', 'summit-seeking', 'structured', 'disciplined', 'enduring', 'measured', 'reserved', 'ancient', 'earned', 'slow-lit'],
  Aquarius:    ['electric', 'detached', 'future-haunted', 'cold-lit', 'visionary', 'estranged', 'signal-sending', 'air-fixed', 'alien', 'reforming', 'disconnected', 'crystalline', 'strange', 'remote', 'ahead', 'untouched'],
  Pisces:      ['dissolving', 'oceanic', 'border-thin', 'permeable', 'fog-born', 'dreaming', 'everything-and-nothing', 'uncontained', 'fluid', 'boundaryless', 'surrendered', 'empathic', 'mythic', 'liminal', 'wavering', 'unnamed'],
};

export const CARD_ADJ: Record<string, string[]> = {
  'The Fool':          ['threshold', 'unbegun', 'unburdened', 'about to fall', 'leaping'],
  'The Magician':      ['channelling', 'willed', 'instrumental', 'deliberate', 'conjuring'],
  'The High Priestess':['veiled', 'unspeaking', 'between', 'lunar', 'kept'],
  'The Empress':       ['abundant', 'embodied', 'fertile', 'earthen', 'overflowing'],
  'The Emperor':       ['structured', 'lawful', 'fathered', 'built', 'immovable'],
  'The Hierophant':    ['inherited', 'transmitted', 'orthodox', 'encoded', 'received'],
  'The Lovers':        ['choosing', 'split', 'mirrored', 'covenanted', 'doubled'],
  'The Chariot':       ['directed', 'harnessed', 'moving', 'controlled', 'driven'],
  'Strength':          ['tamed', 'soft-powerful', 'patient', 'animal', 'held'],
  'The Hermit':        ['solitary', 'lantern-holding', 'withdrawn', 'inward', 'alone'],
  'Wheel of Fortune':  ['turning', 'cyclic', 'fated', 'indifferent', 'returning'],
  'Justice':           ['consequenced', 'balanced', 'exacting', 'clear', 'answering'],
  'The Hanged Man':    ['suspended', 'inverted', 'waiting', 'surrendered', 'still'],
  'Death':             ['ending', 'composting', 'releasing', 'transforming', 'departing'],
  'Temperance':        ['alchemising', 'patient', 'blending', 'middle', 'measured'],
  'The Devil':         ['bound', 'shadowed', 'chained', 'seduced', 'refusing to leave'],
  'The Tower':         ['struck', 'collapsing', 'revealed', 'sudden', 'undone'],
  'The Star':          ['hoping', 'wounded-guiding', 'night-lit', 'open', 'visible'],
  'The Moon':          ['illusory', 'subterranean', 'howling', 'unclear', 'dreaming'],
  'The Sun':           ['clarified', 'returned', 'warm', 'visible', 'named'],
  'Judgement':         ['called', 'resurrected', 'answered', 'awakened', 'summoned'],
  'The World':         ['completed', 'dancing', 'encompassed', 'whole', 'arrived'],
  'Ace of Cups':       ['overflowing', 'given', 'opened', 'held out', 'beginning'],
  'Three of Swords':   ['pierced', 'grief-clear', 'through-cut', 'named at last', 'honest'],
  'Five of Cups':      ['mourning', 'spilled', 'backwards-facing', 'grieving', 'still counting'],
  'Ten of Pentacles':  ['legacy-built', 'accumulated', 'inherited', 'lasting', 'given forward'],
  'Page of Wands':     ['spark-stage', 'unlit', 'restless', 'almost-beginning', 'bright'],
  'Knight of Swords':  ['charging', 'truth-first', 'fast', 'unpausing', 'cutting through'],
  'Queen of Cups':     ['witnessed', 'empathic', 'throne-holding', 'feeling-named', 'present'],
  'King of Pentacles': ['patient-mastered', 'solid', 'earned', 'unhurried', 'grounded'],
  'Seven of Wands':    ['defended', 'summit-alone', 'holding ground', 'outnumbered', 'standing'],
  'Two of Cups':       ['mirrored', 'meeting', 'recognised', 'offered', 'mutual']
};

export const TEMPLATES_LINE = [
  'something {chart} and {card} —',
  'the {sign} in you, {card}',
  'a {chart} thing {card} in the dark',
  '{card}, as only the {sign} knows how',
  'what is {chart} becomes {card}',
  'the {sign} tongue — {chart}, {card}',
  '{chart} light through a {card} window',
  'born {chart}, arriving {card}',
  'the {sign} moves {chart} here — {card}',
  'neither {chart} nor {card}, both',
  'the {chart} part of you that is {card}',
  '{chart} like {sign}, {card} like water',
  'to be {chart} is to become {card}',
  'the {card} surface of a {chart} thing',
  '{chart} hands, {card} intentions',
  'something {sign} — {chart} until {card}',
  '{chart} where it started, {card} where it lands',
  'the {sign} way of being {card}',
  'not quite {chart}, not yet {card}',
  '{card} — which is what {chart} looks like from the outside'
];

export const TEMPLATES_SYNTHESIS = [
  'The {sun} carries something {sunAdj}. The {moon} holds something {moonAdj}. What the cards have drawn toward the surface — {cardAdj1}, then {cardAdj2} — is not new, only finally visible.',
  'Something {sunAdj} in the bones. Something {moonAdj} in the blood. The spread names the space between: {cardAdj1} pressing against {cardAdj2}, the self as its own unfinished argument.',
  'The {sun} arrives {sunAdj}. The {moon} stays {moonAdj}. The three positions reveal what the chart already suspected — a {cardAdj1} life navigating a {cardAdj2} world, still translating.',
  'There is something {sunAdj} about the way it begins, and something {moonAdj} about the way it ends. The middle is what the cards name: {cardAdj1}, then {cardAdj2}, then the long silence after.'
];

export const CARD_SINS: Record<string, string> = {
  'The Fool': 'Gluttony', 'The Magician': 'Pride', 'The High Priestess': 'Envy',
  'The Empress': 'Lust', 'The Emperor': 'Pride', 'The Hierophant': 'Sloth',
  'The Lovers': 'Lust', 'The Chariot': 'Pride', 'Strength': 'Pride',
  'The Hermit': 'Sloth', 'Wheel of Fortune': 'Greed', 'Justice': 'Wrath',
  'The Hanged Man': 'Sloth', 'Death': 'Wrath', 'Temperance': 'Gluttony',
  'The Devil': 'Greed', 'The Tower': 'Wrath', 'The Star': 'Envy',
  'The Moon': 'Envy', 'The Sun': 'Pride', 'Judgement': 'Wrath',
  'The World': 'Gluttony', 'Ace of Cups': 'Lust', 'Three of Swords': 'Wrath',
  'Five of Cups': 'Envy', 'Ten of Pentacles': 'Greed', 'Page of Wands': 'Lust',
  'Knight of Swords': 'Wrath', 'Queen of Cups': 'Lust', 'King of Pentacles': 'Greed',
  'Seven of Wands': 'Pride', 'Two of Cups': 'Lust'
};

export const SIN_MANIFESTATIONS: Record<string, { boon: string; buff: string; curse: string }> = {
  'Pride': {
    boon: "You are imbued with absolute certainty. The world bends to the weight of your presence, and doubt shatters against your skin.",
    buff: "You gain a surge of confidence, shielding you from criticism, though it isolates you. You elevate yourself, but the air grows incredibly thin.",
    curse: "Your vision narrows entirely to your own brilliance. You are blinded by the light of your own making, unable to see the earth rushing to meet you."
  },
  'Greed': {
    boon: "The material fabric of the world aligns in your favor. What you reach for is already moving toward your open hands.",
    buff: "You are granted the sharp, unblinking eye to see opportunity where others see dirt, but you are cursed with the inability to ever feel sated.",
    curse: "You accumulate without end, but the vessel is cracked. You will possess everything, and it will mean absolutely nothing."
  },
  'Lust': {
    boon: "You become a conduit for feral inspiration and visceral attraction. The world is drawn inexorably toward your center.",
    buff: "You are fueled by a sudden, violent passion that overrides all logic. It is a powerful engine, but it runs entirely on your own blood.",
    curse: "Obsession eclipses reason. You will be entirely consumed by the object of your fixation, leaving nothing of your original self behind."
  },
  'Envy': {
    boon: "You are granted the terrifying ability to see the hidden worth and secret flaws in others, turning comparison into absolute strategic advantage.",
    buff: "You are driven to outpace your peers, fueled by a dark, competitive venom. It propels you forward, but leaves a bitter taste in your mouth.",
    curse: "Your own blessings will rot before your eyes, rendered entirely invisible by your fixation on the light of another. You will starve while watching them eat."
  },
  'Gluttony': {
    boon: "You possess the terrifying capacity to absorb every experience, metabolizing chaos and turning excess into pure, raw power.",
    buff: "You are given the endurance to process overwhelming amounts of stress or indulgence without breaking, but you will never know when to stop.",
    curse: "You are paralyzed by abundance. The flood of your own desires will rise above your head, drowning you in the very things you craved."
  },
  'Wrath': {
    boon: "Your anger becomes a precise and holy instrument. It will clear away the dead wood, striking down false idols without consuming your own foundation.",
    buff: "You are granted unstoppable momentum to annihilate the obstacles in your path, but the heat of your advance will alienate those who walk beside you.",
    curse: "The fire turns inward and outward at once. You will destroy the guilty and the innocent indiscriminately, leaving yourself to rule over ashes."
  },
  'Sloth': {
    boon: "You achieve perfect, unbothered stillness. You conserve your essence while the world exhausts itself beating against your walls.",
    buff: "Urgency fails to penetrate your aura. You are completely protected by a heavy apathy, but you watch your life pass as if through a thick fog.",
    curse: "Atrophy rots the foundation. Time and opportunity will continue to move forward, but you will remain forever trapped exactly where you are."
  }
};

export const CARD_CONJ: Record<string, string[]> = {
  'Sun': ['Sun'], 'Moon': ['Moon'], 'Star': ['Venus', 'Moon'], 'Tower': ['Mars', 'Saturn'],
  'Devil': ['Saturn'], 'Lovers': ['Venus', 'Moon'], 'Chariot': ['Mars', 'Sun'],
  'Strength': ['Sun', 'Mars'], 'Hermit': ['Saturn', 'Mercury'], 'Wheel': ['Jupiter', 'Sun'],
  'Justice': ['Saturn', 'Mercury'], 'Hanged': ['Moon'], 'Death': ['Mars'],
  'Temperance': ['Jupiter', 'Venus'], 'Priestess': ['Moon'], 'Empress': ['Venus', 'Moon'],
  'Emperor': ['Sun', 'Saturn'], 'Hierophant': ['Jupiter', 'Saturn'],
  'Magician': ['Mercury', 'Sun'], 'Fool': ['Sun'], 'Judgement': ['Sun'],
  'World': ['Saturn', 'Jupiter'], 'Cups': ['Moon', 'Venus'], 'Swords': ['Mars', 'Mercury'],
  'Wands': ['Sun', 'Mars'], 'Pentacles': ['Saturn', 'Venus']
};

export function getSunSign(month: number, day: number): number {
  const cuts = [
    [3, 21], [4, 20], [5, 21], [6, 21], [7, 23], [8, 23],
    [9, 23], [10, 23], [11, 22], [12, 22], [1, 20], [2, 19]
  ];
  for (let i = 0; i < 12; i++) {
    const [m, d] = cuts[i];
    const [nm, nd] = cuts[(i + 1) % 12];
    if ((month === m && day >= d) || (month === nm && day < nd)) return i;
  }
  return 9;
}

export function toJD(year: number, month: number, day: number, hour = 12): number {
  const a = Math.floor((14 - month) / 12);
  const y = year + 4800 - a;
  const m = month + 12 * a - 3;
  const JDN = day + Math.floor((153 * m + 2) / 5) + 365 * y + Math.floor(y / 4) - Math.floor(y / 100) + Math.floor(y / 400) - 32045;
  return JDN + (hour - 12) / 24;
}

export function getMoonSign(jd: number): number {
  const REF_JD = 2451549.5;
  const REF_SIGN = 9;
  const LUNAR = 29.530589;
  const SIGN_DAYS = LUNAR / 12;
  const offset = Math.floor((jd - REF_JD) / SIGN_DAYS) % 12;
  return ((REF_SIGN + offset) % 12 + 12) % 12;
}

export function getRisingSign(jd: number, birthHour: number): number {
  const sunLon = (jd - 2451545.0) * 360 / 365.25;
  const sunSign = Math.floor(((sunLon % 360) + 360) % 360 / 30);
  const signOffset = Math.round((birthHour - 12) / 2);
  return ((sunSign + signOffset + 3) % 12 + 12) % 12;
}

export function getArabicGlitchText(): string {
  const arabicChars = 'ابجدهوزحطيكلمنسعفصقرشتثخذضظغ✦❂✡☽☉♀♂☿♃♄♆';
  return arabicChars[Math.floor(Math.random() * arabicChars.length)];
}
