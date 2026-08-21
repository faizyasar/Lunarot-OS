import sys

content = open('index.html', encoding='utf-8').read()
idx = content.find('te=_=>{H(b=>{')
target = content[idx:idx+249]

replacement = target.replace(
    'q=()=>{Y(new Set),V(!1)};',
    'q=()=>{Y(new Set),V(!1)};D.useEffect(()=>{const h=e=>{if(e.data&&e.data.type==="LUNAROT_FOCUS"){p(curr=>(curr==="/db/tarot.index"||curr==="/db/music.index")?"":curr)}};window.addEventListener("message",h);return ()=>window.removeEventListener("message",h)},[]);'
)

if target in content:
    new_content = content.replace(target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Replacement successful!')
else:
    print('Target string not found in index.html!')
