import os

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
target_file = os.path.join(root_dir, "style-guide.html")
public_file = os.path.join(root_dir, "public", "style-guide.html")

html_content = r"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LUNAROT // DEKA DESIGN SYSTEM & STYLE GUIDE v6.1</title>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600&family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Playfair+Display:ital,wght@0,500;0,700;1,400;1,600&family=Outfit:wght@300;400;500;700&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            cinzel: ['Cinzel', 'serif'],
            garamond: ['Cormorant Garamond', 'serif'],
            mono: ['JetBrains Mono', 'monospace'],
            playfair: ['Playfair Display', 'serif'],
            sans: ['Outfit', 'sans-serif']
          },
          colors: {
            gold: {
              DEFAULT: '#c8a45a',
              bright: '#e3b341',
              dim: '#8a6e34',
              glow: 'rgba(200, 164, 90, 0.4)'
            },
            parchment: '#cfc9c0',
            telemetry: '#838aa0',
            crimson: '#fb2c36',
            cyan: '#00d2ef'
          }
        }
      }
    }
  </script>

  <style>
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.6); }
    ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.2); border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(200, 164, 90, 0.5); }

    /* Gothic Panel Aesthetics */
    .gothic-panel {
      position: relative;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 1.5rem;
      transition: all 0.3s ease;
    }

    .gothic-panel::before {
      content: '';
      position: absolute;
      inset: 4px;
      border: 1px dashed rgba(255, 255, 255, 0.12);
      pointer-events: none;
    }

    .panel-gold {
      border-color: rgba(200, 164, 90, 0.45);
      box-shadow: 0 0 20px rgba(200, 164, 90, 0.08);
    }
    .panel-gold:hover {
      border-color: rgba(227, 179, 65, 0.8);
      box-shadow: 0 0 25px rgba(227, 179, 65, 0.2);
    }

    .panel-title-tag {
      position: absolute;
      top: -10px;
      left: 14px;
      background: #000;
      padding: 0 8px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 8px;
      font-weight: 700;
      color: #c8a45a;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      border: 1px solid rgba(200, 164, 90, 0.4);
    }

    .panel-footer-tag {
      position: absolute;
      bottom: -9px;
      right: 14px;
      background: #000;
      padding: 0 8px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 8px;
      color: rgba(255, 255, 255, 0.5);
      letter-spacing: 0.2em;
      text-transform: uppercase;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }

    /* Gothic Input Group */
    .gothic-input-field {
      width: 100%;
      background: transparent;
      border: none;
      border-bottom: 1px solid rgba(255, 255, 255, 0.25);
      color: #fff;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      padding: 8px 4px;
      outline: none;
      letter-spacing: 0.1em;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .gothic-input-field:focus {
      border-bottom-color: #c8a45a;
      box-shadow: 0 2px 8px rgba(200, 164, 90, 0.3);
    }

    /* Buttons */
    .gothic-btn-gold {
      background: rgba(200, 164, 90, 0.1);
      border: 1px solid rgba(200, 164, 90, 0.6);
      color: #c8a45a;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      padding: 10px 18px;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .gothic-btn-gold:hover {
      background: rgba(200, 164, 90, 0.25);
      border-color: #e3b341;
      color: #fff;
      box-shadow: 0 0 15px rgba(227, 179, 65, 0.4);
    }

    .gothic-btn-dark {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #cfc9c0;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      padding: 10px 18px;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .gothic-btn-dark:hover {
      background: rgba(255, 255, 255, 0.15);
      border-color: rgba(255, 255, 255, 0.6);
      color: #fff;
    }

    .gothic-btn-crimson {
      background: rgba(251, 44, 54, 0.1);
      border: 1px solid rgba(251, 44, 54, 0.5);
      color: #fb2c36;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      padding: 10px 18px;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .gothic-btn-crimson:hover {
      background: rgba(251, 44, 54, 0.3);
      border-color: #fb2c36;
      color: #fff;
      box-shadow: 0 0 15px rgba(251, 44, 54, 0.4);
    }

    /* Glow Text */
    .text-glow-gold {
      text-shadow: 0 0 10px rgba(200, 164, 90, 0.5);
    }
    .text-glow-white {
      text-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
    }
    .text-glow-crimson {
      text-shadow: 0 0 10px rgba(251, 44, 54, 0.6);
    }

    /* Code Toast Notification */
    #toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #000;
      border: 1px solid #c8a45a;
      color: #c8a45a;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      letter-spacing: 0.15em;
      padding: 10px 20px;
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.3s ease;
      pointer-events: none;
      z-index: 99999;
    }
    #toast.show {
      opacity: 1;
      transform: translateY(0);
    }
  </style>
