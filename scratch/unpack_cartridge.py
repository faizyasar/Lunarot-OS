import json
import re
import os

# Read the HTML provided by the user (save it to a file first)
user_html = r"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Bundled Page</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #1a1a1a; display: flex; align-items: center; justify-content: center; min-height: 100vh; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    #__bundler_loading { position: fixed; bottom: 20px; right: 20px; font: 13px/1.4 -apple-system, BlinkMacSystemFont, sans-serif; color: #666; background: #fff; padding: 8px 14px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.12); z-index: 10000; }
    #__bundler_thumbnail { position: fixed; inset: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: #1a1a1a; z-index: 9999; }
    #__bundler_thumbnail svg { width: 100%; height: 100%; object-fit: contain; }
    #__bundler_placeholder { color: #999; font-size: 14px; }
  </style>
  <noscript>
    <style>#__bundler_loading { display: none; }</style>
    <div style="position:fixed;bottom:12px;left:12px;font:13px/1.4 -apple-system,BlinkMacSystemFont,sans-serif;color:#999;background:rgba(255,255,255,0.9);padding:6px 12px;border-radius:6px;box-shadow:0 1px 4px rgba(0,0,0,0.08);z-index:10000;">
      This page requires JavaScript to display.
    </div>
  </noscript>
</head>
<body>
  <div id="__bundler_thumbnail">
  <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <rect x="60" y="30" width="80" height="140" rx="6" fill="#6e6459"></rect>
    <rect x="72" y="75" width="56" height="58" fill="#e6e0d8" rx="4"></rect>
  </svg>
</div>
  <div id="__bundler_loading">Unpacking...</div>

  <script>
document.addEventListener('DOMContentLoaded', async function() {
  const loading = document.getElementById('__bundler_loading');
  function setStatus(msg) { if (loading) loading.textContent = msg; }
  try {
    const manifestEl = document.querySelector('script[type="__bundler/manifest"]');
    const templateEl = document.querySelector('script[type="__bundler/template"]');
    const manifest = JSON.parse(manifestEl.textContent);
    let template = JSON.parse(templateEl.textContent);
    const extResEl = document.querySelector('script[type="__bundler/ext_resources"]');
    const extResources = extResEl ? JSON.parse(extResEl.textContent) : [];
    const resourceMap = {};
    for (const [uuid, entry] of Object.entries(manifest)) {
      const dataUrl = `data:${entry.mime};base64,${entry.data}`;
      template = template.split(uuid).join(dataUrl);
    }
    for (const entry of extResources) {
      if (manifest[entry.uuid]) {
        resourceMap[entry.id] = `data:${manifest[entry.uuid].mime};base64,${manifest[entry.uuid].data}`;
      }
    }
    const resourceScript = '<script>window.__resources = ' + JSON.stringify(resourceMap).replace(/<\\//g, '<\\\\/') + ';<\\/script>';
    template = template.replace('<head>', '<head>\\n' + resourceScript);
    const doc = new DOMParser().parseFromString(template, 'text/html');
    document.documentElement.replaceWith(doc.documentElement);
    for (const old of Array.from(document.scripts)) {
      const s = document.createElement('script');
      for (const a of old.attributes) s.setAttribute(a.name, a.value);
      s.textContent = old.textContent;
      const p = s.src ? new Promise(r => { s.onload = s.onerror = r; }) : null;
      old.replaceWith(s);
      if (p) await p;
    }
  } catch (err) {
    console.error('Unpack error:', err);
  }
});
  </script>
"""

with open(r'c:\Users\faizy\Desktop\HTMLS\Gameboy Cartridge.html', 'r', encoding='utf-8') as f:
    pass
