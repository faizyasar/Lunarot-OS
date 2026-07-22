import { useEffect, useRef, useState } from 'react';

// --- StarsCanvas Module-Level State ---
let time = 0;
const pointer = { x: -2000, y: -2000, active: false };
const planets = [
  { name: 'Sun', symbol: '☉', deg: 120, color: '#ffffff' },
  { name: 'Moon', symbol: '☽', deg: 245, color: '#efede8' },
  { name: 'Rising', symbol: 'AC', deg: 45, color: '#efede8' },
  { name: 'Mars', symbol: '♂', deg: 180, color: '#ffffff' },
  { name: 'Venus', symbol: '♀', deg: 90, color: '#ffffff' }
];
const activePlanets = new Set(['Sun', 'Moon', 'Rising']);

function hexToRgb(hex: string) {
  if (!hex || hex.length < 7) return '200,164,90';
  return `${parseInt(hex.slice(1, 3), 16)},${parseInt(hex.slice(3, 5), 16)},${parseInt(hex.slice(5, 7), 16)}`;
}

function drawAlchemicalSigil(c: CanvasRenderingContext2D, x: number, y: number, size: number, seed: number) {
  c.save();
  c.translate(x + size / 2, y + size / 2);
  const r = size * 0.42;
  const type = Math.floor(seed) % 8;

  c.strokeStyle = 'rgba(255, 255, 255, 0.012)';
  c.lineWidth = 0.75;
  
  if (seed % 2 > 1) {
    c.strokeRect(-size / 2 + 1, -size / 2 + 1, size - 2, size - 2);
  } else {
    c.beginPath();
    c.arc(0, 0, r, 0, Math.PI * 2);
    c.stroke();
  }

  c.strokeStyle = 'rgba(255, 255, 255, 0.15)';
  c.beginPath();
  switch (type) {
    case 0:
      c.moveTo(-r, 0); c.lineTo(r, 0);
      c.moveTo(0, -r); c.lineTo(0, r);
      c.stroke();
      c.beginPath();
      c.arc(0, 0, r * 0.4, 0, Math.PI * 2);
      break;
    case 1:
      c.arc(0, 0, r * 0.7, 0, Math.PI * 2);
      c.arc(0, 0, r * 0.3, 0, Math.PI * 2);
      c.stroke();
      c.beginPath();
      c.arc(0, 0, 1.5, 0, Math.PI * 2);
      c.fillStyle = 'rgba(255, 255, 255, 0.2)';
      c.fill();
      break;
    case 2:
      c.moveTo(0, -r); c.lineTo(r * 0.86, r * 0.5); c.lineTo(-r * 0.86, r * 0.5);
      c.closePath();
      c.stroke();
      c.beginPath();
      c.arc(0, r * 0.15, r * 0.35, 0, Math.PI * 2);
      break;
    case 3:
      c.moveTo(0, -r); c.lineTo(0, r);
      c.moveTo(-r * 0.6, -r * 0.3); c.lineTo(r * 0.6, -r * 0.3);
      c.moveTo(-r * 0.6, r * 0.3); c.lineTo(r * 0.6, r * 0.3);
      break;
    case 4:
      c.arc(0, 0, r * 0.8, -Math.PI / 2, Math.PI);
      c.stroke();
      c.beginPath();
      c.arc(0, 0, r * 0.5, 0, Math.PI * 1.5);
      break;
    case 5:
      c.moveTo(-r * 0.7, -r * 0.7); c.lineTo(r * 0.7, -r * 0.7);
      c.lineTo(-r * 0.7, r * 0.7); c.lineTo(r * 0.7, r * 0.7);
      c.closePath();
      c.stroke();
      c.beginPath();
      c.moveTo(-r * 0.8, 0); c.lineTo(r * 0.8, 0);
      break;
    case 6:
      c.moveTo(0, -r); c.lineTo(r * 0.8, r * 0.2); c.lineTo(-r * 0.8, r * 0.2);
      c.closePath();
      c.moveTo(0, r * 0.2); c.lineTo(0, r * 0.9);
      c.moveTo(-r * 0.4, r * 0.65); c.lineTo(r * 0.4, r * 0.65);
      break;
    case 7:
      c.arc(0, 0, r * 0.6, 0, Math.PI * 2);
      c.stroke();
      c.beginPath();
      for (let a = 0; a < Math.PI * 2; a += Math.PI / 4) {
        c.moveTo(Math.cos(a) * r * 0.6, Math.sin(a) * r * 0.6);
        c.lineTo(Math.cos(a) * r, Math.sin(a) * r);
      }
      break;
  }
  c.stroke();
  c.restore();
}

