@echo off
chcp 65001 > nul
pushd "%~dp0"
git push origin master
echo.
echo Done
pause > nul
