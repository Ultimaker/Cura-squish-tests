# -*- coding: utf-8 -*-
import platform
from os.path import expanduser
from os.path import getsize
from Helpers.SquishModuleHelper import importSquishSymbols
import squish
import os
from objectmaphelper import Wildcard
import time
import names
import gettext
from pathlib import Path
from shutil import rmtree, copytree, copy, ignore_patterns


class PageObject:
    def __init__(self):
        self.os = platform.system()
        self.home_dir = expanduser("~")
        self.cura_version = '4.1'

        self.windows_dir = r'%s\AppData\Roaming\cura' % self.home_dir
        self.testdata_dir = os.path.join(os.getcwd(), squish.findFile("testdata", ""))

        self.linux_dir = {'local': Path('%s/.local/share/cura' % self.home_dir),
                          'config': Path('%s/.config/cura' % self.home_dir)}

        # Imports functions and members of squish
        importSquishSymbols()

    def startCuraNoConfig(self):
        self.resetPreferences()
        self.startCura()

    def startCuraWithPresetConfig(self):
        self.presetPreferences()
        self.startCura()

    def startCura(self):
        # Get registred AUT name from conf file
        suite_conf = Path(squishinfo.testCase) / "../suite.conf"
        aut = None
        
        with open(suite_conf) as file:
            line = file.readline()
            while line:
                if line.startswith("AUT="):
                    aut = (line.split("AUT=")[1]).rstrip()
                    break
        
        startApplication(aut)
        waitForObject(names.mwi, 50000)

    def startCuraConfigVersion(self, config_version):
        self.presetPreferences(config_version)
        self.startCura()

    def resetPreferences(self, directory):
        self.deleteContentFromDir(directory)

    @staticmethod
    def deleteContentFromDir(location):
        for data in os.listdir(location):
            file_path = os.path.join(location, data)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    rmtree(file_path)
            except Exception as e:
                print(e)

    # TODO: Expand this function for mac
    def presetPreferences(self, version=None):
        if version is not None:
            self.cura_version = version

            # Make sure preferences are completely deleted before copying to that dir
            # Linux config folder only contains .cfg and .log
        if self.os == "Linux":
            for key, value in self.linux_dir.items():
                try:
                    while os.listdir(value):
                        self.resetPreferences(value)
                except FileNotFoundError:
                    os.mkdir(value)
                           
                destination_dir = Path(value / self.cura_version)
                
                if key == "config":
                    os.makedirs(destination_dir, exist_ok=True)
                    copy(findFile("testdata", f"Config/{self.cura_version}/cura.cfg"), destination_dir)
                    continue
                if key == "local":
                    copytree(findFile("testdata", f"Config/{self.cura_version}"), destination_dir, ignore=ignore_patterns('cura.cfg'))
                    continue
               
        else:
            try:
                while os.listdir(self.windows_dir):
                    self.resetPreferences(self.windows_dir)
            except FileNotFoundError:
                os.mkdir(self.windows_dir)    
            
            copytree(findFile("testdata", f"Config/{self.cura_version}"), Path(self.windows_dir, self.cura_version))

    def setTextFieldValue(self, obj, value):
        if self.os in ("Windows", "Linux"):
            clear_combination = "<Ctrl+A>"
        elif self.os == "Darwin":
            clear_combination = "<Command+A>"

        self.write(obj, clear_combination)
        self.write(obj, value)

    def verifyObjDeleted(self, obj, wait_time=5):
        testSettings.objectNotFoundDebugging = False
        start_time = time.time()
        end_time = 0.0
        try:
            while end_time - start_time <= wait_time:
                waitForObject(obj, 0)
                end_time = time.time()
                snooze(1)

            # Object still found after n seconds
            testSettings.objectNotFoundDebugging = True
            return False
        except LookupError:
            testSettings.objectNotFoundDebugging = True
            return True

    # This method looks for children by type recursively
    # Object.children(n) requires a real name (dict) and cannot be used with type 'Object'
    def getChildrenOfType(self, parent_obj, typename, child_obj_list=None):
        if child_obj_list is None:
            child_obj_list = []

        [child_obj_list.append(x) for x in object.children(parent_obj) if typename in className(x)]

        for x in object.children(parent_obj):
            child_obj_list = self.getChildrenOfType(x, typename, child_obj_list)

        return child_obj_list

    @staticmethod
    def click(obj, time_out=15000):
        squish.mouseClick(waitForObject(obj, time_out))

    @staticmethod
    def write(obj, val):
        squish.type(waitForObject(obj), val)

    def findObjectWithText(self, object, value, property='text', lang=None, exact_match=False):
        if lang is not None:
            value = self.getTranslatedText(value, lang)

        obj = object.copy()
        if exact_match:
            obj[property] = value
        else:
            obj[property] = Wildcard("*" + value + "*")
        return waitForObject(obj)

    @staticmethod
    def getTranslatedText(text, lang='nl'):
        t = gettext.translation('cura', findFile("scripts", "locale"), languages=[lang])
        return t.gettext(text)

    @staticmethod
    def replaceObjectProperty(object, value, property='text'):
        obj = object.copy()
        obj[property] = value
        return obj

    def getObjByLang(self, obj, lang='nl'):
        new_val = self.getTranslatedText(obj['text'], lang)
        return self.replaceObjectProperty(obj, new_val)

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

    def getGrandParentObj(self, obj):
        parent = object.parent(waitForObject(obj))
        return object.parent(waitForObject(parent))

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
