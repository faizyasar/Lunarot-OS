import React, { useState, useEffect } from 'react';
import BlurCarousel, { Slide } from './BlurCarousel';

const ART_IMAGES = [
  // Nigredo
  { path: 'gallery05/57548bff.jpg', collection: 'Nigredo', name: 'To Cry' },
  { path: 'gallery05/0f5815a3.jpg', collection: 'Nigredo', name: 'To Typography' },
  { path: 'gallery05/c5f327f1.jpg', collection: 'Nigredo', name: 'To Framing' },
  { path: 'gallery05/34936b53.jpg', collection: 'Nigredo', name: 'To Mortality' },
  { path: 'gallery05/9c950125.jpg', collection: 'Nigredo', name: 'To Vapourwave' },
  { path: 'gallery13/0d5e1463.jpg', collection: 'Nigredo', name: 'Vapour Cyan' },
  { path: 'gallery13/6cef2a33.jpg', collection: 'Nigredo', name: 'Vapour Discus' },
  { path: 'gallery13/b8fec9ce.jpg', collection: 'Nigredo', name: 'Vapour Glitch Red' },
  { path: 'gallery13/bea76ed4.jpg', collection: 'Nigredo', name: 'Vapour Glitch Cyan' },
  { path: 'gallery13/f0a1c3ec.jpg', collection: 'Nigredo', name: 'Vapour Ghosting Cyan' },
  { path: 'gallery13/7a9e87cc.jpg', collection: 'Nigredo', name: 'Vapour Digital Cyan' },
  { path: 'gallery03/c98f9c89.jpg', collection: 'Nigredo', name: 'Vapour Noir Glam' },
  { path: 'gallery03/99800357.jpg', collection: 'Nigredo', name: 'Vapour Crystal Pepsi' },
  { path: 'gallery03/5d4bee43.jpg', collection: 'Nigredo', name: 'Vapour Cry Digital Red' },
  { path: 'gallery03/572f2553.jpg', collection: 'Nigredo', name: 'Vapour Ghosting' },
  { path: 'gallery03/5a887645.jpg', collection: 'Nigredo', name: 'Vapour Magnum Opus' },
  { path: 'gallery03/ca0c855c.jpg', collection: 'Nigredo', name: 'Vapour Branding Pink' },
  { path: 'gallery03/a66c74fd.jpg', collection: 'Nigredo', name: 'Vapour Branding Red' },

  // Albedo
  { path: 'gallery02/2b0604f2.jpg', collection: 'Albedo', name: 'Ode to Vapour' },
  { path: 'gallery02/b3325c39.jpg', collection: 'Albedo', name: 'Ode to Vapour 2' },
  { path: 'gallery02/4141596c.jpg', collection: 'Albedo', name: 'DEKKARD' },
  { path: 'gallery02/145d50d9.jpg', collection: 'Albedo', name: 'Ode to Cloning' },
  { path: 'gallery02/dcf87c23.jpg', collection: 'Albedo', name: 'Ode to Cloning 2' },
  { path: 'gallery02/930ad96b.jpg', collection: 'Albedo', name: 'Ode to Masks' },
  { path: 'gallery02/a3b5792a.jpg', collection: 'Albedo', name: 'Ode to Framing' },
  { path: 'gallery02/064ac1e7.jpg', collection: 'Albedo', name: 'Pre DEKASUPPLY' },
  { path: 'gallery06/8148de8e.jpg', collection: 'Albedo', name: 'DEKA2020' },
  { path: 'gallery06/c38f7448.jpg', collection: 'Albedo', name: 'French 1' },
  { path: 'gallery06/3e628e3a.jpg', collection: 'Albedo', name: 'French 2' },
  { path: 'gallery06/541004e6.jpg', collection: 'Albedo', name: 'French 3' },
  { path: 'gallery06/d422709f.jpg', collection: 'Albedo', name: 'French 4' },
  { path: 'gallery08/53d1b7e6.jpg', collection: 'Albedo', name: 'Ode to DEKASUPPLY' },
  { path: 'gallery08/0a135617.jpg', collection: 'Albedo', name: 'Conceptual Blue' },
  { path: 'gallery08/e57a74be.jpg', collection: 'Albedo', name: 'Conceptual Cloud' },
  { path: 'gallery08/41b2bac1.jpg', collection: 'Albedo', name: 'Conceptual Light Blue' },
  { path: 'gallery08/6ccc14d0.jpg', collection: 'Albedo', name: 'Ode to Crystallic' },

  // FCC
  { path: 'gallery10/e3c0b30e.jpg', collection: 'FCC', name: 'Ice White Blue Red' },
  { path: 'gallery10/c22c0cab.jpg', collection: 'FCC', name: 'Mocha Conceptuals' },
  { path: 'gallery09/c0691322.jpg', collection: 'FCC', name: 'Conceptuals' },
  { path: 'gallery09/bcdfc23d.jpg', collection: 'FCC', name: 'Conceptuals 2' },
  { path: 'gallery09/ca803bbe.jpg', collection: 'FCC', name: 'Iconographies' },
  { path: 'gallery11/c774b936.jpg', collection: 'FCC', name: 'Conceptuals Orange' },
  { path: 'gallery11/ac652d9a.jpg', collection: 'FCC', name: 'Conceptuals Black Red' },
  { path: 'gallery11/e3fcaabf.jpg', collection: 'FCC', name: 'Matcha' },
  { path: 'gallery07/c440f3db.jpg', collection: 'FCC', name: 'Conceptual Skyline' },
  { path: 'gallery07/62811c57.png', collection: 'FCC', name: 'Conceptual Iconographies' },
  { path: 'gallery12/4c239147.jpg', collection: 'FCC', name: 'Drawing Board' },
  { path: 'gallery12/376931f6.jpg', collection: 'FCC', name: 'Ice White Blue Red AF1' },
  { path: 'gallery12/f0b6b2b9.jpg', collection: 'FCC', name: 'Concept True' },
  { path: 'gallery04/638f1174.jpg', collection: 'FCC', name: 'George with Matcha' },
  { path: 'gallery04/b4b34e13.jpg', collection: 'FCC', name: 'Table of Shirts' },
  { path: 'gallery04/eb365823.jpg', collection: 'FCC', name: 'The Babies' },
  { path: 'gallery04/e8c08175.jpg', collection: 'FCC', name: 'Photoshoot' },

  // Rubedo
  { path: 'gallery14/8ed17327.jpg', collection: 'Rubedo', name: 'Watch The Hands' },
  { path: 'gallery14/39ddc854.jpg', collection: 'Rubedo', name: 'DEKA Midjourney' },
  { path: 'gallery14/a7612c08.jpg', collection: 'Rubedo', name: 'Thorns and Conceptual Upgrade' },
  { path: 'gallery16/1203c165.jpg', collection: 'Rubedo', name: 'Time Clock' },
  { path: 'gallery16/ce7141ae.jpg', collection: 'Rubedo', name: 'Seek Horizon' },
  { path: 'gallery16/84c905c8.jpg', collection: 'Rubedo', name: 'Ruski' },
  { path: 'gallery16/3d0cf2c1.jpg', collection: 'Rubedo', name: 'Angelic Style Change' },
  { path: 'gallery15/c1a3b1e5.jpg', collection: 'Rubedo', name: 'Untitled' },
  { path: 'gallery15/fb99b04d.jpg', collection: 'Rubedo', name: 'Untitled' },
  { path: 'gallery15/154ed624.jpg', collection: 'Rubedo', name: 'Untitled' },
  { path: 'gallery15/7d335e72.jpg', collection: 'Rubedo', name: 'Untitled' },
  { path: 'gallery15/8aae9f53.jpg', collection: 'Rubedo', name: 'Untitled' },
  { path: 'gallery15/36912552.png', collection: 'Rubedo', name: 'Untitled' },
  { path: 'gallery15/d77669d5.jpg', collection: 'Rubedo', name: 'Untitled' },
  { path: 'gallery15/fa9ca73c.jpg', collection: 'Rubedo', name: 'Untitled' }
];

