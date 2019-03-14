# -*- coding: utf-8 -*-
import names
from pageobjects.common_page import PageObject
import get_objects_by_properties
import squish_module_helper
import squish

class Preferences(PageObject):
    menu_item = names.preferencesMenuItem
    button_preferences = names.preferencesMenuButton
    printerlist = names.printerListView

    def __init__(self):
        squish_module_helper.import_squish_symbols()
            
    def navigateTo(self, menuItem):
        menuObject = self.findObjectByText(self.menu_item, menuItem)
        squish.mouseClick(menuObject)
        
    def pressButton(self, action):
        button = self.findObjectByText(self.button_preferences, action)
        squish.mouseClick(button)

    def getPrinterList(self, expectedPrinterType):
        printerList = get_objects_by_properties.getObjectsByProperties.get_objects(self.printerlist, {"text": "%s" % expectedPrinterType})
        return printerList
    