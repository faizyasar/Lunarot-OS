import json

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

m_tag = 'script type="__bundler/template"'
pos = text.find(m_tag)
if pos != -1:
    s = text.find('>', pos) + 1
    e = text.find('</script>', s)
    template_str = text[s:e]
    print(f"Template content length: {len(template_str)}")
    
    try:
        data = json.loads(template_str)
        print("[SUCCESS] Template script content is 100% valid JSON!")
    except json.JSONDecodeError as err:
        print(f"[ERROR] Template JSON error at pos {err.pos}: {err}")
        err_pos = err.pos
        chunk = template_str[max(0, err_pos-50):min(len(template_str), err_pos+50)]
        print("Chunk around error:", repr(chunk.encode('ascii', errors='replace').decode('ascii')))
        print("Exact chars around error pos:", [f"chr({ord(c)})={repr(c)}" for c in template_str[max(0, err_pos-5):min(len(template_str), err_pos+5)]])
