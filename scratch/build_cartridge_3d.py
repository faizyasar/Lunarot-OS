import json
import re
import os
import io
import base64
from PIL import Image
from playwright.sync_api import sync_playwright

# 1. Read manifest from the bundled file on Desktop
source_files = [
    r'C:\Users\faizy\Desktop\HTMLS\Astral Pachinko - Cartridge, Case & Magazine.html',
    r'C:\Users\faizy\Desktop\HTMLS\Astral Pachinko (Spinning Transparent).html'
]

manifest = {}
for sf in source_files:
    if os.path.exists(sf):
        with open(sf, 'r', encoding='utf-8') as f:
            text = f.read()
        m = re.search(r'<script type="__bundler/manifest">(.*?)</script>', text, re.DOTALL)
        if m:
            manifest = json.loads(m.group(1))
            break

# The GLB and Cover Art UUIDs
# From user prompt: "d659b33e-6421-45a9-b407-c0115e669e90" and "83e7c9f1-ccb0-4760-9f89-6d3400734e60"
# If not in file manifest, we can search or use the base64 from the prompt
glb_data_url = ""
cover_data_url = ""

for k, v in manifest.items():
    if "data" in v and "Z2xURg" in v["data"][:20]:  # glTF magic header
        glb_data_url = f"data:{v['mime']};base64,{v['data']}"
    elif "data" in v and "UklGR" in v["data"][:20]:  # WebP magic header
        cover_data_url = f"data:{v['mime']};base64,{v['data']}"

# If not found in manifest, extract from prompt's known base64
if not glb_data_url:
    # Save standard glb data url
    pass

print(f"GLB found: {bool(glb_data_url)}, Cover found: {bool(cover_data_url)}")

# 2. Build standalone Three.js HTML for the Gameboy Cartridge
html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Gameboy Cartridge 3D</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    html, body {{ width: 100%; height: 100%; overflow: hidden; background: transparent !important; }}
    #canvas-container {{ width: 100vw; height: 100vh; display: flex; align-items: center; justify-content: center; }}
  </style>
  <script type="importmap">
  {{
    "imports": {{
      "three": "https://unpkg.com/three@0.184.0/build/three.module.js",
      "three/addons/loaders/GLTFLoader.js": "https://unpkg.com/three@0.184.0/examples/jsm/loaders/GLTFLoader.js"
    }}
  }}
  </script>
</head>
<body>
  <div id="canvas-container"></div>

  <script type="module">
    import * as THREE from 'three';
    import {{ GLTFLoader }} from 'three/addons/loaders/GLTFLoader.js';

    const container = document.getElementById('canvas-container');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
    camera.position.set(0, 0, 4.5);

    const renderer = new THREE.WebGLRenderer({{ alpha: true, antialias: true, preserveDrawingBuffer: true }});
    renderer.setSize(800, 800);
    renderer.setPixelRatio(1);
    renderer.setClearColor(0x000000, 0);
    container.appendChild(renderer.domElement);

    // Studio lighting for cartridge
    const ambientLight = new THREE.AmbientLight(0xffffff, 1.2);
    scene.add(ambientLight);

    const dirLight1 = new THREE.DirectionalLight(0xffffff, 1.5);
    dirLight1.position.set(3, 4, 5);
    scene.add(dirLight1);

    const dirLight2 = new THREE.DirectionalLight(0xffffff, 0.8);
    dirLight2.position.set(-3, -2, -4);
    scene.add(dirLight2);

    let cartridgeGroup = new THREE.Group();
    scene.add(cartridgeGroup);

    const loader = new GLTFLoader();
    const glbUrl = "{glb_data_url}";
    const coverUrl = "{cover_data_url}";

    loader.load(glbUrl, async (gltf) => {{
      const model = gltf.scene;
      model.traverse((n) => {{
        if (n.isMesh) {{
          n.castShadow = false;
          n.receiveShadow = false;
        }}
      }});

      const box = new THREE.Box3().setFromObject(model);
      const size = new THREE.Vector3();
      box.getSize(size);

      const half_w = 0.8211;
      const half_h = 0.8680;
      const marker_center = new THREE.Vector3(0.9288, box.max.y - 0.0105, 0.0571);

      const fill_mesh = new THREE.Mesh(
        new THREE.PlaneGeometry(half_w * 2, half_h * 2),
        new THREE.MeshBasicMaterial({{ color: 0xffffff, transparent: true, side: THREE.DoubleSide }})
      );
      fill_mesh.name = 'CoverFill';
      fill_mesh.position.copy(marker_center);
      fill_mesh.rotation.x = -Math.PI / 2;

      // Bake cover texture
      const cover_img = new Image();
      cover_img.src = coverUrl;
      await new Promise(r => {{ cover_img.onload = r; cover_img.onerror = r; }});

      if (cover_img.complete && cover_img.naturalWidth) {{
        const cw = 512, ch = Math.round(512 * (half_h / half_w));
        const radius = Math.min(cw, ch) * 0.06;
        const mask_canvas = document.createElement('canvas');
        mask_canvas.width = cw; mask_canvas.height = ch;
        const mctx = mask_canvas.getContext('2d');
        mctx.filter = 'blur(4px)';
        mctx.fillStyle = '#fff';
        mctx.beginPath();
        mctx.moveTo(radius, 0);
        mctx.arcTo(cw, 0, cw, ch, radius);
        mctx.arcTo(cw, ch, 0, ch, radius);
        mctx.arcTo(0, ch, 0, 0, radius);
        mctx.arcTo(0, 0, cw, 0, radius);
        mctx.closePath();
        mctx.fill();

        const img_canvas = document.createElement('canvas');
        img_canvas.width = cw; img_canvas.height = ch;
        const ictx = img_canvas.getContext('2d');
        ictx.drawImage(cover_img, 0, 0, cw, ch);
        ictx.globalCompositeOperation = 'destination-in';
        ictx.drawImage(mask_canvas, 0, 0);

        const cover_tex = new THREE.CanvasTexture(img_canvas);
        cover_tex.colorSpace = THREE.SRGBColorSpace;
        cover_tex.center.set(0.5, 0.5);
        cover_tex.rotation = Math.PI / 2;
        fill_mesh.material.map = cover_tex;
        fill_mesh.material.needsUpdate = true;
      }}

      const innerGroup = new THREE.Group();
      innerGroup.add(model);
      innerGroup.add(fill_mesh);

      const basis = new THREE.Matrix4().makeBasis(
        new THREE.Vector3(0, -1, 0),
        new THREE.Vector3(0, 0, 1),
        new THREE.Vector3(-1, 0, 0)
      );
      innerGroup.quaternion.setFromRotationMatrix(basis);

      cartridgeGroup.add(innerGroup);

      // Center model
      const box2 = new THREE.Box3().setFromObject(cartridgeGroup);
      const center = new THREE.Vector3();
      box2.getCenter(center);
      cartridgeGroup.position.sub(center);

      window.__isReady = true;
      renderer.render(scene, camera);
    }});

    window.__setRotation = function(degY, degX) {{
      if (!cartridgeGroup) return;
      cartridgeGroup.rotation.y = (degY * Math.PI) / 180;
      cartridgeGroup.rotation.x = (degX !== undefined ? degX : 10) * Math.PI / 180;
      renderer.render(scene, camera);
    }};
  </script>
</body>
</html>
"""

render_html_path = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\gameboy_cartridge_render.html'
with open(render_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Saved render HTML to:", render_html_path)
