@echo off
set theString=%~1
if not defined theString goto:eof
set Return=0
:StringLenth_continue
set /a Return+=1
set thestring=%thestring:~0,-1%
if defined testing goto StringLenth_continue
if not "%2"=="" set %2=%Return%
goto:eof