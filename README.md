## Squish Integration Suite

This is the GUI integration suite for Cura


### Test Results Gitlab

Latest html testresults of the master branch:

https://ultimaker.gitlab.io/cura/Cura-squish-tests/

Gitlab project:

https://gitlab.com/ultimaker/cura/Cura-squish-tests

### Dependencies

Squish IDE for QT

Cura (Master build, as this contains recently added id's required for several tests) 

### Getting started: testing builds

1. Import this suite into Squish
2. Add Cura to the Application Under Test(AUT) (Test Suite Settings next to the suite name)
3. Set the working directory to custom and browse to "shared\testdata"

### Getting started: testing from source on Linux

1. Make sure you download the correct version of Squish for your version of Qt.
2. Import this suite into Squish.
3. As the Application Under Test (AUT), select your python executable, e.g. `/usr/bin/python3`
4. Under "Arguments", fill in the path to your cura_app.py, e.g. `/home/ruben/Projects/Cura/cura_app.py`
5. Make sure that "Hook into sub-processes launched by the application" is enabled.
6. Under "Environment", add the environment variable `PYTHONPATH` with the Python path that you normally require to run Cura from source.
7. Under "Environment", add the environment variable `LD_LIBRARY_PATH` pointing to the Qt libraries you're using in PyQt, e.g. `/home/ruben/.local/lib/python3.7/site-packages/PyQt5/Qt/lib`
8. Go to Edit -> Preferences and navigate to PyDev -> Interpreters -> Python Interpreter. Add a new interpreter there with the name `System Python` and the location of your Python executable, e.g. `/usr/bin/python3`.


### Scripts

In order for Squish to find the correct scripts, add the following to each new testcase (test.py)

`source(findFile("scripts", "init.py"))`

### External files

It is possible to add extensions to Squish. 
There is one extension available that increases the amount of properties that are recorded for menu's specifically.

In order to add it to your Squish installation, complete the following:
1. Add MenusExt.qml (root of this repo) to [SquishDirectory]\lib\extensions\qt\qtquick\
2. Restart Squish
