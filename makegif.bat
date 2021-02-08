@echo off

set module_path=%~dp0
python %module_path%\makegif.py %*
