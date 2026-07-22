import { circleShaderWGSL, lineShaderWGSL } from "./pachinkoShaders";

export class PachinkoWebGPURenderer {
  device!: GPUDevice;
  context!: GPUCanvasContext;
  format!: GPUTextureFormat;

  circlePipeline!: GPURenderPipeline;
  linePipeline!: GPURenderPipeline;

  circleInstanceBuffer!: GPUBuffer;
  cameraBuffer!: GPUBuffer;
  cameraBindGroup!: GPUBindGroup;

  maxInstances = 5000;
  // Reused every frame instead of allocating a new Float32Array per render() call.
  private instanceScratch = new Float32Array(this.maxInstances * 13);
  
  async init(canvas: HTMLCanvasElement) {
    if (!navigator.gpu) {
      throw new Error("WebGPU not supported on this browser.");
    }
    const adapter = await navigator.gpu.requestAdapter({
      powerPreference: 'high-performance'
    });
    if (!adapter) {
      throw new Error("No appropriate GPUAdapter found.");
    }
    this.device = await adapter.requestDevice();
    this.context = canvas.getContext("webgpu") as GPUCanvasContext;
    this.format = navigator.gpu.getPreferredCanvasFormat();
    
    this.context.configure({
      device: this.device,
      format: this.format,
      alphaMode: 'premultiplied'
    });

    // Camera buffer
    this.cameraBuffer = this.device.createBuffer({
      size: 48, // mat3x3 takes 12 floats (padded)
      usage: GPUBufferUsage.UNIFORM | GPUBufferUsage.COPY_DST,
    });

    const circleShader = this.device.createShaderModule({ code: circleShaderWGSL });
    const lineShader = this.device.createShaderModule({ code: lineShaderWGSL });

    // Buffers
    const instanceByteSize = 2 + 1 + 4 + 4 + 1 + 1; // position, radius, color, outlineColor, glowAmt, fillType = 13 floats
    this.circleInstanceBuffer = this.device.createBuffer({
      size: this.maxInstances * 13 * 4,
      usage: GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST,
    });

    // Pipelines
    const bindGroupLayout = this.device.createBindGroupLayout({
      entries: [{ binding: 0, visibility: GPUShaderStage.VERTEX, buffer: { type: 'uniform' } }]
    });

    this.cameraBindGroup = this.device.createBindGroup({
      layout: bindGroupLayout,
      entries: [{ binding: 0, resource: { buffer: this.cameraBuffer } }]
    });

    const pipelineLayout = this.device.createPipelineLayout({ bindGroupLayouts: [bindGroupLayout] });

    this.circlePipeline = this.device.createRenderPipeline({
      layout: pipelineLayout,
      vertex: {
        module: circleShader,
        entryPoint: "vs_main",
        buffers: [{
          arrayStride: 13 * 4,
          stepMode: 'instance',
          attributes: [
            { shaderLocation: 0, offset: 0, format: 'float32x2' },
            { shaderLocation: 1, offset: 8, format: 'float32' },
            { shaderLocation: 2, offset: 12, format: 'float32x4' },
            { shaderLocation: 3, offset: 28, format: 'float32x4' },
            { shaderLocation: 4, offset: 44, format: 'float32' },
            { shaderLocation: 5, offset: 48, format: 'float32' },
          ]
        }]
      },
      fragment: {
        module: circleShader,
        entryPoint: "fs_main",
        targets: [{
          format: this.format,
          blend: {
            color: { srcFactor: 'src-alpha', dstFactor: 'one-minus-src-alpha', operation: 'add' },
            alpha: { srcFactor: 'one', dstFactor: 'one-minus-src-alpha', operation: 'add' }
          }
        }]
      },
      primitive: { topology: 'triangle-list' }
    });
  }

  updateCamera(width: number, height: number) {
    if (!this.device) return;
    // Orthographic projection matrix for WebGPU
    // WebGPU NDC: x: -1 to 1, y: -1 to 1, origin at center.
    const projectionMatrix = new Float32Array([
      2 / width, 0, 0, 0,
      0, -2 / height, 0, 0,
      -1, 1, 1, 0 // translation to make top-left (0,0)
    ]);
    this.device.queue.writeBuffer(this.cameraBuffer, 0, projectionMatrix);
  }

