# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import names


class Preferences(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        importSquishSymbols()

    def navigateTo(self, menu_item, lang=None):
        menu_object = self.findObjectWithText(names.mnu_item_preferences, menu_item, lang=lang)
        self.click(menu_object)

    def selectPreferencesMenu(self, action):
        button = self.replaceObjectProperty(names.prf_mnu_btn, self.getMenuBtn(action), 'id')
        self.click(button)
        
    def getMenuBtn(self, menu_action):
        switcher = {
            'Add': 'addMenuButton',
            'Activate': 'activateMenuButton',
            'Remove': 'removeMenuButton',
            'Rename': 'renameMenuButton',
            'Create': 'createMenuButton',
            'Duplicate': 'duplicateMenuButton',
            'Import': 'importMenuButton',
            'Export': 'exportMenuButton'
        }

        return switcher.get(menu_action)

    def removePrinter(self):
        self.click(names.rpd_btn_confirm)

    def verifyPrinterDeleted(self, printer):
        obj = self.replaceObjectProperty(names.pps_printer_item, printer)
        return self.verifyObjDeleted(obj)

    def getPrinterListSize(self):
        # This list contains non-printer objects, such as 'Local printers' and 'Network printers'
        # As they are the same object type
        printer_list = len(self.getChildrenOfType(findObject(names.pps_printer_list), "QQuickRectangle"))

        # Check if 'Local/Network printers' exists, if so extract one item from the printer list
        if object.exists(self.getObjByLang(names.pps_local_printers)):
            printer_list -= 1
        if object.exists(self.getObjByLang(names.pps_network_printers)):
            printer_list -= 1

        return printer_list

    def getPrinterFromList(self, printer):
        printer_obj = self.replaceObjectProperty(names.pps_printer_item, printer)
        return waitForObject(printer_obj, 5000)

    def selectPrinter(self, printer_type):
        printer_obj = self.getPrinterFromList(printer_type)
        self.click(printer_obj)

    def selectProfile(self, profile_name):
        profile_obj = self.getProfileFromList(profile_name)
        self.click(profile_obj)
      
    def renamePrinter(self, printer_name):
        self.click(names.input_printer_name)
        self.setTextFieldValue(names.input_printer_name, printer_name)
        self.click(names.btn_rename_confirm)

    def verifyPrinterActivated(self):
        object.exists(names.pps_btn_machine_settings)

    def createProfile(self, profile_name):
        self.click(names.input_profile_name)
        self.setTextFieldValue(names.input_profile_name, profile_name)
        self.click(names.btn_create_profile_confirm)

    def duplicateProfile(self, profile_name):
        self.click(names.input_duplicate_profile_name)
        self.setTextFieldValue(names.input_duplicate_profile_name, profile_name)
        self.click(names.btn_duplicate_profile_confirm)
        
    def getProfileFromList(self, profile):
        profile_obj = self.replaceObjectProperty(names.pfs_profile_item, profile)
        waitForObject(profile_obj, 5000)
        return profile_obj