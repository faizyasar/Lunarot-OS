import json
import re

with open(r'C:\Users\faizy\Downloads\standalone (1).html', 'r', encoding='utf-8') as f:
    c = f.read()

# The minified bundle likely assigns this array to a variable or passes it.
# Let's use a regex to capture an array of objects that has "Ein Sof".
# We'll look for: [{... "Ein Sof" ...}]
match = re.search(r'(\[\{.*?"Ein Sof".*?\}\])', c)
if match:
    try:
        data = json.loads(match.group(1))
        with open('scratch/extracted_lexicon.json', 'w', encoding='utf-8') as out:
            json.dump(data, out, indent=2, ensure_ascii=False)
        print("Successfully extracted to scratch/extracted_lexicon.json")
    except Exception as e:
        print("Found array but failed to parse JSON:", e)
        # If it's a JS object without quotes around keys, it's not valid JSON.
        # Just write the raw JS string to a file.
        with open('scratch/extracted_lexicon_raw.js', 'w', encoding='utf-8') as out:
            out.write("const lexicon = " + match.group(1) + ";")
        print("Wrote raw JS to scratch/extracted_lexicon_raw.js")
else:
    # If the array doesn't match easily, let's just dump the block containing Ein Sof
    starts = [m.start() for m in re.finditer(r'Ein Sof', c)]
    if starts:
        s = starts[0]
        with open('scratch/extracted_lexicon_raw.js', 'w', encoding='utf-8') as out:
            out.write(c[max(0, s-2000):min(len(c), s+10000)])
        print("Wrote raw block to scratch/extracted_lexicon_raw.js")
    else:
        print("Could not find 'Ein Sof' at all.")
