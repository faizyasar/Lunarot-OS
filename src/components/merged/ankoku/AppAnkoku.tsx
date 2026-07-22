import React, { useState, useEffect } from 'react';

const DRIVE_IMAGES = [
  { id: '1fr0zV3u5Uz3n3BGFrkVwYoJD9i8V8BzY', name: 'IMG_20210213_112550.png' },
  { id: '1hPpSYVk7Bf5GzChxmQr6M5rBKBuPVER6', name: 'IMG_20210217_134921.png' },
  { id: '1HQfGDW1tDpfD1Vm_fEPp7sL5pe74_dpQ', name: 'IMG_20210911_203447.png' },
  { id: '1HcSgmzOfdbaoCHuBo-C777BUyqCXtBsJ', name: 'IMG_20210925_115602.png' },
  { id: '1I8GgunARUjmliAn_K9K3nBspcn2DL-3E', name: 'IMG_20210925_115825.png' },
  { id: '1IqwFeBUStx0846Oohcoh8MtP2YHxV_Se', name: 'IMG_20210925_121359.png' },
  { id: '1ISRGHggtlcn-vEntswpZW9FXApDPEz87', name: 'Hasselhoff.png' }
];

const SITES_LOG = `# Sites Log (Ankoku Research)

Running record of Japanese personal websites (個人サイト) from the late 1990s through mid-2000s, focused on occult, horror, and material sharing.

---

## 暗黒工房 (Ankoku Koubou)
* **URL:** http://www.ankokukoubou.com/
* **Status:** ✅ Alive  -  last logged update 2018/5/9
* **Founded:** 1998
* **Author:** maki
* **What it is:** The anchor site. A horror-themed Japanese web resource hub  -  original material (wallpapers, images, fonts), horror games, a tarot divination page, ghost-photo collections, a "scary stories" section. Runs an original Japanese horror font called 「悪夢」("Akumu" / Nightmare). Copyright line reads "all right reserved 1998-2007 maki" but the site itself postdates that, still updating into 2018.
* **Notable:** Has a curating link page (/etc/link/link.htm) that is the gateway to most of this list.

---

## Ghost Tail
* **URL:** http://www.ghosttail.com/
* **Status:** ✅ Alive  -  last logged content update 2015
* **Author:** zen
* **What it is:** Horror material and ghost-story site ("z" branding). Sections for material, horror reading ("JuJu"), horror games, links, usage rules, and an original goods shop. Had a LINE sticker shop tie-in by 2015.
* **Notable:** Has an extensive, categorized link page (occult, fortune-telling, sound effects, web design/CSS tutorials, JS/CGI tutorials)  -  mapping the entire early tech scene.
* **Sub-site:** art.ghosttail.com ("OUT OF THE BOX")  -  high-res horror photo wallpapers.

---

## マイタロウ (Madtaro)
* **Original URL:** http://madtaro.net/ → redirected
* **Current URL:** https://madtaro.x0.com/
* **Status:** ✅ Alive and actively updating (confirmed posts from 2026)
* **Founded:** 1998.7.18
* **What it is:** Solo-author original horror fiction site. Sections for stories, a "monologue" diary, site history, escape-room games, a BBS, and original theme music composed by "MACROGUN." Also running a webcomic adaptation project (「東京区13」).
* **Notable:** Nearly 28 years of continuous operation under one author. One of the strongest "unbroken personal site" examples found.

---

## 9612. (read as "Kreuz")
* **URL:** http://skr.s7.xrea.com/
* **Status:** 🟡 Dormant since 2019, but still standing/served
* **Author:** REITO
* **Founded:** May 2000 (under the name 透明な血 / "Transparent Blood")
* **History:**
  - 2000/05/25  -  started as "透明な血" (Transparent Blood)
  - 2001/05/22  -  closed temporarily due to hospitalization
  - 2001/08/14  -  reopened, renamed "Nervenfaser"
  - 2002/01/10  -  renamed again to final form, "9612."
* **What it is:** Free downloadable web material site (images for web design use)  -  self-described as limited to black/white/gray/red, "dark, maybe empty-systematic" in tone.
* **Notable:** Featured in a 2003 print magazine, "ホームページ激裏大全" (Underground Homepage Compendium). Read aloud as "Kreuz" (German for "cross")  -  visible in folder names.
* **Open thread:** A site at https://kngktk.stars.ne.jp/ has been suggested as REITO's current/another site  -  blocked by robots.txt from automated access, unverified.

---

## TO CHECK NEXT
* 闇恭 (barakyo.com)  -  dark material site
* Caverns Of Blood (cavernsofblood.com)  -  English-language sister site, sound/MIDI/horror fonts
* Blue Moon (blue-moon.sblo.jp)  -  heavy-metal-themed material site with custom BGM
* SILVER EMBLEM (silveremblem.sakura.ne.jp)  -  design credited to "ERIS"
* HANGED MAN (fumio.sugoihp.com)  -  wide range of material under one author
* K.LUV DEPTH GENESIS (kluv-depth.com/hyper/)  -  described by curator as "weird but good"
`;

