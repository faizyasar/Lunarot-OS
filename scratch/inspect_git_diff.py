import subprocess
import re

result = subprocess.run(["git", "show", "HEAD~10:index.html"], capture_output=True, cwd=r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0")

content = result.stdout.decode('utf-8', errors='ignore')

# Search for op or social conduit variable definition
for m in re.finditer(r'op\s*=|social-conduit|social|letterboxd', content, re.IGNORECASE):
    idx = m.start()
    snippet = content[max(0, idx-50):min(len(content), idx+150)]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii').replace('\n', ' ')
    print(f"Match at {idx}: {safe_snippet}")
