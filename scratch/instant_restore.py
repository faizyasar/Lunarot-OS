import os
import shutil

src_webp = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\tarot_fast_slow.webp'
out_desktop_webp = r'C:\Users\faizy\Desktop\lunarot_tarot_deck_spinning.webp'

if os.path.exists(src_webp):
    shutil.copy2(src_webp, out_desktop_webp)
    print("Directly copied tarot_fast_slow.webp to Desktop:", os.path.getsize(out_desktop_webp), "bytes")
else:
    print("Source not found")