const LINK_WEB_MAP = `# Link Web Map

How these sites actually found each other. This is the peer-to-peer social structure of hand-curated link pages that defined early web rings. All links are now clickable.

---

## The Core Chain

*   **[ankokukoubou.com](http://www.ankokukoubou.com/)** (1998, maki)
    *   └─ \`/etc/link/link.htm\` → curated link hub, 4 sub-pages
        *   └─ \`link01.htm\` → "Horror Links" page
            *   ├─ **[madtaro.net](https://madtaro.x0.com/)** (1998 → redirected to [madtaro.x0.com](https://madtaro.x0.com/))
            *   ├─ **[ghosttail.com](http://www.ghosttail.com/)** (zen)
            *   ├─ **[gigas.press.ne.jp](https://web.archive.org/web/20041014022830/http://gigas.press.ne.jp/)** (怨み念法)
            *   ├─ **[neckdoll.jp](https://neckdoll.zombie.jp/)** (人形堂  -  active mirror)
            *   ├─ **[geocities.jp/evil666ring/](https://web.archive.org/web/20040608221532/http://www.geocities.jp:80/evil666ring/)** (THE EVIL DESIGN)
            *   ├─ **[yzero.com](https://web.archive.org/web/20041010072559/http://www.yzero.com/)** (0-zero-)
            *   └─ **[geocities.jp/cyberangelo666/](https://web.archive.org/web/20041014163412/http://www.geocities.jp/cyberangelo666/)** (cyber angelo)

*   **[ghosttail.com](http://www.ghosttail.com/)** (zen)
    *   └─ \`/link/index.html\` → large categorized link page
        *   ├─ **Dark art / material** → **[barakyo.com](https://web.archive.org/web/20040822005018/http://www.barakyo.com/)**, **[cavernsofblood.com](https://web.archive.org/web/20041204085448/http://www.cavernsofblood.com/)**, **[blue-moon.sblo.jp](http://blue-moon.sblo.jp/)**, **[silveremblem.sakura.ne.jp](http://silveremblem.sakura.ne.jp/)**, **[skr.s7.xrea.com](http://skr.s7.xrea.com/)** (9612.), **[fumio.sugoihp.com](https://web.archive.org/web/20040803023223/http://fumio.sugoihp.com/)**
        *   ├─ **Occult / ghost stories** → dozens of horror-story and ghost-photo sites
        *   ├─ **Fonts** → links back to **[ankokukoubou.com/font/](http://www.ankokukoubou.com/font/)** directly
        *   └─ **Web design / CSS / JS tutorials** → the actual technical "syllabus" creators used to learn HTML/CSS/JS (**[tagindex.com](https://www.tagindex.com/)**, **[kent-web.com](https://www.kent-web.com/)**, **[htmq.com](https://www.htmq.com/)**, etc.)

---

## Next Steps
- Map Ghost Tail's full link page systematically (currently only spot-checked)
- Cross-reference which sites appear on multiple hub pages (the most central nodes)
- Check whether any of these maintain active webring badges or scripts
`;

const DEV_HISTORY = `# Development History & Vibecoding Log

A forensic trace of the Lunarot Conflux OS engine compilation, extracted directly from local repository commits, combined with the ecosystem development log.

---

## ✦ Git Repository Commits Trace

*   **2026-07-16**  -  \`[lunarot-os:5419300]\` Update compiled lunarot-os.html bundle
*   **2026-07-16**  -  \`[lunarot-os:6f15070]\` Standardize header nav tabs to use index.css .nav-btn classes
*   **2026-07-16**  -  \`[lunarot-os:ef68893]\` Restore header nav selectors (tabs) and sync active card stack highlights
*   **2026-07-16**  -  \`[lunarot-os:c329e32]\` Add standalone lunarot-os-2.html copy-paste template
*   **2026-07-16**  -  \`[lunarot-os:0bfa55a]\` Optimise backgrounds rendering inside lunarot-os.html
*   **2026-07-16**  -  \`[lunarot-os:b75566a]\` Update main README and submodules refs
*   **2026-07-16**  -  \`[lunarot-os:fc43333]\` Update submodule references to optimised versions
*   **2026-07-16**  -  \`[lunarot-os:6b4d650]\` Sync Lunarot OS with standalone shell updates
*   **2026-07-16**  -  \`[Lunarot-Directory:b916d0a]\` Update README with humanised details
*   **2026-07-16**  -  \`[Lunarot-Directory:f34f636]\` Optimise background rendering and add OS components
*   **2026-07-16**  -  \`[Lunarot-Pachinko:4952232]\` Update README with humanised details
*   **2026-07-16**  -  \`[Lunarot-Pachinko:48ab910]\` Optimise background rendering and add OS components
*   **2026-07-16**  -  \`[Lunarot-Tarot:cd0cb99]\` Update README with humanised details
*   **2026-07-16**  -  \`[Lunarot-Tarot:ef84c65]\` Optimise background rendering and add OS components
*   **2026-06-26**  -  \`[Lunarot-Directory:bf9b7d0]\` docs: update metadata and README for alchemical style
*   **2026-06-25**  -  \`[Lunarot-Directory:4df590f]\` feat: scaffold Lunarot Tarot application
*   **2026-06-25**  -  \`[Lunarot-Directory:6f5e4fb]\` Initial commit
*   **2026-06-24**  -  \`[Lunarot-Ankoku:062bb3f]\` Update README.md structure formatting
*   **2026-06-24**  -  \`[Lunarot-Ankoku:3386a82]\` Edit README for improved readability and expression
*   **2026-06-24**  -  \`[Lunarot-Ankoku:1baf135]\` initial research log
*   **2026-06-24**  -  \`[Lunarot-Pachinko:1d84b6c]\` Using the same aesthetic as Lunarot Tarot Engine
*   **2026-06-24**  -  \`[Lunarot-Pachinko:6f4ea31]\` Initial commit
*   **2026-06-24**  -  \`[Lunarot-Tarot-old:d4c82f7]\` Add deprecation notice and point users to Lunarot-Tarot-Engine-1.0
*   **2026-06-23**  -  \`[Lunarot-Tarot-old:7c1080c]\` Merge pull request #1 from faizyasar/copilot/make-repo-crawlable
*   **2026-06-23**  -  \`[Lunarot-Tarot-old:44eda96]\` Enhance sitemap metadata
*   **2026-06-23**  -  \`[Lunarot-Tarot-old:f55c7ba]\` Add crawlability metadata, robots, and sitemap
*   **2026-06-20**  -  \`[Lunarot-Tarot:afc11be]\` chore: generate package-lock.json for project dependencies
*   **2026-06-19**  -  \`[Lunarot-Tarot:89e7f18]\` Update README.md
*   **2026-06-17**  -  \`[Lunarot-Tarot:3797bef]\` feat: add unsettling ASCII eye tracking system
*   **2026-06-17**  -  \`[Lunarot-Tarot:e09060f]\` style: refine layout and visual aesthetic
*   **2026-06-17**  -  \`[Lunarot-Tarot:17b59fc]\` feat: initialize Sacred Draw application
*   **2026-06-17**  -  \`[Lunarot-Tarot:728ca75]\` Initial commit
*   **2026-06-16**  -  \`[Lunarot-Tarot-old:15dac69]\` Update index.html
*   **2026-06-16**  -  \`[Lunarot-Tarot-old:a8c5117]\` Update index.html
*   **2026-06-16**  -  \`[Lunarot-Tarot-old:455cac9]\` Update index.html
*   **2026-06-16**  -  \`[Lunarot-Tarot-old:41ca5c2]\` Update index.html

---

## ✦ Vibecoding Development Log  -  DEKA / Lunarot Ecosystem

A running record of what\'s been built, in what order it surfaced in conversation.

### Origin
*   **DEKA founded ~2019**  -  a graphic design practice built on suprematist composition (shape, colour, line/text) and aesthetics-for-aesthetics\'-sake. No conceptual backstory required; sources range ancient to modern, high to low; style deliberately unfixed.
*   **DEKA Supply Co**  -  Co-founded streetwear label (Guangzhou supplier, Shopify) as the commercial arm  -  same year, ongoing.
*   **Ko-fi Think-tank/Commission**  -  A commission concept (community threads, mood boards, custom design requests) exists at idea stage  -  not yet built.

### The Split  -  Lunarot DEKA
*   **Lunarot DEKA** emerges as the darker, gothic/occult branch of the DEKA practice  -  the shadow twin to the aesthetics-first parent brand.

### Build History
*   **Tarot engine, first pass**  -  pachinko-style mechanic, built on the Gemini API with Vite/TypeScript. A prototype that gambled on chance as its core interaction.
*   **Tarot engine, current**  -  rebuilt clean in Vite/TypeScript, no pachinko mechanic. Deployed live at [lunarotdekatarot.vercel.app](https://lunarotdekatarot.vercel.app/) via Vercel/GitHub. Repo: [faizyasar/Lunarot-Tarot-Engine-1.0](https://github.com/faizyasar/Lunarot-Tarot-Engine-1.0).
*   **Generative stamp field tool (lunarot-stamps-v2.html)**  -  mobile-first, touch-native, twelve symbol sets. A ritual-marking tool disguised as a UI toy.
*   **Golden spiral composition generator (lunarot-phi-v2.html)**  -  \u03c6-driven compositional generator, tying the suprematist DNA of DEKA back into generative logic.
*   **Lunarot Ankoku archive**  -  in progress. Preserving late-1990s - 2000s Japanese personal-site horror culture (個人サイト). Repo: [lunarot-ankoku](https://github.com/faizyasar/lunarot-ankoku). An act of digging up what the web has already buried once.
*   **Unifying UI**  -  not yet built. Intended to bind the tarot engine, generative tools, and the Ankoku archive into one coherent shell. Currently the one open door in the house.
*   **Work In Progress (API uploads)**:
    *   *Lunarot Baseball*  -  work in progress.
    *   *Unified Graphics Maker*  -  work in progress.

### Supporting Infrastructure
*   **Personal web presence**:
    *   Carrd: [faizyasar.life](https://faizyasar.life/)
    *   GitHub: [github.com/faizyasar](https://github.com/faizyasar)
    *   Behance: [behance.net/faizyasar](https://www.behance.net/faizyasar)
    *   Life Portal: [faizyasar.life](https://faizyasar.life/)
    *   *Built as deliberate identity infrastructure, not just a portfolio.*
*   **Google Search Console**: Verified and indexed.
`;

