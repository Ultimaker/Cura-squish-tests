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
                
    def retrievePrinterCount(self):
        waitForObject(self.getObjByLang(names.pps_local_printers))

        # TODO: Fix container of pps_printer_list (title of container is in english)

        printer_list = ObjectDescendants.getObjects(names.pps_printer_list, {"type": "MachineSelectorButton"})
        for obj in printer_list:
            print(obj.text)
        return len(printer_list)
    
    def navigateToPrinterPreferences(self):
        self.openPrinterList()
        self.click(self.getObjByLang(names.mwi_btn_manage_printers))