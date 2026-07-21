import React, { useEffect, useRef } from "react";
import pachinkoBgSkeleton from "../../pachinko_bg_skeleton.webp";
import pachinkoHands from "../../pachinko_hands.webp";

interface LunarotPachinkoProps {
  onBallLand: (binIndex: number) => void;
  onPlanetHit: (planetName: string) => void;
  onPachinkoTelemetry: (msg: string) => void;
  beadsCount: number;
  onBeadLaunched: () => void;
  isLocked: boolean;
  onScoreUpdate?: (points: number) => void;
  hasCards?: boolean;
  eyeMode?: 'normal' | 'buff' | 'curse';
}

interface Ball {
  x: number;
  y: number;
  vx: number;
  vy: number;
  r: number;
  hits: number;
  settled: boolean;
}

interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  color: string;
  size: number;
  alpha: number;
  life: number;
}

interface Peg {
  x: number;
  y: number;
  r: number;
  hit: number;
}

interface PlanetNode {
  name: string;
  symbol: string;
  color: string;
  x: number;
  y: number;
  r: number;
  hit: number;
  pulse: number;
  gravityStrength: number;
}

// Convert Hex to RGB for canvas opacity rendering
function hexToRgb(hex: string): string {
  if (hex.startsWith("#")) hex = hex.slice(1);
  if (hex.length === 3) {
    hex = hex.split("").map((c) => c + c).join("");
  }
  const r = parseInt(hex.slice(0, 2), 16) || 200;
  const g = parseInt(hex.slice(2, 4), 16) || 164;
  const b = parseInt(hex.slice(4, 6), 16) || 90;
  return `${r}, ${g}, ${b}`;
}

// Audio feedback helper
let audioCtx: AudioContext | null = null;
function playPegSound(pitch: number, type: "sine" | "triangle" = "triangle", volume = 0.05) {
  try {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || (window as any).webkitAudioContext)();
    }
    if (audioCtx.state === "suspended") {
      audioCtx.resume();
    }
    const osc = audioCtx.createOscillator();
    const gainNode = audioCtx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(pitch, audioCtx.currentTime);
    gainNode.gain.setValueAtTime(volume, audioCtx.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.15);
    osc.connect(gainNode);
    gainNode.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.17);
  } catch (err) {}
}

const FW = 14;
const FH = 24;

const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
const clamp = (v: number, a: number, b: number) => Math.max(a, Math.min(b, v));

function buildPalette(mode: "curse" | "buff" | "normal") {
  const stops = [];
  for (let i = 0; i < 40; i++) {
    const t = i / 39;
    let h, s, l;
    if (mode === "curse") { h = lerp(300, 350, t); s = 90; l = lerp(4, 78, Math.pow(t, 0.8)); }
    else if (mode === "buff") { h = lerp(190, 150, t); s = 85; l = lerp(4, 88, Math.pow(t, 0.8)); }
    else { h = lerp(8, 50, t); s = 95; l = lerp(4, 85, Math.pow(t, 0.75)); }
    stops.push(i === 0 ? "rgba(0,0,0,0)" : `hsl(${h},${s}%,${l}%)`);
  }
  return stops;
}

const PALETTES = {
  normal: buildPalette("normal"),
  buff: buildPalette("buff"),
  curse: buildPalette("curse"),
};

function spreadFire(buf: Uint8Array, W: number, H: number, decayChance: number) {
  for (let x = 0; x < W; x++) {
    for (let y = H - 1; y >= 1; y--) {
      const src = y * W + x;
      const val = buf[src];
      if (val <= 0) { buf[src - W] = 0; continue; }
      const r = Math.random();
      const dx = r < 0.33 ? -1 : r < 0.66 ? 1 : 0;
      const dstX = clamp(x + dx, 0, W - 1);
      let decay = 0;
      if (Math.random() < decayChance) decay += 1;
      if (Math.random() < decayChance * 0.6) decay += 1;
      buf[(y - 1) * W + dstX] = Math.max(0, val - decay);
    }
  }
}

