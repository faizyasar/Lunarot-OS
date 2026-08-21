import re
import sys
import subprocess
import tempfile

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)

script2 = scripts[1]
lines = script2.split('\n')

with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False, encoding='utf-8') as temp:
    temp.write(script2)
    temp_path = temp.name

result = subprocess.run(['node', '-c', temp_path], capture_output=True, text=True, encoding='utf-8', errors='ignore')
if result.returncode != 0:
    print("=== SYNTAX ERROR IN SCRIPT 2 ===")
    err = result.stderr.split('\n')
    print('\n'.join(err[:10]))
    
    # Try to extract line number
    match = re.search(r'\.js:(\d+)', err[0])
    if match:
        line_num = int(match.group(1))
        print(f"\n=== CONTEXT AROUND LINE {line_num} ===")
        start = max(0, line_num - 5)
        end = min(len(lines), line_num + 5)
        for i in range(start, end):
            prefix = ">> " if i == line_num - 1 else "   "
            print(f"{prefix}{i+1}: {lines[i]}")
