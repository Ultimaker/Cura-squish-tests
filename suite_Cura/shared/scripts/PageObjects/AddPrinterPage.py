# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
import SquishModuleHelper
import squish


class AddPrinter(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        SquishModuleHelper.importSquishSymbols()

    def select(self, printer):
        printer_object = self.findObjectByText(names.pdg_btn_printer, printer)
        squish.mouseClick(printer_object)

    def add(self):
        self.click(names.pdg_btn_add)

    def finish(self):
        self.click(names.pdg_btn_finish)

    def addNetworkPrinter(self, printer_ip):
        self.click(names.pdg_btn_add_network)
        self.click(names.pdg_input_address)
        self.setTextFieldValue(names.pdg_input_address, printer_ip)
        self.click(names.pdg_address_btn_ok)
        self.click(names.pdg_btn_connect)
