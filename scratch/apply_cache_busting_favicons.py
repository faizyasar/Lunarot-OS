import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html (Lunarot OS)
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

os_fav_tags = """<link rel="icon" type="image/webp" href="/favicon.webp?v=671341">
  <link rel="icon" type="image/x-icon" href="/favicon.ico?v=671341">
  <link rel="shortcut icon" href="/favicon.webp?v=671341">
  <link rel="apple-touch-icon" href="/favicon.webp?v=671341">"""

# Replace existing favicon tags or inject clean tags
idx_content = re.sub(r'<link rel="(?:icon|shortcut icon|apple-touch-icon)"[^>]*>\n?', '', idx_content)
idx_content = idx_content.replace("<head>", "<head>\n  " + os_fav_tags, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)
print("[SUCCESS] Updated index.html with cache-busted favicon tags (?v=671341)!")

# 2. Update public/sacred-pachinko.html and public/pachinko.html
pachinko_fav_tags = """<link rel="icon" type="image/webp" href="/pachinkofavicon.webp?v=671341">
  <link rel="icon" type="image/x-icon" href="/pachinko.ico?v=671341">
  <link rel="shortcut icon" href="/pachinkofavicon.webp?v=671341">
  <link rel="apple-touch-icon" href="/pachinkofavicon.webp?v=671341">"""

for p_file in ["public/sacred-pachinko.html", "public/pachinko.html"]:
    if os.path.exists(p_file):
        with open(p_file, "r", encoding="utf-8") as f:
            p_content = f.read()
        
        p_content = re.sub(r'<link rel="(?:icon|shortcut icon|apple-touch-icon)"[^>]*>\n?', '', p_content)
        p_content = p_content.replace("<head>", "<head>\n  " + pachinko_fav_tags, 1)
        
        with open(p_file, "w", encoding="utf-8") as f:
            f.write(p_content)
        print(f"[SUCCESS] Updated {p_file} with cache-busted favicon tags (?v=671341)!")