const SOCIAL_CONDUIT = `# Social Conduits & Alchemical Channels

Direct channels to trace and establish connection with the vessel architect:

---

## ✦ Primary Vessels

*   **Julian Ingress (Github):** [github.com/faizyasar](https://github.com/faizyasar)
    *   *System depository containing code archives and developmental traces.*
*   **Architect Portal (Portfolio):** [faizyasar.life](https://faizyasar.life)
    *   *The general portfolio containing visual artifacts and system architecture.*
*   **Esoteric Art Portal:** [lnrtdka.drr.ac](https://lnrtdka.drr.ac/)
    *   *Visual system layouts, graphic design archives, and sacred illustrations.*
*   **Occupied Grid (LinkedIn):** [linkedin.com/in/faizyasar](https://linkedin.com/in/faizyasar)
    *   *Professional node alignment and graduate network index.*
*   **Inspiration Vault (Pinterest):** [pinterest.com/FaizYasar](https://au.pinterest.com/FaizYasar/)
    *   *Visual references, alchemical motifs, and graphic style-boards.*
*   **Arcade Tarot Conduit:** [tarot.drr.ac](https://tarot.drr.ac/)
    *   *Interactive web divination node.*

---

## ✦ System Status
*   **Architect:** Faiz Yasar
*   **Host Network:** Sydney, Australia [100% Alignment]
*   **Integrity Verification:** verified signature stable
*   **Epoch Synchrony:** active
`;

const DEKA_ARCHIVES = `# DEKA / DEKASUPPLYCO / LUNAROTDEKA

An ongoing refusal to make work that does not first please the eye.

---

## ✦ The Three Forms of DEKA

1.  **DEKA**
    *   *The core aesthetic philosophy:* Pure graphics for aesthetic's sake. No conceptual backstories or academic justifications required. A translation from the heart that speaks past academia.
2.  **DEKASUPPLYCO**
    *   *The streetwear imprint:* A co-founded single-season streetwear label co-founded by three operators with formal profit-share structures. Streetcar-inspired culture meeting DEKA graphic principles, featuring 300gsm tees and custom NOS plush toys, sourced through Guangzhou garment suppliers with a fully integrated Shopify e-commerce backend. One season. One run. Something real to point to.
3.  **LUNAROTDEKA**
    *   *The esoteric art conflux:* The graphical archive layer bridging visual systems, occult geometries, and brand narratives.

---

## ✦ Manifest Specs
*   **Imprint Status:** Unda Construction [,,]
*   **Supplier Base:** Guangzhou Sourcing Hub
*   **Core Directive:** Eye-pleasing graphic supremacy
*   **Visual Asset Repository:** [faizyasar.life/password](https://faizyasar.life/password)
`;

