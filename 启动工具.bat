@echo off
title YTM32 引脚配置工具
set "HTML_FILE=%~dp0index.html"
set "FILE_URL=file:///%HTML_FILE:\=/%"
start msedge --app="%FILE_URL%" --window-size=1400,900
exit
