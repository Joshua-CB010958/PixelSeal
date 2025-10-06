Light weight Batch Image Watermaker

Features
- Batch apply a logo (top-left) and a watermark (bottom-center)
- Adjustable size sliders for logo and watermark
- Supports PNG, JPG/JPEG, and now HEIC/HEIF (via pillow-heif)

Setup
1) Install Python 3.9+ on Windows and ensure "Add Python to PATH" is selected.
2) Run `install_dependencies.bat` to install required packages, including HEIC support.

Usage
- Launch `PixelSeal/Main/PixelSeal.bat` to start the app.
- Select a watermark and/or logo image.
- Select one or more images to process (PNG/JPEG/HEIC supported).
- Choose an output folder. HEIC/HEIF inputs will be saved as `.jpg` for broad compatibility.

Notes
- HEIC/HEIF support is provided by the pillow-heif package. If you still can't open HEIC files, re-run `install_dependencies.bat` or update Python/Pip.
