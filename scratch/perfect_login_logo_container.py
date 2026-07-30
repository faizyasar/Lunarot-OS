import os

target_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"
public_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\public\style-guide.html"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# Enhance login page logo description
content = content.replace(
    '<p class="font-mono text-xs text-zinc-500 mt-1">Official Base64 WebP logo mark used on front page, lockscreen intake, and brand headers.</p>',
    '<p class="font-mono text-xs text-zinc-500 mt-1">Official Base64 WebP logo mark rendered directly on the login / lockscreen intake portal.</p>'
)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

with open(public_file, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Refined login logo description in style-guide.html")
