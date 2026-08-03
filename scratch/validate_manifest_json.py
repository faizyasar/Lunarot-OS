import json

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

m_tag = 'script type="__bundler/manifest"'
pos = text.find(m_tag)
if pos != -1:
    s = text.find('{', pos)
    e = text.find('</script>', s)
    manifest_str = text[s:e]
    print(f"Manifest string length: {len(manifest_str)}")
    try:
        data = json.loads(manifest_str)
        print("[SUCCESS] Manifest JSON is 100% valid!")
    except json.JSONDecodeError as err:
        print(f"[ERROR] Manifest JSON error: {err}")
        print("Char around error:", repr(manifest_str[max(0, err.pos-40):min(len(manifest_str), err.pos+40)]))
else:
    print("[ERROR] Manifest script tag not found")
