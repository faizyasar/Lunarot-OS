import React, { useRef, useEffect, useState, useMemo } from 'react';

interface OptionWheelProps<T> {
  items: T[];
  renderItem: (item: T, isSelected: boolean) => React.ReactNode;
  onSelect: (item: T) => void;
  selectedItem: T;
  itemHeight?: number;
  radius?: number;
  activeColor?: string;
  inactiveColor?: string;
}

export default function OptionWheel<T>({ 
  items, 
  renderItem, 
  onSelect, 
  selectedItem, 
  itemHeight = 64,
  radius = 250,
}: OptionWheelProps<T>) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [scrollY, setScrollY] = useState(0);
  const [isScrolling, setIsScrolling] = useState(false);
  const scrollTimeout = useRef<any>(null);
  
  const isInternalScroll = useRef(false);

  // Virtual multiplier for infinite scrolling
  const MULTIPLIER = 1000;
  const virtualCount = items.length * MULTIPLIER;
  const centerOffset = useMemo(() => Math.floor(MULTIPLIER / 2) * items.length, [items.length]);

  // Initialize scroll position to selected item
  useEffect(() => {
    if (containerRef.current && items.length > 0) {
      const index = items.indexOf(selectedItem);
      if (index !== -1) {
        const virtualIndex = centerOffset + index;
        containerRef.current.scrollTop = virtualIndex * itemHeight;
        setScrollY(virtualIndex * itemHeight);
      }
    }
  }, [items, itemHeight, centerOffset]); // Note: running when items change or mount

  useEffect(() => {
    let frameId: number;
    const handleScroll = () => {
      if (frameId) {
        cancelAnimationFrame(frameId);
      }
      frameId = requestAnimationFrame(() => {
        if (containerRef.current) {
          setScrollY(containerRef.current.scrollTop);
        }
      });

      setIsScrolling(true);
      clearTimeout(scrollTimeout.current);
      scrollTimeout.current = setTimeout(() => {
        setIsScrolling(false);
        // snap to nearest item
        if (containerRef.current) {
          const nearestVirtualIndex = Math.max(0, Math.min(virtualCount - 1, Math.round(containerRef.current.scrollTop / itemHeight)));
          
          isInternalScroll.current = true;
          containerRef.current.scrollTo({
            top: nearestVirtualIndex * itemHeight,
            behavior: 'smooth'
          });
          
          setTimeout(() => {
             isInternalScroll.current = false;
          }, 300);

          const actualIndex = nearestVirtualIndex % items.length;
          const safeIndex = (actualIndex + items.length) % items.length;
          if (items[safeIndex] && items[safeIndex] !== selectedItem) {
             onSelect(items[safeIndex]);
          }
        }
      }, 150);
    };

    const container = containerRef.current;
    if (container) {
      container.addEventListener('scroll', handleScroll, { passive: true });
    }
    return () => {
      if (container) container.removeEventListener('scroll', handleScroll);
      if (frameId) cancelAnimationFrame(frameId);
      clearTimeout(scrollTimeout.current);
    };
  }, [items, selectedItem, itemHeight, onSelect, virtualCount]);

  // Sync scroll when selectedItem changes from outside (e.g. keyboard)
  useEffect(() => {
    if (!isScrolling && !isInternalScroll.current && containerRef.current) {
       const index = items.indexOf(selectedItem);
       if (index !== -1) {
          // Find the closest virtual index for this item
          const currentVirtualCenter = containerRef.current.scrollTop / itemHeight;
          const currentActualIndex = (Math.round(currentVirtualCenter) % items.length + items.length) % items.length;
          
          let diff = index - currentActualIndex;
          
          // Shortcut to scroll the shortest distance
          if (diff > items.length / 2) diff -= items.length;
          if (diff < -items.length / 2) diff += items.length;
          
          const targetVirtualIndex = Math.round(currentVirtualCenter) + diff;
          const targetY = targetVirtualIndex * itemHeight;
          
          if (Math.abs(containerRef.current.scrollTop - targetY) > 5) {
             isInternalScroll.current = true;
             containerRef.current.scrollTo({
               top: targetY,
               behavior: 'smooth'
             });
             setTimeout(() => {
                 isInternalScroll.current = false;
             }, 300);
          }
       }
    }
  }, [selectedItem, items, itemHeight, isScrolling]);
  
  if (items.length === 0) return null;

  // Render a fixed number of items around the current scroll position
  const currentVirtualCenter = scrollY / itemHeight;
  const centerIndex = Math.floor(currentVirtualCenter);
  const itemsToRender = 19; // Must be odd to be symmetric
  const halfRender = Math.floor(itemsToRender / 2);

  const visibleItems = [];
  for (let i = -halfRender; i <= halfRender; i++) {
    const offsetIndex = centerIndex + i;
    const actualIndex = (offsetIndex % items.length + items.length) % items.length;
    const item = items[actualIndex];
    if (item) {
        visibleItems.push({
            offsetIndex,
            actualIndex,
            item
        });
    }
  }

  return (
    <div className="relative w-full h-full flex items-center justify-center overflow-hidden" style={{ perspective: '1000px' }}>
      
      {/* The invisible native scroll container */}
      <div 
        ref={containerRef}
        className="absolute inset-0 z-20 overflow-y-auto scrollbar-hide"
        style={{
          paddingTop: `calc(50% - ${itemHeight / 2}px)`,
          paddingBottom: `calc(50% - ${itemHeight / 2}px)`,
        }}
      >
        <div style={{ height: `${virtualCount * itemHeight}px` }} />
      </div>

      {/* The visual 3D wheel */}
      <div className="absolute inset-0 pointer-events-none flex items-center justify-center z-10" style={{ transformStyle: 'preserve-3d' }}>
        {visibleItems.map(({ offsetIndex, actualIndex, item }) => {
          const relativeOffset = offsetIndex - currentVirtualCenter;
          
          // Control the curvature of the cylinder
          const angle = relativeOffset * 22;
          const clampedAngle = Math.max(-85, Math.min(85, angle));
          const angleRad = (clampedAngle * Math.PI) / 180;
          
          const translateY = radius * Math.sin(angleRad);
          const translateZ = radius * Math.cos(angleRad) - radius;
          const rotateX = -clampedAngle;
          
          // Calculate opacity: full opacity at center, fades out at edges
          const opacity = 1 - Math.pow(Math.abs(clampedAngle) / 80, 2);
          const isSelected = item === selectedItem;

          if (opacity < 0.01) return null;

          return (
            <div
              key={offsetIndex}
              className="absolute w-full px-4 origin-center pointer-events-auto flex items-center"
              style={{
                height: `${itemHeight}px`,
                transform: `translateY(${translateY}px) translateZ(${translateZ}px) rotateX(${rotateX}deg)`,
                opacity: Math.max(0, opacity),
                zIndex: Math.round(100 - Math.abs(clampedAngle)),
                willChange: 'transform, opacity'
              }}
              onClick={() => {
                if (containerRef.current) {
                  containerRef.current.scrollTo({
                    top: offsetIndex * itemHeight,
                    behavior: 'smooth'
                  });
                  onSelect(item);
                }
              }}
            >
              <div className="w-full h-full flex items-center">
                {renderItem(item, isSelected)}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