let sigilsCanvas: HTMLCanvasElement | null = null;
function getSigilsCanvas() {
  if (sigilsCanvas) return sigilsCanvas;
  const cellSize = 30;
  sigilsCanvas = document.createElement('canvas');
  sigilsCanvas.width = 180;
  sigilsCanvas.height = 150;
  const c = sigilsCanvas.getContext('2d');
  if (!c) return sigilsCanvas;

  // Grid lines
  c.strokeStyle = 'rgba(255, 255, 255, 0.02)';
  c.lineWidth = 0.5;
  for (let r = 0; r <= 5; r++) {
    c.beginPath(); c.moveTo(0, r * cellSize); c.lineTo(180, r * cellSize); c.stroke();
  }
  for (let col = 0; col <= 6; col++) {
    c.beginPath(); c.moveTo(col * cellSize, 0); c.lineTo(col * cellSize, 150); c.stroke();
  }

  // Draw sigils
  for (let r = 0; r < 5; r++) {
    for (let col = 0; col < 6; col++) {
      const seedVal = (r * 13 + col * 37 + 7);
      drawAlchemicalSigil(c, col * cellSize, r * cellSize, cellSize, seedVal);
    }
  }
  return sigilsCanvas;
}

interface StarsCanvasProps {
  planets?: any[];
  activePlanets?: Set<string>;
}

