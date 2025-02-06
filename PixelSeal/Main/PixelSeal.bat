@echo off
:: Check if python is installed
python --version
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b
)

:: Run the Python script and minimize the CMD window
start /min python PixelSeal.py
