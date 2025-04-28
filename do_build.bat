@echo off

pyinstaller -y .\main.spec

7z a -t7z .\dist\pyside6-demo.7z .\dist\main\*