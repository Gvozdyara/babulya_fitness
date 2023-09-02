set "app_win_home=%cd%"
robocopy /s .\ *.py \\wsl.localhost\Ubuntu\home\makspeshkov\python_projects\babulya_fitness\src\ /xd venv __pycache__ .git .idea
robocopy /s  .\ *.kv \\wsl.localhost\Ubuntu\home\makspeshkov\python_projects\babulya_fitness\src\ /xd venv __pycache__ .git .idea

pause

copy \\wsl.localhost\Ubuntu\home\makspeshkov\python_projects\babulya_fitness\bin\*.apk .\apk\

adb kill-server
adb start-server
pause
adb install -r apk\babulyafitness-0.1-arm64-v8a_armeabi-v7a-debug.apk
pause
