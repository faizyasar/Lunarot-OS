import os

src = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\nodes.txt'
dest = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem_data.js'

with open(src, 'r', encoding='utf-8') as f:
    data = f.read()

# Make it a valid JS file assigning to a global variable
js_content = f"const mysticalData = {data};\n"

with open(dest, 'w', encoding='utf-8') as f:
    f.write(js_content)
    
print("Created golem_data.js")
