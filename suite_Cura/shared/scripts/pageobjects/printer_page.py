# -*- coding: utf-8 -*-
import names
from pageobjects.page_object import PageObject
import squish_module_helper
import squish

class Printer(PageObject):
    SELECTED_PRINTER = names.mainWindowSelectedPrinter

    def __init__(self):
        squish_module_helper.import_squish_symbols()
        
    def selectedPrinter(self):
        printerType = waitForObject(self.SELECTED_PRINTER).text
        return printerType