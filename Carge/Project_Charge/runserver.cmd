@echo off
cd /d "%~dp0"
py -3 manage.py runserver 127.0.0.1:8080
