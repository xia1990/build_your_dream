@echo off
set /p input=请输入计算表达式：
set /a var=%input%
echo 计算结果:%input%=%var%
pause