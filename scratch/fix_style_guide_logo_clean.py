import re
import os

target_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\style-guide.html"
public_file = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\public\style-guide.html"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the giant src="data:image/webp..." with clean src="lunarot-logo.webp"
new_logo_section = '''    <!-- SECTION 00: LUNAROT OS LOGO MARK -->
    <section id="logo" class="space-y-6">
      <div class="border-b border-white/15 pb-3 flex justify-between items-end">
        <div>
          <h2 class="font-cinzel text-xl font-bold text-white tracking-widest uppercase flex items-center gap-2">
            <span class="text-white">✦</span> 00. OFFICIAL LUNAROT OS LOGO MARK
          </h2>
          <p class="font-mono text-xs text-zinc-500 mt-1">Official logo mark rendered directly on the login / lockscreen intake portal.</p>
        </div>
      </div>

      <div class="gothic-panel panel-white flex flex-col md:flex-row items-center justify-between gap-8 p-8">
        <span class="panel-title-tag">BRAND_MARK // LOGO_SPECIMEN</span>
        
        <div class="flex flex-col items-center justify-center p-6 bg-black/80 border border-white/20 w-full md:w-80 shadow-2xl">
          <img src="lunarot-logo.webp" alt="Lunarot OS Logo Mark" class="w-52 h-auto object-contain filter drop-shadow-[0_0_15px_rgba(255,255,255,0.4)]">
          <span class="font-mono text-[9px] text-[#838aa0] tracking-[0.25em] uppercase mt-4 block text-center font-bold">LUNAROT OS // BRAND MARK</span>
        </div>

        <div class="flex-1 space-y-4 font-mono text-xs text-[#cfc9c0]">
          <div class="space-y-1 border-b border-white/10 pb-3">
            <span class="text-white font-bold tracking-wider uppercase block">// LOGO ASSET SPECIFICATION</span>
            <p class="text-[11px] text-zinc-400 font-sans leading-relaxed">High-resolution WebP asset embedded natively on login portal intake. Inverted monochrome contrast with glass glow filters.</p>
          </div>

          <div class="grid grid-cols-2 gap-4 text-[10px]">
            <div>
              <span class="text-zinc-500 block">ASSET FILENAME:</span>
              <span class="text-white font-bold">lunarot-logo.webp (144 KB)</span>
            </div>
            <div>
              <span class="text-zinc-500 block">RENDER CONTEXT:</span>
              <span class="text-white font-bold">INTAKE & HEADER</span>
            </div>
          </div>

          <button onclick="copyCode(this, `<img src=\\&quot;lunarot-logo.webp\\&quot; alt=\\&quot;Lunarot OS Logo\\&quot; class=\\&quot;w-48 h-auto object-contain\\&quot;>`)" class="gothic-btn-white w-full py-2.5 text-[10px]">
            [ COPY LOGO MARKUP ]
          </button>
        </div>

        <span class="panel-footer-tag">BRAND_ASSET</span>
      </div>
    </section>'''

pattern = r'<!-- SECTION 00: LUNAROT OS LOGO MARK -->.*?</section>'
if re.search(pattern, content, re.DOTALL):
    content = re.sub(pattern, new_logo_section, content, flags=re.DOTALL)
    print("[SUCCESS] Replaced Logo Section with clean src='lunarot-logo.webp'")

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

with open(public_file, "w", encoding="utf-8") as f:
    f.write(content)

print("[COMPLETE] fix_style_guide_logo_clean script finished.")
