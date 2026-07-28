import shutil
import os
import json

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
public_dir = os.path.join(root_dir, "public")
pachinko_src = os.path.join(root_dir, "pachinkoLATEST.html")

# 1. Copy pachinkoLATEST.html to public/sacred-pachinko.html and public/pachinko.html
dest_sacred = os.path.join(public_dir, "sacred-pachinko.html")
dest_pachinko = os.path.join(public_dir, "pachinko.html")

shutil.copyfile(pachinko_src, dest_sacred)
print("[SUCCESS] Copied to public/sacred-pachinko.html")

shutil.copyfile(pachinko_src, dest_pachinko)
print("[SUCCESS] Copied to public/pachinko.html")

# 2. Update vercel.json
vercel_json_path = os.path.join(root_dir, "vercel.json")
vercel_config = {
  "cleanUrls": True,
  "rewrites": [
    { "source": "/sacred-pachinko", "destination": "/pachinkoLATEST.html" },
    { "source": "/sacred-pachinko.html", "destination": "/pachinkoLATEST.html" },
    { "source": "/pachinko", "destination": "/pachinkoLATEST.html" },
    { "source": "/pachinko.html", "destination": "/pachinkoLATEST.html" },
    { "source": "/history", "destination": "/history.html" }
  ]
}

with open(vercel_json_path, "w", encoding="utf-8") as f:
    json.dump(vercel_config, f, indent=2)
print("[SUCCESS] Updated vercel.json with all pachinko rewrites")

# 3. Update index.html to ensure window.open("/sacred-pachinko") is clean
index_path = os.path.join(root_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

old_open = 'const j=()=>{window.open("./sacred-pachinko.html","_blank")}'
new_open = 'const j=()=>{window.open("/sacred-pachinko","_blank")}'

if old_open in content:
    content = content.replace(old_open, new_open)
    print("[SUCCESS] Updated index.html window.open handler")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] Pachinko restoration script complete.")
