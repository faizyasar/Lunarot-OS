import re

filepath = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\open3dviewer_skeletal_figure.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update GLB Loading to store transforms
old_glb_load = """    // Auto-focus full body on load
    setTimeout(() => focusPreset('full'), 100);"""

new_glb_load = """    // Store original transforms and precompute matrices for hover-explosion effect
    scene.meshes.forEach(mesh => {
      if (mesh.getTotalVertices() > 0) {
        mesh.metadata = mesh.metadata || {};
        mesh.metadata.basePosition = mesh.position.clone();
        mesh.metadata.baseScaling = mesh.scaling.clone();
        mesh.computeWorldMatrix(true);
        mesh.metadata.baseAbsPos = mesh.getAbsolutePosition().clone();
        mesh.metadata.invParentWorld = new BABYLON.Matrix();
        if (mesh.parent) {
            mesh.parent.getWorldMatrix().invertToRef(mesh.metadata.invParentWorld);
        } else {
            BABYLON.Matrix.IdentityToRef(mesh.metadata.invParentWorld);
        }
      }
    });

    // Auto-focus full body on load
    setTimeout(() => focusPreset('full'), 100);"""

content = content.replace(old_glb_load, new_glb_load)

# 2. Update render loop for explosion
old_render = """    if (!isCameraAnimating && !cam.useAutoRotationBehavior) {
      cam.alpha += swayAlpha * 0.04;
      cam.beta  += swayBeta * 0.04;
      cam.target.x += swayX * 0.01;
      cam.target.y += swayY * 0.01;
    }

    // Telemetry removed
  });"""

new_render = """    if (!isCameraAnimating && !cam.useAutoRotationBehavior) {
      cam.alpha += swayAlpha * 0.04;
      cam.beta  += swayBeta * 0.04;
      cam.target.x += swayX * 0.01;
      cam.target.y += swayY * 0.01;
    }

    // Micro-explosion hover repulsion
    const effectRadius = 15.0; // Explosion radius
    const maxPush = 2.5; // How far to push out
    const maxScale = 1.15; // How much to scale up

    scene.meshes.forEach(mesh => {
      if (mesh.metadata && mesh.metadata.basePosition) {
        let targetPos = mesh.metadata.basePosition;
        let targetScale = mesh.metadata.baseScaling;

        if (window.currentHitPoint) {
          const dist = BABYLON.Vector3.Distance(mesh.metadata.baseAbsPos, window.currentHitPoint);
          if (dist < effectRadius) {
            const strength = 1.0 - (dist / effectRadius);
            
            let pushDir = mesh.metadata.baseAbsPos.subtract(window.currentHitPoint);
            if (pushDir.lengthSquared() > 0.001) {
                pushDir.normalize();
            } else {
                pushDir = new BABYLON.Vector3(0, 1, 0);
            }

            const localPush = BABYLON.Vector3.TransformNormal(pushDir, mesh.metadata.invParentWorld);
            const easedStrength = strength * strength * (3 - 2 * strength); 
            
            targetPos = mesh.metadata.basePosition.add(localPush.scale(easedStrength * maxPush));
            targetScale = mesh.metadata.baseScaling.scale(1.0 + easedStrength * (maxScale - 1.0));
          }
        }
        mesh.position = BABYLON.Vector3.Lerp(mesh.position, targetPos, 0.2);
        mesh.scaling = BABYLON.Vector3.Lerp(mesh.scaling, targetScale, 0.2);
      }
    });

    // Telemetry removed
  });"""

content = content.replace(old_render, new_render)

# 3. Update pointer observer to track hit point
old_pointer = """  // Store the active preset for rubber-banding
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

new_pointer = """  // Store the active preset for rubber-banding
  window.activePresetKey = 'full';
  window.currentHitPoint = null;

  // Interactive Drag Rubber-Banding and Hover Tracking
  scene.onPointerObservable.add(function(evt) {
    if (evt.type === BABYLON.PointerEventTypes.POINTERUP) {
      if (window.activePresetKey) {
        // Snap back to the current preset
        focusPreset(window.activePresetKey);
      }
    } else if (evt.type === BABYLON.PointerEventTypes.POINTERMOVE) {
      const pickResult = scene.pick(scene.pointerX, scene.pointerY);
      if (pickResult && pickResult.hit) {
        window.currentHitPoint = pickResult.pickedPoint;
      } else {
        window.currentHitPoint = null;
      }
    }
  });"""

content = content.replace(old_pointer, new_pointer)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated with explosion effect!")
