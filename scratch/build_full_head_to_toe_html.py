import base64
import os
import re

print("Rebuilding head-to-toe 3D skeleton HTML with auto-bounding camera framing...")

# Read GLB file
glb_path = 'scratch/gym_skeleton.glb'
with open(glb_path, 'rb') as f:
    glb_bytes = f.read()
glb_b64 = base64.b64encode(glb_bytes).decode('utf-8')

# Read CSS file
css_path = 'scratch/open3dviewer_src/css/3d.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Read SVGs for UI icons
imgs = {}
img_dir = 'scratch/open3dviewer_src/img'
for img_name in os.listdir(img_dir):
    if img_name.endswith('.svg'):
        with open(os.path.join(img_dir, img_name), 'rb') as f:
            imgs[img_name] = 'data:image/svg+xml;base64,' + base64.b64encode(f.read()).decode('utf-8')

# Read open3dviewer index.html template
with open('scratch/open3dviewer_src/index.html', 'r', encoding='utf-8') as f:
    html_src = f.read()

# Replace img/ references with data URIs
for img_name, b64_uri in imgs.items():
    html_src = html_src.replace(f'img/{img_name}', b64_uri)

# Extract body inner content
body_match = re.search(r'<body[^>]*>(.*?)</body>', html_src, re.DOTALL)
if not body_match:
    raise ValueError("Could not find <body> element")
body_inner = body_match.group(1)

# Remove local script tags for babylon JS
body_inner = re.sub(r'<script src="js/babylon[^"]*"></script>', '', body_inner)

# Replace loader call with embedded Base64 Blob URL loading
old_loader = 'BABYLON.SceneLoader.Append("./3dmodels/"+model+"/", model+".glb", scene);'
new_loader = '''
    const binaryString = window.atob(GLB_BASE64);
    const bytes = new Uint8Array(binaryString.length);
    for (let i = 0; i < binaryString.length; i++) {
        bytes[i] = binaryString.charCodeAt(i);
    }
    const blob = new Blob([bytes.buffer], { type: 'model/gltf-binary' });
    const modelUrl = URL.createObjectURL(blob);
    
    BABYLON.SceneLoader.Append("", modelUrl, scene, function(scene) {
        console.log("Full head-to-toe 3D skeleton loaded successfully.");
    }, null, function(scene, message, exception) {
        console.error("Error loading skeleton model:", message, exception);
    }, ".glb");
'''

if old_loader in body_inner:
    body_inner = body_inner.replace(old_loader, new_loader)
else:
    body_inner = re.sub(r'BABYLON\.SceneLoader\.Append\([^;]+\);', new_loader, body_inner)

# Set model variable
body_inner = body_inner.replace(
    "let model=getUrlArgument('model');",
    "let model = 'head-to-toe-skeleton';"
)
body_inner = body_inner.replace(
    "if(set){loadScript('3dmodels/'+model+'/'+set+'.js');}",
    "// Custom preset subset"
)
body_inner = body_inner.replace(
    "document.title = 'open 3D webviewer : '+model+' model';",
    "document.title = 'Open 3D Viewer - Full Head to Toe Human Skeleton';"
)

# Disable overview right-side auto cloning because gym_skeleton already has full symmetric left & right bones
body_inner = body_inner.replace(
    "if(model.split(\"-\")[0] === 'overview'){",
    "if(false){"
)

# Use Babylon's automatic framing for perfect default view of the entire skeleton from head to toe
camera_fix = '''
        scene.createDefaultCamera(true, true, true);
        var cam = scene.activeCamera; 
        cam.wheelPrecision = 600; 
        cam.pinchPrecision = 800; 
        cam.alpha += Math.PI; 
        cam.panningSensibility = 1600; 
        cam.useAutoRotationBehavior = false;
'''

body_inner = re.sub(
    r'scene\.createDefaultCamera\(true, true, true\);.*cam\.useAutoRotationBehavior = false;',
    camera_fix,
    body_inner
)

standalone_html = f'''<!doctype html>
<html lang="en-us">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Open 3D Viewer - Full Head to Toe Human Skeleton</title>
<style>
{css_content}
</style>
<script src="https://cdn.babylonjs.com/babylon.js"></script>
<script src="https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js"></script>
</head>
<body>
<script>
const GLB_BASE64 = "{glb_b64}";
</script>
{body_inner}
</body>
</html>
'''

output_path = 'open3dviewer_skeletal_figure.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(standalone_html)

print(f"SUCCESS! Rebuilt complete head-to-toe skeleton HTML ({os.path.getsize(output_path)} bytes)")
