# Asset Viewer - Usage Instructions

## Quick Start

### Option 1: Direct Opening (Limited PDF Export)
Simply double-click `asset-viewer.html` to open it in your browser.
- ✅ All assets will display correctly in the viewer
- ⚠️ PDF export will show placeholders instead of actual images (due to browser security)

### Option 2: Local Web Server (Full Features)
For full PDF export functionality with images, serve the file via a local web server:

#### Python (if installed):
```bash
cd assets
python -m http.server 8000
# Then open: http://localhost:8000/asset-viewer.html
```

#### Node.js (if installed):
```bash
cd assets  
npx http-server -p 8000
# Then open: http://localhost:8000/asset-viewer.html
```

#### Windows Users:
Double-click `start-server.bat` (requires Python)

#### VS Code Users:
Use the "Live Server" extension and right-click on `asset-viewer.html` → "Open with Live Server"

## Features

### Asset Viewer
- **Visual Grid**: Browse all assets with thumbnails
- **Search**: Filter assets by name or type
- **Categories**: Navigate by asset categories (Favicons, Logos, SVG, etc.)
- **Lightbox**: Click any asset for full-size preview
- **Quick Actions**: Copy path or download individual assets

### PDF Export
- **Export All Assets**: Creates a professional PDF catalog
- **Visual Layout**: 3×4 grid of asset thumbnails per page
- **Organized**: Assets grouped by category
- **Metadata**: Includes filenames, types, and sizes

## Why Use a Web Server?

Modern browsers restrict local file access for security (CORS policy). When you open HTML files directly (file:// protocol), JavaScript cannot load local images into the PDF generator.

Using a web server (http://localhost) bypasses these restrictions, allowing full image rendering in PDFs.

## Troubleshooting

### "Image Load Error" in PDF
This is expected when opening the file directly. Use one of the web server methods above.

### Assets Not Showing in Viewer
- Check that asset files are in the correct folders
- Verify file paths match the structure in the HTML

### PDF Generation Fails
- Ensure you have a stable internet connection (for loading jsPDF library)
- Try using a different browser (Chrome/Edge recommended)

## Asset Structure
```
assets/
├── logos/
│   ├── favicon/
│   ├── original/
│   ├── social/
│   ├── svg/
│   └── web/optimized/
├── video/
├── asset-viewer.html (this viewer)
├── start-server.bat (Windows helper)
└── README-AssetViewer.md (this file)
```