@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: 1. 날짜 설정 (연월일_시분초)
for /f %%a in ('powershell -command "Get-Date -Format yyyyMMdd_HHmmss"') do set NOW=%%a

:: 2. 파일명 설정
set FILENAME=%NOW%_automatedTrading.dj00Trading.json

:: 3. 기존 JSON 파일 제거
echo [INFO] Delete old JSON files...
del /q C:\Dev\ProfitOpenSite\*_automatedTrading.dj00Trading.json

:: 4. MongoDB export
echo [INFO] Export JSON FROM MongoDB...
mongoexport ^
  --db=automatedTrading ^
  --collection=dj00Trading ^
  --out=C:\Dev\ProfitOpenSite\%FILENAME% ^
  --jsonArray

:: 5. Git add/commit/push
cd /d C:\Dev\ProfitOpenSite
git add .
git commit -m "Auto Updated: %NOW%"
git push

echo [DONE] Exported and pushed: %FILENAME%
pause
