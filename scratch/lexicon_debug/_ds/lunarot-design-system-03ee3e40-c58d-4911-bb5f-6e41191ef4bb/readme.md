# Lunarot Design System

Design system for **Lunarot** ("Lunarot DEKA" / "Lunarot Engine") — a fictional-corporate occult tech brand: a "stolen defunct 2000s witchcraft corporation" OS housing a family of divination toys (tarot, pachinko, a card catalog, an art showcase) styled after Web 1.0 Japanese horror/occult personal sites ("闇の工房" — Dark Workshop).

## Sources

This system was built by reading, in order:
- **`lunarot-design-system/`** (attached local codebase) — the canonical, currently-versioned token spec: `tokens.css`, `COMPONENTS.md` (state rules), `CHANGELOG.md`. This is the source of truth for color — it supersedes the gold-accented palette below.
- **`lunarot-os/`** (attached local codebase) — the OS shell (`src/App.tsx`, `src/components/OracleView.tsx`, `ShowcaseView.tsx`, `Effects.tsx`, `SmokyText.tsx`, etc.) plus five sub-projects merged under `projects/`: `Lunarot-Tarot` (Sacred Draw), `Lunarot-Directory` (Sacred Index, card catalog), `Lunarot-Pachinko` (Sacred Pachinko), `Lunarot-Ankoku` (research log on Japanese occult web culture, not a product UI), and a legacy `Lunarot-Tarot-old` build (source of the two occult webfonts).
- **[github.com/faizyasar/Lunarot-Tarot-Engine-1.0](https://github.com/faizyasar/Lunarot-Tarot-Engine-1.0)** — the standalone Sacred Draw repo (`src/App.tsx`, `src/components/*`, `src/types.ts` for the 32-card deck and zodiac copy banks, `src/index.css` for the legacy gold theme). This is the most complete single source for the tarot draw interaction and is worth exploring further for anyone extending this system — it has the full 3D shuffle/drag physics, ASCII-eyes background, and natal-chart canvas that this design system's UI kit only samples.

**Important — two conflicting palettes exist in the source material.** The legacy builds (`lunarot-os`, the GitHub repo, `Lunarot-Directory`/`Lunarot-Pachinko` READMEs) all use a warm gold accent (`#c8a45a`). But `lunarot-design-system/tokens.css` + `CHANGELOG.md` document a deliberate, versioned decision to retire gold entirely into a monochrome black/white system — the four gold-family tokens (`gold`, `gold-dim`, `cream`, `ember`) were audited and found to already all resolve to white, and were collapsed into one honest `--surface` token. **This design system follows that monochrome decision** (it is the newer, authoritative spec) — `COMPONENTS.md`'s state-mapping table was used to translate every legacy gold UI moment (card glow, reversed state, alerts) into its monochrome equivalent. If you want the old gold look back, it's fully documented in `CHANGELOG.md`.

## Products

- **Sacred Draw** (flagship, built out below as a UI kit) — natal-astrology-fused tarot: intake → boot handshake → 3-card draw (Antecedent/Concurrent/Consequent) → "Confluence" synthesis reading.
- **Lunarot Baseball** (built out below as a UI kit) — retro arcade baseball sim reskinned inside the same Lunarot OS shell (identical `◇ LUNAROT OS` header chrome). Source: `uploads/lunarot-baseball/`. Legacy gold theme translated to monochrome here too.
- **Sigil Generator** (built out below as a UI kit) — procedural symbol/glyph canvas tool for print ephemera. Source: `uploads/unified-lunarot-graphics/`. Its print-oriented 8-color palette was swapped to monochrome defaults (still user-editable) and its chrome restyled to match the rest of the OS.
- **Sefirot Codex** (built out below as a UI kit) — Tree of Life explorer + scholarly dossier on Kabbalistic symbolism. Source: `uploads/kabbalah-symbol-research-engine/`. Originally its own identity (amber-on-stone, Playfair Display/Plus Jakarta Sans/Fira Code, no Lunarot branding) — rebuilt here under the Lunarot OS header chrome with Cinzel/Cormorant Garamond/JetBrains Mono and the monochrome token set.
- **Sacred Index** (`Lunarot-Directory`) — card-catalog/database browser for the 32-card deck with astrological cross-references. Not yet built as a UI kit here — flag if you'd like it added.
- **Sacred Pachinko** (`Lunarot-Pachinko`) — physics pachinko board reskinned as divination. Not yet built as a UI kit here.
- **Art Showcase** — image carousel/gallery view (`BlurCarousel`, `InfiniteGallery`). Not yet built as a UI kit here.
- **Ankoku** — a research archive (not a product surface; documents 1990s–2000s Japanese occult personal sites for aesthetic reference).

## Index

- `styles.css` — import this one file; it pulls in every token/font below.
- `tokens/` — `colors.css`, `typography.css`, `spacing.css`, `effects.css` (motion + glow), `fonts.css` (`@font-face` + Google Fonts import).
- `components/` — `core/` (Button, Panel), `forms/` (Input), `navigation/` (NavButton), `cards/` (TarotCard), `effects/` (Typewriter, HoverText). See "Components" below.
- `guidelines/` — foundation specimen cards (colors, type, spacing, radius, motion, brand/logo) shown in the Design System tab.
- `ui_kits/sacred-draw/` — the Sacred Draw click-through recreation (logon → boot → draw → reading).
- `ui_kits/lunarot-baseball/` — the Lunarot Baseball click-through recreation (scoreboard, field, pitch-zone grid).
- `ui_kits/sigil-generator/` — the generative symbol-canvas tool, monochrome defaults.
- `ui_kits/sefirot-codex/` — the Tree of Life explorer + scholarly dossier, rebuilt under Lunarot OS chrome.
- `assets/` — `lunarot_logo.webp` (real brand mark), `fonts/onryou.woff2`, `fonts/ipaexm.woff2`.
- `SKILL.md` — portable skill file for use in Claude Code.

## Components

Intentional additions (no formal component library existed in the source; these are the recurring primitives extracted from the actual CSS/TSX patterns across `lunarot-os` and the tarot engine):
- **Button** (`components/core`) — primary/secondary/ghost, square-cornered, all-caps mono.
- **Panel** (`components/core`) — translucent bordered container with dashed inset + corner tag labels (`gothic-panel`).
- **Input** (`components/forms`) — mono label + right-aligned field, text/date/time/select.
- **NavButton** (`components/navigation`) — OS header-bar view switcher.
- **TarotCard** (`components/cards`) — the flagship divination card: sigil back, default/reversed/broken (Anomaly) states.
- **Typewriter** (`components/effects`) — "flame etch" typing effect with Arabic-glyph flicker on charged words.
- **HoverText** (`components/effects`) — per-character hover scale/rotate/glow.

## Content Fundamentals

**Voice**: second person, ritual/ceremonial register. The product talks to you as a "vessel," never a "user." Copy leans into portentous, slightly absurd corporate-occult fusion — the joke is that a witchcraft mainframe would talk like enterprise IT: *"SECURE NATAL DESCENT HANDSHAKE COMPLETE"*, *"INJECTING FAUSTIAN REGISTRY COOKIES UNSEALED"*, *"RE-ROUTING STREAM THROUGH KABBALISTIC GATEWAY."* System/telemetry copy is always shouty (`UPPERCASE`), hex-code-flavored, and mono-spaced; prose copy (readings, synthesis) is lowercase, literary, italic, and unhurried: *"The ritual has begun. Your birth coordinates are unsealed inside our cloud matrices."*

**Casing as a signal**: ALL CAPS + wide letter-spacing = machine/OS voice (labels, buttons, boot logs, nav). Sentence case + serif italics = the oracle's voice (readings, poetry). Don't mix them within one string.

**Tarot copy specifically** draws vocabulary from world mysticism broadly and eclectically — Sufi ("Fanaa · Sufi Annihilation"), Kabbalah ("Tikkun Olam", "Ein Sof"), Zoroastrian ("Ahura Mazda's Light"), alchemical glyphs (🜁🜂🜃🜄) — deliberately syncretic rather than tied to one tradition.

**Numbers/codes**: fake hex addresses (`0xCC0110`), version strings (`v5.18`), percentages, and countdown-style progress are used as pure atmosphere, not real data — always monospaced.

**Self-aware humor**: source READMEs end with a wink ("For me not for you :P"), and card names sit next to deadpan absurdity ("Strength" → "The Greater Jihad"). Don't sand this off; a completely straight-faced occult tone is not the brand.

**Emoji**: not used in-product. The one ⚠️ found in a boot log is closer to a terminal glyph than emoji and is rare even there — avoid emoji generally; use ◆ ✦ · as bullet/status glyphs instead.

## Visual Foundations

**Palette**: monochrome by policy (see Sources note above) — `--ink` #000 (page bg), `--ash` #080808 (panel bg), `--bone` #efede8 (warm off-white text/borders), `--surface` #fff (brightest layer — primary text, active fills, glow). No accent hue anywhere in chrome; state is expressed only via opacity ramps (`--surface-08` … `--surface-80`) or glow, never a new color. Color is reserved exclusively for imagery: card art, the showcase carousel, and the one full-color asset in the whole system — the painterly moth/wordmark logo.

**Type**: three families, strict roles. `Cinzel` (serif, all-caps, wide tracking) for ritual headers/titles only. `Cormorant Garamond` (serif, often italic) for all prose/poetry/readings — this is "the oracle's voice." `JetBrains Mono` for every piece of OS chrome: labels, buttons, nav, telemetry, boot logs — always uppercase, always letter-spaced 0.15–0.3em. A fourth, `Onryou`/`IPAexMincho` (local occult display faces, bundled in `assets/fonts/`), appears only for corrupted/cursed text moments — extremely sparing, never body copy.

**Spacing**: small and dense — an 4/8/12/16/24/32px scale (`--space-1` … `--space-8`), consistent with a "terminal readout" density rather than generous marketing whitespace.

**Backgrounds**: full-bleed black with a radial vignette (`radial-gradient(circle at 50% 50%, #080808, #000)`) — never flat. Ambient canvas layers (starfield, ASCII "eyes" tracking the cursor, procedural ASCII wave text) sit behind all UI at low opacity, always `pointer-events:none`. No photographic backgrounds; no repeating textures beyond a CRT scanline overlay used in one legacy boot screen.

**Animation — theatrical by default (updated direction)**: the brand's humor is Robert Eggers-adjacent — deadpan, unserious-culty, a haunted stage production playing it completely straight. That means motion should feel *staged*, not ambient: fast, punchy, a little too dramatic for what's actually happening. Every UI moment — tab switches, panel mounts, status-line changes, hover/press — gets a quick theatrical beat via the new fast set in `tokens/effects.css`: `--ease-theatrical` (snappy overshoot, "stage-hand yanked it"), `--ease-snap` (hard cut, no lead-up), durations `--dur-snap`(90ms)/`--dur-quick`(160ms)/`--dur-curtain`(240ms). Keyframes: `lunarot-snap-in` (scale/opacity pop-in, the default entrance for panels/cards/synthesis reveals), `lunarot-tab-punch` (quick squash on button/nav click), `lunarot-curtain-in`/`-out` (clip-path wipe for view/tab-in-tab-out transitions — think stage curtain, not a cross-fade), `lunarot-flicker-cut` (hard on/off/on flicker for status-line or state-label changes, like a marquee bulb). Keep it FAST — nothing here should run past ~250ms; the joke lands because it's brisk, not lingering.

The old slow/ritualistic set (`cubic-bezier(0.16,1,0.3,1)`, `--dur-fast/base/slow` 150/300/800ms, `lunarot-breathe`) is **not removed** — it's now reserved specifically for the oracle's own voice: the reading/synthesis typewriter text itself, and ambient background pulses (starfield, breathing dots). Anything the user *clicks or navigates* should feel theatrical-fast; anything the *oracle is speaking* keeps its slow, unhurried cadence. The "Anomaly" (broken-card) state keeps its own violent 220ms jitter + 2.5s burn-disintegrate sequence, now consistent with rather than an exception to the brand's faster tempo.

**Hover states**: brighten, don't recolor — borders and text step up the opacity ramp toward `--surface`, plus `--glow-surface` (a soft white box/text-shadow). Buttons additionally invert (white→black or vice versa) on hover.

**Press/active states**: same opacity-step logic; no scale/shrink transforms on buttons in the source (only card-hover microinteractions use transform).

**Borders**: hairline (1px), white at low opacity (`--surface-15` default, `--surface-40` for panels wanting more presence) or `--bone` for "white" panel variant. Square everywhere except cards.

**Corner radius**: `0` for all chrome (buttons, panels, inputs) — the brand is deliberately hard-edged/institutional. The single exception is the tarot card face/back: `8px`, because it's meant to read as a physical object, not UI.

**Cards (tarot)**: translucent black (`rgb(6 6 6 / 0.45)`) with `backdrop-filter: blur(3px)`, a bone-colored 1px border, soft white glow shadow, plus a second inset border 5–6px in for a "engraved plate" feel. Reversed = extra 180° roll, inverted contrast. Broken (Anomaly, ~12% draw odds) = grayscale jitter + stronger glow — never colored, per `COMPONENTS.md`.

**Transparency/blur**: `backdrop-filter: blur(2–3px)` on every panel and card so the ambient starfield/ASCII layers stay visible underneath — this is core to the "peering through a haunted terminal" feel, not decorative.

**Imagery color vibe**: the only full-color asset is the brand mark — a painterly moth/butterfly collage bleeding warm ochre, teal and dust-pink watercolor into the LUNAROT wordmark. Zodiac/planet glyphs in the natal chart canvas use soft pastel per-sign colors (see `guidelines/colors-zodiac.html`) but stay confined to that one chart layer.

## Iconography

No icon font, SVG icon set, or icon library exists in any source. The system uses **typographic/unicode glyphs as icons** throughout: ◆ ✦ · as bullets/status markers, alchemical symbols (🜁🜂🜃🜄) and planetary/zodiac glyphs (☉☽♂♀☿♃♄) as card and chart iconography, and a hand-drawn SVG "sigil" (concentric circles + cross lines) for card backs — recreated as inline SVG in `TarotCard.jsx` since it's simple vector geometry, not an icon asset. If a future UI kit needs a general-purpose icon (settings gear, close X, etc.), match this stroke-thin, geometric, unicode-adjacent style rather than importing a mismatched icon font.

## Fonts note

`Cinzel`, `Cormorant Garamond`, and `JetBrains Mono` are all pulled live from Google Fonts (matches the source exactly — same families, same weights). `Onryou` and `IPAexMincho` are the brand's own local occult display faces, copied in from `lunarot-os/projects/Lunarot-Tarot-old/fonts/` — no substitution was needed for any font.

## Caveats & ask

- Four UI kits so far: Sacred Draw, Lunarot Baseball, Sigil Generator, Sefirot Codex. Sacred Index, Sacred Pachinko, and Art Showcase all have real source code (`lunarot-os/src/components/merged/{directory,pachinko,art}/`) that I have **not** yet turned into UI kits — tell me which to build next.
- Sefirot Codex had no Lunarot branding in its source at all — I've folded it into the OS shell and monochrome palette on the assumption it's meant to join the family; say so if that's wrong and I'll keep it visually separate instead.
- Sigil Generator's 4-color palette now defaults to monochrome but stays fully user-editable (it's a print-asset tool, so free color choice is the point) — the original warm/blood/gold print palette is preserved in its own defaults if you want to switch back.
- No production icon set exists anywhere in the source; if you have one in mind (or want me to treat the unicode-glyph approach as final), let me know.
- The Sacred Draw UI kit simplifies the real product's 3D card-shuffle physics, draggable cards, and animated ASCII-eyes background to keep the demo compact — the full versions are in the GitHub repo if you want a more literal recreation.
- I followed `lunarot-design-system/tokens.css`'s monochrome decision over the older gold theme found everywhere else. If that's not what you want for new work, say so and I'll re-derive a gold-accent variant.

Tell me what to fix, add, or push further — happy to iterate until this feels exactly right.
