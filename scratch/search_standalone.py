with open(r'C:\Users\faizy\Downloads\standalone (1).html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "Ein Sof" in line or "Ein%20Sof" in line or "Lexicon" in line:
        print(f"Found on line {i+1}: {line.strip()[:200]}")
