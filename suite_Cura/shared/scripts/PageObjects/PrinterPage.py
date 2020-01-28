# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.GetObjectsByProperties import ObjectDescendants
from Helpers.SquishModuleHelper import importSquishSymbols
import names

import time  # for workaround


class Printer(PageObject):
    def __init__(self):
        importSquishSymbols()

    def selectedPrinter(self):
        return waitForObject(names.mwi_sel_printer).text

    def openPrinterList(self):
        self.click(names.mwi_printer)

    def selectPrinter(self, printer):
        self.openPrinterList()

        printer_list_obj = waitForObject(names.mwi_printer_list)
        printer_list = self.getChildrenOfType(printer_list_obj, "MachineSelectorButton")

        for obj in printer_list:
            if obj.text == printer:
                self.click(obj)
                return
        test.fail(f"Printer {printer} not found")

    def navigateToPrinterPreferences(self):
        self.openPrinterList()
        self.click(names.mwi_btn_manage_printers)
        waitForObject(names.win_pps)

    def getExtruderCount(self):
        extruder_list = ObjectDescendants.getObjects(names.mwi_lst_extruders, {"id": "extruderIcon"})
        return len(extruder_list)

    def syncConfig(self):
        if object.exists(names.btn_to_config):
            self.click(names.btn_to_config)
        elif not object.exists(names.mwi_printer_config_drop):
            self.click(names.mwi_lst_extruders)

            # When the printer is to be set to is a newly added one, it may still be in the process of syncing.
            # However, the extruder-menu won't update when its open, so open and close the menu until synced. 
            check_time = time.time() + 20.0  # <- Don't to wait until the end of time.
            while (time.time() < check_time) and not object.exists(names.btn_to_config):
                snooze(1.0)
                self.click(names.mwi_lst_extruders)
                self.click(names.mwi_lst_extruders)

        self.click(names.btn_printer_sync)

    def isInMonitorPage(self, printer_name):
        self.click(names.mwi_monitor_tab)
        label = self.findObjectWithText(names.lbl_in_monitor, printer_name)
        self.click(names.mwi_prepare_tab)
        return label is not None
    
    def getIntentPrinters(self):
        intents_list = ['Ultimaker S3', 'Ultimaker S5']
        return intents_list
        
    def isIntentPrinter(self, printer):
        printer_list = self.getIntentPrinters(self)
        if printer in printer_list:
            return True
        else:
            return False
        
        