function parseInline(text: string): React.ReactNode[] {
  if (!text) return [];
  const parts: React.ReactNode[] = [];
  let currentText = text;
  let keyIdx = 0;

  while (currentText.length > 0) {
    const linkMatch = currentText.match(/\[([^\]]+)\]\(([^)]+)\)/);
    const boldMatch = currentText.match(/\*\*([^*]+)\*\*/);
    const italicMatch = currentText.match(/\*([^*]+)\*/);
    const codeMatch = currentText.match(/`([^`]+)`/);
    const rawUrlMatch = currentText.match(/(https?:\/\/[^\s)\]]+)/);
    const domainMatch = currentText.match(/\b([a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(?:\/[^\s)\]]*)?)\b/i);

    let firstMatch: { index: number, length: number, type: string, data: any } | null = null;

    if (linkMatch && linkMatch.index !== undefined) {
      firstMatch = {
        index: linkMatch.index,
        length: linkMatch[0].length,
        type: 'link',
        data: { label: linkMatch[1], url: linkMatch[2] }
      };
    }

    if (boldMatch && boldMatch.index !== undefined) {
      if (!firstMatch || boldMatch.index < firstMatch.index) {
        firstMatch = {
          index: boldMatch.index,
          length: boldMatch[0].length,
          type: 'bold',
          data: boldMatch[1]
        };
      }
    }

    if (italicMatch && italicMatch.index !== undefined) {
      if (!firstMatch || italicMatch.index < firstMatch.index) {
        firstMatch = {
          index: italicMatch.index,
          length: italicMatch[0].length,
          type: 'italic',
          data: italicMatch[1]
        };
      }
    }

    if (codeMatch && codeMatch.index !== undefined) {
      if (!firstMatch || codeMatch.index < firstMatch.index) {
        firstMatch = {
          index: codeMatch.index,
          length: codeMatch[0].length,
          type: 'code',
          data: codeMatch[1]
        };
      }
    }

    if (rawUrlMatch && rawUrlMatch.index !== undefined) {
      let rawUrl = rawUrlMatch[1];
      const cleanUrl = rawUrl.replace(/[.,;:)]+$/, '');
      const matchLength = rawUrlMatch[0].length - (rawUrl.length - cleanUrl.length);
      if (!firstMatch || rawUrlMatch.index < firstMatch.index) {
        firstMatch = {
          index: rawUrlMatch.index,
          length: matchLength,
          type: 'raw-url',
          data: cleanUrl
        };
      }
    }

    if (domainMatch && domainMatch.index !== undefined && !firstMatch) {
      let domain = domainMatch[1];
      if (!domain.startsWith('http://') && !domain.startsWith('https://')) {
        const fullUrl = 'https://' + domain;
        firstMatch = {
          index: domainMatch.index,
          length: domainMatch[0].length,
          type: 'link',
          data: { label: domain, url: fullUrl }
        };
      }
    }

    if (!firstMatch) {
      parts.push(currentText);
      break;
    }

    if (firstMatch.index > 0) {
      parts.push(currentText.slice(0, firstMatch.index));
    }

    if (firstMatch.type === 'link') {
      const href = firstMatch.data.url.startsWith('http') ? firstMatch.data.url : 'https://' + firstMatch.data.url;
      parts.push(
        <a
          key={keyIdx++}
          href={href}
          target="_blank"
          rel="noopener noreferrer"
          className="text-[var(--gold)] hover:text-white underline underline-offset-2 font-bold transition-colors cursor-pointer"
        >
          {parseInline(firstMatch.data.label)}
        </a>
      );
    } else if (firstMatch.type === 'raw-url') {
      parts.push(
        <a
          key={keyIdx++}
          href={firstMatch.data}
          target="_blank"
          rel="noopener noreferrer"
          className="text-[var(--gold)] hover:text-white underline underline-offset-2 font-bold transition-colors cursor-pointer break-all"
        >
          {firstMatch.data}
        </a>
      );
    } else if (firstMatch.type === 'bold') {
      parts.push(<strong key={keyIdx++} className="font-bold text-white">{parseInline(firstMatch.data)}</strong>);
    } else if (firstMatch.type === 'italic') {
      parts.push(<em key={keyIdx++} className="italic text-[#efede8]">{parseInline(firstMatch.data)}</em>);
    } else if (firstMatch.type === 'code') {
      parts.push(<code key={keyIdx++} className="bg-black/60 text-[var(--gold)] px-1.5 py-0.5 rounded border border-white/10 font-mono text-[9.5px]">{firstMatch.data}</code>);
    }

    currentText = currentText.slice(firstMatch.index + firstMatch.length);
  }

  return parts;
}

function parseMarkdown(md: string): React.ReactNode[] {
  const lines = md.split('\n');
  const blockElements: React.ReactNode[] = [];
  
  let inCodeBlock = false;
  let codeLines: string[] = [];

  lines.forEach((line, lineIdx) => {
    if (line.trim().startsWith('```')) {
      if (inCodeBlock) {
        blockElements.push(
          <pre key={lineIdx} className="bg-white/15 border border-white/20 p-3 rounded font-mono text-[9px] sm:text-xs text-red-300 overflow-x-auto my-3 leading-relaxed scrollbar-thin scrollbar-thumb-white/10/50">
            <code>{codeLines.join('\n')}</code>
          </pre>
        );
        codeLines = [];
        inCodeBlock = false;
      } else {
        inCodeBlock = true;
      }
      return;
    }

    if (inCodeBlock) {
      codeLines.push(line);
      return;
    }

    if (line.trim() === '---') {
      blockElements.push(<hr key={lineIdx} className="my-4 border-white/20" />);
      return;
    }

    if (line.startsWith('# ')) {
      blockElements.push(
        <h1 key={lineIdx} className="text-base font-bold font-mono tracking-wider text-white uppercase mt-4 mb-2">
          {parseInline(line.substring(2))}
        </h1>
      );
      return;
    }
    if (line.startsWith('## ')) {
      blockElements.push(
        <h2 key={lineIdx} className="text-sm font-bold font-mono tracking-wide text-white/80 uppercase mt-4 mb-2">
          {parseInline(line.substring(3))}
        </h2>
      );
      return;
    }
    if (line.startsWith('### ')) {
      blockElements.push(
        <h3 key={lineIdx} className="text-xs font-bold font-mono text-[#cfc9c0] uppercase mt-3 mb-1">
          {parseInline(line.substring(4))}
        </h3>
      );
      return;
    }

    if (line.trim().startsWith('* ')) {
      const leadingSpaces = line.length - line.trimStart().length;
      const isIndented = leadingSpaces > 0;
      blockElements.push(
        <div key={lineIdx} className={`flex items-start ${isIndented ? 'ml-6 text-xs text-[#838aa0]' : 'ml-2 text-sm text-[#cfc9c0]'} my-1`}>
          <span className="text-zinc-500 mr-2 shrink-0">✦</span>
          <span>{parseInline(line.trim().substring(2))}</span>
        </div>
      );
      return;
    }

    if (line.trim() === '') {
      blockElements.push(<div key={lineIdx} className="h-2" />);
      return;
    }

    blockElements.push(
      <p key={lineIdx} className="text-sm font-garamond text-[#cfc9c0] leading-relaxed my-1">
        {parseInline(line)}
      </p>
    );
  });

  return blockElements;
}

