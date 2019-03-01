# -*- coding: utf-8 -*-
import platform
from os.path import expanduser
import shutil

class PageObject:
    def __init__(self):
        self.os = platform.system()
        homeDir = expanduser("~")
        self.windowsDir = r'%s\AppData\Roaming\cura\4.0\\' % homeDir
        self.linuxDir = {'local': r'%s/.local/share/cura/4.0' % homeDir,
                         'config': r'%s/.config/cura/4.0' % homeDir}
    
    def startCura(self):
        test.log("Starting Cura")
        self.resetPreferences()
        startApplication("Cura")
    
    def resetPreferences(self):
        if self.os == "Windows":
            shutil.rmtree(self.windowsDir, ignore_errors=True)
#         TODO: add Linux/Mac

    def presetPreferences(self):
        self.resetPreferences()
        if self.os == "Windows":
            shutil.copytree(findFile("testdata", "WindowsConfig/4.0"), r'%s\AppData\Roaming\cura\4.0' % self.homeDir)
#         TODO: add Linux/Mac