import subprocess
import re

# Get the original index.html from commit prior to our changes today (e.g. 5419300 or HEAD~20)
result = subprocess.run(["git", "show", "4006ef0~1:index.html"], capture_output=True, cwd=r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0")

content = result.stdout.decode('utf-8', errors='ignore')

print(f"Original index.html length: {len(content)}")

# 1. Search for how xp() rendered main window content in original index.html
pos_xp = content.find("v===\"/apps/sacred-draw.bin\"")
if pos_xp != -1:
    snippet = content[max(0, pos_xp-100):min(len(content), pos_xp+800)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Original xp() rendering snippet:\n", safe_snippet)

# 2. Search for how markdown / research log window was structured in original index.html
pos_ai = content.find("function ai(")
if pos_ai != -1:
    snippet_ai = content[pos_ai:pos_ai+1000]
    safe_snippet_ai = snippet_ai.encode('ascii', errors='replace').decode('ascii')
    print("\nOriginal ai() function snippet:\n", safe_snippet_ai[:600])

# 3. Search for vp array in original index.html
pos_vp = content.find("const vp=[")
if pos_vp != -1:
    snippet_vp = content[pos_vp:pos_vp+400]
    safe_snippet_vp = snippet_vp.encode('ascii', errors='replace').decode('ascii')
    print("\nOriginal vp array snippet:\n", safe_snippet_vp)
