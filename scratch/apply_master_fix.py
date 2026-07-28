import os
import shutil
import json
import re

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
public_dir = os.path.join(root_dir, "public")
src_file = r"C:\Users\faizy\Downloads\Sacred Pachinko 0.9.html"

# ==============================================================================
# 1. SACRED PACHINKO STATIC FILES & VERCEL ROUTING
# ==============================================================================
pachinko_html = os.path.join(public_dir, "pachinko.html")
sacred_pachinko_html = os.path.join(public_dir, "sacred-pachinko.html")

if os.path.exists(src_file):
    shutil.copyfile(src_file, pachinko_html)
    shutil.copyfile(src_file, sacred_pachinko_html)
    print("[SUCCESS] Copied Sacred Pachinko 0.9 to public/pachinko.html and public/sacred-pachinko.html")

vercel_json_path = os.path.join(root_dir, "vercel.json")
vercel_config = {
  "cleanUrls": True,
  "rewrites": [
    { "source": "/sacred-pachinko", "destination": "/sacred-pachinko.html" },
    { "source": "/pachinko", "destination": "/pachinko.html" },
    { "source": "/history", "destination": "/history.html" }
  ]
}

with open(vercel_json_path, "w", encoding="utf-8") as f:
    json.dump(vercel_config, f, indent=2)
print("[SUCCESS] Configured vercel.json")


# ==============================================================================
# 2. LOG FORMAT & GITHUB CONTRIBUTIONS TELEMETRY
# ==============================================================================
github_telemetry_md = """# ✦ GITHUB CONTRIBUTION TELEMETRY

## ✦ 149 CONTRIBUTIONS IN 2026
> **Active Nodes**: Apr, May, Jun, Jul 2026 | **Resonance**: 99.4% High Rotation
> **Epoch Selectors**: [ 2026 (ACTIVE) ] · [ 2025 ] · [ 2024 ]

### ✦ 2026 HEATMAP MATRIX
```
Aug  Sep  Oct  Nov  Dec  Jan  Feb  Mar  Apr   May   Jun   Jul
 .    .    .    .    .    .    .    .    🟩    🟩    🟩🟩  🟩🟩🟩
 .    .    .    .    .    .    .    .    .     .     🟩🟩  🟩🟩
 .    .    .    .    .    .    .    .    .     .     🟩    🟩
```

# ✦ 2026

## 29/07
*   [lunarot-os:4006ef0] feat: add music conduit tab, boy harsher lastfm stats, letterboxd and pi.fyi links
*   [lunarot-os:9b6d2de] fix: place music.index and deka-archive.index under database, fix bottom bar faizyasar.life link

## 28/07
*   [lunarot-os:0930e5c] feat: group logs in D/M/Y format, restore sacred pachinko routes and database folders

## 26/07
*   [lunarot-os:0.9.0] Static serve routing for osLATEST.html and pachinkoLATEST.html

## 24/07
*   [lunarot-os:0.5.0] Integrated Sacred Pachinko 3 standalone build and single-file HTML bundler configuration

## 16/07
*   [lunarot-os:5419300] Update compiled lunarot-os.html bundle
*   [lunarot-os:6f15070] Standardize header nav tabs to use index.css .nav-btn classes
*   [lunarot-os:ef68893] Restore header nav selectors (tabs) and sync active card stack highlights
*   [lunarot-os:c329e32] Add standalone lunarot-os-2.html copy-paste template
*   [lunarot-os:0bfa55a] Optimise backgrounds rendering inside lunarot-os.html
*   [lunarot-os:b75566a] Update main README and submodules refs
*   [lunarot-os:fc43333] Update submodule references to optimised versions
*   [lunarot-os:6b4d650] Sync Lunarot OS with standalone shell updates
*   [Lunarot-Directory:b916d0a] Update README with humanised details
*   [Lunarot-Directory:f34f636] Optimise background rendering and add OS components
*   [Lunarot-Pachinko:4952232] Update README with humanised details
*   [Lunarot-Pachinko:48ab910] Optimise background rendering and add OS components
*   [Lunarot-Tarot:cd0cb99] Update README with humanised details
*   [Lunarot-Tarot:ef84c65] Optimise background rendering and add OS components

## 26/06
*   [Lunarot-Directory:bf9b7d0] docs: update metadata and README for alchemical style

## 25/06
*   [Lunarot-Directory:4df590f] feat: scaffold Lunarot Tarot application
*   [Lunarot-Directory:6f5e4fb] Initial commit

## 24/06
*   [Lunarot-Ankoku:062bb3f] Update README.md structure formatting
*   [Lunarot-Ankoku:3386a82] Edit README for improved readability and expression
*   [Lunarot-Ankoku:1baf135] initial research log
*   [Lunarot-Pachinko:1d84b6c] Using the same aesthetic as Lunarot Tarot Engine
*   [Lunarot-Pachinko:6f4ea31] Initial commit
*   [Lunarot-Tarot-old:d4c82f7] Add deprecation notice and point users to Lunarot-Tarot-Engine-1.0

## 23/06
*   [Lunarot-Tarot-old:7c1080c] Merge pull request #1 from faizyasar/copilot/make-repo-crawlable
*   [Lunarot-Tarot-old:44eda96] Enhance sitemap metadata
*   [Lunarot-Tarot-old:f55c7ba] Add crawlability metadata, robots, and sitemap

## 20/06
*   [Lunarot-Tarot:afc11be] chore: generate package-lock.json for project dependencies

## 19/06
*   [Lunarot-Tarot:89e7f18] Update README.md

## 17/06
*   [Lunarot-Tarot:3797bef] feat: add unsettling ASCII eye tracking system
*   [Lunarot-Tarot:e09060f] style: refine layout and visual aesthetic
*   [Lunarot-Tarot:17b59fc] feat: initialize Sacred Draw application
*   [Lunarot-Tarot:728ca75] Initial commit

## 16/06
*   [Lunarot-Tarot-old:15dac69] Update index.html
*   [Lunarot-Tarot-old:a8c5117] Update index.html
*   [Lunarot-Tarot-old:455cac9] Update index.html
*   [Lunarot-Tarot-old:41ca5c2] Update index.html"""

