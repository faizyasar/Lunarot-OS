import json
import struct

with open('scratch/gym_skeleton.glb', 'rb') as f:
    data = f.read()

json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

nodes = gltf.get('nodes', [])
meshes = gltf.get('meshes', [])

print("=== MANDIBLE NODE DETAILS ===")
for i, n in enumerate(nodes):
    name = n.get('name', '')
    if 'mandible' in name.lower() or 'sternum' in name.lower() or 'costal' in name.lower():
        print(f"Node {i:3d}: Name='{name}'")
        if 'translation' in n: print(f"         Translation: {n['translation']}")
        if 'rotation' in n: print(f"         Rotation (quat): {n['rotation']}")
        if 'matrix' in n: print(f"         Matrix: {n['matrix']}")
        if 'scale' in n: print(f"         Scale: {n['scale']}")
