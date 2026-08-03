import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

# Extract video src data URI from index.html
v_match = re.search(r'(data:video/webm;base64,[A-Za-z0-9+/=]+)', index_content)
if not v_match:
    print("[ERROR] Could not extract video base64 data URI from index.html!")
    sys.exit(1)

video_data_uri = v_match.group(1)
print(f"[SUCCESS] Extracted video data URI of length {len(video_data_uri)}")

# Extract poster data URI from index.html
p_match = re.search(r'(data:image/webp;base64,[A-Za-z0-9+/=]+)', index_content)
poster_data_uri = p_match.group(1) if p_match else ""

with open("public/sacred-pachinko.html", "r", encoding="utf-8") as f:
    pachinko_content = f.read()

# 1. Update body background style in sacred-pachinko.html
pachinko_content = pachinko_content.replace("body { background: #000000;", "body { background: #000000; ")

# 2. Inject background video tag before </body>
bg_video_html = f"""
<video autoPlay muted loop playsInline preload="auto" poster="{poster_data_uri}" src="{video_data_uri}" style="position:fixed;inset:0;width:100vw;height:100vh;object-fit:cover;z-index:-1;pointer-events:none;opacity:0.9;"></video>
<script>
  (function() {{
    function forcePlay() {{
      var v = document.querySelector('video');
      if (v) {{
        v.muted = true;
        v.play().catch(function(){{}});
      }}
    }}
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', forcePlay);
    }} else {{
      forcePlay();
    }}
    window.addEventListener('click', forcePlay, {{ once: true }});
    window.addEventListener('touchstart', forcePlay, {{ once: true }});
  }})();
</script>
"""

if "</body>" in pachinko_content:
    pachinko_content = pachinko_content.replace("</body>", bg_video_html + "</body>", 1)
    print("[SUCCESS] Injected CRT background video into public/sacred-pachinko.html!")
else:
    print("[WARN] </body> tag not found in sacred-pachinko.html!")

with open("public/sacred-pachinko.html", "w", encoding="utf-8") as f:
    f.write(pachinko_content)

print("[COMPLETE] sacred-pachinko.html updated with CRT video background!")
