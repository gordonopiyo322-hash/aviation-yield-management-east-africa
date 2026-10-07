@echo off
echo ===INASUKUMWA GITHUB ===
git add .
set /p m="Andika ujumbe wa leo:"
git commit -m "%m%"
git push
echo === IMESUKUMWA ===
pause
