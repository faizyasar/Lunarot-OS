import { useEffect, useRef, useState } from "react"

const COMPONENT_DEFAULTS = {
    characters: " .:-+*=%@#",
    elementSize: 14,
    color: "rgba(200, 164, 90, 0.15)", // Modified to match the theme
    direction: "left",
    background: "transparent",
    invert: false,
    fontWeight: "400",
    speed: 15,
    waveTension: 5,
    noiseScale: 12,
    intensity: 10,
    hasCursorInteraction: false,
    interactionIntensity: 15,
    interactionRadius: 200,
}

export function ASCIIWaves(props: any) {
    props = { ...COMPONENT_DEFAULTS, ...props }
    const {
        characters,
        elementSize,
        color,
        direction,
        background,
        invert,
        waveTension,
        speed,
        noiseScale,
        intensity,
        hasCursorInteraction,
        interactionIntensity,
        interactionRadius,
        fontWeight,
        style,
    } = props

    const containerRef = useRef<HTMLDivElement>(null)
    const canvasRef = useRef<HTMLCanvasElement>(null)
    const rafRef = useRef(0)
    const startRef = useRef(performance.now())
    const pointerRef = useRef({ x: -9999, y: -9999, active: false })
    const [size, setSize] = useState({ w: 0, h: 0 })
    const isStatic = false

    const rampArr = (
        characters && characters.length > 0 ? characters : " .:-+*=%@#"
    )
        .split("")
        [invert ? "reverse" : "slice"]()
        .join("")

    useEffect(() => {
        if (!containerRef.current) return
        const el = containerRef.current
        const ro = new ResizeObserver((entries) => {
            for (const entry of entries) {
                const cr = entry.contentRect
                setSize({
                    w: Math.max(1, Math.floor(cr.width)),
                    h: Math.max(1, Math.floor(cr.height)),
                })
            }
        })
        ro.observe(el)
        return () => ro.disconnect()
    }, [])

    useEffect(() => {
        if (!hasCursorInteraction || isStatic) return
        const el = containerRef.current
        if (!el) return
        const onMove = (e: PointerEvent) => {
            const rect = el.getBoundingClientRect()
            pointerRef.current = {
                x: e.clientX - rect.left,
                y: e.clientY - rect.top,
                active: true,
            }
        }
        const onLeave = () => {
            pointerRef.current.active = false
        }
        window.addEventListener("pointermove", onMove as any)
        window.addEventListener("pointerleave", onLeave)
        return () => {
            window.removeEventListener("pointermove", onMove as any)
            window.removeEventListener("pointerleave", onLeave)
        }
    }, [hasCursorInteraction, isStatic])

    useEffect(() => {
        const canvas = canvasRef.current
        if (!canvas) return
        const ctx = canvas.getContext("2d")
        if (!ctx) return

        const dpr = Math.max(
            1,
            Math.min(
                2,
                typeof window !== "undefined" ? window.devicePixelRatio || 1 : 1
            )
        )
        const { w, h } = size
        if (w === 0 || h === 0) return

        canvas.width = Math.floor(w * dpr)
        canvas.height = Math.floor(h * dpr)
        canvas.style.width = `${w}px`
        canvas.style.height = `${h}px`
        ctx.scale(dpr, dpr)

        const speedVal = speed / 20
        const tensionVal = waveTension / 10
        const twistVal = 0.1
        const scaleVal = noiseScale / 100
        const intensityVal = intensity / 10
        const cursorForceVal = interactionIntensity / 10

        const driftMap = {
            left: [1, 0],
            right: [-1, 0],
            top: [0, 1],
            bottom: [0, -1],
        }
        const [driftX, driftY] =
            driftMap[direction as keyof typeof driftMap] || driftMap.left
        const driftRate = 1.5

        const cell = Math.max(4, elementSize)
        const colStep = cell * 0.6
        const cols = Math.ceil(w / colStep) + 1
        const rows = Math.ceil(h / cell) + 1

        ctx.font = `${fontWeight} ${cell}px ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
        ctx.textBaseline = "top"
        ctx.textAlign = "left"

        // Cache characters on offscreen canvases to avoid expensive ctx.fillText
        const charCache: Record<string, HTMLCanvasElement> = {}
        const getCharCanvas = (ch: string) => {
            if (charCache[ch]) return charCache[ch]
            const charCanvas = document.createElement("canvas")
            charCanvas.width = Math.ceil(cell)
            charCanvas.height = Math.ceil(cell)
            const charCtx = charCanvas.getContext("2d")
            if (charCtx) {
                charCtx.font = ctx.font
                charCtx.textBaseline = "top"
                charCtx.textAlign = "left"
                charCtx.fillStyle = color
                charCtx.fillText(ch, 0, 0)
            }
            charCache[ch] = charCanvas
            return charCanvas
        }

        const rampMax = rampArr.length - 1
        const interactionRadiusSq = interactionRadius * interactionRadius

        const draw = (now: number) => {
            const t = ((now - startRef.current) / 1000) * speedVal
            ctx.clearRect(0, 0, w, h)
            if (background !== "transparent") {
                ctx.fillStyle = background
                ctx.fillRect(0, 0, w, h)
            }

            const p = pointerRef.current
            const ox = t * driftRate * driftX
            const oy = t * driftRate * driftY

            // Precompute row factors to avoid Math.sin inside nested loop
            const rowSin = new Float32Array(rows)
            const rowPy = new Float32Array(rows)
            for (let j = 0; j < rows; j++) {
                rowSin[j] = Math.sin((j + t) * twistVal) * 2
                rowPy[j] = j * cell
            }

            // Precompute col factors to avoid Math.cos inside nested loop
            const colCos = new Float32Array(cols)
            const colPx = new Float32Array(cols)
            for (let i = 0; i < cols; i++) {
                colCos[i] = Math.cos((i + t) * twistVal) * 2
                colPx[i] = i * colStep
            }

            const nt = t * tensionVal
            const nt_07 = nt * 0.7
            const nt_05 = nt * 0.5
            const nt_03 = nt * 0.3
            const t_4 = t * 4

            const noise = (x: number, y: number) => {
                const a = Math.sin(x * 1.3 + nt) * Math.cos(y * 1.1 - nt_07)
                const b = Math.sin((x + y) * 0.7 + nt_05)
                const c = Math.sin(x * 0.4 - y * 0.6 + nt_03)
                return (a + b + c) / 3
            }

            for (let j = 0; j < rows; j++) {
                const py = rowPy[j]
                const sinVal = rowSin[j]
                const yScale = j * scaleVal + oy

                for (let i = 0; i < cols; i++) {
                    const px = colPx[i]
                    const cosVal = colCos[i]
                    const nx = i * scaleVal + ox + sinVal
                    const ny = yScale + cosVal
                    let v = noise(nx, ny)

                    if (hasCursorInteraction && p.active) {
                        const dx = px - p.x
                        const dy = py - p.y
                        const dSq = dx * dx + dy * dy
                        if (dSq < interactionRadiusSq) {
                            const d = Math.sqrt(dSq)
                            const falloff = 1 - d / interactionRadius
                            v +=
                                Math.sin(d * 0.08 - t_4) *
                                falloff *
                                cursorForceVal
                        }
                    }

                    const norm = Math.max(
                        0,
                        Math.min(1, (v * intensityVal + 1) / 2)
                    )
                    const ch = rampArr.charAt(Math.round(norm * rampMax))
                    if (ch !== " ") {
                        ctx.drawImage(getCharCanvas(ch), px, py)
                    }
                }
            }
        }

        if (isStatic) {
            draw(startRef.current + 1000)
            return
        }

        let lastUpdate = 0
        const fpsInterval = 1000 / 30 // Target 30 FPS to reduce CPU footprint

        const loop = (now: number) => {
            rafRef.current = requestAnimationFrame(loop)
            const elapsed = now - lastUpdate
            if (elapsed < fpsInterval) return
            lastUpdate = now - (elapsed % fpsInterval)
            draw(now)
        }
        rafRef.current = requestAnimationFrame(loop)
        return () => cancelAnimationFrame(rafRef.current)
    }, [
        size,
        elementSize,
        color,
        direction,
        background,
        rampArr,
        waveTension,
        speed,
        noiseScale,
        intensity,
        hasCursorInteraction,
        interactionIntensity,
        interactionRadius,
        fontWeight,
        isStatic,
    ])

    return (
        <div
            ref={containerRef}
            style={{
                ...style,
                position: "fixed",
                inset: 0,
                zIndex: 0,
                overflow: "hidden",
                background,
                width: "100%",
                height: "100%",
                pointerEvents: "none",
            }}
        >
            <canvas ref={canvasRef} style={{ display: "block" }} />
        </div>
    )
}
