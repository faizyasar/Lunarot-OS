import re
import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. FIX SIDEBAR CLICK HANDLER he(_): Remove corrupting g("music"), g("deka") calls!
old_he = 'he=_=>{if(_.startsWith("http://")||_.startsWith("https://")){window.open(_,"_blank");return}p(_);if(_==="/db/music.index")g("music");else if(_==="/db/deka-archive.index")g("deka");else if(_==="/research/sites-log.md")g("log");else if(_==="/research/link-web-map.md")g("map");else if(_==="/research/dev-history.md")g("dev");else if(_==="/research/social-conduit.md")g("social");else if(_==="/research/deka-archives.md")g("deka_poetry");if(window.innerWidth<768)r(!1)};'

new_he = 'he=_=>{if(_.startsWith("http://")||_.startsWith("https://")){window.open(_,"_blank");return}p(_);if(window.innerWidth<768)r(!1)};'

if old_he in content:
    content = content.replace(old_he, new_he)
    print("[SUCCESS] Fixed he(_) click handler - removed state corrupting calls")

# 2. Update front page logo build badge to show EXACT commit number: a699551
old_front_badge = 'children:"BUILD v6.1 // cac02eb"'
new_front_badge = 'children:"BUILD a699551"'

if old_front_badge in content:
    content = content.replace(old_front_badge, new_front_badge)
    print("[SUCCESS] Updated front page badge under logo to BUILD a699551")

# 3. Update bottom status bar build number tag to match commit number: a699551
# Search for lunarot OS build in footer
old_footer_build = re.search(r'children:\["lunarot OS build ","[^"]+"\]', content)

if old_footer_build:
    content = content.replace(old_footer_build.group(0), 'children:["lunarot OS build ","a699551"]')
    print("[SUCCESS] Updated bottom status bar build tag to lunarot OS build a699551")
else:
    print("[WARN] Could not find footer build tag pattern")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] apply_build_and_click_fix script finished.")
