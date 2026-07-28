import subprocess

# Let's inspect index.html at commit 5419300
result = subprocess.run(["git", "show", "5419300:index.html"], capture_output=True, cwd=r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0")

content = result.stdout.decode('utf-8', errors='ignore')

print(f"5419300 index.html length: {len(content)}")
print(f"Starts with: {content[:100]}")
