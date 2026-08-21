import re

with open('golem.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update EXACT_PRESETS
presets_replacements = {
    'full':   "{ target: new BABYLON.Vector3(-77.1, 85.0, 0.0), radius: 210.0, alpha: 1.76, beta: 1.56, title: 'Full Tree', sub: 'Sephirotic Skeleton' }",
    'chokhmah':"{ target: new BABYLON.Vector3(-10.0, 151.1, 4.0), radius: 17.4, alpha: 2.17, beta: 1.44, title: 'Chokhmah', sub: 'Wisdom' }",
    'binah':  "{ target: new BABYLON.Vector3(9.9, 150.0, 5.0), radius: 17.4, alpha: -0.23, beta: 1.82, title: 'Binah', sub: 'Understanding' }",
    'chesed': "{ target: new BABYLON.Vector3(-25.2, 120.0, 2.2), radius: 35.0, alpha: 0.26, beta: 1.75, title: 'Chesed', sub: 'Mercy / Grace' }",
    'gevurah':"{ target: new BABYLON.Vector3(25.2, 120.1, 2.2), radius: 35.0, alpha: -0.61, beta: 1.44, title: 'Gevurah', sub: 'Severity / Justice' }",
    'netzach':"{ target: new BABYLON.Vector3(-15.0, 60.0, 0.0), radius: 81.0, alpha: 0.43, beta: 1.16, title: 'Netzach', sub: 'Victory / Endurance' }",
    'hod':    "{ target: new BABYLON.Vector3(14.9, 60.0, 0.0), radius: 65.0, alpha: -1.43, beta: 2.47, title: 'Hod', sub: 'Splendor / Submission' }",
    'malkhut':"{ target: new BABYLON.Vector3(-0.0, 16.0, 10.0), radius: 50.0, alpha: 0.54, beta: 3.06, title: 'Malkhut', sub: 'Kingdom / Immanence' }"
}

for key, new_val in presets_replacements.items():
    pattern = rf"'{key}':\s*\{{[^\}}]+\}}"
    content = re.sub(pattern, f"'{key}':  {new_val}", content)


# 2. Update the Sephirot Overlay CSS and JS to put the Lexicon on the right side
# Find the CSS block for .sephirah-marker and change it to a flex list style
old_css = """  .sephirah-marker {
    position: absolute;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    opacity: 0;
    transition: opacity 0.5s ease;
  }"""
new_css = """  .sephirah-marker {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 2px;
    opacity: 0;
    transition: opacity 0.5s ease;
  }"""
content = content.replace(old_css, new_css)

old_sephirot_overlay = """  #sephirot-overlay {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 5;
  }"""
new_sephirot_overlay = """  #sephirot-overlay {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 5;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-end;
    padding-right: 80px;
    gap: 12px;
  }"""
content = content.replace(old_sephirot_overlay, new_sephirot_overlay)


# Remove the 3D Tracking logic inside the loop and just make them visible if showMarkers
tracking_loop_regex = r"for\s*\(\s*const key of Object\.keys\(sephirotMarkers\)\s*\)\s*\{.*?marker\.classList\.remove\('visible'\);\s*\}\s*\}"
new_tracking_loop = """for (const key of Object.keys(sephirotMarkers)) {
          const marker = sephirotMarkers[key];
          if (showMarkers) {
             marker.classList.add('visible');
             // Hide the white dot since it's a lexicon now
             const dot = marker.querySelector('.dot');
             if (dot) dot.style.display = 'none';
          } else {
             marker.classList.remove('visible');
          }
       }"""
content = re.sub(tracking_loop_regex, new_tracking_loop, content, flags=re.DOTALL)


with open('golem.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Presets updated and lexicon moved to the right.")
