# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import names


class AddPrinter(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        importSquishSymbols()

    def addNetworkPrinterByIP(self, printer_ip):
        self.click(names.pdg_cbo_network_printer)
        self.click(names.pdg_btn_add_printer_by_ip)
        self.click(names.pdg_input_address)
        self.setTextFieldValue(names.pdg_input_address, printer_ip)
        self.click(names.pdg_btn_add_ip_printer)
        self.click(names.pdg_btn_connect)

    def addNetworkPrinterByName(self, printer_name):
        self.click(names.pdg_cbo_network_printer)
        obj_printer_label = self.findObjectWithText(names.btn_net_printer, printer_name)
        self.click(obj_printer_label)
        obj_add_button = waitForObject(names.btn_add_printer)
        self.click(obj_add_button)

    def addLocalPrinter(self, printer):
        self.click(names.pdg_cbo_local_printer)
        self.setTextFieldValue(names.prs_name_field, printer)
        #self.click(self.findObjectWithText(names.pdg_rbtn_printer, printer))
        self.click(names.pdg_btn_add_printer)

    def addLocalPrinterFromOnb(self, printer):
        self.click(self.replaceOnboardingObjProperty(names.pdg_cbo_local_printer))
        self.click(self.findObjectWithText(self.replaceOnboardingObjProperty(names.pdg_rbtn_printer), printer))
        self.click(self.replaceOnboardingObjProperty(names.pdg_btn_add_printer))

    def replaceOnboardingObjProperty(self, obj):
        return self.replaceObjectProperty(obj, names.mwi, "container")
