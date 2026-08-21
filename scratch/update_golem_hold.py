import re

filepath = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the render loop
old_render = """    // Micro-explosion hover repulsion with 5s hold and slow retract
    const effectRadius = 15.0; // Explosion radius
    const maxPush = 2.5; // How far to push out
    const maxScale = 1.15; // How much to scale up
    const now = performance.now();

    scene.meshes.forEach(mesh => {
      if (mesh.metadata && mesh.metadata.basePosition) {
        mesh.metadata.state = mesh.metadata.state || 0; // 0: resting, 1: exploded, 2: retracting
        mesh.metadata.explodeTimer = mesh.metadata.explodeTimer || 0;
        
        let targetPos = mesh.metadata.basePosition;
        let targetScale = mesh.metadata.baseScaling;
        let lerpSpeed = 0.2; // default fast lerp

        // State 0: Resting, waiting for hover
        if (mesh.metadata.state === 0) {
          if (window.currentHitPoint) {
            const dist = BABYLON.Vector3.Distance(mesh.metadata.baseAbsPos, window.currentHitPoint);
            if (dist < effectRadius) {
              mesh.metadata.state = 1;
              mesh.metadata.explodeTimer = now + 5000; // stick out for 5 seconds
              
              const strength = 1.0 - (dist / effectRadius);
              let pushDir = mesh.metadata.baseAbsPos.subtract(window.currentHitPoint);
              if (pushDir.lengthSquared() > 0.001) {
                  pushDir.normalize();
              } else {
                  pushDir = new BABYLON.Vector3(0, 1, 0);
              }

              const localPush = BABYLON.Vector3.TransformNormal(pushDir, mesh.metadata.invParentWorld);
              const easedStrength = strength * strength * (3 - 2 * strength); 
              
              mesh.metadata.targetPos = mesh.metadata.basePosition.add(localPush.scale(easedStrength * maxPush));
              mesh.metadata.targetScale = mesh.metadata.baseScaling.scale(1.0 + easedStrength * (maxScale - 1.0));
            }
          }
        }
        
        // State 1: Exploded (holding position)
        if (mesh.metadata.state === 1) {
          targetPos = mesh.metadata.targetPos;
          targetScale = mesh.metadata.targetScale;
          lerpSpeed = 0.2; // smooth explosion outward
          
          if (now > mesh.metadata.explodeTimer) {
             mesh.metadata.state = 2; // begin slow retract
          }
        }
        
        // State 2: Retracting (uninteractable)
        if (mesh.metadata.state === 2) {
          targetPos = mesh.metadata.basePosition;
          targetScale = mesh.metadata.baseScaling;
          lerpSpeed = 0.015; // slow return to normal
          
          if (BABYLON.Vector3.DistanceSquared(mesh.position, targetPos) < 0.0001) {
             mesh.metadata.state = 0; // done retracting, interactable again
             mesh.position.copyFrom(targetPos);
             mesh.scaling.copyFrom(targetScale);
          }
        }

        mesh.position = BABYLON.Vector3.Lerp(mesh.position, targetPos, lerpSpeed);
        mesh.scaling = BABYLON.Vector3.Lerp(mesh.scaling, targetScale, lerpSpeed);
      }
    });"""

new_render = """    // Micro-explosion hover repulsion that sticks out indefinitely
    const effectRadius = 15.0; // Explosion radius
    const maxPush = 2.5; // How far to push out
    const maxScale = 1.15; // How much to scale up

    scene.meshes.forEach(mesh => {
      if (mesh.metadata && mesh.metadata.basePosition) {
        mesh.metadata.state = mesh.metadata.state || 0; // 0: resting, 1: exploded, 2: retracting
        
        let targetPos = mesh.metadata.basePosition;
        let targetScale = mesh.metadata.baseScaling;
        let lerpSpeed = 0.2; // default fast lerp

        // State 0: Resting, waiting for hover
        if (mesh.metadata.state === 0) {
          if (window.currentHitPoint) {
            const dist = BABYLON.Vector3.Distance(mesh.metadata.baseAbsPos, window.currentHitPoint);
            if (dist < effectRadius) {
              mesh.metadata.state = 1;
              
              const strength = 1.0 - (dist / effectRadius);
              let pushDir = mesh.metadata.baseAbsPos.subtract(window.currentHitPoint);
              if (pushDir.lengthSquared() > 0.001) {
                  pushDir.normalize();
              } else {
                  pushDir = new BABYLON.Vector3(0, 1, 0);
              }

              const localPush = BABYLON.Vector3.TransformNormal(pushDir, mesh.metadata.invParentWorld);
              const easedStrength = strength * strength * (3 - 2 * strength); 
              
              mesh.metadata.targetPos = mesh.metadata.basePosition.add(localPush.scale(easedStrength * maxPush));
              mesh.metadata.targetScale = mesh.metadata.baseScaling.scale(1.0 + easedStrength * (maxScale - 1.0));
            }
          }
        }
        
        // State 1: Exploded (holding position indefinitely until camera preset change)
        if (mesh.metadata.state === 1) {
          targetPos = mesh.metadata.targetPos;
          targetScale = mesh.metadata.targetScale;
          lerpSpeed = 0.2; // smooth explosion outward
        }
        
        // State 2: Retracting (uninteractable)
        if (mesh.metadata.state === 2) {
          targetPos = mesh.metadata.basePosition;
          targetScale = mesh.metadata.baseScaling;
          lerpSpeed = 0.015; // slow return to normal
          
          if (BABYLON.Vector3.DistanceSquared(mesh.position, targetPos) < 0.0001) {
             mesh.metadata.state = 0; // done retracting, interactable again
             mesh.position.copyFrom(targetPos);
             mesh.scaling.copyFrom(targetScale);
          }
        }

        mesh.position = BABYLON.Vector3.Lerp(mesh.position, targetPos, lerpSpeed);
        mesh.scaling = BABYLON.Vector3.Lerp(mesh.scaling, targetScale, lerpSpeed);
      }
    });"""

# 2. Update focusPreset to trigger retraction
old_preset = """  function focusPreset(presetKey) {
    window.activePresetKey = presetKey;
    const p = EXACT_PRESETS[presetKey];
    if (!p) return;
    
    hl.removeAllMeshes();"""

new_preset = """  function focusPreset(presetKey) {
    window.activePresetKey = presetKey;
    const p = EXACT_PRESETS[presetKey];
    if (!p) return;
    
    // Retract any exploded bones on camera change
    if (typeof scene !== 'undefined' && scene.meshes) {
      scene.meshes.forEach(mesh => {
        if (mesh.metadata && mesh.metadata.state === 1) {
          mesh.metadata.state = 2; // Trigger retraction
        }
      });
    }

    hl.removeAllMeshes();"""

if old_render in content and old_preset in content:
    content = content.replace(old_render, new_render)
    content = content.replace(old_preset, new_preset)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated successfully!")
else:
    print("Error: Could not find strings to replace.")
