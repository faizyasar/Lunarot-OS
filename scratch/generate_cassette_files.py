import base64
import json
import os

with open(r'scratch/cassette_assets/6ccebc4c-66be-442e-b4ba-b676b7c75717', 'rb') as f:
    side_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

with open(r'scratch/cassette_assets/525f4264-35e5-497d-b97b-41b08cebb73a', 'rb') as f:
    front_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

with open(r'scratch/cassette_assets/dd58951b-1b53-46db-9c57-feaa8680f9c1', 'rb') as f:
    back_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Compact Cassette - Standalone 3D</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ width: 100%; height: 100%; overflow: hidden; background: transparent; }}
  #container {{ width: 100vw; height: 100vh; display: flex; align-items: center; justify-content: center; }}
  canvas {{ width: 100%; height: 100%; display: block; }}
</style>
<script type="importmap">
{{
  "imports": {{
    "three": "https://unpkg.com/three@0.184.0/build/three.module.js",
    "three/addons/": "https://unpkg.com/three@0.184.0/examples/jsm/"
  }}
}}
</script>
</head>
<body>
<div id="container"></div>

<script type="module">
import * as THREE from 'three';
import {{ OrbitControls }} from 'three/addons/controls/OrbitControls.js';

const container = document.getElementById('container');
const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(36, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 0, 195);

const renderer = new THREE.WebGLRenderer({{
  antialias: true,
  alpha: true,
  preserveDrawingBuffer: true,
  powerPreference: "high-performance"
}});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio || 2);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.2;
renderer.outputColorSpace = THREE.SRGBColorSpace;
container.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.target.set(0, 0, 0);

// Crisp Studio Lighting
scene.add(new THREE.HemisphereLight(0xffffff, 0xe8ecf0, 1.6));

const keyLight = new THREE.DirectionalLight(0xffffff, 1.8);
keyLight.position.set(60, 90, 80);
scene.add(keyLight);

const fillLight = new THREE.DirectionalLight(0xffffff, 1.3);
fillLight.position.set(-60, 40, -50);
scene.add(fillLight);

const rimLight = new THREE.DirectionalLight(0xffffff, 1.2);
rimLight.position.set(0, -60, 50);
scene.add(rimLight);

const bottomLight = new THREE.DirectionalLight(0xffffff, 0.8);
bottomLight.position.set(-40, -50, 40);
scene.add(bottomLight);

const texLoader = new THREE.TextureLoader();
function skinTex(url) {{
  const t = texLoader.load(url);
  t.colorSpace = THREE.SRGBColorSpace;
  return t;
}}

const sideTex = skinTex("{side_b64}");
const frontTex = skinTex("{front_b64}");
const backTex = skinTex("{back_b64}");

for (const t of [frontTex, backTex]) {{
  t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.center.set(0.5, 0.5);
}}

const M = {{
  shell: new THREE.MeshPhysicalMaterial({{
    name: 'shell_side_skin',
    map: sideTex,
    color: 0xffffff,
    roughness: 0.35,
    transparent: true,
    opacity: 0.25,
    side: THREE.DoubleSide,
    depthWrite: false
  }}),
  tape: new THREE.MeshStandardMaterial({{ name: 'magnetic_tape', color: 0x111111, roughness: 0.7 }}),
  hub: new THREE.MeshStandardMaterial({{ name: 'hub_plastic', color: 0xf4f1ea, roughness: 0.45 }}),
  dark: new THREE.MeshStandardMaterial({{ name: 'liner_black', color: 0x5a5650, roughness: 0.55 }}),
  metal: new THREE.MeshStandardMaterial({{ name: 'steel', color: 0xc4cbd4, roughness: 0.25, metalness: 0.35, transparent: true, opacity: 0.9 }}),
  felt: new THREE.MeshStandardMaterial({{ name: 'pressure_pad', color: 0xa08e76, roughness: 0.95 }})
}};

const named = (geo, mat, name) => {{ const m = new THREE.Mesh(geo, mat); m.name = name; return m; }};
const box = (w,h,d,mat,name,x=0,y=0,z=0) => {{ const m = named(new THREE.BoxGeometry(w,h,d), mat, name); m.position.set(x,y,z); return m; }};
const cyl = (r,h,mat,name,seg=32) => named(new THREE.CylinderGeometry(r,r,h,seg), mat, name);

const W = 100.4, H = 63.8, T = 12.0, HX = W/2, HY = H/2;
const HUB_X = 21.25, HUB_Y = 3.0;

