# -*- coding: utf-8 -*-
import names
from pageobjects.page_object import PageObject
from get_objects_by_properties import getObjectsByProperties
import squish_module_helper as squish_module_helper
import squish

class AddPrinter(PageObject):
    squish_module_helper.import_squish_symbols()
    BUTTON_ADD = names.addPrinter
    BUTTON_FINISH = names.addPrinterFinish
    SELECTED_PRINTER = names.selectedPrinter
    
    def select(self, printer):
        printerObject = self.findObjectByText(self.SELECTED_PRINTER, printer)
        squish.mouseClick(printerObject)
   
    def add(self):
        squish.mouseClick(waitForObject(self.BUTTON_ADD))

    def finish(self):
        squish.mouseClick(waitForObject(self.BUTTON_FINISH))