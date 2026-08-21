import json
import struct

data = open('scratch/human_skeleton.glb', 'rb').read()
json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

mats = [m.get('name') for m in gltf.get('materials', [])]
print("Materials in human_skeleton.glb:", mats)
