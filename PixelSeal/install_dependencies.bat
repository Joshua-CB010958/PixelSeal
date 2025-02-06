@echo off
:: Check if python is installed
python --version
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python first.
    exit /b
)

:: Upgrade pip to the latest version
python -m pip install --upgrade pip

:: Install Pillow (for image processing)
pip install pillow

:: Install tkinter (if not already installed, but usually included with Python)
pip install tk

:: Optionally, if you need any other dependencies, you can add them here
:: pip install other-dependency

:: Run your Python script
python your_script_name.py

echo Dependencies installed and script executed successfully.
pause