const COLLECTIONS = [
  'ALL',
  'Nigredo',
  'Albedo',
  'FCC',
  'Rubedo'
];

interface AppArtShowcaseProps {
  onContextChange?: (text: string) => void;
}

export default function AppArtShowcase({ onContextChange }: AppArtShowcaseProps) {
  const [selectedCollection, setSelectedCollection] = useState('ALL');
  const [activeIndex, setActiveIndex] = useState(0);
  const [lightboxImg, setLightboxImg] = useState<string | null>(null);
  const [lightboxVisible, setLightboxVisible] = useState(false);

  const filteredImages = selectedCollection === 'ALL'
    ? ART_IMAGES
    : ART_IMAGES.filter(img => img.collection === selectedCollection);

  const mappedSlides: Slide[] = filteredImages.map(img => ({
    image: {
      src: `https://lnrtdka.drr.ac/assets/images/${img.path}`,
      alt: img.name
    },
    title: `${img.name}\n - \n${img.collection}`
  }));

  // Emit contextual active slide text to OS status bar
  useEffect(() => {
    const img = filteredImages[activeIndex];
    if (img && onContextChange) {
      onContextChange(`${img.name.toUpperCase()} // ${img.collection.toUpperCase()}`);
    }
  }, [activeIndex, filteredImages, onContextChange]);

  const handleCollectionChange = (col: string) => {
    setSelectedCollection(col);
    setActiveIndex(0);
  };

  const handleOpenLightbox = (src: string) => {
    setLightboxImg(src);
    setTimeout(() => {
      setLightboxVisible(true);
    }, 10);
  };

  const handleCloseLightbox = () => {
    setLightboxVisible(false);
    setTimeout(() => {
      setLightboxImg(null);
    }, 300);
  };

  return (
    <div className="flex-1 flex flex-col h-full w-full bg-black/35 backdrop-blur-[2px] border border-yellow-950/20 relative z-25 group overflow-hidden shadow-[0_0_20px_rgba(255,255,255,0.02)] p-4 sm:p-6 md:p-8">
      {/* Visual background details */}
      <div className="absolute inset-1.5 border border-dashed border-yellow-950/10 pointer-events-none z-0" />
      
      {/* File tags */}
      <span className="absolute top-2 left-3 font-mono text-[7px] text-[#ffffff]/40 tracking-[0.3em] uppercase pointer-events-none">PORTAL_INGRESS // LUNAROT_DEKA</span>
      <span className="absolute bottom-2 right-3 font-mono text-[6px] text-[#ffffff]/40 tracking-[0.2em] uppercase pointer-events-none">AESTHETIC_CONFLUX</span>

      {/* Header and Motto */}
      <div className="text-center mt-2 mb-6 z-10 select-none">
        <h1 className="text-xl font-bold font-mono tracking-[0.25em] text-[#ffffff] uppercase">LUNAROT DEKA</h1>
        <p className="font-garamond text-xs italic text-[#cfc9c0]/80 mt-1 max-w-[500px] mx-auto">
          "Scientia sicut papilio in lunae splendore vivit in eius defectu moritur"
        </p>
      </div>

      {/* Collection Filters */}
      <div className="flex border-b border-yellow-950/15 mb-6 relative z-10 select-none overflow-x-auto scrollbar-none gap-2 pb-1">
        {COLLECTIONS.map(col => (
          <button
            key={col}
            onClick={() => handleCollectionChange(col)}
            className={`px-3 py-1.5 font-mono text-[9px] sm:text-[10px] tracking-wider uppercase transition-all duration-300 border-b-2 shrink-0 ${
              selectedCollection === col
                ? 'border-[#ffffff] text-[#ffffff] font-bold text-shadow-[0_0_8px_rgba(255,255,255,0.3)]'
                : 'border-transparent text-[#838aa0] hover:text-white'
            }`}
          >
            {col}
          </button>
        ))}
      </div>

      {/* Carousel Container */}
      <div className="flex-1 relative z-10 w-full overflow-hidden border border-yellow-950/15 rounded bg-black/40 flex items-center justify-center">
        <div className="w-full max-w-[640px] aspect-[4/5] flex items-center justify-center p-4">
          <BlurCarousel
            slides={mappedSlides}
            movement="horizontal"
            cardWidth={420}
            cardHeight={480}
            radius={6}
            tilt={15}
            blurAmount={24}
            autoplay={false}
            showTitle={false} // Hidden inside the carousel since titles reside in the contextual footer!
            onIndexChange={setActiveIndex}
            onImageClick={handleOpenLightbox}
          />
        </div>
      </div>

      {/* Lightbox Modal */}
      {lightboxImg && (
        <div 
          className={`fixed inset-0 bg-black/90 z-[9999] flex flex-col items-center justify-center p-4 cursor-zoom-out transition-opacity duration-300 ease-out ${
            lightboxVisible ? 'opacity-100' : 'opacity-0'
          }`}
          onClick={handleCloseLightbox}
        >
          <div 
            className={`relative max-w-full max-h-[90vh] transition-all duration-300 ease-out ${
              lightboxVisible ? 'scale-100 opacity-100' : 'scale-95 opacity-0'
            }`}
          >
            <img 
              src={lightboxImg} 
              alt="Showcase High-Res preview" 
              className="max-w-full max-h-[90vh] object-contain border border-[#ffffff]/20 shadow-2xl rounded"
            />
            <button 
              onClick={handleCloseLightbox}
              className="absolute -top-10 right-0 font-mono text-[10px] text-white/60 hover:text-white tracking-widest uppercase bg-black/55 px-3 py-1.5 border border-white/10 rounded cursor-pointer"
            >
              [ CLOSE ]
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
