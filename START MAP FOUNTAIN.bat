@echo off
cd /d "%~dp0"
title Rasta USB Map Fountain
where py >nul 2>nul
if %errorlevel%==0 (
    start "" pyw -3 Map_Fountain_GUI.py
) else (
    start "" pythonw Map_Fountain_GUI.py
)
