
  // 22 Major Arcana  the main spread
  var MAJORS = [
    { name: 'The Fool', num: '0', glyph: '🜁', trad: 'The Leap of Faith' },
    { name: 'The Magician', num: 'I', glyph: '☿', trad: 'The Vessel' },
    { name: 'The High Priestess', num: 'II', glyph: '☽', trad: 'The Inner Sanctum' },
    { name: 'The Empress', num: 'III', glyph: '♀', trad: 'The Holy Mother' },
    { name: 'The Emperor', num: 'IV', glyph: '♂', trad: 'The Divine Law' },
    { name: 'The Hierophant', num: 'V', glyph: '♉', trad: 'The Initiated Teaching' },
    { name: 'The Lovers', num: 'VI', glyph: '♊', trad: 'The Holy Covenant' },
    { name: 'The Chariot', num: 'VII', glyph: '♋', trad: 'Merkabah Mysticism' },
    { name: 'Strength', num: 'VIII', glyph: '♌', trad: 'The Greater Jihad' },
    { name: 'The Hermit', num: 'IX', glyph: '⊕', trad: 'The Desert Fathers' },
    { name: 'Wheel of Fortune', num: 'X', glyph: '♃', trad: 'Divine Providence' },
    { name: 'Justice', num: 'XI', glyph: '♎', trad: 'The Final Reckoning' },
    { name: 'The Hanged Man', num: 'XII', glyph: '♆', trad: 'The Dark Night' },
    { name: 'Death', num: 'XIII', glyph: '♏', trad: 'Fanaa · Sufi Annihilation' },
    { name: 'Temperance', num: 'XIV', glyph: '♐', trad: 'Tikkun Olam' },
    { name: 'The Devil', num: 'XV', glyph: '♑', trad: 'Zoroastrian Shadow' },
    { name: 'The Tower', num: 'XVI', glyph: '🜂', trad: 'The Prophetic Strike' },
    { name: 'The Star', num: 'XVII', glyph: '★', trad: 'Ahura Mazda\u2019s Light' },
    { name: 'The Moon', num: 'XVIII', glyph: '☾', trad: 'The Veil of Maya' },
    { name: 'The Sun', num: 'XIX', glyph: '☉', trad: 'The Divine Illumination' },
    { name: 'Judgement', num: 'XX', glyph: '🜃', trad: 'The Final Trumpet' },
    { name: 'The World', num: 'XXI', glyph: '♄', trad: 'Return to Ein Sof' }
  ];
  // 56 Minor Arcana  four suit columns behind the main spread
  var SUITS = [
    { name: 'Wands', glyph: '🜂', trad: 'The Suit of Flame' },
    { name: 'Cups', glyph: '🜄', trad: 'The Suit of the Vessel' },
    { name: 'Swords', glyph: '🜁', trad: 'The Suit of the Blade' },
    { name: 'Pentacles', glyph: '🜃', trad: 'The Suit of the Seal' }
  ];
  var RANKS = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Page', 'Knight', 'Queen', 'King'];
  var RANK_NUMS = ['A', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'PG', 'KN', 'QN', 'KG'];
  var DECK = MAJORS.slice();
  SUITS.forEach(function (s) {
    RANKS.forEach(function (r, ri) {
      DECK.push({ name: r + ' of ' + s.name, num: RANK_NUMS[ri], glyph: s.glyph, trad: s.trad });
    });
  });
  // Sacred Index lore banks  lifted verbatim from the production build (index.html)
  var LORE = {"The Fool":"The Leap of Faith in esoteric tradition represents stepping into the unknown without attachment. It is the raw, unformed *potential* before creation, the breath of the void preceding form.","The Magician":"The Vessel symbolizes the human body and mind as a channel for divine will. It is the conduit through which celestial energy manifests into the earthly *flesh* and material reality.","The High Priestess":"The Inner Sanctum represents the hidden, esoteric knowledge guarded behind the veil. It is the silent *shadow* space of intuition where the unwritten mysteries are held.","The Empress":"The Holy Mother in mystical traditions is the active, nurturing principle of nature. She embodies the physical *flesh*, the fertile earth, and the divine matrix of all creation.","The Emperor":"The Divine Law signifies the structural order of the universe imposed upon the chaos of the *void*. It is the unyielding framework that governs celestial mechanics and earthly empires.","The Hierophant":"The Initiated Teaching refers to the unbroken lineage of sacred, spoken truths. It represents the *soul* remembering its celestial origins through rigorous orthodox transmission.","The Lovers":"The Holy Covenant is the alchemical marriage of opposites. It signifies the binding of two fractured halves into a perfect union, seeking to repair the original *shadow* of separation.","The Chariot":"Merkabah (Hebrew: מרכבה) Mysticism centers on the ascent to the divine throne. It is the willed discipline of navigating the *void* and mastering the conflicting forces of light and dark.",Strength:"The Greater Jihad (Arabic: جهاد أكبر) is the internal spiritual struggle against the lower self. It represents the quiet taming of one's own feral *flesh* and animalistic instincts.","The Hermit":"The Desert Fathers were early Christian ascetics who retreated into the barren wilderness. It signifies the deliberate isolation from the world to hear the quiet voice of the *soul*.","Wheel of Fortune":"Divine Providence is the inescapable turning of fate's axis. It signifies the underlying, hidden machinery of destiny that operates beyond human *blood* and understanding.",Justice:"The Final Reckoning is the ultimate weighing of the *soul* against the feather of truth. It represents inescapable cosmic equilibrium and the precise balancing of karmic debts.","The Hanged Man":"The Dark Night of the Soul is the painful purgation of the senses. It is the willing suspension in the *abyss* to dissolve old attachments before spiritual rebirth.",Death:'Fanaa (Arabic: فناء) in Sufism is the "passing away" or "annihilation" of the ego and individual self. Often described as "to die before one dies", it represents the complete dissolution of selfish desires into the *void*, leading to a state of ultimate spiritual union.',Temperance:"Tikkun Olam (Hebrew: תיקון עולם) is the Jewish concept of repairing the shattered vessels of creation. It represents the careful alchemical blending required to heal the fractured *soul* of the world.","The Devil":"Ahriman, the Zoroastrian Shadow, is the destructive spirit of falsehood and bondage. It represents the *abyss* of materialism where the spirit becomes chained to its own basest desires.","The Tower":"The Prophetic Strike is the sudden, violent shattering of false structures. It is the divine *flame* that obliterates intellectual pride and built illusions in a single moment.","The Star":"Ahura Mazda's Light is the uncreated, eternal truth of the highest heaven. It represents the distant, pure radiance that guides the *soul* back from the darkness of the material world.","The Moon":"The Veil of Maya (Sanskrit: माया) is the cosmic illusion of the phenomenal world. It represents the deceptive *shadow* realm that obscures the ultimate, undivided reality from mortal eyes.","The Sun":"The Divine Illumination is the sudden, blinding apprehension of absolute truth. It represents the *flame* of pure consciousness dispelling the last remnants of earthly darkness.",Judgement:"The Final Trumpet is the apocalyptic call to awakening. It signifies the resurrection of the true self from the *flesh* and the final assessment of all earthly actions.","The World":"Ein Sof (Hebrew: אֵין סוֹף) is the Infinite, the absolute state before emanation. It represents the *soul* completing its journey and re-merging flawlessly into the boundless, unknowable divine.","Ace of Cups":"Agape (Greek: ἀघापी) is the unconditional, self-sacrificing love of the divine. It represents the pure, overflowing grace that washes away the stains of the mortal *flesh*.","Three of Swords":"The Pierced Heart symbolizes the necessary trauma of disillusionment. It represents the sharp, clarifying pain that opens the *soul* to truths previously obscured by sentiment.","Five of Cups":"The Spilled and Standing represents the tension between irrecoverable loss and remaining grace. It is the heavy *blood* of grief blinding one to the salvation still present.","Ten of Pentacles":"The Living Legacy is the accumulation of generational wisdom and material stability. It represents the deep roots embedded in the earth and the *blood* lineage stretching through time.","Page of Wands":"The Unlit Torch is the nascent spark of divine inspiration before action. It represents the pure, unformed *flame* of potential waiting for the will to ignite it.","Knight of Swords":"Truth at Speed is the ruthless, kinetic pursuit of intellectual clarity. It represents cutting through the *shadow* of ignorance without hesitation or emotional attachment.","Queen of Cups":"The Throne of Empathy is the seat of profound intuitive understanding. It represents the deep, silent *abyss* of the unconscious where all emotional currents are felt and held.","King of Pentacles":"The Patient Empire is the ultimate mastery over the material sphere. It represents the slow, deliberate cultivation of the *flesh* and earth into a lasting, unshakeable sanctuary.","Seven of Wands":"The Defended Summit is the desperate holding of higher ground against opposition. It represents the solitary *flame* of conviction standing firm against the overwhelming tide of the collective.","Two of Cups":"The Mirrored Soul is the profound recognition of the divine in another. It represents the sacred union of opposites, bridging the *void* between two isolated beings."};
  var SINS = {"The Fool":"Gluttony","The Magician":"Pride","The High Priestess":"Envy","The Empress":"Lust","The Emperor":"Pride","The Hierophant":"Sloth","The Lovers":"Lust","The Chariot":"Pride",Strength:"Pride","The Hermit":"Sloth","Wheel of Fortune":"Greed",Justice:"Wrath","The Hanged Man":"Sloth",Death:"Wrath",Temperance:"Gluttony","The Devil":"Greed","The Tower":"Wrath","The Star":"Envy","The Moon":"Envy","The Sun":"Pride",Judgement:"Wrath","The World":"Gluttony","Ace of Cups":"Lust","Three of Swords":"Wrath","Five of Cups":"Envy","Ten of Pentacles":"Greed","Page of Wands":"Lust","Knight of Swords":"Wrath","Queen of Cups":"Lust","King of Pentacles":"Greed","Seven of Wands":"Pride","Two of Cups":"Lust"};
  var N = DECK.length;

  var scene = document.getElementById('scene');
  var deckEl = document.getElementById('deck');
  var band = document.getElementById('band');
  var wrap = document.getElementById('wrap');
  var flap = document.getElementById('flap');
  var box = document.getElementById('box');
  var statusHint = document.getElementById('statusHint');
  var cardCaption = document.getElementById('cardCaption');

  // build only the 22 major cards + two proxy cards for the minor stack (perf)
  var cards = [];
  var proxy = null;      // the flying/drawn minor card
  var proxyTop = null;   // the card visibly on top of the stack
  var minorTop = 22;
  var cardsBuilt = false;
  function cardFace(c) {
    return '<div class="card-side side-a"></div>' +
      '<div class="card-side side-b">' +
        '<span class="cf-num">' + c.num + '</span>' +
        '<span class="cf-glyph">' + c.glyph + '\uFE0E</span>' +
        '<span class="cf-name">' + c.name + '</span>' +
      '</div>';
  }
  function setProxy(i) {
    proxy.dataset.i = i;
    proxy.innerHTML = cardFace(DECK[i]);
  }
  function setStackTop(i) {
    minorTop = i;
    proxyTop.dataset.i = i;
    proxyTop.innerHTML = cardFace(DECK[i]);
  }
  function nextMinor(i) { return i + 1 > N - 1 ? 22 : i + 1; }
  function buildCards() {
    if (cardsBuilt) return;
    cardsBuilt = true;
    var frag = document.createDocumentFragment();
    for (var i = 0; i < 22; i++) {
      var el = document.createElement('div');
      el.className = 'card';
      el.dataset.i = i;
      el.style.transform = 'translateZ(' + ((i - 10.5) * 0.85) + 'px)';
      el.innerHTML = cardFace(DECK[i]);
      frag.appendChild(el);
      cards.push(el);
    }
    proxy = document.createElement('div');
    proxy.className = 'card minor-proxy hidden';
    setProxy(22);
    proxy.style.transform = MINOR_SPOT;
    frag.appendChild(proxy);
    proxyTop = document.createElement('div');
    proxyTop.className = 'card minor-proxy';
    proxyTop.style.transform = MINOR_SPOT;
    frag.appendChild(proxyTop);
    setStackTop(22);
    frag.appendChild(proxy);
    var stack = document.createElement('div');
    stack.className = 'card minor-stack';
    stack.style.transform = MINOR_STACK_SPOT;
    stack.innerHTML = '<div class="ms-edge ms-top"></div><div class="ms-edge ms-left"></div><div class="ms-edge ms-right"></div><div class="ms-edge ms-bottom"></div><div class="ms-under"></div><div class="ms-cap"></div>';
    frag.appendChild(stack);
    band.parentNode.insertBefore(frag, band);
  }

  /* ===== state machine =====
     wrapped -> boxed -> flapOpen -> drawn -> unbanded -> spread -> inspect */
  var state = 'wrapped';
  var inspected = -1;
  var HINTS = {
    wrapped: 'CLICK TO TEAR THE SHRINK WRAP',
    boxed: 'CLICK THE FLAP TO OPEN THE BOX',
    flapOpen: 'CLICK THE BOX TO SLIDE THE DECK OUT',
    drawn: 'CLICK THE BELLY BAND TO TEAR IT',
    unbanded: 'CLICK THE DECK TO SPREAD IT',
    spread: 'SELECT A CONDUIT',
    inspect: '‹ › BROWSE · CLICK CARD TO RETURN'
  };
  function setHint() {
    var h = HINTS[state];
    statusHint.textContent = h;
    try { parent.postMessage({ lunarotTarotHint: h }, '*'); } catch (e) {}
  }

  var rotX = 14, rotY = 26;
  /* ===== CAMERA PRESETS =====
     One framing per state, desktop vs portrait phone.
     TUNE HERE: drag/pinch on the device to a framing you like,
     tap the CAM readout to copy the numbers, paste them in. */
  var CAM = {
    desktop: {
      wrapped:  { x: 14,    y: 26,  z: 1.25 },
      boxed:    { x: 14,    y: 26,  z: 1.25 },
      flapOpen: { x: 14,    y: 26,  z: 1.25 },
      drawn:    { x: -12,   y: 0,   z: 1.25 },
      unbanded: { x: -12,   y: 0,   z: 1.25 },
      spread:   { x: -30.4, y: 4.0, z: 1.0  },
      inspect:  { x: -30.4, y: 4.0, z: 1.1  }
    },
    portrait: {
      /* reset to stock desktop framing  re-place with the XYZ editor */
      wrapped:  { x: 14,    y: 26,  z: 1.25 },
      boxed:    { x: 14,    y: 26,  z: 1.25 },
      flapOpen: { x: 14,    y: 26,  z: 1.25 },
      drawn:    { x: -12,   y: 0,   z: 1.25 },
      unbanded: { x: -12,   y: 0,   z: 1.25 },
      spread:   { x: -30.4, y: 4.0, z: 1.0  },
      inspect:  { x: -30.4, y: 4.0, z: 1.1  }
    }
  };
  function camMode() {
    return window.innerHeight > window.innerWidth ? 'portrait' : 'desktop';
  }
  /* how wide each state's composition is at scale 1, incl. breathing room 
     zoom is capped so this always fits the viewport width */
  var FIT_W = {
    wrapped: 340, boxed: 340, flapOpen: 360,
    drawn: 360, unbanded: 360,
    spread: 800, inspect: 800
  };
  function goCam(s) {
    var p = CAM[camMode()][s] || CAM[camMode()].boxed;
    var zFit = window.innerWidth / (FIT_W[s] || 700);
    animateRotTo(p.x, p.y);
    setScale(Math.min(p.z, zFit));
  }
  function updateCamReadout() {
    
  }
  function applyRot() { scene.style.transform = 'rotateX(' + rotX + 'deg) rotateY(' + rotY + 'deg)'; updateCamReadout(); }
  function setScale(s) {
    baseScale = s;
    var st = document.getElementById('stage');
    st.style.transition = 'transform 0.7s cubic-bezier(0.2, 0.8, 0.2, 1)';
    st.style.transform = 'scale(' + s + ')';
    updateCamReadout();
  }
  function animateRotTo(x, y) {
    rotX = x; rotY = y;
    scene.style.transition = 'transform 0.7s cubic-bezier(0.2, 0.8, 0.2, 1)';
    applyRot();
  }

  function spreadTransform(i) {
    if (i >= 22) return MINOR_SPOT;
    // major arcana: the main fan up front
    var a = -54 + (108 / 21) * i;
    var rad = a * Math.PI / 180;
    var R = 330;
    var x = Math.sin(rad) * R;
    var z = Math.cos(rad) * R - R + 130;
    var y = 146 - i * 0.06;
    return 'translate3d(' + x + 'px,' + y + 'px,' + z + 'px) rotateX(-90deg) rotateZ(' + a + 'deg)';
  }
  // the 56 minors live as one face-down stack beside the box; only its top card is real DOM
  var MINOR_SPOT = 'translate3d(-450px,131px,-100px) rotateX(-90deg) rotateZ(-48deg)';
  var MINOR_STACK_SPOT = 'translate3d(-450px,146px,-100px) rotateX(-90deg) rotateZ(-48deg)';
  // half-pulled pose: hovering above the stack, mid-draw
  var MINOR_PULL = 'translate3d(-430px,-10px,-40px) rotateX(-64deg) rotateZ(-40deg)';
  var pullTimer = null;
  function cardElFor(i) { return i < 22 ? cards[i] : proxy; }
  function inspectTransform() {
    var p = CAM[camMode()].inspect;
    var portrait = camMode() === 'portrait';
    // cancel the camera's pitch/yaw so the card sits flat to the lens
    var rx = -p.x, ry = 180 + p.y;
    if (portrait) {
      // phone: no box/panel competing for width, so push in and lift toward centre
      return 'translate3d(-75px,-210px,260px) rotateX(' + rx + 'deg) rotateY(' + ry + 'deg) scale(1.95)';
    }
    return 'translate3d(-90px,-90px,260px) rotateX(' + rx + 'deg) rotateY(' + ry + 'deg) scale(1.25)';
  }

  function doSpread() {
    state = 'spread';
    scene.classList.add('spread');
    cards.forEach(function (el, i) { el.style.transform = spreadTransform(i); });
    document.body.classList.add('show-rebox');
    goCam('spread');
    setHint();
  }
  // fly the drawn minor back: hover over the stack, set it down, absorb into the pile top
  function returnMinor(idx) {
    proxy.style.transform = MINOR_PULL;
    pullTimer = setTimeout(function () {
      proxy.style.transform = MINOR_SPOT;
      pullTimer = setTimeout(function () {
        setStackTop(idx);
        proxy.classList.add('hidden');
      }, 480);
    }, 340);
  }
  function doInspect(i) {
    clearTimeout(pullTimer);
    var wasMinor = inspected >= 22;
    var prev = inspected;
    if (prev >= 0 && prev !== i && prev < 22) cards[prev].style.transform = spreadTransform(prev);
    if (wasMinor && i < 22) returnMinor(prev);
    inspected = i;
    var c = DECK[i];
    var el = cardElFor(i);
    if (i >= 22) {
      setProxy(i);
      if (!wasMinor) {
        // pull the top card off the stack; the next card is revealed beneath it
        proxy.classList.remove('hidden');
        proxy.style.transition = 'none';
        proxy.style.transform = MINOR_SPOT;
        void proxy.offsetWidth;
        proxy.style.transition = '';
        proxy.style.transform = MINOR_PULL;
        pullTimer = setTimeout(function () { proxy.style.transform = inspectTransform(); }, 320);
      } else {
        proxy.style.transform = inspectTransform();
      }
      setStackTop(nextMinor(i));
    } else {
      el.style.transform = inspectTransform();
    }
    cardCaption.textContent = c.num + ' · ' + c.name + ' ' + (i + 1) + ' / ' + N;
    // populate the Sacred Index panel
    var lore = LORE[c.name] || (c.trad + ' a conduit of ' + c.name.split(' of ')[1] + '. Full index entry pending transcription by the circle.');
    document.getElementById('ipNum').textContent = 'CONDUIT ' + c.num + ' · ' + (i + 1) + '/' + N;
    document.getElementById('ipName').textContent = c.name;
    document.getElementById('ipTrad').textContent = c.trad;
    document.getElementById('ipLore').innerHTML = lore.replace(/\*([^*]+)\*/g, '<i>$1</i>');
    var sin = SINS[c.name];
    document.getElementById('ipSin').innerHTML = sin ? 'ASSOCIATED SIN <b>' + sin + '</b>' : 'ASSOCIATED SIN <b>UNLOGGED</b>';
    state = 'inspect';
    document.body.classList.add('show-nav');
    goCam('inspect');
    setHint();
  }
  function endInspect() {
    clearTimeout(pullTimer);
    if (inspected >= 22) {
      returnMinor(inspected);
    } else if (inspected >= 0) {
      cardElFor(inspected).style.transform = spreadTransform(inspected);
    }
    inspected = -1;
    state = 'spread';
    document.body.classList.remove('show-nav');
    goCam('spread');
    setHint();
  }
  function rebox() {
    endInspect();
    clearTimeout(pullTimer);
    state = 'unbanded';
    document.body.classList.remove('show-rebox', 'show-nav');
    scene.classList.remove('spread');
    cards.forEach(function (el, i) {
      el.style.transform = 'translateZ(' + ((i - 10.5) * 0.85) + 'px)';
    });
    if (proxy) proxy.style.transform = 'translateZ(0px)';
    goCam('boxed');
    setTimeout(function () {
      scene.classList.remove('drawn');
      scene.classList.add('lift');
      setTimeout(function () { scene.classList.remove('lift'); }, 500);
      state = 'flapOpen';
      setTimeout(function () {
        scene.classList.remove('flap-open');
        state = 'boxed';
        // despawn the cards while boxed to keep it light
        cards.forEach(function (el) { el.remove(); });
        if (proxy) { proxy.remove(); proxy = null; }
        if (proxyTop) { proxyTop.remove(); proxyTop = null; }
        var ms = deckEl.querySelector('.minor-stack');
        if (ms) ms.remove();
        cards = [];
        cardsBuilt = false;
        setHint();
      }, 1200);
      setHint();
    }, 950);
    setHint();
  }

  /* ===== DUST BURST =====
     Motes disturbed off the film. Screen-space so they drift on their own
     axis rather than riding the 3D camera — reads as air, not geometry. */
  var dustField = document.getElementById('dustField');
  function burstDust(count, originX, originY, spread) {
    if (!dustField) return;
    var frag = document.createDocumentFragment();
    for (var i = 0; i < count; i++) {
      var m = document.createElement('div');
      m.className = 'mote' + (Math.random() < 0.28 ? ' lit' : '');
      var size = 0.8 + Math.random() * 2.9;       // fine grit through to flecks
      m.style.width = size + 'px';
      m.style.height = size + 'px';
      var sx = originX + (Math.random() - 0.5) * spread;
      var sy = originY + (Math.random() - 0.5) * spread * 1.25;
      var driftX = (Math.random() - 0.5) * 260;
      var rise = -(30 + Math.random() * 130);     // outward puff
      var fall = 90 + Math.random() * 260;        // then the lazy settle
      var dur = 2600 + Math.random() * 3400;
      var delay = Math.random() * 340;
      m.style.transform = 'translate3d(' + sx + 'px,' + sy + 'px,0)';
      frag.appendChild(m);
      (function (el, sx, sy, driftX, rise, fall, dur, delay) {
        setTimeout(function () {
          el.style.transition = 'transform ' + dur + 'ms cubic-bezier(0.15,0.5,0.35,1), opacity ' + dur + 'ms ease-out';
          el.style.opacity = 0.16 + Math.random() * 0.6;
          el.style.transform = 'translate3d(' + (sx + driftX * 0.4) + 'px,' + (sy + rise) + 'px,0)';
          setTimeout(function () {
            el.style.transition = 'transform ' + dur + 'ms linear, opacity ' + (dur * 0.8) + 'ms ease-in';
            el.style.opacity = 0;
            el.style.transform = 'translate3d(' + (sx + driftX) + 'px,' + (sy + rise + fall) + 'px,0)';
          }, dur * 0.34);
          setTimeout(function () { el.remove(); }, dur * 1.6);
        }, delay);
      })(m, sx, sy, driftX, rise, fall, dur, delay);
    }
    dustField.appendChild(frag);
  }
  function boxScreenCentre() {
    var r = box && box.getBoundingClientRect ? box.getBoundingClientRect() : null;
    if (r && r.width) return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    return { x: window.innerWidth / 2, y: window.innerHeight / 2 };
  }

  wrap.addEventListener('click', function (e) {
    e.stopPropagation();
    if (state !== 'wrapped') return;
    scene.classList.add('wrap-off');
    // the seal breaks — years of shelf dust lifts off the film in three waves
    var dc = boxScreenCentre();
    burstDust(46, dc.x, dc.y, 190);
    setTimeout(function () { burstDust(26, dc.x, dc.y - 40, 240); }, 220);
    setTimeout(function () { burstDust(14, dc.x, dc.y - 90, 300); }, 560);
    setTimeout(function () { wrap.style.display = 'none'; }, 950);
    state = 'boxed';
    setHint();
  });
  function drawDeck() {
    buildCards();
    goCam('drawn');
    scene.classList.add('lift');
    setTimeout(function () {
      scene.classList.remove('lift');
      scene.classList.add('drawn');
    }, 480);
    state = 'drawn';
    setHint();
  }
  flap.addEventListener('click', function (e) {
    e.stopPropagation();
    if (state === 'boxed') {
      scene.classList.add('flap-open');
      state = 'flapOpen';
      setHint();
    } else if (state === 'flapOpen') {
      drawDeck();
    }
  });
  box.addEventListener('click', function (e) {
    e.stopPropagation();
    if (state === 'boxed') { flap.click(); return; }
    if (state === 'flapOpen') {
      drawDeck();
    } else if (state === 'spread') {
      rebox();
    }
  });
  band.addEventListener('click', function (e) {
    e.stopPropagation();
    if (state !== 'drawn') return;
    scene.classList.add('band-off');
    setTimeout(function () { band.style.display = 'none'; }, 900);
    state = 'unbanded';
    setHint();
  });
  deckEl.addEventListener('click', function (e) {
    if (state === 'unbanded') {
      e.stopPropagation();
      doSpread();
      return;
    }
    if (state === 'drawn') {
      // clicking the stack (not the band) also tears the band first
      e.stopPropagation();
      scene.classList.add('band-off');
      setTimeout(function () { band.style.display = 'none'; }, 900);
      state = 'unbanded';
      setHint();
      return;
    }
    var card = e.target.closest('.card');
    if (!card) return;
    e.stopPropagation();
    var i = +card.dataset.i;
    if (state === 'spread') doInspect(i);
    else if (state === 'inspect') {
      if (i === inspected) endInspect();
      else doInspect(i);
    }
  });
  document.getElementById('btnRebox').addEventListener('click', function (e) { e.stopPropagation(); rebox(); });
  document.getElementById('btnPrev').addEventListener('click', function (e) { e.stopPropagation(); if (inspected >= 0) doInspect((inspected + N - 1) % N); });
  document.getElementById('btnNext').addEventListener('click', function (e) { e.stopPropagation(); if (inspected >= 0) doInspect((inspected + 1) % N); });
  document.addEventListener('keydown', function (e) {
    if (state !== 'inspect') return;
    if (e.key === 'ArrowLeft') doInspect((inspected + N - 1) % N);
    else if (e.key === 'ArrowRight') doInspect((inspected + 1) % N);
    else if (e.key === 'Escape') endInspect();
  });

  setHint();
  updateCamReadout();
  

  // drag to rotate + pinch zoom (same feel as music.index)
  var dragging = false, lastX = 0, lastY = 0, moved = 0;
  var baseScale = 1.25, pinchStart = 0, pinchBaseScale = 1.25;
  var stage = document.getElementById('stage');
  function applyScale() { stage.style.transition = 'none'; stage.style.transform = 'scale(' + baseScale + ')'; updateCamReadout(); }
  document.addEventListener('mousedown', function (e) {
    if (e.target.closest('.btn')) return;
    dragging = true; moved = 0; lastX = e.clientX; lastY = e.clientY;
    scene.style.transition = 'none';
  });
  document.addEventListener('mousemove', function (e) {
    if (!dragging) return;
    moved += Math.abs(e.clientX - lastX) + Math.abs(e.clientY - lastY);
    rotY += (e.clientX - lastX) * 0.4;
    rotX -= (e.clientY - lastY) * 0.4;
    rotX = Math.max(-80, Math.min(80, rotX));
    lastX = e.clientX; lastY = e.clientY;
    applyRot();
  });
  document.addEventListener('mouseup', function () {
    dragging = false;
    scene.style.transition = 'transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1)';
    if (state === 'inspect') goCam('inspect');
  });
  // suppress clicks that were actually drags
  document.addEventListener('click', function (e) {
    if (moved > 8) { e.stopPropagation(); moved = 0; }
  }, true);
  document.addEventListener('wheel', function (e) {
    baseScale = Math.max(0.5, Math.min(3.2, baseScale - e.deltaY * 0.0012));
    applyScale();
  }, { passive: true });
  document.addEventListener('touchstart', function (e) {
    if (e.touches.length === 2) {
      pinchStart = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
      pinchBaseScale = baseScale;
      dragging = false;
    } else if (e.touches.length === 1) {
      dragging = true; moved = 0; lastX = e.touches[0].clientX; lastY = e.touches[0].clientY;
      scene.style.transition = 'none';
    }
  }, { passive: false });
  document.addEventListener('touchmove', function (e) {
    if (e.touches.length === 2 && pinchStart) {
      e.preventDefault();
      var d = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
      baseScale = Math.max(0.5, Math.min(3.2, pinchBaseScale * d / pinchStart));
      applyScale();
    } else if (dragging && e.touches.length === 1) {
      e.preventDefault();
      moved += Math.abs(e.touches[0].clientX - lastX) + Math.abs(e.touches[0].clientY - lastY);
      rotY += (e.touches[0].clientX - lastX) * 0.4;
      rotX -= (e.touches[0].clientY - lastY) * 0.4;
      rotX = Math.max(-80, Math.min(80, rotX));
      lastX = e.touches[0].clientX; lastY = e.touches[0].clientY;
      applyRot();
    }
  }, { passive: false });
  document.addEventListener('touchend', function (e) {
    if (e.touches.length < 2) pinchStart = 0;
    if (e.touches.length === 0) {
      dragging = false;
      scene.style.transition = 'transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1)';
      if (state === 'inspect') goCam('inspect');
    }
  });

  // portrait: dock the Sacred Index panel to the bottom of the screen
  // (fixed positioning can't escape the scene's transform, so the node moves)
  var infoPanelEl = document.getElementById('infoPanel');
  var infoPanelHome = infoPanelEl.parentNode;
  function placeInfoPanel() {
    if (camMode() === 'portrait') {
      if (infoPanelEl.parentNode !== document.body) document.body.appendChild(infoPanelEl);
      infoPanelEl.classList.add('sheet');
    } else {
      if (infoPanelEl.parentNode !== infoPanelHome) infoPanelHome.appendChild(infoPanelEl);
      infoPanelEl.classList.remove('sheet');
    }
  }


  // initial framing for whichever orientation we loaded in
  goCam(state);
  placeInfoPanel();
  var camResizeTimer = null;
  window.addEventListener('resize', function () {
    clearTimeout(camResizeTimer);
    camResizeTimer = setTimeout(function () { goCam(state); placeInfoPanel(); }, 150);
  });
