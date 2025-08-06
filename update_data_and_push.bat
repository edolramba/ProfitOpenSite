@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: 1. 날짜 설정
for /f %%a in ('powershell -command "Get-Date -Format yyyy-MM-dd_HHmmss"') do set NOW=%%a

:: 2. MongoDB에서 export
echo [INFO] Export JSON FROM MongoDB...
mongoexport ^
  --db=automatedTrading ^
  --collection=dj00Trading ^
  --out=C:\Dev\ProfitOpenSite\automatedTrading.dj00Trading.json ^
  --jsonArray ^
  --pretty

:: 3. Git 작업 디렉토리로 이동
cd /d C:\Dev\ProfitOpenSite

:: 4. Git 상태 확인
git add automatedTrading.dj00Trading.json
git diff --cached --quiet

IF ERRORLEVEL 1 (
    git commit -m "Auto Updated: !NOW!"
    git push
    echo [DONE] JSON export & GitHub Push Complete.
) ELSE (
    echo [INFO] No changes detected. Skipping commit and push.
)

pause
