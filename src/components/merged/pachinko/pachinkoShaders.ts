export const circleShaderWGSL = `
struct CameraUniform {
  viewProj: mat3x3<f32>,
};
@group(0) @binding(0) var<uniform> camera: CameraUniform;

struct InstanceInput {
  @location(0) position: vec2<f32>,
  @location(1) radius: f32,
  @location(2) color: vec4<f32>,
  @location(3) outlineColor: vec4<f32>,
  @location(4) glowAmt: f32,
  @location(5) fillType: f32, // 0 = solid, 1 = planet
};

struct VertexOutput {
  @builtin(position) position: vec4<f32>,
  @location(0) color: vec4<f32>,
  @location(1) outlineColor: vec4<f32>,
  @location(2) localPos: vec2<f32>, // -1 to 1 for drawing circles in frag
  @location(3) glowAmt: f32,
  @location(4) fillType: f32,
};

// Quad vertices centered at 0,0, range -1 to 1
var<private> pos: array<vec2<f32>, 6> = array<vec2<f32>, 6>(
  vec2<f32>(-1.0, -1.0),
  vec2<f32>( 1.0, -1.0),
  vec2<f32>( 1.0,  1.0),
  vec2<f32>(-1.0, -1.0),
  vec2<f32>( 1.0,  1.0),
  vec2<f32>(-1.0,  1.0)
);

@vertex
fn vs_main(
  @builtin(vertex_index) vertexIndex: u32,
  instance: InstanceInput
) -> VertexOutput {
  var out: VertexOutput;
  let local_p = pos[vertexIndex];
  
  // Expand bounds to allow glow rendering outside the strict radius
  let scale = instance.radius + max(instance.glowAmt * 4.0, 2.0);
  
  let worldPos = instance.position + local_p * scale;
  let transformedPos = camera.viewProj * vec3<f32>(worldPos, 1.0);
  
  out.position = vec4<f32>(transformedPos.xy, 0.0, 1.0);
  out.color = instance.color;
  out.outlineColor = instance.outlineColor;
  out.localPos = local_p * (scale / instance.radius); // Normalizing to radius = 1.0
  out.glowAmt = instance.glowAmt;
  out.fillType = instance.fillType;
  return out;
}

@fragment
fn fs_main(in: VertexOutput) -> @location(0) vec4<f32> {
  let dist = length(in.localPos);
  
  // Base circle boundary
  let smoothEdge = 1.0 - smoothstep(0.95, 1.0, dist);
  
  var outColor: vec4<f32> = vec4<f32>(0.0);
  
  if (in.fillType == 0.0) {
    // Basic solid / glowing circle
    let fill = in.color * smoothEdge;
    
    // Add glow outside
    var glow = 0.0;
    if (in.glowAmt > 0.0 && dist > 1.0) {
      glow = exp(-(dist - 1.0) * (5.0 / in.glowAmt)) * in.glowAmt * 0.5;
    }
    
    outColor = fill + vec4<f32>(in.outlineColor.rgb, in.outlineColor.a * glow);
    if (dist <= 1.0 && in.outlineColor.a > 0.0) {
       // Outline
       let outline = smoothstep(0.85, 0.95, dist) * smoothEdge;
       outColor = mix(outColor, in.outlineColor, outline);
    }
  } else if (in.fillType == 1.0) {
    // Planet type
    outColor = in.color * smoothEdge;
    let outline = smoothstep(0.85, 0.95, dist) * smoothEdge;
    outColor = mix(outColor, in.outlineColor, outline);
    
    // Planet Glow
    if (in.glowAmt > 0.0 && dist > 1.0) {
      let g = exp(-(dist - 1.0) * 3.0) * in.glowAmt * 0.8;
      outColor = outColor + vec4<f32>(in.outlineColor.rgb, g);
    }
  }
  
  return outColor;
}
`;

export const lineShaderWGSL = `
struct CameraUniform {
  viewProj: mat3x3<f32>,
};
@group(0) @binding(0) var<uniform> camera: CameraUniform;

struct VertexInput {
  @location(0) position: vec2<f32>,
  @location(1) color: vec4<f32>,
};

struct VertexOutput {
  @builtin(position) position: vec4<f32>,
  @location(0) color: vec4<f32>,
};

@vertex
fn vs_main(in: VertexInput) -> VertexOutput {
  var out: VertexOutput;
  let transformedPos = camera.viewProj * vec3<f32>(in.position, 1.0);
  out.position = vec4<f32>(transformedPos.xy, 0.0, 1.0);
  out.color = in.color;
  return out;
}

@fragment
fn fs_main(in: VertexOutput) -> @location(0) vec4<f32> {
  return in.color;
}
`;
