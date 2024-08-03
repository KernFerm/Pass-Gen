@echo off
setlocal

:: Check for Python installation
echo Checking for Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python before running this script.
    pause
    exit /b 1
)

:: Check for pip installation
echo Checking for pip installation...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --upgrade
    if %errorlevel% neq 0 (
        echo Failed to install pip. Please install pip manually.
        pause
        exit /b 1
    )
)

:: Create a virtual environment
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Failed to create virtual environment. Please check your Python installation.
    pause
    exit /b 1
)

:: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment. Please check your virtual environment setup.
    pause
    exit /b 1
)

:: Install cryptography
echo Installing cryptography...
pip install cryptography
if %errorlevel% neq 0 (
    echo Failed to install cryptography. Please check your internet connection and pip configuration.
    pause
    exit /b 1
)

echo cryptography has been successfully installed in the virtual environment.
pause

endlocal
