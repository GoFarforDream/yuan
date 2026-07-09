@echo off
set ROOT_DIR=%~dp0..

if not exist "%ROOT_DIR%\backend.pid" (
  echo pid file not found
  exit /b 0
)

set /p PID=<"%ROOT_DIR%\backend.pid"
taskkill /PID %PID% /F >nul 2>&1
del /f /q "%ROOT_DIR%\backend.pid" >nul 2>&1
echo backend stopped
