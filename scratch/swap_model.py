import base64
import re

with open('scratch/human_skeleton.glb', 'rb') as f:
    glb_b64 = base64.b64encode(f.read()).decode('utf-8')

with open('open3dviewer_skeletal_figure.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace GLB_BASE64
content = re.sub(r'const GLB_BASE64 = ".*?";', f'const GLB_BASE64 = "{glb_b64}";', content, count=1)

# Remove mandible rotation
content = re.sub(
    r'\s*// Open Mandible.*?\s*scene\.transformNodes\.forEach\(node => \{.*?\s*if \(node\.name && node\.name\.toLowerCase\(\)\.includes\(\'mandible\'\)\) \{.*?\s*node\.rotate\(BABYLON\.Axis\.X, 0\.12, BABYLON\.Space\.LOCAL\);.*?\s*\}.*?\s*\}\);.*?\s*scene\.meshes\.forEach\(mesh => \{.*?\s*if \(mesh\.name && mesh\.name\.toLowerCase\(\)\.includes\(\'mandible\'\)\) \{.*?\s*mesh\.rotate\(BABYLON\.Axis\.X, 0\.12, BABYLON\.Space\.LOCAL\);.*?\s*\}.*?\s*\}\);',
    '',
    content,
    flags=re.DOTALL
)

# Update HUD logic
content = re.sub(
    r'const parentName = mesh\.parent \? mesh\.parent\.name\.replace\(\'\.g\', \'\'\)\.replace\(\'\.r\', \'\'\)\.replace\(\'\.l\', \'\'\) : \'Skeletal System\';\s*updateHUD\(mesh\.name, parentName\);',
    r'const parentName = mesh.parent ? mesh.parent.name.replace(\'.g\', \'\').replace(\'.r\', \'\').replace(\'.l\', \'\') : \'Skeletal System\';\n        let cleanName = mesh.name;\n        if (cleanName.includes(\'Object_\')) cleanName = "Human Skeleton Model";\n        updateHUD(cleanName, parentName);',
    content
)

with open('open3dviewer_skeletal_figure.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated open3dviewer_skeletal_figure.html successfully.")
