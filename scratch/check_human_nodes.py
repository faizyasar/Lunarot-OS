import json
import struct

data = open('scratch/human_skeleton.glb', 'rb').read()
json_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+json_len].decode('utf-8'))

nodes = [n.get('name') for n in gltf.get('nodes', [])]
print("Nodes in human_skeleton.glb:", nodes)
