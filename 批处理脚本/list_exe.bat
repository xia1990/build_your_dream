@echo off
::查找C盘下的.exe文件并输到file.txt文件中
for /r c:\ %i in (*.exe) do echo %i >> file.txt
pause