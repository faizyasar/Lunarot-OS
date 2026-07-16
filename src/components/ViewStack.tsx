import React, { useState, useEffect } from "react"
import { motion, PanInfo } from "motion/react"

const PERSPECTIVE = 1000 // px
const DEPTH_SPACING = 40 // px

export function ViewStack({ views, cardWidth = 900, cardHeight = 650 }: { views: React.ReactNode[], cardWidth?: number, cardHeight?: number }) {
    const actualCardCount = views.length;

    const [cards, setCards] = useState(() =>
        Array.from({ length: actualCardCount }, (_, i) => ({
            id: i,
            content: views[i],
            originalIndex: i,
        }))
    )

    useEffect(() => {
        if (cards.length > 0) {
            const topCard = cards[0];
            window.dispatchEvent(
                new CustomEvent("top-card-changed", {
                    detail: { originalIndex: topCard.originalIndex },
                })
            );
        }
    }, [cards]);

    useEffect(() => {
        const handleCardChange = (e: any) => {
            const cardId = e.detail?.cardId;
            setCards((prevCards) => {
                const idx = prevCards.findIndex(c => c.originalIndex === cardId);
                if (idx !== -1 && idx !== 0) {
                    const selected = prevCards[idx];
                    const remaining = prevCards.filter((_, i) => i !== idx);
                    return [selected, ...remaining];
                }
                return prevCards;
            });
        };
        window.addEventListener("change-card", handleCardChange);
        return () => window.removeEventListener("change-card", handleCardChange);
    }, []);

    const [isPressed, setIsPressed] = useState(false)
    const [shouldReturnToCenter, setShouldReturnToCenter] = useState(false)

    const handlePointerDown = () => setIsPressed(true)
    const handlePointerUp = () => setIsPressed(false)

    const swipeThreshold = 50
    const tiltAngleStart = 0
    const tiltAngle = -3
    const xOffset = 30

    const handleDragEnd = (info: PanInfo) => {
        setIsPressed(false)
        const { offset } = info
        const distance = Math.sqrt(offset.x * offset.x + offset.y * offset.y)
        if (distance > swipeThreshold) {
            setCards((prevCards) => {
                const [topCard, ...restCards] = prevCards
                return [...restCards, topCard]
            })
        } else {
            setShouldReturnToCenter(true)
            setTimeout(() => setShouldReturnToCenter(false), 1000)
        }
    }

    const transition = { type: "spring" as const, stiffness: 60, damping: 20, mass: 1.5 }

    const getCardStyle = (index: number) => {
        const totalCards = cards.length
        const stackOffset = index * 12
        const scaleValue = 1 - index * 0.04
        const rotationValue =
            totalCards > 1
                ? tiltAngleStart +
                  (index / (totalCards - 1)) * (tiltAngle - tiltAngleStart)
                : tiltAngleStart
        const xOffsetValue =
            totalCards > 1 ? (index / (totalCards - 1)) * xOffset : 0
        const depthOffset = index * DEPTH_SPACING
        const isTopCard = index === 0
        const shouldReturn = isTopCard && shouldReturnToCenter

        return {
            zIndex: cards.length - index,
            scale: scaleValue,
            x: shouldReturn ? 0 : xOffsetValue,
            y: shouldReturn ? 0 : -stackOffset,
            rotate: shouldReturn ? 0 : rotationValue,
            z: -depthOffset,
            opacity: 1 - index * 0.15,
        }
    }

    return (
        <div
            style={{
                width: "100%",
                height: "100%",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                position: "relative",
                perspective: `${PERSPECTIVE}px`,
            }}
        >
            <div
                style={{
                    position: "relative",
                    width: "100%",
                    maxWidth: cardWidth,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                }}
            >
                {cards.map((card, index) => {
                    const isTopCard = index === 0
                    const cardStyle = getCardStyle(index)

                    return (
                        <motion.div
                            key={card.id}
                            drag={isTopCard ? true : false}
                            dragConstraints={false}
                            dragElastic={1}
                            dragMomentum={true}
                            onMouseDown={isTopCard ? handlePointerDown : undefined}
                            onMouseUp={isTopCard ? handlePointerUp : undefined}
                            onDragEnd={isTopCard ? (_: any, info: any) => handleDragEnd(info) : undefined}
                            animate={cardStyle}
                            transition={{
                                x: transition,
                                y: transition,
                                rotate: transition,
                                scale: transition,
                                zIndex: { duration: 0.5, ease: "easeOut" },
                                z: { duration: 0.5, ease: "easeOut" },
                            }}
                            whileDrag={{
                                scale: 1.05,
                                rotate: tiltAngleStart,
                                zIndex: 1000,
                                cursor: "grabbing"
                            }}
                            style={{
                                position: "absolute",
                                width: "100%",
                                display: "flex",
                                alignItems: "center",
                                justifyContent: "center",
                                cursor: isTopCard ? (isPressed ? "grabbing" : "grab") : "default",
                                userSelect: "none",
                                pointerEvents: isTopCard ? "auto" : "none",
                            }}
                        >
                            <div 
                                style={{ width: '100%', pointerEvents: isTopCard ? "auto" : "none" }}
                                onPointerDown={(e) => {
                                    // Stop propagation if we are clicking inside a scrollable area, 
                                    // or input elements so they don't trigger drag
                                    if ((e.target as HTMLElement).tagName === 'INPUT' || (e.target as HTMLElement).tagName === 'SELECT' || (e.target as HTMLElement).tagName === 'BUTTON') {
                                        e.stopPropagation();
                                    }
                                }}
                            >
                                {card.content}
                            </div>
                        </motion.div>
                    )
                })}
            </div>
        </div>
    )
}
