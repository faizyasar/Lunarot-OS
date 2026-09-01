# Lunarot OS ✦ Canonical Ecosystem

> **One OS. One Pachinko. Pure Void.**

UI of the Lunarot Ecosystem // Standalone Shell & Production Pipeline

---

## ✦ Repository Architecture & System Overview

### Canonical Production Files
- **`index.html`**: Canonical production build of Lunarot OS (standalone single-file bundle with integrated tarot engine, baked pachinko index, and touch gesture layer).
- **`golem.html` & `golem_data.js`**: Interactive 3D golem visualizer subsystem with real-time transformation telemetry and model inspection.
- **`lexicon.html`**: Alchemical index and ecosystem terminology catalogue.
- **`vercel.json`**: Zero-build static routing configuration for high-performance edge deployment.
- **`package.json` & `vite.config.ts`**: Minimal build definitions for local single-file bundling and static serving.

### Rendered 3D Media Artefacts
- **`astral_pachinko_spinning.gif`**: Seamless 360-degree rotation capture of the Astral Pachinko cabinet.
- **`cassette_spinning.gif`**: Turntable rotation of the retro magnetic audio cassette.
- **`cd_jewel_case_spinning.gif`**: Optimised jewel case turntable animation with transparency support.
- **`lunarot_tarot_deck_spinning.gif`**: Full-orbit spinning render of the Lunarot gilded tarot deck.

---

## 📜 Full Version & Evolution Log

### Phase 1: Modular React/TypeScript Genesis
- Multi-component React application located in `src/` featuring `OracleView`, `ShowcaseView`, `ASCIIWaves`, `SmokyText`, `VariableFontProximity`, and `ViewStack`.
- Git submodules tracked under `projects/` (`Lunarot-Ankoku`, `Lunarot-Pachinko`, `Lunarot-Tarot`, `Lunarot-Directory`).
- Alchemical design system tokens defined in HSL/Hex (`#000000` Void, `#080808` Ash, `#c8a45a` Gold, `#efede8` Parchment).

### Phase 2: Standalone HTML Fragmentation & Iterations
- Created multiple single-file bundle exports for standalone hosting:
  - `lunarot-os.html`
  - `lunarot-os-2.html`
  - `lunarot-os-3.html`
  - `Sacred Pachinko (standalone) 1-3`
  - `Lunarot-OS-trimmed.html`
  - `Lunarot-OS-Standalone.html`
- Temporary redirection layers (`osLATEST.html` and `sacred-pachinko.html`).

### Phase 3: The Great Deletion & Consolidation
- **Deleted Obsolete Source Code**: Removed `src/`, `projects/` (submodules), `dumbsets/`, `dist/`, and legacy node artefacts.
- **Unlinked Submodules**: Completely removed `.gitmodules` and unlinked external repository references.
- **Cleaned Redirection Layers**: Removed intermediate redirect files to ensure direct root resolution.

### Phase 4: Direct OS54 Integration & Clean Vite Pipeline
- **Root Promotion**: Set `Lunarot-OS54.html` directly as the canonical root `index.html`.
- **Clean Build Pipeline**: Restored lightweight `package.json` and `vite.config.ts` (`vite-plugin-singlefile`) so Vercel builds natively without dependencies or mock scripts.
- **Permanent Change Tracking**: Added `CHANGELOG.md` to permanently record all ecosystem iterations and commit history.

### Phase 5: Standalone Monolith, 3D Subsystems & Asset Pipeline
- **Monolith Bundle**: Unified all application logic, CSS animations, and asset buffers directly into `index.html` (Builds v6.8, v0.68, v0.191, up to current canonical).
- **Mobile Gesture Layer**: Added dedicated swipe and touch event listeners for fluid card stack navigation on touch devices.
- **Baked Pachinko Index**: Integrated local pachinko engine logic directly into the primary payload to remove runtime network bottlenecks.
- **Zero-Build Edge Deployment**: Configured `vercel.json` with direct static directory routing (`outputDirectory: "."`).
- **3D Asset Capture Suite**: Added automated Playwright frame capture and colour-quantised GIF optimisation pipelines under `scratch/`.

---

## ✦ Core Design System

| Token | Hex | Role |
|---|---|---|
| **Void** | `#000000` | Absolute black background |
| **Ash** | `#080808` | Vignette ambient shadows |
| **Gold** | `#c8a45a` | Warm Elden-style alchemical gold |
| **Parchment** | `#efede8` | Bone-white body typography |
| **Cream** | `#ffffff` | High-contrast highlight tags |

---

*Lunarot Ecosystem // 2026*
