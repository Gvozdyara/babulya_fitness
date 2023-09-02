set "app_win_home=%cd%"
robocopy /s .\ *.py \\wsl.localhost\Ubuntu\home\makspeshkov\python_projects\babulya_fitness\src\ /xd venv __pycache__ .git .idea
robocopy /s  .\ *.kv \\wsl.localhost\Ubuntu\home\makspeshkov\python_projects\babulya_fitness\src\ /xd venv __pycache__ .git .idea

robocopy /s  .\ *.png \\wsl.localhost\Ubuntu\home\makspeshkov\python_projects\babulya_fitness\src\ /xd venv __pycache__ .git .idea

pause
del .\apk\ *.apk
copy \\wsl.localhost\Ubuntu\home\makspeshkov\python_projects\babulya_fitness\bin\*.apk .\apk\


adb kill-server
adb start-server
pause
cd apk
for /r %%x in (*) do (adb install -r %%x)
pause
