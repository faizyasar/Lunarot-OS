# Lunarot OS

UI of the Lunarot Ecosystem // Standalone Shell

---

## ✦ Core Design System

### 1. Harmony Colour Palette (HSL & Hex)
Custom alchemical colours defined in `src/index.css`:
- **Void** (`#000000`): Absolute black background container.
- **Ash** (`#080808`): Dark vignette ambient shadows.
- **Gold** (`#c8a45a`): Warm, elegant Elden-style gold for accents and glows.
- **Parchment** (`#efede8`): Cozy, bone-white lettering.
- **Cream** (`#ffffff`): High-contrast white tags.

### 2. Typography Classes
- **Cinzel** (`font-cinzel`): Serif headings for ritual headers and sacred titles.
- **Cormorant Garamond** (`font-garamond`): Prose style, optimised for body sentences and poetic descriptions.
- **JetBrains Mono** (`font-mono`): Retrogaming telemetry fonts for console codes, specs, and status grids.

### 3. Absolute Scaling Because I hate scrolling because scrolling is ugly and stupid (`--c-scale`)
To GUARANTEE that pages fit perfectly inside custom frames (like Carrd or custom viewports) without double scrollbars, the style sheet locks the dimensions of outer containers and automatically updates a scale factor (`--c-scale`) using CSS media queries:
```css
:root { --c-scale: 0.95; }
@media (max-width: 1023px) { :root { --c-scale: 0.72; } }
@media (max-height: 750px) { :root { --c-scale: 0.70; } }
```

---

## ✦ Standalone UI Components

All components are written in React and TypeScript under `src/components/`:

### 1. `Backgrounds`
Houses `StarsCanvas` (optimised Concentric Spoke radial coordinates matrix rendering at 30 FPS with pre-rendered sigils canvas) and `AsciiEyes` (30 FPS throttled ASCII eyes that blink and track pupil movement dynamically).

### 2. `ASCIIWaves`
A hypnotic backdrop of procedurally undulating math-driven ASCII waves representing energy streams from the void.

### 3. `OracleView`
The transitional gate for NATAL OS connection handshake procedures.

### 4. `ShowcaseView`
The aesthetic token specification guide and style dashboard cards.

### 5. `SmokyText`
An automated letter-by-letter typographic dispersion effect mimicking drifting smoke.

### 6. `VariableFontProximity`
Font weight warping proximity tracking where letters stretch and breathe based on mouse cursor distance.

### 7. `ViewStack`
A 3D-perspective stacked cards layout allowing cards to be dragged, tilted, and swiped off one by one.

---

For me not for you :P
