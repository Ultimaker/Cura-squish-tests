# -*- coding: utf-8 -*-
import names
from pageobjects.common_page import PageObject
import squish_module_helper
import squish

class AddPrinter(PageObject):
    button_add = names.addPrinter
    button_finish = names.addPrinterFinish
    selected_printer = names.selectedPrinter
    add_networkprinter = names.addNetworkPrinter
    networkprinter_inputfield = names.printerAddressInputField
    networkprinter_ok = names.printerAddressOKButton
    connect_networkprinter = names.connectNetworkPrinter

    def __init__(self):
        PageObject.__init__(self)
        squish_module_helper.import_squish_symbols()
            
    def select(self, printer):
        printerObject = self.findObjectByText(self.selected_printer, printer)
        squish.mouseClick(printerObject)
   
    def add(self):
        squish.mouseClick(waitForObject(self.button_add))

    def finish(self):
        squish.mouseClick(waitForObject(self.button_finish))
        
    def addNetworkPrinter(self, printerIP):
        squish.mouseClick(waitForObject(self.add_networkprinter))
        squish.mouseClick(waitForObject(self.networkprinter_inputfield))
        self.setTextFieldValue(self.networkprinter_inputfield, printerIP)
        squish.mouseClick(waitForObject(self.networkprinter_ok))
        squish.mouseClick(waitForObject(self.connect_networkprinter))