# -*- coding: utf-8 -*-
import names
import squish_module_helper as squish_module_helper
import squish

class Printer():
    squish_module_helper.import_squish_symbols()
    SELECTED_PRINTER = names.mainWindowSelectedPrinter

    def selectedPrinter(self):
        printerType = waitForObject(self.SELECTED_PRINTER).text
        return printerType