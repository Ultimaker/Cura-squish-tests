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

        printer_list_obj = waitForObject(names.mwi_printer_list)
        printer_list = self.getChildrenOfType(printer_list_obj, "MachineSelectorButton")

        for obj in printer_list:
            if obj.text == printer:
                self.click(obj)
                return
        test.fail(f"Printer {printer} not found")

    def navigateToPrinterPreferences(self):
        self.openPrinterList()
        self.click(names.mwi_btn_manage_printers)
        waitForObject(names.win_pps)

    def getExtruderCount(self):
        extruder_list = ObjectDescendants.getObjects(names.mwi_lst_extruders, {"id": "extruderIcon"})
        return len(extruder_list)