# -*- coding: utf-8 -*-
import platform
import distutils.dir_util
from Helpers.SquishModuleHelper import importSquishSymbols
from Helpers.CuraResources import CuraResources
import squish
import object
import os
import os.path
from objectmaphelper import Wildcard
import time
import names
import gettext
import shutil
# To get the current operating system
import sys
# Needed for the scrolling
import pynput
from pynput.mouse import Controller



class PageObject:
    def __init__(self):
<<<<<<< Updated upstream
        self.cura_version = '4.2'
=======
        self.cura_version = '4.6'
>>>>>>> Stashed changes
        self.cura_resources = CuraResources(self.cura_version)
        self.testdata_dir = os.path.join(os.getcwd(), squish.findFile("testdata", ""))

        # Imports functions and members of Squish
        importSquishSymbols()

    def startCuraNoConfig(self):
        self.resetAllPreferences()
        self.startCura()

    def startCuraWithPresetConfig(self):
        self.presetPreferences()
        self.startCura()

    def startCura(self):
        # Get registered AUT name from conf file
        suite_conf = os.path.join(squishinfo.testCase, "..", "suite.conf")
        aut = None

        with open(suite_conf) as file:
            line = file.readline()
            while line:
                if line.startswith("AUT="):
                    aut = (line.split("AUT=")[1]).rstrip()
                    break
<<<<<<< Updated upstream
        
        startApplication(aut)
        waitForObject(names.mwi, 50000)

=======
        if aut:
            startApplication(aut)
        else:
            attachToApplication("cura_app.py")
            
        waitForObject(names.mwi, 50000)
        if object.exists(names.mwi_changelog):
            self.click(names.mwi_changelog_btn_close)
        if object.exists(names.wel_main):
            self.click(waitForObject(names.onb_btn_next))
            self.click(waitForObject(names.onb_btn_accept_agreement))
            self.click(waitForObject(names.onb_btn_next))
            self.click(waitForObject(names.onb_btn_next))
            self.click(waitForObject(names.pdg_cbo_local_printer))
            self.click(self.findObjectWithText(names.pdg_rbtn_printer, 'Ultimaker 3'))
        
    def startCuraWithArguments(self):
        
        # Get registered AUT name from conf file
        suite_conf = os.path.join(squishinfo.testCase, "..", "suite.conf")
        aut = None

        with open(suite_conf) as file:
            line = file.readline()
            while line:
                if line.startswith("AUT="):
                    aut = (line.split("AUT=")[1]).rstrip()
                    break
        try:
            projFile = "3mf" in aut
            startApplication(aut)
            waitForObject(names.open_project_file_QQuickWindowQmlImpl, 50000)
        except LookupError:
            test.log("No project file given as an argument to Cura")
            
>>>>>>> Stashed changes
    def restartCura(self):
        squish.snooze(12) #Allow autosave to kick in.
        squish.currentApplicationContext().detach()
        self.startCura()
<<<<<<< Updated upstream
=======
        
    def restartCuraWithArguments(self):
        squish.snooze(12) #Allow autosave to kick in.
        squish.currentApplicationContext().detach()
                
        # Get registered AUT name from conf file
        suite_conf = os.path.join(squishinfo.testCase, "..", "suite.conf")
        aut = None

        with open(suite_conf) as file:
            line = file.readline()
            while line:
                if line.startswith("AUT="):
                    aut = (line.split("AUT=")[1]).rstrip()
                    break
        try:
            projFile = "3mf" in aut
            startApplication(aut)
            waitForObject(names.open_Project_QQuickWindowQmlImpl, 50000)
        except LookupError:
            test.log("No project file given as an argument to Cura")
>>>>>>> Stashed changes

    def startCuraConfigVersion(self, config_version):
        self.presetPreferences()
        self.startCura()

    def resetPreferences(self, directory):
        try:
            shutil.rmtree(directory)
        except FileNotFoundError:
            pass #If it's not found, then it was already deleted but that's okay.
        
    def resetAllPreferences(self):
        temp_resources = CuraResources("")
        
        self.resetPreferences(temp_resources.config)
        self.resetPreferences(temp_resources.data)
        self.resetPreferences(temp_resources.cache)

    def presetPreferences(self):
        #Make sure preferences are completely deleted before copying to that dir.
        self.resetPreferences(self.cura_resources.config)
        self.resetPreferences(self.cura_resources.data)
        self.resetPreferences(self.cura_resources.cache)

        #Copy the cfg file to the config directory.
        os.makedirs(self.cura_resources.config, exist_ok = True)
        shutil.copy(squish.findFile("testdata", f"Config/{self.cura_version}/cura.cfg"), self.cura_resources.config)
        shutil.copy(squish.findFile("testdata", f"Config/{self.cura_version}/plugins.json"), self.cura_resources.config)

        #Copy the rest to the data directory (we don't copy any cache files).
        os.makedirs(self.cura_resources.data, exist_ok = True)
        distutils.dir_util.copy_tree(squish.findFile("testdata", f"Config/{self.cura_version}"), self.cura_resources.data)
        os.remove(os.path.join(self.cura_resources.data, "cura.cfg"))
        os.remove(os.path.join(self.cura_resources.data, "plugins.json"))

    def setTextFieldValue(self, obj, value):
        if sys.platform in ("win32", "linux"):
            clear_combination = "<Ctrl+A>"
        elif sys.platform == "darwin":
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
    def click(obj, time_out = 30000, snooze = 100):
        squish.snooze(snooze / 1000)
        squish.mouseClick(waitForObject(obj, time_out))

    # Clears a text field.
    @staticmethod
    def clear(obj):
        item = waitForObject(obj)
        squish.type(item, "<Ctrl+A>")
        squish.type(item, "<Delete>")

    @staticmethod
    def write(obj, val):
        squish.type(waitForObject(obj), val)

    def findObjectWithText(self, object, value, property='text', lang=None, exact_match=False, delay = 0, time_out = 15000):
        squish.snooze(delay / 1000.0)
        if lang is not None:
            value = self.getTranslatedText(value, lang)

        obj = object.copy()
        if exact_match:
            obj[property] = value
        else:
            obj[property] = Wildcard("*" + value + "*")
        return waitForObject(obj, time_out)

    def objectWithTextExists(self, object_template, value, property = "text", lang = None, exact_match = False, pause = 0):
        squish.snooze(pause / 1000.0) #Possibly we need to wait for the interface to update.
        if lang is not None:
            value = self.getTranslatedText(value, lang)

        obj = object_template.copy()
        if exact_match:
            obj[property] = value
        else:
            obj[property] = Wildcard("*" + value + "*")
        return object.exists(obj)

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
        return self.convertBytes(os.path.getsize(file))

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
        # mouseClick() on menu items is unreliable, so use native mouse actions

        x = 5
        y = 5
        mousePress(obj, x, y, MouseButton.LeftButton)
        mouseRelease(obj, x, y, MouseButton.LeftButton)
        
    @staticmethod
    def mouseScrolling(x, y):
        """ 
        Method that implements a scrolling mechanism. The first integer is for 
        horizontal which is left to right scroll; a positive integer will scroll 
        right vice versa. The second integer is for vertical which is up to down 
        scroll; a positive integer will scroll up vice versa
        """
            
        mouse_scroll = Controller()
        mouse_scroll.scroll(x, y)
