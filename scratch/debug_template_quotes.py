import json

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

m_tag = 'script type="__bundler/template"'
pos = text.find(m_tag)
s = text.find('>', pos) + 1
e = text.find('</script>', s)
template_str = text[s:e]

pos_str = template_str.find('TarotStandaloneView')
print("TarotStandaloneView pos in template_str:", pos_str)

# Find quote before pos_str
quote_start = template_str.rfind('"', 0, pos_str)
print("Quote start:", quote_start, repr(template_str[quote_start:pos_str]))

# Check if quote is escaped or unescaped
print("Chars before quote_start:", repr(template_str[quote_start-5:quote_start+5]))
