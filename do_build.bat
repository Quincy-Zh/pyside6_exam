@echo off

pyinstaller -y -w -n pyside6-demo .\main.py

7z a dist\pyside6-demo.7z .\dist\pyside6-demo\* -mx
