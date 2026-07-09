@echo off
set ROOT_DIR=%~dp0..
set PORT=13144

if exist "%ROOT_DIR%\backend.pid" (
  set /p OLD_PID=<"%ROOT_DIR%\backend.pid"
  taskkill /PID %OLD_PID% /F >nul 2>&1
  del /f /q "%ROOT_DIR%\backend.pid" >nul 2>&1
)

start "yuan-backend" /B python -m uvicorn backend.main:app --app-dir "%ROOT_DIR%" --host 0.0.0.0 --port %PORT% > "%ROOT_DIR%\backend.log" 2>&1
echo backend started on port %PORT%
