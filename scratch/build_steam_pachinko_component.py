import sys

sys.stdout.reconfigure(encoding='utf-8')

steam_pachinko_code = """function ip({user:c,onUpdatePlanets:E,onUpdateActivePlanets:g,onReset:f,isPurging:v,setIsPurging:p}){
  const [para, setPara] = D.useState({x:0, y:0});
  const [activeTab, setActiveTab] = D.useState('activity');

  D.useEffect(()=>{
    const x=c.sunIdx*30+15,r=c.moonIdx*30+15,L=[{name:"Sun",symbol:"☉",deg:x,sign:c.sun,color:bn[c.sun]||"#f5c842"},{name:"Moon",symbol:"☽",deg:r,sign:c.moon,color:bn[c.moon]||"#c8c8ff"}];
    c.rising&&L.push({name:"Rising",symbol:"▲",deg:c.risingIdx*30+15,sign:c.rising,color:bn[c.rising]||"#ffffff"});
    E(L);
    g(new Set(["Sun","Moon","Rising"]));
  },[c,E,g]);

  const launchGame = () => { window.open("/sacred-pachinko", "_blank"); };
  const H = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace";

  const handleMouseMove = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = (e.clientX - rect.left - rect.width / 2) / (rect.width / 2);
    const y = (e.clientY - rect.top - rect.height / 2) / (rect.height / 2);
    setPara({ x, y });
  };

  const handleMouseLeave = () => {
    setPara({ x: 0, y: 0 });
  };

  return s.jsxs("div", {
    style: { width: "100%", height: "100%", overflowY: "auto", fontFamily: H, color: "#969b9e", background: "#0e141b", boxSizing: "border-box" },
    children: [
      /* --- STEAM HERO BANNER WITH PARALLAX --- */
      s.jsxs("div", {
        onMouseMove: handleMouseMove,
        onMouseLeave: handleMouseLeave,
        style: {
          position: "relative",
          width: "100%",
          height: "340px",
          overflow: "hidden",
          background: "radial-gradient(circle at 50% 30%, #1b2838 0%, #0e141b 100%)",
          perspective: "1000px",
          cursor: "pointer"
        },
        children: [
          /* Layer 0: Stars / Nebulae (Back Parallax) */
          s.jsx("div", {
            style: {
              position: "absolute",
              inset: "-20px",
              backgroundImage: "radial-gradient(1.5px 1.5px at 20px 30px, #ffffff 100%, transparent), radial-gradient(2px 2px at 40px 70px, rgba(255,255,255,0.7) 100%, transparent), radial-gradient(1px 1px at 90px 40px, #ffffff 100%, transparent)",
              backgroundSize: "180px 180px",
              opacity: 0.6,
              transform: `translate3d(${para.x * -8}px, ${para.y * -8}px, 0)`,
              transition: "transform 0.15s ease-out"
            }
          }),
          /* Layer 1: Radiant Skull / Skeleton Mid-ground */
          s.jsxs("div", {
            style: {
              position: "absolute",
              inset: 0,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              transform: `translate3d(${para.x * -24}px, ${para.y * -18}px, 0) rotateY(${para.x * 5}deg) rotateX(${para.y * -5}deg)`,
              transition: "transform 0.12s ease-out",
              pointerEvents: "none"
            },
            children: [
              s.jsx("div", {
                style: {
                  width: "280px",
                  height: "280px",
                  borderRadius: "50%",
                  background: "radial-gradient(circle, rgba(255, 120, 20, 0.25) 0%, rgba(239, 68, 68, 0.08) 50%, transparent 75%)",
                  filter: "blur(20px)",
                  position: "absolute"
                }
              }),
              s.jsx("div", {
                style: {
                  fontSize: "110px",
                  filter: "drop-shadow(0 0 25px rgba(255,140,0,0.6)) drop-shadow(0 0 50px rgba(239,68,68,0.4))",
                  userSelect: "none"
                },
                children: "💀"
              })
            ]
          }),
          /* Layer 2: Foreground Title & Subtitle */
          s.jsxs("div", {
            style: {
              position: "absolute",
              inset: 0,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              justifyContent: "center",
              transform: `translate3d(${para.x * -38}px, ${para.y * -30}px, 0) rotateY(${para.x * 8}deg)`,
              transition: "transform 0.1s ease-out",
              textShadow: "0 4px 20px rgba(0,0,0,0.9)",
              pointerEvents: "none"
            },
            children: [
              s.jsx("div", {
                style: { fontSize: "10px", letterSpacing: "0.4em", color: "#e3b341", fontWeight: 800, textTransform: "uppercase", marginBottom: "6px" },
                children: "LUNAROT OCCULT SIMULATOR"
              }),
              s.jsx("h1", {
                style: {
                  margin: 0,
                  fontSize: "36px",
                  fontWeight: 900,
                  letterSpacing: "0.15em",
                  color: "#ffffff",
                  textTransform: "uppercase",
                  fontFamily: H,
                  background: "linear-gradient(180deg, #ffffff 0%, #d4cebe 100%)",
                  WebkitBackgroundClip: "text",
                  WebkitTextFillColor: "transparent",
                  filter: "drop-shadow(0 2px 8px rgba(0,0,0,0.8))"
                },
                children: "SACRED PACHINKO"
              }),
              s.jsx("div", {
                style: { fontSize: "11px", letterSpacing: "0.2em", color: "#a89f92", marginTop: "8px" },
                children: "78 TAROT CONDUITS // CURSED PHYSICS MACHINE"
              })
            ]
          }),
          /* Steam Vignette Gradient Overlay */
          s.jsx("div", {
            style: {
              position: "absolute",
              inset: 0,
              background: "linear-gradient(180deg, rgba(14,20,27,0.2) 0%, rgba(14,20,27,0.85) 85%, #0e141b 100%)",
              pointerEvents: "none"
            }
          })
        ]
      }),

      /* --- STEAM ACTION BAR & STATS --- */
      s.jsxs("div", {
        style: {
          background: "#161d24",
          borderTop: "1px solid rgba(255,255,255,0.08)",
          borderBottom: "1px solid rgba(0,0,0,0.4)",
          padding: "16px 32px",
          display: "flex",
          flexWrap: "wrap",
          alignItems: "center",
          justifyContent: "space-between",
          gap: "20px"
        },
        children: [
          /* Left: Green Play Button */
          s.jsxs("div", {
            style: { display: "flex", alignItems: "center", gap: "16px" },
            children: [
              s.jsxs("button", {
                onClick: launchGame,
                style: {
                  display: "inline-flex",
                  alignItems: "center",
                  justifyContent: "center",
                  gap: "12px",
                  padding: "14px 42px",
                  background: "linear-gradient(135deg, #5cba02 0%, #4b9801 100%)",
                  border: "none",
                  borderRadius: "3px",
                  color: "#ffffff",
                  fontFamily: H,
                  fontSize: "16px",
                  fontWeight: 800,
                  letterSpacing: "0.15em",
                  textTransform: "uppercase",
                  cursor: "pointer",
                  boxShadow: "0 0 16px rgba(92,186,2,0.4), inset 0 1px 0 rgba(255,255,255,0.3)",
                  transition: "all 0.15s ease"
                },
                onMouseEnter: (e) => {
                  e.currentTarget.style.background = "linear-gradient(135deg, #6bd103 0%, #58b002 100%)";
                  e.currentTarget.style.boxShadow = "0 0 24px rgba(92,186,2,0.65), inset 0 1px 0 rgba(255,255,255,0.4)";
                },
                onMouseLeave: (e) => {
                  e.currentTarget.style.background = "linear-gradient(135deg, #5cba02 0%, #4b9801 100%)";
                  e.currentTarget.style.boxShadow = "0 0 16px rgba(92,186,2,0.4), inset 0 1px 0 rgba(255,255,255,0.3)";
                },
                children: [
                  s.jsx("span", { style: { fontSize: "14px" }, children: "▶" }),
                  "PLAY"
                ]
              }),
              s.jsxs("div", {
                style: { fontSize: "11px", color: "#67707b" },
                children: [
                  s.jsx("div", { style: { color: "#acb2b8", fontWeight: 700 }, children: "READY TO LAUNCH" }),
                  s.jsx("div", { children: "Vessel Handshake Synced" })
                ]
              })
            ]
          }),
          /* Right: Steam Stats Badges */
          s.jsxs("div", {
            style: { display: "flex", alignItems: "center", gap: "28px", fontSize: "11px" },
            children: [
              s.jsxs("div", {
                children: [
                  s.jsx("div", { style: { color: "#67707b", fontSize: "9px", textTransform: "uppercase", letterSpacing: "0.1em" }, children: "CLOUD STATUS" }),
                  s.jsx("div", { style: { color: "#66c0f4", fontWeight: 700, marginTop: "2px" }, children: "☁ Up to date" })
                ]
              }),
              s.jsxs("div", {
                children: [
                  s.jsx("div", { style: { color: "#67707b", fontSize: "9px", textTransform: "uppercase", letterSpacing: "0.1em" }, children: "LAST PLAYED" }),
                  s.jsx("div", { style: { color: "#c6d4df", fontWeight: 700, marginTop: "2px" }, children: "Today" })
                ]
              }),
              s.jsxs("div", {
                children: [
                  s.jsx("div", { style: { color: "#67707b", fontSize: "9px", textTransform: "uppercase", letterSpacing: "0.1em" }, children: "PLAY TIME" }),
                  s.jsx("div", { style: { color: "#c6d4df", fontWeight: 700, marginTop: "2px" }, children: "146.9 hours" })
                ]
              }),
              s.jsxs("div", {
                children: [
                  s.jsx("div", { style: { color: "#67707b", fontSize: "9px", textTransform: "uppercase", letterSpacing: "0.1em" }, children: "BEADS RECORD" }),
                  s.jsx("div", { style: { color: "#e3b341", fontWeight: 700, marginTop: "2px" }, children: "1,000" })
                ]
              })
            ]
          })
        ]
      }),

      /* --- STEAM SUB-NAV BAR --- */
      s.jsx("div", {
        style: {
          background: "#10161d",
          borderBottom: "1px solid rgba(255,255,255,0.05)",
          padding: "0 32px",
          display: "flex",
          gap: "24px",
          fontSize: "11px",
          fontWeight: 700,
          letterSpacing: "0.1em",
          textTransform: "uppercase"
        },
        children: ["Store Page", "DLC", "Community Hub", "Discussions", "Guides", "Workshop", "Support"].map((tab) => {
          const isAct = (tab.toLowerCase() === "discussions" && activeTab === "discussions") || (tab === "Store Page" && activeTab === "activity");
          return s.jsx("button", {
            key: tab,
            onClick: () => setActiveTab(tab.toLowerCase() === "discussions" ? "discussions" : "activity"),
            style: {
              background: "none",
              border: "none",
              borderBottom: isAct ? "2px solid #1a9fff" : "2px solid transparent",
              color: isAct ? "#ffffff" : "#67707b",
              padding: "12px 0",
              cursor: "pointer",
              fontFamily: H,
              transition: "color 0.15s, border-color 0.15s"
            },
            onMouseEnter: (e) => { if (!isAct) e.currentTarget.style.color = "#c6d4df"; },
            onMouseLeave: (e) => { if (!isAct) e.currentTarget.style.color = "#67707b"; },
            children: tab
          });
        })
      }),

      /* --- 2-COLUMN MAIN BODY LAYOUT --- */
      s.jsxs("div", {
        style: {
          maxWidth: "1120px",
          margin: "0 auto",
          padding: "32px",
          display: "grid",
          gridTemplateColumns: "1fr 300px",
          gap: "32px"
        },
        children: [
          /* LEFT COLUMN: ACTIVITY & PATCH NOTES */
          s.jsxs("div", {
            style: { display: "flex", flexDirection: "column", gap: "24px" },
            children: [
              /* Steam Activity Post Box */
              s.jsxs("div", {
                style: { background: "#161f2c", border: "1px solid rgba(255,255,255,0.06)", borderRadius: "4px", padding: "16px" },
                children: [
                  s.jsx("div", { style: { fontSize: "10px", color: "#67707b", textTransform: "uppercase", letterSpacing: "0.15em", marginBottom: "10px", fontWeight: 700 }, children: "ACTIVITY" }),
                  s.jsx("input", {
                    type: "text",
                    placeholder: "Say something about this game to your occult vessels...",
                    style: {
                      width: "100%",
                      background: "#0b0f14",
                      border: "1px solid rgba(255,255,255,0.1)",
                      borderRadius: "3px",
                      padding: "12px 14px",
                      color: "#c6d4df",
                      fontFamily: H,
                      fontSize: "12px",
                      outline: "none"
                    }
                  })
                ]
              }),

              /* News / Update Card 1 */
              s.jsxs("div", {
                style: { background: "#161f2c", border: "1px solid rgba(255,255,255,0.06)", borderRadius: "4px", overflow: "hidden" },
                children: [
                  s.jsxs("div", {
                    style: { padding: "16px 20px", borderBottom: "1px solid rgba(255,255,255,0.05)", display: "flex", justifyContent: "space-between", alignItems: "center" },
                    children: [
                      s.jsx("div", { style: { fontSize: "9px", color: "#66c0f4", fontWeight: 700, letterSpacing: "0.15em", textTransform: "uppercase" }, children: "AUGUST 3 // PATCH 671341 RELEASED" }),
                      s.jsx("div", { style: { fontSize: "10px", color: "#67707b" }, children: "Official Update" })
                    ]
                  }),
                  s.jsxs("div", {
                    style: { padding: "20px" },
                    children: [
                      s.jsx("h3", { style: { margin: "0 0 10px", fontSize: "16px", color: "#ffffff", fontWeight: 700 }, children: "Full CRT Video Shader & Dual Hand Anchor Synchronization" }),
                      s.jsx("p", { style: { margin: "0 0 14px", fontSize: "12px", lineHeight: "1.6", color: "#acb2b8" }, children: "Updated Sacred Pachinko standalone engine with fixed viewport transparency, edge-locked skeleton hands, and direct CRT video rendering." }),
                      s.jsx("a", { href: "#", onClick: launchGame, style: { fontSize: "11px", color: "#66c0f4", textDecoration: "none", fontWeight: 700 }, children: "Read full patch notes →" })
                    ]
                  })
                ]
              }),

              /* News / Update Card 2 */
              s.jsxs("div", {
                style: { background: "#161f2c", border: "1px solid rgba(255,255,255,0.06)", borderRadius: "4px", overflow: "hidden" },
                children: [
                  s.jsxs("div", {
                    style: { padding: "16px 20px", borderBottom: "1px solid rgba(255,255,255,0.05)", display: "flex", justifyContent: "space-between", alignItems: "center" },
                    children: [
                      s.jsx("div", { style: { fontSize: "9px", color: "#e3b341", fontWeight: 700, letterSpacing: "0.15em", textTransform: "uppercase" }, children: "GHOSTTAIL INSPIRATION // DEV LOG" }),
                      s.jsx("div", { style: { fontSize: "10px", color: "#67707b" }, children: "Community Feature" })
                    ]
                  }),
                  s.jsxs("div", {
                    style: { padding: "20px" },
                    children: [
                      s.jsx("h3", { style: { margin: "0 0 10px", fontSize: "16px", color: "#ffffff", fontWeight: 700 }, children: "Chasing the Vibe: A Possessed Pachinko Machine" }),
                      s.jsx("p", { style: { margin: "0 0 14px", fontSize: "12px", lineHeight: "1.6", color: "#acb2b8" }, children: "Big shout out to ghosttail.com/game — a real inspiration for this whole thing. A possessed pachinko machine, a skeleton behind the glass judging you, tarot cards deciding your fate." }),
                      s.jsx("a", { href: "https://www.ghosttail.com/game/", target: "_blank", rel: "noreferrer", style: { fontSize: "11px", color: "#e3b341", textDecoration: "none", fontWeight: 700 }, children: "Visit ghosttail.com/game →" })
                    ]
                  })
                ]
              })
            ]
          }),

          /* RIGHT COLUMN: FRIENDS WHO PLAY & ACHIVEMENTS */
          s.jsxs("div", {
            style: { display: "flex", flexDirection: "column", gap: "24px" },
            children: [
              /* Friends / Vessels Section */
              s.jsxs("div", {
                style: { background: "#161f2c", border: "1px solid rgba(255,255,255,0.06)", borderRadius: "4px", padding: "20px" },
                children: [
                  s.jsx("div", { style: { fontSize: "10px", color: "#acb2b8", textTransform: "uppercase", letterSpacing: "0.15em", marginBottom: "14px", fontWeight: 700 }, children: "VESSELS WHO PLAY" }),
                  s.jsx("div", { style: { fontSize: "11px", color: "#67707b", marginBottom: "14px" }, children: "4 vessels currently in resonance" }),
                  s.jsx("div", {
                    style: { display: "flex", gap: "10px", flexWrap: "wrap", marginBottom: "16px" },
                    children: [
                      { glyph: "☉", name: "Sun Vessel", bg: "#f5c842" },
                      { glyph: "☽", name: "Moon Vessel", bg: "#c8c8ff" },
                      { glyph: "▲", name: "Rising Vessel", bg: "#ffffff" },
                      { glyph: "👁", name: "Eye Vessel", bg: "#ef4444" }
                    ].map((vessel, idx) => {
                      return s.jsx("div", {
                        key: idx,
                        title: vessel.name,
                        style: {
                          width: "42px",
                          height: "42px",
                          borderRadius: "4px",
                          background: "#0b0f14",
                          border: `1px solid ${vessel.bg}`,
                          display: "flex",
                          alignItems: "center",
                          justifyContent: "center",
                          fontSize: "18px",
                          color: vessel.bg,
                          boxShadow: `0 0 10px ${vessel.bg}33`
                        },
                        children: vessel.glyph
                      });
                    })
                  }),
                  s.jsx("div", { style: { fontSize: "10px", color: "#66c0f4", fontWeight: 700, cursor: "pointer" }, children: "4 vessels have Sacred Pachinko on wishlist" })
                ]
              }),

              /* Unlocked Achievements Section */
              s.jsxs("div", {
                style: { background: "#161f2c", border: "1px solid rgba(255,255,255,0.06)", borderRadius: "4px", padding: "20px" },
                children: [
                  s.jsx("div", { style: { fontSize: "10px", color: "#acb2b8", textTransform: "uppercase", letterSpacing: "0.15em", marginBottom: "12px", fontWeight: 700 }, children: "OCCULT ACHIEVEMENTS" }),
                  s.jsxs("div", { style: { fontSize: "11px", color: "#c6d4df", marginBottom: "12px", display: "flex", justifyContent: "space-between" }, children: [s.jsx("span", { children: "Tarot Conduits Unsealed" }), s.jsx("strong", { style: { color: "#e3b341" }, children: "78 / 78" })] }),
                  s.jsx("div", {
                    style: { width: "100%", height: "6px", background: "#0b0f14", borderRadius: "3px", overflow: "hidden", marginBottom: "16px" },
                    children: s.jsx("div", { style: { width: "100%", height: "100%", background: "linear-gradient(90deg, #e3b341, #5cba02)" } })
                  }),
                  s.jsxs("div", {
                    style: { display: "flex", gap: "8px" },
                    children: ["🎴", "🔥", "🔮", "💀"].map((icon, i) => s.jsx("div", { key: i, style: { width: "36px", height: "36px", background: "#0b0f14", border: "1px solid rgba(255,255,255,0.1)", borderRadius: "3px", display: "flex", alignItems: "center", justifyCenter: "center", fontSize: "16px" }, children: icon }))
                  })
                ]
              })
            ]
          })
        ]
      })
    ]
  });
}"""

print("Steam Pachinko Component JS generated cleanly!")
print("Length:", len(steam_pachinko_code))
