import re
import sys
import subprocess
import tempfile

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
script2 = scripts[1]

with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False, encoding='utf-8') as temp:
    temp.write(script2)
    temp_path = temp.name

# Run node with --print to check syntax properly, or just use node -c
result = subprocess.run(['node', '-c', temp_path], capture_output=True, text=True, encoding='utf-8', errors='ignore')

if result.returncode != 0:
    err = result.stderr
    print("=== FULL ERROR ===")
    print(err)
    
    # Also extract the exact lines from temp_path to show the error
    match = re.search(r'\.js:(\d+)', err)
    if match:
        line_num = int(match.group(1))
        lines = script2.split('\n')
        print(f"\n=== CONTEXT AROUND LINE {line_num} ===")
        start = max(0, line_num - 10)
        end = min(len(lines), line_num + 10)
        for i in range(start, end):
            prefix = ">> " if i == line_num - 1 else "   "
            print(f"{prefix}{i+1}: {lines[i]}")