export function StarsCanvas({ planets: customPlanets, activePlanets: customActivePlanets }: StarsCanvasProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const canvasGPURef = useRef<HTMLCanvasElement>(null);
  const planetsRef = useRef(customPlanets);
  const activePlanetsRef = useRef(customActivePlanets);
  const [webGpuActive, setWebGpuActive] = useState(false);

  useEffect(() => {
    planetsRef.current = customPlanets;
    activePlanetsRef.current = customActivePlanets;
  }, [customPlanets, customActivePlanets]);

  // WebGPU initialization & rendering loop
  useEffect(() => {
    if (!(navigator as any).gpu) return;
    let active = true;
    let device: any;
    let context: any;
    let pipeline: any;
    let uniformBuffer: any;
    let uniformBindGroup: any;
    let animId: number;

    const canvas = canvasGPURef.current;
    if (!canvas) return;

    async function initGPU() {
      try {
        const adapter = await (navigator as any).gpu.requestAdapter();
        if (!adapter) return;
        device = await adapter.requestDevice();
        if (!active) return;

        context = canvas.getContext('webgpu') as any;
        const format = (navigator as any).gpu.getPreferredCanvasFormat();
        context.configure({
          device,
          format,
          alphaMode: 'premultiplied'
        });

        // WGSL Shader code
        const shaderCode = `
          struct VertexOutput {
            @builtin(position) position: vec4<f32>,
            @location(0) uv: vec2<f32>,
          };

          struct Uniforms {
            time: f32,
            width: f32,
            height: f32,
            mouseX: f32,
            mouseY: f32,
            mouseActive: f32,
            pad1: f32,
            pad2: f32,
          };

          @group(0) @binding(0) var<uniform> uniforms: Uniforms;

          fn hash(p: vec2<f32>) -> f32 {
            var p3 = fract(vec3<f32>(p.xyx) * 0.13);
            p3 = p3 + dot(p3, p3.yzx + 3.33);
            return fract((p3.x + p3.y) * p3.z);
          }

          fn noise(p: vec2<f32>) -> f32 {
            let i = floor(p);
            let f = fract(p);
            let u = f * f * (3.0 - 2.0 * f);
            return mix(mix(hash(i + vec2<f32>(0.0,0.0)), hash(i + vec2<f32>(1.0,0.0)), u.x),
                       mix(hash(i + vec2<f32>(0.0,1.0)), hash(i + vec2<f32>(1.0,1.0)), u.x), u.y);
          }

          fn fbm(p: vec2<f32>) -> f32 {
            var v = 0.0;
            var a = 0.5;
            var shift = vec2<f32>(100.0);
            var p_mut = p;
            for (var i = 0; i < 4; i = i + 1) {
              v += a * noise(p_mut);
              p_mut = p_mut * 2.0 + shift;
              a *= 0.5;
            }
            return v;
          }

          @vertex
          fn vs_main(@builtin(vertex_index) vertexIndex: u32) -> VertexOutput {
            var out: VertexOutput;
            let x = f32(i32(vertexIndex & 1u) * 2 - 1);
            let y = f32(i32(vertexIndex & 2u) - 1);
            out.position = vec4<f32>(x, y, 0.0, 1.0);
            out.uv = vec2<f32>((x + 1.0) * 0.5, (1.0 - y) * 0.5);
            return out;
          }

          @fragment
          fn fs_main(in: VertexOutput) -> @location(0) vec4<f32> {
            let cx = uniforms.width * 0.5;
            let cy = uniforms.height * 0.5;
            let center = vec2<f32>(cx, cy);

            // Grid coordinates with mouse warp
            var grid_coord = in.position.xy;
            if (uniforms.mouseActive > 0.5) {
              let mouse_pos = vec2<f32>(uniforms.mouseX, uniforms.mouseY);
              let dist = distance(grid_coord, mouse_pos);
              if (dist < 180.0) {
                let force = (180.0 - dist) / 180.0;
                let dir = normalize(grid_coord - mouse_pos);
                // Warp space outwards
                grid_coord += dir * force * 18.0;
              }
            }

            let grid_size = 60.0;
            let gx = fract(grid_coord.x / grid_size);
            let gy = fract(grid_coord.y / grid_size);
            var grid_val = 0.0;
            if (gx < 0.015 || gy < 0.015) {
              grid_val = 0.024; // grid lines intensity
            }

            // Faint concentric orbits
            let dist_from_center = distance(in.position.xy, center);
            var orbit_val = 0.0;
            let orbits = array<f32, 5>(110.0, 190.0, 275.0, 360.0, 440.0);
            for (var i = 0; i < 5; i = i + 1) {
              let r = orbits[i];
              let dist_to_orbit = abs(dist_from_center - r);
              if (dist_to_orbit < 1.0) {
                var draw_orbit = true;
                if (i % 2 == 1) {
                  let angle = atan2(in.position.y - cy, in.position.x - cx);
                  let dash = fract(angle * 10.0 / 3.14159);
                  if (dash > 0.3) {
                    draw_orbit = false;
                  }
                }
                if (draw_orbit) {
                  orbit_val = max(orbit_val, (1.0 - dist_to_orbit) * 0.045);
                }
              }
            }

            // FBM Alchemical Nebula background
            let uv = (in.position.xy - center) / min(uniforms.width, uniforms.height);
            let noise_pos = uv * 2.8 + vec2<f32>(uniforms.time * 0.03, -uniforms.time * 0.018);
            let smoke = fbm(noise_pos);
            let gold_color = vec3<f32>(0.78, 0.64, 0.35); // #c8a45a gold
            let nebula_color = gold_color * smoke * 0.07;

            let final_color = vec3<f32>(grid_val + orbit_val) * vec3<f32>(0.5, 0.5, 0.5) + nebula_color;
            return vec4<f32>(final_color, 1.0);
          }
        `;

        const shaderModule = device.createShaderModule({ code: shaderCode });

        // Create uniform buffer
        uniformBuffer = device.createBuffer({
          size: 32, // 8 floats * 4 bytes
          usage: 64 | 8 // GPUBufferUsage.UNIFORM | GPUBufferUsage.COPY_DST
        });

        // Create bind group layout and bind group
        const bindGroupLayout = device.createBindGroupLayout({
          entries: [{
            binding: 0,
            visibility: 2, // GPUShaderStage.FRAGMENT
            buffer: {}
          }]
        });

        uniformBindGroup = device.createBindGroup({
          layout: bindGroupLayout,
          entries: [{
            binding: 0,
            resource: { buffer: uniformBuffer }
          }]
        });

        pipeline = device.createRenderPipeline({
          layout: device.createPipelineLayout({ bindGroupLayouts: [bindGroupLayout] }),
          vertex: {
            module: shaderModule,
            entryPoint: 'vs_main'
          },
          fragment: {
            module: shaderModule,
            entryPoint: 'fs_main',
            targets: [{ format }]
          }
        });

        setWebGpuActive(true);

        // Render loop
        let dpr = window.devicePixelRatio || 1;
        let lastTime = performance.now();
        let accumTime = 0;

        function resize() {
          if (!canvas) return;
          dpr = window.devicePixelRatio || 1;
          const w = window.innerWidth;
          const h = window.innerHeight;
          canvas.width = w * dpr;
          canvas.height = h * dpr;
          canvas.style.width = `${w}px`;
          canvas.style.height = `${h}px`;
        }

        window.addEventListener('resize', resize);
        resize();

        function render(now: number) {
          if (!active) return;
          animId = requestAnimationFrame(render);

          const elapsed = (now - lastTime) / 1000;
          lastTime = now;
          accumTime += elapsed;

          const w = window.innerWidth;
          const h = window.innerHeight;
          const dprVal = window.devicePixelRatio || 1;

          // Fill uniforms: time, width, height, mouseX, mouseY, mouseActive, pad1, pad2
          const uniformData = new Float32Array([
            accumTime,
            w * dprVal,
            h * dprVal,
            pointer.x * dprVal,
            pointer.y * dprVal,
            pointer.active ? 1.0 : 0.0,
            0.0,
            0.0
          ]);

          device.queue.writeBuffer(uniformBuffer, 0, uniformData.buffer);

          const commandEncoder = device.createCommandEncoder();
          const textureView = context.getCurrentTexture().createView();

          const renderPass = commandEncoder.beginRenderPass({
            colorAttachments: [{
              view: textureView,
              clearValue: { r: 0, g: 0, b: 0, a: 1 },
              loadOp: 'clear',
              storeOp: 'store'
            }]
          });

          renderPass.setPipeline(pipeline);
          renderPass.setBindGroup(0, uniformBindGroup);
          renderPass.draw(3); // Render full-screen quad
          renderPass.end();

          device.queue.submit([commandEncoder.finish()]);
        }

        animId = requestAnimationFrame(render);
      } catch (err) {
        console.warn("Error setting up WebGPU context:", err);
      }
    }

    initGPU();

    return () => {
      active = false;
      cancelAnimationFrame(animId);
    };
  }, []);

  // Standard 2D Canvas rendering loop (falls back or acts as text/label overlay)
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animId: number;
    let dpr = window.devicePixelRatio || 1;
    let cssWidth = window.innerWidth;
    let cssHeight = window.innerHeight;

    function resizeCanvas() {
      if (canvas) {
        dpr = window.devicePixelRatio || 1;
        cssWidth = window.innerWidth;
        cssHeight = window.innerHeight;
        canvas.width = cssWidth * dpr;
        canvas.height = cssHeight * dpr;
        canvas.style.width = `${cssWidth}px`;
        canvas.style.height = `${cssHeight}px`;
      }
    }

    const onPointerMove = (e: PointerEvent) => {
      pointer.x = e.clientX;
      pointer.y = e.clientY;
      pointer.active = true;
    };

    const onPointerLeave = () => {
      pointer.x = -2000;
      pointer.y = -2000;
      pointer.active = false;
    };

    window.addEventListener('resize', resizeCanvas);
    window.addEventListener('pointermove', onPointerMove);
    window.addEventListener('pointerleave', onPointerLeave);
    resizeCanvas();

    let lastUpdate = performance.now();
    const fpsInterval = 1000 / 30; // Throttle background canvas to 30 FPS

    function renderStars(timestamp: number) {
      animId = requestAnimationFrame(renderStars);

      const elapsed = timestamp - lastUpdate;
      if (elapsed < fpsInterval) return;
      lastUpdate = timestamp - (elapsed % fpsInterval);

      if (!canvas || !ctx) return;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, cssWidth, cssHeight);
      time += (elapsed / 1000) * 0.027; // Frame-rate independent drift update

      const cx = cssWidth / 2;
      const cy = cssHeight / 2;
      const px = pointer.x;
      const py = pointer.y;
      const hasPointer = pointer.active && px > 0 && py > 0;

      const applyInterference = (x: number, y: number, maxDist = 130, pullAmt = 7) => {
        if (!hasPointer) return { dx: 0, dy: 0 };
        const dxCoord = x - px;
        const dyCoord = y - py;
        const dist = Math.hypot(dxCoord, dyCoord);
        if (dist < maxDist) {
          const force = (maxDist - dist) / maxDist;
          const angle = Math.atan2(dyCoord, dxCoord);
          return {
            dx: Math.cos(angle) * force * pullAmt,
            dy: Math.sin(angle) * force * pullAmt
          };
        }
        return { dx: 0, dy: 0 };
      };

      // Background Grid - Draw only if WebGPU is not rendering it
      if (!webGpuActive) {
        ctx.lineWidth = 0.5;
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.012)';
        const gridSize = 60;
        for (let x = 0; x < cssWidth; x += gridSize) {
          ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, cssHeight); ctx.stroke();
        }
        for (let y = 0; y < cssHeight; y += gridSize) {
          ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(cssWidth, y); ctx.stroke();
        }
      }

      // Orbits - Draw only if WebGPU is not active (WebGPU draws orbits too!)
      const orbits = [110, 190, 275, 360, 440];
      if (!webGpuActive) {
        orbits.forEach((r, idx) => {
          ctx.beginPath();
          if (idx % 2 === 1) ctx.setLineDash([3, 7]);
          else ctx.setLineDash([]);
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.035)';
          ctx.arc(cx, cy, r, 0, Math.PI * 2);
          ctx.stroke();
          ctx.setLineDash([]);
        });
      }

      // Astrolabe pyramid projected cone (lower left maps)
      const gcx = 190;
      const gcy = cssHeight - 180;
      if (gcy > 300) {
        const gr = 70;
        const gWarp = applyInterference(gcx, gcy, 120, 6);
        const gx = gcx + gWarp.dx;
        const gy = gcy + gWarp.dy;

        // Draw astrolabe graphics only if WebGPU didn't render it
        if (!webGpuActive) {
          ctx.beginPath();
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
          ctx.arc(gx, gy, gr, 0, Math.PI * 2);
          ctx.stroke();

          ctx.beginPath();
          ctx.ellipse(gx, gy, gr, gr * 0.45, 0, 0, Math.PI * 2);
          ctx.ellipse(gx, gy, gr, gr * 0.18, 0, 0, Math.PI * 2);
          ctx.ellipse(gx, gy, gr * 0.6, gr, 0, 0, Math.PI * 2);
          ctx.ellipse(gx, gy, gr * 0.25, gr, 0, 0, Math.PI * 2);
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.02)';
          ctx.stroke();

          ctx.beginPath();
          ctx.moveTo(gx - gr - 15, gy); ctx.lineTo(gx + gr + 15, gy);
          ctx.moveTo(gx, gy - gr - 15); ctx.lineTo(gx, gy + gr + 15);
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.035)';
          ctx.stroke();
        }

        ctx.fillStyle = 'rgba(255, 255, 255, 0.15)';
        ctx.font = '6px "JetBrains Mono", monospace';
        ctx.textAlign = 'center';
        ctx.fillText('SOL_COORD_GRID [V4]', gx, gy + gr + 30);
      }

      // Sigils Matrix (lower right) - Draw pre-rendered canvas in single draw call
      const cellSize = 30;
      const gStartX = cssWidth - 180 - 50;
      const gStartY = cssHeight - 150 - 110;
      if (gStartY > 250 && gStartX > cx + 100) {
        const sCanvas = getSigilsCanvas();
        if (sCanvas) {
          ctx.drawImage(sCanvas, gStartX, gStartY);
        }
      }

      // Planetary coordinates mapping
      const currentPlanets = planetsRef.current || planets;
      const currentActivePlanets = activePlanetsRef.current || activePlanets;

      currentPlanets.forEach((p, idx) => {
        const isActive = currentActivePlanets.has(p.name);
        const slowDrift = p.deg + time * 8;
        const rad = ((slowDrift - 90) * Math.PI) / 180;
        const currentRadius = orbits[idx % orbits.length] || 275;
        
        const rx = cx + currentRadius * Math.cos(rad);
        const ry = cy + currentRadius * Math.sin(rad);
        const inf = applyInterference(rx, ry, 130, 8);
        const fx = rx + inf.dx;
        const fy = ry + inf.dy;

        const alpha = isActive ? 0.9 : 0.08;
        const size = isActive ? 5.5 : 2.5;

        // Radial orbit coordinates
        ctx.beginPath();
        ctx.setLineDash([2, 5]);
        ctx.strokeStyle = `rgba(${hexToRgb(p.color)}, ${alpha * 0.35})`;
        ctx.moveTo(cx, cy); ctx.lineTo(fx, fy);
        ctx.stroke();
        ctx.setLineDash([]);

        // Planet nodes
        ctx.beginPath();
        ctx.arc(fx, fy, size, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(${hexToRgb(p.color)}, ${alpha * 0.8})`;
        ctx.fillStyle = isActive ? `rgba(${hexToRgb(p.color)}, 0.15)` : 'rgba(0,0,0,0.4)';
        ctx.fill(); ctx.stroke();

        if (isActive) {
          ctx.beginPath();
          ctx.arc(fx, fy, 1.5, 0, Math.PI * 2);
          ctx.fillStyle = p.color;
          ctx.fill();

          ctx.font = '12px "Cormorant Garamond", serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillStyle = p.color;
          ctx.fillText(p.symbol, fx, fy - 15);

          ctx.font = '6px "JetBrains Mono", monospace';
          ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
          ctx.fillText(`${p.name.toUpperCase()} [${p.deg.toFixed(1)}°]`, fx, fy + 14);
        }
      });
    }
    renderStars(performance.now());

    return () => {
      window.removeEventListener('resize', resizeCanvas);
      window.removeEventListener('pointermove', onPointerMove);
      window.removeEventListener('pointerleave', onPointerLeave);
      cancelAnimationFrame(animId);
    };
  }, [webGpuActive]);

  if (webGpuActive) {
    return (
      <div style={{ position: 'fixed', inset: 0, zIndex: 0, overflow: 'hidden', width: '100%', height: '100%', pointerEvents: 'none' }}>
        <canvas ref={canvasGPURef} style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', display: 'block' }} />
        <canvas id="starsCanvas" ref={canvasRef} style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', display: 'block', zIndex: 1 }} />
      </div>
    );
  }

  return <canvas id="starsCanvas" ref={canvasRef} />;
}

// --- AsciiEyes Module-Level State ---
const mouse = { x: 0, y: 0, tx: 0, ty: 0 };
const blink = { state: 'open', timer: 0, progress: 1 };
const stateObj = {
  action: 'mouse', // 'mouse' | 'track-element'
  targetId: '',
  crazyUntil: 0,
  trackingUntil: 0,
};

let blinkTimer = Math.random() * 2000 + 3000;

export function AsciiEyes() {
  const preRef = useRef<HTMLPreElement>(null);

  useEffect(() => {
    // Initialize mouse coordinates based on actual window size
    mouse.x = window.innerWidth / 2;
    mouse.y = window.innerHeight / 2;
    mouse.tx = window.innerWidth / 2;
    mouse.ty = window.innerHeight / 2;

    const onMouseMove = (e: MouseEvent) => {
      mouse.tx = e.clientX;
      mouse.ty = e.clientY;
    };

    const onCustomControl = (e: any) => {
      const detail = e.detail || {};
      const now = performance.now();
      
      if (detail.action === 'crazy') {
        stateObj.crazyUntil = now + (detail.duration || 4000);
        blink.state = 'closing';
        blink.progress = 0;
        blink.timer = 0;
      } else if (detail.action === 'track-element') {
        stateObj.action = 'track-element';
        stateObj.targetId = detail.targetId;
        stateObj.trackingUntil = now + (detail.duration || 99999);
      } else if (detail.action === 'reset') {
        stateObj.action = 'mouse';
        stateObj.targetId = '';
        stateObj.trackingUntil = 0;
      }
    };

    window.addEventListener('mousemove', onMouseMove);
    window.addEventListener('ascii-eyes-control-custom', onCustomControl);

    let animId: number;
    const COLS = 104;
    const ROWS = 24;
    const CX_L = 30;
    const CX_R = 74;
    const CY = 12;
    const EYE_W = 22;
    const HEIGHT_MAX = 5.2;

    let lastUpdate = performance.now();
    const fpsInterval = 1000 / 30; // Throttle preformatted text recalculation to 30 FPS

    function runEyes(timestamp: number) {
      animId = requestAnimationFrame(runEyes);

      const elapsed = timestamp - lastUpdate;
      if (elapsed < fpsInterval) return;
      lastUpdate = timestamp - (elapsed % fpsInterval);

      const isCrazy = performance.now() < stateObj.crazyUntil;
      const preEyes = preRef.current;
      if (!preEyes) return;
      
      let targetX = mouse.tx;
      let targetY = mouse.ty;

      if (stateObj.action === 'track-element' && stateObj.targetId) {
        const el = document.getElementById(stateObj.targetId);
        if (el) {
          const rect = el.getBoundingClientRect();
          targetX = rect.left + rect.width / 2;
          targetY = rect.top + rect.height / 2;
        } else {
          stateObj.action = 'mouse';
        }
      }

      // Smooth pupillary easing (frame-rate independent scaling)
      const speedScale = elapsed / 16.67;
      const easeRate = stateObj.action === 'track-element' ? 0.15 : 0.08;
      const scaledEase = 1 - Math.pow(1 - easeRate, speedScale);
      mouse.x += (targetX - mouse.x) * scaledEase;
      mouse.y += (targetY - mouse.y) * scaledEase;

      // Eyelid blinking loops
      blink.timer += elapsed;
      if (isCrazy) {
        blink.progress = 0.35 + 0.65 * Math.sin(timestamp * 0.08) * (Math.random() > 0.5 ? 1 : 0.2);
        blink.state = 'open';
      } else {
        if (blink.state === 'open' && blink.timer > blinkTimer) {
          blink.state = 'closing'; blink.timer = 0;
        } else if (blink.state === 'closing') {
          blink.progress -= 0.18 * speedScale;
          if (blink.progress <= 0) {
            blink.progress = 0; blink.state = 'closed'; blink.timer = 0;
          }
        } else if (blink.state === 'closed') {
          if (blink.timer > 100) { blink.state = 'opening'; blink.timer = 0; }
        } else if (blink.state === 'opening') {
          blink.progress += 0.15 * speedScale;
          if (blink.progress >= 1) {
            blink.progress = 1; blink.state = 'open'; blink.timer = 0;
            blinkTimer = Math.random() * 4000 + 4000;
          }
        }
      }

      // Pupil translations
      const dxViewport = mouse.x - window.innerWidth / 2;
      const dyViewport = mouse.y - window.innerHeight / 2;
      const dist = Math.hypot(dxViewport, dyViewport) || 1;
      const limit = 220;
      const factor = Math.min(dist, limit) / limit;
      const angle = Math.atan2(dyViewport, dxViewport);
      
      let pupilShiftX = Math.cos(angle) * factor * 4.2;
      let pupilShiftY = Math.sin(angle) * factor * 1.8;

      if (isCrazy) {
        pupilShiftX += Math.sin(timestamp * 0.1) * 2.5;
        pupilShiftY += Math.cos(timestamp * 0.12) * 1.3;
      }

      let out = '';
      const hEye = HEIGHT_MAX * blink.progress;
      const IRIS_RINGS_NORMAL = ['◈', '◇', '✦', '·'];
      const IRIS_RINGS_CRAZY = ['⍼', '☠', '☣', '✖', '✥', '╬', '█', '0', '1'];
      const IRIS_RINGS = isCrazy ? IRIS_RINGS_CRAZY : IRIS_RINGS_NORMAL;
      const PUPIL_CHAR = isCrazy ? (Math.random() > 0.5 ? '⛧' : '✖') : '◉';
      const R_PUPIL = isCrazy ? 1.7 : 1.3;
      const R_IRIS = isCrazy ? 4.2 : 3.6;

      for (let r = 0; r < ROWS; r++) {
        let line = '';
        for (let c = 0; c < COLS; c++) {
          const inLeft = Math.abs(c - CX_L) <= EYE_W / 2;
          const inRight = Math.abs(c - CX_R) <= EYE_W / 2;
          
          if (inLeft || inRight) {
            const eyeCenterX = inLeft ? CX_L : CX_R;
            const tx = (c - eyeCenterX) / (EYE_W / 2);
            const lensFactor = Math.cos(tx * Math.PI / 2);
            const boundaryHalfH = hEye * lensFactor;
            const dy = r - CY;
            const isInside = Math.abs(dy) <= boundaryHalfH;

            if (isInside) {
              if (blink.progress < 0.12 && !isCrazy) {
                line += ' - ';
              } else {
                const pCenterX = eyeCenterX + pupilShiftX;
                const pCenterY = CY + pupilShiftY;
                const distToPupil = Math.hypot((c - pCenterX) * 0.75, r - pCenterY);

                if (distToPupil < R_PUPIL) line += PUPIL_CHAR;
                else if (distToPupil < R_IRIS) {
                  const idx = Math.floor((distToPupil - R_PUPIL) * 1.5) % IRIS_RINGS.length;
                  line += IRIS_RINGS[idx];
                } else {
                  const densityVal = (r * 11 + c * 3) % (isCrazy ? 8 : 17);
                  if (densityVal === 0) line += isCrazy ? '✖' : '·';
                  else if (densityVal === 1) line += isCrazy ? '⍼' : '°';
                  else line += ' ';
                }
              }
            } else {
              const distToBoundary = Math.abs(Math.abs(dy) - boundaryHalfH);
              if (distToBoundary < 0.65) {
                line += (dy < 0) ? '⎴' : '⎵';
              } else {
                const cellCheck = (r * 7 + c * 13) % 233;
                if (cellCheck === 4) line += isCrazy ? '☠' : '+';
                else if (cellCheck === 12 && r % 4 === 0) line += '·';
                else line += ' ';
              }
            }
          } else {
            const cellCheck = (r * 7 + c * 13) % 233;
            if (cellCheck === 4 && r % 3 === 0) line += '·';
            else if (cellCheck === 99 && c % 12 === 0) line += isCrazy ? '⍼' : '+';
            else if (isCrazy && cellCheck === 33) line += Math.random() > 0.5 ? '1' : '0';
            else line += ' ';
          }
        }
        out += line + '\n';
      }

      preEyes.innerText = out;
      
      if (isCrazy) {
        const shakeX = (Math.random() - 0.5) * 18;
        const shakeY = (Math.random() - 0.5) * 18;
        preEyes.style.transform = `translate3d(${shakeX}px, ${shakeY}px, 0)`;
        preEyes.style.color = '#ffffff';
        preEyes.style.textShadow = '0 0 12px rgba(255, 255, 255, 0.9)';
      } else {
        preEyes.style.transform = 'none';
        preEyes.style.color = 'rgba(255, 255, 255, 0.2)';
        preEyes.style.textShadow = '0 0 4px rgba(255, 255, 255, 0.4)';
      }
    }
    animId = requestAnimationFrame(runEyes);

    return () => {
      window.removeEventListener('mousemove', onMouseMove);
      window.removeEventListener('ascii-eyes-control-custom', onCustomControl);
      cancelAnimationFrame(animId);
    };
  }, []);

  return <pre id="asciiEyes" ref={preRef}></pre>;
}

export function CompactEye() {
  const preRef = useRef<HTMLPreElement>(null);

  useEffect(() => {
    const compactFrames = [
      `     .--------.     \n    /  (  ●  )  \\   \n    \\           /   \n     '--------'     `,
      `     .--------.     \n    /  (●   )   \\   \n    \\           /   \n     '--------'     `,
      `     .--------.     \n    /   (   ●)  \\   \n    \\           /   \n     '--------'     `,
      `     .--------.     \n    /  ( ◉ ◉ )  \\   \n    \\           /   \n     '--------'     `,
      `     .--------.     \n    /   - - -   \\   \n    \\           /   \n     '--------'     `,
      `     .--------.     \n    =============   \n     '--------'     `
    ];
    let compFrame = 0;
    const interval = setInterval(() => {
      const r = Math.random();
      if (r < 0.4) compFrame = 0;
      else if (r < 0.6) compFrame = 1;
      else if (r < 0.75) compFrame = 2;
      else if (r < 0.85) compFrame = 3;
      else if (r < 0.92) compFrame = 4;
      else {
        compFrame = 5;
        setTimeout(() => { 
          if (preRef.current) preRef.current.innerText = compactFrames[0] + '\n// OS_GATE_ONLINE //'; 
        }, 100);
      }
      if (preRef.current) {
        preRef.current.innerText = compactFrames[compFrame] + '\n// OS_GATE_ONLINE //';
      }
    }, 900);

    return () => clearInterval(interval);
  }, []);

  return <pre id="compactEyeFrame" ref={preRef}>// LOADING GATE //</pre>;
}
