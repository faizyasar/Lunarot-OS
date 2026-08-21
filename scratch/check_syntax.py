import re
import sys
import subprocess
import tempfile

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
print(f"Found {len(scripts)} scripts in index.html")

for idx, script in enumerate(scripts):
    with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False, encoding='utf-8') as temp:
        temp.write(script)
        temp_path = temp.name
    
    try:
        # Run node -c (check syntax only)
        result = subprocess.run(['node', '-c', temp_path], capture_output=True, text=True, encoding='utf-8', errors='ignore')
        if result.returncode != 0:
            print(f"--- SCRIPT {idx+1} HAS SYNTAX ERROR ---")
            print(result.stderr.split('\n')[0:10]) # Print first 10 lines of stderr
        else:
            print(f"Script {idx+1} syntax OK.")
    except Exception as e:
        print(f"Error checking script {idx+1}: {e}")
