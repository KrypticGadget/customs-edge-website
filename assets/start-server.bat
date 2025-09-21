@echo off
echo Starting local web server for Asset Viewer...
echo.
echo The asset viewer will open at: http://localhost:8000/asset-viewer.html
echo.
echo Press Ctrl+C to stop the server when done.
echo.
python -m http.server 8000
pause