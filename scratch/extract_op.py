import subprocess
import re

result = subprocess.run(["git", "show", "HEAD~10:index.html"], capture_output=True, cwd=r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0")

content = result.stdout.decode('utf-8', errors='ignore')

pos = content.find("op=`")
if pos != -1:
    snippet = content[pos:pos+1500]
    safe_snippet = snippet.encode('ascii', errors='replace').decode('ascii')
    print("Exact original op string:\n", safe_snippet)
