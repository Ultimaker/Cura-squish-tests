# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
from GetObjectsByProperties import ObjectDescendants
import SquishModuleHelper


class Printer(PageObject):
    def __init__(self):
        SquishModuleHelper.importSquishSymbols()
        
    def selectedPrinter(self):
        printerType = waitForObject(names.mainWindowSelectedPrinter).text
        return printerType
    
    def openPrinterList(self):
        self.click(names.mainWindowPrinter)
        
    def selectPrinter(self, printer):
        self.openPrinterList()
        
        waitForObject(names.mainWindowPrinterList)
        printerList = ObjectDescendants.getObjects(names.mainWindowPrinterList, {"type": "MachineSelectorButton"})
        for obj in printerList:
            if obj.text == printer:
                self.click(obj)