export default function LunarotPachinko({
  onBallLand,
  onPlanetHit,
  onPachinkoTelemetry,
  beadsCount,
  onBeadLaunched,
  isLocked,
  onScoreUpdate,
  hasCards = false,
  eyeMode = "normal",
}: LunarotPachinkoProps) {
  const rootRef = useRef<HTMLDivElement | null>(null);
  const boardCanvasRef = useRef<HTMLCanvasElement | null>(null);
  const fireLeftCanvasRef = useRef<HTMLCanvasElement | null>(null);
  const fireRightCanvasRef = useRef<HTMLCanvasElement | null>(null);
  const leftHandRef = useRef<HTMLDivElement | null>(null);
  const rightHandRef = useRef<HTMLDivElement | null>(null);

  const DESIGN_W = 480;
  const DESIGN_H = 680;
  const WALL = 14;
  const playTop = 26;
  const playLeft = WALL;
  const playRight = DESIGN_W - WALL;
  const playBottom = DESIGN_H - 84;

  const gates = [
    { label: "VOID", color: "#5b6472" },
    { label: "CUPS", color: "#38bdf8" },
    { label: "WANDS", color: "#ef4444" },
    { label: "COSMOS", color: "#e3b341" },
    { label: "EARTH", color: "#10b981" },
    { label: "AIR", color: "#a78bfa" },
    { label: "VOID", color: "#5b6472" },
  ];

  // Game references
  const ballsRef = useRef<Ball[]>([]);
  const pegsRef = useRef<Peg[]>([]);
  const particlesRef = useRef<Particle[]>([]);
  const planetsRef = useRef<PlanetNode[]>([]);
  
  // Fire overlays
  const fireBufL = useRef(new Uint8Array(FW * FH));
  const fireBufR = useRef(new Uint8Array(FW * FH));
  const flareBoost = useRef(0);
  const time = useRef(0);
  const handState = useRef({ recoilY: 0 });

  useEffect(() => {
    // 1. Setup planets inside DESIGN_H=680 cabinet coordinates
    const planetsList: PlanetNode[] = [
      { name: "Mars", symbol: "♂", color: "#ef4444", x: playLeft + 90, y: playTop + 110, r: 18, hit: 0, pulse: 0, gravityStrength: 4.8 },
      { name: "Mercury", symbol: "☿", color: "#10b981", x: playRight - 90, y: playTop + 110, r: 16, hit: 0, pulse: Math.PI / 4, gravityStrength: 4.0 },
      { name: "Sun", symbol: "☉", color: "#e3b341", x: DESIGN_W / 2, y: playTop + 195, r: 23, hit: 0, pulse: Math.PI / 2, gravityStrength: 6.2 },
      { name: "Moon", symbol: "☽", color: "#38bdf8", x: DESIGN_W / 2 - 110, y: playTop + 295, r: 18, hit: 0, pulse: Math.PI, gravityStrength: 5.2 },
      { name: "Saturn", symbol: "♄", color: "#f59e0b", x: DESIGN_W / 2 + 110, y: playTop + 295, r: 21, hit: 0, pulse: Math.PI * 1.5, gravityStrength: 5.5 },
      { name: "Prism-L", symbol: "✧", color: "#d946ef", x: playLeft + 45, y: playTop + 215, r: 14, hit: 0, pulse: 0, gravityStrength: 2.0 },
      { name: "Prism-R", symbol: "✧", color: "#0ea5e9", x: playRight - 45, y: playTop + 215, r: 14, hit: 0, pulse: Math.PI, gravityStrength: 2.0 },
    ];
    planetsRef.current = planetsList;

    // 2. Setup pegs grid bypassing planetary centers
    const rows = 10;
    const rowGap = (playBottom - playTop - 60) / rows;
    const pegsList: Peg[] = [];
    const PEG_R = 3.6;

    for (let r = 0; r < rows; r++) {
      const y = playTop + 30 + r * rowGap;
      const cols = r % 2 === 0 ? 8 : 7;
      const usableW = playRight - playLeft - 16;
      const spacing = usableW / (cols - 1 + (r % 2 === 0 ? 0 : 1));
      const offset = r % 2 === 0 ? 8 : 8 + spacing / 2;
      for (let c = 0; c < cols; c++) {
        const x = playLeft + offset + c * spacing;
        if (x < playLeft + 6 || x > playRight - 6) continue;

        const sitsInPlanet = planetsList.some(
          (p) => Math.sqrt((x - p.x) * (x - p.x) + (y - p.y) * (y - p.y)) < p.r + 14
        );
        if (!sitsInPlanet) {
          pegsList.push({ x, y, r: PEG_R, hit: 0 });
        }
      }
    }
    pegsRef.current = pegsList;

    resize();
    const handleResize = () => resize();
    window.addEventListener("resize", handleResize);

    const interval = setInterval(() => tick(), 16);

    return () => {
      clearInterval(interval);
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  const scaleFactorRef = useRef(1);

  const resize = () => {
    const canvas = boardCanvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    scaleFactorRef.current = rect.width / DESIGN_W;
    canvas.width = Math.round(rect.width * dpr);
    canvas.height = Math.round(rect.height * dpr);
    const ctx = canvas.getContext("2d");
    if (ctx) {
      ctx.setTransform(dpr * scaleFactorRef.current, 0, 0, dpr * scaleFactorRef.current, 0, 0);
    }
  };

  const spawnParticles = (x: number, y: number, color: string, count: number) => {
    for (let i = 0; i < count; i++) {
      const phi = Math.random() * Math.PI * 2;
      const v = 1 + Math.random() * 2.5;
      particlesRef.current.push({
        x,
        y,
        vx: Math.cos(phi) * v,
        vy: Math.sin(phi) * v - 1.2,
        color,
        size: 1.5 + Math.random() * 2,
        alpha: 1,
        life: 24 + Math.random() * 20,
      });
    }
  };

  const handlePointerDown = (e: React.PointerEvent<HTMLCanvasElement>) => {
    if (isLocked || beadsCount <= 0) return;

    // Safety constraint: max 1 active ball in flight to preserve cards flow
    const activeCount = ballsRef.current.filter((b) => !b.settled).length;
    if (activeCount > 0) return;

    const canvas = boardCanvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const scale = rect.width / DESIGN_W;
    let x = (e.clientX - rect.left) / scale;
    x = clamp(x, playLeft + 6, playRight - 6);

    ballsRef.current.push({
      x,
      y: 16,
      vx: (Math.random() - 0.5) * 0.6,
      vy: 0,
      r: 5.2,
      hits: 0,
      settled: false,
    });

    onBeadLaunched();
    onPachinkoTelemetry("bead released // descending through the lattice");
  };

  const tickPhysics = () => {
    const GRAVITY = 0.52;
    const RESTITUTION = 0.58;
    const FRICTION = 0.993;
    const balls = ballsRef.current;

    for (let i = balls.length - 1; i >= 0; i--) {
      const b = balls[i];
      if (b.settled) {
        balls.splice(i, 1);
        continue;
      }

      // 1. Planets gravity pull calculations
      for (const p of planetsRef.current) {
        const dx = p.x - b.x;
        const dy = p.y - b.y;
        const dist = Math.hypot(dx, dy);
        if (dist < 90 && dist > p.r) {
          const force = (p.gravityStrength / (dist * dist)) * 10;
          b.vx += (dx / dist) * force;
          b.vy += (dy / dist) * force;
        }
      }

      b.vy += GRAVITY;
      b.vx *= FRICTION;
      b.vy *= FRICTION;
      b.x += b.vx;
      b.y += b.vy;

      // 2. Left & right wall bounce
      if (b.x - b.r < playLeft) {
        b.x = playLeft + b.r;
        b.vx = Math.abs(b.vx) * RESTITUTION;
        b.hits++;
        playPegSound(250, "triangle", 0.04);
      }
      if (b.x + b.r > playRight) {
        b.x = playRight - b.r;
        b.vx = -Math.abs(b.vx) * RESTITUTION;
        b.hits++;
        playPegSound(250, "triangle", 0.04);
      }

      // 3. Peg collisions resolving
      for (const peg of pegsRef.current) {
        const dx = b.x - peg.x;
        const dy = b.y - peg.y;
        const minDist = b.r + peg.r;
        const distSq = dx * dx + dy * dy;
        if (distSq < minDist * minDist && distSq > 0.0001) {
          const dist = Math.sqrt(distSq);
          const nx = dx / dist;
          const ny = dy / dist;
          const overlap = minDist - dist;
          b.x += nx * overlap;
          b.y += ny * overlap;
          const dot = b.vx * nx + b.vy * ny;
          b.vx = (b.vx - 2 * dot * nx) * RESTITUTION;
          b.vy = (b.vy - 2 * dot * ny) * RESTITUTION;
          b.vx += (Math.random() - 0.5) * 0.35;
          b.hits++;
          peg.hit = 1;

          const pitch = 220 + (peg.y - playTop) * 1.1;
          playPegSound(pitch, "triangle", 0.045);

          if (b.hits % 3 === 0 && onScoreUpdate) {
            onScoreUpdate(5);
          }
          flareBoost.current = Math.min(1.5, flareBoost.current + 0.08);
        }
      }

      // 4. Planets bump collisions resolving
      for (const p of planetsRef.current) {
        const dx = b.x - p.x;
        const dy = b.y - p.y;
        const minDist = b.r + p.r;
        const distSq = dx * dx + dy * dy;
        if (distSq < minDist * minDist && distSq > 0.0001) {
          const dist = Math.sqrt(distSq);
          const nx = dx / dist;
          const ny = dy / dist;
          const overlap = minDist - dist;
          b.x += nx * overlap;
          b.y += ny * overlap;
          const dot = b.vx * nx + b.vy * ny;
          b.vx = (b.vx - 2 * dot * nx) * RESTITUTION;
          b.vy = (b.vy - 2 * dot * ny) * RESTITUTION;
          b.vx += (Math.random() - 0.5) * 0.35;
          b.hits++;
          p.hit = 1.0;

          onPlanetHit(p.name);
          playPegSound(440 + p.gravityStrength * 40, "sine", 0.08);
          spawnParticles(b.x, b.y, p.color, 12);
          flareBoost.current = Math.min(2.0, flareBoost.current + 0.35);
        }
      }

      // 5. Landing in pockets
      if (b.y > playBottom) {
        b.settled = true;
        const usable = playRight - playLeft;
        const gw = usable / gates.length;
        let idx = Math.floor((b.x - playLeft) / gw);
        idx = clamp(idx, 0, gates.length - 1);
        
        const gate = gates[idx];
        spawnParticles(b.x, playBottom, gate.color, 16);
        onBallLand(idx);
        playPegSound(150, "sine", 0.1);
        flareBoost.current = Math.min(2.5, flareBoost.current + 0.85);
      }
    }

    const particles = particlesRef.current;
    for (let i = particles.length - 1; i >= 0; i--) {
      const p = particles[i];
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.08;
      p.life--;
      p.alpha = Math.max(0, p.life / 40);
      if (p.life <= 0) {
        particles.splice(i, 1);
      }
    }
  };

  const drawBoard = () => {
    const canvas = boardCanvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    ctx.clearRect(0, 0, DESIGN_W, DESIGN_H);

    // Render astronomical planet nodes
    for (const p of planetsRef.current) {
      p.hit *= 0.9;
      p.pulse += 0.04;
      const radiusOffset = Math.sin(p.pulse) * 1.5;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r + p.hit * 4 + radiusOffset, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${hexToRgb(p.color)}, ${0.15 + p.hit * 0.4})`;
      ctx.strokeStyle = p.color;
      ctx.lineWidth = 1 + p.hit * 2;
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = p.color;
      ctx.font = `${p.r * 0.8}px ui-monospace, monospace`;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(p.symbol, p.x, p.y);
    }

    // Render lattice grid pegs
    for (const peg of pegsRef.current) {
      peg.hit *= 0.9;
      ctx.beginPath();
      ctx.arc(peg.x, peg.y, peg.r + peg.hit * 2, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, 255, 255, ${0.28 + peg.hit * 0.5})`;
      ctx.fill();
    }

    // Render divider gate partitions
    const usable = playRight - playLeft;
    const gw = usable / gates.length;
    ctx.font = "8px ui-monospace, monospace";
    ctx.textAlign = "center";
    ctx.textBaseline = "alphabetic";

    for (let i = 0; i < gates.length; i++) {
      const gate = gates[i];
      const gx = playLeft + i * gw;
      ctx.strokeStyle = "rgba(255,255,255,0.12)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(gx, playBottom);
      ctx.lineTo(gx, playBottom + 40);
      ctx.stroke();

      ctx.fillStyle = gate.color;
      ctx.globalAlpha = 0.85;
      ctx.fillText(gate.label, gx + gw / 2, playBottom + 22);
      ctx.globalAlpha = 1;
    }
    
    // Boundary line right edge
    ctx.strokeStyle = "rgba(255,255,255,0.12)";
    ctx.beginPath();
    ctx.moveTo(playRight, playBottom);
    ctx.lineTo(playRight, playBottom + 40);
    ctx.stroke();

    // Render physical beads
    for (const b of ballsRef.current) {
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
      ctx.fillStyle = "#e3d9c6";
      ctx.shadowColor = "rgba(227,217,198,0.8)";
      ctx.shadowBlur = 8;
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    // Render burst particles
    for (const p of particlesRef.current) {
      ctx.globalAlpha = p.alpha;
      ctx.fillStyle = p.color;
      ctx.fillRect(p.x, p.y, p.size, p.size);
      ctx.globalAlpha = 1;
    }
  };

  const drawFire = (canvas: HTMLCanvasElement | null, buf: Uint8Array, palette: string[]) => {
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    ctx.clearRect(0, 0, FW, FH);
    for (let y = 0; y < FH; y++) {
      for (let x = 0; x < FW; x++) {
        const v = buf[y * FW + x];
        if (v <= 0) continue;
        ctx.fillStyle = palette[v];
        ctx.fillRect(x, y, 1, 1);
      }
    }
  };

  const tick = () => {
    time.current += 1;
    tickPhysics();
    drawBoard();

    // Cellular Automata fire update step
    const cap = 12;
    const isGameOver = beadsCount <= 0 && !hasCards;
    flareBoost.current *= 0.94;
    const baseT = isGameOver ? 0 : clamp(beadsCount / cap, 0, 1);
    const effT = isGameOver ? 0 : clamp(baseT + flareBoost.current * 0.55, 0, 1.35);
    const decayChance = isGameOver ? 0.98 : lerp(0.85, 0.1, Math.min(1, effT));
    const sourceVal = isGameOver ? 0 : Math.round(lerp(14, 39, Math.min(1, effT)));

    for (let x = 0; x < FW; x++) {
      const idx = (FH - 1) * FW + x;
      fireBufL.current[idx] = sourceVal > 0 ? Math.max(0, sourceVal - Math.floor(Math.random() * 4)) : 0;
      fireBufR.current[idx] = sourceVal > 0 ? Math.max(0, sourceVal - Math.floor(Math.random() * 4)) : 0;
    }
    spreadFire(fireBufL.current, FW, FH, decayChance);
    spreadFire(fireBufR.current, FW, FH, decayChance);

    const palette = PALETTES[eyeMode] || PALETTES.normal;
    drawFire(fireLeftCanvasRef.current, fireBufL.current, palette);
    drawFire(fireRightCanvasRef.current, fireBufR.current, palette);

    // Symmetrical recoil update
    const activeCount = ballsRef.current.length;
    let targetRecoil = 0;
    if (activeCount > 0) targetRecoil = 3;
    handState.current.recoilY = lerp(handState.current.recoilY, targetRecoil + Math.sin(time.current * 0.05) * 3, 0.08);

    if (leftHandRef.current) {
      leftHandRef.current.style.transform = `translateY(${handState.current.recoilY}px)`;
    }
    if (rightHandRef.current) {
      rightHandRef.current.style.transform = `translateY(${handState.current.recoilY}px)`;
    }
  };

  const isBoardInteractive = !isLocked && beadsCount > 0;

  return (
    <div ref={rootRef} className="w-full flex flex-col items-center select-none" id="game-wrap">
      <div
        id="frame"
        className="relative flex flex-col items-center bg-transparent transition-transform duration-200"
        style={{
          width: "92vw",
          maxWidth: "460px",
          aspectRatio: "480/680",
          boxShadow: "none",
        }}
      >
        {/* Breathing skeleton image backdrop */}
        <img
          src={pachinkoBgSkeleton}
          alt="skeleton"
          style={{
            position: "absolute",
            inset: 0,
            width: "100%",
            height: "100%",
            objectFit: "cover",
            objectPosition: "center",
            pointerEvents: "none",
            userSelect: "none",
            animation: "skeleton-breath 10s ease-in-out infinite",
            filter: beadsCount <= 0 && !hasCards ? "grayscale(1) brightness(0.6)" : "none",
            zIndex: 1,
          }}
        />

        {/* Eye fire pixel canvases */}
        <div style={{ position: "absolute", left: "30%", top: "13.8%", width: "9%", aspectRatio: "1/1.8", transform: "translate(-50%, -96%)", pointerEvents: "none", zIndex: 2 }}>
          <canvas ref={fireLeftCanvasRef} width={FW} height={FH} style={{ width: "100%", height: "100%", imageRendering: "pixelated", display: "block" }} />
        </div>
        <div style={{ position: "absolute", left: "62.6%", top: "13.8%", width: "9%", aspectRatio: "1/1.8", transform: "translate(-50%, -96%)", pointerEvents: "none", zIndex: 2 }}>
          <canvas ref={fireRightCanvasRef} width={FW} height={FH} style={{ width: "100%", height: "100%", imageRendering: "pixelated", display: "block" }} />
        </div>

        {/* Recoil side hands */}
        <div style={{ position: "absolute", inset: "-6% -16% -4% -16%", zIndex: 3, display: "flex", justifyContent: "space-between", pointerEvents: "none" }}>
          <div ref={leftHandRef} style={{ width: "32%", display: "flex", alignItems: "flex-end", transformOrigin: "bottom left" }}>
            <img src={pachinkoHands} alt="Left Hand" style={{ width: "100%", height: "auto", display: "block", filter: "drop-shadow(0 0 10px rgba(0,0,0,0.85))" }} />
          </div>
          <div ref={rightHandRef} style={{ width: "32%", display: "flex", alignItems: "flex-end", justifyContent: "flex-end", transformOrigin: "bottom right" }}>
            <img src={pachinkoHands} alt="Right Hand" style={{ width: "100%", height: "auto", display: "block", transform: "scaleX(-1)", filter: "drop-shadow(0 0 10px rgba(0,0,0,0.85))" }} />
          </div>
        </div>

        {/* Primary 2D Canvas board layout */}
        <canvas
          ref={boardCanvasRef}
          onPointerDown={handlePointerDown}
          style={{
            position: "absolute",
            inset: 0,
            width: "100%",
            height: "100%",
            zIndex: 4,
            cursor: isBoardInteractive ? "pointer" : "default",
            touchAction: "none",
          }}
        />
      </div>
    </div>
  );
}
