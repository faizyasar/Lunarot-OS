/* @ds-bundle: {"format":4,"namespace":"LunarotDesignSystem_03ee3e","components":[{"name":"TarotCard","sourcePath":"components/cards/TarotCard.jsx"},{"name":"Button","sourcePath":"components/core/Button.jsx"},{"name":"Panel","sourcePath":"components/core/Panel.jsx"},{"name":"HoverText","sourcePath":"components/effects/HoverText.jsx"},{"name":"Typewriter","sourcePath":"components/effects/Typewriter.jsx"},{"name":"Input","sourcePath":"components/forms/Input.jsx"},{"name":"NavButton","sourcePath":"components/navigation/NavButton.jsx"}],"sourceHashes":{"components/cards/TarotCard.jsx":"b7908bc36474","components/core/Button.jsx":"fd7af45c45ff","components/core/Panel.jsx":"05aec846a98e","components/effects/HoverText.jsx":"cf6f4f65b410","components/effects/Typewriter.jsx":"13ccd12e98c3","components/forms/Input.jsx":"755cf5a653cb","components/navigation/NavButton.jsx":"c31b0530ebe5","ui_kits/lunarot-baseball/BaseballScreen.jsx":"534ff75b32f1","ui_kits/sacred-draw/LogonScreen.jsx":"6a35591bcaac","ui_kits/sacred-draw/MainScreen.jsx":"c183b1a96907","ui_kits/sacred-draw/deck.js":"ea828615b5a2","ui_kits/sefirot-codex/SefirotScreen.jsx":"1ad7f16ce849","ui_kits/sefirot-codex/sefirot-data.js":"04750e5a9fc2","ui_kits/sigil-generator/check.js":"b19dbd72c89d"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.LunarotDesignSystem_03ee3e = window.LunarotDesignSystem_03ee3e || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/cards/TarotCard.jsx
try { (() => {
const SVG_BACK = /*#__PURE__*/React.createElement("svg", {
  viewBox: "0 0 200 200",
  style: {
    position: 'absolute',
    width: '90%',
    height: '90%',
    opacity: 0.5
  }
}, /*#__PURE__*/React.createElement("circle", {
  cx: "100",
  cy: "100",
  r: "85",
  fill: "none",
  stroke: "#fff",
  strokeWidth: "0.6",
  strokeDasharray: "3 3"
}), /*#__PURE__*/React.createElement("circle", {
  cx: "100",
  cy: "100",
  r: "75",
  fill: "none",
  stroke: "#fff",
  strokeWidth: "0.4"
}), /*#__PURE__*/React.createElement("circle", {
  cx: "100",
  cy: "100",
  r: "50",
  fill: "none",
  stroke: "#fff",
  strokeWidth: "0.8"
}), /*#__PURE__*/React.createElement("circle", {
  cx: "100",
  cy: "100",
  r: "30",
  fill: "none",
  stroke: "#fff",
  strokeWidth: "0.5"
}), /*#__PURE__*/React.createElement("circle", {
  cx: "100",
  cy: "100",
  r: "15",
  fill: "none",
  stroke: "#fff",
  strokeWidth: "1"
}), /*#__PURE__*/React.createElement("line", {
  x1: "100",
  y1: "10",
  x2: "100",
  y2: "190",
  stroke: "#fff",
  strokeWidth: "0.4",
  strokeDasharray: "2 4"
}), /*#__PURE__*/React.createElement("line", {
  x1: "10",
  y1: "100",
  x2: "190",
  y2: "100",
  stroke: "#fff",
  strokeWidth: "0.4",
  strokeDasharray: "2 4"
}));
function TarotCard({
  card,
  flipped = false,
  reversed = false,
  broken = false,
  onClick,
  width = 148,
  height = 258
}) {
  const transform = flipped ? reversed ? 'rotateY(180deg) rotateZ(180deg)' : 'rotateY(180deg)' : 'rotateY(0deg)';
  return /*#__PURE__*/React.createElement("div", {
    style: {
      perspective: 1200
    }
  }, /*#__PURE__*/React.createElement("div", {
    onClick: onClick,
    style: {
      width,
      height,
      position: 'relative',
      transformStyle: 'preserve-3d',
      cursor: 'pointer',
      transition: 'transform 1.1s cubic-bezier(.23,1,.32,1)',
      transform
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'absolute',
      inset: 0,
      borderRadius: 'var(--radius-card)',
      backfaceVisibility: 'hidden',
      background: 'rgb(4 4 4 / 0.18)',
      backdropFilter: 'blur(2px)',
      border: '1px solid var(--surface-40)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      overflow: 'hidden',
      boxShadow: '0 0 15px var(--surface-08)'
    }
  }, SVG_BACK, /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'absolute',
      inset: 6,
      border: '1px solid var(--surface-15)',
      borderRadius: 5
    }
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'absolute',
      inset: 0,
      borderRadius: 'var(--radius-card)',
      backfaceVisibility: 'hidden',
      transform: 'rotateY(-180deg)',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '15px 11px',
      color: 'var(--bone)',
      background: broken ? 'linear-gradient(170deg, #181818, #000000)' : 'rgb(6 6 6 / 0.45)',
      backdropFilter: 'blur(3px)',
      border: broken ? '1px solid var(--surface)' : '1px solid var(--bone)',
      boxShadow: broken ? '0 0 25px var(--surface-40)' : '0 0 20px var(--surface-08)'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'absolute',
      inset: 5,
      border: '1px solid var(--surface-25)',
      borderRadius: 5,
      pointerEvents: 'none'
    }
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: 10,
      letterSpacing: 'var(--tracking-wide)',
      animation: broken ? 'lunarot-jitter 0.22s infinite' : 'none',
      textShadow: broken ? '1.5px 0 0 #00f, -1.5px 0 0 #f00' : 'none'
    }
  }, card.num), /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 28,
      animation: broken ? 'lunarot-jitter 0.22s infinite' : 'none'
    }
  }, card.glyph), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: 12,
      textAlign: 'center',
      letterSpacing: 'var(--tracking-normal)',
      animation: broken ? 'lunarot-jitter 0.22s infinite' : 'none',
      textShadow: broken ? '1.5px 0 0 #00f, -1.5px 0 0 #f00' : 'none'
    }
  }, card.name))));
}
Object.assign(__ds_scope, { TarotCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/cards/TarotCard.jsx", error: String((e && e.message) || e) }); }

// components/core/Button.jsx
try { (() => {
function Button({
  variant = 'primary',
  full = false,
  disabled = false,
  glyph = '◆',
  children,
  onClick,
  style
}) {
  const [punching, setPunching] = React.useState(false);
  const base = {
    padding: '10px 24px',
    fontFamily: 'var(--font-system)',
    fontSize: 9,
    fontWeight: 'bold',
    textTransform: 'uppercase',
    letterSpacing: 'var(--tracking-wide)',
    borderRadius: 'var(--radius-none)',
    cursor: disabled ? 'default' : 'pointer',
    transition: `background-color var(--dur-quick) var(--ease-theatrical), color var(--dur-quick) var(--ease-theatrical), border-color var(--dur-quick) var(--ease-theatrical), box-shadow var(--dur-quick) var(--ease-theatrical)`,
    display: 'inline-block',
    width: full ? '100%' : 'auto',
    textAlign: full ? 'center' : 'left',
    opacity: disabled ? 0.35 : 1,
    pointerEvents: disabled ? 'none' : 'auto',
    animation: punching ? 'lunarot-tab-punch var(--dur-curtain) var(--ease-theatrical)' : 'none'
  };
  const variants = {
    primary: {
      border: '1px solid var(--surface)',
      backgroundColor: 'var(--surface)',
      color: 'var(--ink)'
    },
    secondary: {
      border: '1px solid var(--surface-40)',
      backgroundColor: 'var(--ink-60)',
      color: 'var(--surface-80)'
    },
    ghost: {
      border: '1px solid var(--surface-15)',
      backgroundColor: 'transparent',
      color: 'var(--surface-60)'
    }
  };
  const hovers = {
    primary: {
      backgroundColor: 'var(--ink)',
      color: 'var(--surface)',
      borderColor: 'var(--surface)',
      boxShadow: 'var(--glow-surface)'
    },
    secondary: {
      color: 'var(--surface)',
      borderColor: 'var(--surface)',
      boxShadow: 'var(--glow-surface)'
    },
    ghost: {
      color: 'var(--surface)',
      borderColor: 'var(--surface-40)'
    }
  };
  const [hover, setHover] = React.useState(false);
  return /*#__PURE__*/React.createElement("button", {
    onClick: e => {
      setPunching(true);
      onClick && onClick(e);
    },
    onAnimationEnd: () => setPunching(false),
    disabled: disabled,
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
      ...base,
      ...variants[variant],
      ...(hover && !disabled ? hovers[variant] : {}),
      ...style
    }
  }, glyph ? `${glyph} ` : '', children);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Button.jsx", error: String((e && e.message) || e) }); }

// components/core/Panel.jsx
try { (() => {
function Panel({
  variant = 'gold',
  tag,
  footerTag,
  children,
  style
}) {
  const border = variant === 'gold' ? 'var(--surface-40)' : 'var(--bone)';
  const insetBorder = variant === 'gold' ? 'var(--surface-15)' : 'rgb(239 237 232 / 0.15)';
  return /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'relative',
      padding: 'var(--space-6)',
      backgroundColor: 'var(--bg-panel)',
      backdropFilter: 'var(--blur-panel)',
      WebkitBackdropFilter: 'var(--blur-panel)',
      border: `1px solid ${border}`,
      boxShadow: '0 0 15px var(--surface-08)',
      width: '100%',
      animation: 'lunarot-snap-in var(--dur-curtain) var(--ease-theatrical)',
      ...style
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'absolute',
      inset: 6,
      border: `1px dashed ${insetBorder}`,
      pointerEvents: 'none'
    }
  }), tag ? /*#__PURE__*/React.createElement("span", {
    style: {
      position: 'absolute',
      top: 8,
      left: 12,
      fontFamily: 'var(--font-system)',
      fontSize: 7,
      color: 'var(--surface-25)',
      letterSpacing: 'var(--tracking-widest)',
      textTransform: 'uppercase'
    }
  }, tag) : null, footerTag ? /*#__PURE__*/React.createElement("span", {
    style: {
      position: 'absolute',
      bottom: 8,
      right: 12,
      fontFamily: 'var(--font-system)',
      fontSize: 6,
      color: 'var(--surface-25)',
      letterSpacing: 'var(--tracking-wider)',
      textTransform: 'uppercase'
    }
  }, footerTag) : null, children);
}
Object.assign(__ds_scope, { Panel });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Panel.jsx", error: String((e && e.message) || e) }); }

// components/effects/HoverText.jsx
try { (() => {
function HoverText({
  text,
  style
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-body)',
      ...style
    }
  }, text.split('').map((char, i) => /*#__PURE__*/React.createElement("span", {
    key: i,
    style: {
      display: 'inline-block',
      transition: 'all 0.3s cubic-bezier(0.25,1,0.5,1.1)',
      cursor: 'default'
    },
    onMouseEnter: e => {
      e.currentTarget.style.transform = 'scale(1.35) translateY(-6px) rotate(6deg)';
      e.currentTarget.style.color = 'var(--surface)';
      e.currentTarget.style.textShadow = '0 0 8px var(--surface)';
    },
    onMouseLeave: e => {
      e.currentTarget.style.transform = 'none';
      e.currentTarget.style.color = '';
      e.currentTarget.style.textShadow = 'none';
    }
  }, char === ' ' ? '\u00A0' : char)));
}
Object.assign(__ds_scope, { HoverText });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/effects/HoverText.jsx", error: String((e && e.message) || e) }); }

// components/effects/Typewriter.jsx
try { (() => {
const {
  useEffect,
  useRef
} = React;
const ARABIC = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي';
const randArabic = () => ARABIC[Math.floor(Math.random() * ARABIC.length)];
const delay = ms => new Promise(r => setTimeout(r, ms));
function Typewriter({
  text,
  chargedList = [],
  style
}) {
  const ref = useRef(null);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const session = Math.random().toString();
    el.setAttribute('data-session', session);
    let rendered = '';
    const words = text.split(' ');
    (async () => {
      for (const word of words) {
        if (el.getAttribute('data-session') !== session) return;
        const isAsterisk = word.startsWith('*') && word.endsWith('*');
        const clean = word.replace(/\*/g, '');
        const cleanLower = clean.toLowerCase().replace(/[^a-z-]/g, '');
        const charged = isAsterisk || chargedList.some(w => w.toLowerCase() === cleanLower);
        if (charged) {
          el.innerHTML = rendered + '<span class="lunarot-etch-cursor">▌</span>';
          await delay(150);
          for (let f = 0; f < 6; f++) {
            const ghost = clean.split('').map(c => c.match(/[a-zA-Z]/) ? randArabic() : c).join('');
            el.innerHTML = rendered + `<span class="lunarot-etch-ghost">${ghost}</span><span class="lunarot-etch-cursor">▌</span>`;
            await delay(35);
          }
          rendered += `<span class="lunarot-etch-word">${clean}</span> `;
        } else {
          rendered += clean + ' ';
          el.innerHTML = rendered + '<span class="lunarot-etch-cursor">▌</span>';
          await delay(clean.match(/[.!?]$/) ? 350 : 16);
        }
        el.innerHTML = rendered + '<span class="lunarot-etch-cursor">▌</span>';
      }
      if (el.getAttribute('data-session') === session) el.innerHTML = rendered.trim();
    })();
  }, [text]);
  return /*#__PURE__*/React.createElement("div", {
    ref: ref,
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: 13,
      lineHeight: 1.6,
      color: 'var(--text-body)',
      ...style
    }
  });
}
Object.assign(__ds_scope, { Typewriter });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/effects/Typewriter.jsx", error: String((e && e.message) || e) }); }

// components/forms/Input.jsx
try { (() => {
function Input({
  label,
  type = 'text',
  value,
  defaultValue,
  onChange,
  placeholder,
  options,
  width
}) {
  const fieldStyle = {
    background: type === 'select' ? 'var(--ink)' : 'none',
    border: type === 'select' ? '1px solid var(--surface-15)' : 'none',
    textAlign: type === 'select' ? 'left' : 'right',
    fontFamily: 'var(--font-system)',
    fontSize: 8.5,
    color: 'var(--surface)',
    outline: 'none',
    textTransform: 'uppercase',
    letterSpacing: 'var(--tracking-normal)',
    padding: type === 'select' ? '2px 4px' : 0,
    width: width || (type === 'date' ? 110 : type === 'time' ? 80 : 160)
  };
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 4,
      width: '100%',
      fontFamily: 'var(--font-system)',
      fontSize: 8,
      letterSpacing: 'var(--tracking-normal)'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '8px 0',
      borderBottom: '1px solid var(--surface-08)'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      color: 'var(--surface-40)',
      fontWeight: 'bold',
      fontSize: 7,
      textTransform: 'uppercase'
    }
  }, label), type === 'select' ? /*#__PURE__*/React.createElement("select", {
    style: fieldStyle,
    value: value,
    onChange: onChange
  }, (options || []).map(o => /*#__PURE__*/React.createElement("option", {
    key: o.value,
    value: o.value
  }, o.label))) : /*#__PURE__*/React.createElement("input", {
    type: type,
    style: fieldStyle,
    value: value,
    defaultValue: defaultValue,
    onChange: onChange,
    placeholder: placeholder
  })));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Input.jsx", error: String((e && e.message) || e) }); }

// components/navigation/NavButton.jsx
try { (() => {
function NavButton({
  active,
  children,
  onClick
}) {
  const [punching, setPunching] = React.useState(false);
  const style = active === 'primary' ? {
    backgroundColor: 'var(--surface)',
    borderColor: 'var(--surface)',
    color: 'var(--ink)',
    boxShadow: '0 0 10px var(--surface-25)'
  } : active === 'secondary' ? {
    backgroundColor: 'var(--ink-60)',
    borderColor: 'var(--surface-40)',
    color: 'var(--surface-40)',
    boxShadow: '0 0 10px var(--surface-15)'
  } : {
    backgroundColor: 'transparent',
    borderColor: 'var(--surface-15)',
    color: 'var(--surface-40)'
  };
  const handleClick = e => {
    setPunching(true);
    onClick && onClick(e);
  };
  return /*#__PURE__*/React.createElement("button", {
    onClick: handleClick,
    onAnimationEnd: () => setPunching(false),
    style: {
      background: 'none',
      border: '1px solid var(--surface-15)',
      padding: '4px 12px',
      fontFamily: 'var(--font-system)',
      fontSize: 8,
      fontWeight: 'bold',
      letterSpacing: 'var(--tracking-wider)',
      cursor: 'pointer',
      transition: `background-color var(--dur-quick) var(--ease-theatrical), color var(--dur-quick) var(--ease-theatrical), border-color var(--dur-quick) var(--ease-theatrical), box-shadow var(--dur-quick) var(--ease-theatrical)`,
      textTransform: 'uppercase',
      animation: punching ? 'lunarot-tab-punch var(--dur-curtain) var(--ease-theatrical)' : 'none',
      ...style
    }
  }, children);
}
Object.assign(__ds_scope, { NavButton });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/navigation/NavButton.jsx", error: String((e && e.message) || e) }); }

// ui_kits/lunarot-baseball/BaseballScreen.jsx
try { (() => {
function BaseballScreen() {
  const {
    Panel,
    Button,
    Typewriter
  } = window.LunarotDesignSystem_03ee3e;
  const [score, setScore] = React.useState({
    visitor: 0,
    home: 0
  });
  const [count, setCount] = React.useState({
    balls: 0,
    strikes: 0,
    outs: 0
  });
  const [inning, setInning] = React.useState({
    n: 1,
    top: true
  });
  const [message, setMessage] = React.useState('CHOOSE YOUR PITCH...');
  const [pitching, setPitching] = React.useState(false);
  const [ballPos, setBallPos] = React.useState(null);
  const [aim, setAim] = React.useState(null);
  const pitch = (r, c) => {
    if (pitching) return;
    setPitching(true);
    setAim({
      r,
      c
    });
    setBallPos({
      x: 8,
      y: 70
    });
    setMessage('PITCHING...');
    setTimeout(() => setBallPos({
      x: 50 + (c - 1) * 12,
      y: 20 + (r - 1) * 10
    }), 50);
    setTimeout(() => {
      const outcomes = ['strike', 'ball', 'contact'];
      const outcome = outcomes[Math.floor(Math.random() * 3)];
      if (outcome === 'strike') {
        setCount(cnt => {
          const s = cnt.strikes + 1;
          if (s >= 3) {
            setMessage('STRIKEOUT-!');
            return {
              balls: 0,
              strikes: 0,
              outs: cnt.outs + 1
            };
          }
          setMessage('STRIKE-!');
          return {
            ...cnt,
            strikes: s
          };
        });
      } else if (outcome === 'ball') {
        setCount(cnt => {
          const b = cnt.balls + 1;
          if (b >= 4) {
            setMessage('WALK...');
            return {
              balls: 0,
              strikes: 0,
              outs: cnt.outs
            };
          }
          setMessage('BALL-!');
          return {
            ...cnt,
            balls: b
          };
        });
      } else {
        setMessage('CRACK-! CONTACT!');
        if (Math.random() < 0.3) setScore(s => ({
          ...s,
          home: s.home + 1
        }));
      }
      setPitching(false);
      setBallPos(null);
      setAim(null);
    }, 900);
  };
  return /*#__PURE__*/React.createElement("div", {
    style: {
      width: '100%',
      height: '100%',
      display: 'flex',
      flexDirection: 'column',
      background: '#000'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: '10px 24px',
      borderBottom: '1px solid var(--surface-15)',
      fontFamily: 'var(--font-system)',
      fontSize: 9,
      color: 'var(--surface-40)',
      letterSpacing: '0.15em',
      textTransform: 'uppercase'
    }
  }, /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("span", {
    style: {
      color: 'var(--surface)'
    }
  }, "\u25C7"), " LUNAROT OS"), /*#__PURE__*/React.createElement("span", {
    style: {
      background: 'var(--surface)',
      color: 'var(--ink)',
      padding: '3px 10px',
      fontWeight: 'bold'
    }
  }, "\u25C6 LUNAROT BASEBALL"), /*#__PURE__*/React.createElement("span", null, "ASTRAL_SHELL_OK")), /*#__PURE__*/React.createElement("div", {
    style: {
      flex: 1,
      display: 'flex',
      gap: 20,
      padding: 24
    }
  }, /*#__PURE__*/React.createElement(Panel, {
    variant: "white",
    tag: "SCOREBOARD",
    style: {
      width: 220,
      flexShrink: 0
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-system)',
      color: 'var(--surface-80)',
      fontSize: 11
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      justifyContent: 'space-between',
      marginBottom: 8
    }
  }, /*#__PURE__*/React.createElement("span", null, inning.top ? '▲' : '▼', " ", inning.n, " INN"), /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 20,
      fontWeight: 'bold'
    }
  }, score.visitor, " | ", score.home)), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 4,
      fontSize: 9,
      color: 'var(--surface-40)'
    }
  }, /*#__PURE__*/React.createElement("div", null, "B ", '●'.repeat(count.balls), '○'.repeat(3 - count.balls)), /*#__PURE__*/React.createElement("div", null, "S ", '●'.repeat(count.strikes), '○'.repeat(2 - count.strikes)), /*#__PURE__*/React.createElement("div", null, "O ", '●'.repeat(count.outs), '○'.repeat(2 - count.outs))))), /*#__PURE__*/React.createElement("div", {
    style: {
      flex: 1,
      position: 'relative',
      border: '1px solid var(--surface-15)',
      background: '#050507'
    }
  }, /*#__PURE__*/React.createElement("svg", {
    viewBox: "0 0 100 100",
    style: {
      width: '100%',
      height: '100%'
    }
  }, /*#__PURE__*/React.createElement("polygon", {
    points: "50,20 25,70 75,70",
    fill: "none",
    stroke: "var(--surface-25)",
    strokeWidth: "0.5"
  }), /*#__PURE__*/React.createElement("rect", {
    x: "46",
    y: "66",
    width: "8",
    height: "6",
    fill: "none",
    stroke: "var(--bone)",
    strokeWidth: "0.5"
  }), /*#__PURE__*/React.createElement("circle", {
    cx: "50",
    cy: "35",
    r: "4",
    fill: "none",
    stroke: "var(--bone)",
    strokeWidth: "0.5"
  }), ballPos && /*#__PURE__*/React.createElement("circle", {
    cx: ballPos.x,
    cy: ballPos.y,
    r: "1.5",
    fill: "var(--surface)"
  })), pitching && /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'absolute',
      top: 8,
      left: '50%',
      transform: 'translateX(-50%)',
      fontFamily: 'var(--font-system)',
      fontSize: 9,
      color: 'var(--surface-60)',
      letterSpacing: '0.2em'
    }
  }, "\u25C6 PITCH IN FLIGHT \u25C6")), /*#__PURE__*/React.createElement("div", {
    style: {
      width: 160,
      flexShrink: 0,
      display: 'flex',
      flexDirection: 'column',
      gap: 8
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-system)',
      fontSize: 8,
      color: 'var(--surface-40)',
      letterSpacing: '0.15em',
      textAlign: 'center'
    }
  }, "\u25C6 ACTUATOR GRID \u25C6"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: 'repeat(3,1fr)',
      gap: 6,
      border: '1px solid var(--surface-15)',
      padding: 8
    }
  }, [0, 1, 2].map(r => [0, 1, 2].map(c => /*#__PURE__*/React.createElement("button", {
    key: `${r}-${c}`,
    disabled: pitching,
    onClick: () => pitch(r, c),
    style: {
      aspectRatio: '1',
      border: aim && aim.r === r && aim.c === c ? '1px solid var(--surface)' : '1px solid var(--surface-15)',
      background: aim && aim.r === r && aim.c === c ? 'var(--surface-15)' : 'transparent',
      color: 'var(--surface-25)',
      cursor: pitching ? 'default' : 'pointer'
    }
  }, "+")))))), /*#__PURE__*/React.createElement(Panel, {
    variant: "gold",
    style: {
      margin: '0 24px 24px',
      width: 'auto'
    }
  }, /*#__PURE__*/React.createElement(Typewriter, {
    key: message,
    text: `SYS> ${message}`
  })));
}
window.BaseballScreen = BaseballScreen;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/lunarot-baseball/BaseballScreen.jsx", error: String((e && e.message) || e) }); }

