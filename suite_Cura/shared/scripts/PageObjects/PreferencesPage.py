# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
from GetObjectsByProperties import ObjectDescendants
import SquishModuleHelper


class Preferences(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        SquishModuleHelper.importSquishSymbols()

    def navigateTo(self, menu_item):
        menu_object = self.findObjectByText(names.mnu_item_preferences, menu_item)
        self.click(menu_object)

    def pressButton(self, action):
        button = self.findObjectByText(names.pps_mnu_btn, action)
        self.click(button)

    def getPrinterList(self, expected_printer_type):
        waitForObject(names.pps_printer_list)
        printer_list = ObjectDescendants.getObjects(names.pps_printer_list, {"text": f"{expected_printer_type}"})
        return printer_list

    def selectPrinter(self, printer_type):
        printer_list = self.getPrinterList(printer_type)

        if len(printer_list) != 0:
            self.click(printer_list[0])
        else:
            test.fail("Printer %s not found" % printer_type)

    def renamePrinter(self, printer_name):
        self.click(names.input_printer_name)
        self.setTextFieldValue(names.input_printer_name, printer_name)
