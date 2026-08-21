import sys

content = open('index.html', encoding='utf-8').read()

target = 'te=_=>{H(b=>{const U=new Set(b);return U.has(_)?U.delete(_):U.add(_),U})},q=()=>{Y(new Set),V(!1)};D.useEffect(()=>{if(!c){K("chancellery of the void");return}switch(v){case"/apps/sacred-draw.bin":K("SACRED GEOMETRY CANVAS // DRAW TO CONJURE");'

replacement = 'te=_=>{H(b=>{const U=new Set(b);return U.has(_)?U.delete(_):U.add(_),U})},q=()=>{Y(new Set),V(!1)};D.useEffect(()=>{const h=e=>{if(e.data&&e.data.type==="LUNAROT_FOCUS"){p(curr=>(curr==="/db/tarot.index"||curr==="/db/music.index")?"":curr)}};window.addEventListener("message",h);return ()=>window.removeEventListener("message",h)},[]);D.useEffect(()=>{if(!c){K("chancellery of the void");return}switch(v){case"/apps/sacred-draw.bin":K("SACRED GEOMETRY CANVAS // DRAW TO CONJURE");'

if target in content:
    new_content = content.replace(target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Replacement successful!')
else:
    print('Target string not found in index.html!')