const FRONT = [
  [-42.0, 3.4, 4.6],
  [-26.5, 2.4, 4.6],
  [-13.5, 3.8, 5.0],
  [  0.0, 7.2, 5.4],
  [ 13.5, 3.8, 5.0],
  [ 26.5, 2.4, 4.6],
  [ 42.0, 3.4, 4.6],
];
const REAR = [[-44.5, 4.0, 4.0], [44.5, 4.0, 4.0]];

function shellShape() {{
  const s = new THREE.Shape(), r = 3;
  s.moveTo(-HX + r, -HY);
  for (const [cx, hw, d] of FRONT) {{
    s.lineTo(cx - hw, -HY); s.lineTo(cx - hw, -HY + d);
    s.lineTo(cx + hw, -HY + d); s.lineTo(cx + hw, -HY);
  }}
  s.lineTo(HX - r, -HY);
  s.quadraticCurveTo(HX, -HY, HX, -HY + r);
  s.lineTo(HX, HY - r);
  s.quadraticCurveTo(HX, HY, HX - r, HY);
  for (const [cx, hw, d] of [...REAR].reverse()) {{
    s.lineTo(cx + hw, HY); s.lineTo(cx + hw, HY - d);
    s.lineTo(cx - hw, HY - d); s.lineTo(cx - hw, HY);
  }}
  s.lineTo(-HX + r, HY);
  s.quadraticCurveTo(-HX, HY, -HX, HY - r);
  s.lineTo(-HX, -HY + r);
  s.quadraticCurveTo(-HX, -HY, -HX + r, -HY);

  for (const sx of [-1, 1]) {{
    const h = new THREE.Path();
    h.absarc(sx * HUB_X, HUB_Y, 10.2, 0, Math.PI * 2, true);
    s.holes.push(h);
  }}
  const win = new THREE.Path();
  win.moveTo(-15, -20.5); win.lineTo(15, -20.5); win.lineTo(15, -10.5); win.lineTo(-15, -10.5);
  s.holes.push(win);
  return s;
}}

const cassette = new THREE.Group(); cassette.name = 'cassette';

const shellGeo = new THREE.ExtrudeGeometry(shellShape(), {{ depth: T, bevelEnabled: false, curveSegments: 24 }});
shellGeo.translate(0, 0, -T/2);
{{
  const pos = shellGeo.attributes.position, uv = shellGeo.attributes.uv;
  const idx = shellGeo.index;
  const vertAt = idx ? (i => idx.getX(i)) : (i => i);
  for (const g of shellGeo.groups) {{
    let zMin = Infinity, zMax = -Infinity;
    for (let i = g.start; i < g.start + g.count; i++) {{
      const vi = vertAt(i);
      zMin = Math.min(zMin, pos.getZ(vi)); zMax = Math.max(zMax, pos.getZ(vi));
    }}
    if (zMax - zMin < T * 0.5) continue;
    for (let i = g.start; i < g.start + g.count; i++) {{
      const vi = vertAt(i);
      uv.setXY(vi, (pos.getX(vi) + HX) / W, (pos.getZ(vi) + T/2) / T);
    }}
  }}
}}
cassette.add(named(shellGeo, M.shell, 'shell'));

function skinFace(name, tex, z, flip) {{
  const geo = new THREE.ShapeGeometry(shellShape(), 24);
  const uv2 = geo.attributes.uv, pos2 = geo.attributes.position;
  for (let i = 0; i < pos2.count; i++) {{
    const u = (pos2.getX(i) + HX) / W, v = (pos2.getY(i) + HY) / H;
    uv2.setXY(i, u, v);
  }}
  const mat = new THREE.MeshStandardMaterial({{ name: name + '_mat', map: tex, roughness: 0.5, side: THREE.DoubleSide, transparent: true, alphaTest: 0 }});
  const m = named(geo, mat, name);
  m.position.z = z;
  if (flip) m.rotation.y = Math.PI;
  return m;
}}
cassette.add(skinFace('shell_front_skin', frontTex, T/2 + 0.05, false));
cassette.add(skinFace('shell_back_skin', backTex, -T/2 - 0.05, true));

for (const [cx, hw, d] of REAR) {{
  cassette.add(box(hw*2 - 0.6, d - 0.8, T - 1.4, M.dark, 'write_protect_tab', cx, HY - d/2 - 0.4, 0));
}}

