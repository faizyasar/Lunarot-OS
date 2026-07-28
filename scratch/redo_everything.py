import os
import shutil
import json
import re

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
public_dir = os.path.join(root_dir, "public")
src_file = r"C:\Users\faizy\Downloads\Sacred Pachinko 0.9.html"

# ==============================================================================
# 1. FIX SACRED PACHINKO STATIC FILES & VERCEL ROUTING
# ==============================================================================
# Copy Sacred Pachinko 0.9.html to BOTH sacred-pachinko.html and pachinko.html in public/
pachinko_html = os.path.join(public_dir, "pachinko.html")
sacred_pachinko_html = os.path.join(public_dir, "sacred-pachinko.html")

if os.path.exists(src_file):
    shutil.copyfile(src_file, pachinko_html)
    shutil.copyfile(src_file, sacred_pachinko_html)
    print("[SUCCESS] Copied Sacred Pachinko 0.9 to public/pachinko.html and public/sacred-pachinko.html")
else:
    print("[WARN] Downloads file not found")

# Clean vercel.json
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
print("[SUCCESS] Configured vercel.json with static html rewrites")


# ==============================================================================
# 2. UPDATE LOG FORMAT TO [year] / [day-month] / content
# ==============================================================================
formatted_2026_log = """# ✦ 2026

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
*   `[lunarot-os:6f15070]` Standardize header nav tabs to use index.css .nav-btn classes
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
*   `[Lunarot-Tarot-old:41ca5c2]` Update index.html"""

# Update CHANGELOG.md
changelog_path = os.path.join(root_dir, "CHANGELOG.md")
with open(changelog_path, "w", encoding="utf-8") as f:
    f.write("# Changelog - Lunarot OS Ecosystem History\n\nAll notable changes, deletions, and architecture shifts of Lunarot OS are logged here.\n\n" + formatted_2026_log)
print("[SUCCESS] Updated CHANGELOG.md with [year] / [day-month] format")

# Update public/history.html
history_html_path = os.path.join(public_dir, "history.html")
history_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lunarot OS - Ecosystem History Log</title>
  <style>
    body {{
      background: #000;
      color: #cfc9c0;
      font-family: ui-monospace, 'SF Mono', Menlo, Consolas, monospace;
      padding: 32px 24px;
      line-height: 1.6;
      max-width: 800px;
      margin: 0 auto;
    }}
    h1 {{ color: #ffffff; font-size: 22px; letter-spacing: 0.1em; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 12px; }}
    h2 {{ color: #ffffff; font-size: 18px; margin-top: 32px; border-bottom: 1px dashed rgba(255,255,255,0.15); padding-bottom: 4px; }}
    h3 {{ color: #838aa0; font-size: 14px; margin-top: 20px; letter-spacing: 0.15em; }}
    ul {{ list-style-type: square; padding-left: 20px; }}
    li {{ margin-bottom: 6px; font-size: 13px; }}
    code {{ color: #ffffff; background: rgba(255,255,255,0.1); padding: 2px 6px; font-size: 11px; }}
    a {{ color: #ffffff; text-decoration: underline; }}
  </style>
</head>
<body>
  <h1>✦ Lunarot OS - Ecosystem History Log</h1>
  <div id="content">
"""

# Convert markdown to html elements for history.html
for line in formatted_2026_log.split('\n'):
    if line.startswith('# ✦ '):
        history_content += f"<h2>{line[4:]}</h2>\n"
    elif line.startswith('## '):
        history_content += f"<h3>Day: {line[3:]}</h3>\n<ul>\n"
    elif line.startswith('*   '):
        item_text = line[4:].replace('`', '<code>', 1).replace('`', '</code>', 1)
        history_content += f"  <li>{item_text}</li>\n"

history_content += """
  </div>
</body>
</html>"""

with open(history_html_path, "w", encoding="utf-8") as f:
    f.write(history_content)
print("[SUCCESS] Updated public/history.html with [year] / [day-month] format")

print("[COMPLETE] Script finished.")
