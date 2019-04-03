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
        printer_object = self.findObjectByText(names.selectedPrinter, printer)
        squish.mouseClick(printer_object)
    
    def add(self):
        self.click(names.addPrinter)

    def finish(self):
        self.click(names.addPrinterFinish)
        
    def addNetworkPrinter(self, printer_ip):
        self.click(names.addNetworkPrinter)
        self.click(names.printerAddressInputField)
        self.setTextFieldValue(names.printerAddressInputField, printer_ip)
        self.click(names.printerAddressOKButton)
        self.click(names.connectNetworkPrinter)