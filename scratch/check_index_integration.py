import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

has_component = "function TarotStandaloneView" in text
has_iframe_src = "/tarot-standalone.html" in text
has_render_hook = 'v==="/db/tarot-directory.index"&&s.jsx(TarotStandaloneView' in text

print(f"TarotStandaloneView Component defined: {has_component}")
print(f"Iframe src /tarot-standalone.html: {has_iframe_src}")
print(f"tarot-directory.index render hook updated: {has_render_hook}")
