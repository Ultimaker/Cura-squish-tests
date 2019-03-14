# -*- coding: utf-8 -*-
import names
from pageobjects.common_page import PageObject
import get_objects_by_properties
import squish_module_helper
import squish

class Printer(PageObject):
    selected_printer = names.mainWindowSelectedPrinter
    button_printerlist = names.mainWindowPrinter
    printerlist = names.mainWindowPrinterList
    
    def __init__(self):
        squish_module_helper.import_squish_symbols()
        
    def selectedPrinter(self):
        printerType = waitForObject(self.selected_printer).text
        return printerType
    
    def openPrinterList(self):
        squish.mouseClick(waitForObject(self.button_printerlist))
        
    def selectPrinter(self, printer):
        self.openPrinterList()
        
        printerList = get_objects_by_properties.getObjectsByProperties.get_objects(self.printerlist, {"type": "MachineSelectorButton"})
        for obj in printerList:
            if obj.text == printer:
                squish.mouseClick(obj)