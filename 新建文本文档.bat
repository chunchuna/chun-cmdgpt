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
set /p UserInput=请在py文件中填写自己的API API的Base是国内的https://api.closeai-asia.com 
python pe.py %UserInput%
pause
