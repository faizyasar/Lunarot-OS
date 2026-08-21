import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

backup_path = r"C:\Users\faizy\Desktop\Lunarot OS 671341.html"
current_path = "index.html"

# Detect encoding of the backup file
try:
    with open(backup_path, 'r', encoding='utf-8') as f:
        backup = f.read()
except UnicodeDecodeError:
    with open(backup_path, 'r', encoding='utf-16le') as f:
        backup = f.read()

# We need the favicons from the current app (which we already know from the previous script output)
favicons = [
    '<link rel="icon" type="image/webp" href="/favicon.webp?v=671341">',
    '<link rel="icon" type="image/x-icon" href="/favicon.ico?v=671341">'
]

backup_favicons = re.findall(r'<link[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*>', backup, re.IGNORECASE)

# Remove old favicons
for b_fav in backup_favicons:
    backup = backup.replace(b_fav, '')

# Inject new favicons
head_end = backup.find('</head>')
if head_end != -1:
    backup = backup[:head_end] + '\n  ' + '\n  '.join(favicons) + '\n' + backup[head_end:]

with open(current_path, 'w', encoding='utf-8') as f:
    f.write(backup)

print("Restored backup and injected favicons!")
