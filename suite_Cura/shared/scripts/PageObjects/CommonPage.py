# -*- coding: utf-8 -*-
import platform
from os.path import expanduser
from os.path import getsize
import shutil
import SquishModuleHelper
import squish
import os
from objectmaphelper import Wildcard


class PageObject:
    def __init__(self):
        self.os = platform.system()
        self.home_dir = expanduser("~")
        self.windows_dir = r'%s\AppData\Roaming\cura\4.0\\' % self.home_dir
        self.linux_dir = {'local': r'%s/.local/share/cura/4.0/' % self.home_dir,
                          'config': r'%s/.config/cura/4.0/' % self.home_dir}

        # Imports functions and members of squish
        SquishModuleHelper.importSquishSymbols()

    def startCuraNoConfig(self):
        test.log("Starting Cura with no user preferences")
        self.resetPreferences()
        if self.os == "Windows":
            startApplication("Cura")
        elif self.os == "Linux":
            startApplication("Cura.AppImage")

    def startCuraWithPresetConfig(self):
        test.log("Starting Cura")
        self.presetPreferences()
        if self.os == "Windows":
            startApplication("Cura -platformtheme none")
        elif self.os == "Linux":
            startApplication("Cura.AppImage -platformtheme none")

    def startCura(self):
        startApplication("Cura -platformtheme none")

    def resetPreferences(self):
        if self.os == "Windows":
            shutil.rmtree(self.windows_dir, ignore_errors=True)
        elif self.os == "Linux":
            print("REMOVING SHIIITE")
            shutil.rmtree(self.linux_dir["local"], ignore_errors=True)
            shutil.rmtree(self.linux_dir["config"], ignore_errors=True)

    def presetPreferences(self):
        # Make sure preferences are completely deleted before copying to that dir
        while os.path.isdir(self.windows_dir):
            self.resetPreferences()

        # Set the CWD to the testdata folder
        config_file = findFile("testdata", "WindowsConfig/4.0/cura.cfg")
        testdata_dir = os.path.join(os.getcwd(), findFile("testdata", ""))

        with open(config_file, "r") as file:
            content = file.readlines()

        with open(config_file, "w") as new_file:
            for line in content:
                if ("dialog_load_path" in line) or ("dialog_save_path" in line):
                    continue

                if line == "[local_file]\n":
                    line = line + "dialog_load_path = " + testdata_dir + "\ndialog_save_path = " + testdata_dir + "\n"

                new_file.write(line)

        if self.os == "Windows":
            shutil.copytree(findFile("testdata", "WindowsConfig/4.0"), self.windows_dir)
        elif self.os == "Linux":
            shutil.copytree(findFile("testdata", "WindowsConfig/4.0"), self.linux_dir["local"])
            shutil.copytree(findFile("testdata", "WindowsConfig/4.0"), self.linux_dir["config"])

    def setTextFieldValue(self, obj, value):
        if self.os in ("Windows", "Linux"):
            clear_combination = "<Ctrl+A>"
        elif self.os == "Darwin":
            clear_combination = "<Command+A>"

        self.write(obj, clear_combination)
        self.write(obj, value)

    @staticmethod
    def click(obj, time_out=15000):
        squish.mouseClick(waitForObject(obj, time_out))

    @staticmethod
    def write(obj, val):
        squish.type(waitForObject(obj), val)

    @staticmethod
    def findObjectByText(object, value, property=None):
        if property is None:
            property = 'text'

        obj = object.copy()
        obj[property] = Wildcard("*" + value + "*")
        return waitForObject(obj)

    def fileSize(self, file):
        return self.convertBytes(getsize(file))

    @staticmethod
    def lineCount(fname):
        with open(fname) as f:
            for i, _ in enumerate(f):
                pass
        return i + 1

    @staticmethod
    def convertBytes(size, unit='KB'):
        # Size arrives in bytes
        units = ['KB', 'MB', 'GB']
        index = units.index(unit) + 1
        i = 0
        while i < index:
            i += 1
            size = size / 1024
        if size < 1:
            test.fail("Gcode file smaller than 1 KB")
        return round(size)

    @staticmethod
    def activateMenuItem(menu_object_names):
        count = len(menu_object_names)
        for i, object_name in enumerate(menu_object_names):
            if i < count - 1:
                selectMenuItem(waitForObject(object_name))
            else:
                mouseClickMenuItem(waitForObject(object_name))

    @staticmethod
    def selectMenuItem(obj):
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

    @staticmethod
    def mouseClickMenuItem(obj):
        """mouseClick() on menu items is unreliable, so use native mouse actions"""

        x = 5
        y = 5
        mousePress(obj, x, y, MouseButton.LeftButton)
        mouseRelease(obj, x, y, MouseButton.LeftButton)
