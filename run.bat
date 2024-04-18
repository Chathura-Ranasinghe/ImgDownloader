@echo off

echo Activate virtual environment
call imgDownloader\Scripts\activate

echo Running...
python main.py

rem Pause to keep the command prompt window open (optional)
pause