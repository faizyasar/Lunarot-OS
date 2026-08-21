import json
import struct

with open('scratch/gym_skeleton.glb', 'rb') as f:
    data = f.read()

json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

print("=== INSPECTING GLTF ACCESSORS & BOUNDS ===")
accessors = gltf.get('accessors', [])
nodes = gltf.get('nodes', [])
meshes = gltf.get('meshes', [])

mesh_nodes = {}
for i, n in enumerate(nodes):
    m_idx = n.get('mesh')
    if m_idx is not None:
        mesh_nodes[m_idx] = n.get('name', f'Node_{i}')

min_y_global = float('inf')
max_y_global = float('-inf')

for i, m in enumerate(meshes):
    name = mesh_nodes.get(i, m.get('name', f'Mesh_{i}'))
    primitives = m.get('primitives', [])
    for p in primitives:
        pos_acc_idx = p.get('attributes', {}).get('POSITION')
        if pos_acc_idx is not None:
            acc = accessors[pos_acc_idx]
            min_val = acc.get('min')
            max_val = acc.get('max')
            if min_val and max_val:
                min_y_global = min(min_y_global, min_val[1])
                max_y_global = max(max_y_global, max_val[1])
                center_y = (min_val[1] + max_val[1]) / 2.0
                height = max_val[1] - min_val[1]
                print(f"Name: {name:35s} | Y min: {min_val[1]:7.3f}, Y max: {max_val[1]:7.3f}, Center Y: {center_y:7.3f}")

print(f"\nGLOBAL BOUNDS Y: min={min_y_global:.3f}, max={max_y_global:.3f}, total_height={max_y_global-min_y_global:.3f}")
