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

set /p UserInput=chunchunGpt测试版

python pe.py %UserInput%
pause
