import re
import os

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"
target_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"
public_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\public\style-guide.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    index_content = f.read()

# Extract Data URL #1
match = re.search(r'data:image/webp;base64,[^"]+', index_content)
if not match:
    print("[ERROR] Data URL not found")
    exit(1)

y0_str = match.group(0)
print(f"[FOUND] Base64 Logo URL ({len(y0_str)} chars)")

with open(target_file, "r", encoding="utf-8") as f:
    sg_content = f.read()

# Check if section 00 already exists
if 'id="logo"' in sg_content:
    print("[INFO] Logo section already exists")
else:
    logo_section_html = f'''
    <!-- SECTION 00: LUNAROT OS LOGO MARK -->
    <section id="logo" class="space-y-6">
      <div class="border-b border-white/15 pb-3 flex justify-between items-end">
        <div>
          <h2 class="font-cinzel text-xl font-bold text-white tracking-widest uppercase flex items-center gap-2">
            <span class="text-white">✦</span> 00. OFFICIAL LUNAROT OS LOGO MARK
          </h2>
          <p class="font-mono text-xs text-zinc-500 mt-1">Official Base64 WebP logo mark used on front page, lockscreen intake, and brand headers.</p>
        </div>
      </div>

      <div class="gothic-panel panel-white flex flex-col md:flex-row items-center justify-between gap-8 p-8">
        <span class="panel-title-tag">BRAND_MARK // LOGO_SPECIMEN</span>
        
        <div class="flex flex-col items-center justify-center p-6 bg-black/80 border border-white/20 w-full md:w-80 shadow-2xl">
          <img src="{y0_str}" alt="Lunarot OS Logo Mark" class="w-52 h-auto object-contain filter drop-shadow-[0_0_15px_rgba(255,255,255,0.3)]">
          <span class="font-mono text-[9px] text-[#838aa0] tracking-[0.25em] uppercase mt-4 block text-center font-bold">LUNAROT OS // BRAND MARK</span>
        </div>

        <div class="flex-1 space-y-4 font-mono text-xs text-[#cfc9c0]">
          <div class="space-y-1 border-b border-white/10 pb-3">
            <span class="text-white font-bold tracking-wider uppercase block">// LOGO ASSET SPECIFICATION</span>
            <p class="text-[11px] text-zinc-400 font-sans leading-relaxed">High-resolution inline WebP asset embedded natively across single-file builds. Inverted monochrome contrast with glass glow filters.</p>
          </div>

          <div class="grid grid-cols-2 gap-4 text-[10px]">
            <div>
              <span class="text-zinc-500 block">ASSET FORMAT:</span>
              <span class="text-white font-bold">WEBP / BASE64 (192 KB)</span>
            </div>
            <div>
              <span class="text-zinc-500 block">RENDER CONTEXT:</span>
              <span class="text-white font-bold">INTAKE & HEADER</span>
            </div>
          </div>

          <button onclick="copyCode(this, `<img src=&quot;{y0_str[:50]}...&quot; alt=&quot;Lunarot OS Logo&quot; class=&quot;w-48 h-auto object-contain&quot;>`)" class="gothic-btn-white w-full py-2.5 text-[10px]">
            [ COPY LOGO MARKUP ]
          </button>
        </div>

        <span class="panel-footer-tag">BRAND_ASSET</span>
      </div>
    </section>
'''

    target_marker = '<section id="colors"'
    if target_marker in sg_content:
        sg_content = sg_content.replace(target_marker, logo_section_html + "\n\n    " + target_marker)
        print("[SUCCESS] Inserted Logo Specimen Section into style-guide.html")

    # Add 00. Logo link to header nav
    nav_marker = '<a href="#colors"'
    if nav_marker in sg_content and '00. Logo' not in sg_content:
        sg_content = sg_content.replace(nav_marker, '<a href="#logo" class="px-3 py-1.5 border border-white/15 text-zinc-400 hover:text-white hover:border-white transition-all">00. Logo Mark</a>\n      ' + nav_marker)
        print("[SUCCESS] Added Logo Mark to header nav")

with open(target_file, "w", encoding="utf-8") as f:
    f.write(sg_content)

with open(public_file, "w", encoding="utf-8") as f:
    f.write(sg_content)

print("[COMPLETE] add_logo_to_style_guide script finished.")
