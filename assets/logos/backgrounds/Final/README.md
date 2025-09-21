# Final Production Background Images

## Image Inventory

### Desktop Backgrounds
- **hero-bg-desktop.png** - 1920x1080 (Full HD) - Main desktop background
- **hero-bg-desktop-2k.png** - 2560x1440 (2K/QHD) - High-resolution desktop

### Mobile Backgrounds  
- **hero-bg-mobile.png** - 414x896 - Standard mobile portrait
- **hero-bg-mobile-landscape.png** - 896x414 - Mobile landscape orientation
- **hero-bg-mobile-tablet.png** - 768x1024 - Tablet/iPad portrait

## Recommended Usage

```css
/* Desktop (1920x1080 and up) */
@media (min-width: 1024px) {
  .hero-background {
    background-image: url('assets/logos/backgrounds/Final/hero-bg-desktop.png');
  }
}

/* High-res desktop (2K displays) */
@media (min-width: 1920px) and (min-resolution: 2dppx) {
  .hero-background {
    background-image: url('assets/logos/backgrounds/Final/hero-bg-desktop-2k.png');
  }
}

/* Tablet (768px to 1023px) */
@media (min-width: 768px) and (max-width: 1023px) {
  .hero-background {
    background-image: url('assets/logos/backgrounds/Final/hero-bg-mobile-tablet.png');
  }
}

/* Mobile Portrait (up to 767px) */
@media (max-width: 767px) and (orientation: portrait) {
  .hero-background {
    background-image: url('assets/logos/backgrounds/Final/hero-bg-mobile.png');
  }
}

/* Mobile Landscape */
@media (max-width: 767px) and (orientation: landscape) {
  .hero-background {
    background-image: url('assets/logos/backgrounds/Final/hero-bg-mobile-landscape.png');
  }
}
```

## Image Specifications

All images feature:
- Flowing blue, cyan, and purple lines
- Hexagonal network pattern overlay
- Light gray/white background
- Modern tech aesthetic
- Optimized PNG format

## File Sizes
- Desktop: 1.9 MB
- Desktop 2K: 2.8 MB  
- Mobile: 411 KB
- Mobile Landscape: 530 KB
- Tablet: 836 KB