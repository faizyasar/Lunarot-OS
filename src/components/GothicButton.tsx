import { ButtonHTMLAttributes } from 'react';

interface GothicButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary';
  fullWidth?: boolean;
}

export default function GothicButton({
  children,
  variant = 'primary',
  fullWidth = false,
  className = '',
  ...props
}: GothicButtonProps) {
  const baseStyle =
    'px-6 py-2.5 text-[8.5px] md:text-[9.5px] font-mono font-bold uppercase tracking-[0.25em] transition-all duration-300 rounded-none cursor-pointer focus:outline-none disabled:opacity-50 disabled:cursor-not-allowed';

  const variantStyles = {
    primary:
      'border border-white bg-white text-black hover:bg-black hover:text-white hover:border-white shadow-[0_0_0px_transparent] hover:shadow-[0_0_15px_rgba(255,255,255,0.4)]',
    secondary:
      'border border-[var(--gold)] bg-black/60 text-[var(--gold)] hover:text-white hover:border-white hover:shadow-[0_0_12px_rgba(200,164,90,0.4)]',
  };

  const widthStyle = fullWidth ? 'w-full' : 'inline-block';

  return (
    <button
      className={`${baseStyle} ${variantStyles[variant]} ${widthStyle} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
}
