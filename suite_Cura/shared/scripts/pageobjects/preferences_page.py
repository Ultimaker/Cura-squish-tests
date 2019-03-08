# -*- coding: utf-8 -*-
import names
from pageobjects.page_object import PageObject
import get_objects_by_properties
import squish_module_helper
import squish

class Preferences(PageObject):
    squish_module_helper.import_squish_symbols()
    MENU_ITEM = names.preferencesMenuItem
    PREFERENCES_BUTTON = names.preferencesMenuButton
    PRINTERLIST = names.printerListView
    
    def navigateTo(self, menuItem):
        menuObject = self.findObjectByText(self.MENU_ITEM, menuItem)
        squish.mouseClick(menuObject)
        
    def pressButton(self, action):
        button = self.findObjectByText(self.PREFERENCES_BUTTON, action)
        squish.mouseClick(button)

    def getPrinterList(self):
        printerList = get_objects_by_properties.getObjectsByProperties.get_objects(self.PRINTERLIST, {"text": "Ultimaker 3", "type": "Text"})
        return printerList