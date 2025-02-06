@echo off
setlocal
set folder=%~dp0

echo Are you sure you want to delete the folder and everything inside? (Y/N)
set /p confirm=Your choice: 
if /I "%confirm%"=="Y" (
    echo Deleting folder...
    rmdir /S /Q "%folder%"
    echo Folder deleted successfully.
) else (
    echo Aborted. No files were deleted.
)
pause
