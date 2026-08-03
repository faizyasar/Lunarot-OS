import base64
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("public/sacred-pachinko.html", "r", encoding="utf-8") as f:
    content = f.read()

print("=== PUBLIC/SACRED-PACHINKO.HTML DECODED / BUNDLE INSPECTION ===")
print("Total length:", len(content))

# Check for canvas/body/style in sacred-pachinko.html
styles = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
print(f"Found {len(styles)} style tags in sacred-pachinko.html")
for i, s in enumerate(styles):
    print(f"\n--- STYLE {i+1} ---")
    print(s[:500])

# Check for canvas elements or body tags
print("\nBody / Canvas tags:")
for m in re.finditer(r'<(?:body|canvas|div id="app"|div class="stage")[^>]*>', content):
    print("  ", m.group(0))

