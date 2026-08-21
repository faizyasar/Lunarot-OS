import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/old_index.html", "r", encoding="utf-16le") as f:
    content = f.read()

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Restored original index.html!")
