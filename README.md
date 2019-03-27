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

### Getting started

1. Import this suite into Squish
2. Add Cura to the Application Under Test(AUT) (Test Suite Settings next to the suite name)
3. Set the working directory to custom and browse to "shared\testdata"



### Scripts

In order for Squish to find the correct scripts, add the following to each new testcase (test.py)

`source(findFile("scripts", "init.py"))`

### External files

It is possible to add extensions to Squish. 
There is one extension available that increases the amount of properties that are recorded for menu's specifically.

In order to add it to your Squish installation, complete the following:
1. Add MenusExt.qml (root of this repo) to [SquishDirectory]\lib\extensions\qt\qtquick\
2. Restart Squish