function reel(x, packR, name) {{
  const g = new THREE.Group(); g.name = name;
  const pack = cyl(packR, 8.6, M.tape, name + '_tape_pack', 48);
  pack.rotation.x = Math.PI/2; g.add(pack);

  const flangeT = named(new THREE.CylinderGeometry(7.5, 7.5, 0.6, 40), M.hub, name + '_flange_top');
  flangeT.rotation.x = Math.PI/2; flangeT.position.z = 4.5; g.add(flangeT);
  const flangeB = flangeT.clone(); flangeB.name = name + '_flange_bottom'; flangeB.position.z = -4.5; g.add(flangeB);

  const barrel = named(new THREE.CylinderGeometry(5.6, 5.6, 10.4, 32, 1, true), M.hub, name + '_hub');
  barrel.rotation.x = Math.PI/2; g.add(barrel);

  for (let i = 0; i < 6; i++) {{
    const t = box(1.5, 2.6, 10.2, M.hub, name + '_tooth_' + i);
    const a = i * Math.PI/3;
    t.position.set(Math.cos(a) * 4.6, Math.sin(a) * 4.6, 0);
    t.rotation.z = a;
    g.add(t);
  }}
  g.position.set(x, HUB_Y, 0);
  return g;
}}
const packL = 17.4, packR = 11.8;
cassette.add(reel(-HUB_X, packL, 'reel_supply'));
cassette.add(reel( HUB_X, packR, 'reel_takeup'));

const ROLLER = [[-42.0, -25.6], [42.0, -25.6]];
for (const [x, y] of ROLLER) {{
  const r = cyl(2.3, 9.0, M.metal, 'tape_guide_roller', 24);
  r.rotation.x = Math.PI/2; r.position.set(x, y, 0);
  cassette.add(r);
}}
function tapeSpan(x1, y1, x2, y2, name) {{
  const len = Math.hypot(x2-x1, y2-y1);
  const m = box(len, 0.16, 3.81, M.tape, name, (x1+x2)/2, (y1+y2)/2, 0);
  m.rotation.z = Math.atan2(y2-y1, x2-x1);
  return m;
}}
function tangent(px, py, cx, cy, r, sign) {{
  const d = Math.hypot(cx-px, cy-py), L = Math.sqrt(Math.max(d*d - r*r, 1));
  const a = Math.atan2(cy-py, cx-px) + sign * Math.atan2(r, L);
  return [px + Math.cos(a)*L, py + Math.sin(a)*L];
}}
cassette.add(tapeSpan(-42.0, -27.9, 42.0, -27.9, 'tape_head_span'));
{{
  const [tx, ty] = tangent(-39.7, -26.2, -HUB_X, HUB_Y, packL, -1);
  cassette.add(tapeSpan(-39.7, -26.2, tx, ty, 'tape_supply_run'));
  const [ux, uy] = tangent(39.7, -26.2, HUB_X, HUB_Y, packR, 1);
  cassette.add(tapeSpan(39.7, -26.2, ux, uy, 'tape_takeup_run'));
}}

cassette.add(box(30, 0.5, 9.0, M.metal, 'head_shield_plate', 0, -23.6, 0));
cassette.add(box(13, 0.4, 5.4, M.metal, 'pad_leaf_spring', 0, -25.4, 0));
cassette.add(box(6.4, 1.6, 4.4, M.felt, 'pressure_pad', 0, -26.6, 0));

for (const [x, y] of [[-44,-26],[44,-26],[-44,26],[44,26],[0,-24]]) {{
  const s = cyl(1.2, 0.8, M.metal, 'shell_screw', 12);
  s.rotation.x = Math.PI/2; s.position.set(x, y, -T/2 + 0.3);
  cassette.add(s);
  const w = cyl(1.9, 0.9, M.metal, 'screw_boss', 14);
  w.rotation.x = Math.PI/2; w.position.set(x, y, -T/2 + 0.75);
  cassette.add(w);
}}

// Perfect geometric center offset
cassette.position.set(0, 0, 0);

const root = new THREE.Group();
root.name = 'cassette_root';
root.add(cassette);
scene.add(root);

// Precision control function
window.__setRotation = function(yRad, xRad = 0.14, zRad = 0) {{
  root.rotation.set(xRad, yRad, zRad);
  renderer.render(scene, camera);
}};

let autoSpin = true;
function animate() {{
  requestAnimationFrame(animate);
  if (autoSpin) {{
    root.rotation.y += 0.015;
    root.rotation.x = 0.14;
  }}
  controls.update();
  renderer.render(scene, camera);
}}
animate();

window.addEventListener('resize', () => {{
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}});

window.addEventListener('pointerdown', () => {{ autoSpin = false; }});
</script>
</body>
</html>
"""

with open(r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\scratch\cassette_clean_render.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Saved clean render HTML")
