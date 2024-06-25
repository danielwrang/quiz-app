# Python Qt Windows Desktop Quiz Application
The project creates a Quiz application with `Python3` and `Qt6` for the graphical user interface.
To compile the program into a Windows executable, the package `cx_Freeze` is used.
The quiz questions are stored in JSON files.

## Releases
Instead of building from source, Windows releases are available on the release page:
https://github.com/danielwrang/quiz-app/releases.

## Contents
* `config` - JSON file for configuration of the app.
* `documentation` - The raw version of the user manual, gets converted into PDF during release build.
* `questions` - JSON files with the quiz questions.
* `schema` - JSON file(s) with the validation schema for the questions.
* `source` - Python files with source code implementation.
* `styles` - QSS file(s) specifying the style for the application.
* `build.bat` - Script to build a release bundle.
* `main.py` - Entrypoint for the application.
* `readme.md` - This readme file.
* `requirements.txt` - Packages for the Python development environment.
* `setup.py` - Build script to compile the source code into an executable.

## Installation
Install Python3 on the system, developed with version 3.9.13.

### Python packages
Install the packages listed below, also listed in `requirements.txt`
* `pip install cx_Freeze`
* `pip install fpdf2`
* `pip install jsonschema`
* `pip install mdpdf`
* `pip install PyQt6`

or just do
* `pip install -Ur requirements.txt`

## Development
To run the application during development, run the main program `main.py`.

## Build
To create a release, including a Windows executable (.exe) of the program and a PDF of the user manual, run the build
script `build.bat`. The output is stored in a folder `build`.

## Contact
For issues and improvements, please contact Daniel Wrang, daniel.wrang@gmail.com.
