import base64
import os
import re

print("Building standalone skeletal figure HTML (bones only, full left/right structure)...")

# Read GLB file
glb_path = 'scratch/open3dviewer_src/3dmodels/overview-demo/overview-demo.glb'
with open(glb_path, 'rb') as f:
    glb_b64 = base64.b64encode(f.read()).decode('utf-8')

# Read CSS file
css_path = 'scratch/open3dviewer_src/css/3d.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Read SVGs
imgs = {}
img_dir = 'scratch/open3dviewer_src/img'
for img_name in os.listdir(img_dir):
    if img_name.endswith('.svg'):
        with open(os.path.join(img_dir, img_name), 'rb') as f:
            imgs[img_name] = 'data:image/svg+xml;base64,' + base64.b64encode(f.read()).decode('utf-8')

# Read original index.html
with open('scratch/open3dviewer_src/index.html', 'r', encoding='utf-8') as f:
    html_src = f.read()

# Replace img/ references with data URIs
for img_name, b64_uri in imgs.items():
    html_src = html_src.replace(f'img/{img_name}', b64_uri)

# Extract body inner content
body_match = re.search(r'<body[^>]*>(.*?)</body>', html_src, re.DOTALL)
if not body_match:
    raise ValueError("Could not find <body> element in source HTML")
body_inner = body_match.group(1)

# Remove local script tags for babylon JS
body_inner = re.sub(r'<script src="js/babylon[^"]*"></script>', '', body_inner)

# Custom loader code that:
# 1. Loads GLB from Base64 Data URL
# 2. Clones right-side structures to left-side to form the complete symmetrical skeleton
# 3. Hides muscle meshes so ONLY the skeletal bones are rendered
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
        console.log("Full skeletal model loaded.");
    }, null, function(scene, message, exception) {
        console.error("Error loading skeletal model:", message, exception);
    }, ".glb");
'''

if old_loader in body_inner:
    body_inner = body_inner.replace(old_loader, new_loader)
else:
    body_inner = re.sub(r'BABYLON\.SceneLoader\.Append\([^;]+\);', new_loader, body_inner)

# Handle model parameter
body_inner = body_inner.replace(
    "let model=getUrlArgument('model');",
    "let model = 'overview-demo';"
)
body_inner = body_inner.replace(
    "if(set){loadScript('3dmodels/'+model+'/'+set+'.js');}",
    "// Subset preset override handled"
)
body_inner = body_inner.replace(
    "document.title = 'open 3D webviewer : '+model+' model';",
    "document.title = 'Open 3D Viewer - Full Skeletal Model';"
)

# Update condition for cloning so overview cloning always triggers for complete skeleton
body_inner = body_inner.replace(
    "if(model.split(\"-\")[0] === 'overview'){",
    "if(true){"
)

# Inject post-processing to hide muscles by default & update menu state
muscle_hide_code = '''
        // Hide muscles by default so only the skeletal figure is displayed
        scene.meshes.forEach(function(mesh) {
            if (mesh.name.toLowerCase().includes('muscle') || (mesh.parent && mesh.parent.name.toLowerCase().includes('muscle'))) {
                mesh.isVisible = false;
            }
        });
        
        // Update menu class for muscle items to 'off'
        document.querySelectorAll('.cp').forEach(function(el) {
            if (el.innerHTML.toLowerCase().includes('muscle') || (el.id && el.id.toLowerCase().includes('muscle'))) {
                el.classList.replace('on', 'off');
                if (el.parentNode && el.parentNode.children) {
                    for (let child of el.parentNode.children) {
                        child.classList.replace('on', 'off');
                    }
                }
            }
        });
'''

# Place muscle hide code after menu generation
target_menu_end = 'document.getElementById("switches-box").innerHTML = codeBlock;'
body_inner = body_inner.replace(target_menu_end, target_menu_end + muscle_hide_code)

standalone_html = f'''<!doctype html>
<html lang="en-us">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Open 3D Viewer - Full Skeletal Model (LUMC Anatomy)</title>
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

print(f"DONE! Written pure skeletal HTML to {output_path} ({os.path.getsize(output_path)} bytes)")
