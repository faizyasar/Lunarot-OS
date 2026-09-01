# Changelog - Lunarot OS Ecosystem History

# ✦ DEV HISTORY CHRONICLES

# ✦ 2026

## 01/09
*   `[asset-pipeline]` Render and optimise 3D turntable GIF artefacts (`astral_pachinko_spinning.gif`, `cassette_spinning.gif`, `cd_jewel_case_spinning.gif`, `lunarot_tarot_deck_spinning.gif`) via headless Playwright capture.
*   `[docs]` Synchronise README and CHANGELOG with canonical standalone architecture, zero-build deployment definitions, and complete commit history.

## 22/08
*   `[lunarot-os:6da1a00]` feat: update standalone index.html with baked pachinko index and mobile gesture layer for tarot
*   `[lunarot-os:b7114ec]` fix(deploy): update index.html to latest standalone export and configure static zero-build deployment for Vercel
*   `[lunarot-os:bc8ac01]` fix(html): move fallback div from head noscript to body noscript for HTML standard compliance
*   `[lunarot-os:958b947]` Update index.html to standalone v0.191

## 07/08
*   `[lunarot-os:cb363e5]` feat: update index.html to v0.68 standalone build
*   `[lunarot-os:cf23b2c]` force: trigger fresh vercel deployment [v6.811]
*   `[lunarot-os:911fb45]` fix(loader): separate style and div in noscript tag and move div to body
*   `[lunarot-os:b850373]` feat: update index.html to v6.811 standalone

## 05/08
*   `[lunarot-os:f94b897]` fix: safely force vercel rebuild with UTF-8 comment
*   `[lunarot-os:9124eb6]` fix(loader): separate style and div in noscript tag and move div to body
*   `[lunarot-os:097418b]` revert: restore Lunarot OS v6.8 - Standalone.html from Desktop
*   `[lunarot-os:9eb4a20]` fix(loader): move noscript fallback div to body to prevent HTML parse error
*   `[lunarot-os:31e16ab]` feat: update index.html with Lunarot OS v6.8 - Standalone

## 04/08
*   `[lunarot-os:4ce1794]` chore: delete all extra HTML files
*   `[lunarot-os:97c9a0b]` feat(loader): apply index1.html loading screen UI design
*   `[lunarot-os:e12b717]` fix(loader): restore build 671342 title and original svg thumbnail in loading screen
*   `[lunarot-os:e708beb]` fix(loader): restore original clean unpacking loading screen
*   `[lunarot-os:dd810de]` revert: restore last working iteration of index.html
*   `[lunarot-os:aadfc80]` fix(build): move noscript tag from head to body to fix parse5 HTML build error
*   `[lunarot-os:534778e]` build(os): update index.html to build 671342 with occult loading animation

## 03/08
*   `[lunarot-os:96844ec]` revert: rollback index.html to stable backup while preserving favicons
*   `[lunarot-os:ae765a8]` fix: properly json-escape component injection for __bundler/template to resolve unpacking error
*   `[lunarot-os:a535268]` fix: correct component injection boundaries to prevent JS syntax error on boot
*   `[lunarot-os:372dfa0]` feat: redesign Sacred Pachinko dashboard into Steam Library layout with 3D mouse parallax
*   `[lunarot-os:960cdcf]` fix: update page titles to LUNAROT OS
*   `[lunarot-os:afefded]` fix: add cache-busting version query and icon fallback tags for Vercel favicon updates
*   `[lunarot-os:c874289]` feat: add custom favicons for Lunarot OS and Sacred Pachinko
*   `[lunarot-os:d113ed3]` fix: anchor right hand to right edge in Sacred Pachinko
*   `[lunarot-os:59dc911]` feat: integrate CRT video background into Sacred Pachinko
*   `[lunarot-os:aee5f27]` feat: update Lunarot OS to Build 671341

