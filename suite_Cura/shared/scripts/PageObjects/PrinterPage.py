# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
from GetObjectsByProperties import ObjectDescendants
import SquishModuleHelper


class Printer(PageObject):
    def __init__(self):
        SquishModuleHelper.importSquishSymbols()

    def selectedPrinter(self):
        printer_type = waitForObject(names.mwi_sel_printer).text
        return printer_type

    def openPrinterList(self):
        self.click(names.mwi_printer)

    def selectPrinter(self, printer):
        self.openPrinterList()

        waitForObject(names.mwi_printer_list)
        printer_list = ObjectDescendants.getObjects(names.mwi_printer_list, {"type": "MachineSelectorButton"})
        for obj in printer_list:
            if obj.text == printer:
                self.click(obj)
