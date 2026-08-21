import base64
import os

print("Rebuilding Viewer: Parting Mandible Jaw via Local Axis Rotation to Display Teeth Rows...")

# Read GLB file
glb_path = 'scratch/gym_skeleton.glb'
with open(glb_path, 'rb') as f:
    glb_b64 = base64.b64encode(f.read()).decode('utf-8')

# Read CRT video
crt_path = 'crt-bg.webm'
with open(crt_path, 'rb') as f:
    crt_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>Lunarot® OS - High DPI Camera Telemetry 3D Skeleton</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;600&display=swap');

  * {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    user-select: none;
    -webkit-user-select: none;
  }}

  html, body {{
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #000000;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #ffffff;
  }}

  /* Background CRT Video (Monochrome Greyscale) */
  #crt-video {{
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 1;
    opacity: 0.55;
    filter: grayscale(100%) contrast(1.3) brightness(0.65);
  }}

  /* CRT Overlay & Ultra-Fine Scanlines */
  .crt-overlay {{
    position: fixed;
    inset: 0;
    z-index: 2;
    pointer-events: none;
    background: linear-gradient(rgba(0, 0, 0, 0) 50%, rgba(0, 0, 0, 0.45) 50%),
                linear-gradient(90deg, rgba(255, 255, 255, 0.02), rgba(0, 0, 0, 0.02));
    background-size: 100% 2px, 3px 100%;
    box-shadow: inset 0 0 150px rgba(0, 0, 0, 0.95);
  }}

  /* 3D Canvas */
  #render-canvas {{
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 3;
    touch-action: none;
    outline: none;
  }}

  /* Header Branding HUD */
  .hud-header {{
    position: fixed;
    top: 20px;
    left: 24px;
    z-index: 10;
    display: flex;
    align-items: center;
    gap: 14px;
    background: rgba(10, 10, 10, 0.85);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 10px 18px;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.8);
  }}

  .hud-logo {{
    font-family: 'Cinzel', serif;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #ffffff;
    text-shadow: 0 0 8px rgba(255, 255, 255, 0.4);
  }}

  .hud-badge {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    color: rgba(255, 255, 255, 0.65);
    background: rgba(255, 255, 255, 0.08);
    padding: 3px 8px;
    border-radius: 4px;
    border: 1px solid rgba(255, 255, 255, 0.15);
  }}

  /* Focused Bone Info Card HUD */
  .focus-hud {{
    position: fixed;
    top: 20px;
    right: 24px;
    z-index: 10;
    min-width: 240px;
    background: rgba(10, 10, 10, 0.85);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    padding: 12px 18px;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.8);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  .focus-label {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: rgba(255, 255, 255, 0.7);
    margin-bottom: 4px;
  }}

  .focus-title {{
    font-family: 'Cinzel', serif;
    font-size: 16px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.05em;
  }}

  .focus-sub {{
    font-size: 11px;
    color: rgba(255, 255, 255, 0.55);
    margin-top: 2px;
  }}

  /* Live Camera XYZ & Angles Telemetry HUD Panel */
  .telemetry-hud {{
    position: fixed;
    top: 80px;
    left: 24px;
    z-index: 10;
    background: rgba(8, 8, 8, 0.88);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    padding: 12px 16px;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.8);
    min-width: 250px;
  }}

  .telemetry-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    color: rgba(255, 255, 255, 0.65);
    margin-bottom: 10px;
    padding-bottom: 6px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  }}

  .copy-coords-btn {{
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.25);
    color: #ffffff;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    padding: 3px 8px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
  }}

  .copy-coords-btn:hover {{
    background: rgba(255, 255, 255, 0.25);
    border-color: #ffffff;
  }}

  .telemetry-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px 12px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
  }}

  .telemetry-item {{
    display: flex;
    justify-content: space-between;
    color: rgba(255, 255, 255, 0.55);
  }}

  .telemetry-val {{
    color: #ffffff;
    font-weight: 600;
  }}

  /* Camera Quick Focus Bar */
  .quick-focus-bar {{
    position: fixed;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(8, 8, 8, 0.85);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 8px 12px;
    border-radius: 16px;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.8);
    max-width: 92vw;
    overflow-x: auto;
    scrollbar-width: none;
  }}

  .quick-focus-bar::-webkit-scrollbar {{ display: none; }}

  .focus-btn {{
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: rgba(255, 255, 255, 0.75);
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 500;
    padding: 8px 14px;
    border-radius: 10px;
    cursor: pointer;
    white-space: nowrap;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s ease;
  }}

  .focus-btn:hover, .focus-btn.active {{
    background: rgba(255, 255, 255, 0.2);
    border-color: rgba(255, 255, 255, 0.8);
    color: #ffffff;
    box-shadow: 0 0 12px rgba(255, 255, 255, 0.25);
    transform: translateY(-1px);
  }}

  .focus-btn:active {{
    transform: translateY(1px);
  }}

  /* Floating Action Buttons */
  .fab-group {{
    position: fixed;
    right: 24px;
    bottom: 90px;
    z-index: 10;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}

  .fab-btn {{
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: rgba(8, 8, 8, 0.85);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
    transition: all 0.2s ease;
  }}

  .fab-btn:hover {{
    background: rgba(255, 255, 255, 0.25);
    border-color: #ffffff;
    color: #ffffff;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    transform: scale(1.05);
  }}

  .fab-btn:active {{
    transform: scale(0.95);
  }}

  /* Interactive Help Banner */
  .interaction-hint {{
    position: fixed;
    bottom: 84px;
    left: 24px;
    z-index: 10;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.1em;
    color: rgba(255, 255, 255, 0.45);
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(8px);
    padding: 6px 12px;
    border-radius: 6px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    pointer-events: none;
  }}

  @media (max-width: 768px) {{
    .hud-header {{ top: 12px; left: 12px; padding: 8px 12px; }}
    .telemetry-hud {{ top: 64px; left: 12px; padding: 10px 12px; min-width: 200px; }}
    .focus-hud {{ top: 12px; right: 12px; padding: 10px 14px; min-width: 180px; }}
    .quick-focus-bar {{ bottom: 16px; padding: 6px 8px; gap: 6px; }}
    .focus-btn {{ padding: 6px 10px; font-size: 11px; }}
    .fab-group {{ right: 12px; bottom: 74px; }}
    .interaction-hint {{ display: none; }}
  }}
</style>
<script src="https://cdn.babylonjs.com/babylon.js"></script>
<script src="https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js"></script>
</head>
<body>

  <!-- Background CRT Video -->
  <video id="crt-video" autoplay loop muted playsinline>
    <source src="data:video/webm;base64,{crt_b64}" type="video/webm">
  </video>

  <!-- CRT Overlay & Ultra-Fine Scanlines -->
  <div class="crt-overlay"></div>

  <!-- Header HUD Branding -->
  <div class="hud-header">
    <div class="hud-logo">LUNAROT®</div>
    <div class="hud-badge">HIGH-DPI 8x8 DEEP DITHER SCANNER</div>
  </div>

  <!-- Live Camera XYZ & Angles Telemetry HUD Panel -->
  <div class="telemetry-hud">
    <div class="telemetry-header">
      <span>CAMERA XYZ & ROTATION</span>
      <button class="copy-coords-btn" onclick="copyCameraCoords()">COPY DATA</button>
    </div>
    <div class="telemetry-grid">
      <div class="telemetry-item">X: <span id="cam-tx" class="telemetry-val">0.00</span></div>
      <div class="telemetry-item">Y: <span id="cam-ty" class="telemetry-val">85.00</span></div>
      <div class="telemetry-item">Z: <span id="cam-tz" class="telemetry-val">0.00</span></div>
      <div class="telemetry-item">RAD: <span id="cam-r" class="telemetry-val">185.00</span></div>
      <div class="telemetry-item">ALPHA: <span id="cam-a" class="telemetry-val">1.57</span></div>
      <div class="telemetry-item">BETA: <span id="cam-b" class="telemetry-val">1.57</span></div>
    </div>
  </div>

  <!-- Active Focus Info HUD -->
  <div class="focus-hud" id="focus-hud">
    <div class="focus-label" id="hud-status">● TARGET LOCKED</div>
    <div class="focus-title" id="hud-title">Full Skeleton</div>
    <div class="focus-sub" id="hud-sub">Anatomical System • 217 Bones</div>
  </div>

  <!-- Floating Action Buttons for Zoom & Tools -->
  <div class="fab-group">
    <button class="fab-btn" id="btn-zoom-in" title="Zoom In">+</button>
    <button class="fab-btn" id="btn-zoom-out" title="Zoom Out">−</button>
    <button class="fab-btn" id="btn-rotate" title="Toggle Auto Rotation">⟲</button>
    <button class="fab-btn" id="btn-reset" title="Reset View (Full Body)">⌂</button>
    <button class="fab-btn" id="btn-fullscreen" title="Toggle Fullscreen">⛶</button>
  </div>

  <!-- Interaction Hint -->
  <div class="interaction-hint">
    TAP / CLICK BONE TO FOCUS • PINCH / SCROLL TO ZOOM • DRAG TO ROTATE
  </div>

  <!-- Quick Focus Preset Camera Bar -->
  <div class="quick-focus-bar">
    <button class="focus-btn active" id="btn-preset-full" onclick="focusPreset('full')">🧍 Full Body</button>
    <button class="focus-btn" id="btn-preset-skull" onclick="focusPreset('skull')">💀 Head / Teeth</button>
    <button class="focus-btn" id="btn-preset-spine" onclick="focusPreset('spine')">🦴 Spine & Neck</button>
    <button class="focus-btn" id="btn-preset-thorax" onclick="focusPreset('thorax')">🫁 Thorax & Ribs</button>
    <button class="focus-btn" id="btn-preset-pelvis" onclick="focusPreset('pelvis')">🦴 Pelvis</button>
    <button class="focus-btn" id="btn-preset-hands" onclick="focusPreset('hands')">🖐️ Arms & Hands</button>
    <button class="focus-btn" id="btn-preset-feet" onclick="focusPreset('feet')">🦶 Legs & Feet</button>
  </div>

  <!-- 3D Babylon Canvas -->
  <canvas id="render-canvas"></canvas>

<script>
  const GLB_BASE64 = "{glb_b64}";

  const canvas = document.getElementById("render-canvas");
  
  // Enable Native High-DPI Hardware Scaling
  const engine = new BABYLON.Engine(canvas, true, {{
    preserveDrawingBuffer: true,
    stencil: true,
    adaptToDeviceRatio: true
  }});
  engine.setHardwareScalingLevel(1.0 / Math.max(window.devicePixelRatio || 1.0, 2.0));

  const scene = new BABYLON.Scene(engine);
  scene.clearColor = new BABYLON.Color4(0, 0, 0, 0);

  // Setup Highlight Layer for pure white outline selection glow
  const hl = new BABYLON.HighlightLayer("hl1", scene);
  hl.outerGlow = true;
  hl.innerGlow = false;

  // Arc Rotate Camera setup tuned to initial user fullbody view
  const cam = new BABYLON.ArcRotateCamera("Camera", 0.67, 2.68, 86.8, new BABYLON.Vector3(-0.0, 139.9, -6.1), scene);
  cam.attachControl(canvas, true);
  cam.wheelPrecision = 8;
  cam.pinchPrecision = 12;
  cam.panningSensibility = 50;
  cam.lowerRadiusLimit = 2.0;
  cam.upperRadiusLimit = 400.0;
  cam.useAutoRotationBehavior = false;

  // High Contrast Monochrome Greyscale Lighting setup
  const hemiLight = new BABYLON.HemisphericLight("hemiLight", new BABYLON.Vector3(0, 1, 0), scene);
  hemiLight.intensity = 1.4;
  hemiLight.groundColor = new BABYLON.Color3(0.0, 0.0, 0.0);
  hemiLight.diffuse = new BABYLON.Color3(1.0, 1.0, 1.0);

  const dirLight1 = new BABYLON.DirectionalLight("dirLight1", new BABYLON.Vector3(-1, -2, 1), scene);
  dirLight1.intensity = 1.3;
  dirLight1.diffuse = new BABYLON.Color3(1.0, 1.0, 1.0);

  const dirLight2 = new BABYLON.DirectionalLight("dirLight2", new BABYLON.Vector3(1, 1, -1), scene);
  dirLight2.intensity = 0.9;
  dirLight2.diffuse = new BABYLON.Color3(0.7, 0.7, 0.7);

  // Deep 8x8 64-Level Bayer Ordered Dither Shader
  BABYLON.Effect.ShadersStore["deepBayerDitherFragmentShader"] = `
    precision highp float;
    varying vec2 vUV;
    uniform sampler2D textureSampler;
    uniform vec2 uResolution;
    uniform float uGridSize;

    float getBayer8(vec2 pos) {{
      ivec2 p = ivec2(mod(pos, 8.0));
      float val = 0.0;
      if (p.y == 0) {{ if(p.x==0) val=0.0; else if(p.x==1) val=32.0; else if(p.x==2) val=8.0; else if(p.x==3) val=40.0; else if(p.x==4) val=2.0; else if(p.x==5) val=34.0; else if(p.x==6) val=10.0; else val=42.0; }}
      else if (p.y == 1) {{ if(p.x==0) val=48.0; else if(p.x==1) val=16.0; else if(p.x==2) val=56.0; else if(p.x==3) val=24.0; else if(p.x==4) val=50.0; else if(p.x==5) val=18.0; else if(p.x==6) val=58.0; else val=26.0; }}
      else if (p.y == 2) {{ if(p.x==0) val=12.0; else if(p.x==1) val=44.0; else if(p.x==2) val=4.0; else if(p.x==3) val=36.0; else if(p.x==4) val=14.0; else if(p.x==5) val=46.0; else if(p.x==6) val=6.0; else val=38.0; }}
      else if (p.y == 3) {{ if(p.x==0) val=60.0; else if(p.x==1) val=28.0; else if(p.x==2) val=52.0; else if(p.x==3) val=20.0; else if(p.x==4) val=62.0; else if(p.x==5) val=30.0; else if(p.x==6) val=54.0; else val=22.0; }}
      else if (p.y == 4) {{ if(p.x==0) val=3.0; else if(p.x==1) val=35.0; else if(p.x==2) val=11.0; else if(p.x==3) val=43.0; else if(p.x==4) val=1.0; else if(p.x==5) val=33.0; else if(p.x==6) val=9.0; else val=41.0; }}
      else if (p.y == 5) {{ if(p.x==0) val=51.0; else if(p.x==1) val=19.0; else if(p.x==2) val=59.0; else if(p.x==3) val=27.0; else if(p.x==4) val=49.0; else if(p.x==5) val=17.0; else if(p.x==6) val=57.0; else val=25.0; }}
      else if (p.y == 6) {{ if(p.x==0) val=15.0; else if(p.x==1) val=47.0; else if(p.x==2) val=7.0; else if(p.x==3) val=39.0; else if(p.x==4) val=13.0; else if(p.x==5) val=45.0; else if(p.x==6) val=5.0; else val=37.0; }}
      else {{ if(p.x==0) val=63.0; else if(p.x==1) val=31.0; else if(p.x==2) val=55.0; else if(p.x==3) val=23.0; else if(p.x==4) val=61.0; else if(p.x==5) val=29.0; else if(p.x==6) val=53.0; else val=21.0; }}
      return (val + 0.5) / 64.0;
    }}

    void main() {{
      vec2 fragCoord = gl_FragCoord.xy;
      vec2 cellCoord = fragCoord / uGridSize;
      vec4 tex = texture2D(textureSampler, vUV);
      
      // Calculate greyscale luminance with gamma curve for rich deep shadows
      float luminance = dot(tex.rgb, vec3(0.299, 0.587, 0.114));
      luminance = pow(luminance, 1.25);
      
      // Deep 8x8 Bayer threshold lookup
      float threshold = getBayer8(cellCoord);
      float dithered = luminance >= threshold ? 1.0 : 0.0;
      
      gl_FragColor = vec4(vec3(dithered) * tex.a, tex.a);
    }}
  `;

  const ditherPass = new BABYLON.PostProcess(
    "DeepBayerDitherShader",
    "deepBayerDither",
    ["uResolution", "uGridSize"],
    null,
    1.0,
    cam
  );

  ditherPass.onApply = function(effect) {{
    effect.setFloat2("uResolution", engine.getRenderWidth(), engine.getRenderHeight());
    effect.setFloat("uGridSize", 1.25);
  }};

  // Organic Handheld Micro Camera Sway Engine
  let swayTime = 0;
  let isCameraAnimating = false;

  scene.onBeforeRenderObservable.add(() => {{
    swayTime += engine.getDeltaTime() * 0.001;

    // Multi-octave natural breathing & handheld camera drift (subtle micro motion)
    const swayAlpha = (Math.sin(swayTime * 0.75) * 0.003 + Math.cos(swayTime * 1.35) * 0.0015);
    const swayBeta  = (Math.cos(swayTime * 0.95) * 0.0025 + Math.sin(swayTime * 1.65) * 0.0012);
    const swayY     = (Math.sin(swayTime * 0.85) * 0.06);
    const swayX     = (Math.cos(swayTime * 0.65) * 0.04);

    // Apply micro sway continuously when not auto-animating preset transitions
    if (!isCameraAnimating && !cam.useAutoRotationBehavior) {{
      cam.alpha += swayAlpha * 0.04;
      cam.beta  += swayBeta * 0.04;
      cam.target.x += swayX * 0.01;
      cam.target.y += swayY * 0.01;
    }}

    // Update Live Telemetry Readouts
    document.getElementById('cam-tx').textContent = cam.target.x.toFixed(2);
    document.getElementById('cam-ty').textContent = cam.target.y.toFixed(2);
    document.getElementById('cam-tz').textContent = cam.target.z.toFixed(2);
    document.getElementById('cam-r').textContent = cam.radius.toFixed(2);
    document.getElementById('cam-a').textContent = cam.alpha.toFixed(2);
    document.getElementById('cam-b').textContent = cam.beta.toFixed(2);
  }});

  // Copy Full Camera Coordinates & Angles (X, Y, Z, Radius, Alpha, Beta)
  function copyCameraCoords() {{
    const coordsStr = `target: new BABYLON.Vector3(${{cam.target.x.toFixed(1)}}, ${{cam.target.y.toFixed(1)}}, ${{cam.target.z.toFixed(1)}}), radius: ${{cam.radius.toFixed(1)}}, alpha: ${{cam.alpha.toFixed(2)}}, beta: ${{cam.beta.toFixed(2)}}`;
    navigator.clipboard.writeText(coordsStr).then(() => {{
      const btn = document.querySelector('.copy-coords-btn');
      btn.textContent = 'COPIED!';
      setTimeout(() => btn.textContent = 'COPY DATA', 1500);
    }}).catch(() => {{
      alert(coordsStr);
    }});
  }}

  // User Preset Coordinates updated with exact custom positions and angles
  const EXACT_PRESETS = {{
    'full':   {{ target: new BABYLON.Vector3(-0.0, 139.9, -6.1), radius: 86.8, alpha: 0.67, beta: 2.68, title: 'Full Skeleton', sub: 'Anatomical System • 217 Bones' }},
    'skull':  {{ target: new BABYLON.Vector3(-0.0, 156.9, 5.2),  radius: 17.4, alpha: 1.02, beta: 2.52, title: 'Cranium, Teeth & Jaw', sub: 'Upper & Lower Teeth Rows, Mandible, Cranium' }},
    'spine':  {{ target: new BABYLON.Vector3(0.0, 149.3, -2.6),  radius: 32.5, alpha: 3.79, beta: 2.16, title: 'Vertebral Column', sub: 'Cervical, Thoracic & Lumbar Vertebrae' }},
    'thorax': {{ target: new BABYLON.Vector3(0.0, 125.6, -6.3),  radius: 41.0, alpha: 1.20, beta: 2.35, title: 'Thoracic Skeleton', sub: 'Sternum & Ribs (1–12)' }},
    'pelvis': {{ target: new BABYLON.Vector3(0.0, 90.0, 0.0),    radius: 51.9, alpha: 2.66, beta: 2.02, title: 'Pelvic Girdle', sub: 'Sacrum, Coccyx & Hip Bones' }},
    'hands':  {{ target: new BABYLON.Vector3(25.2, 84.1, 2.2),   radius: 25.2, alpha: 1.39, beta: 2.51, title: 'Upper Extremities', sub: 'Scapula, Humerus, Radius, Ulna, Carpals' }},
    'feet':   {{ target: new BABYLON.Vector3(0.0, 35.0, 0.0),    radius: 65.0, alpha: 0.29, beta: 2.98, title: 'Lower Extremities', sub: 'Femur, Patella, Tibia, Fibula, Tarsals' }}
  }};

  // Load 3D GLB Model from Base64
  const binaryString = window.atob(GLB_BASE64);
  const bytes = new Uint8Array(binaryString.length);
  for (let i = 0; i < binaryString.length; i++) {{
    bytes[i] = binaryString.charCodeAt(i);
  }}
  const blob = new Blob([bytes.buffer], {{ type: 'model/gltf-binary' }});
  const modelUrl = URL.createObjectURL(blob);

  BABYLON.SceneLoader.Append("", modelUrl, scene, function(scene) {{
    console.log("Lunarot 3D Skeleton Model successfully loaded.");

    // Hide only soft tissue nasal cartilages (keep costal cartilages untouched)
    scene.meshes.forEach(mesh => {{
      if (!mesh || !mesh.name) return;
      const nameLower = mesh.name.toLowerCase();
      if (nameLower.includes('nasal septal') || nameLower.includes('alar cartilage') || nameLower.includes('nasal cartilage')) {{
        mesh.isVisible = false;
      }}
      if (mesh.material && mesh.material.backFaceCulling !== undefined) {{
        mesh.material.backFaceCulling = false;
      }}
    }});

    // Open Mandible / Jaw by rotating locally around X-axis (~0.12 rad / 7 degrees)
    // This parts the jaw open without destroying parent quaternion alignment, revealing upper and lower teeth rows
    scene.transformNodes.forEach(node => {{
      if (node.name && node.name.toLowerCase().includes('mandible')) {{
        node.rotate(BABYLON.Axis.X, 0.12, BABYLON.Space.LOCAL);
      }}
    }});
    scene.meshes.forEach(mesh => {{
      if (mesh.name && mesh.name.toLowerCase().includes('mandible')) {{
        mesh.rotate(BABYLON.Axis.X, 0.12, BABYLON.Space.LOCAL);
      }}
    }});

    // Auto-focus full body on load
    setTimeout(() => focusPreset('full'), 100);
  }}, null, function(s, msg, ex) {{
    console.error("Error loading 3D skeleton:", msg, ex);
  }}, ".glb");

  // Smooth Camera Animation to Target Position, Radius, Alpha (Yaw), and Beta (Pitch/Tilt)
  function animateCamera(targetPos, desiredRadius, desiredAlpha = null, desiredBeta = null, speed = 35) {{
    isCameraAnimating = true;

    BABYLON.Animation.CreateAndStartAnimation(
      'camTargetAnim', cam, 'target', 60, speed,
      cam.target.clone(), targetPos,
      BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT,
      new BABYLON.CubicEase(),
      () => {{ isCameraAnimating = false; }}
    );

    BABYLON.Animation.CreateAndStartAnimation(
      'camRadiusAnim', cam, 'radius', 60, speed,
      cam.radius, desiredRadius,
      BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT,
      new BABYLON.CubicEase()
    );

    if (desiredAlpha !== null && desiredAlpha !== undefined) {{
      BABYLON.Animation.CreateAndStartAnimation(
        'camAlphaAnim', cam, 'alpha', 60, speed,
        cam.alpha, desiredAlpha,
        BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT,
        new BABYLON.CubicEase()
      );
    }}

    if (desiredBeta !== null && desiredBeta !== undefined) {{
      BABYLON.Animation.CreateAndStartAnimation(
        'camBetaAnim', cam, 'beta', 60, speed,
        cam.beta, desiredBeta,
        BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT,
        new BABYLON.CubicEase()
      );
    }}
  }}

  function focusPreset(presetKey) {{
    const p = EXACT_PRESETS[presetKey];
    if (!p) return;
    
    hl.removeAllMeshes();
    animateCamera(p.target, p.radius, p.alpha, p.beta);
    updateHUD(p.title, p.sub);

    // Update active button state
    document.querySelectorAll('.focus-btn').forEach(btn => btn.classList.remove('active'));
    const activeBtn = document.getElementById('btn-preset-' + presetKey);
    if (activeBtn) activeBtn.classList.add('active');
  }}

  // Interactive 3D Mesh Picking (Click/Tap on any individual bone)
  scene.onPointerObservable.add(function(evt) {{
    if (evt.type === BABYLON.PointerEventTypes.POINTERTAP) {{
      const pickResult = scene.pick(scene.pointerX, scene.pointerY);
      if (pickResult && pickResult.hit && pickResult.pickedMesh) {{
        const mesh = pickResult.pickedMesh;
        hl.removeAllMeshes();
        hl.addMesh(mesh, new BABYLON.Color3(1.0, 1.0, 1.0)); // Pure white outline selection

        mesh.computeWorldMatrix(true);
        const boundingInfo = mesh.getBoundingInfo();
        const centerWorld = boundingInfo.boundingSphere.centerWorld;
        const radiusWorld = boundingInfo.boundingSphere.radiusWorld;
        const idealRadius = Math.max(radiusWorld * 3.5, 12.0);

        animateCamera(centerWorld, idealRadius);

        const parentName = mesh.parent ? mesh.parent.name.replace('.g', '').replace('.r', '').replace('.l', '') : 'Skeletal System';
        updateHUD(mesh.name, parentName);
      }}
    }}
  }});

  // Update HUD Display text
  function updateHUD(title, sub) {{
    document.getElementById('hud-title').textContent = title;
    document.getElementById('hud-sub').textContent = sub;
  }}

  // Floating Action Button Listeners
  document.getElementById('btn-zoom-in').onclick = () => {{
    cam.radius = Math.max(cam.radius * 0.65, cam.lowerRadiusLimit);
  }};

  document.getElementById('btn-zoom-out').onclick = () => {{
    cam.radius = Math.min(cam.radius * 1.45, cam.upperRadiusLimit);
  }};

  document.getElementById('btn-rotate').onclick = (e) => {{
    cam.useAutoRotationBehavior = !cam.useAutoRotationBehavior;
    if (cam.useAutoRotationBehavior) {{
      cam.autoRotationBehavior.idleRotationSpeed = 0.3;
    }}
    e.target.style.borderColor = cam.useAutoRotationBehavior ? '#ffffff' : 'rgba(255,255,255,0.2)';
  }};

  document.getElementById('btn-reset').onclick = () => {{
    focusPreset('full');
  }};

  document.getElementById('btn-fullscreen').onclick = () => {{
    if (!document.fullscreenElement) {{
      document.documentElement.requestFullscreen().catch(err => {{}});
    }} else {{
      document.exitFullscreen().catch(err => {{}});
    }}
  }};

  // Keyboard Navigation (+/- zoom)
  window.addEventListener('keydown', (e) => {{
    if (e.key === '+' || e.key === '=') cam.radius = Math.max(cam.radius * 0.75, cam.lowerRadiusLimit);
    if (e.key === '-' || e.key === '_') cam.radius = Math.min(cam.radius * 1.25, cam.upperRadiusLimit);
  }});

  // Render Loop & Resize Handling
  engine.runRenderLoop(() => scene.render());
  window.addEventListener("resize", () => engine.resize());

</script>
</body>
</html>
'''

output_path = 'open3dviewer_skeletal_figure.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"SUCCESS! Rebuilt Viewer with Parted Mandible to Prominently Display Teeth Rows ({os.path.getsize(output_path)} bytes)")
