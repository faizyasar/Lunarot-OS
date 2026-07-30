import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"
sg_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    index_content = f.read()

with open(sg_path, "r", encoding="utf-8", errors="ignore") as f:
    sg_content = f.read()

# Extract logo data URL from login page in index.html
match_login_img = re.search(r'Y0="([^"]+)"', index_content)
if not match_login_img:
    match_login_img = re.search(r'data:image/webp;base64,[^"]+', index_content)

if match_login_img:
    login_url = match_login_img.group(0 if match_login_img.group(0).startswith("data:") else 1)
    print(f"[FOUND LOGIN LOGO] Length: {len(login_url)}, Starts with: {login_url[:60]}...")

    # Check if this exact data url is in style-guide.html
    if login_url in sg_content:
        print("[MATCH SUCCESS] The exact login page logo image is embedded in style-guide.html!")
    else:
        print("[MISMATCH] The exact login page logo was not found in style-guide.html")
else:
    print("[ERROR] Login logo url not found in index.html")
