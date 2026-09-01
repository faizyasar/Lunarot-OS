import os

desktop_html_path = r'C:\Users\faizy\Desktop\HTMLS\Lunarot Tarot Deck (Spinning Transparent).html'
with open(desktop_html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Make the auto-spin slow, smooth, relaxed and hypnotic (0.25 degrees per frame -> ~24 seconds per full 360 rotation)
# Or for a nice ~6-8s rotation: 0.8 / 0.5
text = text.replace('currentY = (currentY + 1.2) % 360;', 'currentY = (currentY + 0.3) % 360;')
text = text.replace('currentY = (currentY + 0.6) % 360;', 'currentY = (currentY + 0.3) % 360;')

with open(desktop_html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Desktop HTML live spin speed to slow smooth drift (0.3 deg/frame)")
