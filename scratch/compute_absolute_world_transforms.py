import json
import struct
import math

with open('scratch/gym_skeleton.glb', 'rb') as f:
    data = f.read()

json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

nodes = gltf.get('nodes', [])
meshes = gltf.get('meshes', [])
accessors = gltf.get('accessors', [])

parent_map = {}
for i, n in enumerate(nodes):
    for c in n.get('children', []):
        parent_map[c] = i

def quat_to_matrix(q):
    x, y, z, w = q
    return [
        [1 - 2*y*y - 2*z*z, 2*x*y - 2*z*w, 2*x*z + 2*y*w, 0],
        [2*x*y + 2*z*w, 1 - 2*x*x - 2*z*z, 2*y*z - 2*x*w, 0],
        [2*x*z - 2*y*w, 2*y*z + 2*x*w, 1 - 2*x*x - 2*y*y, 0],
        [0, 0, 0, 1]
    ]

def mat_mult(A, B):
    C = [[0.0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(4))
    return C

def get_node_matrix(node):
    if 'matrix' in node:
        m = node['matrix']
        return [[m[i + j*4] for j in range(4)] for i in range(4)]
    
    t = node.get('translation', [0, 0, 0])
    r = node.get('rotation', [0, 0, 0, 1])
    s = node.get('scale', [1, 1, 1])

    rot = quat_to_matrix(r)
    for i in range(3):
        for j in range(3):
            rot[i][j] *= s[j]
        rot[i][3] = t[i]
    return rot

def get_world_matrix(node_idx):
    m = get_node_matrix(nodes[node_idx])
    curr = node_idx
    while curr in parent_map:
        curr = parent_map[curr]
        m = mat_mult(get_node_matrix(nodes[curr]), m)
    return m

def transform_point(m, p):
    x = m[0][0]*p[0] + m[0][1]*p[1] + m[0][2]*p[2] + m[0][3]
    y = m[1][0]*p[0] + m[1][1]*p[1] + m[1][2]*p[2] + m[1][3]
    z = m[2][0]*p[0] + m[2][1]*p[1] + m[2][2]*p[2] + m[2][3]
    return (x, y, z)

print("=== ABSOLUTE WORLD Y BOUNDS OF KEY NODES ===")
for i, n in enumerate(nodes):
    name = n.get('name', '')
    m_idx = n.get('mesh')
    if m_idx is not None:
        world_m = get_world_matrix(i)
        mesh = meshes[m_idx]
        for p in mesh.get('primitives', []):
            pos_acc = accessors[p['attributes']['POSITION']]
            min_l = pos_acc['min']
            max_l = pos_acc['max']
            
            corners_l = [
                (min_l[0], min_l[1], min_l[2]), (max_l[0], min_l[1], min_l[2]),
                (min_l[0], max_l[1], min_l[2]), (max_l[0], max_l[1], min_l[2]),
                (min_l[0], min_l[1], max_l[2]), (max_l[0], min_l[1], max_l[2]),
                (min_l[0], max_l[1], max_l[2]), (max_l[0], max_l[1], max_l[2])
            ]
            corners_w = [transform_point(world_m, pt) for pt in corners_l]
            min_y = min(pt[1] for pt in corners_w)
            max_y = max(pt[1] for pt in corners_w)
            center_y = (min_y + max_y) / 2.0
            
            if any(k in name.lower() for k in ['cranium', 'parietal', 'frontal', 'vertebra c1', 'atlas', 'sternum', 'hip bone', 'femur', 'tibia', 'talus', 'calcaneus', 'first metatarsal']):
                print(f"Node {i:3d}: {name:35s} | World Y min: {min_y:7.3f}, max: {max_y:7.3f} | Center Y: {center_y:7.3f}")
