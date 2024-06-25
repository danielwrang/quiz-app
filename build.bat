@echo off

:: Set variables
set source_folder=build/exe.win-amd64-3.9
set zip_file=quiz_app.zip

:: Build executable
python setup.py build

:: Generate user manual
mdpdf -o user_manual.pdf documentation/user_manual.md
del mdpdf.log
move user_manual.pdf "%source_folder%"/readme.pdf
