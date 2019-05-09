@echo off
setlocal enabledelayedexpansion
for /i %%i in (1,1,5) do(
set a=%%icacls
echo !a!
)
pause