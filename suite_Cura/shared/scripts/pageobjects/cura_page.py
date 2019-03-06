# -*- coding: utf-8 -*-
import names
from pageobjects.page_object import PageObject
import squish_module_helper as squish_module_helper
import squish

class Cura(PageObject):
    squish_module_helper.import_squish_symbols()
    BUTTON_AGREEMENT = names.agreementButton
    MENU_ITEM = names.menuItem
    MAIN_WINDOW = names.mainWindow
    CONFIG_CURA = names.configureCura
    
    def acceptAgreement(self):
        mousePress(waitForObjectExists(Cura.BUTTON_AGREEMENT))
        
    def navigateTo(self, menuItem, subMenuItem, property=None):
        menuObject = PageObject.findObjectByText(Cura.MENU_ITEM, menuItem, "plainText")
        squish.mouseClick(menuObject)
        
        if "Configure Cura" in subMenuItem:
            squish.mouseClick(waitForObject(Cura.CONFIG_CURA))
            
    def curaIsStarted(self):
        waitForObjectExists(Cura.MAIN_WINDOW)