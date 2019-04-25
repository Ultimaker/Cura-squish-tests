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

    def selectPrinterMenu(self, action):
        button = self.findObjectByText(names.pps_mnu_btn, action)
        self.click(button)

    def removePrinter(self):
        self.click(names.rpd_btn_confirm)

    def verifyPrinterDeleted(self, printer):
        obj = self.replaceObjectTextProperty(names.pps_printer_item, printer)
        return self.verifyObjDeleted(obj)

    def getPrinterList(self, expected_printer_type):
        waitForObject(names.pps_local_printers)
        printer_list = ObjectDescendants.getObjects(names.pps_printer_list, {"text": f"{expected_printer_type}"})
        return printer_list

    def selectPrinter(self, printer_type):
        printer_list = self.getPrinterList(printer_type)

        if len(printer_list) != 0:
            self.click(printer_list[0])
        else:
            test.fail("Printer %s not found" % printer_type)

    def renamePrinter(self, printer_name):
        self.selectPrinterMenu("Rename")
        self.click(names.input_printer_name)
        self.setTextFieldValue(names.input_printer_name, printer_name)
        self.click(names.btn_rename_confirm)

    def verifyPrinterActivated(self):
        object.exists(names.pps_btn_machine_settings)
