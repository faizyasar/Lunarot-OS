import React from 'react';

interface GothicPanelProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: 'gold' | 'white';
  titleTag?: string;
  footerTag?: string;
  doubleRim?: boolean;
}

export default function GothicPanel({
  children,
  variant = 'gold',
  titleTag,
  footerTag,
  doubleRim = true,
  className = '',
  ...props
}: GothicPanelProps) {
  const borderStyle =
    variant === 'gold'
      ? 'border border-[var(--gold)]/45 shadow-[0_0_15px_rgba(200,164,90,0.08)]'
      : 'border border-[#efede8]/55 shadow-[0_0_20px_rgba(255,255,255,0.05)]';

  const innerRim = doubleRim
    ? variant === 'gold'
      ? 'before:content-[""] before:absolute before:inset-[6px] before:border before:border-[var(--gold)]/15 before:border-dashed before:pointer-events-none before:rounded-[3px]'
      : 'before:content-[""] before:absolute before:inset-[6px] before:border before:border-[#efede8]/15 before:border-dashed before:pointer-events-none before:rounded-[3px]'
    : '';

  return (
    <div
      className={`relative p-6 bg-black/45 backdrop-blur-[3px] rounded-none ${borderStyle} ${innerRim} ${className}`}
      {...props}
    >
      {titleTag && (
        <span className="absolute top-2 left-3 font-mono text-[7px] text-white/30 tracking-[0.3em] uppercase select-none pointer-events-none">
          [ {titleTag} ]
        </span>
      )}
      
      <div className="w-full h-full relative z-10">
        {children}
      </div>

      {footerTag && (
        <span className="absolute bottom-2 right-3 font-mono text-[6px] text-white/30 tracking-[0.2em] uppercase select-none pointer-events-none">
          // {footerTag} //
        </span>
      )}
    </div>
  );
}
