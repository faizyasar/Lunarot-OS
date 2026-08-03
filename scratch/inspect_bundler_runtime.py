import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

s_first = text.find('<script>')
e_first = text.find('</script>', s_first)

first_script = text[s_first+8:e_first]

print("First script length:", len(first_script))

pos = first_script.find('JSON.parse')
while pos != -1:
    print(f"JSON.parse match at {pos}:", repr(first_script[max(0, pos-20):min(len(first_script), pos+60)]))
    pos = first_script.find('JSON.parse', pos + 1)
