# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
from GetObjectsByProperties import ObjectDescendants
import SquishModuleHelper


class Preferences(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        SquishModuleHelper.importSquishSymbols()
            
    def navigateTo(self, menuItem):
        menu_object = self.findObjectByText(names.preferencesMenuItem, menuItem)
        self.click(menu_object)
        
    def pressButton(self, action):
        button = self.findObjectByText(names.preferencesMenuButton, action)
        self.click(button)

    def getPrinterList(self, expectedPrinterType):
        waitForObject(names.printerListView)
        printerList = ObjectDescendants.getObjects(names.printerListView, {"text": "%s" % expectedPrinterType})
        return printerList
    
    def selectPrinter(self, printerType):
        printerList = self.getPrinterList(printerType)
        
        if len(printerList) != 0:
            self.click(printerList[0])
        else:
            test.fail("Printer %s not found" % printerType)
            
    def renamePrinter(self, printerName):
        self.click(names.renamePrinter)
        self.setTextFieldValue(names.renamePrinter, printerName)