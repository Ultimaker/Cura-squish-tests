# -*- coding: utf-8 -*-
import names

class Printer():
    SELECTED_PRINTER = names.mainWindowSelectedPrinter
    
    def selectedPrinter(self):
        printerType = waitForObject(self.SELECTED_PRINTER).text
        return printerType