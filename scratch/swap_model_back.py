import base64
import re

print("Starting model swap...")
with open("scratch/gym_skeleton.glb", "rb") as f:
    glb_data = f.read()

base64_glb = base64.b64encode(glb_data).decode("utf-8")
print("Encoded gym_skeleton.glb to base64.")

with open("open3dviewer_skeletal_figure.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace the base64 string
pattern = re.compile(r"(const\s+GLB_BASE64\s*=\s*['\"])[^'\"]*(['\"])")
new_html = pattern.sub(r"\g<1>" + base64_glb + r"\g<2>", html_content)

with open("open3dviewer_skeletal_figure.html", "w", encoding="utf-8") as f:
    f.write(new_html)
    
print("Successfully swapped model back to gym_skeleton.glb!")
