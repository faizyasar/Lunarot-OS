import re
import json

with open(r'C:\Users\faizy\Downloads\standalone (1).html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's try to find a JSON object containing the lexicon terms
matches = re.search(r'const lexiconData = (\[.*?\]);', c, re.DOTALL)
if matches:
    print('Found lexiconData!')
    print(matches.group(1)[:500] + '...')
    
    # Save the full lexicon data to a file for easier viewing
    with open('scratch/lexiconData.js', 'w', encoding='utf-8') as out:
        out.write("const lexiconData = " + matches.group(1) + ";")
else:
    print('lexiconData not found, looking for alternative structures...')
