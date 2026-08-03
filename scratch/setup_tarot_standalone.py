import shutil
import os
import json

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
public_dir = os.path.join(root_dir, "public")

src_standalone = r"C:\Users\faizy\Downloads\Lunarot_Tarot_Deck_-_Standalone.html"
dst_standalone = os.path.join(public_dir, "tarot-standalone.html")

shutil.copyfile(src_standalone, dst_standalone)

with open(dst_standalone, "r", encoding="utf-8") as f:
    st_code = f.read()

# Inject postMessage notify inside doInspect & endInspect in tarot-standalone.html
target_inspect_str = "    state = 'inspect';\n    document.body.classList.add('show-nav');"
replace_inspect_str = "    state = 'inspect';\n    document.body.classList.add('show-nav');\n    try { window.parent.postMessage({ type: 'LUNAROT_TAROT_INSPECT', cardName: c.name, num: c.num, trad: c.trad, index: i }, '*'); } catch(e){}"

if target_inspect_str in st_code:
    st_code = st_code.replace(target_inspect_str, replace_inspect_str)
    print("[SUCCESS] Injected postMessage to doInspect")
else:
    print("[WARN] Could not find target_inspect_str")

target_deselect_str = "    inspected = -1;\n    state = 'spread';"
replace_deselect_str = "    inspected = -1;\n    state = 'spread';\n    try { window.parent.postMessage({ type: 'LUNAROT_TAROT_DESELECT' }, '*'); } catch(e){}"

if target_deselect_str in st_code:
    st_code = st_code.replace(target_deselect_str, replace_deselect_str)
    print("[SUCCESS] Injected postMessage to endInspect")
else:
    print("[WARN] Could not find target_deselect_str")

with open(dst_standalone, "w", encoding="utf-8") as f:
    f.write(st_code)

print("[SUCCESS] Prepared public/tarot-standalone.html with postMessage telemetry bridge")

# Update vercel.json
vercel_path = os.path.join(root_dir, "vercel.json")
v_config = {
  "cleanUrls": True,
  "rewrites": [
    { "source": "/tarot-standalone", "destination": "/tarot-standalone.html" },
    { "source": "/tarot", "destination": "/tarot-standalone.html" },
    { "source": "/sacred-pachinko", "destination": "/sacred-pachinko.html" },
    { "source": "/pachinko", "destination": "/pachinko.html" },
    { "source": "/history", "destination": "/history.html" }
  ]
}
with open(vercel_path, "w", encoding="utf-8") as f:
    json.dump(v_config, f, indent=2)

print("[SUCCESS] Configured vercel.json")
