import re

filepath = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\open3dviewer_skeletal_figure.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Modify Camera setup
old_cam_setup = """  cam.attachControl(canvas, true);
  cam.wheelPrecision = 8;
  cam.pinchPrecision = 12;
  cam.panningSensibility = 50;"""

new_cam_setup = """  cam.attachControl(canvas, true);
  if (cam.inputs.attached.mousewheel) cam.inputs.remove(cam.inputs.attached.mousewheel);
  if (cam.inputs.attached.keyboard) cam.inputs.remove(cam.inputs.attached.keyboard);
  cam.panningSensibility = 0; // Disable panning completely"""
content = content.replace(old_cam_setup, new_cam_setup)

# 2. Remove mesh picking and add rubber banding
old_pointer = """  // Interactive 3D Mesh Picking (Click/Tap on any individual bone)
  scene.onPointerObservable.add(function(evt) {
    if (evt.type === BABYLON.PointerEventTypes.POINTERTAP) {
      const pickResult = scene.pick(scene.pointerX, scene.pointerY);
      if (pickResult && pickResult.hit && pickResult.pickedMesh) {
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
        let cleanName = mesh.name;
        if (cleanName.includes('Object_')) cleanName = "Human Skeleton Model";
        updateHUD(cleanName, parentName);
      }
    }
  });"""

new_pointer = """  // Store the active preset for rubber-banding
  window.activePresetKey = 'full';

  // Interactive Drag Rubber-Banding
  scene.onPointerObservable.add(function(evt) {
    if (evt.type === BABYLON.PointerEventTypes.POINTERUP) {
      if (window.activePresetKey) {
        // Snap back to the current preset
        focusPreset(window.activePresetKey);
      }
    }
  });"""
content = content.replace(old_pointer, new_pointer)

# 3. Update focusPreset to track active preset
old_focus = """  function focusPreset(presetKey) {
    const p = EXACT_PRESETS[presetKey];"""
new_focus = """  function focusPreset(presetKey) {
    window.activePresetKey = presetKey;
    const p = EXACT_PRESETS[presetKey];"""
content = content.replace(old_focus, new_focus)

# 4. Remove Floating Action Buttons (HTML)
old_fab_html = """  <!-- Floating Action Buttons for Zoom & Tools -->
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
  </div>"""
content = content.replace(old_fab_html, "")

# 5. Remove Floating Action Button Listeners (JS)
old_fab_js = """  // Floating Action Button Listeners
  document.getElementById('btn-zoom-in').onclick = () => {
    cam.radius = Math.max(cam.radius * 0.65, cam.lowerRadiusLimit);
  };

  document.getElementById('btn-zoom-out').onclick = () => {
    cam.radius = Math.min(cam.radius * 1.45, cam.upperRadiusLimit);
  };

  document.getElementById('btn-rotate').onclick = (e) => {
    cam.useAutoRotationBehavior = !cam.useAutoRotationBehavior;
    if (cam.useAutoRotationBehavior) {
      cam.autoRotationBehavior.idleRotationSpeed = 0.3;
    }
    e.target.style.borderColor = cam.useAutoRotationBehavior ? '#ffffff' : 'rgba(255,255,255,0.2)';
  };

  document.getElementById('btn-reset').onclick = () => {
    focusPreset('full');
  };

  document.getElementById('btn-fullscreen').onclick = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => {});
    } else {
      document.exitFullscreen().catch(err => {});
    }
  };

  // Keyboard Navigation (+/- zoom)
  window.addEventListener('keydown', (e) => {
    if (e.key === '+' || e.key === '=') cam.radius = Math.max(cam.radius * 0.75, cam.lowerRadiusLimit);
    if (e.key === '-' || e.key === '_') cam.radius = Math.min(cam.radius * 1.25, cam.upperRadiusLimit);
  });"""
content = content.replace(old_fab_js, "")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully.")
