import json
import base64

with open('open3dviewer_skeletal_figure.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

b64 = lines[336].split('"')[1]
glb = base64.b64decode(b64)
json_len = int.from_bytes(glb[12:16], 'little')
json_data = glb[20:20+json_len].decode('utf-8')
data = json.loads(json_data)

print("Materials:", json.dumps(data.get('materials', []), indent=2))
