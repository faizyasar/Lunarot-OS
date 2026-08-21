import sys

content = open('index.html', encoding='utf-8').read()

target = '.barcode-block{width:clamp(120px,14vw,160px);position:absolute;bottom:4vh;left:6.5%}'

new_css = "@media (max-width:768px){.panel-left{width:16%;min-width:48px;max-width:72px;justify-content:center;align-items:center}.gap-mid{width:1%}.gap-mid:after{opacity:.35}.panel-right{padding:0 2% 0 1%!important;align-items:flex-end;justify-content:center}.mark-wrap{width:100%;margin-left:0;margin-right:0;padding:0 2px}.mark{max-width:48px;width:100%;margin:0 auto}.mark-wrap>span{font-size:5.5px!important;letter-spacing:.1em!important;margin-top:4px!important;opacity:.7}.panel-right>div[style*='width']{width:100%!important;max-width:100%!important;padding-right:0!important}}"

replacement = target + new_css

if target in content:
    new_content = content.replace(target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Replacement successful!')
else:
    print('Target string not found in index.html!')
