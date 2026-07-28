import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update research window tab buttons array to ONLY ["log","map","dev","social"]
# (Removing "deka" and "music" from the top tabs bar in Research, so Deka Gallery Showcase and Music are under Database)
old_tabs_bar = '["log","map","dev","deka","social","music"].map('
new_tabs_bar = '["log","map","dev","social"].map('
if old_tabs_bar in content:
    content = content.replace(old_tabs_bar, new_tabs_bar)
    print("[SUCCESS] Updated top tab bar to ['log', 'map', 'dev', 'social']")

# 2. Update nav labels mapping
old_nav_labels = 'C==="dev"?"📜 DEV-HISTORY.MD":C==="music"?"🎵 MUSIC-CONDUIT.MD":"📡 SOCIAL-CONDUIT.MD"'
new_nav_labels = 'C==="dev"?"📜 DEV-HISTORY.MD":"📡 SOCIAL-CONDUIT.MD"'
if old_nav_labels in content:
    content = content.replace(old_nav_labels, new_nav_labels)
    print("[SUCCESS] Reverted nav labels mapping for tab bar")

# 3. Update Ve() switch case
old_ve_switch = 'Ve=()=>{switch(E){case"log":return nh;case"map":return sp;case"dev":return up;case"social":return op;case"deka":return cp;default:return nh}}'
new_ve_switch = 'Ve=()=>{switch(E){case"log":return nh;case"map":return sp;case"dev":return up;case"social":return op;case"deka":return"";case"music":return"";default:return nh}}'
if old_ve_switch in content:
    content = content.replace(old_ve_switch, new_ve_switch)
    print("[SUCCESS] Updated Ve() switch case so music and deka return empty string for markdown parser")

# 4. Update sidebar click handler he(_) so clicking sidebar items updates both v and E state
old_he_fn = 'he=_=>{if(_.startsWith("http://")||_.startsWith("https://")){window.open(_,"_blank");return}p(_),window.innerWidth<768&&r(!1)};'
new_he_fn = 'he=_=>{if(_.startsWith("http://")||_.startsWith("https://")){window.open(_,"_blank");return}p(_);if(_==="/db/music.index")g("music");else if(_==="/db/deka-archive.index")g("deka");else if(_==="/research/sites-log.md")g("log");else if(_==="/research/link-web-map.md")g("map");else if(_==="/research/dev-history.md")g("dev");else if(_==="/research/social-conduit.md")g("social");else if(_==="/research/deka-archives.md")g("deka_poetry");if(window.innerWidth<768)r(!1)};'

if old_he_fn in content:
    content = content.replace(old_he_fn, new_he_fn)
    print("[SUCCESS] Updated he(_) click handler to sync state E when sidebar files are clicked")
else:
    print("[WARN] Could not find old_he_fn target")

# 5. Fix main content area rendering so rp(Ve()) only renders when there IS markdown, and music/deka render cleanly on their own
old_render_block = 's.jsxs("div",{className:"space-y-1",children:[rp(Ve()),E==="music"&&'
new_render_block = 's.jsxs("div",{className:"space-y-1",children:[E!=="music"&&E!=="deka"&&rp(Ve()),E==="music"&&'

if old_render_block in content:
    content = content.replace(old_render_block, new_render_block)
    print("[SUCCESS] Fixed content area rendering so music and deka gallery are NOT grafted on sites-log")
else:
    print("[WARN] Could not find old_render_block target")

# 6. Make sure switch case handles /research/deka-archives.md as poetry
old_switch_cases = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;case"/db/music.index":K("AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES");g("music");break;case"/db/deka-archive.index":K("DEKA DRIVE GALLERY // LIVE ASSET PREVIEWER");g("deka");break;'
new_switch_cases = 'case"/research/social-conduit.md":K("COMMUNICATIONS CONDUITS // INGRESS SOCIALS");break;case"/research/deka-archives.md":K("DEKA POETRY & HISTORICAL DOSSIER");g("deka_poetry");break;case"/db/music.index":K("AUDIAL TELEMETRY // SPOTIFY & LAST.FM SCROBBLES");g("music");break;case"/db/deka-archive.index":K("DEKA DRIVE GALLERY // LIVE ASSET PREVIEWER");g("deka");break;'

if old_switch_cases in content:
    content = content.replace(old_switch_cases, new_switch_cases)
    print("[SUCCESS] Updated switch cases for deka poetry and database files")

# 7. Update Ve() case "deka_poetry" to return cp (the DEKA poetry text)
if 'case"deka_poetry":return cp;' not in content:
    content = content.replace('case"social":return op;', 'case"social":return op;case"deka_poetry":return cp;')
    print("[SUCCESS] Added deka_poetry case to Ve()")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] apply_perfect_fixes script complete.")
