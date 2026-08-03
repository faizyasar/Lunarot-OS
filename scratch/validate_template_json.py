import json

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

m_tag = 'script type="__bundler/template"'
pos = text.find(m_tag)
if pos != -1:
    s = text.find('{', pos)
    e = text.find('</script>', s)
    template_str = text[s:e]
    print(f"Template string length: {len(template_str)}")
    try:
        data = json.loads(template_str)
        print("[SUCCESS] Template JSON is 100% valid!")
    except json.JSONDecodeError as err:
        print(f"[ERROR] Template JSON error at pos {err.pos}: {err}")
        snippet = template_str[max(0, err.pos-50):min(len(template_str), err.pos+50)]
        ascii_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
        print("Snippet around error:", repr(ascii_snippet))
        print("Byte values around error:", [ord(c) for c in template_str[max(0, err.pos-5):min(len(template_str), err.pos+5)]])