// ui_kits/sacred-draw/LogonScreen.jsx
try { (() => {
function LogonScreen({
  onBoot
}) {
  const {
    Button,
    Input
  } = window.LunarotDesignSystem_03ee3e;
  const [stage, setStage] = React.useState('intake');
  const [tokenId, setTokenId] = React.useState('COGNITION_VESSEL');
  const [epoch, setEpoch] = React.useState('1999-08-11');
  const [axis, setAxis] = React.useState('12:12');
  const [progress, setProgress] = React.useState(0);
  const [logs, setLogs] = React.useState([]);
  const BOOT_LOGS = [{
    prg: 15,
    log: '◆ [0xCC0110] BIND SECURE PORTS TO HOST 0.0.0.0... [OK]'
  }, {
    prg: 35,
    log: '✦ [0x8FA12B] SYNCHRONIZING METEORIC DRIFT TO SOLAR CORRIDORS... [OK]'
  }, {
    prg: 55,
    log: '⚠ [0x77BE1D] DETECTED PLANETARY INTERFERENCE DRIFT...'
  }, {
    prg: 60,
    log: '✦ RETRYING CONDUIT CONNECTION (Attempt 1/2)... [OK]'
  }, {
    prg: 80,
    log: '◆ [0xEE334A] INJECTING REGISTRY COOKIES UNSEALED... [OK]'
  }, {
    prg: 100,
    log: '✦ [0xAA99E1] SECURE NATAL DESCENT HANDSHAKE COMPLETE'
  }];
  const execute = () => {
    setStage('boot');
    setProgress(0);
    setLogs([]);
    let p = 0,
      idx = 0;
    const tick = () => {
      p = Math.min(100, p + 6 + Math.random() * 8);
      while (idx < BOOT_LOGS.length && p >= BOOT_LOGS[idx].prg) {
        const logText = BOOT_LOGS[idx].log;
        setLogs(l => [...l, logText]);
        idx++;
      }
      setProgress(Math.round(p));
      if (p < 100) setTimeout(tick, 140);else setTimeout(() => onBoot({
        name: tokenId,
        sun: 'Leo',
        moon: 'Pisces'
      }), 700);
    };
    tick();
  };
  const blocks = Math.floor(progress / 4);
  return /*#__PURE__*/React.createElement("div", {
    style: {
      width: '100%',
      height: '100%',
      display: 'flex',
      background: '#000'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      flex: '0 0 46%',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      borderRight: '1px solid var(--surface-15)'
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/lunarot_logo.webp",
    alt: "Lunarot",
    style: {
      width: '80%',
      opacity: 0.9
    }
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      flex: 1,
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      padding: '0 60px',
      gap: 24
    }
  }, stage === 'intake' ? /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(Input, {
    label: "TOKEN ID",
    type: "text",
    value: tokenId,
    onChange: e => setTokenId(e.target.value)
  }), /*#__PURE__*/React.createElement(Input, {
    label: "SOLAR EPOCH",
    type: "date",
    value: epoch,
    onChange: e => setEpoch(e.target.value)
  }), /*#__PURE__*/React.createElement(Input, {
    label: "TEMP AXIS",
    type: "time",
    value: axis,
    onChange: e => setAxis(e.target.value)
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 12
    }
  }, /*#__PURE__*/React.createElement(Button, {
    variant: "primary",
    onClick: execute
  }, "EXECUTE SYSTEM LINK"))) : /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-system)'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      justifyContent: 'space-between',
      borderBottom: '1px solid var(--surface-15)',
      paddingBottom: 8,
      marginBottom: 16,
      fontSize: 10,
      color: 'var(--surface)'
    }
  }, /*#__PURE__*/React.createElement("span", null, "[ LUNAROT ENGINE OS v5.18 ]"), /*#__PURE__*/React.createElement("span", {
    style: {
      color: 'var(--surface-40)'
    }
  }, "RE-LINKING CONDUIT")), /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 100,
      fontSize: 8,
      color: 'var(--surface-60)',
      lineHeight: 1.9
    }
  }, logs.map((l, i) => /*#__PURE__*/React.createElement("div", {
    key: i
  }, l))), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      justifyContent: 'space-between',
      fontSize: 7,
      color: 'var(--surface-40)',
      marginTop: 20
    }
  }, /*#__PURE__*/React.createElement("span", null, "INITIALIZING CHANNELS"), /*#__PURE__*/React.createElement("span", null, progress, "%")), /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 9,
      color: 'var(--surface-80)',
      marginTop: 4
    }
  }, "[", '█'.repeat(blocks), '░'.repeat(25 - blocks), "]")), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-system)',
      fontSize: 8,
      color: 'var(--surface-25)',
      letterSpacing: '0.12em',
      marginTop: 40
    }
  }, "(c) 2026 lunarotdeka")));
}
window.LogonScreen = LogonScreen;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/sacred-draw/LogonScreen.jsx", error: String((e && e.message) || e) }); }

// ui_kits/sacred-draw/MainScreen.jsx
try { (() => {
function MainScreen({
  user,
  onReset
}) {
  const {
    TarotCard,
    Button,
    Typewriter,
    Panel
  } = window.LunarotDesignSystem_03ee3e;
  const [cards] = React.useState(() => window.LunarotDeck.drawThree());
  const [flipped, setFlipped] = React.useState([false, false, false]);
  const allFlipped = flipped.every(Boolean);
  const POSITIONS = ['I: ANTECEDENT', 'II: CONCURRENT', 'III: CONSEQUENT'];
  const flip = i => setFlipped(f => f.map((v, idx) => idx === i ? true : v));
  return /*#__PURE__*/React.createElement("div", {
    style: {
      width: '100%',
      height: '100%',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      padding: '40px 24px',
      gap: 28,
      overflowY: 'auto'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-system)',
      fontSize: 9,
      color: 'var(--surface-40)',
      letterSpacing: '0.2em',
      textTransform: 'uppercase',
      animation: 'lunarot-flicker-cut var(--dur-curtain) var(--ease-snap)'
    },
    key: allFlipped ? 'done' : 'progress'
  }, allFlipped ? 'DESCENT COMPLETE // CIRCLE STABILIZED' : 'DESCENT IN PROGRESS // TAP EACH CONDUIT TO REVEAL'), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 32
    }
  }, cards.map((c, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    style: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 8
    }
  }, /*#__PURE__*/React.createElement(TarotCard, {
    card: c,
    flipped: flipped[i],
    reversed: c.reversed,
    broken: c.broken,
    onClick: () => flip(i)
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-system)',
      fontSize: 7,
      color: 'var(--surface-25)',
      letterSpacing: '0.2em'
    }
  }, POSITIONS[i])))), allFlipped && /*#__PURE__*/React.createElement(Panel, {
    variant: "white",
    tag: "SYNTHESIS",
    footerTag: "CONFLUENCE",
    style: {
      maxWidth: 640
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 14
    }
  }, window.LunarotDeck.synthesis(user, cards).map((p, i) => /*#__PURE__*/React.createElement(Typewriter, {
    key: i,
    text: p
  })))), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 16
    }
  }, /*#__PURE__*/React.createElement(Button, {
    variant: "secondary",
    onClick: onReset
  }, "CHANGE THE DATE")));
}
window.MainScreen = MainScreen;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/sacred-draw/MainScreen.jsx", error: String((e && e.message) || e) }); }

