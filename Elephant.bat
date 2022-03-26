@ECHO OFF
REM VARIABLES DEFINITIONS
SET project_name=project

REM PATHS DEFINITIONS
SET current_path=%~dp0
SET project_folder=%current_path%%project_name%

REM WRITE SHORT DESCRIPTION OF PROGRAM
TYPE %current_path%START.md

REM VIRTUAL ENVIRONNEMENT SETUP
CALL %current_path%env\Scripts\activate

REM LAUNCH LOCAL SERVER
START http://127.0.0.1:8000/

REM LAUNCH DJANGO PROJECT
python %project_folder%\manage.py runserver

PAUSE