</head>
<body class="bg-[#050505] text-[#cfc9c0] font-sans antialiased min-h-screen selection:bg-[#c8a45a] selection:text-black">

  <!-- Header Navigation -->
  <header class="sticky top-0 z-50 bg-black/80 backdrop-blur-md border-b border-white/15 px-6 py-4 flex flex-col sm:flex-row justify-between items-center gap-4">
    <div class="flex items-center gap-3">
      <span class="text-[#c8a45a] text-lg font-cinzel font-extrabold tracking-widest text-glow-gold">✦ LUNAROT</span>
      <span class="text-zinc-600 font-mono text-xs">//</span>
      <span class="text-white/80 font-mono text-xs tracking-widest uppercase">DESIGN SYSTEM & STYLE GUIDE</span>
      <span class="bg-white/10 text-[#c8a45a] font-mono text-[9px] px-2 py-0.5 border border-[#c8a45a]/30">v6.1</span>
    </div>
    <nav class="flex flex-wrap items-center gap-2 font-mono text-[10px] tracking-wider uppercase">
      <a href="#colors" class="px-3 py-1.5 border border-white/15 text-zinc-400 hover:text-white hover:border-[#c8a45a] transition-all">01. Colors</a>
      <a href="#typography" class="px-3 py-1.5 border border-white/15 text-zinc-400 hover:text-white hover:border-[#c8a45a] transition-all">02. Typography</a>
      <a href="#components" class="px-3 py-1.5 border border-white/15 text-zinc-400 hover:text-white hover:border-[#c8a45a] transition-all">03. Panels & Form</a>
      <a href="#buttons" class="px-3 py-1.5 border border-white/15 text-zinc-400 hover:text-white hover:border-[#c8a45a] transition-all">04. Buttons & Badges</a>
      <a href="#interactive" class="px-3 py-1.5 border border-white/15 text-zinc-400 hover:text-white hover:border-[#c8a45a] transition-all">05. Workbench</a>
    </nav>
  </header>

  <!-- Toast Notification -->
  <div id="toast">✓ COPIED TO CLIPBOARD</div>

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-16">

    <!-- Hero Header -->
    <section class="gothic-panel panel-gold space-y-4 text-center sm:text-left">
      <span class="panel-title-tag">SYSTEM_MANIFESTO // v6.1</span>
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <div>
          <h1 class="font-cinzel text-2xl sm:text-3xl font-extrabold text-white tracking-widest uppercase text-glow-white">LUNAROT OS AESTHETIC DESIGN SYSTEM</h1>
          <p class="font-garamond text-base sm:text-lg text-[#cfc9c0] mt-1 leading-relaxed">Canonical UI tokens, typographic scales, gothic glassmorphism frames, interactive state components, and alchemical color palettes for Lunarot & DEKA engines.</p>
        </div>
        <button onclick="copyCode(this, `/* LUNAROT AESTHETIC SYSTEM INTEGRATION */\n@import 'https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=JetBrains+Mono:wght@400;700&display=swap';`)" class="gothic-btn-gold shrink-0">
          [ COPY ALL TOKENS ]
        </button>
      </div>
      <span class="panel-footer-tag">ALCHEMICAL_FOUNDATION</span>
    </section>

    <!-- SECTION 01: COLORS -->
    <section id="colors" class="space-y-6">
      <div class="border-b border-white/15 pb-3 flex justify-between items-end">
        <div>
          <h2 class="font-cinzel text-xl font-bold text-white tracking-widest uppercase flex items-center gap-2">
            <span class="text-[#c8a45a]">✦</span> 01. COLOR PALETTE TOKENS
          </h2>
          <p class="font-mono text-xs text-zinc-500 mt-1">Click any color card to copy hex code directly to clipboard.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 font-mono">

        <!-- Gold Primary -->
        <div onclick="copyHex(this, '#c8a45a')" class="gothic-panel panel-gold group cursor-pointer hover:-translate-y-1 transition-all">
          <span class="panel-title-tag">GOLD_PRIMARY</span>
          <div class="h-24 w-full bg-[#c8a45a] rounded-none border border-white/20 shadow-[0_0_15px_rgba(200,164,90,0.4)] group-hover:scale-[1.02] transition-transform"></div>
          <div class="mt-4 space-y-1">
            <div class="text-xs font-bold text-white flex justify-between">
              <span>ALCHEMICAL GOLD</span>
              <span class="text-[#c8a45a]">#c8a45a</span>
            </div>
            <p class="text-[10px] text-zinc-400 font-sans">Primary brand accent, card stack borders, active highlights.</p>
          </div>
          <span class="panel-footer-tag">VAR(--GOLD)</span>
        </div>

        <!-- Gold Bright -->
        <div onclick="copyHex(this, '#e3b341')" class="gothic-panel panel-gold group cursor-pointer hover:-translate-y-1 transition-all">
          <span class="panel-title-tag">GOLD_BRIGHT</span>
          <div class="h-24 w-full bg-[#e3b341] rounded-none border border-white/20 shadow-[0_0_20px_rgba(227,179,65,0.6)] group-hover:scale-[1.02] transition-transform"></div>
          <div class="mt-4 space-y-1">
            <div class="text-xs font-bold text-white flex justify-between">
              <span>BRIGHT GLOW GOLD</span>
              <span class="text-[#e3b341]">#e3b341</span>
            </div>
            <p class="text-[10px] text-zinc-400 font-sans">Hover active glow, planetary focus state, primary buttons.</p>
          </div>
          <span class="panel-footer-tag">HEX: #E3B341</span>
        </div>

        <!-- Void Black -->
        <div onclick="copyHex(this, '#050505')" class="gothic-panel group cursor-pointer hover:-translate-y-1 transition-all">
          <span class="panel-title-tag">VOID_PITCH</span>
          <div class="h-24 w-full bg-[#050505] rounded-none border border-white/20 group-hover:scale-[1.02] transition-transform"></div>
          <div class="mt-4 space-y-1">
            <div class="text-xs font-bold text-white flex justify-between">
              <span>PITCH VOID BLACK</span>
              <span class="text-zinc-400">#050505</span>
            </div>
            <p class="text-[10px] text-zinc-400 font-sans">Background viewport base, glassmorphic backdrop overlay.</p>
          </div>
          <span class="panel-footer-tag">BACKGROUND_BASE</span>
        </div>

        <!-- Parchment Text -->
        <div onclick="copyHex(this, '#cfc9c0')" class="gothic-panel group cursor-pointer hover:-translate-y-1 transition-all">
          <span class="panel-title-tag">PARCHMENT</span>
          <div class="h-24 w-full bg-[#cfc9c0] rounded-none border border-white/20 group-hover:scale-[1.02] transition-transform"></div>
          <div class="mt-4 space-y-1">
            <div class="text-xs font-bold text-black flex justify-between">
              <span>PARCHMENT GREY</span>
              <span class="text-[#cfc9c0]">#cfc9c0</span>
            </div>
            <p class="text-[10px] text-zinc-400 font-sans">Markdown body text, prose descriptions, list content.</p>
          </div>
          <span class="panel-footer-tag">PROSE_TEXT</span>
        </div>

        <!-- Telemetry Slate -->
        <div onclick="copyHex(this, '#838aa0')" class="gothic-panel group cursor-pointer hover:-translate-y-1 transition-all">
          <span class="panel-title-tag">TELEMETRY</span>
          <div class="h-24 w-full bg-[#838aa0] rounded-none border border-white/20 group-hover:scale-[1.02] transition-transform"></div>
          <div class="mt-4 space-y-1">
            <div class="text-xs font-bold text-white flex justify-between">
              <span>TELEMETRY SLATE</span>
              <span class="text-[#838aa0]">#838aa0</span>
            </div>
            <p class="text-[10px] text-zinc-400 font-sans">Muted subtitles, header tags, system metadata captions.</p>
          </div>
          <span class="panel-footer-tag">SUBTITLE_MUTED</span>
        </div>

        <!-- Crimson Ritual -->
        <div onclick="copyHex(this, '#fb2c36')" class="gothic-panel group cursor-pointer hover:-translate-y-1 transition-all">
          <span class="panel-title-tag">CRIMSON</span>
          <div class="h-24 w-full bg-[#fb2c36] rounded-none border border-white/20 shadow-[0_0_15px_rgba(251,44,54,0.5)] group-hover:scale-[1.02] transition-transform"></div>
          <div class="mt-4 space-y-1">
            <div class="text-xs font-bold text-white flex justify-between">
              <span>CRIMSON RITUAL</span>
              <span class="text-[#fb2c36]">#fb2c36</span>
            </div>
            <p class="text-[10px] text-zinc-400 font-sans">Purge action buttons, warning banners, active scrobble highlights.</p>
          </div>
          <span class="panel-footer-tag">ACCENT_RITUAL</span>
        </div>

        <!-- Cyan Conflux -->
        <div onclick="copyHex(this, '#00d2ef')" class="gothic-panel group cursor-pointer hover:-translate-y-1 transition-all">
          <span class="panel-title-tag">CONFLUX_CYAN</span>
          <div class="h-24 w-full bg-[#00d2ef] rounded-none border border-white/20 shadow-[0_0_15px_rgba(0,210,239,0.5)] group-hover:scale-[1.02] transition-transform"></div>
          <div class="mt-4 space-y-1">
            <div class="text-xs font-bold text-white flex justify-between">
              <span>GATEWAY CYAN</span>
              <span class="text-[#00d2ef]">#00d2ef</span>
            </div>
            <p class="text-[10px] text-zinc-400 font-sans">Handshake conf, astral conduit indicators, link highlights.</p>
          </div>
          <span class="panel-footer-tag">GATEWAY_ACTIVE</span>
        </div>

        <!-- Pure White -->
        <div onclick="copyHex(this, '#ffffff')" class="gothic-panel group cursor-pointer hover:-translate-y-1 transition-all">
          <span class="panel-title-tag">PURE_WHITE</span>
          <div class="h-24 w-full bg-[#ffffff] rounded-none border border-white/20 group-hover:scale-[1.02] transition-transform"></div>
          <div class="mt-4 space-y-1">
            <div class="text-xs font-bold text-black flex justify-between">
              <span>PURE WHITE</span>
              <span class="text-zinc-300">#ffffff</span>
            </div>
            <p class="text-[10px] text-zinc-400 font-sans">Main headings, active tab highlights, top border lines.</p>
          </div>
          <span class="panel-footer-tag">HEADER_WHITE</span>
        </div>

      </div>
    </section>

    <!-- SECTION 02: TYPOGRAPHY -->
    <section id="typography" class="space-y-6">
      <div class="border-b border-white/15 pb-3 flex justify-between items-end">
        <div>
          <h2 class="font-cinzel text-xl font-bold text-white tracking-widest uppercase flex items-center gap-2">
            <span class="text-[#c8a45a]">✦</span> 02. TYPOGRAPHY SCALES
          </h2>
          <p class="font-mono text-xs text-zinc-500 mt-1">Cinzel for headings, Cormorant Garamond for prose, JetBrains Mono for system telemetry.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">

        <!-- Cinzel Serif Display -->
        <div class="gothic-panel panel-gold space-y-4">
          <span class="panel-title-tag">FONT_FAMILY // CINZEL</span>
          <div class="space-y-2 border-b border-white/10 pb-4">
            <span class="font-mono text-[9px] text-[#c8a45a] tracking-widest uppercase">.font-cinzel (Serif Display Header)</span>
            <h3 class="font-cinzel text-2xl font-bold text-white tracking-widest uppercase">LUNAROT ARCHIVAL VESSEL</h3>
            <h4 class="font-cinzel text-lg font-semibold text-[#c8a45a] tracking-wider uppercase">Chancellery of the Void // Geocentric Conflux</h4>
          </div>
          <div class="font-mono text-[10px] text-zinc-400 space-y-1">
            <p><strong class="text-white">Use Case:</strong> System titles, window headers, modal titles, front page brand mark.</p>
            <p><strong class="text-white">Tailwind Class:</strong> <code class="text-[#c8a45a]">font-cinzel tracking-widest uppercase</code></p>
          </div>
          <span class="panel-footer-tag">DISPLAY_SERIF</span>
        </div>

        <!-- Cormorant Garamond Prose -->
        <div class="gothic-panel panel-gold space-y-4">
          <span class="panel-title-tag">FONT_FAMILY // CORMORANT GARAMOND</span>
          <div class="space-y-2 border-b border-white/10 pb-4">
            <span class="font-mono text-[9px] text-[#c8a45a] tracking-widest uppercase">.font-garamond (Poetic Body Text)</span>
            <p class="font-garamond text-xl text-[#cfc9c0] leading-relaxed italic">
              "To let flame die its own death, relight itself. Amuse-bouche grey aftermath, undemanding void. For headfirst presence, smokelike, only to be enchanted by the pause."
            </p>
          </div>
          <div class="font-mono text-[10px] text-zinc-400 space-y-1">
            <p><strong class="text-white">Use Case:</strong> Markdown paragraphs, prose poetry, dev history logs, item descriptions.</p>
            <p><strong class="text-white">Tailwind Class:</strong> <code class="text-[#c8a45a]">font-garamond text-[#cfc9c0] leading-relaxed</code></p>
          </div>
          <span class="panel-footer-tag">PROSE_BODY</span>
        </div>

        <!-- JetBrains Mono Technical -->
        <div class="gothic-panel space-y-4">
          <span class="panel-title-tag">FONT_FAMILY // JETBRAINS MONO</span>
          <div class="space-y-2 border-b border-white/10 pb-4">
            <span class="font-mono text-[9px] text-zinc-400 tracking-widest uppercase">.font-mono (System Code & Telemetry)</span>
            <pre class="font-mono text-xs text-red-300 bg-white/5 border border-white/15 p-3 rounded-none overflow-x-auto leading-relaxed">
[0xAA99E1] SECURE NATAL DESCENT HANDSHAKE COMPLETE
VESSEL: FAIZ_YASAR | SUN: LEO (145.2°) | ASC: SCORPIO
TELEMETRY RESONANCE: 99.8% // STATUS: NOMINAL</pre>
          </div>
          <div class="font-mono text-[10px] text-zinc-400 space-y-1">
            <p><strong class="text-white">Use Case:</strong> Code blocks, bottom bar status text, badges, sidebar navigation, form inputs.</p>
            <p><strong class="text-white">Tailwind Class:</strong> <code class="text-[#c8a45a]">font-mono tracking-wider</code></p>
          </div>
          <span class="panel-footer-tag">SYSTEM_MONO</span>
        </div>

        <!-- Playfair Display Quote -->
        <div class="gothic-panel space-y-4">
          <span class="panel-title-tag">FONT_FAMILY // PLAYFAIR DISPLAY</span>
          <div class="space-y-2 border-b border-white/10 pb-4">
            <span class="font-mono text-[9px] text-zinc-400 tracking-widest uppercase">.font-playfair (Alchemical Epigraph)</span>
            <blockquote class="font-playfair text-lg text-white/90 italic border-l-2 border-[#c8a45a] pl-4 py-1">
              "As above, so below; as within, so without. The wheel turns through nineteen planetary aspects."
            </blockquote>
          </div>
          <div class="font-mono text-[10px] text-zinc-400 space-y-1">
            <p><strong class="text-white">Use Case:</strong> Blockquotes, alchemical epigraphs, tarot card interpretations.</p>
            <p><strong class="text-white">Tailwind Class:</strong> <code class="text-[#c8a45a]">font-playfair italic border-l-2 border-[#c8a45a]</code></p>
          </div>
          <span class="panel-footer-tag">EPIGRAPH_SERIF</span>
        </div>

      </div>
    </section>

    <!-- SECTION 03: PANELS & FORMS -->
    <section id="components" class="space-y-6">
      <div class="border-b border-white/15 pb-3 flex justify-between items-end">
        <div>
          <h2 class="font-cinzel text-xl font-bold text-white tracking-widest uppercase flex items-center gap-2">
            <span class="text-[#c8a45a]">✦</span> 03. GOTHIC PANELS & INPUT FIELDS
          </h2>
          <p class="font-mono text-xs text-zinc-500 mt-1">Glassmorphic containers with inner dashed borders, absolute tags, and sacred form groups.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 font-mono">

        <!-- Gold Gothic Panel Specimen -->
        <div class="gothic-panel panel-gold space-y-4">
          <span class="panel-title-tag">GOTHIC_PANEL // GOLD_FRAME</span>
          <h3 class="text-sm font-bold text-white uppercase tracking-widest">SACRED ALCHEMICAL CONTAINER</h3>
          <p class="text-xs font-garamond text-[#cfc9c0] leading-relaxed">
            Constructed using a dark translucent background (<code class="font-mono text-xs text-[#c8a45a]">bg-black/60</code>) with backdrop blur, a subtle gold border (<code class="font-mono text-xs text-[#c8a45a]">border-[#c8a45a]/45</code>), and a dashed inset ring (<code class="font-mono text-xs text-[#c8a45a]">border-dashed border-white/10</code>).
          </p>
          <div class="pt-2 border-t border-white/10 flex justify-between items-center text-[9px] text-zinc-400">
            <span>STATUS: NOMINAL</span>
            <button onclick="copyCode(this, `<div class=\&quot;gothic-panel panel-gold\&quot;>\n  <span class=\&quot;panel-title-tag\&quot;>TITLE_TAG</span>\n  <p>Content...</p>\n  <span class=\&quot;panel-footer-tag\&quot;>FOOTER_TAG</span>\n</div>`)" class="hover:text-white underline">
              [ COPY HTML ]
            </button>
          </div>
          <span class="panel-footer-tag">CONTAINER_SPECIMEN</span>
        </div>

        <!-- Form Elements -->
        <div class="gothic-panel space-y-5">
          <span class="panel-title-tag">FORM_GROUPS // INPUT_FIELDS</span>

          <div class="space-y-1">
            <label class="text-[9px] text-zinc-400 uppercase tracking-widest block">VESSEL NAME INGRESS</label>
            <input type="text" value="COGNITION_VESSEL" class="gothic-input-field" placeholder="Enter vessel name...">
          </div>

          <div class="space-y-1">
            <label class="text-[9px] text-zinc-400 uppercase tracking-widest block">JULIAN NATAL DATE (YYYY-MM-DD)</label>
            <input type="date" value="1999-08-11" class="gothic-input-field">
          </div>

          <div class="pt-2 border-t border-white/10 flex justify-between items-center text-[9px] text-zinc-400">
            <span>INPUT STYLING: UNDERLINE FOCUS GLOW</span>
            <button onclick="copyCode(this, `<input type=\&quot;text\&quot; class=\&quot;gothic-input-field\&quot; placeholder=\&quot;Input...\&quot;>`)" class="hover:text-white underline">
              [ COPY INPUT ]
            </button>
          </div>

          <span class="panel-footer-tag">SACRED_FORM</span>
        </div>

      </div>
    </section>

    <!-- SECTION 04: BUTTONS & BADGES -->
    <section id="buttons" class="space-y-6">
      <div class="border-b border-white/15 pb-3 flex justify-between items-end">
        <div>
          <h2 class="font-cinzel text-xl font-bold text-white tracking-widest uppercase flex items-center gap-2">
            <span class="text-[#c8a45a]">✦</span> 04. BUTTONS, BADGES & CHIPS
          </h2>
          <p class="font-mono text-xs text-zinc-500 mt-1">Interactive primary buttons, secondary shields, crimson purges, and telemetry badges.</p>
        </div>
      </div>

      <div class="gothic-panel panel-gold space-y-6">
        <span class="panel-title-tag">BUTTON_WORKSHOP & CHIPS</span>

        <!-- Button Row -->
        <div class="space-y-3">
          <span class="font-mono text-[9px] text-[#c8a45a] tracking-widest uppercase block">// BUTTON VARIANTS</span>
          <div class="flex flex-wrap items-center gap-4">
            <button class="gothic-btn-gold">[ INITIATE CONDUIT ]</button>
            <button class="gothic-btn-dark">[ RITUAL SHIELD ]</button>
            <button class="gothic-btn-crimson">[ PURGE VESSEL ]</button>
          </div>
        </div>

        <!-- Badges Row -->
        <div class="space-y-3 pt-4 border-t border-white/10">
          <span class="font-mono text-[9px] text-[#c8a45a] tracking-widest uppercase block">// TELEMETRY BADGES & CHIPS</span>
          <div class="flex flex-wrap items-center gap-3 font-mono text-[9px]">
            <span class="border border-[#c8a45a]/50 bg-[#c8a45a]/10 text-[#c8a45a] px-2.5 py-1 uppercase tracking-widest font-bold">[ OK ]</span>
            <span class="border border-white/20 bg-black/60 text-white px-2.5 py-1 uppercase tracking-widest">[ ONLINE ]</span>
            <span class="border border-red-500/40 bg-red-500/10 text-red-400 px-2.5 py-1 uppercase tracking-widest">[ SCROBBLED ]</span>
            <span class="border border-cyan-400/40 bg-cyan-400/10 text-cyan-300 px-2.5 py-1 uppercase tracking-widest">[ RE-LINKING ]</span>
            <span class="bg-white/10 text-zinc-300 px-2 py-0.5 rounded text-[8px] font-mono">BUILD v6.1</span>
          </div>
        </div>

        <span class="panel-footer-tag">INTERACTIVE_ELEMENTS</span>
      </div>
    </section>

    <!-- SECTION 05: INTERACTIVE WORKBENCH -->
    <section id="interactive" class="space-y-6">
      <div class="border-b border-white/15 pb-3 flex justify-between items-end">
        <div>
          <h2 class="font-cinzel text-xl font-bold text-white tracking-widest uppercase flex items-center gap-2">
            <span class="text-[#c8a45a]">✦</span> 05. LIVE INTERACTIVE WORKBENCH
          </h2>
          <p class="font-mono text-xs text-zinc-500 mt-1">Test live character hover rotators, font size scaling, and copy code snippets.</p>
        </div>
      </div>

      <div class="gothic-panel panel-gold space-y-6 font-mono">
        <span class="panel-title-tag">WORKBENCH // CHARACTER_ROTATOR</span>

        <div class="space-y-4">
          <div class="flex justify-between items-center text-xs">
            <span class="text-white font-bold">// HOVER OVER THE TEXT BELOW TO WATCH CHARACTERS ROTATE</span>
            <span id="charCount" class="text-[#c8a45a]">CHARACTERS: 124</span>
          </div>

          <div id="rotator" class="p-6 bg-black/80 border border-white/20 text-sm font-mono text-[#cfc9c0] leading-relaxed cursor-pointer selection:bg-white selection:text-black">
            LUNAROT ARCHIVAL VESSEL // CHANCELLERY OF THE VOID // ALCHEMICAL CONFLUX ENGINE // GEOCENTRIC NATAL MATRIX // 2026
          </div>
        </div>

        <span class="panel-footer-tag">LIVE_WORKBENCH</span>
      </div>
    </section>

  </main>

  <footer class="border-t border-white/15 py-8 text-center font-mono text-xs text-zinc-500 space-y-2">
    <p class="tracking-widest uppercase text-zinc-400">LUNAROT OS // DEKA DESIGN SYSTEM v6.1</p>
    <p class="text-[10px]">Standalone Single-File Style Guide Specification — 2026</p>
  </footer>

  <script>
    // Copy Hex Code
    function copyHex(el, hex) {
      navigator.clipboard.writeText(hex);
      showToast('✓ COPIED HEX: ' + hex);
    }

    // Copy Snippet Code
    function copyCode(btn, code) {
      navigator.clipboard.writeText(code);
      showToast('✓ SNIPPET COPIED');
    }

    // Toast Notification Handler
    function showToast(msg) {
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2000);
    }

    // Interactive Character Rotator
    const rotator = document.getElementById('rotator');
    const originalText = rotator.innerText;
    const chars = "✦✶✴✹★ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@$%&*";

    rotator.addEventListener('mousemove', () => {
      let scrambled = "";
      for (let i = 0; i < originalText.length; i++) {
        if (Math.random() < 0.25 && originalText[i] !== " ") {
          scrambled += chars[Math.floor(Math.random() * chars.length)];
        } else {
          scrambled += originalText[i];
        }
      }
      rotator.innerText = scrambled;
    });

    rotator.addEventListener('mouseleave', () => {
      rotator.innerText = originalText;
    });
  </script>
</body>
</html>
"""

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(public_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[SUCCESS] Generated standalone Style Guide HTML at {target_file} and {public_file}")
