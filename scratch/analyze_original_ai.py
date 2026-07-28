import re

with open(r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\original_ai_function.js", "r", encoding="utf-8") as f:
    code = f.read()

print(f"Code length: {len(code)}")

# Search for return statement in ai
pos_return = code.find("return s.jsxs(\"div\",{className:\"flex-1 flex flex-col")
if pos_return != -1:
    snippet = code[pos_return:pos_return+3000]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Return statement snippet:\n", safe_snippet[:1500])
else:
    print("Return statement not found with exact match, searching return s.jsxs")
    pos_ret2 = code.find("return s.")
    if pos_ret2 != -1:
        snippet2 = code[pos_ret2:pos_ret2+1500]
        safe_snippet2 = snippet2.encode('ascii', errors='replace').decode('ascii')
        print("Return snippet:\n", safe_snippet2)
