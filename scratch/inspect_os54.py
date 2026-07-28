import os
import re

os54_path = r"C:\Users\faizy\Downloads\Lunarot-OS54.html"

if os.path.exists(os54_path):
    print(f"[FOUND] {os54_path} ({os.path.getsize(os54_path)} bytes)")
    with open(os54_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 1. Search for Google Fonts or font imports in head or style tags
    fonts = re.findall(r'<link[^>]+font[^>]+>', content, re.IGNORECASE)
    print("\n--- Font Link tags ---")
    for fn in fonts[:10]:
        safe = fn.encode('ascii', errors='replace').decode('ascii')
        print(safe)

    # 2. Search for font-family in <style>
    styles = re.findall(r'font-family:[^;}\n]+', content, re.IGNORECASE)
    print("\n--- Font-family rules ---")
    for st in set(styles[:20]):
        safe = st.encode('ascii', errors='replace').decode('ascii')
        print(safe)

    # 3. Search for font classes or markdown typography in rp() or container
    pos_rp = content.find("function rp(")
    if pos_rp != -1:
        print("\n--- rp() snippet in OS54 ---")
        snippet = content[pos_rp:pos_rp+800]
        safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
        print(safe_snippet)
else:
    print(f"[ERROR] {os54_path} does not exist")
