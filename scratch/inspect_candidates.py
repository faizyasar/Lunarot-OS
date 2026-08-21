import json
import os
import struct
import urllib.request

urls = {
    'human_skeleton.glb': 'https://raw.githubusercontent.com/DavidVeksler/CheatSheets/main/human_skeleton.glb',
    'gym_skeleton.glb': 'https://raw.githubusercontent.com/sesgigikimo/gym-muscle/main/skeleton.glb'
}

for name, url in urls.items():
    out = os.path.join('scratch', name)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req).read()
        with open(out, 'wb') as f:
            f.write(data)
        
        # Extract GLTF json
        magic, ver, length = struct.unpack('<III', data[:12])
        json_len, _ = struct.unpack('<II', data[12:20])
        gltf = json.loads(data[20:20+json_len].decode('utf-8'))
        nodes = [n.get('name') for n in gltf.get('nodes', []) if n.get('name')]
        print(f"=== {name} ({len(data)} bytes) ===")
        print(f"Nodes count: {len(gltf.get('nodes', []))}, Meshes count: {len(gltf.get('meshes', []))}")
        print(f"Sample node names: {nodes[:20]}\n")
    except Exception as e:
        print(f"Error {name}: {e}")