## 29/07
*   `[lunarot-os:4006ef0]` feat: add music conduit tab, boy harsher lastfm stats, letterboxd and pi.fyi links
*   `[lunarot-os:9b6d2de]` fix: place music.index and deka-archive.index under database, fix bottom bar faizyasar.life link

## 28/07
*   `[lunarot-os:0930e5c]` feat: group logs in D/M/Y format, restore sacred pachinko routes and database folders

## 26/07
*   `[lunarot-os:0.9.0]` Static serve routing for osLATEST.html and pachinkoLATEST.html

## 24/07
*   `[lunarot-os:0.5.0]` Integrated Sacred Pachinko 3 standalone build and single-file HTML bundler configuration

## 16/07
*   `[lunarot-os:5419300]` Update compiled lunarot-os.html bundle
*   `[lunarot-os:6f15070]` Standardise header nav tabs to use index.css .nav-btn classes
*   `[lunarot-os:ef68893]` Restore header nav selectors (tabs) and sync active card stack highlights
*   `[lunarot-os:c329e32]` Add standalone lunarot-os-2.html copy-paste template
*   `[lunarot-os:0bfa55a]` Optimise backgrounds rendering inside lunarot-os.html
*   `[lunarot-os:b75566a]` Update main README and submodules refs
*   `[lunarot-os:fc43333]` Update submodule references to optimised versions
*   `[lunarot-os:6b4d650]` Sync Lunarot OS with standalone shell updates
*   `[Lunarot-Directory:b916d0a]` Update README with humanised details
*   `[Lunarot-Directory:f34f636]` Optimise background rendering and add OS components
*   `[Lunarot-Pachinko:4952232]` Update README with humanised details
*   `[Lunarot-Pachinko:48ab910]` Optimise background rendering and add OS components
*   `[Lunarot-Tarot:cd0cb99]` Update README with humanised details
*   `[Lunarot-Tarot:ef84c65]` Optimise background rendering and add OS components

## 26/06
*   `[Lunarot-Directory:bf9b7d0]` docs: update metadata and README for alchemical style

## 25/06
*   `[Lunarot-Directory:4df590f]` feat: scaffold Lunarot Tarot application
*   `[Lunarot-Directory:6f5e4fb]` Initial commit

## 24/06
*   `[Lunarot-Ankoku:062bb3f]` Update README.md structure formatting
*   `[Lunarot-Ankoku:3386a82]` Edit README for improved readability and expression
*   `[Lunarot-Ankoku:1baf135]` initial research log
*   `[Lunarot-Pachinko:1d84b6c]` Using the same aesthetic as Lunarot Tarot Engine
*   `[Lunarot-Pachinko:6f4ea31]` Initial commit
*   `[Lunarot-Tarot-old:d4c82f7]` Add deprecation notice and point users to Lunarot-Tarot-Engine-1.0

## 23/06
*   `[Lunarot-Tarot-old:7c1080c]` Merge pull request #1 from faizyasar/copilot/make-repo-crawlable
*   `[Lunarot-Tarot-old:44eda96]` Enhance sitemap metadata
*   `[Lunarot-Tarot-old:f55c7ba]` Add crawlability metadata, robots, and sitemap

## 20/06
*   `[Lunarot-Tarot:afc11be]` chore: generate package-lock.json for project dependencies

## 19/06
*   `[Lunarot-Tarot:89e7f18]` Update README.md

## 17/06
*   `[Lunarot-Tarot:3797bef]` feat: add unsettling ASCII eye tracking system
*   `[Lunarot-Tarot:e09060f]` style: refine layout and visual aesthetic
*   `[Lunarot-Tarot:17b59fc]` feat: initialize Sacred Draw application
*   `[Lunarot-Tarot:728ca75]` Initial commit

## 16/06
*   `[Lunarot-Tarot-old:15dac69]` Update index.html
*   `[Lunarot-Tarot-old:a8c5117]` Update index.html
*   `[Lunarot-Tarot-old:455cac9]` Update index.html
*   `[Lunarot-Tarot-old:41ca5c2]` Update index.html