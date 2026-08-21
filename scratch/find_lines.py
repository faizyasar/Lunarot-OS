with open('golem.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "btn-preset-full" in line:
        print(f"Line {i+1}: {line.strip()}")
    if "window.activePresetKey =" in line:
        print(f"Line {i+1}: {line.strip()}")
    if "focusPreset('full')" in line:
        print(f"Line {i+1}: {line.strip()}")
