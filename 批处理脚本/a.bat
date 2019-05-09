@echo off
:start
set /a var+=1
echo %var%
if %var% leq 3 GOTO start
pause