import re

with open('golem.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the Lexicon block
start_marker = "// --- LEXICON DATA & MAPPING ---"
# We'll use a regex to capture everything from start_marker to the end of initLexiconMarkers
# initLexiconMarkers ends with `    });\n  }`
pattern = re.compile(r'(// --- LEXICON DATA & MAPPING ---.*?function initLexiconMarkers\(\) \{.*?\}\n)', re.DOTALL)
match = pattern.search(html)

if match:
    block = match.group(1)
    # Remove it from the original location
    html = html.replace(block, '')
    
    # Insert it right after <script>
    # Find <script>
    script_idx = html.find('<script>')
    if script_idx != -1:
        insert_pos = script_idx + len('<script>\n')
        html = html[:insert_pos] + block + '\n' + html[insert_pos:]
        
        with open('golem.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Successfully moved Lexicon block to the top of the script!")
    else:
        print("Could not find <script> tag.")
else:
    print("Could not find Lexicon block.")
