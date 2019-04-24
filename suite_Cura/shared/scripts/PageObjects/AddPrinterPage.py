# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
import SquishModuleHelper
import squish


class AddPrinter(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        SquishModuleHelper.importSquishSymbols()

    def addNetworkPrinter(self, printer_ip):
        self.click(names.pdg_cbo_network_printer)
        self.click(names.pdg_btn_add_printer_by_ip)
        self.click(names.pdg_input_address)
        self.setTextFieldValue(names.pdg_input_address, printer_ip)
        self.click(names.pdg_btn_add_ip_printer)
        self.click(names.pdg_btn_connect)

    def addLocalPrinter(self, printer):
        self.click(names.pdg_cbo_local_printer)
        self.click(self.findObjectByText(names.pdg_rbtn_printer, printer))
        self.click(names.pdg_btn_add_printer)
