@echo off
for /r c:\ %i in （*.exe） do echo %icacls
pause