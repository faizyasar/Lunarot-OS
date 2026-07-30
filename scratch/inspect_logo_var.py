import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

pos = content.find('alt:"LUNAROT Logo"')
if pos != -1:
    snippet = content[max(0, pos-200):min(len(content), pos+100)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Logo snippet:\n", safe_snippet)

    # Search for Y0 definition
    match_var = re.search(r'src:\s*([a-zA-Z0-9_$]+)', snippet)
    if match_var:
        var_name = match_var.group(1)
        print(f"\nSearching definition of var: {var_name}")
        def_pos = content.find(f"const {var_name}=")
        if def_pos == -1:
            def_pos = content.find(f"var {var_name}=")
        if def_pos == -1:
            def_pos = content.find(f"{var_name}=")
        if def_pos != -1:
            def_snippet = content[def_pos:def_pos+200]
            print("Var definition:\n", def_snippet[:150])
