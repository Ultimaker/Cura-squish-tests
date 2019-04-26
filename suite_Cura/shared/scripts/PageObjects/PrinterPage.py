# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.GetObjectsByProperties import ObjectDescendants
from Helpers.SquishModuleHelper import importSquishSymbols
import names


class Printer(PageObject):
    def __init__(self):
        importSquishSymbols()

    def selectedPrinter(self):
        return waitForObject(names.mwi_sel_printer).text

    def openPrinterList(self):
        self.click(names.mwi_printer)

    def selectPrinter(self, printer):
        self.openPrinterList()

        waitForObject(names.mwi_printer_list)
        printer_list = ObjectDescendants.getObjects(names.mwi_printer_list, {"type": "MachineSelectorButton"})
        for obj in printer_list:
            if obj.text == printer:
                self.click(obj)
