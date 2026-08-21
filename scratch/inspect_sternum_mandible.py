import json
import struct

with open('scratch/gym_skeleton.glb', 'rb') as f:
    data = f.read()

json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

nodes = gltf.get('nodes', [])
meshes = gltf.get('meshes', [])

print("=== MANDIBLE & STERNUM NODES AND PARENT HIERARCHY ===")
for i, n in enumerate(nodes):
    name = n.get('name', '')
    if any(k in name.lower() for k in ['mandible', 'sternum', 'manubrium', 'xiphoid', 'costal']):
        t = n.get('translation', [0, 0, 0])
        r = n.get('rotation', [0, 0, 0, 1])
        s = n.get('scale', [1, 1, 1])
        m_idx = n.get('mesh')
        print(f"Node {i:3d}: Name='{name}', Translation={t}, Scale={s}, MeshIdx={m_idx}")
