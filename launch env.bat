ECHO OFF

REM PATHS DEFINITIONS
SET current_path=%~dp0

REM VIRTUAL ENVIRONNEMENT SETUP
start %current_path%env\Scripts\activate

PAUSE