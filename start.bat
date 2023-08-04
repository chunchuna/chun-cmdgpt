@echo off
chcp 65001

echo.
echo  ####  #    #  ####  #    # 
timeout /t 1 /nobreak >nul
echo #    # ##  ## #    # ##   # 
echo #    # # ## # #    # # #  # 
timeout /t 1 /nobreak >nul
echo #    # #    # #    # #  # # 
echo #    # #    # #    # #   ## 
timeout /t 1 /nobreak >nul
echo  ####  #    #  ####  #    # 
echo.

set /p UserInput=cmd-chungpt

python pe.py %UserInput%
pause
