import json
import struct

with open('scratch/gym_skeleton.glb', 'rb') as f:
    data = f.read()

json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

nodes = gltf.get('nodes', [])
meshes = gltf.get('meshes', [])

print("=== ALL SKULL / NOSE / TEETH RELATED NODES & MESHES ===")
for i, n in enumerate(nodes):
    name = n.get('name', '')
    m_idx = n.get('mesh')
    if any(k in name.lower() for k in ['nasal', 'cartilage', 'teeth', 'tooth', 'incisor', 'canine', 'molar', 'maxilla', 'mandible', 'dent', 'alveolar']):
        print(f"Node {i:3d}: Name='{name}', MeshIdx={m_idx}")
        if m_idx is not None and m_idx < len(meshes):
            m_name = meshes[m_idx].get('name', '')
            print(f"         Mesh Name='{m_name}'")
