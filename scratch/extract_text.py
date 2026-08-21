import re
import json

filepath = r'C:\Users\faizy\Downloads\standalone (1).html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

strings = re.findall(r'"([^"\\]{30,})"', content)
prose = list(set([s for s in strings if ' ' in s and not 'function' in s and not '{' in s and not '<' in s and not 'return ' in s]))

with open(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\extracted_text.json', 'w', encoding='utf-8') as f:
    json.dump(prose, f, indent=2, ensure_ascii=False)
