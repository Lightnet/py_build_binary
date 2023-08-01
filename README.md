# py_build_binary

# License: MIT

# Created By: Lightnet

# Packages:
 * Python 3.11.4
 * NumPy 1.6.2
 * pyinstaller (exe build)
 * CPython (lib build)

# Information:
  This is just sample test build for binary execute file.

  Using the Virtual environment to isolated applicaiton build for sync python 3.11.1 version or package mismatch version conflict.

# Set up for development build and Virtual Environment:

pip3 is for python 3.x to handle package version match version.

```
pip3 install --user pipenv
```
## Create folder current dir:
```
.venv
```
If create .venv folder current project dir else by default C:\Users\<username>\.virtualenvs\<name>

## set current dir:
```
set PIPENV_VENV_IN_PROJECT=1
```
## install package:
```
pipenv install -r requirements.txt
```
Install packages in the text file.

```
pipenv install <package_name>
pipenv install <package_name>==version
```

# Save Packages:
```
pipenv run pip freeze > requirements.txt
```
Save what packages for needed to run application.


# Run shell:
```
pipenv shell
```
  Run sandbox mode.
```
python src/main.py
```
  Run application.
```
exit
```
  Quit shell

# build application lib:
```
python setup.py build_ext --inplace
```

# Build application bin:
```
pyinstaller --onefile --clean src/main.py
```
```
pyinstaller --onefile -w --clean src/main.py
```


# Refs:
 * https://www.youtube.com/watch?v=sFSLY7n3YsM
 * https://www.youtube.com/watch?v=Ab8TOSFfNp4&t=282s Creating a Voxel Engine (like Minecraft) from Scratch in Python 
 * https://github.com/StanislavPetrovV/Minecraft
 * https://docs.python.org/3/library/tkinter.html
 * https://github.com/pygame/pygame
 * https://github.com/theochem/python-cython-ci-example/tree/master
 * https://neurohackweek.github.io/cython-tutorial/02-compiling/
 * https://stackoverflow.com/questions/2581784/can-cython-compile-to-an-exe
 * https://stackoverflow.com/questions/5105482/compile-main-python-program-using-cython
 * https://nbari.com/pipenv-pyinstaller/
