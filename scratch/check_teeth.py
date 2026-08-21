import json
import base64

with open('open3dviewer_skeletal_figure.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

b64 = lines[336].split('"')[1]
glb = base64.b64decode(b64)
json_len = int.from_bytes(glb[12:16], 'little')
json_data = glb[20:20+json_len].decode('utf-8')
data = json.loads(json_data)

maxilla = [m for m in data['meshes'] if 'Maxilla' in m['name']][0]
mandible = [m for m in data['meshes'] if 'Mandible' in m['name']][0]

print('Maxilla primitives:', maxilla['primitives'])
print('Mandible primitives:', mandible['primitives'])

# Let's check nodes to see if there are any hidden teeth nodes
nodes = [n.get('name') for n in data.get('nodes', [])]
teeth_nodes = [n for n in nodes if n and ('teeth' in n.lower() or 'tooth' in n.lower())]
print('Teeth nodes:', teeth_nodes)
