# -*- coding: utf-8 -*-
import platform
from os.path import expanduser
import shutil
import names
import squish_module_helper
import squish


class PageObject:
    def __init__(self):
        self.os = platform.system()
        homeDir = expanduser("~")
        self.windowsDir = r'%s\AppData\Roaming\cura\4.0\\' % homeDir
        self.linuxDir = {'local': r'%s/.local/share/cura/4.0' % homeDir,
                         'config': r'%s/.config/cura/4.0' % homeDir}
        squish_module_helper.import_squish_symbols()
    
    def startCuraNoConfig(self):
        test.log("Starting Cura with no user preferences")
        self.resetPreferences()
        startApplication("Cura")
    
    def startCura(self):
        test.log("Starting Cura")
        self.presetPreferences()
        startApplication("Cura")
        squish.mouseClick(waitForObjectExists(names.changelogClose, 50000))
    
    def resetPreferences(self):
        if self.os == "Windows":
            shutil.rmtree(self.windowsDir, ignore_errors=True)
#         TODO: add Linux/Mac

    def presetPreferences(self):
        self.resetPreferences()
        if self.os == "Windows":
            shutil.copytree(findFile("testdata", "WindowsConfig/4.0"), self.windowsDir)
#         TODO: add Linux/Mac

    @staticmethod
    def findObjectByText(object, value, property=None):
        if property is None:
            property = 'text'
            
        obj = object.copy()
        obj[property] = value
        return waitForObject(obj)