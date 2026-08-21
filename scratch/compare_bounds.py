import json, struct

def get_bounds(path):
    data = open(path, 'rb').read()
    json_len, _ = struct.unpack('<II', data[12:20])
    gltf = json.loads(data[20:20+json_len].decode('utf-8'))
    pos_acc = [a for a in gltf['accessors'] if a['type'] == 'VEC3']
    if not pos_acc: return None
    mins = [a.get('min') for a in pos_acc if 'min' in a]
    maxs = [a.get('max') for a in pos_acc if 'max' in a]
    
    min_x = min([m[0] for m in mins])
    min_y = min([m[1] for m in mins])
    min_z = min([m[2] for m in mins])
    
    max_x = max([m[0] for m in maxs])
    max_y = max([m[1] for m in maxs])
    max_z = max([m[2] for m in maxs])
    return (min_x, min_y, min_z), (max_x, max_y, max_z)

print("Gym bounds:", get_bounds('scratch/gym_skeleton.glb'))
print("Human bounds:", get_bounds('scratch/human_skeleton.glb'))
