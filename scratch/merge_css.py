old = open('index.html', encoding='utf-8').read()
new = open('C:\\Users\\faizy\\Downloads\\Lunarot-OS-v6.8-Standalone-mobile-login (1).html', encoding='utf-8').read()

marker = '.power-cluster{align-items:flex-end;gap:4px;display:flex}'
start_str = '@media(max-width:768px){.panels{overflow:hidden;'

idx_old = old.find(start_str)
end_old = old.find(marker, idx_old)
old_css = old[idx_old:end_old]

idx_new = new.find(start_str)
end_new = new.find(marker, idx_new)
new_css = new[idx_new:end_new]

if not new_css.endswith('}'):
    print('Appending missing closing brace to new CSS')
    new_css += '}'

old = old.replace(old_css, new_css)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(old)
print(f'Replaced CSS! Length old={len(old_css)}, new={len(new_css)}')
