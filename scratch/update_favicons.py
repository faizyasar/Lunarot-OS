import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html (Lunarot OS main app)
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

os_favicon_tag = '<link rel="icon" type="image/webp" href="/favicon.webp">\n<link rel="shortcut icon" type="image/webp" href="/favicon.webp">'

if '<link rel="icon"' not in idx_content:
    idx_content = idx_content.replace("<head>", "<head>\n  " + os_favicon_tag, 1)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("[SUCCESS] Added main OS favicon to index.html!")
else:
    print("[INFO] Favicon tag already present in index.html")

# 2. Update public/sacred-pachinko.html and public/pachinko.html
pachinko_favicon_tag = '<link rel="icon" type="image/webp" href="/pachinkofavicon.webp">\n<link rel="shortcut icon" type="image/webp" href="/pachinkofavicon.webp">'

for p_file in ["public/sacred-pachinko.html", "public/pachinko.html"]:
    if os.path.exists(p_file):
        with open(p_file, "r", encoding="utf-8") as f:
            p_content = f.read()
        
        if '<link rel="icon"' not in p_content:
            p_content = p_content.replace("<head>", "<head>\n  " + pachinko_favicon_tag, 1)
            with open(p_file, "w", encoding="utf-8") as f:
                f.write(p_content)
            print(f"[SUCCESS] Added Pachinko favicon to {p_file}!")
        else:
            print(f"[INFO] Favicon tag already present in {p_file}")

