# Copyright (c) 2017 Thomas Karl Pietrowski

# Python built-ins
import os
import sys

# Uranium/Cura
from UM.Logger import Logger # @UnresolvedImport

# Using 3rd-party module directory
Logger.log("i", "Python version: {}".format(sys.version_info))
third_party_dir = os.path.join(os.path.split(__file__)[0], "..", "3rd-party")
if os.path.isdir(third_party_dir):
    Logger.log("d", "Found 3rd-party directory and adding in into PYTHONPATH.")
    sys.path.append(third_party_dir)

try:
    Logger.log("i", "Looking for win32com in Cura..")
    import win32com
    del win32com
except:
    Logger.logException("i", ".. Probably couldn't find it. Using our own..")
    
    ## Getting PyWin32 on board
    # os.sys additions
    pyd_dirs = [os.path.join(third_party_dir, "pythonwin"),
                os.path.join(third_party_dir, "win32"),
                os.path.join(third_party_dir, "win32", "lib"),
                os.path.join(third_party_dir, "pywin32_system32"),
                ]
    for pyd_dir in pyd_dirs:
        pyd_dir = os.path.realpath(pyd_dir)
        if os.path.isdir(pyd_dir):
            sys.path.append(pyd_dir)
            print("i", "Added <{}> to sys.path!".format(pyd_dir))
    
    # os.environ['PATH'] additions
    dll_dirs = [os.path.join(third_party_dir, "pywin32_system32"),
                ]
    for dll_dir in dll_dirs:
        dll_dir = os.path.realpath(dll_dir)
        if os.path.isdir(dll_dir):
            os.environ['PATH'] = dll_dir + ';' + os.environ['PATH']
            print("i", "Added <{}> to os.environ['PATH']!".format(dll_dir))

Logger.log("d", "sys.path: {}".format(sys.path))

# Trying to import one of the COM modules
try:
    from .PyWin32Connector import ComConnector
    Logger.log("i", "ComFactory: Using pywin32!")
except ImportError:
    from .ComTypesConnector import ComConnector
    Logger.logException("i", "ComFactory: Using comtypes!")
