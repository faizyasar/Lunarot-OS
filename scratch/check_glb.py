import base64
import json
import re

with open('c:/Users/faizy/Documents/Lunarot Engine/Lunarot-Tarot-Engine-1.0/open3dviewer_skeletal_figure.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const GLB_BASE64 = "(.*?)";', content, re.DOTALL)
if match:
    b64_data = match.group(1)
    glb_data = base64.b64decode(b64_data)
    
    # GLB header is 12 bytes
    # chunk 0 header is 8 bytes
    
    json_chunk_length = int.from_bytes(glb_data[12:16], byteorder='little')
    json_chunk_type = glb_data[16:20]
    
    if json_chunk_type == b'JSON':
        json_data = glb_data[20:20+json_chunk_length].decode('utf-8')
        data = json.loads(json_data)
        
        print("Has skins:", 'skins' in data)
        if 'skins' in data:
            print("Number of skins:", len(data['skins']))
            
        print("Number of nodes:", len(data.get('nodes', [])))
        
        node_names = [n.get('name', 'unnamed') for n in data.get('nodes', [])]
        print("Sample node names:")
        for name in node_names[:20]:
            print(f" - {name}")
            
        print("Mandible nodes found:", [n for n in node_names if 'mandible' in n.lower()])
    else:
        print("No JSON chunk found.")
else:
    print("Base64 string not found.")
