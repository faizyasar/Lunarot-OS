# Changelog - Lunarot OS Ecosystem History

All notable changes, deletions, and architecture shifts of Lunarot OS are logged here.

## [1.0.0-OS54] - 29/07/2026

### Added
- Promoted `Lunarot-OS54` directly as the canonical root `index.html`.
- Added `public/history.html` accessible live at `/history` for interactive in-browser ecosystem telemetry and changelog.
- Established clean, minimal Vite build pipeline (`package.json`, `vite.config.ts`, `vite-plugin-singlefile`) with zero extraneous dependencies.

### Changed
- Updated `vercel.json` with clean rewrites for `/pachinko`, `/sacred-pachinko`, and `/history`.
- Re-architected deployment pipeline for native 4.9s Vercel production compilation.

### Removed (The Great Deletion)
- **Deleted React Source Files**: Removed `src/` (including `App.tsx`, `components/`, `merged/` subcomponents).
- **Deleted Git Submodules**: Unlinked and removed `projects/` (`Lunarot-Ankoku`, `Lunarot-Pachinko`, `Lunarot-Tarot`, `Lunarot-Directory`) and `.gitmodules`.
- **Deleted Obsolete Standalone Exports**:
  - `lunarot-os.html`
  - `lunarot-os-2.html`
  - `lunarot-os-3.html`
  - `Lunarot-OS-Standalone.html`
  - `Lunarot-OS-trimmed.html`
  - `Sacred Pachinko (standalone) 1-3`
  - `dumbsets/` image bundles
- **Deleted Legacy Redirection Hacks**: Removed intermediate `osLATEST.html` and `sacred-pachinko.html` redirector files.

---

## [0.9.0] - 26/07/2026
### Added
- Static serve routing for `osLATEST.html` and `pachinkoLATEST.html`.

## [0.5.0] - 24/07/2026
### Added
- Integrated Sacred Pachinko 3 standalone build.
- Single-file HTML bundler configuration (`vite-plugin-singlefile`).

## [0.1.0] - 20/06/2026
### Added
- Initial modular React + TypeScript Lunarot OS template.
- Integrated alchemical color tokens (`#000000` Void, `#c8a45a` Gold) and typography classes.
