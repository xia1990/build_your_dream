@echo off
rem 首先建立临时文件 test.txt
echo ;注释行,这是临时文件,用完删除 >test.txt
echo 11 段 12 段 13 段 14 段 15 段 16 段 >>test.txt
echo 21 段,22 段,23 段,24 段,25 段,26 段 >>test.txt
echo 31 段-32 段-33 段-34 段-35 段-36 段 >>test.txt
FOR /F "eol=; tokens=1,3* delims=,- " %%i in (test.txt) do echo %%i %%j %%k
Pause
Del test.txt