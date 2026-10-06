@echo off
echo===INASKUMA GITHUB AUTOMATIC===
cd/d "%~dp0"
set GIT_PATH=%LOCALAPPDATA%\GitHubDesktop\app-*\resources\app\git\cmd\git.exe
for /f "delims=" %%i in (;dir /b/s "%GIT_PATH%" 2^>nul') do set GIT=%%i
if not defined GIT(
   echo Git ya GitHub Desktop haipo, tafadhali tumia njia  2
   pause
   exit
)
"%GIT% add .
set /p ujumbe="Andika ujumbe wa leo (mf:Lesson 03 complete):"
"%GIT%" commit -m "%ujumbe%"
"%GIT%" push
echo.
echo === IMESUKUMWA! ANGALIA GITHUB===
pause