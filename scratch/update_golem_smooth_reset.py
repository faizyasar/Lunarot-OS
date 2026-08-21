import re

filepath = r'c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\golem.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update focusPreset to take retractBones = true
old_preset = """  function focusPreset(presetKey) {
    window.activePresetKey = presetKey;
    const p = EXACT_PRESETS[presetKey];
    if (!p) return;
    
    // Retract any exploded bones on camera change
    if (typeof scene !== 'undefined' && scene.meshes) {"""

new_preset = """  function focusPreset(presetKey, retractBones = true) {
    window.activePresetKey = presetKey;
    const p = EXACT_PRESETS[presetKey];
    if (!p) return;
    
    // Retract any exploded bones on camera change
    if (retractBones && typeof scene !== 'undefined' && scene.meshes) {"""

# 2. Update POINTERUP to not retract bones and add a 2 second delay before rubber banding
old_pointer = """  // Interactive Drag Rubber-Banding and Hover Tracking
  scene.onPointerObservable.add(function(evt) {
    if (evt.type === BABYLON.PointerEventTypes.POINTERUP) {
      if (window.activePresetKey) {
        // Snap back to the current preset
        focusPreset(window.activePresetKey);
      }
    } else if (evt.type === BABYLON.PointerEventTypes.POINTERMOVE) {"""

new_pointer = """  // Interactive Drag Rubber-Banding and Hover Tracking
  let rubberBandTimeout = null;
  scene.onPointerObservable.add(function(evt) {
    if (evt.type === BABYLON.PointerEventTypes.POINTERDOWN) {
      if (rubberBandTimeout) clearTimeout(rubberBandTimeout);
    } else if (evt.type === BABYLON.PointerEventTypes.POINTERUP) {
      if (window.activePresetKey) {
        if (rubberBandTimeout) clearTimeout(rubberBandTimeout);
        // Add a smooth 1.5 second delay before snapping the camera back, and don't retract bones
        rubberBandTimeout = setTimeout(() => {
            focusPreset(window.activePresetKey, false);
        }, 1500);
      }
    } else if (evt.type === BABYLON.PointerEventTypes.POINTERMOVE) {"""

if old_preset in content and old_pointer in content:
    content = content.replace(old_preset, new_preset)
    content = content.replace(old_pointer, new_pointer)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated successfully!")
else:
    print("Error: Could not find strings to replace.")
