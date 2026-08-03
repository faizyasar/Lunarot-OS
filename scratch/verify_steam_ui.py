import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("1. ip component present:", "function ip({" in content)
print("2. Mouse parallax handler present:", "handleMouseMove = (e)" in content or "onMouseMove: handleMouseMove" in content)
print("3. Green Play button present:", "PLAY" in content and "#5cba02" in content)
print("4. Steam stats present:", "CLOUD STATUS" in content and "BEADS RECORD" in content)
print("5. Vessels who play present:", "VESSELS WHO PLAY" in content)
