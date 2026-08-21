import re, base64, json, struct

with open('golem.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'data:video/webm;base64,[A-Za-z0-9+/=]+', content) # This is crt-video. We need GLB.
# Let's search for GLB base64
match = re.search(r'const\s+GLB_BASE64\s*=\s*[\'"]([A-Za-z0-9+/=]+)[\'"]', content)
if not match:
    # Maybe it's defined in golem_data.js?
    with open('golem_data.js', 'r', encoding='utf-8') as f:
        data_content = f.read()
    match = re.search(r'const\s+GLB_BASE64\s*=\s*[\'"]([A-Za-z0-9+/=]+)[\'"]', data_content)

if match:
    b64_data = match.group(1)
    glb_data = base64.b64decode(b64_data)
    json_len = struct.unpack('<I', glb_data[12:16])[0]
    gltf = json.loads(glb_data[20:20+json_len].decode('utf-8'))
    print("Found nodes:")
    for i, n in enumerate(gltf.get('nodes', [])):
        print(f"[{i}] {n.get('name', '')}")
else:
    print("Could not find GLB_BASE64")
