import React, { useEffect, useRef } from "react";
import pachinkoHands from "../../pachinko_hands.webp";

export default function AsciiFrontHands() {
  const leftHandRef = useRef<HTMLDivElement | null>(null);
  const rightHandRef = useRef<HTMLDivElement | null>(null);

  // Dynamic physics tracking state
  const stateRef = useRef({
    recoilY: 0,
    recoilX: 0,
    mouseY: 0,
    mouseX: 0,
    targetMouseY: 0,
    targetMouseX: 0,
    time: 0,
  });

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;
      // Map coordinates to normalized limits
      stateRef.current.targetMouseX = ((e.clientX - cx) / cx) * 16;
      stateRef.current.targetMouseY = ((e.clientY - cy) / cy) * 16;
    };

    const handleControl = (e: Event) => {
      const customEvent = e as CustomEvent;
      const detail = customEvent.detail || {};

      if (detail.action === "peg-bounce") {
        stateRef.current.recoilY += 1.4;
      } else if (detail.action === "wall-bounce") {
        stateRef.current.recoilX = detail.side === "left" ? -4.0 : 4.0;
      } else if (detail.action === "ball-landed") {
        stateRef.current.recoilY += 7.0;
      } else if (detail.action === "planet-hit") {
        stateRef.current.recoilY -= 3.5;
      }
    };

    window.addEventListener("mousemove", handleMouseMove);
    window.addEventListener("ascii-eyes-control", handleControl);

    let animationId: number;

    const tickPhysics = () => {
      const s = stateRef.current;
      s.time += 0.025;

      // Damp recoil springs
      s.recoilY *= 0.86;
      s.recoilX *= 0.86;

      // Lag follow mouse
      s.mouseX += (s.targetMouseX - s.mouseX) * 0.07;
      s.mouseY += (s.targetMouseY - s.mouseY) * 0.07;

      // Organic float breathing
      const breatheY = Math.sin(s.time) * 4.5;
      const breatheX = Math.cos(s.time * 0.6) * 2.5;

      // Symmetrical left hand transform updates
      if (leftHandRef.current) {
        const lx = s.mouseX + breatheX + s.recoilX;
        const ly = s.mouseY + breatheY + s.recoilY;
        const rot = -((s.mouseX * 0.3) + (s.recoilX * 0.8));
        leftHandRef.current.style.transform = `translate3d(${lx}px, ${ly}px, 0) rotate(${rot}deg)`;
      }

      // Symmetrical right hand transform updates
      if (rightHandRef.current) {
        const rx = s.mouseX - breatheX + s.recoilX;
        const ry = s.mouseY + breatheY + s.recoilY;
        const rot = -((s.mouseX * 0.3) + (s.recoilX * 0.8));
        rightHandRef.current.style.transform = `translate3d(${rx}px, ${ry}px, 0) rotate(${rot}deg)`;
      }

      animationId = requestAnimationFrame(tickPhysics);
    };

    animationId = requestAnimationFrame(tickPhysics);

    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("ascii-eyes-control", handleControl);
      cancelAnimationFrame(animationId);
    };
  }, []);

  return (
    <div className="absolute inset-x-[-120px] bottom-[-45px] top-[10px] w-[calc(100%+240px)] h-[calc(100%+55px)] pointer-events-none select-none z-30 flex justify-between">
      {/* Symmetrical Left Hand */}
      <div 
        ref={leftHandRef}
        className="relative w-1/2 h-full opacity-[0.94] select-none flex items-end justify-start transition-transform duration-75 ease-out"
        style={{
          transformOrigin: "bottom left",
        }}
      >
        <img 
          src={pachinkoHands} 
          alt="Left Hand" 
          className="w-[185px] h-auto object-contain object-bottom filter drop-shadow-[0_0_12px_rgba(0,0,0,0.8)]"
          style={{ maxHeight: '90%' }}
        />
      </div>

      {/* Symmetrical Right Hand */}
      <div 
        ref={rightHandRef}
        className="relative w-1/2 h-full opacity-[0.94] select-none flex items-end justify-end transition-transform duration-75 ease-out"
        style={{
          transformOrigin: "bottom right",
        }}
      >
        <img 
          src={pachinkoHands} 
          alt="Right Hand" 
          className="w-[185px] h-auto object-contain object-bottom scale-x-[-1] filter drop-shadow-[0_0_12px_rgba(0,0,0,0.8)]"
          style={{ maxHeight: '90%' }}
        />
      </div>
    </div>
  );
}