// ui_kits/sacred-draw/deck.js
try { (() => {
(function () {
  const DECK = [{
    name: "The Fool",
    num: "0",
    glyph: "🜁",
    tradition: "The Leap of Faith"
  }, {
    name: "The Magician",
    num: "I",
    glyph: "☿",
    tradition: "The Vessel"
  }, {
    name: "The High Priestess",
    num: "II",
    glyph: "☽",
    tradition: "The Inner Sanctum"
  }, {
    name: "The Empress",
    num: "III",
    glyph: "♀",
    tradition: "The Holy Mother"
  }, {
    name: "The Emperor",
    num: "IV",
    glyph: "♂",
    tradition: "The Divine Law"
  }, {
    name: "The Hierophant",
    num: "V",
    glyph: "♉",
    tradition: "The Initiated Teaching"
  }, {
    name: "The Lovers",
    num: "VI",
    glyph: "♊",
    tradition: "The Holy Covenant"
  }, {
    name: "The Chariot",
    num: "VII",
    glyph: "♋",
    tradition: "Merkabah Mysticism"
  }, {
    name: "Strength",
    num: "VIII",
    glyph: "♌",
    tradition: "The Greater Jihad"
  }, {
    name: "The Hermit",
    num: "IX",
    glyph: "⊕",
    tradition: "The Desert Fathers"
  }, {
    name: "Wheel of Fortune",
    num: "X",
    glyph: "♃",
    tradition: "Divine Providence"
  }, {
    name: "Death",
    num: "XIII",
    glyph: "♏",
    tradition: "Fanaa · Sufi Annihilation"
  }, {
    name: "The Tower",
    num: "XVI",
    glyph: "🜂",
    tradition: "The Prophetic Strike"
  }, {
    name: "The Star",
    num: "XVII",
    glyph: "★",
    tradition: "Ahura Mazda's Light"
  }, {
    name: "The Moon",
    num: "XVIII",
    glyph: "☾",
    tradition: "The Veil of Maya"
  }, {
    name: "The Sun",
    num: "XIX",
    glyph: "☉",
    tradition: "The Divine Illumination"
  }];
  function drawThree() {
    const pool = [...DECK];
    const out = [];
    for (let i = 0; i < 3; i++) {
      const idx = Math.floor(Math.random() * pool.length);
      const card = pool.splice(idx, 1)[0];
      out.push({
        ...card,
        reversed: Math.random() < 0.4,
        broken: Math.random() < 0.15
      });
    }
    return out;
  }
  function synthesis(user, cards) {
    const [past, present, future] = cards;
    return [`Your Sun rests in ${user.sun}, your Moon drifts through ${user.moon} — the circle reads this confluence against three drawn conduits.`, `${past.name}${past.reversed ? ' (reversed)' : ''} marks the antecedent: what shaped the vessel before this descent began.`, `${present.name}${present.reversed ? ' (reversed)' : ''} holds the concurrent — the pressure active in the circle right now.`, `${future.name}${future.reversed ? ' (reversed)' : ''} names the consequent: where the current bends, if the circle is not broken.`];
  }
  window.LunarotDeck = {
    DECK,
    drawThree,
    synthesis
  };
})();
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/sacred-draw/deck.js", error: String((e && e.message) || e) }); }

// ui_kits/sefirot-codex/SefirotScreen.jsx
try { (() => {
function SefirotScreen() {
  const {
    Panel,
    Button,
    NavButton,
    Typewriter
  } = window.LunarotDesignSystem_03ee3e;
  const {
    SEPHIROT,
    PATHWAYS
  } = window.SefirotData;
  const [selected, setSelected] = React.useState(SEPHIROT[0]);
  const byId = id => SEPHIROT.find(s => s.id === id);
  return /*#__PURE__*/React.createElement("div", {
    style: {
      width: '100%',
      height: '100%',
      display: 'flex',
      flexDirection: 'column',
      background: '#000'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: '10px 24px',
      borderBottom: '1px solid var(--surface-15)',
      fontFamily: 'var(--font-system)',
      fontSize: 9,
      color: 'var(--surface-40)',
      letterSpacing: '0.15em',
      textTransform: 'uppercase'
    }
  }, /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("span", {
    style: {
      color: 'var(--surface)'
    }
  }, "\u25C7"), " LUNAROT OS"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 10
    }
  }, /*#__PURE__*/React.createElement(NavButton, {
    active: "primary"
  }, "SEFIROT CODEX"), /*#__PURE__*/React.createElement(NavButton, null, "LEXICON")), /*#__PURE__*/React.createElement("span", null, "ARCHIVE_SYNC_OK")), /*#__PURE__*/React.createElement("div", {
    style: {
      flex: 1,
      display: 'flex',
      gap: 24,
      padding: 24,
      overflow: 'hidden'
    }
  }, /*#__PURE__*/React.createElement(Panel, {
    variant: "white",
    tag: "ETZ CHAIM",
    footerTag: "TREE OF LIFE",
    style: {
      width: 340,
      flexShrink: 0
    }
  }, /*#__PURE__*/React.createElement("svg", {
    viewBox: "20 20 360 660",
    style: {
      width: '100%',
      height: 460
    }
  }, PATHWAYS.map(([a, b, letter], i) => {
    const pa = byId(a),
      pb = byId(b);
    return /*#__PURE__*/React.createElement("line", {
      key: i,
      x1: pa.x,
      y1: pa.y,
      x2: pb.x,
      y2: pb.y,
      stroke: "var(--surface-15)",
      strokeWidth: "1"
    });
  }), SEPHIROT.map(s => /*#__PURE__*/React.createElement("g", {
    key: s.id,
    onClick: () => setSelected(s),
    style: {
      cursor: 'pointer'
    }
  }, /*#__PURE__*/React.createElement("circle", {
    cx: s.x,
    cy: s.y,
    r: selected.id === s.id ? 22 : 16,
    fill: selected.id === s.id ? 'var(--surface)' : 'var(--ash)',
    stroke: "var(--bone)",
    strokeWidth: "1.5"
  }), /*#__PURE__*/React.createElement("text", {
    x: s.x,
    y: s.y + 5,
    textAnchor: "middle",
    fontSize: "14",
    fill: selected.id === s.id ? 'var(--ink)' : 'var(--surface-60)',
    fontFamily: "serif"
  }, s.hebrew[0]))))), /*#__PURE__*/React.createElement(Panel, {
    variant: "gold",
    tag: "SCHOLARLY DOSSIER",
    footerTag: selected.pillar + ' PILLAR',
    style: {
      flex: 1,
      overflowY: 'auto'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'flex-start',
      borderBottom: '1px solid var(--surface-15)',
      paddingBottom: 16,
      marginBottom: 16
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: 28,
      color: 'var(--surface)',
      letterSpacing: '0.05em',
      margin: 0
    }
  }, selected.name), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: 'var(--font-body)',
      fontStyle: 'italic',
      fontSize: 14,
      color: 'var(--surface-60)',
      margin: '4px 0 0'
    }
  }, "\"", selected.meaning, "\"")), /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: 'right'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: 36,
      color: 'var(--surface)'
    }
  }, selected.hebrew), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-system)',
      fontSize: 10,
      color: 'var(--surface-40)'
    }
  }, "/", selected.translit, "/"))), /*#__PURE__*/React.createElement(Typewriter, {
    key: selected.id,
    text: selected.desc,
    style: {
      marginBottom: 16
    }
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'var(--surface-08)',
      border: '1px solid var(--surface-15)',
      padding: 14
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-system)',
      fontSize: 8,
      color: 'var(--surface-40)',
      letterSpacing: '0.15em',
      textTransform: 'uppercase',
      marginBottom: 6
    }
  }, "\u25C6 Trilateral Consonantal Root"), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: 16,
      color: 'var(--bone)'
    }
  }, selected.root), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-body)',
      fontStyle: 'italic',
      fontSize: 12,
      color: 'var(--surface-40)',
      marginTop: 6
    }
  }, "Etymology: ", selected.etymology)))));
}
window.SefirotScreen = SefirotScreen;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/sefirot-codex/SefirotScreen.jsx", error: String((e && e.message) || e) }); }

