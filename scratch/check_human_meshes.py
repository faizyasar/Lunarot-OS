import json
import struct

data = open('scratch/human_skeleton.glb', 'rb').read()
json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

for i, m in enumerate(gltf.get('meshes', [])):
    print(f"Mesh {i}: {m.get('name')}")
    for p in m.get('primitives', []):
        mat_idx = p.get('material')
        mat = gltf['materials'][mat_idx] if mat_idx is not None else None
        print(f"  Material: {mat.get('name') if mat else 'None'}")
