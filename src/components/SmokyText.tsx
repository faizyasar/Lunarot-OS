import React, { useState, useEffect, useRef } from "react";

export function SmokyText({
  text,
  font,
  color = "var(--gold)",
  appearTrigger = "default",
  scrollConfig,
  appearTransition,
  intensity = 10,
}: any) {
  const [displayText, setDisplayText] = useState("");
  const iterationRef = useRef(0);
  const frameRef = useRef<number | null>(null);

  const startScramble = () => {
    iterationRef.current = 0;
    if (frameRef.current) cancelAnimationFrame(frameRef.current);

    const glitchPool = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789⍼✦☿☽☉♁☾";
    const totalSteps = text.length * 2.5;

    const tick = () => {
      iterationRef.current += 0.5;
      let current = "";
      
      for (let i = 0; i < text.length; i++) {
        if (text[i] === " " || text[i] === "\n") {
          current += text[i];
        } else if (i < iterationRef.current / 2.5) {
          current += text[i];
        } else if (Math.random() < 0.3) {
          current += glitchPool[Math.floor(Math.random() * glitchPool.length)];
        } else {
          current += text[i].toLowerCase();
        }
      }

      setDisplayText(current);

      if (iterationRef.current < totalSteps) {
        frameRef.current = requestAnimationFrame(tick);
      } else {
        setDisplayText(text);
      }
    };

    frameRef.current = requestAnimationFrame(tick);
  };

  useEffect(() => {
    startScramble();
    return () => {
      if (frameRef.current) cancelAnimationFrame(frameRef.current);
    };
  }, [text]);

  const fontAny = font as any;
  const textAlign = (fontAny?.textAlign ?? "center") as string;
  const justify =
    textAlign === "right"
      ? "flex-end"
      : textAlign === "center"
        ? "center"
        : "flex-start";

  return (
    <div style={{ display: "flex", width: "100%", justifyContent: justify }}>
      <span style={{ ...fontAny, color: color, textShadow: "none", display: "inline-block" }}>
        {displayText}
      </span>
    </div>
  );
}
