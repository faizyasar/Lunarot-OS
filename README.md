# Lunarot OS

UI of the Lunarot Ecosystem

---

## ✦ Core Design System

### 1. Harmony Color Palette (HSL & Hex)
Custom alchemical colors defined in `src/index.css`:
- **Void** (`#000000`): Absolute black background container.
- **Ash** (`#080808`): Dark vignette ambient shadows.
- **Gold** (`#c8a45a`): Warm, elegant Elden-style gold for accents and glows.
- **Parchment** (`#efede8`): Cozy, bone-white lettering.
- **Cream** (`#ffffff`): High-contrast white tags.

### 2. Typography Classes
- **Cinzel** (`font-cinzel`): Serif headings for ritual headers and sacred titles.
- **Cormorant Garamond** (`font-garamond`): Prose style, optimized for body sentences and poetic descriptions.
- **JetBrains Mono** (`font-mono`): Retrogaming telemetry fonts for console codes, specs, and status grids.

### 3. Absolute Scaling (`--c-scale`)
To guarantee that pages fit perfectly inside custom frames (like Carrd or custom viewports) without double scrollbars, the style sheet locks the dimensions of outer containers and automatically updates a scale factor (`--c-scale`) using CSS media queries:
```css
:root { --c-scale: 0.95; }
@media (max-width: 1023px) { :root { --c-scale: 0.72; } }
@media (max-height: 750px) { :root { --c-scale: 0.70; } }
```

---

## ✦ Isolated UI Components

All components are written in React and TypeScript under `src/components/`:

### 1. `HeaderNav`
A sleek, responsive top navigation bar styled with terminal-gothic border frames that handles view toggles.

### 2. `GothicPanel`
A glassmorphic layout panel that supports title/footer annotations, dark parchment overlays, custom outer borders, and a double-dashed inner border rim.

### 3. `GothicButton`
Customizable terminal styled buttons:
- **Primary (Light)**: High-contrast white background, bold text, border outline, hover white-glow.
- **Secondary (Dark)**: Glassmorphic gold border, dark backfill, hover scale and gold-glow.

### 4. `GothicInput` / `GothicDateInput` / `GothicTimeInput` / `GothicSelect`
Form controls styled to match the dark alchemical aesthetic. Includes a date alignment preview option with custom zodiac indicators.

### 5. `BootLoader`
A simulated retro-terminal progress bootloader. Perfect for transitional logins, unsealing animations, and boot delays. Accepts log strings, completion callbacks, and speed multipliers.

### 6. `FlameEtchedText`
An automated typewriter printer that analyzes sentences:
- Normal words print with standard typewriter delays.
- Charged words (e.g. wrapped in `*asterisks*` or custom lists) trigger Arabic ghost glyphs, flicker, and settle on a gold glow.

### 7. `InteractiveText`
Splits paragraphs into individual letter spans, applying a letter-by-letter hover zoom, rotation, and gold-color shift.

---

## ✦ Atmospheric Backgrounds

### 1. `AsciiBackgroundEyes`
A mathematical `<pre>` element rendering mouse-tracking ASCII pupils.
- **Mouse Idle**: Randomly glances at coordinate tags on the screen.
- **Lock Track**: Can target any element ID when custom events are triggered.
- **Crazy Mode**: Eyelids twitch spasmically and pupil characters morph into alchemical sigils for a set duration.

### 2. `StarBackground`
A WebGL/Canvas backdrop drawing radial concentric orbits, Sephirotic coordinate nodes, weight wires, and planetary coordinates drifting smoothly over time.

---

For me not for you :P
