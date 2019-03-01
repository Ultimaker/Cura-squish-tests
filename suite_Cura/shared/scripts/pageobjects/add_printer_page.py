# -*- coding: utf-8 -*-
import names
source(findFile("scripts", "get_objects_by_properties.py"))

class AddPrinter():
    DIALOG = names.addPrinterDialog
    BUTTON_ADD = names.addPrinter
    BUTTON_FINISH = names.addPrinterFinish
    SELECTED_PRINTER = names.selectedPrinter
    
    def select(self, printer):
        selected_printer_object = self.SELECTED_PRINTER.copy()
        selected_printer_object["text"] = printer
        
        mouseClick(waitForObject(selected_printer_object))
   
    def add(self):
        mouseClick(waitForObject(self.BUTTON_ADD))
        mouseClick(waitForObject(self.BUTTON_FINISH))