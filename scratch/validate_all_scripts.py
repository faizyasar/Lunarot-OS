import json

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

pos = 0
while True:
    s_idx = text.find('<script', pos)
    if s_idx == -1:
        break
    tag_end = text.find('>', s_idx)
    close_idx = text.find('</script>', tag_end)
    tag = text[s_idx:tag_end+1]
    content = text[tag_end+1:close_idx].strip()
    print(f"Script tag: {tag[:80]} | Content len: {len(content)}")
    if content.startswith('{') or content.startswith('['):
        try:
            json.loads(content)
            print(" -> Valid JSON")
        except json.JSONDecodeError as err:
            print(f" -> JSON ERROR at pos {err.pos}: {err}")
            snippet = content[max(0, err.pos-40):min(len(content), err.pos+40)]
            print(" -> Snippet:", repr(snippet))
    pos = close_idx + 9
