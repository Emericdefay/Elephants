@ECHO OFF
REM VARIABLES DEFINITIONS

REM PATHS DEFINITIONS
SET current_path=%~dp0

REM VIRTUAL ENVIRONNEMENT SETUP
CALL %current_path%env\Scripts\activate

REM GIT
git pull

REM PIP COMPILE
pip-compile requirements.in && pip install -r requirements.txt

REM PIP INSTALL


REM FLAKE8
flake8 project

REM ...

PAUSE