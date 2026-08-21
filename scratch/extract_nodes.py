import re
import json

filepath = r'C:\Users\faizy\Downloads\standalone (1).html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We can find the array of objects. It looks like `const nodes = [{id:"keter",...}, ...]`
# Let's search for "LEGS & FEET" and extract the whole array manually or via regex.
match = re.search(r'\[\{id:"keter".*?\]\}\]', content)
if match:
    data = match.group(0)
    with open(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\nodes.txt', 'w', encoding='utf-8') as out:
        out.write(data)
    print("Found nodes array!")
else:
    print("Could not find nodes array.")