type TabType = 'log' | 'map' | 'dev' | 'social' | 'deka';

interface DriveFile {
  id: string;
  name: string;
  mimeType: string;
  embedUrl: string;
  thumbnailUrl: string;
  parentFolder: string;
  parentFolderId: string;
}

// Rewrites raw drive uc/view URLs to working high-res public thumbnail URLs (fixes CORS/Google block)
const getWorkingImageUrl = (url: string, id: string) => {
  if (url && (url.includes('drive.google.com/uc') || url.includes('/file/d/'))) {
    return `https://drive.google.com/thumbnail?id=${id}&sz=w800`;
  }
  return url;
};

export default function AppAnkoku({ defaultTab = 'deka' }: { defaultTab?: TabType }) {
  const [activeTab, setActiveTab] = useState<TabType>(defaultTab);
  const [lightboxImg, setLightboxImg] = useState<string | null>(null);
  const [lightboxVisible, setLightboxVisible] = useState(false);
  const [activeLightboxFileId, setActiveLightboxFileId] = useState<string | null>(null);
  const [lightboxBg, setLightboxBg] = useState<'dark-grid' | 'light-grid' | 'solid-black' | 'solid-white'>('dark-grid');
  const [copiedCode, setCopiedCode] = useState(false);

  // Dynamic Apps Script Explorer states
  const [scriptUrl, setScriptUrl] = useState(() => localStorage.getItem('deka_apps_script_url') || 'https://script.google.com/macros/s/AKfycbz7UkjHDHm_-KV3P2_sEvSaTeLzvMIOepFGHNWyd0ww4rhIw4vtL2OhBaZjWfEcos8H/exec');
  const [inputUrl, setInputUrl] = useState(scriptUrl);
  const [files, setFiles] = useState<DriveFile[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [selectedFolderFilter, setSelectedFolderFilter] = useState('ALL');
  
  // Inline Document Iframe Viewer States
  const [activeEmbedUrl, setActiveEmbedUrl] = useState<string | null>(null);

  // Sync tab with external active file route changes
  useEffect(() => {
    setActiveTab(defaultTab);
  }, [defaultTab]);

  // Fetch files from Apps Script Web App
  const fetchDriveFiles = async (url: string) => {
    if (!url) return;
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(url);
      const json = await res.json();
      if (json.success) {
        setFiles(json.data);
      } else {
        setError(json.error || 'Failed to fetch directory tree.');
      }
    } catch (err: any) {
      setError(err.message || 'CORS block or connection failure.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (scriptUrl) {
      fetchDriveFiles(scriptUrl);
    }
  }, [scriptUrl]);

  const handleSaveUrl = (e: React.FormEvent) => {
    e.preventDefault();
    const cleanUrl = inputUrl.trim();
    localStorage.setItem('deka_apps_script_url', cleanUrl);
    setScriptUrl(cleanUrl);
  };

  const handleImageClick = (src: string, id: string) => {
    setLightboxImg(src);
    setActiveLightboxFileId(id);
    setTimeout(() => {
      setLightboxVisible(true);
    }, 10);
  };

  const handleCloseLightbox = () => {
    setLightboxVisible(false);
    setTimeout(() => {
      setLightboxImg(null);
      setActiveLightboxFileId(null);
    }, 300);
  };

  // Next / Prev triggers for dynamic image preview cycling
  const getImageFiles = () => {
    const activeFiles = selectedFolderFilter === 'ALL' 
      ? files 
      : files.filter(f => f.parentFolderId === selectedFolderFilter);
    return activeFiles.filter(f => f.mimeType.startsWith('image/'));
  };

  const handleNextImage = () => {
    const images = getImageFiles();
    if (images.length === 0) return;
    const currentIdx = images.findIndex(f => f.id === activeLightboxFileId);
    if (currentIdx !== -1) {
      const nextIdx = (currentIdx + 1) % images.length;
      const nextFile = images[nextIdx];
      setLightboxImg(getWorkingImageUrl(nextFile.thumbnailUrl, nextFile.id));
      setActiveLightboxFileId(nextFile.id);
    }
  };

  const handlePrevImage = () => {
    const images = getImageFiles();
    if (images.length === 0) return;
    const currentIdx = images.findIndex(f => f.id === activeLightboxFileId);
    if (currentIdx !== -1) {
      const prevIdx = (currentIdx - 1 + images.length) % images.length;
      const prevFile = images[prevIdx];
      setLightboxImg(getWorkingImageUrl(prevFile.thumbnailUrl, prevFile.id));
      setActiveLightboxFileId(prevFile.id);
    }
  };

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!lightboxImg) return;
      if (e.key === 'ArrowRight') {
        handleNextImage();
      } else if (e.key === 'ArrowLeft') {
        handlePrevImage();
      } else if (e.key === 'Escape') {
        handleCloseLightbox();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [lightboxImg, activeLightboxFileId, selectedFolderFilter, files]);

  // Get distinct folder names and IDs for filtering
  const folderMap = new Map<string, string>();
  files.forEach(f => {
    if (f.parentFolderId && f.parentFolder) {
      folderMap.set(f.parentFolderId, f.parentFolder);
    }
  });
  const foldersList = [['ALL', 'ALL'], ...Array.from(folderMap.entries())];

  const filteredFiles = selectedFolderFilter === 'ALL' 
    ? files 
    : files.filter(f => f.parentFolderId === selectedFolderFilter);

  const getContent = () => {
    switch (activeTab) {
      case 'log': return SITES_LOG;
      case 'map': return LINK_WEB_MAP;
      case 'dev': return DEV_HISTORY;
      case 'social': return SOCIAL_CONDUIT;
      case 'deka': return DEKA_ARCHIVES;
      default: return SITES_LOG;
    }
  };

  const appsScriptCode = `function doGet(e) {
  const output = ContentService.createTextOutput();
  output.setMimeType(ContentService.MimeType.JSON);
  
  // CORS Headers
  output.addHeader("Access-Control-Allow-Origin", "*");
  output.addHeader("Access-Control-Allow-Methods", "GET");
  
  try {
    const rootFolderId = "10LAgjxxPvE0Jp6lFkUhM2qaXKHqs_BJ3";
    const rootFolder = DriveApp.getFolderById(rootFolderId);
    
    const results = [];
    crawlFolder(rootFolder, results);
    
    output.setContent(JSON.stringify({ success: true, data: results }));
  } catch (err) {
    output.setContent(JSON.stringify({ success: false, error: err.toString() }));
  }
  
  return output;
}

function crawlFolder(folder, resultsList) {
  const files = folder.getFiles();
  while (files.hasNext()) {
    const file = files.next();
    const fileId = file.getId();
    const mime = file.getMimeType();
    
    // Clean embed preview URL for iframes and lightboxes
    const embedUrl = "https://drive.google.com/file/d/" + fileId + "/preview";
    
    // Generate reliable image preview and thumbnail URL
    let thumbnailUrl = embedUrl;
    if (mime.includes('image/')) {
      thumbnailUrl = "https://drive.google.com/uc?export=view&id=" + fileId;
    }

    resultsList.push({
      id: fileId,
      name: file.getName(),
      mimeType: mime,
      embedUrl: embedUrl,
      thumbnailUrl: thumbnailUrl,
      parentFolder: folder.getName(),
      parentFolderId: folder.getId()
    });
  }
  
  const subfolders = folder.getFolders();
  while (subfolders.hasNext()) {
    crawlFolder(subfolders.next(), resultsList); 
  }
}`;

  return (
    <div className="flex-1 flex flex-col h-full w-full bg-black/35 backdrop-blur-[2px] border border-white/40 relative z-25 group overflow-hidden shadow-[0_0_20px_rgba(255,255,255,0.02)] p-4 sm:p-6 md:p-8">
      {/* Visual background details */}
      <div className="absolute inset-1.5 border border-dashed border-white/15 pointer-events-none z-0" />
      
      {/* File tags */}
      <span className="absolute top-2 left-3 font-mono text-[7px] text-zinc-500/50 tracking-[0.3em] uppercase pointer-events-none">RESEARCH_LOG // ANKOKU</span>
      <span className="absolute bottom-2 right-3 font-mono text-[6px] text-[#ef4444]/40 tracking-[0.2em] uppercase pointer-events-none">OCCULT_W3_DIG</span>

      {/* Tabs */}
      <div className="flex border-b border-white/20 mb-6 relative z-10 select-none mt-2 overflow-x-auto scrollbar-none">
        {['log', 'map', 'dev', 'deka', 'social'].map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab as TabType)}
            className={`px-4 py-2 font-mono text-[10px] sm:text-xs tracking-widest uppercase transition-all duration-300 border-b-2 shrink-0 ${
              activeTab === tab
                ? 'border-red-800 text-white font-bold text-shadow-[0_0_8px_rgba(255,255,255,0.4)]'
                : 'border-transparent text-[#838aa0] hover:text-white'
            }`}
          >
            📄 {tab === 'deka' ? '🖼️ DEKA GALLERY SHOWCASE' : tab === 'pinterest' ? '📌 PINTEREST BOARDS' : tab === 'log' ? '📄 SITES-LOG.MD' : tab === 'map' ? '🌐 LINK-WEB-MAP.MD' : tab === 'dev' ? '📜 DEV-HISTORY.MD' : '📡 SOCIAL-CONDUIT.MD'}
          </button>
        ))}
      </div>

      {/* Document View Area */}
      <div className="flex-1 overflow-y-auto pt-2 pb-6 px-1 md:px-4 leading-relaxed relative z-10 scrollbar-thin scrollbar-thumb-white/10 text-justify">
        <div className="space-y-1">
          {parseMarkdown(getContent())}

          {/* Apps Script Dynamic File Previewer (Specific to DEKA tab) */}
          {activeTab === 'deka' && (
            <div className="mt-8 border-t border-white/20 pt-6">
              
              {/* If Web App URL is not set, show the Setup Instructions */}
              {!scriptUrl ? (
                <div className="bg-black/60 border border-white/30 p-5 rounded-none font-mono text-left mb-6">
                  <h3 className="text-xs font-bold text-white uppercase mb-3 tracking-wider">
                    ✦ Connect Deka Google Drive Live Previewer
                  </h3>
                  <p className="text-[10px] text-[#cfc9c0]/80 mb-4 leading-relaxed font-sans">
                    Setup a serverless Google Apps Script Web App to load, query, and preview all folders, subfolders, and documents recursively from Google Drive.
                  </p>
                  
                  <div className="space-y-3 text-[10px] text-[#cfc9c0] mb-5">
                    <div className="flex items-start"><span className="text-zinc-500 mr-2">1.</span><span>Open <a href="https://script.google.com" target="_blank" rel="noreferrer" className="text-white hover:underline">script.google.com</a> and click <b>New Project</b>.</span></div>
                    <div className="flex items-start"><span className="text-zinc-500 mr-2">2.</span><span>Paste the script code below into the editor.</span></div>
                    <div className="flex items-start"><span className="text-zinc-500 mr-2">3.</span><span>Click <b>Deploy &gt; New Deployment</b>. Select <b>Web App</b>.</span></div>
                    <div className="flex items-start"><span className="text-zinc-500 mr-2">4.</span><span>Configure: <i>Execute as:</i> <b>Me</b>, <i>Who has access:</i> <b>Anyone</b>. Click Deploy.</span></div>
                    <div className="flex items-start"><span className="text-zinc-500 mr-2">5.</span><span>Copy the generated <b>Web App URL</b> and paste it below.</span></div>
                  </div>

                  <form onSubmit={handleSaveUrl} className="flex gap-2 mb-6">
                    <input 
                      type="url" 
                      placeholder="Paste Google Apps Script Web App URL here..."
                      value={inputUrl}
                      onChange={(e) => setInputUrl(e.target.value)}
                      className="flex-1 bg-black border border-white/30 px-3 py-1.5 text-xs text-white focus:outline-none focus:border-red-800"
                      required
                    />
                    <button 
                      type="submit"
                      className="px-4 py-1.5 border border-zinc-700 bg-white/20 text-white hover:bg-white/40 text-xs font-bold uppercase tracking-wider cursor-pointer"
                    >
                      Connect
                    </button>
                  </form>

                  <div className="flex justify-between items-centre mb-2">
                    <h4 className="text-[10px] text-white uppercase tracking-widest font-bold">Google Apps Script Code:</h4>
                    <button
                      onClick={(e) => {
                        e.preventDefault();
                        navigator.clipboard.writeText(appsScriptCode);
                        setCopiedCode(true);
                        setTimeout(() => setCopiedCode(false), 2000);
                      }}
                      className="px-3 py-1 border border-zinc-700 bg-white/20 text-white hover:bg-white/40 text-[9px] font-mono tracking-widest uppercase cursor-pointer select-none"
                    >
                      {copiedCode ? '✦ COPIED ✦' : '[ COPY SCRIPT ]'}
                    </button>
                  </div>
                  <pre className="bg-black/90 border border-white/20 p-3 rounded font-mono text-[9px] text-[#cfc9c0] overflow-x-auto max-h-40 scrollbar-thin select-text" style={{ userSelect: 'text' }}>
                    <code>{appsScriptCode}</code>
                  </pre>
                </div>
              ) : (
                <div className="flex flex-col gap-4 font-mono">
                  
                  {/* File Explorer Header controls */}
                  <div className="flex flex-col sm:flex-row justify-between items-start sm:items-centre gap-3 border-b border-white/25 pb-3">
                    <div className="flex items-centre gap-2 text-[10px]">
                      <span className="text-[#838aa0]">ACTIVE_VESSEL :</span>
                      <span className="text-white font-bold">10LAgjxx... (Deka Archive)</span>
                    </div>
                    
                    <div className="flex flex-wrap items-centre gap-3">
                      {/* Filter by subfolder */}
                      <div className="flex items-centre gap-1.5 text-[10px]">
                        <span className="text-[#838aa0]">FILTER_FOLDER :</span>
                        <select
                          value={selectedFolderFilter}
                          onChange={(e) => setSelectedFolderFilter(e.target.value)}
                          className="bg-black border border-white/30 text-white px-2 py-0.5 focus:outline-none focus:border-red-800 text-[10px]"
                        >
                          {foldersList.map(([fid, name]) => (
                            <option key={fid} value={fid}>{name}</option>
                          ))}
                        </select>
                      </div>

                      {/* Reset App Script URL */}
                      <button
                        onClick={() => {
                          localStorage.removeItem('deka_apps_script_url');
                          setScriptUrl('');
                          setInputUrl('');
                        }}
                        className="text-[9px] text-[#838aa0] hover:text-white underline cursor-pointer"
                      >
                        [ Configure Web App ]
                      </button>
                    </div>
                  </div>

                  {/* Loading/Error Telemetries */}
                  {loading && (
                    <div className="flex items-centre justify-centre py-12">
                      <span className="text-xs text-white animate-pulse tracking-widest uppercase">
                        ✦ LINKING DRIVE COGNITION TREE...
                      </span>
                    </div>
                  )}

                  {error && (
                    <div className="border border-white/40 bg-white/10 text-white p-4 text-xs">
                      <p className="font-bold mb-2">ERROR : connection handshake failed</p>
                      <p className="opacity-80">{error}</p>
                      <button
                        onClick={() => fetchDriveFiles(scriptUrl)}
                        className="mt-3 px-3 py-1 border border-zinc-700 text-white hover:bg-red-900/10 uppercase tracking-widest text-[9px] cursor-pointer"
                      >
                        Retry Handshake
                      </button>
                    </div>
                  )}

                  {/* Inline document preview viewport (when a document file is clicked) */}
                  {activeEmbedUrl && (
                    <div className="relative w-full h-[550px] bg-black/40 border border-white/30 overflow-hidden rounded">
                      <div className="absolute top-2 right-3 z-30 flex gap-2">
                        <a 
                          href={activeEmbedUrl.replace('/preview', '/view')}
                          target="_blank" 
                          rel="noreferrer"
                          className="font-mono text-[9px] text-white hover:text-white bg-black/60 px-3 py-1.5 border border-white/30 rounded"
                        >
                          [ OPEN IN DRIVE ]
                        </a>
                        <button 
                          onClick={() => setActiveEmbedUrl(null)}
                          className="font-mono text-[9px] text-white hover:text-white bg-black/60 px-3 py-1.5 border border-white/30 rounded cursor-pointer"
                        >
                          [ CLOSE PREVIEW ]
                        </button>
                      </div>
                      
                      {/* Dark-themed embedded iframe preview */}
                      <iframe
                        src={activeEmbedUrl}
                        width="100%"
                        height="100%"
                        frameBorder="0"
                        className="w-full h-full filter invert-[88%] hue-rotate-180 brightness-[85%] saturate-[95%] opacity-95"
                        allowFullScreen
                        loading="lazy"
                        sandbox="allow-scripts allow-same-origin allow-popups"
                      ></iframe>
                    </div>
                  )}

                  {/* dynamic file list rendering */}
                  {!loading && !error && files.length > 0 && (
                    <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
                      {filteredFiles.map((file, idx) => {
                        const isImage = file.mimeType.startsWith('image/');
                        const workingThumbUrl = getWorkingImageUrl(file.thumbnailUrl, file.id);
                        return (
                          <div 
                            key={idx}
                            onClick={() => {
                              if (isImage) {
                                handleImageClick(workingThumbUrl, file.id);
                              } else {
                                setActiveEmbedUrl(file.embedUrl);
                              }
                            }}
                            className="aspect-square relative bg-black/45 border border-white/25 hover:border-red-500/50 rounded overflow-hidden cursor-zoom-in group/item transition-all duration-300 hover:shadow-[0_0_12px_rgba(239,68,68,0.15)] flex flex-col justify-between"
                          >
                            {isImage ? (
                              <img 
                                src={workingThumbUrl} 
                                alt={file.name} 
                                loading="lazy"
                                className="w-full h-full object-cover filter saturate-[65%] group-hover/item:saturate-100 transition-all duration-500"
                              />
                            ) : (
                              <div className="flex-1 flex flex-col items-centre justify-centre p-3 text-centre gap-2">
                                <span className="text-2xl text-red-950 group-hover/item:text-white transition-colours duration-300">📄</span>
                                <span className="text-[9px] text-[#cfc9c0]/80 tracking-wider truncate w-full">{file.name}</span>
                              </div>
                            )}

                            {/* Info overlay bar */}
                            <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-black via-black/80 to-transparent p-2 flex flex-col gap-0.5">
                              <span className="font-mono text-[9px] text-white tracking-wider truncate w-full">{file.name}</span>
                              <span className="font-mono text-[7px] text-[#838aa0] uppercase tracking-widest truncate w-full">
                                {file.parentFolder} // {isImage ? 'IMG' : 'DOC'}
                              </span>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  )}

                  {!loading && !error && files.length === 0 && (
                    <div className="text-centre py-12 border border-dashed border-white/20">
                      <span className="text-[10px] text-[#838aa0] uppercase tracking-widest">
                        No previewable assets found in this folder.
                      </span>
                    </div>
                  )}
                </div>
              )}


            </div>
          )}
        </div>
      </div>

      {/* Lightbox Modal (rendered at z-[10100] on top of CRT bezel and scanlines) */}
      {lightboxImg && (
        <div 
          className={`fixed inset-0 bg-black/95 z-[10100] flex flex-col md:flex-row items-stretch transition-opacity duration-300 ease-out ${
            lightboxVisible ? 'opacity-100' : 'opacity-0'
          }`}
          onClick={handleCloseLightbox}
        >
          {/* Left sidebar: Folders List (visible on desktop) */}
          <div 
            className="w-64 border-r border-white/40 p-5 overflow-y-auto hidden md:flex flex-col bg-black/90 font-mono select-none text-left z-50 shrink-0"
            onClick={(e) => e.stopPropagation()} // prevent closing
          >
            <h3 className="text-[10px] tracking-widest text-white uppercase font-bold mb-4 border-b border-white/30 pb-2">
              ✦ ARCHIVE FOLDERS
            </h3>
            {foldersList.map(([fid, name]) => (
              <button
                key={fid}
                onClick={() => {
                  setSelectedFolderFilter(fid);
                  const newFiltered = files.filter(f => fid === 'ALL' ? f.mimeType.startsWith('image/') : (f.parentFolderId === fid && f.mimeType.startsWith('image/')));
                  if (newFiltered.length > 0) {
                    setLightboxImg(getWorkingImageUrl(newFiltered[0].thumbnailUrl, newFiltered[0].id));
                    setActiveLightboxFileId(newFiltered[0].id);
                  }
                }}
                className={`text-left px-3 py-2 border text-[10px] tracking-wider transition-all duration-300 cursor-pointer ${
                  selectedFolderFilter === fid
                    ? 'border-red-800 text-white bg-white/20 font-bold'
                    : 'border-transparent text-[#838aa0] hover:text-white'
                }`}
              >
                📁 {name}
              </button>
            ))}
          </div>

          {/* Top selector bar (visible on mobile) */}
          <div 
            className="md:hidden p-4 bg-black border-b border-white/40 flex justify-between items-centre z-50 shrink-0"
            onClick={(e) => e.stopPropagation()}
          >
            <span className="font-mono text-[9px] text-[#838aa0] tracking-wider">FILTER_FOLDER :</span>
            <select
              value={selectedFolderFilter}
              onChange={(e) => {
                const fid = e.target.value;
                setSelectedFolderFilter(fid);
                const newFiltered = files.filter(f => fid === 'ALL' ? f.mimeType.startsWith('image/') : (f.parentFolderId === fid && f.mimeType.startsWith('image/')));
                if (newFiltered.length > 0) {
                  setLightboxImg(getWorkingImageUrl(newFiltered[0].thumbnailUrl, newFiltered[0].id));
                  setActiveLightboxFileId(newFiltered[0].id);
                }
              }}
              className="bg-black border border-white/40 text-white px-3 py-1 focus:outline-none focus:border-red-800 text-[10px] font-mono"
            >
              {foldersList.map(([fid, name]) => (
                <option key={fid} value={fid}>{name}</option>
              ))}
            </select>
          </div>

          {/* Main content: Active Image viewport */}
          <div className="flex-1 flex flex-col items-centre justify-centre p-4 relative z-10 select-none">
            
            <div 
              className={`relative max-w-full max-h-[80vh] flex items-centre justify-centre transition-all duration-300 ease-out ${
                lightboxVisible ? 'scale-100 opacity-100' : 'scale-95 opacity-0'
              }`}
              onClick={(e) => e.stopPropagation()} // prevent closing on clicking image itself
            >
              {/* Image viewport with dynamic transparency grid inspection backgrounds */}
              <div className="max-w-full max-h-[80vh] flex items-centre justify-centre">
                <img 
                  src={lightboxImg} 
                  alt="Drive Archive High-Res Preview" 
                  className="max-w-full max-h-[70vh] object-contain"
                />
              </div>

              {/* Float indicators */}
              <div className="absolute bottom-6 left-1/2 -translate-x-1/2 bg-black/75 px-4 py-2 border border-white/40 font-mono text-[9px] text-[#cfc9c0] text-centre tracking-wider max-w-[90%] truncate">
                {files.find(f => f.id === activeLightboxFileId)?.name || 'Previewing Image'}
              </div>
            </div>

            {/* Next/Prev buttons (repositioned inwards to avoid CRT bezel cutoff) */}
            <div className="absolute inset-y-0 left-0 right-0 flex items-centre justify-between pointer-events-none px-12 md:px-24">
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  handlePrevImage();
                }}
                className="pointer-events-auto bg-black/60 border border-white/30 text-white hover:text-white p-3 md:p-4 rounded-full hover:bg-black/85 transition-all duration-300 font-bold text-sm md:text-base select-none cursor-pointer"
              >
                ◀
              </button>
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  handleNextImage();
                }}
                className="pointer-events-auto bg-black/60 border border-white/30 text-white hover:text-white p-3 md:p-4 rounded-full hover:bg-black/85 transition-all duration-300 font-bold text-sm md:text-base select-none cursor-pointer"
              >
                ▶
              </button>
            </div>

            {/* Close button */}
            <button 
              onClick={handleCloseLightbox}
              className="absolute top-4 right-4 font-mono text-[10px] text-white/60 hover:text-white tracking-widest uppercase bg-black/55 px-3 py-1.5 border border-white/10 rounded cursor-pointer z-50"
            >
              [ CLOSE ]
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
