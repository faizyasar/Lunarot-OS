import os
import shutil
import json
import re

root_dir = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0"
public_dir = os.path.join(root_dir, "public")
src_file = r"C:\Users\faizy\Downloads\Sacred Pachinko 0.9.html"

# The SINGLE canonical pachinko file in public/
canonical_public_pachinko = os.path.join(public_dir, "pachinko.html")

# Copy 0.9 to public/pachinko.html
if os.path.exists(src_file):
    shutil.copyfile(src_file, canonical_public_pachinko)
    print("[SUCCESS] Set Sacred Pachinko 0.9 as public/pachinko.html")
else:
    print("[ERROR] Downloads file not found")

# Remove redundant duplicate pachinko files in public/ and root if present
redundant_files = [
    os.path.join(public_dir, "sacred-pachinko.html"),
    os.path.join(public_dir, "pachinkoLATEST.html"),
    os.path.join(root_dir, "pachinkoLATEST.html")
]

for rf in redundant_files:
    if os.path.exists(rf):
        os.remove(rf)
        print(f"[REMOVED] Redundant file: {rf}")

# Update vercel.json to route /sacred-pachinko and /pachinko to /pachinko.html
vercel_json_path = os.path.join(root_dir, "vercel.json")
vercel_config = {
  "cleanUrls": True,
  "rewrites": [
    { "source": "/sacred-pachinko", "destination": "/pachinko.html" },
    { "source": "/pachinko", "destination": "/pachinko.html" },
    { "source": "/history", "destination": "/history.html" }
  ]
}

with open(vercel_json_path, "w", encoding="utf-8") as f:
    json.dump(vercel_config, f, indent=2)
print("[SUCCESS] vercel.json clean single pachinko rewrite configured")

# Update index.html to point launcher button to /sacred-pachinko
index_path = os.path.join(root_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace any old window.open links for pachinko with /sacred-pachinko
content = re.sub(r'window\.open\([^)]*pachinko[^)]*\)', 'window.open("/sacred-pachinko","_blank")', content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)
print("[SUCCESS] Updated index.html launcher button to /sacred-pachinko")

print("[COMPLETE] Cleanup operation finished.")