// ui_kits/sefirot-codex/sefirot-data.js
try { (() => {
(function () {
  const S = [{
    id: 'keter',
    name: 'Keter',
    hebrew: 'כֶּתֶר',
    translit: 'Kether',
    meaning: 'Crown',
    pillar: 'Center',
    x: 200,
    y: 55,
    desc: 'The absolute source, the primordial will from which all things emanate — the boundary between the infinite (Ein Sof) and the manifest universe. Known as Ayin ("Nothingness") because it precedes all differentiation.',
    root: 'כ.ת.ר (Kaf-Tav-Resh)',
    etymology: '"To surround, encircle, or crown."'
  }, {
    id: 'chokhmah',
    name: 'Chokhmah',
    hebrew: 'חָכְמָה',
    translit: 'Chokhmah',
    meaning: 'Wisdom',
    pillar: 'Right',
    x: 300,
    y: 120,
    desc: 'The raw, unshaped flash of wisdom — the initial seed of creation, the point that expands into Binah. Called "Being from Nothingness," the intuitive spark before logical development.',
    root: 'ח.כ.מ (Chet-Kaf-Mem)',
    etymology: '"To count, hold wisdom, align insight."'
  }, {
    id: 'binah',
    name: 'Binah',
    hebrew: 'בִּינָה',
    translit: 'Binah',
    meaning: 'Understanding',
    pillar: 'Left',
    x: 100,
    y: 120,
    desc: 'The active, architectural analytical intelligence. It receives the seed of Chokhmah and expands it into structured concepts — the blueprint of existence. Known as the Mother (Imma).',
    root: 'ב.י.נ (Bet-Yod-Nun)',
    etymology: 'From "Bain" (between) and "Lehavin" (to distinguish, analyze).'
  }, {
    id: 'daat',
    name: "Da'at",
    hebrew: 'דַּעַת',
    translit: "Da'ath",
    meaning: 'Knowledge',
    pillar: 'Center',
    x: 200,
    y: 190,
    desc: 'The unique "invisible" Sephirah — the synthesis of Chokhmah and Binah, transforming theory into internalized, living knowledge. Not counted among the traditional ten.',
    root: 'י.ד.ע (Yod-Dalet-Ayin)',
    etymology: '"To know, perceive by intimacy" (as in "Adam knew Eve").'
  }, {
    id: 'chesed',
    name: 'Chesed',
    hebrew: 'חֶסֶד',
    translit: 'Chesed',
    meaning: 'Mercy / Lovingkindness',
    pillar: 'Right',
    x: 300,
    y: 260,
    desc: 'Unconditional benevolence and the expansive force of love — the drive to bestow goodness infinitely, without checking worthiness. The first day of creation.',
    root: 'ח.ס.ד (Chet-Samekh-Dalet)',
    etymology: '"Benevolence, compassion, pact of kindness."'
  }, {
    id: 'gevurah',
    name: 'Gevurah',
    hebrew: 'גְּבוּרָה',
    translit: 'Gevurah',
    meaning: 'Severity / Strength',
    pillar: 'Left',
    x: 100,
    y: 260,
    desc: "Cosmic constraint, boundary, and judgment. Without it Chesed's light would overwhelm creation; Gevurah is the vessel that concentrates light into boundaries that allow individual existence.",
    root: 'ג.ב.ר (Gimel-Bet-Resh)',
    etymology: '"To be strong, conquer, define borders."'
  }, {
    id: 'tiferet',
    name: 'Tiferet',
    hebrew: 'תִּפְאֶרֶת',
    translit: 'Tiphareth',
    meaning: 'Beauty / Harmony',
    pillar: 'Center',
    x: 200,
    y: 330,
    desc: 'Sits at the core of the Tree, balancing the expanding flow of Chesed and the restrictive vessel of Gevurah — the heart center, corresponding to beauty and equilibrium.',
    root: 'פ.א.ר (Pe-Alef-Resh)',
    etymology: '"Glorify, adorn, beautiful patterns."'
  }, {
    id: 'netzach',
    name: 'Netzach',
    hebrew: 'נֶצַח',
    translit: 'Netzach',
    meaning: 'Victory / Endurance',
    pillar: 'Right',
    x: 300,
    y: 450,
    desc: 'Endurance, active push, conquest of obstacles, and propagation. Active, masculine, outward-facing — the dynamic propulsion of divine light.',
    root: 'נ.צ.ח (Nun-Tsade-Chet)',
    etymology: '"To conquer, to last forever."'
  }, {
    id: 'hod',
    name: 'Hod',
    hebrew: 'הוֹד',
    translit: 'Hod',
    meaning: 'Splendor / Reverence',
    pillar: 'Left',
    x: 100,
    y: 450,
    desc: 'Aesthetic splendor, surrender, and receptive alignment. While Netzach pushes forward, Hod yields — translating raw push into structured, beautiful expression.',
    root: 'ה.ו.ד (He-Vav-Dalet)',
    etymology: '"To acknowledge, praise, submit, majesty."'
  }, {
    id: 'yesod',
    name: 'Yesod',
    hebrew: 'יְסוֹד',
    translit: 'Yesod',
    meaning: 'Foundation',
    pillar: 'Center',
    x: 200,
    y: 540,
    desc: 'The funnel and foundation of consciousness — collects the energies of the upper Sephirot, unifies them, and channels them down into Malkhut.',
    root: 'י.ס.ד (Yod-Samekh-Dalet)',
    etymology: '"To base, lay a foundation stone."'
  }, {
    id: 'malkhut',
    name: 'Malkhut',
    hebrew: 'מַלְכוּת',
    translit: 'Malkhuth',
    meaning: 'Kingdom / Presence',
    pillar: 'Center',
    x: 200,
    y: 650,
    desc: 'The lowest point of the Tree — physical reality, the material universe, the Shechinah (feminine Divine immanence). An empty vessel with no light of its own, receiving everything.',
    root: 'מ.ל.כ (Mem-Lamed-Kaf)',
    etymology: '"To rule, reign, sovereign presence."'
  }];
  const PATHWAYS = [['keter', 'chokhmah', 'א'], ['keter', 'binah', 'ב'], ['keter', 'tiferet', 'ג'], ['chokhmah', 'binah', 'ד'], ['chokhmah', 'tiferet', 'ה'], ['chokhmah', 'chesed', 'ו'], ['binah', 'tiferet', 'ז'], ['binah', 'gevurah', 'ח'], ['chesed', 'gevurah', 'ט'], ['chesed', 'tiferet', 'י'], ['chesed', 'netzach', 'כ'], ['gevurah', 'tiferet', 'ל'], ['gevurah', 'hod', 'מ'], ['tiferet', 'netzach', 'נ'], ['tiferet', 'hod', 'ס'], ['tiferet', 'yesod', 'ע'], ['netzach', 'hod', 'פ'], ['netzach', 'yesod', 'צ'], ['netzach', 'malkhut', 'ק'], ['hod', 'yesod', 'ר'], ['hod', 'malkhut', 'ש'], ['yesod', 'malkhut', 'ת']];
  window.SefirotData = {
    SEPHIROT: S,
    PATHWAYS
  };
})();
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/sefirot-codex/sefirot-data.js", error: String((e && e.message) || e) }); }

// ui_kits/sigil-generator/check.js
try { (() => {
const cv = document.getElementById('c');
const ctx = cv.getContext('2d');
const DPR = Math.min(window.devicePixelRatio || 2, 3);

// ── STATE ──────────────────────────────────────────────
const PALETTE = [{
  label: 'INK',
  val: '#0a0806'
}, {
  label: 'BG',
  val: '#f5f2ed'
}, {
  label: 'BLOOD',
  val: '#8a1a1a'
}, {
  label: 'GOLD',
  val: '#8a7438'
}, {
  label: 'BONE',
  val: '#c8c2b6'
}, {
  label: 'VOID',
  val: '#04040a'
}, {
  label: 'ASH',
  val: '#2a2826'
}, {
  label: 'ALT',
  val: '#1a3a6a'
}];
const SECRET_COLOR = '#ff003c';
let particles = [];
let mouse = {
  x: -1000,
  y: -1000,
  vx: 0,
  vy: 0
};
let state = {
  ink: '#ffffff',
  bg: '#000000',
  ac: '#efede8',
  third: '#080808',
  secretColor: '#ff003c',
  activeSlot: 0,
  sw: 0.6,
  seed: Math.random() * 99999 | 0,
  inverted: false,
  exporting: false,
  sets: {
    cert: true,
    cyber: true,
    geo: true,
    arrow: true,
    occult: true,
    ascii: true,
    text: true,
    data: true,
    unicode: true
  }
};

// ── PALETTE STRIP BUILD ────────────────────────────────
const palDiv = document.getElementById('palette');
// 4 colour slots
const slotLabels = ['SURFACE', 'VOID', 'BONE', 'ASH'];
const slotKeys = ['ink', 'bg', 'ac', 'third'];
const slotColors = [state.ink, state.bg, state.ac, state.third];
slotColors.forEach((col, i) => {
  const d = document.createElement('div');
  d.className = 'pal-swatch' + (i === 0 ? ' active' : '');
  d.style.background = col;
  d.dataset.slot = i;
  d.title = slotLabels[i];
  const inp = document.createElement('input');
  inp.type = 'color';
  inp.value = col;
  inp.style.position = 'fixed';
  inp.style.left = '50vw';
  inp.style.top = '50vh';
  inp.style.opacity = '0';
  inp.style.pointerEvents = 'none';
  document.body.appendChild(inp);
  inp.addEventListener('input', e => {
    state[slotKeys[i]] = e.target.value;
    d.style.background = e.target.value;
  });
  d.addEventListener('pointerdown', e => {
    document.querySelectorAll('.pal-swatch').forEach(s => s.classList.remove('active'));
    d.classList.add('active');
    state.activeSlot = i;
    document.getElementById('activePip').textContent = slotLabels[i];
  });
  d.addEventListener('click', e => {
    try {
      inp.showPicker();
    } catch (err) {
      inp.click();
    }
  });
  palDiv.appendChild(d);
});

// ── RNG ───────────────────────────────────────────────
let rng;
function mkRng(s) {
  let n = s * 2654435761 >>> 0;
  return () => {
    n ^= n << 13;
    n ^= n >> 17;
    n ^= n << 5;
    return (n >>> 0) / 0xffffffff;
  };
}
function pick(a) {
  return a[Math.floor(rng() * a.length)];
}
function drawCircularText(c, txt, x, y, r, fontSize, ink) {
  c.fillStyle = ink;
  c.font = `700 ${fontSize}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  let step = Math.PI * 2 / txt.length;
  for (let i = 0; i < txt.length; i++) {
    c.save();
    c.translate(x + Math.cos(i * step) * r, y + Math.sin(i * step) * r);
    c.rotate(i * step + Math.PI / 2);
    c.fillText(txt[i], 0, 0);
    c.restore();
  }
}

// ── SYMBOL LIBRARIES ──────────────────────────────────

const certSymbols = [(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  drawCircularText(c, pick(labels).replace(/ /g, '') + '•', x, y, sz * .32, sz * .1, ink);
  c.fillStyle = ink;
  c.font = `700 ${sz * .18}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(labels), x, y);
}, (c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .46, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .36, 0, Math.PI * 2);
  c.stroke();
  drawCircularText(c, pick(labels) + ' • ' + pick(labels), x, y, sz * .41, sz * .08, ink);
  c.fillStyle = ink;
  c.font = `700 ${sz * .12}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(labels), x, y - sz * .1);
  c.fillText(pick(labels), x, y + sz * .1);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.font = `700 ${sz * .26}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(labels), x, y);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  [-sz * .22, 0, sz * .22].forEach(dx => {
    c.beginPath();
    c.arc(x + dx, y, sz * .2, 0, Math.PI * 2);
    c.stroke();
  });
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x, y - sz * .42);
  c.lineTo(x + sz * .3, y);
  c.lineTo(x, y + sz * .42);
  c.lineTo(x - sz * .3, y);
  c.closePath();
  c.stroke();
  c.fillStyle = ink;
  c.font = `700 ${sz * .15}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(labels), x, y);
}, (c, x, y, sz, ink, sw) => {
  const hw = sz * .38,
    hh = sz * .22;
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - hw, y - hh, hw * 2, hh * 2);
  c.fillStyle = ink;
  c.font = `700 ${sz * .18}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(labels), x, y - hh * .3);
  c.font = `400 ${sz * .11}px 'Tiny5', sans-serif`;
  c.fillText(pick(labels), x, y + hh * .4);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.font = `900 ${sz * .34}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('K', x, y);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  [sz * .42, sz * .26].forEach(r => {
    c.beginPath();
    c.arc(x, y, r, 0, Math.PI * 2);
    c.stroke();
  });
  c.fillStyle = ink;
  c.font = `700 ${sz * .18}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(labels), x, y);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .44, y - sz * .24, sz * .88, sz * .48);
  c.fillStyle = ink;
  c.font = `400 ${sz * .12}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(labels), x, y);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw * 1.1;
  c.beginPath();
  c.arc(x - sz * .1, y, sz * .34, Math.PI * .3, Math.PI * 1.7);
  c.stroke();
  c.beginPath();
  c.arc(x + sz * .1, y, sz * .34, Math.PI * .3, Math.PI * 1.7, true);
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .14, 0, Math.PI * 2);
  c.stroke();
  for (let i = 0; i < 6; i++) {
    const a = i * Math.PI / 3;
    c.beginPath();
    c.moveTo(x + Math.cos(a) * sz * .18, y + Math.sin(a) * sz * .18);
    c.lineTo(x + Math.cos(a) * sz * .42, y + Math.sin(a) * sz * .42);
    c.stroke();
  }
}];
const eyeSymbols = [(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x - sz * .42, y);
  c.quadraticCurveTo(x, y - sz * .32, x + sz * .42, y);
  c.quadraticCurveTo(x, y + sz * .32, x - sz * .42, y);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .16, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .07, 0, Math.PI * 2);
  c.fill();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .28, y);
  c.quadraticCurveTo(x, y - sz * .2, x + sz * .28, y);
  c.quadraticCurveTo(x, y + sz * .2, x - sz * .28, y);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .08, 0, Math.PI * 2);
  c.fill();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .42, y - sz * .36, sz * .84, sz * .72);
  c.beginPath();
  c.moveTo(x - sz * .26, y + sz * .06);
  c.quadraticCurveTo(x, y - sz * .18, x + sz * .26, y + sz * .06);
  c.quadraticCurveTo(x, y + sz * .28, x - sz * .26, y + sz * .06);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y + sz * .1, sz * .07, 0, Math.PI * 2);
  c.fill();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.ellipse(x, y, sz * .42, sz * .26, 0, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .2, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x - sz * .06, y - sz * .06, sz * .08, 0, Math.PI * 2);
  c.fill();
  c.beginPath();
  c.arc(x, y, sz * .04, 0, Math.PI * 2);
  c.fill();
},
// Sephirotic eye — rays
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .22, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .08, 0, Math.PI * 2);
  c.fill();
  c.lineWidth = sw * .6;
  for (let i = 0; i < 8; i++) {
    const a = i * Math.PI / 4;
    c.beginPath();
    c.moveTo(x + Math.cos(a) * sz * .25, y + Math.sin(a) * sz * .25);
    c.lineTo(x + Math.cos(a) * sz * .38, y + Math.sin(a) * sz * .38);
    c.stroke();
  }
},
// Weeping eye (lashes)
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x - sz * .38, y);
  c.quadraticCurveTo(x, y - sz * .28, x + sz * .38, y);
  c.quadraticCurveTo(x, y + sz * .28, x - sz * .38, y);
  c.stroke();
  for (let i = -3; i <= 3; i++) {
    c.beginPath();
    c.moveTo(x + i * sz * .1, y - sz * .28);
    c.lineTo(x + i * sz * .12, y - sz * .42);
    c.stroke();
  }
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .1, 0, Math.PI * 2);
  c.fill();
},
// Almond eye extreme
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x - sz * .48, y);
  c.bezierCurveTo(x - sz * .2, y - sz * .38, x + sz * .2, y - sz * .38, x + sz * .48, y);
  c.bezierCurveTo(x + sz * .2, y + sz * .38, x - sz * .2, y + sz * .38, x - sz * .48, y);
  c.stroke();
  [sz * .2, sz * .1, sz * .04].forEach(r => {
    c.beginPath();
    c.arc(x, y, r, 0, Math.PI * 2);
    c.stroke();
  });
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .04, 0, Math.PI * 2);
  c.fill();
},
// Many eyes grid
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw * .7;
  [[-sz * .2, -sz * .18], [sz * .2, -sz * .18], [0, sz * .18]].forEach(([ox, oy]) => {
    c.beginPath();
    c.moveTo(x + ox - sz * .14, y + oy);
    c.quadraticCurveTo(x + ox, y + oy - sz * .1, x + ox + sz * .14, y + oy);
    c.quadraticCurveTo(x + ox, y + oy + sz * .1, x + ox - sz * .14, y + oy);
    c.stroke();
    c.fillStyle = ink;
    c.beginPath();
    c.arc(x + ox, y + oy, sz * .04, 0, Math.PI * 2);
    c.fill();
  });
},
// -- 15 MORE EYE VARIATIONS --
// 1. Oval eye with solid pupil and highlight
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.ellipse(x, y, sz * .4, sz * .2, 0, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.ellipse(x, y, sz * .15, sz * .15, 0, 0, Math.PI * 2);
  c.fill();
  c.fillStyle = state.bg;
  c.beginPath();
  c.arc(x + sz * .05, y - sz * .05, sz * .03, 0, Math.PI * 2);
  c.fill();
},
// 2. Wide oval eye with crosshair pupil
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.ellipse(x, y, sz * .45, sz * .15, 0, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .1, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .1, y);
  c.lineTo(x + sz * .1, y);
  c.stroke();
  c.beginPath();
  c.moveTo(x, y - sz * .1);
  c.lineTo(x, y + sz * .1);
  c.stroke();
},
// 3. Sticker eye with white outline
(c, x, y, sz, ink, sw) => {
  c.fillStyle = state.bg;
  c.beginPath();
  c.ellipse(x, y, sz * .42, sz * .25, 0, 0, Math.PI * 2);
  c.fill();
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .12, 0, Math.PI * 2);
  c.fill();
  c.fillStyle = state.bg;
  c.beginPath();
  c.arc(x + sz * .03, y - sz * .03, sz * .02, 0, Math.PI * 2);
  c.fill();
  c.beginPath();
  c.arc(x - sz * .03, y + sz * .02, sz * .01, 0, Math.PI * 2);
  c.fill();
},
// 4. Double stroked eye
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw * .5;
  c.beginPath();
  c.ellipse(x, y, sz * .4, sz * .2, 0, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.ellipse(x, y, sz * .35, sz * .15, 0, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .08, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .03, 0, Math.PI * 2);
  c.fill();
},
// 5. Vertical slit eye
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.ellipse(x, y, sz * .4, sz * .25, 0, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.ellipse(x, y, sz * .05, sz * .15, 0, 0, Math.PI * 2);
  c.fill();
},
// 6. Angled sticker eye
(c, x, y, sz, ink, sw) => {
  c.save();
  c.translate(x, y);
  c.rotate(Math.PI / 6);
  c.fillStyle = state.bg;
  c.beginPath();
  c.ellipse(0, 0, sz * .4, sz * .2, 0, 0, Math.PI * 2);
  c.fill();
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(0, 0, sz * .1, 0, Math.PI * 2);
  c.fill();
  c.fillStyle = state.bg;
  c.beginPath();
  c.arc(sz * .03, -sz * .03, sz * .02, 0, Math.PI * 2);
  c.fill();
  c.restore();
},
// 7. Minimalist line eye
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x - sz * .4, y);
  c.quadraticCurveTo(x, y - sz * .3, x + sz * .4, y);
  c.stroke();
  c.beginPath();
  c.arc(x, y + sz * .05, sz * .1, 0, Math.PI * 2);
  c.stroke();
},
// 8. Geometric triangle eye
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x - sz * .4, y);
  c.lineTo(x, y - sz * .25);
  c.lineTo(x + sz * .4, y);
  c.lineTo(x, y + sz * .25);
  c.closePath();
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .12, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .05, 0, Math.PI * 2);
  c.fill();
},
// 9. Floating pupil eye
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.ellipse(x, y, sz * .4, sz * .2, 0, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x + sz * .15, y, sz * .08, 0, Math.PI * 2);
  c.fill();
},
// 10. Bleeding sticker eye
(c, x, y, sz, ink, sw) => {
  c.fillStyle = state.bg;
  c.beginPath();
  c.ellipse(x, y, sz * .4, sz * .2, 0, 0, Math.PI * 2);
  c.fill();
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .1, 0, Math.PI * 2);
  c.fill();
  c.beginPath();
  c.moveTo(x - sz * .05, y + sz * .05);
  c.lineTo(x - sz * .05, y + sz * .3);
  c.lineTo(x + sz * .05, y + sz * .25);
  c.lineTo(x + sz * .05, y + sz * .05);
  c.fill();
},
// 11. Multi-ring eye
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw * .6;
  c.beginPath();
  c.ellipse(x, y, sz * .45, sz * .25, 0, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .2, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .15, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .1, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .05, 0, Math.PI * 2);
  c.fill();
},
// 12. Square pupil eye
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.ellipse(x, y, sz * .4, sz * .2, 0, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.fillRect(x - sz * .1, y - sz * .1, sz * .2, sz * .2);
  c.fillStyle = state.bg;
  c.fillRect(x - sz * .03, y - sz * .03, sz * .06, sz * .06);
},
// 13. Dot matrix eye
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.ellipse(x, y, sz * .4, sz * .25, 0, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  for (let i = 0; i < 5; i++) {
    c.beginPath();
    c.arc(x - sz * .2 + i * sz * .1, y, sz * .03, 0, Math.PI * 2);
    c.fill();
  }
},
// 14. Drooping sticker eye
(c, x, y, sz, ink, sw) => {
  c.fillStyle = state.bg;
  c.beginPath();
  c.moveTo(x - sz * .4, y);
  c.quadraticCurveTo(x, y - sz * .2, x + sz * .4, y);
  c.quadraticCurveTo(x, y + sz * .4, x - sz * .4, y);
  c.fill();
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y + sz * .05, sz * .1, 0, Math.PI * 2);
  c.fill();
},
// 15. Hypnotic spiral eye
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.ellipse(x, y, sz * .45, sz * .25, 0, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  for (let i = 0; i < 20; i++) {
    let a = i * Math.PI / 4;
    let r = i * sz * .01;
    if (i === 0) c.moveTo(x + Math.cos(a) * r, y + Math.sin(a) * r);else c.lineTo(x + Math.cos(a) * r, y + Math.sin(a) * r);
  }
  c.stroke();
},
// 16. Scattered clustered sticker eyes
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  for (let i = 0; i < 9; i++) {
    let ox = (prng() - 0.5) * sz * .7;
    let oy = (prng() - 0.5) * sz * .7;
    let esz = sz * (0.15 + prng() * 0.1);
    c.save();
    c.translate(x + ox, y + oy);
    c.rotate((prng() - 0.5) * 0.5);
    c.fillStyle = state.bg;
    c.beginPath();
    c.moveTo(-esz, 0);
    c.quadraticCurveTo(0, -esz * 0.8, esz, 0);
    c.quadraticCurveTo(0, esz * 0.8, -esz, 0);
    c.fill();
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.8;
    c.stroke();
    c.fillStyle = ink;
    c.beginPath();
    c.arc(0, 0, esz * 0.45, 0, Math.PI * 2);
    c.fill();
    c.fillStyle = state.bg;
    c.beginPath();
    c.arc(esz * 0.1, -esz * 0.1, esz * 0.15, 0, Math.PI * 2);
    c.fill();
    c.restore();
  }
},
// 17. Lilith mask eyes
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x - sz * .45, y - sz * .4);
  c.lineTo(x + sz * .45, y - sz * .4);
  c.lineTo(x, y + sz * .45);
  c.closePath();
  c.stroke();
  c.beginPath();
  c.moveTo(x, y - sz * .4);
  c.lineTo(x, y + sz * .45);
  c.stroke();
  const drawEye = (ex, ey, esz) => {
    c.beginPath();
    c.moveTo(ex - esz, ey);
    c.quadraticCurveTo(ex, ey - esz * 0.6, ex + esz, ey);
    c.quadraticCurveTo(ex, ey + esz * 0.6, ex - esz, ey);
    c.stroke();
    c.beginPath();
    c.arc(ex, ey, esz * 0.35, 0, Math.PI * 2);
    c.stroke();
  };
  // Left eyes
  drawEye(x - sz * .22, y - sz * .2, sz * .15);
  drawEye(x - sz * .17, y, sz * .15);
  drawEye(x - sz * .12, y + sz * .2, sz * .15);
  // Right eyes
  drawEye(x + sz * .22, y - sz * .25, sz * .14);
  drawEye(x + sz * .22, y - sz * .08, sz * .14);
  drawEye(x + sz * .17, y + sz * .1, sz * .14);
  drawEye(x + sz * .12, y + sz * .28, sz * .14);
}];
const kabbalSymbols = [
// Tree of Life nodes (Sephirot positions abstracted)
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  const pts = [[0, -.44], [-.22, -.2], [.22, -.2], [0, 0], [-.22, .2], [.22, .2], [0, .44]].map(([px, py]) => [x + px * sz, y + py * sz]);
  pts.forEach(([px, py]) => {
    c.beginPath();
    c.arc(px, py, sz * .08, 0, Math.PI * 2);
    c.stroke();
  });
  for (let i = 0; i < pts.length - 1; i++) {
    c.beginPath();
    c.moveTo(...pts[i]);
    c.lineTo(...pts[i + 1]);
    c.stroke();
  }
},
// Hexagram (Star of David)
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  [[0, 1], [Math.PI, 1]].forEach(([rot]) => {
    c.save();
    c.translate(x, y);
    c.rotate(rot);
    c.beginPath();
    const r = sz * .4;
    c.moveTo(0, -r);
    for (let i = 1; i < 3; i++) c.lineTo(Math.sin(i * Math.PI * 2 / 3) * r, -Math.cos(i * Math.PI * 2 / 3) * r);
    c.closePath();
    c.stroke();
    c.restore();
  });
},
// Aleph in circle
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.font = `900 ${sz * .42}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('א', x, y + sz * .04);
},
// Ayin (eye letter)
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.font = `900 ${sz * .38}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('ע', x, y + sz * .04);
},
// Kabbalistic cross
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x, y - sz * .44);
  c.lineTo(x, y + sz * .44);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .44, y - sz * .12);
  c.lineTo(x + sz * .44, y - sz * .12);
  c.stroke();
  c.beginPath();
  c.arc(x, y - sz * .12, sz * .12, 0, Math.PI * 2);
  c.stroke();
  for (let i = 0; i < 4; i++) {
    const a = i * Math.PI / 2;
    c.beginPath();
    c.arc(x + Math.cos(a) * sz * .32, y - sz * .12 + Math.sin(a) * sz * .32, sz * .05, 0, Math.PI * 2);
    c.stroke();
  }
},
// Ein Sof — infinity triple rings
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  [sz * .42, sz * .3, sz * .18].forEach(r => {
    c.beginPath();
    c.arc(x, y, r, 0, Math.PI * 2);
    c.stroke();
  });
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .05, 0, Math.PI * 2);
  c.fill();
  c.font = `400 ${sz * .1}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'top';
  c.fillText('∞', x, y + sz * .46);
},
// Shin letter (fire / spirit)
(c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `900 ${sz * .44}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('ש', x, y + sz * .04);
},
// Tetragrammaton block
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .4, y - sz * .28, sz * .8, sz * .56);
  c.fillStyle = ink;
  c.font = `700 ${sz * .28}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('יהוה', x, y + sz * .04);
}];
const arabicSymbols = [(c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `900 ${sz * .42}px 'Coral Pixels',serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('بسم', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.font = `900 ${sz * .36}px 'Coral Pixels',serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('الله', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `700 ${sz * .28}px 'Coral Pixels',serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('نور', x, y - sz * .1);
  c.font = `700 ${sz * .18}px 'Tiny5', sans-serif`;
  c.fillText('NUR', x, y + sz * .18);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .42, y - sz * .3, sz * .84, sz * .6);
  c.fillStyle = ink;
  c.font = `700 ${sz * .26}px 'Coral Pixels',serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('روح', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `900 ${sz * .4}px 'Coral Pixels',serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('عين', x, y + sz * .04);
},
// Ayn — eye
(c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `700 ${sz * .22}px 'Coral Pixels',serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  const words = ['قمر', 'نار', 'أرض', 'هواء'];
  c.fillText(pick(words), x, y + sz * .04);
},
// Arabic letters as geometric — calligraphic strokes
(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw * 1.3;
  c.beginPath();
  c.moveTo(x - sz * .38, y);
  c.bezierCurveTo(x - sz * .1, y - sz * .38, x + sz * .1, y - sz * .38, x + sz * .38, y);
  c.stroke();
  c.beginPath();
  c.moveTo(x, y - sz * .3);
  c.lineTo(x, y + sz * .3);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x - sz * .38, y, sz * .04, 0, Math.PI * 2);
  c.fill();
}];
const jpSymbols = [(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.font = `900 ${sz * .36}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('検', x, y + sz * .02);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .4, y - sz * .32, sz * .8, sz * .64);
  c.fillStyle = ink;
  c.font = `900 ${sz * .34}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('視', x, y + sz * .02);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .38, y - sz * .3, sz * .76, sz * .6);
  c.fillStyle = ink;
  c.font = `900 ${sz * .24}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('金太', x, y - sz * .06);
  c.font = `700 ${sz * .12}px 'Tiny5', sans-serif`;
  c.fillText('TITANIUM', x, y + sz * .14);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `900 ${sz * .38}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(['霊', '魂', '呪', '死', '闇', '血']), x, y + sz * .02);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.font = `900 ${sz * .28}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('製品', x, y + sz * .02);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `700 ${sz * .18}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('遠', x, y - sz * .28);
  c.fillText('視', x, y + sz * .2);
  c.fillText('近', x - sz * .28, y);
  c.fillText('幅', x + sz * .28, y);
  c.strokeStyle = ink;
  c.lineWidth = sw * .7;
  c.beginPath();
  c.moveTo(x, y - sz * .15);
  c.lineTo(x, y + sz * .08);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .15, y);
  c.lineTo(x + sz * .15, y);
  c.stroke();
}];
const krSymbols = [(c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `900 ${sz * .38}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('루나', x, y + sz * .02);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.font = `900 ${sz * .32}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('데카', x, y + sz * .02);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .4, y - sz * .28, sz * .8, sz * .56);
  c.fillStyle = ink;
  c.font = `900 ${sz * .26}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(['저주', '어둠', '영혼', '달빛']), x, y + sz * .02);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `700 ${sz * .36}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('한', x, y + sz * .02);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .44, 0, Math.PI * 2);
  c.stroke();
}];
const curseSymbols = [(c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('⛧', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  for (let i = 0; i < 5; i++) {
    const a = i * Math.PI * 2 / 5 - Math.PI / 2,
      b = (i + 2) * Math.PI * 2 / 5 - Math.PI / 2;
    c.moveTo(x + Math.cos(a) * sz * .42, y + Math.sin(a) * sz * .42);
    c.lineTo(x + Math.cos(b) * sz * .42, y + Math.sin(b) * sz * .42);
  }
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  for (let i = 0; i < 5; i++) {
    const a = i * Math.PI * 2 / 5 - Math.PI / 2,
      b = (i + 2) * Math.PI * 2 / 5 - Math.PI / 2;
    c.moveTo(x + Math.cos(a) * sz * .38, y + Math.sin(a) * sz * .38);
    c.lineTo(x + Math.cos(b) * sz * .38, y + Math.sin(b) * sz * .38);
  }
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .44}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('🜏', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x, y - sz * .44);
  c.lineTo(x + sz * .44, y + sz * .3);
  c.lineTo(x - sz * .44, y + sz * .3);
  c.closePath();
  c.stroke();
  c.beginPath();
  c.moveTo(x, y + sz * .44);
  c.lineTo(x + sz * .44, y - sz * .3);
  c.lineTo(x - sz * .44, y - sz * .3);
  c.closePath();
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .36}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(['☽', '☾', '🌑', '⚸']), x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .3, y - sz * .2);
  c.lineTo(x + sz * .3, y + sz * .2);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .3, y + sz * .2);
  c.lineTo(x + sz * .3, y - sz * .2);
  c.stroke();
  c.beginPath();
  c.moveTo(x, y - sz * .42);
  c.lineTo(x, y + sz * .42);
  c.stroke();
}];
const cyberSymbols = [(c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `700 ${sz * .28}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'left';
  c.textBaseline = 'top';
  [pick(labels), pick(labels), pick(labels)].forEach((l, i) => c.fillText(l, x - sz * .38, y - sz * .28 + i * sz * .2));
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .42, y - sz * .34, sz * .84, sz * .68);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `400 ${sz * .11}px 'Tiny5', sans-serif`;
  c.textAlign = 'left';
  c.textBaseline = 'top';
  ['INPUT: 12V 3A', 'OUTPUT:5V 2A', '50-60Hz'].forEach((l, i) => c.fillText(l, x - sz * .4, y - sz * .22 + i * sz * .17));
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .44, y - sz * .3, sz * .88, sz * .6);
}, (c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.fillStyle = ink;
  c.font = `700 ${sz * .14}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(`0x${(prng() * 0xFFFF | 0).toString(16).toUpperCase().padStart(4, '0')}`, x, y - sz * .1);
  c.font = `400 ${sz * .1}px 'Tiny5', sans-serif`;
  c.fillText(`${pick(labels)}_${prng() * 999 | 0}`, x, y + sz * .1);
  c.strokeStyle = ink;
  c.lineWidth = sw * .6;
  c.beginPath();
  c.moveTo(x - sz * .42, y - sz * .2);
  c.lineTo(x + sz * .42, y - sz * .2);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .42, y + sz * .2);
  c.lineTo(x + sz * .42, y + sz * .2);
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `900 ${sz * .22}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(labels), x, y - sz * .12);
  c.font = `400 ${sz * .1}px 'Tiny5', sans-serif`;
  c.fillText(pick(labels), x, y + sz * .1);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x - sz * .42, y - sz * .42);
  c.lineTo(x + sz * .42, y - sz * .42);
  c.lineTo(x + sz * .42, y + sz * .42);
  c.lineTo(x - sz * .42, y + sz * .42);
  c.closePath();
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .28, y - sz * .28);
  c.lineTo(x + sz * .28, y - sz * .28);
  c.lineTo(x + sz * .28, y + sz * .28);
  c.lineTo(x - sz * .28, y + sz * .28);
  c.closePath();
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .42, y - sz * .42);
  c.lineTo(x - sz * .28, y - sz * .28);
  c.stroke();
  c.beginPath();
  c.moveTo(x + sz * .42, y - sz * .42);
  c.lineTo(x + sz * .28, y - sz * .28);
  c.stroke();
}, (c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.fillStyle = ink;
  c.font = `400 ${sz * .1}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  const lines = [`MFD-${prng() * 9000 + 1000 | 0}`, `COMPLYON PRH`, `ICES-33-20`];
  lines.forEach((l, i) => c.fillText(l, x, y - sz * .15 + i * sz * .18));
  c.strokeStyle = ink;
  c.lineWidth = sw * .5;
  c.strokeRect(x - sz * .42, y - sz * .28, sz * .84, sz * .56);
}];
const horrorSymbols = [(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.font = `${sz * .36}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('☠', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.ellipse(x, y - sz * .06, sz * .28, sz * .32, 0, 0, Math.PI * 2);
  c.stroke();
  c.strokeRect(x - sz * .2, y + sz * .18, sz * .4, sz * .2);
  c.beginPath();
  c.moveTo(x - sz * .28, y + sz * .18);
  c.lineTo(x - sz * .28, y + sz * .38);
  c.moveTo(x + sz * .28, y + sz * .18);
  c.lineTo(x + sz * .28, y + sz * .38);
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x - sz * .42, y);
  c.quadraticCurveTo(x, y - sz * .3, x + sz * .42, y);
  c.quadraticCurveTo(x, y + sz * .3, x - sz * .42, y);
  c.stroke();
  [[-sz * .16, 0], [sz * .16, 0]].forEach(([ox]) => {
    c.beginPath();
    c.moveTo(x + ox - sz * .07, y - sz * .07);
    c.lineTo(x + ox + sz * .07, y + sz * .07);
    c.stroke();
    c.beginPath();
    c.moveTo(x + ox + sz * .07, y - sz * .07);
    c.lineTo(x + ox - sz * .07, y + sz * .07);
    c.stroke();
  });
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .42}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(['🜔', '🜃', '🜁', '🜂', '🜄']), x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  for (let i = 0; i < 4; i++) {
    c.beginPath();
    c.moveTo(x - sz * .32 + i * sz * .16, y - sz * .3);
    c.lineTo(x - sz * .28 + i * sz * .16, y + sz * .3);
    c.stroke();
  }
  c.beginPath();
  c.moveTo(x - sz * .38, y + sz * .1);
  c.lineTo(x + sz * .32, y - sz * .1);
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x, y + sz * .38);
  c.bezierCurveTo(x - sz * .5, y + sz * .1, x - sz * .5, y - sz * .3, x, y - sz * .06);
  c.bezierCurveTo(x + sz * .5, y - sz * .3, x + sz * .5, y + sz * .1, x, y + sz * .38);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .12, y - sz * .06);
  c.bezierCurveTo(x - sz * .3, y - sz * .3, x - sz * .1, y - sz * .44, x, y - sz * .28);
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x, y - sz * .44);
  c.lineTo(x, y + sz * .2);
  c.stroke();
  c.beginPath();
  c.arc(x, y + sz * .28, sz * .1, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .1, y + sz * .05);
  c.lineTo(x, y + sz * .2);
  c.lineTo(x + sz * .1, y + sz * .05);
  c.stroke();
},
// Neural/Circuit grid
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  for (let i = 0; i < 6; i++) {
    let x1 = x + (prng() - 0.5) * sz * 0.8;
    let y1 = y + (prng() - 0.5) * sz * 0.8;
    let x2 = x + (prng() - 0.5) * sz * 0.8;
    let y2 = y + (prng() - 0.5) * sz * 0.8;
    c.moveTo(x1, y1);
    if (prng() > 0.5) {
      c.lineTo(x2, y1);
      c.lineTo(x2, y2);
    } else {
      c.lineTo(x1, y2);
      c.lineTo(x2, y2);
    }
  }
  c.stroke();
  for (let i = 0; i < 4; i++) {
    c.fillStyle = prng() > 0.5 ? ink : state.ac;
    c.beginPath();
    c.arc(x + (prng() - 0.5) * sz * 0.8, y + (prng() - 0.5) * sz * 0.8, sw * 1.5, 0, Math.PI * 2);
    c.fill();
  }
},
// Machine Eye
(c, x, y, sz, ink, sw, seed) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.ellipse(x, y, sz * .4, sz * .2, 0, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .15, 0, Math.PI * 2);
  c.stroke();
  let prng = mkRng(seed || 1234);
  c.fillStyle = prng() > 0.5 ? state.ac : ink;
  c.beginPath();
  c.arc(x, y, sz * .05, 0, Math.PI * 2);
  c.fill();
  c.beginPath();
  c.moveTo(x, y - sz * .2);
  c.lineTo(x, y - sz * .4);
  c.stroke();
  c.beginPath();
  c.moveTo(x, y + sz * .2);
  c.lineTo(x, y + sz * .4);
  c.stroke();
},
// Data Veins
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.lineWidth = sw * .8;
  c.beginPath();
  let cy = y - sz * .4;
  c.moveTo(x, cy);
  while (cy < y + sz * .4) {
    cy += sz * .1;
    let cx = x + Math.sin(cy / sz * 10 + prng() * 2) * sz * .2;
    c.lineTo(cx, cy);
  }
  c.stroke();
  c.strokeStyle = state.ac;
  c.beginPath();
  cy = y - sz * .4;
  c.moveTo(x - sz * .1, cy);
  while (cy < y + sz * .4) {
    cy += sz * .15;
    let cx = x - sz * .1 + Math.cos(cy / sz * 8 + prng() * 2) * sz * .15;
    c.lineTo(cx, cy);
  }
  c.stroke();
},
// Terminal Block
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.fillStyle = ink;
  c.fillRect(x - sz * .4, y - sz * .3, sz * .8, sz * .6);
  c.fillStyle = state.inverted ? state.ink : state.bg;
  c.font = `700 ${sz * .12}px 'Tiny5', sans-serif`;
  c.textAlign = 'left';
  c.textBaseline = 'top';
  c.fillText("ERR", x - sz * .35, y - sz * .25);
  c.fillText(pick(labels), x - sz * .35, y - sz * .05);
  c.fillText(`0x${(prng() * 0xFF | 0).toString(16).toUpperCase()}`, x - sz * .35, y + sz * .15);
},
// Barcode / Matrix
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.fillStyle = ink;
  for (let i = 0; i < 10; i++) {
    let h = sz * .1 + prng() * sz * .5;
    let w = sw + prng() * sw * 2;
    let px = x - sz * .4 + i * (sz * .8 / 10);
    c.fillRect(px, y - h / 2, w, h);
  }
  c.fillStyle = state.ac;
  c.font = `400 ${sz * .1}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'top';
  c.fillText((prng() * 999999999 | 0).toString().padStart(9, '0'), x, y + sz * .3);
},
// Abstract Machine Diagram
(c, x, y, sz, ink, sw, seed) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .3, y - sz * .3, sz * .6, sz * .6);
  c.beginPath();
  c.moveTo(x - sz * .3, y - sz * .3);
  c.lineTo(x + sz * .3, y + sz * .3);
  c.stroke();
  c.beginPath();
  c.moveTo(x + sz * .3, y - sz * .3);
  c.lineTo(x - sz * .3, y + sz * .3);
  c.stroke();
  c.fillStyle = state.bg;
  c.fillRect(x - sz * .1, y - sz * .1, sz * .2, sz * .2);
  c.strokeRect(x - sz * .1, y - sz * .1, sz * .2, sz * .2);
  c.fillStyle = state.ac;
  c.beginPath();
  c.arc(x, y, sz * .04, 0, Math.PI * 2);
  c.fill();
  [[x - sz * .3, y], [x + sz * .3, y], [x, y - sz * .3], [x, y + sz * .3]].forEach(([px, py]) => {
    c.beginPath();
    c.moveTo(px, py);
    c.lineTo(px + (px - x) * 0.3, py + (py - y) * 0.3);
    c.stroke();
  });
}];
const geoSymbols = [(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  [sz * .42, sz * .26, sz * .12].forEach(r => {
    c.beginPath();
    c.arc(x, y, r, 0, Math.PI * 2);
    c.stroke();
  });
  c.beginPath();
  c.moveTo(x - sz * .5, y);
  c.lineTo(x + sz * .5, y);
  c.stroke();
  c.beginPath();
  c.moveTo(x, y - sz * .5);
  c.lineTo(x, y + sz * .5);
  c.stroke();
  if (prng() > 0.5) drawCircularText(c, 'VECTOR • MATRIX •', x, y, sz * .34, sz * .08, ink);
}, (c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  for (let i = 0; i < 6; i++) {
    const a = i * Math.PI / 3 - Math.PI / 6;
    i === 0 ? c.moveTo(x + sz * .42 * Math.cos(a), y + sz * .42 * Math.sin(a)) : c.lineTo(x + sz * .42 * Math.cos(a), y + sz * .42 * Math.sin(a));
  }
  c.closePath();
  c.stroke();
  drawCircularText(c, pick(labels) + ' • ', x, y, sz * .31, sz * .09, ink);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  [sz * .42, sz * .28, sz * .14].forEach(r => c.strokeRect(x - r, y - r, r * 2, r * 2));
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  for (let i = 0; i < 6; i++) {
    const a = i * Math.PI / 3 - Math.PI / 6;
    i === 0 ? c.moveTo(x + sz * .42 * Math.cos(a), y + sz * .42 * Math.sin(a)) : c.lineTo(x + sz * .42 * Math.cos(a), y + sz * .42 * Math.sin(a));
  }
  c.closePath();
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.roundRect(x - sz * .45, y - sz * .32, sz * .9, sz * .64, sz * .14);
  c.stroke();
  c.fillStyle = ink;
  [-sz * .22, 0, sz * .22].forEach(dx => {
    c.beginPath();
    c.arc(x + dx, y, sz * .08, 0, Math.PI * 2);
    c.fill();
  });
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x, y - sz * .44);
  c.lineTo(x + sz * .44, y + sz * .3);
  c.lineTo(x - sz * .44, y + sz * .3);
  c.closePath();
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .26, y);
  c.lineTo(x + sz * .26, y);
  c.stroke();
  c.beginPath();
  c.moveTo(x, y - sz * .26);
  c.lineTo(x, y + sz * .26);
  c.stroke();
}];
const arrowSymbols = [(c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw * 1.4;
  c.beginPath();
  c.moveTo(x - sz * .36, y);
  c.lineTo(x + sz * .28, y);
  c.stroke();
  c.beginPath();
  c.moveTo(x + sz * .14, y - sz * .12);
  c.lineTo(x + sz * .28, y);
  c.lineTo(x + sz * .14, y + sz * .12);
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw * 1.4;
  c.beginPath();
  c.moveTo(x - sz * .38, y);
  c.lineTo(x + sz * .38, y);
  c.stroke();
  [[x - sz * .38, 1], [x + sz * .38, -1]].forEach(([px, d]) => {
    c.beginPath();
    c.moveTo(px + d * sz * .14, y - sz * .1);
    c.lineTo(px, y);
    c.lineTo(px + d * sz * .14, y + sz * .1);
    c.stroke();
  });
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .38, -.3, Math.PI * 1.8);
  c.stroke();
  const ex = x + sz * .38 * Math.cos(Math.PI * 1.8),
    ey = y + sz * .38 * Math.sin(Math.PI * 1.8);
  c.beginPath();
  c.moveTo(ex - sz * .1, ey - sz * .08);
  c.lineTo(ex, ey);
  c.lineTo(ex + sz * .08, ey - sz * .1);
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  [[0, -1], [1, 0], [0, 1], [-1, 0]].forEach(([dx, dy]) => {
    const ex = x + dx * sz * .4,
      ey = y + dy * sz * .4;
    c.beginPath();
    c.moveTo(x + dx * sz * .14, y + dy * sz * .14);
    c.lineTo(ex, ey);
    c.stroke();
    c.beginPath();
    c.moveTo(ex - dy * sz * .09 - dx * sz * .1, ey + dx * sz * .09 - dy * sz * .1);
    c.lineTo(ex, ey);
    c.lineTo(ex + dy * sz * .09 - dx * sz * .1, ey - dx * sz * .09 - dy * sz * .1);
    c.stroke();
  });
}];
const dystopSymbols = [(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  const bars = 16,
    bw = sz * .88 / bars;
  for (let i = 0; i < bars; i++) {
    const thick = i % 3 === 0 ? bw * 1.9 : bw * .65;
    c.fillStyle = ink;
    c.fillRect(x - sz * .44 + i * bw, y - sz * .28, thick, sz * .56);
  }
  c.font = `400 ${sz * .1}px 'Tiny5', sans-serif`;
  c.fillStyle = ink;
  c.textAlign = 'center';
  c.textBaseline = 'top';
  c.fillText(`${prng() * 9000 + 1000 | 0}`, x, y + sz * .3);
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .44, y - sz * .32, sz * .88, sz * .64);
  c.fillStyle = ink;
  c.font = `400 ${sz * .12}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  ['SECTOR IV', 'WATCHGATE', 'ACTIVE'].forEach((l, i) => c.fillText(l, x, y - sz * .14 + i * sz * .17));
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .42, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.font = `900 ${sz * .2}px 'Coral Pixels', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('DO NOT', x, y - sz * .08);
  c.fillText('ENTER', x, y + sz * .14);
  c.lineWidth = sw * 1.4;
  c.beginPath();
  c.moveTo(x - sz * .3, y + sz * .02);
  c.lineTo(x + sz * .3, y + sz * .02);
  c.stroke();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x, y - sz * .44);
  c.lineTo(x + sz * .44, y + sz * .3);
  c.lineTo(x - sz * .44, y + sz * .3);
  c.closePath();
  c.stroke();
  c.lineWidth = sw * 1.4;
  c.beginPath();
  c.moveTo(x, y - sz * .24);
  c.lineTo(x, y + sz * .08);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y + sz * .18, sz * .05, 0, Math.PI * 2);
  c.fill();
}, (c, x, y, sz, ink, sw) => {
  c.strokeStyle = ink;
  c.lineWidth = sw;
  [[0, -1], [1, 0], [0, 1], [-1, 0]].forEach(([dx, dy]) => {
    c.beginPath();
    c.moveTo(x + dx * sz * .18, y + dy * sz * .18);
    c.lineTo(x + dx * sz * .42, y + dy * sz * .42);
    c.stroke();
    c.beginPath();
    c.arc(x + dx * sz * .42, y + dy * sz * .42, sz * .06, 0, Math.PI * 2);
    c.stroke();
  });
  c.beginPath();
  c.arc(x, y, sz * .14, 0, Math.PI * 2);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.arc(x, y, sz * .06, 0, Math.PI * 2);
  c.fill();
}, (c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.fillStyle = ink;
  c.font = `400 ${sz * .11}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  let p = prng();
  [`${pick(labels)}:${['A', 'B', 'C', 'D'][p * 4 | 0]}`, `${pick(labels)} ${prng() * 9 | 0}`, pick(labels)].forEach((l, i) => c.fillText(l, x, y - sz * .18 + i * sz * .2));
  c.strokeStyle = ink;
  c.lineWidth = sw * .6;
  c.strokeRect(x - sz * .4, y - sz * .3, sz * .8, sz * .6);
}];
const labels = ['SYSCORE', 'TELEMETRY', 'TXR', 'RCV', 'DIPLEXER', 'BASEBAND', 'NRZ-C', 'SYNC STATUS', 'CODING STATUS', 'CMD TONES', 'DSS 12', 'SNR', 'DL', 'PIONEER', 'ORBITAL', 'AZIMUTH', 'ELEVATION', 'ZENITH', 'NADIR', 'APOGEE', 'PERIGEE', 'APSE', 'NODE', 'ECLIPTIC', 'EQUATORIAL', 'DECLINATION', 'RIGHT ASCENSION', 'SIDEREAL', 'SYNODIC', 'KEPLERIAN', 'PERTURBATION', 'RESONANCE', 'LIBRATION', 'BARYCENTER', 'HELIOPAUSE', 'BOW SHOCK', 'MAGNETOSPHERE', 'IONOSPHERE', 'TROPOSPHERE', 'STRATOSPHERE', 'MESOSPHERE', 'THERMOSPHERE', 'EXOSPHERE', 'ALBEDO', 'INSOLATION', 'IRRADIANCE', 'FLUX', 'LUMINOSITY', 'MAGNITUDE', 'PARALLAX', 'DOPPLER', 'REDSHIFT', 'BLUESHIFT', 'SPECTROSCOPY', 'PHOTOMETRY', 'POLARIMETRY', 'INTERFEROMETRY', 'ASTROMETRY', 'CELESTIAL', 'TERRESTRIAL', 'LUNAR', 'SOLAR', 'STELLAR', 'GALACTIC', 'COSMIC', 'NEBULAR', 'PLANETARY', 'ASTEROIDAL', 'COMETARY', 'METEORIC', 'ANALYSIS', 'COMPUTATION', 'ALGORITHM', 'HEURISTIC', 'STOCHASTIC', 'DETERMINISTIC', 'PROBABILISTIC', 'BAYESIAN', 'MARKOV', 'MONTE CARLO', 'FOURIER', 'LAPLACE', 'EULER', 'LAGRANGE', 'HAMILTON', 'NEWTON', 'EINSTEIN', 'PLANCK', 'BOHR', 'HEISENBERG', 'SCHRODINGER', 'DIRAC', 'FEYNMAN', 'HAWKING', 'PENROSE', 'GODEL', 'TURING', 'VON NEUMANN', 'SHANNON', 'WIENER', 'KALMAN', 'NYQUIST', 'BODE', 'NICHOLS', 'ROOT LOCUS', 'STATE SPACE', 'TRANSFER FUNCTION', 'FEEDBACK', 'FEEDFORWARD', 'PID', 'LQR', 'MPC', 'ADAPTIVE', 'ROBUST', 'NONLINEAR', 'OPTIMAL', 'STABILITY', 'CONTROLLABILITY', 'OBSERVABILITY', 'ESTIMATION', 'FILTERING', 'PREDICTION', 'SMOOTHING', 'DIAGNOSTICS', 'PROGNOSTICS', 'HEALTH MANAGEMENT', 'FAULT TOLERANCE', 'REDUNDANCY', 'RELIABILITY', 'AVAILABILITY', 'MAINTAINABILITY', 'SAFETY', 'SECURITY', 'INTEGRITY', 'CONFIDENTIALITY', 'AUTHENTICATION', 'AUTHORIZATION', 'ACCOUNTABILITY', 'NON-REPUDIATION', 'CRYPTOGRAPHY', 'ENCRYPTION', 'DECRYPTION', 'HASHING', 'SIGNATURE', 'CERTIFICATE', 'KEY MANAGEMENT', 'PROTOCOL', 'INTERFACE', 'STANDARD', 'SPECIFICATION', 'REQUIREMENT', 'DESIGN', 'IMPLEMENTATION', 'VERIFICATION', 'VALIDATION', 'INTEGRATION', 'TESTING', 'DEPLOYMENT', 'OPERATION', 'MAINTENANCE', 'DECOMMISSIONING', 'DISPOSAL', 'LUNA', 'ROT', 'DEKA', 'LNRT', 'DKA', 'SYS', 'AUTH', 'OK', 'ERR', 'WARN', 'INFO', 'DEBUG', 'TRACE'];
const barcodeSymbols = [(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.fillStyle = ink;
  const w = sz * (3 + prng() * 5); // longer
  const h = sz * (0.15 + prng() * 0.15); // smaller height
  const bars = 60 + prng() * 60 | 0;
  const bw = w / bars;
  let cx = x - w / 2;
  for (let i = 0; i < bars; i++) {
    if (prng() > 0.1) {
      const thick = bw * (1 + (prng() * 4 | 0));
      if (cx + thick > x + w / 2) break;
      c.fillRect(cx, y - h / 2, thick, h);
      cx += thick + bw * (0.2 + prng() * 0.8);
    } else {
      cx += bw * (1 + prng() * 3);
    }
    if (cx > x + w / 2) break;
  }
  if (prng() > 0.4) {
    c.font = `700 ${sz * 0.12}px 'Tiny5', sans-serif`;
    c.textAlign = 'center';
    c.textBaseline = 'top';
    c.fillText(`${prng() * 900000 | 0} ${prng() * 900000 | 0}`, x, y + h / 2 + sz * 0.04);
  }
}, (c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.fillStyle = ink;
  const w = sz * (4 + prng() * 6); // even longer
  const h = sz * (0.1 + prng() * 0.1); // smaller
  const bw = sz * (0.015 + prng() * 0.015);
  let cx = x - w / 2;
  while (cx < x + w / 2) {
    if (prng() > 0.1) {
      const thick = bw * (1 + (prng() * 5 | 0));
      if (cx + thick > x + w / 2) break;
      c.fillRect(cx, y - h / 2, thick, h);
      cx += thick + bw * (0.5 + prng() * 1.5);
    } else {
      cx += bw * (2 + prng() * 3);
    }
  }
}];
const asciiSymbols = [(c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `700 ${sz * 0.6}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(labels), x, y);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `400 ${sz * 0.4}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('┼┴┬┤', x, y - sz * 0.25);
  c.fillText('├┼┼┤', x, y);
  c.fillText('├┬┴┼', x, y + sz * 0.25);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `700 ${sz * 0.5}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(['\\_\\_\\', '///', '***', '+++', '|||']), x, y);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `700 ${sz * 0.4}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('██▓▒░', x, y - sz * 0.2);
  c.fillText('░▒▓██', x, y + sz * 0.2);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `400 ${sz * 0.3}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(pick(['LUNAROT.DK', 'LNRT.DK', 'LN.ROTDEKA', 'ROT']), x, y - sz * 0.3);
  c.fillText('0 1 1 0 1 0', x, y);
  c.fillText('L U N A R O T', x, y + sz * 0.3);
}];
const occultExtras = [(c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('⛤', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('⚕', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('♆', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('👁‍🗨', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('🜲', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .4}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('☽𖤐☾', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('⛧', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('𓃵', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('🜏', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('⛥⃝', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('𓁺', x, y + sz * .04);
}, (c, x, y, sz, ink, sw) => {
  c.fillStyle = ink;
  c.font = `${sz * .5}px 'Jacquard 12', system-ui`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('𓆙', x, y + sz * .04);
}];
const occultSymbols = [...curseSymbols, ...kabbalSymbols, ...eyeSymbols, ...horrorSymbols, ...dystopSymbols, ...occultExtras];
const makeVariants = (pool, count, cat) => {
  let res = [...pool];
  for (let base of pool) {
    for (let i = 1; i < count; i++) {
      res.push((c, x, y, sz, ink, sw, seed) => {
        let prng = mkRng(seed ? seed + i * 999 : i * 999);
        c.save();
        c.translate(x, y);
        let rot = 0;
        if (prng() > 0.5) rot = (prng() * 4 | 0) * (Math.PI / 2);
        if (cat !== 'ascii' && cat !== 'cert') c.rotate(rot);
        let s = 0.7 + prng() * 0.6;
        c.scale(s, s);
        base(c, 0, 0, sz, ink, sw * (0.5 + prng()), seed);
        c.restore();
        c.save();
        c.translate(x, y);
        c.strokeStyle = ink;
        c.fillStyle = ink;
        c.lineWidth = sw;
        let p = prng();
        if (cat === 'cyber' && p < 0.4) {
          c.font = `400 ${sz * .12}px 'Tiny5', sans-serif`;
          c.textAlign = 'center';
          c.textBaseline = 'middle';
          c.fillText(`V.${prng() * 99 | 0}`, 0, sz * 0.6);
          c.strokeRect(-sz * 0.5, -sz * 0.5, sz, sz);
        }
        if (cat === 'geo' && p < 0.4) {
          c.beginPath();
          c.arc(0, 0, sz * 0.55, 0, Math.PI * 2);
          c.stroke();
          if (prng() > 0.5) {
            c.beginPath();
            c.arc(0, 0, sz * 0.45, 0, Math.PI * 2);
            c.stroke();
          }
        }
        if (cat === 'occult' && p < 0.5) {
          c.font = `${sz * .3}px 'Jacquard 12', system-ui`;
          c.textAlign = 'center';
          c.textBaseline = 'middle';
          c.fillText(['👁', '⛧', '☽', '☾', '🜏'][prng() * 5 | 0], (prng() - 0.5) * sz, (prng() - 0.5) * sz);
        }
        if (cat === 'cert' && p < 0.4) {
          c.beginPath();
          c.arc(0, 0, sz * 0.5, 0, Math.PI * 2);
          c.stroke();
          c.font = `700 ${sz * .1}px 'Tiny5', sans-serif`;
          c.textAlign = 'center';
          c.textBaseline = 'middle';
          c.fillText(pick(labels), 0, -sz * 0.55);
        }
        if (cat === 'arrow' && p < 0.4) {
          c.beginPath();
          c.arc(0, 0, sz * 0.4, 0, Math.PI * 2);
          c.stroke();
        }
        if (cat === 'ascii' && p < 0.4) {
          c.font = `700 ${sz * .15}px 'Tiny5', sans-serif`;
          c.textAlign = 'center';
          c.textBaseline = 'middle';
          c.fillText(['[X]', '<0>', '---', '***'][prng() * 4 | 0], 0, sz * 0.55);
        }
        c.restore();
      });
    }
  }
  return res;
};
const textFormatSymbols = [(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  let txt = prng() > 0.5 ? pick(labels) : pick(labels) + ' ' + pick(labels);
  c.font = `400 ${sz * .15}px 'Tiny5', sans-serif`;
  let m = c.measureText(txt);
  c.fillStyle = prng() > 0.5 ? state.ac : state.third;
  c.fillRect(x - m.width / 2 - sz * .02, y - sz * .08, m.width + sz * .04, sz * .16);
  c.fillStyle = state.inverted ? state.ink : state.bg;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(txt, x, y);
}, (c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  let txt = prng() > 0.5 ? pick(labels) : pick(labels) + ' ERR ' + (Math.random() * 999 | 0);
  c.font = `700 ${sz * .12}px 'Tiny5', sans-serif`;
  c.fillStyle = ink;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(txt, x, y);
  let m = c.measureText(txt);
  c.strokeStyle = ink;
  c.lineWidth = sw * 1.5;
  c.beginPath();
  c.moveTo(x - m.width / 2, y);
  c.lineTo(x + m.width / 2, y);
  c.stroke();
}, (c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  let txt = pick(labels);
  c.font = `400 ${sz * .15}px 'Tiny5', sans-serif`;
  c.fillStyle = ink;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(txt, x, y);
  let m = c.measureText(txt);
  c.strokeStyle = prng() > 0.5 ? state.ac : state.third;
  c.lineWidth = sw * 3;
  c.lineCap = 'square';
  c.beginPath();
  c.moveTo(x - m.width / 2 - sz * .05, y - sz * .05 + (prng() - 0.5) * sz * .1);
  c.lineTo(x + m.width / 2 + sz * .05, y + sz * .05 + (prng() - 0.5) * sz * .1);
  c.stroke();
}, (c, x, y, sz, ink, sw, seed) => {
  let txt = pick(labels);
  c.font = `400 ${sz * .25}px 'Tiny5', sans-serif`;
  c.fillStyle = ink;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(txt, x, y);
}, (c, x, y, sz, ink, sw, seed) => {
  let txt = pick(labels);
  c.font = `400 ${sz * .2}px 'Tiny5', sans-serif`;
  c.fillStyle = ink;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText(txt, x, y);
}, (c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.font = `400 ${sz * .1}px 'Tiny5', sans-serif`;
  let lines = [pick(labels), pick(labels), pick(labels)];
  c.textAlign = 'left';
  c.textBaseline = 'middle';
  let lh = sz * .15;
  let startY = y - lh;
  lines.forEach((l, i) => {
    let m = c.measureText(l);
    if (prng() > 0.3) {
      c.fillStyle = prng() > 0.5 ? state.ac : state.third;
      c.fillRect(x - sz * .4 - sz * .02, startY + i * lh - sz * .05, m.width + sz * .04, sz * .1);
      c.fillStyle = state.inverted ? state.ink : state.bg;
    } else {
      c.fillStyle = ink;
    }
    c.fillText(l, x - sz * .4, startY + i * lh);
  });
}, (c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.font = `700 ${sz * .18}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillStyle = ink;
  let m = (prng() * 12 + 1 | 0).toString().padStart(2, '0');
  let d = (prng() * 28 + 1 | 0).toString().padStart(2, '0');
  let yr = prng() * 10 + 20 | 0;
  let prefixes = ['EXP', 'USE BY', 'SELL BY', 'BEST BEFORE'];
  c.fillText(`${prefixes[prng() * prefixes.length | 0]}`, x, y - sz * .1);
  c.fillText(`${m}/${d}/${yr}`, x, y + sz * .1);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .4, y - sz * .3, sz * .8, sz * .6);
}];

// --- DOUBLING GRAPHIC SETS ---

if (typeof certSymbols !== 'undefined') {
  certSymbols.push(...certSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof eyeSymbols !== 'undefined') {
  eyeSymbols.push(...eyeSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof kabbalSymbols !== 'undefined') {
  kabbalSymbols.push(...kabbalSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof arabicSymbols !== 'undefined') {
  arabicSymbols.push(...arabicSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof jpSymbols !== 'undefined') {
  jpSymbols.push(...jpSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof krSymbols !== 'undefined') {
  krSymbols.push(...krSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof curseSymbols !== 'undefined') {
  curseSymbols.push(...curseSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof cyberSymbols !== 'undefined') {
  cyberSymbols.push(...cyberSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof horrorSymbols !== 'undefined') {
  horrorSymbols.push(...horrorSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof geoSymbols !== 'undefined') {
  geoSymbols.push(...geoSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof arrowSymbols !== 'undefined') {
  arrowSymbols.push(...arrowSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof dystopSymbols !== 'undefined') {
  dystopSymbols.push(...dystopSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof barcodeSymbols !== 'undefined') {
  barcodeSymbols.push(...barcodeSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof asciiSymbols !== 'undefined') {
  asciiSymbols.push(...asciiSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof textFormatSymbols !== 'undefined') {
  textFormatSymbols.push(...textFormatSymbols.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}
if (typeof occultExtras !== 'undefined') {
  occultExtras.push(...occultExtras.map(f => (c, x, y, sz, ink, sw, seed) => {
    c.save();
    // Inner scale
    f(c, x, y, sz * 0.75, ink, sw, seed);
    c.restore();
    // Outer frame variation
    c.strokeStyle = ink;
    c.lineWidth = sw * 0.5;
    let prng = typeof mkRng !== 'undefined' ? mkRng((seed || 1234) + 99) : Math.random;
    let roll = typeof mkRng !== 'undefined' ? prng() : Math.random();
    if (roll < 0.33) {
      c.beginPath();
      c.arc(x, y, sz * 0.48, 0, Math.PI * 2);
      c.stroke();
    } else if (roll < 0.66) {
      c.strokeRect(x - sz * 0.48, y - sz * 0.48, sz * 0.96, sz * 0.96);
    } else {
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.38, y - sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.38, y + sz * 0.48);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y - sz * 0.48);
      c.lineTo(x - sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y - sz * 0.48);
      c.lineTo(x + sz * 0.48, y - sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x - sz * 0.48, y + sz * 0.48);
      c.lineTo(x - sz * 0.48, y + sz * 0.38);
      c.stroke();
      c.beginPath();
      c.moveTo(x + sz * 0.48, y + sz * 0.48);
      c.lineTo(x + sz * 0.48, y + sz * 0.38);
      c.stroke();
    }
  }));
}

// -----------------------------
const dataSymbols = [
// Graph: Bar Chart
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.fillStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x - sz * .4, y + sz * .4);
  c.lineTo(x + sz * .4, y + sz * .4);
  c.stroke(); // X axis
  c.beginPath();
  c.moveTo(x - sz * .4, y + sz * .4);
  c.lineTo(x - sz * .4, y - sz * .4);
  c.stroke(); // Y axis
  let w = sz * .8 / 5;
  for (let i = 0; i < 4; i++) {
    let h = (0.2 + prng() * 0.7) * sz * 0.8;
    c.fillRect(x - sz * .35 + i * w, y + sz * .4 - h, w * 0.7, h);
  }
},
// Scatter Plot (like Pioneer telemetry)
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.fillStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .45, y - sz * .3, sz * .9, sz * .6);
  // Grid lines
  c.lineWidth = sw * 0.3;
  for (let i = 1; i < 4; i++) {
    let gy = y - sz * .3 + i * (sz * .6 / 4);
    c.beginPath();
    c.moveTo(x - sz * .45, gy);
    c.lineTo(x + sz * .45, gy);
    c.stroke();
    let gx = x - sz * .45 + i * (sz * .9 / 4);
    c.beginPath();
    c.moveTo(gx, y - sz * .3);
    c.lineTo(gx, y + sz * .3);
    c.stroke();
  }
  // Dots (SNR)
  c.lineWidth = sw;
  for (let i = 0; i < 15; i++) {
    let px = x - sz * .4 + prng() * sz * .8;
    let py = y - sz * .25 + prng() * sz * .5;
    c.beginPath();
    c.arc(px, py, sz * .015, 0, Math.PI * 2);
    c.fill();
  }
  // Triangles (DL)
  for (let i = 0; i < 12; i++) {
    let px = x - sz * .4 + prng() * sz * .8;
    let py = y - sz * .25 + prng() * sz * .5;
    c.beginPath();
    c.moveTo(px, py - sz * .03);
    c.lineTo(px + sz * .03, py + sz * .02);
    c.lineTo(px - sz * .03, py + sz * .02);
    c.closePath();
    c.stroke();
  }
},
// Block Diagram (Telemetry configuration)
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.fillStyle = ink;
  c.lineWidth = sw;
  let bw = sz * 0.18;
  let bh = sz * 0.12;
  c.font = `400 ${sz * .07}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';

  // Simplify: Just a few connected boxes
  let b1x = x - sz * .2,
    b1y = y - sz * .15;
  let b2x = x + sz * .2,
    b2y = y - sz * .15;
  let b3x = x,
    b3y = y + sz * .15;
  c.strokeRect(b1x - bw / 2, b1y - bh / 2, bw, bh);
  c.strokeRect(b2x - bw / 2, b2y - bh / 2, bw, bh);
  c.strokeRect(b3x - bw / 2, b3y - bh / 2, bw, bh);
  c.fillText('RCV', b1x, b1y);
  c.fillText('SDA', b2x, b2y);
  c.fillText('TCP', b3x, b3y);

  // Connections
  c.beginPath();
  c.moveTo(b1x + bw / 2, b1y);
  c.lineTo(b2x - bw / 2, b2y);
  c.stroke(); // line
  c.beginPath();
  c.moveTo(b1x, b1y + bh / 2);
  c.lineTo(b1x, b3y);
  c.lineTo(b3x - bw / 2, b3y);
  c.stroke();
},
// Graph: Line Chart with points
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.fillStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.moveTo(x - sz * .4, y + sz * .4);
  c.lineTo(x + sz * .4, y + sz * .4);
  c.stroke(); // X axis
  c.beginPath();
  c.moveTo(x - sz * .4, y + sz * .4);
  c.lineTo(x - sz * .4, y - sz * .4);
  c.stroke(); // Y axis
  c.beginPath();
  let pts = [];
  for (let i = 0; i < 6; i++) {
    pts.push([x - sz * .35 + i * (sz * .75 / 5), y + sz * .4 - (0.1 + prng() * 0.8) * sz * .8]);
  }
  c.moveTo(pts[0][0], pts[0][1]);
  for (let i = 1; i < 6; i++) c.lineTo(pts[i][0], pts[i][1]);
  c.stroke();
  pts.forEach(p => {
    c.beginPath();
    c.arc(p[0], p[1], sz * .03, 0, Math.PI * 2);
    c.fill();
  });
},
// Data Ring (Telemetry)
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .4, 0, Math.PI * 2);
  c.stroke();
  for (let i = 0; i < 12; i++) {
    if (prng() > 0.3) {
      c.beginPath();
      c.arc(x, y, sz * .4, i * Math.PI / 6, (i + 0.8) * Math.PI / 6);
      c.stroke();
      c.beginPath();
      c.arc(x, y, sz * .35, i * Math.PI / 6, (i + 0.8) * Math.PI / 6);
      c.stroke();
    }
  }
  c.fillStyle = ink;
  c.font = `400 ${sz * .15}px 'Tiny5', sans-serif`;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText((prng() * 999 | 0).toString().padStart(3, '0'), x, y);
},
// Node Network
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.fillStyle = ink;
  c.lineWidth = sw * 0.5;
  let pts = [];
  for (let i = 0; i < 5; i++) {
    pts.push([x + (prng() - 0.5) * sz * .8, y + (prng() - 0.5) * sz * .8]);
  }
  for (let i = 0; i < pts.length; i++) {
    for (let j = i + 1; j < pts.length; j++) {
      if (prng() > 0.4) {
        c.beginPath();
        c.moveTo(pts[i][0], pts[i][1]);
        c.lineTo(pts[j][0], pts[j][1]);
        c.stroke();
      }
    }
  }
  pts.forEach(p => {
    c.beginPath();
    c.arc(p[0], p[1], sz * .06, 0, Math.PI * 2);
    c.fill();
  });
},
// Radar/Sonar Sweep
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.beginPath();
  c.arc(x, y, sz * .4, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.arc(x, y, sz * .2, 0, Math.PI * 2);
  c.stroke();
  c.beginPath();
  c.moveTo(x, y - sz * .4);
  c.lineTo(x, y + sz * .4);
  c.stroke();
  c.beginPath();
  c.moveTo(x - sz * .4, y);
  c.lineTo(x + sz * .4, y);
  c.stroke();
  c.fillStyle = ink;
  c.beginPath();
  c.moveTo(x, y);
  c.arc(x, y, sz * .4, 0, Math.PI / 3);
  c.lineTo(x, y);
  c.globalAlpha = 0.3;
  c.fill();
  c.globalAlpha = 1;
  for (let i = 0; i < 3; i++) {
    c.beginPath();
    c.arc(x + (prng() - 0.5) * sz * .6, y + (prng() - 0.5) * sz * .6, sz * .03, 0, Math.PI * 2);
    c.fill();
  }
},
// Signal waveform
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  c.strokeStyle = ink;
  c.lineWidth = sw;
  c.strokeRect(x - sz * .45, y - sz * .25, sz * .9, sz * .5);
  c.beginPath();
  let steps = 40;
  for (let i = 0; i <= steps; i++) {
    let cx = x - sz * .4 + i * (sz * .8 / steps);
    let cy = y + Math.sin(i * 0.4 + prng() * 10) * sz * .15 + (prng() - 0.5) * sz * .1;
    if (i === 0) c.moveTo(cx, cy);else c.lineTo(cx, cy);
  }
  c.stroke();
},
// Heatmap Grid
(c, x, y, sz, ink, sw, seed) => {
  let prng = mkRng(seed || 1234);
  let cells = 4;
  let cellW = sz * .8 / cells;
  c.fillStyle = ink;
  c.strokeStyle = ink;
  c.lineWidth = sw * 0.5;
  c.strokeRect(x - sz * .4, y - sz * .4, sz * .8, sz * .8);
  for (let r = 0; r < cells; r++) {
    for (let c2 = 0; c2 < cells; c2++) {
      let cx = x - sz * .4 + c2 * cellW;
      let cy = y - sz * .4 + r * cellW;
      c.globalAlpha = prng();
      c.fillRect(cx, cy, cellW, cellW);
    }
  }
  c.globalAlpha = 1;
}];
const unicodeSymbols = [...['✹', '✦', '✧', '✺', '❁', '❃', '⎈', '⌬', '⌖', '⌘', '◎', '◉', '◈', '▣', '▤', '▥', '▦', '▧', '▨', '▩', '◐', '◑', '◒', '◓', '◔', '◕', '◖', '◗', '◘', '◙', '◚', '◛', '◜', '◝', '◞', '◟', '◠', '◡', '◢', '◣', '◤', '◥', '◧', '◨', '◩', '◪', '◫', '◬', '◭', '◮', '☀', '☁', '☂', '☃', '☄', '★', '☆', '☇', '☈', '☉', '☊', '☋', '☌', '☍', '☎', '☏', '☐', '☑', '☒', '☓', '☔', '☕', '☖', '☗', '☘', '☙', '☚', '☛', '☜', '☝', '☞', '☟', '☠', '☡', '☢', '☣', '☤', '☥', '☦', '☧', '☨', '☩', '☪', '☫', '☬', '☭', '☮', '☯', '☰', '☱', '☲', '☳', '☴', '☵', '☶', '☷', '☸', '☹', '☺', '☻', '☼', '☽', '☾', '☿', '♀', '♁', '♂', '♃', '♄', '♅', '♆', '♇', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓', '♔', '♕', '♖', '♗', '♘', '♙', '♚', '♛', '♜', '♝', '♞', '♟', '♠', '♡', '♢', '♣', '♤', '♥', '♦', '♧', '♨', '♩', '♪', '♫', '♬', '♭', '♮', '♯', '♰', '♱'].map(char => (c, x, y, sz, ink, sw, seed) => {
  c.fillStyle = ink;
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.font = `${sz * .7}px sans-serif`;
  c.fillText(char, x, y);
})];
const setMap = {
  cert: certSymbols,
  cyber: cyberSymbols,
  geo: geoSymbols,
  arrow: arrowSymbols,
  occult: occultSymbols,
  ascii: asciiSymbols,
  text: textFormatSymbols,
  data: dataSymbols,
  unicode: unicodeSymbols
};
const expandedBarcodes = barcodeSymbols;
function createGenerativeSymbol(pools, seed, isBarcode) {
  return (c, x, y, sz, ink, sw, _s) => {
    let prng = mkRng(seed);
    c.save();
    c.translate(x, y);
    let layers = isBarcode ? 1 : 1 + (prng() * 2.5 | 0);
    for (let k = 0; k < layers; k++) {
      let poolObj = pools[prng() * pools.length | 0];
      let cat = poolObj.cat;
      let basePool = poolObj.symbols;
      let base = basePool[prng() * basePool.length | 0];
      c.save();
      let rot = 0;
      if (prng() > 0.3) rot = (prng() * 4 | 0) * (Math.PI / 2);
      if (cat !== 'ascii' && cat !== 'cert' && cat !== 'text' && cat !== 'data' && cat !== 'unicode' && !isBarcode) {
        if (prng() > 0.8) rot += prng() * Math.PI;
      } else if (cat === 'data' || cat === 'unicode') {
        rot = 0; // Never rotate data and unicode
      }
      if (!isBarcode) c.rotate(rot);
      let s = k === 0 ? 1.0 : 0.4 + prng() * 0.5;
      c.scale(s, s);
      if (k > 0 && prng() > 0.5 && !isBarcode) {
        c.translate((prng() - 0.5) * sz * 0.6, (prng() - 0.5) * sz * 0.6);
      }
      base(c, 0, 0, sz, ink, sw * (0.5 + prng() * 0.8), seed + k * 999);
      c.restore();
    }
    if (!isBarcode) {
      c.strokeStyle = ink;
      c.fillStyle = ink;
      c.lineWidth = sw;
      let p = prng();
      if (p < 0.1) {
        c.beginPath();
        c.arc(0, 0, sz * 0.55, 0, Math.PI * 2);
        c.stroke();
      } else if (p < 0.15) {
        c.strokeRect(-sz * 0.5, -sz * 0.5, sz, sz);
      } else if (p < 0.2) {
        c.font = `400 ${sz * .12}px 'Tiny5', sans-serif`;
        c.textAlign = 'center';
        c.textBaseline = 'middle';
        c.fillText(`V.${prng() * 99 | 0}`, 0, sz * 0.6);
      }
    }
    c.restore();
  };
}

// ── NOISE ──────────────────────────────────
let noiseCanvas = document.createElement('canvas');
noiseCanvas.width = 1;
noiseCanvas.height = 1;
let noiseCtx = noiseCanvas.getContext('2d');
function initNoise(W, H) {
  W = Math.floor(W);
  H = Math.floor(H);
  if (W === 0 || H === 0) return;
  noiseCanvas.width = W;
  noiseCanvas.height = H;
  const id = noiseCtx.createImageData(W, H);
  const d = id.data;
  for (let i = 0; i < d.length; i += 4) {
    const v = Math.random() * 255;
    d[i] = v;
    d[i + 1] = v;
    d[i + 2] = v;
    d[i + 3] = 12;
  }
  noiseCtx.putImageData(id, 0, 0);
}

// ── LAYOUT & PHYSICS ──────────────────────────────────
let scrollX = 0;
let scrollY = 0;
let isSnipping = false;
let snipStart = {
  x: 0,
  y: 0
};
let snipEnd = {
  x: 0,
  y: 0
};
let links = [];
function initLayout() {
  rng = mkRng(state.seed);
  particles = [];
  links = [];
  const W = cv.width / DPR;
  const H = cv.height / DPR;
  const baseRadius = Math.min(W, H) * 0.015;
  const counts = [3, 8, 21, 55, 89];
  const scales = [30.0, 15.0, 8.0, 4.0, 2.0]; // Expanded scaling for deeper complexity

  let nonOccultPool = [];
  Object.entries(setMap).forEach(([k, v]) => {
    if (k !== 'occult' && state.sets[k]) nonOccultPool.push({
      cat: k,
      symbols: v
    });
  });
  if (nonOccultPool.length === 0) nonOccultPool = [{
    cat: 'cert',
    symbols: certSymbols
  }];
  const marginX = W * 0.08;
  const marginY = H * 0.08;
  const innerW = W - marginX * 2;
  const innerH = H - marginY * 2;
  let totalParticles = counts.reduce((a, b) => a + b, 0); // 60
  let cols = Math.ceil(Math.sqrt(totalParticles * (innerW / innerH)));
  let rows = Math.ceil(totalParticles / cols);
  const cellW = innerW / cols;
  const cellH = innerH / rows;
  let gridPositions = [];
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      gridPositions.push({
        x: marginX + (c + 0.5) * cellW,
        y: marginY + (r + 0.5) * cellH
      });
    }
  }
  gridPositions.sort(() => rng() - 0.5);
  for (let i = 0; i < counts.length; i++) {
    for (let j = 0; j < counts[i]; j++) {
      let sym;
      let isBarcode = false;
      let seed = rng() * 999999 | 0;
      if (i === 0 && j < 2) {
        sym = createGenerativeSymbol([{
          cat: 'barcode',
          symbols: expandedBarcodes
        }], seed, true);
        isBarcode = true;
      } else {
        let pool = state.sets.occult && rng() < 0.33 ? [{
          cat: 'occult',
          symbols: occultSymbols
        }] : nonOccultPool;
        sym = createGenerativeSymbol(pool, seed, false);
      }
      const radius = baseRadius * scales[i];
      const roll = rng();
      const color = roll < 0.10 ? 'secret' : roll < 0.35 ? 'third' : roll < 0.60 ? 'ac' : 'ink';
      let pos = gridPositions.pop();
      if (!pos) pos = {
        x: marginX + rng() * innerW,
        y: marginY + rng() * innerH
      };
      particles.push({
        x: pos.x,
        y: pos.y,
        r: radius,
        sym: sym,
        colorKey: color,
        label: !isBarcode && rng() > 0.55 ? pick(labels) : null,
        isBarcode: isBarcode,
        seed: seed
      });
    }
  }
  let numLinks = Math.floor(particles.length * 0.7);
  for (let i = 0; i < numLinks; i++) {
    let a = rng() * particles.length | 0;
    let b = rng() * particles.length | 0;
    if (a !== b) links.push({
      a,
      b
    });
  }
  scrollX = 0;
  scrollY = 0;
  render();
}

// ── DRAW ──────────────────────────────────────────────
function drawParticles(targetCtx = ctx, isExport = false) {
  const W = cv.width / DPR;
  const H = cv.height / DPR;
  const bg = state.inverted ? state.ink : state.bg;
  const inkColor = state.inverted ? state.bg : state.ink;
  if (targetCtx === ctx) {
    targetCtx.clearRect(0, 0, W, H);
  }
  if (!isExport) {
    targetCtx.fillStyle = bg;
    targetCtx.fillRect(0, 0, targetCtx.canvas.width / DPR, targetCtx.canvas.height / DPR);
  }
  let offsetX = -scrollX;
  let offsetY = -scrollY;
  targetCtx.save();

  // Modulo wrap coordinate system (infinite scroll)
  const wrapX = x => ((x + offsetX) % W + W) % W;
  const wrapY = y => ((y + offsetY) % H + H) % H;
  targetCtx.save();
  targetCtx.lineWidth = state.sw * 0.3;
  targetCtx.globalAlpha = 0.4;
  targetCtx.setLineDash([state.sw, state.sw * 1.5]);
  for (let link of links) {
    let p1 = particles[link.a];
    let p2 = particles[link.b];
    if (p1 && p2) {
      let wx1 = wrapX(p1.x),
        wy1 = wrapY(p1.y);
      let wx2 = wrapX(p2.x),
        wy2 = wrapY(p2.y);
      let dist = Math.hypot(wx2 - wx1, wy2 - wy1);
      if (dist > W * 0.4) continue; // Prevent overwhelmingly long lines

      for (let k = 0; k < 3; k++) {
        let prng = mkRng(p1.seed + p2.seed + k);
        targetCtx.strokeStyle = prng() > 0.5 ? state.ac : inkColor;
        targetCtx.beginPath();
        targetCtx.moveTo(wx1 + (prng() - 0.5) * state.sw * 2, wy1 + (prng() - 0.5) * state.sw * 2);
        targetCtx.lineTo(wx2 + (prng() - 0.5) * state.sw * 2, wy2 + (prng() - 0.5) * state.sw * 2);
        targetCtx.stroke();
      }
    }
  }
  targetCtx.setLineDash([]);
  targetCtx.globalAlpha = 1;
  for (let p of particles) {
    let currentInk = p.colorKey === 'secret' ? state.secretColor : p.colorKey === 'ink' ? inkColor : state[p.colorKey];
    let wx = wrapX(p.x),
      wy = wrapY(p.y);
    targetCtx.save();
    try {
      p.sym(targetCtx, wx, wy, p.r * 0.85, currentInk, state.sw, p.seed);
    } catch (e) {}
    targetCtx.restore();
    if (p.label) {
      targetCtx.fillStyle = inkColor;
      targetCtx.globalAlpha = 0.2;
      targetCtx.font = `400 ${Math.max(5, p.r * 0.2)}px 'Tiny5', sans-serif`;
      targetCtx.textAlign = 'center';
      targetCtx.textBaseline = 'top';
      targetCtx.fillText(p.label, wx, wy + p.r * 0.8);
      targetCtx.globalAlpha = 1;
    }
  }
  targetCtx.restore();
  if (!isExport && targetCtx === ctx) {
    targetCtx.save();
    targetCtx.globalCompositeOperation = state.inverted ? 'screen' : 'multiply';
    if (noiseCanvas.width > 0 && noiseCanvas.height > 0) {
      targetCtx.drawImage(noiseCanvas, 0, 0);
    }
    targetCtx.restore();
  }
  if (isSnipping && !isExport && targetCtx === ctx) {
    targetCtx.globalCompositeOperation = 'difference';
    targetCtx.strokeStyle = '#fff';
    targetCtx.lineWidth = 1.5;
    targetCtx.setLineDash([6, 6]);
    targetCtx.strokeRect(snipStart.x, snipStart.y, snipEnd.x - snipStart.x, snipEnd.y - snipStart.y);
    targetCtx.setLineDash([]);
    targetCtx.globalCompositeOperation = 'source-over';
  }
  if (!isExport && targetCtx === ctx) {
    const seedTag = document.getElementById('seedTag');
    if (seedTag) seedTag.textContent = `SEED ${state.seed}`;
  }
}
let needsRender = true;
function renderLoop() {
  if (needsRender) {
    drawParticles(ctx, false);
    needsRender = false;
  }
  requestAnimationFrame(renderLoop);
}
requestAnimationFrame(renderLoop);
function render() {
  needsRender = true;
}

// ── TOUCH / MOUSE ─────────────────────────────────────
let tx0 = 0,
  ty0 = 0,
  tt0 = 0,
  holdT = null,
  holding = false,
  isPanning = false;
const STROKES = [0.6, 1.0, 1.5, 2.2, 3.2, 4.8];
cv.addEventListener('pointermove', e => {
  mouse.x = e.clientX;
  mouse.y = e.clientY;
  let rEl = document.getElementById('sring');
  if (rEl && rEl.style.opacity === '1') {
    let dx = e.clientX - tx0,
      dy = e.clientY - ty0;
    let a = Math.atan2(dy, dx);
    if (a < 0) a += Math.PI * 2;
    let seg = Math.floor(a / (Math.PI * 2) * STROKES.length) % STROKES.length;
    document.getElementById('swVal').innerText = STROKES[seg].toFixed(1);
    isSnipping = false;
    return;
  }
  if (holding) {
    let dx = e.clientX - tx0,
      dy = e.clientY - ty0;
    if (dx * dx + dy * dy > 64) {
      holding = false;
      clearTimeout(holdT);
    }
  }
  if (isPanning) {
    scrollX -= e.clientX - mouse.prevX;
    scrollY -= e.clientY - mouse.prevY;
    render();
  } else if (isSnipping) {
    snipEnd = {
      x: e.clientX,
      y: e.clientY
    };
    render();
  }
  mouse.prevX = e.clientX;
  mouse.prevY = e.clientY;
});
cv.addEventListener('wheel', e => {
  scrollX += e.deltaX;
  scrollY += e.deltaY;
  render();
}, {
  passive: true
});
cv.addEventListener('pointerleave', () => {
  mouse.x = -1000;
  mouse.y = -1000;
});
cv.addEventListener('pointerdown', e => {
  if (e.pointerType === 'mouse' && e.button !== 0) return;
  e.preventDefault();
  tx0 = e.clientX;
  ty0 = e.clientY;
  tt0 = Date.now();
  if (!e.target.closest('.set-btn, .pal-swatch, .corner-btn')) {
    holding = true;
    holdT = setTimeout(() => {
      if (!holding) return;
      let dx = e.clientX - tx0,
        dy = e.clientY - ty0;
      if (dx * dx + dy * dy > 64) return;
      let el = document.getElementById('sring');
      if (el) {
        el.style.left = tx0 + 'px';
        el.style.top = ty0 + 'px';
        el.style.opacity = 1;
      }
      isSnipping = false;
    }, 350);
    mouse.prevX = e.clientX;
    mouse.prevY = e.clientY;
    if (e.shiftKey) {
      isSnipping = true;
      snipStart = {
        x: e.clientX,
        y: e.clientY
      };
      snipEnd = {
        x: e.clientX,
        y: e.clientY
      };
    } else {
      isPanning = true;
    }
  }
});
function saveSnip(sx, sy, swidth, sheight) {
  const tempCanvas = document.createElement('canvas');
  tempCanvas.width = swidth * DPR;
  tempCanvas.height = sheight * DPR;
  const tempCtx = tempCanvas.getContext('2d');
  tempCtx.scale(DPR, DPR);
  tempCtx.translate(-sx, -sy);
  drawParticles(tempCtx, true);
  const a = document.createElement('a');
  a.download = `lunarot-snip-${state.seed}.png`;
  a.href = tempCanvas.toDataURL('image/png');
  a.click();
  flash();
}
cv.addEventListener('pointerup', e => {
  e.preventDefault();
  holding = false;
  isPanning = false;
  clearTimeout(holdT);
  let rEl = document.getElementById('sring');
  if (rEl && rEl.style.opacity === '1') {
    rEl.style.opacity = 0;
    let dx = e.clientX - tx0,
      dy = e.clientY - ty0;
    let a = Math.atan2(dy, dx);
    if (a < 0) a += Math.PI * 2;
    let seg = Math.floor(a / (Math.PI * 2) * STROKES.length) % STROKES.length;
    state.sw = STROKES[seg];
    document.getElementById('swVal').textContent = state.sw.toFixed(1);
    initLayout();
    flash();
    return;
  }
  let dx = Math.abs(e.clientX - tx0),
    dy = Math.abs(e.clientY - ty0),
    dt = Date.now() - tt0;
  if (isSnipping) {
    isSnipping = false;
    let w = Math.abs(snipEnd.x - snipStart.x);
    let h = Math.abs(snipEnd.y - snipStart.y);
    if (w > 10 && h > 10) {
      saveSnip(Math.min(snipStart.x, snipEnd.x), Math.min(snipStart.y, snipEnd.y), w, h);
      return;
    }
  }

  // It was just a click (panning didn't move much, snipping didn't drag much)
  if (dx < 14 && dy < 14 && dt < 280) {
    state.seed = Math.random() * 99999 | 0;
    state.secretColor = `hsl(${Math.random() * 360 | 0}, 100%, 60%)`;
    initLayout();
    flash();
  }
});
function flash() {
  const f = document.getElementById('flash');
  f.style.opacity = .12;
  setTimeout(() => f.style.opacity = 0, 100);
}

// ── SET BUTTONS ───────────────────────────────────────
document.getElementById('sets').addEventListener('click', e => {
  const btn = e.target.closest('.set-btn');
  if (!btn) return;
  const k = btn.dataset.set;
  const active = Object.values(state.sets).filter(Boolean).length;
  if (state.sets[k] && active <= 1) return;
  state.sets[k] = !state.sets[k];
  btn.classList.toggle('on', state.sets[k]);
  state.seed = Math.random() * 99999 | 0;
  initLayout();
});
function updateSetBtns() {
  document.querySelectorAll('.set-btn').forEach(b => b.classList.toggle('on', state.sets[b.dataset.set]));
}

// ── CORNER BUTTONS ────────────────────────────────────
document.getElementById('btnRegen').addEventListener('click', () => {
  state.seed = Math.random() * 99999 | 0;
  state.secretColor = `hsl(${Math.random() * 360 | 0}, 100%, 60%)`;
  initLayout();
  flash();
});
document.getElementById('btnInvert').addEventListener('click', () => {
  state.inverted = !state.inverted;
});
document.getElementById('btnExport').addEventListener('click', () => {
  state.exporting = true;
  drawParticles(ctx, true);
  const a = document.createElement('a');
  a.download = `lunarot-${state.seed}.png`;
  a.href = cv.toDataURL('image/png');
  a.click();
  state.exporting = false;
  drawParticles(ctx, false);
  flash();
});

// ── KEYBOARD ──────────────────────────────────────────
window.addEventListener('keydown', e => {
  if (e.code === 'Space') {
    state.seed = Math.random() * 99999 | 0;
    initLayout();
  }
  if (e.code === 'KeyI') {
    state.inverted = !state.inverted;
  }
});

// ── INIT ──────────────────────────────────────────────
function resize() {
  const W = window.innerWidth;
  const H = window.innerHeight;
  cv.style.width = W + 'px';
  cv.style.height = H + 'px';
  cv.width = W * DPR;
  cv.height = H * DPR;
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  initNoise(cv.width, cv.height);
  initLayout();
}
window.addEventListener('resize', () => setTimeout(resize, 80));
window.addEventListener('load', () => setTimeout(resize, 200));
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/sigil-generator/check.js", error: String((e && e.message) || e) }); }

__ds_ns.TarotCard = __ds_scope.TarotCard;

__ds_ns.Button = __ds_scope.Button;

__ds_ns.Panel = __ds_scope.Panel;

__ds_ns.HoverText = __ds_scope.HoverText;

__ds_ns.Typewriter = __ds_scope.Typewriter;

__ds_ns.Input = __ds_scope.Input;

__ds_ns.NavButton = __ds_scope.NavButton;

})();
