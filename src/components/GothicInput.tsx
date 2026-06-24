import React, { InputHTMLAttributes, SelectHTMLAttributes } from 'react';

interface BaseInputProps {
  label: string;
  prefixSymbol?: string;
}

// Gothic Text Input
export interface GothicTextInputProps
  extends Omit<InputHTMLAttributes<HTMLInputElement>, 'type'>,
    BaseInputProps {}

export function GothicTextInput({
  label,
  prefixSymbol = '◆',
  className = '',
  ...props
}: GothicTextInputProps) {
  return (
    <div className={`flex flex-col gap-1 w-full font-mono text-[8px] tracking-[0.15em] ${className}`}>
      <div className="flex justify-between text-[7px] text-white/40 font-bold uppercase select-none pb-1 border-b border-white/10">
        <span>{prefixSymbol} {label}</span>
      </div>
      <div className="flex items-center justify-between py-2 border-b border-white-[0.03]">
        <span className="text-white/40 font-bold select-none text-[7px]">TOKEN_ID :</span>
        <input
          type="text"
          className="bg-transparent border-none text-right font-mono text-[8.5px] text-white placeholder-white/20 focus:outline-none select-text cursor-text uppercase tracking-widest w-40"
          {...props}
        />
      </div>
    </div>
  );
}

// Gothic Date Input with optional zodiac glyph calculation preview
export interface GothicDateInputProps
  extends Omit<InputHTMLAttributes<HTMLInputElement>, 'type'>,
    BaseInputProps {
  zodiacGlyph?: string;
}

export function GothicDateInput({
  label,
  prefixSymbol = '◆',
  zodiacGlyph,
  className = '',
  ...props
}: GothicDateInputProps) {
  return (
    <div className={`flex flex-col gap-1 w-full font-mono text-[8px] tracking-[0.15em] ${className}`}>
      <div className="flex justify-between text-[7px] text-white/40 font-bold uppercase select-none pb-1 border-b border-white/10">
        <span>{prefixSymbol} {label}</span>
      </div>
      <div className="flex items-center justify-between py-2 border-b border-white-[0.03]">
        <span className="text-white/40 font-bold select-none text-[7px]">SOLAR_EPOCH :</span>
        <div className="flex items-center justify-end gap-1.5">
          <input
            type="date"
            className="bg-transparent border-none text-right font-mono text-[8.5px] text-white focus:outline-none select-text cursor-text w-28 uppercase tracking-widest"
            style={{ colorScheme: 'dark' }}
            {...props}
          />
          {zodiacGlyph && (
            <span className="text-white/70 select-none text-[8px] w-6 text-center">
              {zodiacGlyph}
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

// Gothic Time Input
export interface GothicTimeInputProps
  extends Omit<InputHTMLAttributes<HTMLInputElement>, 'type'>,
    BaseInputProps {
  timeGlyph?: string;
}

export function GothicTimeInput({
  label,
  prefixSymbol = '◆',
  timeGlyph = '☀',
  className = '',
  ...props
}: GothicTimeInputProps) {
  return (
    <div className={`flex flex-col gap-1 w-full font-mono text-[8px] tracking-[0.15em] ${className}`}>
      <div className="flex justify-between text-[7px] text-white/40 font-bold uppercase select-none pb-1 border-b border-white/10">
        <span>{prefixSymbol} {label}</span>
      </div>
      <div className="flex items-center justify-between py-2">
        <span className="text-white/40 font-bold select-none text-[7px]">TEMP_AXIS :</span>
        <div className="flex items-center justify-end gap-1.5">
          <input
            type="time"
            className="bg-transparent border-none text-right font-mono text-[8.5px] text-white focus:outline-none select-text cursor-text w-20 tracking-widest"
            style={{ colorScheme: 'dark' }}
            {...props}
          />
          <span className="text-white/70 select-none text-[8px] w-6 text-center">
            {timeGlyph}
          </span>
        </div>
      </div>
    </div>
  );
}

// Gothic Select Dropdown Input
export interface GothicSelectProps
  extends SelectHTMLAttributes<HTMLSelectElement>,
    BaseInputProps {
  options: { value: string; label: string }[];
  placeholder?: string;
}

export function GothicSelect({
  label,
  prefixSymbol = '◆',
  options,
  placeholder,
  className = '',
  ...props
}: GothicSelectProps) {
  return (
    <div className={`flex flex-col gap-1 w-full font-mono text-[8px] tracking-[0.15em] ${className}`}>
      <div className="flex justify-between text-[7px] text-white/40 font-bold uppercase select-none pb-1 border-b border-white/10">
        <span>{prefixSymbol} {label}</span>
      </div>
      <div className="flex items-center justify-between py-2 border-b border-white-[0.03]">
        <span className="text-white/40 font-bold select-none text-[7px]">SELECT_VAL :</span>
        <select
          className="bg-black border border-white/10 text-right font-mono text-[8.5px] text-white focus:outline-none select-text cursor-pointer w-40 uppercase tracking-widest"
          {...props}
        >
          {placeholder && <option value="">{placeholder}</option>}
          {options.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
}