changelog_path = os.path.join(root_dir, "CHANGELOG.md")
with open(changelog_path, "w", encoding="utf-8") as f:
    f.write("# Changelog - Lunarot OS Ecosystem History\n\n" + github_telemetry_md)
print("[SUCCESS] Updated CHANGELOG.md with GitHub telemetry graph")

history_html_path = os.path.join(public_dir, "history.html")
history_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lunarot OS - Ecosystem History & GitHub Telemetry</title>
  <style>
    body {{
      background: #000;
      color: #cfc9c0;
      font-family: ui-monospace, 'SF Mono', Menlo, Consolas, monospace;
      padding: 32px 24px;
      line-height: 1.6;
      max-width: 850px;
      margin: 0 auto;
    }}
    h1 {{ color: #ffffff; font-size: 22px; letter-spacing: 0.1em; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 12px; }}
    h2 {{ color: #ffffff; font-size: 18px; margin-top: 28px; border-bottom: 1px dashed rgba(255,255,255,0.15); padding-bottom: 4px; }}
    h3 {{ color: #838aa0; font-size: 13px; margin-top: 18px; letter-spacing: 0.15em; }}
    ul {{ list-style-type: square; padding-left: 20px; }}
    li {{ margin-bottom: 6px; font-size: 13px; }}
    pre {{ background: rgba(255,255,255,0.05); padding: 12px; border: 1px solid rgba(255,255,255,0.1); color: #4ade80; overflow-x: auto; }}
    blockquote {{ border-left: 2px solid #ef4444; padding-left: 12px; color: #cfc9c0; background: rgba(255,255,255,0.02); padding-top: 4px; padding-bottom: 4px; }}
  </style>
</head>
<body>
  <h1>✦ Lunarot OS - Ecosystem History & GitHub Telemetry</h1>
  <div id="content">
"""

for line in github_telemetry_md.split('\n'):
    if line.startswith('# ✦ '):
        history_html_content += f"<h2>{line[4:]}</h2>\n"
    elif line.startswith('## ✦ '):
        history_html_content += f"<h2>{line[5:]}</h2>\n"
    elif line.startswith('## '):
        history_html_content += f"<h3>Day: {line[3:]}</h3>\n<ul>\n"
    elif line.startswith('### '):
        history_html_content += f"<h3>{line[4:]}</h3>\n"
    elif line.startswith('> '):
        history_html_content += f"<blockquote>{line[2:]}</blockquote>\n"
    elif line.startswith('*   '):
        history_html_content += f"  <li>{line[4:]}</li>\n"

history_html_content += """
  </div>
</body>
</html>"""

with open(history_html_path, "w", encoding="utf-8") as f:
    f.write(history_html_content)
print("[SUCCESS] Updated public/history.html with GitHub telemetry")


# ==============================================================================
# 3. UPDATE INDEX.HTML WITH CLEAN LOGS & SIDEBAR ROUTING
# ==============================================================================
index_path = os.path.join(root_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update vp array
old_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📄"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📄"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📄"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"📁"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

new_vp = 'const vp=[{name:"📁 applications",key:"apps",files:[{name:"sacred-draw.bin",path:"/apps/sacred-draw.bin",icon:"✦"},{name:"astral-pachinko.bin",path:"/apps/astral-pachinko.bin",icon:"✶"}]},{name:"📁 research",key:"research",files:[{name:"sites-log.md",path:"/research/sites-log.md",icon:"📄"},{name:"link-web-map.md",path:"/research/link-web-map.md",icon:"📄"},{name:"dev-history.md",path:"/research/dev-history.md",icon:"📜"},{name:"deka-archives.md",path:"/research/deka-archives.md",icon:"📜"},{name:"social-conduit.md",path:"/research/social-conduit.md",icon:"📡"}]},{name:"📁 database",key:"db",files:[{name:"tarot-directory.index",path:"/db/tarot-directory.index",icon:"🎴"},{name:"music.index",path:"/db/music.index",icon:"🎵"},{name:"deka-archive.index",path:"/db/deka-archive.index",icon:"🖼️"}]},{name:"📁 system",key:"sys",files:[{name:"show-aesthetic-tokens.exe",path:"/sys/show-aesthetic-tokens.exe",icon:"⚙"},{name:"edit-vessel-handshake.conf",path:"/sys/edit-vessel-handshake.conf",icon:"⟳"}]}];'

if old_vp in content:
    content = content.replace(old_vp, new_vp)
    print("[SUCCESS] Updated vp array in index.html")

# Update research top tabs bar to ONLY ["log","map","dev","social"]
old_tabs_bar = 'children:["log","map","dev","deka","social"].map('
new_tabs_bar = 'children:["log","map","dev","social"].map('
if old_tabs_bar in content:
    content = content.replace(old_tabs_bar, new_tabs_bar)
    print("[SUCCESS] Updated research top tabs bar in index.html")

# Update Ve() function to switch on file path v
old_ve_fn = 'Ve=()=>{switch(E){case"log":return nh;case"map":return sp;case"dev":return up;case"social":return op;case"deka":return cp;default:return nh}}'
new_ve_fn = 'Ve=()=>{switch(v){case"/research/sites-log.md":return nh;case"/research/link-web-map.md":return sp;case"/research/dev-history.md":return up;case"/research/social-conduit.md":return op;case"/research/deka-archives.md":return cp;default:return nh}}'

if old_ve_fn in content:
    content = content.replace(old_ve_fn, new_ve_fn)
    print("[SUCCESS] Updated Ve() function in index.html")

# Replace up variable with new github_telemetry_md (safe escaped for JS template string)
safe_up_js = github_telemetry_md.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
up_match = re.search(r'up=`#.*?(?=`,cp=)', content, re.DOTALL)

if up_match:
    content = content.replace(up_match.group(0), f'up=`{safe_up_js}')
    print("[SUCCESS] Replaced up string in index.html with escaped GitHub telemetry log")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] Master fix script finished.")
