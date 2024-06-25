import os
from cx_Freeze import setup, Executable

# Additional files to include in the build
additional_files = [
    ('config', 'config'),
    ('questions', 'questions'),
    ('schema', 'schema'),
    ('styles', 'styles')
]

# All locally installed packages get included in the release by default, so exclude them to reduce build size
excludes = ["cryptography", "email", "http", "numpy", "PIL", "pydoc_data", "pytest", "tkinter", "unittest", "xml"]

# Include additional files in the build
build_exe_options = {
    "packages": ["fpdf", "jsonschema", "PyQt6", "source"],  # Include the "source" package
    "include_files": additional_files,
    "excludes": excludes,
}

base = None
if os.name == 'nt':
    base = 'Win32GUI'  # Use this if your application is a GUI app

executables = [
    Executable('main.py', base=base)
]

setup(
    name='MyQtApp',
    version='0.1',
    description='My Qt Application',
    options={"build_exe": build_exe_options},
    executables=executables
)
