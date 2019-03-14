# -*- coding: utf-8 -*-
import names
from pageobjects.common_page import PageObject
import squish_module_helper
import squish

class AddPrinter(PageObject):
    button_add = names.addPrinter
    button_finish = names.addPrinterFinish
    selected_printer = names.selectedPrinter

    def __init__(self):
        squish_module_helper.import_squish_symbols()
            
    def select(self, printer):
        printerObject = self.findObjectByText(self.selected_printer, printer)
        squish.mouseClick(printerObject)
   
    def add(self):
        squish.mouseClick(waitForObject(self.button_add))

    def finish(self):
        squish.mouseClick(waitForObject(self.button_finish))