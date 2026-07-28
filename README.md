# Lunarot OS ✦ Canonical Ecosystem

> **One OS. One Pachinko. Pure Void.**

UI of the Lunarot Ecosystem // Standalone Shell & Production Pipeline

---

## ✦ Repository Architecture & Deletion History Log

### Current Canonical Production Architecture
- **`index.html`**: Canonical production build of Lunarot OS (Lunarot-OS54 standalone single-file bundle).
- **`pachinkoLATEST.html`**: Standalone production build of Sacred Pachinko (served live at `/pachinko` and `/sacred-pachinko`).
- **`public/history.html`**: Interactive web history log (served live at `/history`).
- **`vite.config.ts` & `package.json`**: Minimalist, clean Vite pipeline using `vite-plugin-singlefile` for instant Vercel deployments.

---

## 📜 Full Version & Deletion Log

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
- **Deleted Obsolete Source Code**: Removed `src/`, `projects/` (submodules), `dumbsets/`, `dist/`, and legacy node artifacts.
- **Unlinked Submodules**: Completely removed `.gitmodules` and unlinked external repository references.
- **Banished Redirection Hacks**: Deleted intermediate redirect files (`osLATEST.html`, `sacred-pachinko.html`).

### Phase 4: Direct OS54 Integration & Clean Vite Pipeline
- **Root Promotion**: Set `Lunarot-OS54.html` directly as the canonical root `index.html`.
- **Sacred Pachinko**: Retained `pachinkoLATEST.html` in `public/` and configured Vercel clean rewrites.
- **Clean Build Pipeline**: Restored lightweight `package.json` and `vite.config.ts` (`vite-plugin-singlefile`) so Vercel builds natively without dependencies or mock scripts.
- **Website History**: Added `/history` (`public/history.html`) and `CHANGELOG.md` to permanently record all ecosystem iterations.

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
