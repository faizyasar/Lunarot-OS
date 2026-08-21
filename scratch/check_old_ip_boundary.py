import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/old_index.html", "r", encoding="utf-16le") as f:
    content = f.read()

idx_start = content.find("function ip({")
if idx_start != -1:
    idx_next_fn = content.find("function ", idx_start + 20)
    if idx_next_fn == -1:
        idx_next_fn = content.find("const ", idx_start + 20)
        
    print("Found idx_start:", idx_start)
    print("Found idx_next_fn:", idx_next_fn)
    print("Code at idx_next_fn:", repr(content[idx_next_fn-50:idx_next_fn+50]))
