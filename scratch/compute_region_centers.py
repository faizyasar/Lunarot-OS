import json
import struct

with open('scratch/gym_skeleton.glb', 'rb') as f:
    data = f.read()

json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

accessors = gltf.get('accessors', [])
nodes = gltf.get('nodes', [])
meshes = gltf.get('meshes', [])

mesh_nodes = {}
for i, n in enumerate(nodes):
    m_idx = n.get('mesh')
    if m_idx is not None:
        mesh_nodes[m_idx] = n.get('name', f'Node_{i}')

regions = {
    'Skull': ['cranium', 'parietal', 'frontal', 'occipital', 'mandible', 'maxilla', 'nasal', 'temporal', 'zygomatic'],
    'Spine': ['vertebra', 'atlas', 'axis', 'sacrum', 'coccyx'],
    'Thorax': ['rib', 'sternum', 'manubrium', 'xiphoid'],
    'Pelvis': ['hip bone', 'pelvic'],
    'Arms/Hands': ['humerus', 'radius', 'ulna', 'clavicle', 'scapula', 'metacarpal', 'phalanx of first finger of hand'],
    'Legs/Feet': ['femur', 'patella', 'tibia', 'fibula', 'talus', 'calcaneus', 'metatarsal', 'phalanx of first finger of foot']
}

region_bounds = {r: [float('inf'), float('-inf'), float('inf'), float('-inf'), float('inf'), float('-inf')] for r in regions}

for i, m in enumerate(meshes):
    name = mesh_nodes.get(i, m.get('name', f'Mesh_{i}'))
    name_lower = name.lower()
    primitives = m.get('primitives', [])
    for p in primitives:
        pos_acc_idx = p.get('attributes', {}).get('POSITION')
        if pos_acc_idx is not None:
            acc = accessors[pos_acc_idx]
            min_val = acc.get('min')
            max_val = acc.get('max')
            if min_val and max_val:
                for reg, keywords in regions.items():
                    if any(k in name_lower for k in keywords):
                        b = region_bounds[reg]
                        b[0] = min(b[0], min_val[0])
                        b[1] = max(b[1], max_val[0])
                        b[2] = min(b[2], min_val[1])
                        b[3] = max(b[3], max_val[1])
                        b[4] = min(b[4], min_val[2])
                        b[5] = max(b[5], max_val[2])

print("=== EXACT ANATOMICAL REGION BOUNDING BOXES ===")
for reg, b in region_bounds.items():
    center_x = (b[0] + b[1]) / 2.0
    center_y = (b[2] + b[3]) / 2.0
    center_z = (b[4] + b[5]) / 2.0
    size_y = b[3] - b[2]
    print(f"Region: {reg:12s} | Center: ({center_x:6.3f}, {center_y:6.3f}, {center_z:6.3f}) | Y-Range: [{b[2]:6.3f}, {b[3]:6.3f}] | Height: {size_y:5.3f}")
