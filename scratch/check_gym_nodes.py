import json
import struct

with open('scratch/gym_skeleton.glb', 'rb') as f:
    data = f.read()

json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

print("=== ALL BONE NODES IN GYM_SKELETON.GLB ===")
for i, n in enumerate(gltf.get('nodes', [])):
    print(f"{i:3d}: {n.get('name')}")