  // hex to rgb float array [r,g,b,a]  -  cached since pegs/planets/particles reuse the same few hex strings every frame
  private colorCache = new Map<string, number[]>();
  hexToColor(hex: string, alpha = 1.0) {
    const cacheKey = hex + '|' + alpha;
    const cached = this.colorCache.get(cacheKey);
    if (cached) return cached;

    let h = hex.startsWith('#') ? hex.slice(1) : hex;
    if (h.length === 3) h = h.split('').map(c => c + c).join('');
    const r = parseInt(h.slice(0, 2), 16) / 255;
    const g = parseInt(h.slice(2, 4), 16) / 255;
    const b = parseInt(h.slice(4, 6), 16) / 255;
    let a = alpha;
    if (h.length === 8) a = parseInt(h.slice(6, 8), 16) / 255;

    const result = [r, g, b, a];
    this.colorCache.set(cacheKey, result);
    return result;
  }

  render(params: any) {
    if (!this.device || !this.context) return;
    
    // Parse params (pegs, balls, particles, planets) and build instance array
    const instances = this.instanceScratch;
    let count = 0;

    const addCircle = (x: number, y: number, r: number, color: number[], outlineColor: number[], glowAmt: number, fillType: number) => {
      if (count >= this.maxInstances) return;
      const offset = count * 13;
      instances[offset] = x;
      instances[offset + 1] = y;
      instances[offset + 2] = r;
      instances.set(color, offset + 3);
      instances.set(outlineColor, offset + 7);
      instances[offset + 11] = glowAmt;
      instances[offset + 12] = fillType;
      count++;
    };

    // Particles
    for (const p of params.particles) {
      addCircle(p.x, p.y, p.size, this.hexToColor(p.color, p.life / 45), [0,0,0,0], 0, 0);
    }

    // Pegs
    for (const peg of params.pegs) {
      const isGlowing = peg.hit > 0.04;
      const c = isGlowing ? [1,1,1,1] : [1,1,1,0.4];
      addCircle(peg.x, peg.y, isGlowing ? peg.r + peg.hit * 1.6 : peg.r, c, [0,0,0,0], peg.hit * 2, 0);
    }

    // Dividers
    for (const div of params.dividers) {
      const isGlowing = div.hit > 0.04;
      const c = isGlowing ? [1,1,1,1] : [1,1,1,0.5];
      addCircle(div.x, div.y, isGlowing ? div.r + div.hit * 1.2 : div.r, c, [0,0,0,0], div.hit * 1.5, 0);
    }

    // Planets
    for (const p of params.planets) {
       const glow = p.hit || 0;
       const color = this.hexToColor(p.color);
       const r = p.r + Math.sin(p.pulse) * 1.2;
       addCircle(p.x, p.y, r, [color[0], color[1], color[2], 0.05 + glow * 0.2], [color[0], color[1], color[2], 1], glow, 1);
       // Add orbit ring
       addCircle(p.x, p.y, r + 11, [0,0,0,0], [color[0], color[1], color[2], 0.12 + glow * 0.4], 0, 0);
    }
    
    // Balls
    for (const b of params.balls) {
      for (let t = 0; t < b.trail.length; t++) {
         const tp = b.trail[t];
         const alpha = ((t + 1) / b.trail.length) * 0.16;
         addCircle(tp.x, tp.y, b.r * 0.72, [1,1,1,alpha], [0,0,0,0], 0, 0);
      }
      addCircle(b.x, b.y, b.r, [1,1,1,1], [1,1,1,0.4], 1.5, 0);
    }

    this.device.queue.writeBuffer(this.circleInstanceBuffer, 0, instances.buffer, 0, count * 13 * 4);

    const commandEncoder = this.device.createCommandEncoder();
    const textureView = this.context.getCurrentTexture().createView();
    const renderPassDescriptor: GPURenderPassDescriptor = {
      colorAttachments: [{
        view: textureView,
        clearValue: { r: 0.0, g: 0.0, b: 0.0, a: 0.0 }, // Fully transparent
        loadOp: 'clear',
        storeOp: 'store',
      }]
    };

    const passEncoder = commandEncoder.beginRenderPass(renderPassDescriptor);
    passEncoder.setPipeline(this.circlePipeline);
    passEncoder.setBindGroup(0, this.cameraBindGroup);
    passEncoder.setVertexBuffer(0, this.circleInstanceBuffer);
    passEncoder.draw(6, count, 0, 0);
    passEncoder.end();

    this.device.queue.submit([commandEncoder.finish()]);
  }
}
