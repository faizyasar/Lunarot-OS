import React, { useEffect } from "react";
import { NatalUser, Planet, ELEMENT_COLOR } from "../types";

interface AppPachinkoProps {
  user: NatalUser;
  onUpdatePlanets: (planets: Planet[]) => void;
  onUpdateActivePlanets: (active: Set<string>) => void;
  onReset: () => void;
  isPurging: boolean;
  setIsPurging: (val: boolean) => void;
}

export default function AppPachinko({
  user,
  onUpdatePlanets,
  onUpdateActivePlanets,
  onReset,
  isPurging,
  setIsPurging,
}: AppPachinkoProps) {
  useEffect(() => {
    const sunDeg = user.sunIdx * 30 + 15;
    const moonDeg = user.moonIdx * 30 + 15;
    const initialPlanets: Planet[] = [
      { name: "Sun", symbol: "☉", deg: sunDeg, sign: user.sun, color: ELEMENT_COLOR[user.sun] || "#f5c842" },
      { name: "Moon", symbol: "☽", deg: moonDeg, sign: user.moon, color: ELEMENT_COLOR[user.moon] || "#c8c8ff" },
    ];
    if (user.rising) {
      initialPlanets.push({
        name: "Rising",
        symbol: "▲",
        deg: user.risingIdx * 30 + 15,
        sign: user.rising,
        color: ELEMENT_COLOR[user.rising] || "#ffffff",
      });
    }
    onUpdatePlanets(initialPlanets);
    onUpdateActivePlanets(new Set(["Sun", "Moon", "Rising"]));
  }, [user, onUpdatePlanets, onUpdateActivePlanets]);

  const handleLaunchGame = () => {
    window.open("./sacred-pachinko.html", "_blank");
  };

  const mono = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace";

  return (
    <div style={{ width: "100%", height: "100%", overflowY: "auto", fontFamily: mono, color: "#a89f92", fontSize: "13px", lineHeight: "1.75", boxSizing: "border-box", padding: "32px 24px 64px" }}>
      <div style={{ maxWidth: "620px", margin: "0 auto" }}>

        {/* Header */}
        <div style={{ borderBottom: "1px solid rgba(255,255,255,0.1)", paddingBottom: "20px", marginBottom: "32px" }}>
          <div style={{ fontSize: "9px", letterSpacing: "0.25em", textTransform: "uppercase", color: "#5a5248", marginBottom: "8px" }}>BUILD LOG</div>
          <h1 style={{ margin: 0, fontSize: "20px", fontWeight: 700, letterSpacing: "0.05em", color: "#e8e2da", fontFamily: mono }}>Sacred Pachinko</h1>
          <div style={{ marginTop: "6px", fontSize: "11px", color: "#6a6258", letterSpacing: "0.1em", textTransform: "uppercase" }}>Making It Feel Cursed</div>
        </div>

        {/* Launch button */}
        <div style={{ marginBottom: "36px" }}>
          <button
            onClick={handleLaunchGame}
            style={{
              display: "inline-flex", alignItems: "center", gap: "10px",
              padding: "12px 24px",
              background: "none", border: "1px solid rgba(255,255,255,0.25)", borderRadius: "6px",
              color: "#e8e2da", fontFamily: mono, fontSize: "11px", fontWeight: 700,
              letterSpacing: "0.2em", textTransform: "uppercase", cursor: "pointer",
              transition: "border-color 0.2s, background 0.2s",
            }}
            onMouseEnter={e => { (e.target as HTMLButtonElement).style.borderColor = "rgba(255,255,255,0.7)"; (e.target as HTMLButtonElement).style.background = "rgba(255,255,255,0.04)"; }}
            onMouseLeave={e => { (e.target as HTMLButtonElement).style.borderColor = "rgba(255,255,255,0.25)"; (e.target as HTMLButtonElement).style.background = "none"; }}
          >
            <span style={{ display: "inline-block", width: "8px", height: "8px", borderRadius: "50%", background: "#ef4444", animation: "pulse 1.5s ease-in-out infinite" }} />
            Open Sacred Pachinko
          </button>
        </div>

        {/* Intro */}
        <p style={{ color: "#7a7268", fontSize: "11px", margin: "0 0 16px", fontStyle: "italic" }}>
          Not a technical spec, just notes on chasing the vibe: a possessed pachinko machine, a skeleton behind the glass judging you, tarot cards deciding your fate. Here's how it got there.
        </p>
        <p style={{ margin: "0 0 36px" }}>
          Big shout out to <a href="https://www.ghosttail.com/game/" style={{ color: "#e3b341", textDecoration: "none" }} target="_blank" rel="noreferrer">ghosttail.com/game</a>, a real inspiration for this whole thing.
        </p>

        {/* Section: Getting the look right */}
        <h2 style={{ fontSize: "10px", letterSpacing: "0.2em", textTransform: "uppercase", color: "#cfc9c0", margin: "0 0 12px", paddingTop: "24px", borderTop: "1px solid rgba(255,255,255,0.06)", fontFamily: mono }}>
          Getting the look right
        </h2>
        <p style={{ margin: "0 0 10px" }}>Wanted a flame effect licking up from behind the tarot card, it kept disappearing entirely at first, invisible. Turned out it was collapsing to nothing behind the scenes. Got it visible, then made it bigger and moved it so it actually peeks out dramatically from behind the card like it's on fire.</p>
        <p style={{ margin: "0 0 10px" }}>The card kept getting swallowed up by the hands and the CRT static behind it, total mess, couldn't read it. Fixed the layering so the card sits clearly on top like it should.</p>
        <p style={{ margin: "0 0 36px" }}>Score and bead counter vanished behind the background at one point too, same kind of layering ghost. Brought it back to the front.</p>

        {/* Section: Making it feel alive */}
        <h2 style={{ fontSize: "10px", letterSpacing: "0.2em", textTransform: "uppercase", color: "#cfc9c0", margin: "0 0 12px", paddingTop: "24px", borderTop: "1px solid rgba(255,255,255,0.06)", fontFamily: mono }}>
          Making it feel alive and dramatic
        </h2>
        <p style={{ margin: "0 0 10px" }}>The card now punches onto screen with a hard overshoot, then settles into a slow, uneasy float, like it doesn't want to sit still.</p>
        <p style={{ margin: "0 0 10px" }}>The hands that present the card now lunge in bigger, with more spring and twist.</p>
        <p style={{ margin: "0 0 10px" }}>The chest and skull breathe on their own separate rhythms now instead of moving in lockstep, feels less robotic, more like something alive (or undead).</p>
        <p style={{ margin: "0 0 10px" }}>All the hands got a floatier, twitchier idle motion.</p>
        <p style={{ margin: "0 0 10px" }}>The skull's tilt and shake reaction got pushed way more violent when things go wrong.</p>
        <p style={{ margin: "0 0 10px" }}>The little glowing dots on the board got cranked up bright, real glow and bloom on impact.</p>
        <p style={{ margin: "0 0 10px" }}>The beads pulse with a warm glow now instead of just sitting there flat.</p>
        <p style={{ margin: "0 0 36px" }}>First pass on all of this was honestly too much, dialled the breathing, shake and hand movement back down by half so it reads as unsettling instead of seizure inducing.</p>

        {/* Section: Board feel */}
        <h2 style={{ fontSize: "10px", letterSpacing: "0.2em", textTransform: "uppercase", color: "#cfc9c0", margin: "0 0 12px", paddingTop: "24px", borderTop: "1px solid rgba(255,255,255,0.06)", fontFamily: mono }}>
          Board feel
        </h2>
        <p style={{ margin: "0 0 10px" }}>Swapped the plain gate labels for bold glowing suit symbols, reads more ritualistic.</p>
        <p style={{ margin: "0 0 10px" }}>Score glows gold now, more like a prize than a stat.</p>
        <p style={{ margin: "0 0 10px" }}>Bottom row of pegs now kicks the bead back much harder and more unpredictably.</p>
        <p style={{ margin: "0 0 10px" }}>Every other row of dots now gives the bead a random little upward hop, so it doesn't just fall straight down.</p>
        <p style={{ margin: "0 0 10px" }}>A bead that barely touches anything on the way down now just gets refunded instead of forcing a card draw, didn't feel earned otherwise.</p>
        <p style={{ margin: "0 0 36px" }}>Hitting the side walls now launches the bead hard instead of a soft bounce, much more physical, more chaotic.</p>

        {/* Section: Winning and losing */}
        <h2 style={{ fontSize: "10px", letterSpacing: "0.2em", textTransform: "uppercase", color: "#cfc9c0", margin: "0 0 12px", paddingTop: "24px", borderTop: "1px solid rgba(255,255,255,0.06)", fontFamily: mono }}>
          Winning and losing
        </h2>
        <p style={{ margin: "0 0 10px" }}>Game over now hits with a flash and a shatter, text stumbling in piece by piece instead of just appearing.</p>
        <p style={{ margin: "0 0 10px" }}>Restart flashes and zooms out first instead of just snapping back to the start.</p>
        <p style={{ margin: "0 0 10px" }}>Added an actual win state, the skull gets redder and angrier the higher the score climbs, and there's a proper victory moment at the top.</p>
        <p style={{ margin: "0 0 36px" }}>That victory moment didn't show up the first time it was wired in, turned out the win flag just wasn't being passed through to the screen at all. Fixed, now it fires.</p>

        {/* Section: The annoying part */}
        <h2 style={{ fontSize: "10px", letterSpacing: "0.2em", textTransform: "uppercase", color: "#cfc9c0", margin: "0 0 12px", paddingTop: "24px", borderTop: "1px solid rgba(255,255,255,0.06)", fontFamily: mono }}>
          The annoying part
        </h2>
        <p style={{ margin: "0 0 36px" }}>Things got painfully laggy for a stretch as more effects piled on, every tweak took forever to preview, which is its own kind of horror. Also lost some time running the background effect on WebGPU for no real payoff. Splitting the heavy background effect out into its own separate piece instead of cramming everything into one place fixed the lag for good.</p>

        {/* Footer */}
        <div style={{ marginTop: "48px", paddingTop: "20px", borderTop: "1px solid rgba(255,255,255,0.05)", fontSize: "9px", color: "#3a3530", letterSpacing: "0.2em", textTransform: "uppercase", textAlign: "center" }}>
          END OF LOG
        </div>

      </div>
    </div>
  );
}
