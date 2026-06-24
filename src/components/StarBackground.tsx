import { useEffect, useRef } from 'react';
import { Planet } from '../types';

interface StarBackgroundProps {
  planets: Planet[];
  activePlanets: Set<string>;
}

export default function StarBackground({ planets, activePlanets }: StarBackgroundProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const animationRef = useRef<number | null>(null);
  const timeRef = useRef<number>(0);
  const pointerRef = useRef({ x: -2000, y: -2000, active: false });

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const resizeCanvas = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    // Track user pointers dynamically for subtle line distortion/warp (analog feel)
    const handlePointerMove = (e: PointerEvent) => {
      pointerRef.current.x = e.clientX;
      pointerRef.current.y = e.clientY;
      pointerRef.current.active = true;
    };

    const handlePointerLeave = () => {
      pointerRef.current.x = -2000;
      pointerRef.current.y = -2000;
      pointerRef.current.active = false;
    };

    window.addEventListener('pointermove', handlePointerMove);
    window.addEventListener('pointerleave', handlePointerLeave);

    const hexToRgb = (hex: string) => {
      if (!hex || hex.length < 7) return '200,164,90';
      return `${parseInt(hex.slice(1, 3), 16)},${parseInt(hex.slice(3, 5), 16)},${parseInt(hex.slice(5, 7), 16)}`;
    };

    // Draw procedural alchemical glyph in a small cell
    const drawAlchemicalSigil = (
      c: CanvasRenderingContext2D,
      x: number,
      y: number,
      size: number,
      seed: number
    ) => {
      c.save();
      c.translate(x + size / 2, y + size / 2);

      const r = size * 0.42;
      const type = Math.floor(seed) % 8;

      // Draw base bounding box or circle
      c.strokeStyle = 'rgba(255, 255, 255, 0.08)';
      c.lineWidth = 0.75;
      
      if (seed % 2 > 1) {
        c.strokeRect(-size / 2 + 1, -size / 2 + 1, size - 2, size - 2);
      } else {
        c.beginPath();
        c.arc(0, 0, r, 0, Math.PI * 2);
        c.stroke();
      }

      c.strokeStyle = 'rgba(200, 164, 90, 0.15)';
      switch (type) {
        case 0: // Cross with circles on tip
          c.beginPath();
          c.moveTo(-r, 0); c.lineTo(r, 0);
          c.moveTo(0, -r); c.lineTo(0, r);
          c.stroke();
          c.beginPath();
          c.arc(0, 0, r * 0.4, 0, Math.PI * 2);
          c.stroke();
          break;
        case 1: // Target dots
          c.beginPath();
          c.arc(0, 0, r * 0.7, 0, Math.PI * 2);
          c.arc(0, 0, r * 0.3, 0, Math.PI * 2);
          c.stroke();
          c.beginPath();
          c.arc(0, 0, 1.5, 0, Math.PI * 2);
          c.fillStyle = 'rgba(200, 164, 90, 0.2)';
          c.fill();
          break;
        case 2: // Triangle inside circle
          c.beginPath();
          c.moveTo(0, -r);
          c.lineTo(r * 0.86, r * 0.5);
          c.lineTo(-r * 0.86, r * 0.5);
          c.closePath();
          c.stroke();
          c.beginPath();
          c.arc(0, r * 0.15, r * 0.35, 0, Math.PI * 2);
          c.stroke();
          break;
        case 3: // Spinal divide with crosshairs
          c.beginPath();
          c.moveTo(0, -r); c.lineTo(0, r);
          c.moveTo(-r * 0.6, -r * 0.3); c.lineTo(r * 0.6, -r * 0.3);
          c.moveTo(-r * 0.6, r * 0.3); c.lineTo(r * 0.6, r * 0.3);
          c.stroke();
          break;
        case 4: // Triple concentric arcs
          c.beginPath();
          c.arc(0, 0, r * 0.8, -Math.PI / 2, Math.PI);
          c.stroke();
          c.beginPath();
          c.arc(0, 0, r * 0.5, 0, Math.PI * 1.5);
          c.stroke();
          break;
        case 5: // Hourglass / Alchemical Salt
          c.beginPath();
          c.moveTo(-r * 0.7, -r * 0.7); c.lineTo(r * 0.7, -r * 0.7);
          c.lineTo(-r * 0.7, r * 0.7); c.lineTo(r * 0.7, r * 0.7);
          c.closePath();
          c.stroke();
          c.beginPath();
          c.moveTo(-r * 0.8, 0); c.lineTo(r * 0.8, 0);
          c.stroke();
          break;
        case 6: // Sulphur / Fire Triangle
          c.beginPath();
          c.moveTo(0, -r);
          c.lineTo(r * 0.8, r * 0.2);
          c.lineTo(-r * 0.8, r * 0.2);
          c.closePath();
          c.moveTo(0, r * 0.2); c.lineTo(0, r * 0.9);
          c.moveTo(-r * 0.4, r * 0.65); c.lineTo(r * 0.4, r * 0.65);
          c.stroke();
          break;
        case 7: // Solar spirit wheel
          c.beginPath();
          c.arc(0, 0, r * 0.6, 0, Math.PI * 2);
          c.stroke();
          c.beginPath();
          for (let a = 0; a < Math.PI * 2; a += Math.PI / 4) {
            c.moveTo(Math.cos(a) * r * 0.6, Math.sin(a) * r * 0.6);
            c.lineTo(Math.cos(a) * r, Math.sin(a) * r);
          }
          c.stroke();
          break;
      }
      c.restore();
    };

    const draw = () => {
      if (!canvas || !ctx) return;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      timeRef.current += 0.00045; // Slow, majestic rotation (not whimsical)

      const cx = canvas.width / 2;
      const cy = canvas.height / 2;
      const px = pointerRef.current.x;
      const py = pointerRef.current.y;
      const hasPointer = pointerRef.current.active && px > 0 && py > 0;

      // Distortion lens function (analog chalkboard feel)
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
            dy: Math.sin(angle) * force * pullAmt,
          };
        }
        return { dx: 0, dy: 0 };
      };

      // ─── PART A: SUBTLE BACKGROUND GRID ───
      ctx.lineWidth = 0.5;
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.012)';
      const gridSize = 60;
      for (let x = 0; x < canvas.width; x += gridSize) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();
      }
      for (let y = 0; y < canvas.height; y += gridSize) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
      }

      // ─── PART B: NODDER'S PERIODIC ORBITS (CONCENTRIC CODES) ───
      const orbits = [110, 190, 275, 360, 440];
      const spokeAngles = [0, 45, 90, 135, 180, 225, 270, 315];
      const spokeLabels = ['0 // HE', '1 // H', '2 // LI', '3 // BE', '4 // B', '5 // C', '6 // N', '7 // O'];

      orbits.forEach((r, idx) => {
        ctx.beginPath();
        // Alternating dashed and solid lines for scientific schematics
        if (idx % 2 === 1) {
          ctx.setLineDash([3, 7]);
        } else {
          ctx.setLineDash([]);
        }
        ctx.strokeStyle = 'rgba(215, 205, 190, 0.035)';
        ctx.arc(cx, cy, r, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);
      });

      // Spoke radial coordinates (Nodder vectors)
      spokeAngles.forEach((deg, i) => {
        const rad = (deg * Math.PI) / 180;
        const orbitLimit = orbits[orbits.length - 1] + 15;
        const rawEndX = cx + orbitLimit * Math.cos(rad);
        const rawEndY = cy + orbitLimit * Math.sin(rad);

        const inf = applyInterference(rawEndX, rawEndY, 140, 6);
        const endX = rawEndX + inf.dx;
        const endY = rawEndY + inf.dy;

        const infCenter = applyInterference(cx, cy, 140, 6);
        const startX = cx + infCenter.dx;
        const startY = cy + infCenter.dy;

        ctx.beginPath();
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.025)';
        ctx.moveTo(startX, startY);
        ctx.lineTo(endX, endY);
        ctx.stroke();

        // Spoke numbers at outer perimeter
        ctx.fillStyle = 'rgba(215, 205, 190, 0.3)';
        ctx.font = '7px "JetBrains Mono", monospace';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        
        const labelX = cx + (orbitLimit + 15) * Math.cos(rad);
        const labelY = cy + (orbitLimit + 15) * Math.sin(rad);
        ctx.fillText(spokeLabels[i], labelX, labelY);
      });

      // Intersecting secondary coordinate system (Nodder's dual-eye epicycles)
      const ecx = cx + 220;
      const ecy = cy + 130;
      const epicycleOrbits = [50, 95, 140];
      epicycleOrbits.forEach((r) => {
        ctx.beginPath();
        ctx.setLineDash([2, 5]);
        ctx.strokeStyle = 'rgba(250, 240, 220, 0.02)';
        ctx.arc(ecx, ecy, r, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);
      });

      // Crosshairs of secondary epicycle
      ctx.beginPath();
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.015)';
      ctx.moveTo(ecx - 160, ecy); ctx.lineTo(ecx + 160, ecy);
      ctx.moveTo(ecx, ecy - 160); ctx.lineTo(ecx, ecy + 160);
      ctx.stroke();

      // ─── PART C: SEPHIROTIC SPINAL BACKBONE (NEURAL NETWORK) ───
      const scx = cx - 340;
      const scy = cy - 60;
      const sephirothNodes = [
        { label: '01_KETHER', x: 0, y: -220, active: true },
        { label: '02_CHOKMAH', x: 75, y: -170, active: false },
        { label: '03_BINAH', x: -75, y: -170, active: false },
        { label: '04_CHESED', x: 75, y: -90, active: false },
        { label: '05_GEBURAH', x: -75, y: -90, active: false },
        { label: '06_TIPHERETH', x: 0, y: -40, active: true },
        { label: '07_NETZACH', x: 75, y: 40, active: false },
        { label: '08_HOD', x: -75, y: 40, active: false },
        { label: '09_YESOD', x: 0, y: 90, active: true },
        { label: '10_MALKUTH', x: 0, y: 170, active: true },
      ];

      // Draw path wires (synaptic conduits) between network nodes
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.025)';
      ctx.lineWidth = 0.5;

      const getWarpedNodeCoords = (n: { x: number; y: number }) => {
        const rawX = scx + n.x;
        const rawY = scy + n.y;
        const inf = applyInterference(rawX, rawY, 120, 6);
        return { x: rawX + inf.dx, y: rawY + inf.dy };
      };

      // Draw connection lines between related nodes
      for (let i = 0; i < sephirothNodes.length; i++) {
        for (let j = i + 1; j < sephirothNodes.length; j++) {
          const n1 = sephirothNodes[i];
          const n2 = sephirothNodes[j];
          // Connect neighboring layers or diagonal paths physically
          const distY = Math.abs(n1.y - n2.y);
          const distX = Math.abs(n1.x - n2.x);
          if (distY < 140 && distX < 160) {
            const p1 = getWarpedNodeCoords(n1);
            const p2 = getWarpedNodeCoords(n2);
            ctx.beginPath();
            ctx.moveTo(p1.x, p1.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();

            // Scribe weight labels along some of the transmission cords
            if ((i + j) % 5 === 0) {
              const mx = (p1.x + p2.x) / 2;
              const my = (p1.y + p2.y) / 2;
              const weightVal = (Math.sin(i * 12 + j * 9) * 2.5).toFixed(5);
              ctx.fillStyle = 'rgba(200, 164, 90, 0.15)';
              ctx.font = '5.5px "JetBrains Mono", monospace';
              ctx.fillText(weightVal, mx + 5, my);
            }
          }
        }
      }

      // Draw the neural network nodes themselves
      sephirothNodes.forEach((n) => {
        const pt = getWarpedNodeCoords(n);
        
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, 4, 0, Math.PI * 2);
        ctx.strokeStyle = n.active ? 'rgba(200, 164, 90, 0.4)' : 'rgba(255, 255, 255, 0.1)';
        ctx.fillStyle = n.active ? 'rgba(200, 164, 90, 0.15)' : 'rgba(0, 0, 0, 0.3)';
        ctx.lineWidth = 0.75;
        ctx.fill();
        ctx.stroke();

        // Inner core
        if (n.active) {
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, 1.2, 0, Math.PI * 2);
          ctx.fillStyle = 'rgba(200, 164, 90, 0.6)';
          ctx.fill();
        }

        // Draw node title tags
        ctx.fillStyle = 'rgba(255, 255, 255, 0.2)';
        ctx.font = '6px "JetBrains Mono", monospace';
        ctx.textAlign = 'left';
        ctx.fillText(n.label, pt.x + 8, pt.y + 2);
      });

      // ─── PART D: ASTROLABE WIREFRAME GLOBE (LOWER LEFT MAPS) ───
      const gcx = 190;
      const gcy = canvas.height - 180;
      if (gcy > 300) {
        const gr = 70;
        const gWarp = applyInterference(gcx, gcy, 120, 6);
        const gx = gcx + gWarp.dx;
        const gy = gcy + gWarp.dy;

        // Outer sphere ring
        ctx.beginPath();
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
        ctx.arc(gx, gy, gr, 0, Math.PI * 2);
        ctx.stroke();

        // Longitude coordinates arcs
        ctx.beginPath();
        ctx.ellipse(gx, gy, gr, gr * 0.45, 0, 0, Math.PI * 2);
        ctx.ellipse(gx, gy, gr, gr * 0.18, 0, 0, Math.PI * 2);
        // Latitude vertical arcs
        ctx.ellipse(gx, gy, gr * 0.6, gr, 0, 0, Math.PI * 2);
        ctx.ellipse(gx, gy, gr * 0.25, gr, 0, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.02)';
        ctx.stroke();

        // Horizontal baseline axis
        ctx.beginPath();
        ctx.moveTo(gx - gr - 15, gy);
        ctx.lineTo(gx + gr + 15, gy);
        ctx.moveTo(gx, gy - gr - 15);
        ctx.lineTo(gx, gy + gr + 15);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.035)';
        ctx.stroke();

        // Pyramid projection cone (map projector)
        ctx.beginPath();
        ctx.moveTo(gx, gy - gr);
        ctx.lineTo(gx - gr * 1.5, gy + gr * 1.4);
        ctx.lineTo(gx + gr * 1.5, gy + gr * 1.4);
        ctx.closePath();
        ctx.strokeStyle = 'rgba(200, 164, 90, 0.025)';
        ctx.stroke();

        // Concentric projection arcs rising from bottom
        ctx.beginPath();
        ctx.arc(gx, gy + gr * 1.4, gr * 0.8, Math.PI, 0);
        ctx.arc(gx, gy + gr * 1.4, gr * 1.5, Math.PI, 0);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.015)';
        ctx.stroke();

        ctx.fillStyle = 'rgba(255, 255, 255, 0.15)';
        ctx.font = '6px "JetBrains Mono", monospace';
        ctx.textAlign = 'center';
        ctx.fillText('SOL_COORD_GRID [V4]', gx, gy + gr + 30);
      }

      // ─── PART E: ALCHEMICAL SEALS GRID (LOWER RIGHT SIGILS MATRIX) ───
      const srgColCount = 6;
      const srgRowCount = 5;
      const cellSize = 30;
      const gridWidth = srgColCount * cellSize;
      const gridHeight = srgRowCount * cellSize;
      
      const gStartX = canvas.width - gridWidth - 50;
      const gStartY = canvas.height - gridHeight - 110;

      if (gStartY > 250 && gStartX > cx + 150) {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.02)';
        ctx.lineWidth = 0.5;

        // Draw grid bounding dividers
        for (let r = 0; r <= srgRowCount; r++) {
          const rx = gStartX;
          const ry = gStartY + r * cellSize;
          ctx.beginPath();
          ctx.moveTo(rx, ry);
          ctx.lineTo(rx + gridWidth, ry);
          ctx.stroke();
        }
        for (let c = 0; c <= srgColCount; c++) {
          const rx = gStartX + c * cellSize;
          const ry = gStartY;
          ctx.beginPath();
          ctx.moveTo(rx, ry);
          ctx.lineTo(rx, ry + gridHeight);
          ctx.stroke();
        }

        // Draw mini alchemical symbols deterministically inside cells
        for (let r = 0; r < srgRowCount; r++) {
          for (let c = 0; c < srgColCount; c++) {
            const x = gStartX + c * cellSize;
            const y = gStartY + r * cellSize;
            const seedVal = (r * 13 + c * 37 + 7);
            drawAlchemicalSigil(ctx, x, y, cellSize, seedVal);
          }
        }

        // Grid caption
        ctx.fillStyle = 'rgba(215, 205, 190, 0.25)';
        ctx.font = '6.5px "JetBrains Mono", monospace';
        ctx.textAlign = 'right';
        ctx.fillText('SIGIL_MATRIX // CHRONOS_SEALS', gStartX + gridWidth, gStartY - 10);
      }

      // ─── PART F: TELEMETRY ANNOTATIONS IN SCREEN MARGINS ───
      ctx.fillStyle = 'rgba(215, 205, 190, 0.18)';
      ctx.font = '6.5px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';

      // Left panel labels
      ctx.fillText('PLANETARY_ENGINES: ACTIVE', 40, 80);
      ctx.fillText('BIOPHASIC_SPINE_ALIGN // YES', 40, 100);
      ctx.fillText('SPECTRUM: CJS_STANDALONE', 40, 120);

      // Right panel labels
      ctx.textAlign = 'right';
      ctx.fillText('ASTRAL_OS_v3.2_SOL-CONDUITS', canvas.width - 40, 80);
      ctx.fillText('INTEGRATION_STEPS: 9399', canvas.width - 40, 100);
      ctx.fillText('ERR_CALCULATION_COF: 1.645119', canvas.width - 40, 120);
      
      // Bottom axis coordinates list
      ctx.textAlign = 'left';
      ctx.fillText('X_AXIS: [λ - 23.4°]   Y_AXIS: [φ + 12.8°]   CONCURRENT_COF: 3', 40, canvas.height - 35);

      // ─── PART G: PLANETARY INSTANCES & THEIR RADIATIVE SYSTEM ───
      planets.forEach((p, idx) => {
        const isActive = activePlanets.has(p.name);
        
        // Extremely slow drift/rotation for cosmic alignment, not fast or whimsical
        const slowDriftDeg = p.deg + timeRef.current * 8; 
        const rad = ((slowDriftDeg - 90) * Math.PI) / 180;
        
        // Find corresponding distance sphere orbit
        // Mars/Sun etc. are plotted on matching ring radii
        const currentRadius = orbits[idx % orbits.length] || 275;
        const rxNode = cx + currentRadius * Math.cos(rad);
        const ryNode = cy + currentRadius * Math.sin(rad);

        const infNode = applyInterference(rxNode, ryNode, 130, 8);
        const finalX = rxNode + infNode.dx;
        const finalY = ryNode + infNode.dy;

        const valAlpha = isActive ? 0.9 : 0.08;
        const sizeVal = isActive ? 5.5 : 2.5;

        // Draw dotted radial line from epicenter to planet instance
        ctx.beginPath();
        ctx.setLineDash([2, 5]);
        ctx.strokeStyle = `rgba(${hexToRgb(p.color)}, ${valAlpha * 0.35})`;
        ctx.moveTo(cx, cy);
        ctx.lineTo(finalX, finalY);
        ctx.stroke();
        ctx.setLineDash([]);

        // Planet shell node circle
        ctx.beginPath();
        ctx.arc(finalX, finalY, sizeVal, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(${hexToRgb(p.color)}, ${valAlpha * 0.8})`;
        ctx.fillStyle = isActive ? `rgba(${hexToRgb(p.color)}, 0.15)` : 'rgba(0,0,0,0.4)';
        ctx.lineWidth = 1;
        ctx.fill();
        ctx.stroke();

        if (isActive) {
          // Inner glowing core dot
          ctx.beginPath();
          ctx.arc(finalX, finalY, 1.5, 0, Math.PI * 2);
          ctx.fillStyle = p.color;
          ctx.fill();

          // Scribe astrological glyph symbol floating above
          ctx.font = '13px "Cormorant Garamond", serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillStyle = `rgba(${hexToRgb(p.color)}, 0.5)`;
          ctx.fillText(p.symbol, finalX, finalY - 14);

          ctx.fillStyle = p.color;
          ctx.fillText(p.symbol, finalX, finalY - 15);

          // Annotation of degrees/alignment
          ctx.font = '6px "JetBrains Mono", monospace';
          ctx.fillStyle = 'rgba(215, 205, 190, 0.7)';
          ctx.textAlign = 'center';
          ctx.fillText(`${p.name.toUpperCase()} [${p.deg.toFixed(1)}°]`, finalX, finalY + 14);
        } else {
          // Hollow node with tiny symbol
          ctx.font = '8px "Cormorant Garamond", serif';
          ctx.fillStyle = `rgba(255, 255, 255, 0.08)`;
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(p.symbol, finalX, finalY);
        }
      });

      // ─── PART H: DRAW BRIDGING TRIPLE MOMENT DEVIATOR SHIELD ───
      // Connect active nodes in our spread with a dashed constellation pattern
      const activeCoords: { x: number; y: number; color: string }[] = [];
      planets.forEach((p, idx) => {
        if (activePlanets.has(p.name)) {
          const slowDriftDeg = p.deg + timeRef.current * 8;
          const rad = ((slowDriftDeg - 90) * Math.PI) / 180;
          const currentRadius = orbits[idx % orbits.length] || 275;
          const rxNode = cx + currentRadius * Math.cos(rad);
          const ryNode = cy + currentRadius * Math.sin(rad);
          const infNode = applyInterference(rxNode, ryNode, 130, 8);
          activeCoords.push({
            x: rxNode + infNode.dx,
            y: ryNode + infNode.dy,
            color: p.color,
          });
        }
      });

      if (activeCoords.length > 1) {
        ctx.beginPath();
        ctx.moveTo(activeCoords[0].x, activeCoords[0].y);
        for (let i = 1; i < activeCoords.length; i++) {
          ctx.lineTo(activeCoords[i].x, activeCoords[i].y);
        }
        if (activeCoords.length > 2) {
          ctx.lineTo(activeCoords[0].x, activeCoords[0].y);
        }
        
        // Gentle diagrammatic pulsing connector lines
        const pulseAlpha = 0.22 + 0.08 * Math.sin(Date.now() / 900);
        ctx.strokeStyle = `rgba(200, 164, 90, ${pulseAlpha})`;
        ctx.lineWidth = 0.75;
        ctx.setLineDash([5, 6]);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      animationRef.current = requestAnimationFrame(draw);
    };

    draw();

    return () => {
      window.removeEventListener('resize', resizeCanvas);
      window.removeEventListener('pointermove', handlePointerMove);
      window.removeEventListener('pointerleave', handlePointerLeave);
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [planets, activePlanets]);

  return (
    <canvas
      ref={canvasRef}
      id="constellationCanvas"
      className="stars-canvas fixed inset-0 w-screen h-screen z-0 pointer-events-none"
    />
  );
}
