import React, { useEffect, useRef } from 'react';

export default function AtmosphericFluff() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animationFrameId: number;
    let dpr = window.devicePixelRatio || 1;
    let width = window.innerWidth;
    let height = window.innerHeight;

    const resize = () => {
      dpr = window.devicePixelRatio || 1;
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = width * dpr;
      canvas.height = height * dpr;
      canvas.style.width = `${width}px`;
      canvas.style.height = `${height}px`;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };
    
    window.addEventListener('resize', resize);
    resize();

    // Dust particles
    const dustCount = 45;
    const dust: { x: number, y: number, r: number, vx: number, vy: number, alpha: number }[] = [];
    for (let i = 0; i < dustCount; i++) {
      dust.push({
        x: Math.random() * width,
        y: Math.random() * height,
        r: Math.random() * 1.5 + 0.5,
        vx: (Math.random() - 0.5) * 0.1,
        vy: (Math.random() - 0.5) * 0.15 - 0.05, // very slowly drift up
        alpha: Math.random() * 0.5 + 0.1
      });
    }

    // Terminal Scramble Streams (Originkit)
    const streamsCount = 15;
    const streams: { x: number, y: number, vy: number, text: string, opacity: number }[] = [];
    const phrases = [
      "integrity stable",
      "conduit active",
      "0xaf0a9c",
      "reciprocate.bin",
      "chance_factor: 1",
      "lunarot os v6.1",
      "alchemical conflux",
      "stability: nominal",
      "chancellery void",
      "orbit active",
      "astral.db: online"
    ];
    
    const createStream = () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      vy: -(Math.random() * 0.4 + 0.25), // slowly drift up
      text: phrases[Math.floor(Math.random() * phrases.length)],
      opacity: Math.random() * 0.12 + 0.04
    });

    for (let i = 0; i < streamsCount; i++) {
      streams.push(createStream());
    }

    let time = 0;
    let lastTime = 0;
    const fps = 25;
    const fpsInterval = 1000 / fps;

    const render = (timestamp: number) => {
      animationFrameId = requestAnimationFrame(render);
      const deltaTime = timestamp - lastTime;
      if (deltaTime < fpsInterval) return;
      lastTime = timestamp - (deltaTime % fpsInterval);

      time += 0.01;
      ctx.clearRect(0, 0, width, height);

      // Draw dust
      dust.forEach(p => {
        p.x += p.vx + Math.sin(time + p.y * 0.01) * 0.2;
        p.y += p.vy;
        
        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255, 255, 255, ${p.alpha * 0.5})`;
        ctx.fill();
      });

      // Draw terminal scramble streams
      streams.forEach((p) => {
        p.y += p.vy;

        if (p.y < -30) {
          p.y = height + 30;
          p.x = Math.random() * width;
        }

        // Generate a scrambling text using the glitch letters
        let scrambled = "";
        const glitchPool = "abcdefghijklmnopqrstuvwxyz0123456789⍼✦☿☽☉♁☾";
        for (let idx = 0; idx < p.text.length; idx++) {
          if (p.text[idx] === " ") {
            scrambled += " ";
          } else if (Math.random() < 0.20) {
            scrambled += glitchPool[Math.floor(Math.random() * glitchPool.length)];
          } else {
            scrambled += p.text[idx];
          }
        }

        ctx.font = "500 7px monospace";
        ctx.fillStyle = `rgba(255, 255, 255, ${p.opacity})`;
        ctx.fillText(scrambled, p.x, p.y);
      });
    };

    animationFrameId = requestAnimationFrame(render);

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <div className="fixed inset-0 pointer-events-none z-10 flex flex-col items-center overflow-hidden">
      {/* Canvas for smoke and fluff */}
      <canvas ref={canvasRef} className="absolute inset-0 w-full h-full" />

      {/* Chandelier ASCII Art hanging from top */}
      <div className="relative mt-0 text-[#ffffff] opacity-30 flex flex-col items-center" style={{ textShadow: '0 0 15px rgba(255,255,255,0.4)' }}>
        <div className="font-mono text-xs leading-none whitespace-pre text-center">
{`    |
   /|\\
  / | \\
 /  |  \\
----|----
\\ / | \\ /
 v  v  v `}
        </div>
        
        <div className="absolute top-[80%] flex justify-center w-full gap-[3.5rem] px-2">
            <span className="animate-pulse text-[#ffffff] text-xs blur-[0.5px]">✦</span>
            <span className="animate-pulse text-[#ffffff] text-sm blur-[1px] delay-75">✦</span>
            <span className="animate-pulse text-[#ffffff] text-xs blur-[0.5px] delay-150">✦</span>
        </div>
        
        {/* Subtle light cast down */}
        <div className="absolute top-[85%] w-96 h-96 bg-gradient-to-b from-[#ffffff]/5 via-[#ffffff]/2 to-transparent blur-3xl pointer-events-none" />
      </div>

    </div>
  );
}
