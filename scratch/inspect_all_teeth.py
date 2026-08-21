import json
import struct

with open('scratch/gym_skeleton.glb', 'rb') as f:
    data = f.read()

json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

nodes = gltf.get('nodes', [])
meshes = gltf.get('meshes', [])

print("=== ALL GLTF MESHES & NODES RELATED TO HEAD/TEETH/SKULL ===")
for i, n in enumerate(nodes):
    name = n.get('name', '')
    m_idx = n.get('mesh')
    m_name = meshes[m_idx].get('name', '') if m_idx is not None and m_idx < len(meshes) else ''
    if any(k in name.lower() or k in m_name.lower() for k in ['tooth', 'teeth', 'dens', 'dentes', 'incisor', 'canine', 'molar', 'premolar', 'mandible', 'maxilla', 'cranium', 'head', 'skull']):
        print(f"Node {i:3d}: Name='{name}', MeshIdx={m_idx}, MeshName='{m_name}'")
