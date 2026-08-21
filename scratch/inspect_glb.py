import json
import struct

with open('scratch/open3dviewer_src/3dmodels/overview-demo/overview-demo.glb', 'rb') as f:
    data = f.read()

magic, version, length = struct.unpack('<III', data[:12])
json_len, json_type = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

print("=== NODES ===")
for i, n in enumerate(gltf.get('nodes', [])):
    name = n.get('name', 'unnamed')
    mesh_idx = n.get('mesh')
    children = n.get('children', [])
    print(f"Node {i}: name='{name}', mesh={mesh_idx}, children={children}")

print("\n=== MESHES ===")
for i, m in enumerate(gltf.get('meshes', [])):
    print(f"Mesh {i}: name='{m.get('name')}'")
