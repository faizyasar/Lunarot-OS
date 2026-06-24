import { useState } from 'react';

interface InteractiveTextProps {
  text: string;
  className?: string;
  hoverClassName?: string;
}

export default function InteractiveText({ text, className = '', hoverClassName = '' }: InteractiveTextProps) {
  return (
    <span className={`inline-block select-none ${className}`}>
      {text.split('').map((char, index) => {
        // Render spaces nicely
        if (char === ' ') {
          return <span key={index} className="inline-block">&nbsp;</span>;
        }
        return (
          <span
            key={index}
            className={`inline-block transition-all duration-300 transform hover:scale-[1.35] hover:text-[#c8a45a] hover:-translate-y-1.5 hover:rotate-[6deg] cursor-default active:scale-90 ${hoverClassName}`}
            style={{
              transitionTimingFunction: 'cubic-bezier(0.25, 1, 0.5, 1.1)'
            }}
          >
            {char}
          </span>
        );
      })}
    </span>
  );
}
