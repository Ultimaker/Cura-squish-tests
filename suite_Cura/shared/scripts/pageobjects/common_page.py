# -*- coding: utf-8 -*-
import platform
from os.path import expanduser
from os.path import getsize
import shutil
import names
import squish_module_helper
import squish
import os

class PageObject:
    def __init__(self):
        self.os = platform.system()
        self.homeDir = expanduser("~")
        self.windowsDir = r'%s\AppData\Roaming\cura\4.0\\' % self.homeDir
        self.linuxDir = {'local': r'%s/.local/share/cura/4.0' % self.homeDir,
                         'config': r'%s/.config/cura/4.0' % self.homeDir}
        
        squish_module_helper.import_squish_symbols()
    
    def startCuraNoConfig(self):
        test.log("Starting Cura with no user preferences")
        self.resetPreferences()
        startApplication("Cura")
    
    def startCura(self):
        test.log("Starting Cura")
        self.presetPreferences()
        startApplication("Cura")

    def resetPreferences(self):
        if self.os == "Windows":
            shutil.rmtree(self.windowsDir, ignore_errors=True)
#         TODO: add Linux/Mac

    def presetPreferences(self):
        self.resetPreferences()
        if self.os == "Windows":
            shutil.copytree(findFile("testdata", "WindowsConfig/4.0"), self.windowsDir)
#         TODO: add Linux/Mac
    #     Set the CWD to the testdata folder
        configFile = findFile("testdata", "WindowsConfig/4.0/cura.cfg")
        testdataDir = os.getcwd() + "\\" + findFile("testdata", "")
    
        with open(configFile, "r") as file:
            content = file.readlines()
            
        with open(configFile, "w") as new_file:
            for line in content:
                if ("dialog_load_path" in line) or ("dialog_save_path" in line):
                    continue
                                
                if line == "[local_file]\n":
                    line = line + "dialog_load_path = "+testdataDir + "\ndialog_save_path = "+testdataDir + "\n"
                    
                new_file.write(line)
                    
    def setTextFieldValue(self, object, value):
        if self.os in ("Windows", "Linux"):
            clearCombination = "<Ctrl+A>"
        elif self.os == "Darwin":
            clearCombination = "<Command+A>"
        
        squish.type(waitForObject(object), clearCombination)
        squish.type(waitForObject(object), value)       

    @staticmethod
    def findObjectByText(object, value, property=None):
        if property is None:
            property = 'text'
            
        obj = object.copy()
        obj[property] = value
        return waitForObject(obj)
    
    def fileSize(self, file):
        return self.convertBytes(getsize(file))
    
    @staticmethod
    def lineCount(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1    
    
    def convertBytes(self, size, unit='KB', precision=2):
        units = ['KB', 'MB', 'GB']
        index = units.index(unit) + 1
        i = 0
        while i < index:
            i += 1
            size = size / float(1024)
        if size < 1:
            test.fail("Gcode file smaller than 1 KB")
        return "%.2f" % size
    
    def activateMenuItem(self, menu_object_names):
        count = len(menu_object_names)
        for i, object_name in enumerate(menu_object_names):
            if i < count - 1:
                selectMenuItem(waitForObject(object_name))
            else:
                mouseClickMenuItem(waitForObject(object_name))
            
    def selectMenuItem(self, obj):
        x = 5
        y = 5
        mouseMove(obj, x, y)
    
        # Minimal movement required to cause selection:
        mouseMove(obj, x + 1, y)
        mouseMove(obj, x, y)
        mouseMove(obj, x + 1, y)
    
        # Delay required else click on the next item may
        # not take place:
        snooze(0.5)
        
    def mouseClickMenuItem(self, obj):
        """mouseClick() on menu items is unreliable, so use native mouse actions"""
    
        x = 5
        y = 5
        mousePress(obj, x, y, MouseButton.LeftButton)
        mouseRelease(obj, x, y, MouseButton.LeftButton)