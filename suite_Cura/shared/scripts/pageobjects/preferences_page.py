# -*- coding: utf-8 -*-
import names
from pageobjects.page_object import PageObject
import get_objects_by_properties
import squish_module_helper
import squish

class Preferences(PageObject):
    MENU_ITEM = names.preferencesMenuItem
    PREFERENCES_BUTTON = names.preferencesMenuButton
    PRINTERLIST = names.printerListView

    def __init__(self):
        squish_module_helper.import_squish_symbols()
            
    def navigateTo(self, menuItem):
        menuObject = self.findObjectByText(self.MENU_ITEM, menuItem)
        squish.mouseClick(menuObject)
        
    def pressButton(self, action):
        button = self.findObjectByText(self.PREFERENCES_BUTTON, action)
        squish.mouseClick(button)

    def getPrinterList(self, expectedPrinterType):
        printerList = get_objects_by_properties.getObjectsByProperties.get_objects(self.PRINTERLIST, {"text": "%s" % expectedPrinterType})
        return printerList