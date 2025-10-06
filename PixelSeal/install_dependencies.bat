@echo off
:: Check if python is installed
python --version
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python first.
    exit /b
)

:: Upgrade pip to the latest version
python -m pip install --upgrade pip

:: Install Pillow (for image processing) and HEIC/HEIF support
python -m pip install --upgrade pillow pillow-heif

:: Install tkinter (if not already installed, but usually included with Python)
python -m pip install tk

:: Optionally, if you need any other dependencies, you can add them here
:: pip install other-dependency

echo Dependencies installed successfully.
pause
